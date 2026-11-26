#!/usr/bin/env python3
"""Clay episode audio + timing.
usage: clay_audio.py WORKDIR            (WORKDIR holds script.py with VOICES and LINES, see CLAY_FORMAT.md)
Writes WORKDIR/vo/lNN.mp3|wav, cues/lNN.json (host lines, Rhubarb), anim.json, vo_full.wav, mix_final.wav, sfx_events.json, caps_filter.txt, cap/cNN.txt.
Reuses existing vo/lNN.mp3 (no ElevenLabs spend). Needs env ELEVENLABS_API_KEY only for missing lines. Needs rhubarb on PATH or $RHUBARB."""
import sys, os, json, math, textwrap, subprocess, urllib.request, shutil, numpy as np, soundfile as sf
W = os.path.abspath(sys.argv[1]); os.chdir(W)
HERE = os.path.dirname(os.path.abspath(__file__)); ENG = os.path.dirname(HERE)
ns = {}; exec(open('script.py').read(), ns); VOICES, LINES = ns['VOICES'], ns['LINES']
FPS = 15; START = 0.7; GAP = 0.26
for d in ('vo', 'cues', 'cap'): os.makedirs(d, exist_ok=True)
def sh(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))
used = 0
for i, (who, hi, rom) in enumerate(LINES):
    mp3 = f'vo/l{i:02d}.mp3'
    if not os.path.exists(mp3):
        key = os.environ.get('ELEVENLABS_API_KEY')
        if not key: sys.exit('no ELEVENLABS_API_KEY and no vo/l%02d.mp3' % i)
        body = json.dumps({'text': hi, 'model_id': 'eleven_flash_v2_5', 'language_code': 'hi',
                           'voice_settings': {'stability': .45, 'similarity_boost': .8, 'style': .2, 'use_speaker_boost': True}}).encode()
        rq = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICES[who]}', body,
                                    {'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
        open(mp3, 'wb').write(urllib.request.urlopen(rq, timeout=120).read()); used += len(hi)
    sh('ffmpeg', '-y', '-i', mp3, '-ar', '44100', '-ac', '1', f'vo/l{i:02d}.wav')
json.dump({'eleven_chars_used': used}, open('eleven_usage.json', 'w'))
segs = []; t = START
for i, (who, hi, rom) in enumerate(LINES):
    if i == len(LINES) - 1: t += 0.8  # beat before the twist
    d = round(dur(f'vo/l{i:02d}.wav'), 3); segs.append({'i': i, 'who': who, 'start': round(t, 3), 'dur': d, 'cap': rom}); t += d + GAP
total = float(math.ceil(segs[-1]['start'] + segs[-1]['dur'] + 1.5)); frames = int(total * FPS) + 1
RH = os.environ.get('RHUBARB') or shutil.which('rhubarb') or sys.exit('rhubarb not found: see SKILL.md setup')
mouth = ['X'] * frames; env = [0.0] * frames
for s in segs:
    f0 = int(round(s['start'] * FPS))
    if s['who'] == 'h':
        sh(RH, '--recognizer', 'phonetic', '-f', 'json', '-o', f"cues/l{s['i']:02d}.json", f"vo/l{s['i']:02d}.wav")
        cues = json.load(open(f"cues/l{s['i']:02d}.json"))['mouthCues']
        for f in range(f0, min(frames, int(round((s['start'] + s['dur']) * FPS)) + 1)):
            tt = f / FPS - s['start']
            for c in cues:
                if c['start'] <= tt < c['end']: mouth[f] = c['value']; break
    else:
        x, sr = sf.read(f"vo/l{s['i']:02d}.wav"); hop = sr // FPS
        r = [float(np.sqrt(np.mean(x[k:k + hop] ** 2))) for k in range(0, len(x), hop)]
        m = max(r) or 1
        for k, v in enumerate(r):
            if f0 + k < frames: env[f0 + k] = round(min(1.0, v / m * 1.2), 3)
json.dump({'fps': FPS, 'total': total, 'frames': frames, 'segs': segs, 'mouth': mouth, 'env': env}, open('anim.json', 'w'))
# voice track
sr = 44100; vo = np.zeros(int((total + 1) * sr))
for s in segs:
    x, _ = sf.read(f"vo/l{s['i']:02d}.wav"); a = int(s['start'] * sr); vo[a:a + len(x)] += x
sf.write('vo_raw_full.wav', vo, sr)
sh('ffmpeg', '-y', '-i', 'vo_raw_full.wav', '-af', 'highpass=f=80,lowpass=f=11000,acompressor=threshold=-20dB:ratio=3,loudnorm=I=-16:TP=-1.5', 'vo_full.wav')
# sfx: pop at start, whoosh+ding on each cut to a new speaker after the third line, zip/subdrop/thud on the ending
ev = [('pop', 0.12)]
for s in segs[3:-1]:
    if s['who'] == 'h' and s['i'] % 4 == 0: ev += [('whoosh', s['start'] - 0.2), ('ding', s['start'] + 0.2)]
ev += [('subdrop', segs[-1]['start'] + segs[-1]['dur'] - 0.85), ('thud', segs[-1]['start'] + segs[-1]['dur'] + 0.15)]
json.dump(ev, open('sfx_events.json', 'w'))
sys.path.insert(0, ENG); import sfx_lib as L
SR2 = L.SR; sfx = np.zeros(int((total + 1) * SR2))
for n, tt in ev:
    fn = {'pop': L.pop, 'whoosh': L.whoosh, 'ding': L.ding, 'subdrop': L.sub_drop, 'thud': L.impact}[n]
    y, anchor, _k = fn(); y = np.asarray(y); y = y[:, 0] if y.ndim > 1 else y; a = int(max(0, tt - anchor) * SR2); sfx[a:a + len(y)] += y[:len(sfx) - a] * 0.35
sf.write('sfx.wav', sfx, SR2)
sh('python3', os.path.join(ENG, 'lofi.py'), 'bed.wav', str(total), '84', '7', 'warm')
sh('ffmpeg', '-y', '-i', 'vo_full.wav', '-i', 'bed.wav', '-i', 'sfx.wav', '-filter_complex',
   '[1:a]volume=0.22[b];[2:a]volume=0.8[x];[0:a][b][x]amix=inputs=3:normalize=0,loudnorm=I=-16:TP=-1.5', '-t', str(total), '-ar', '48000', 'mix_final.wav')
# captions
parts = []
for s in segs:
    open(f"cap/c{s['i']:02d}.txt", 'w').write('\n'.join(textwrap.wrap(s['cap'], 26)))
    col = 'white' if s['who'] == 'h' else '0x5DE0B0'
    parts.append(f"drawtext=fontfile=/usr/share/fonts/opentype/inter/Inter-Bold.otf:textfile=cap/c{s['i']:02d}.txt:fontsize=68:fontcolor={col}:borderw=7:bordercolor=black@0.85:shadowx=0:shadowy=4:shadowcolor=black@0.5:line_spacing=10:x=(w-text_w)/2:y=1400-text_h/2:enable='between(t,{s['start']:.3f},{s['start']+s['dur']+0.1:.3f})'")
open('caps_filter.txt', 'w').write(','.join(parts))
print('ok', total, 'frames', frames, 'segs', len(segs), 'eleven chars', used)
