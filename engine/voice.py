"""Make voiceover + timeline.  usage: python3 voice.py WORKDIR [voice=pratham] [tempo=1.18]
WORKDIR/script.py must define LINES = [(scene, devanagari_tts_text, roman_caption[, speaker]), ...]
Optional VOICES={'c':('pratham',1.24),'b':('rohan',1.14)} in script.py maps speaker -> (voice, tempo[, pitch]) for two-character chats."""
import sys, json, subprocess, os
GAP_SC=float(os.environ.get('GAP_SC',0.38)); GAP_LN=float(os.environ.get('GAP_LN',0.14))
W=sys.argv[1]; voice=sys.argv[2] if len(sys.argv)>2 else 'pratham'; tempo=float(sys.argv[3]) if len(sys.argv)>3 else 1.18
sys.path.insert(0,W); import script; LINES=script.LINES; VOICES=getattr(script,'VOICES',{})
os.makedirs(f'{W}/vo',exist_ok=True)
here=os.path.dirname(os.path.abspath(__file__)); out=[]; t=0.12; prev=None
for i,L in enumerate(LINES):
    sc,tt,cap=L[:3]; spk=L[3] if len(L)>3 else ''; vt=VOICES.get(spk,(voice,tempo)); v,tp=vt[0],vt[1]; pf=vt[2] if len(vt)>2 else 1.0
    m=f'/tmp/tts/vits-piper-hi_IN-{v}-medium/hi_IN-{v}-medium.onnx'
    raw=f'{W}/vo/r{i:02d}.wav'; fin=f'{W}/vo/f{i:02d}.wav'
    if v.startswith('kokoro:'):
        global KK
        if 'KK' not in globals():
            from kokoro_onnx import Kokoro; KK=Kokoro('/tmp/tts/kx/kokoro-v1.0.onnx','/tmp/tts/kx/voices-v1.0.bin')
        import soundfile as _sf; smp,sr=KK.create(tt,voice=v.split(':')[1],speed=1.0,lang='hi'); _sf.write(raw,smp,sr); SR=sr
    else:
        subprocess.run(['python3',f'{here}/tts_piper.py',m,tt,raw,'0.84'],check=True,capture_output=True); SR=22050
    subprocess.run(['ffmpeg','-v','error','-y','-i',raw,'-af',f'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,asetrate={int(SR*pf)},aresample={SR},atempo={tp/pf:.4f},aresample=48000','-ac','2',fin],check=True)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',fin]))
    if prev is not None: t+=GAP_SC if prev!=sc else GAP_LN
    import numpy as _np, soundfile as _sf2
    _a,_r=_sf2.read(fin); _a=_a.mean(1) if _a.ndim>1 else _a; hop=_r//30
    rms=_np.array([_np.sqrt(_np.mean(_a[k:k+hop]**2)) for k in range(0,len(_a),hop)]); rms=_np.clip(rms/(_np.percentile(rms,95)+1e-6),0,1)
    env=''.join(str(int(x*9)) for x in rms)
    out.append(dict(i=i,scene=sc,cap=cap,spk=spk,file=fin,dur=d,start=round(t,3),env=env,cam=(L[4] if len(L)>4 else ''))); t+=d; prev=sc
json.dump(dict(lines=out,total=t+1.3),open(f'{W}/timeline.json','w'),indent=1)
for x in out: print(x['i'],x['scene'],x['start'],round(x['dur'],2))
print('TOTAL',round(t+1.3,2))
