"""Make voiceover + timeline.  usage: python3 voice.py WORKDIR [voice=pratham] [tempo=1.18]
WORKDIR/script.py must define LINES = [(scene, devanagari_tts_text, roman_caption[, speaker]), ...]
Optional VOICES={'c':('pratham',1.24),'b':('rohan',1.14)} in script.py maps speaker -> (voice, tempo[, pitch]) for two-character chats.
ElevenLabs: voice 'eleven:<voice_id>[@model]' (default model eleven_flash_v2_5 = 0.5 credit/char). Needs env ELEVENLABS_API_KEY
(never in the repo). Every line is cached in ~/.cache/tb_eleven by (voice, model, text) so re-renders cost nothing; a reel over
ELEVEN_MAX_CHARS (default 900) or any API error falls back to the 4th tuple item, else Kokoro hm_omega. Usage is logged to
WORKDIR/eleven_usage.json."""
import sys, json, subprocess, os
GAP_SC=float(os.environ.get('GAP_SC',0.38)); GAP_LN=float(os.environ.get('GAP_LN',0.14))
W=sys.argv[1]; voice=sys.argv[2] if len(sys.argv)>2 else 'pratham'; tempo=float(sys.argv[3]) if len(sys.argv)>3 else 1.18
sys.path.insert(0,W); import script; LINES=script.LINES; VOICES=getattr(script,'VOICES',{})
os.makedirs(f'{W}/vo',exist_ok=True)
here=os.path.dirname(os.path.abspath(__file__)); out=[]; t=0.12; prev=None
for i,L in enumerate(LINES):
    sc,tt,cap=L[:3]; spk=L[3] if len(L)>3 else ''; vt=VOICES.get(spk,(voice,tempo)); v,tp=vt[0],vt[1]; pf=vt[2] if len(vt)>2 else 1.0; src=v.split(':')[0]
    if v.startswith('file:'):   # pre-made voice file (e.g. Voicebox clone): 'file:vo_in/b_{i:02d}.wav', 4th item = fallback voice tuple
        fp=os.path.join(W,v[5:].format(i=i))
        if not os.path.exists(fp) and len(vt)>3: fb=vt[3]; v,tp=fb[0],fb[1]; pf=fb[2] if len(fb)>2 else 1.0; src='standin:'+v.split(':')[-1]
    m=f'/tmp/tts/vits-piper-hi_IN-{v}-medium/hi_IN-{v}-medium.onnx'
    raw=f'{W}/vo/r{i:02d}.wav'; fin=f'{W}/vo/f{i:02d}.wav'
    if v.startswith('eleven:'):
        _ok=False
        try:
            import hashlib, urllib.request
            _vid,_,_mdl=v.split(':',1)[1].partition('@'); _mdl=_mdl or 'eleven_flash_v2_5'
            _ck=os.path.expanduser('~/.cache/tb_eleven'); os.makedirs(_ck,exist_ok=True)
            _h=hashlib.sha1(f'{_vid}|{_mdl}|{tt}'.encode()).hexdigest()[:16]; _mp3=f'{_ck}/{_h}.mp3'
            _tot=sum(len(x[1]) for x,(xs) in zip(LINES,[VOICES.get(x[3] if len(x)>3 else '',(voice,tempo)) for x in LINES]) if xs[0].startswith('eleven:'))
            if not os.path.exists(_mp3):
                _key=os.environ.get('ELEVENLABS_API_KEY','')
                if not _key: raise RuntimeError('no ELEVENLABS_API_KEY')
                if _tot>int(os.environ.get('ELEVEN_MAX_CHARS','900')): raise RuntimeError(f'reel uses {_tot} chars > ELEVEN_MAX_CHARS')
                _body=json.dumps(dict(text=tt,model_id=_mdl,voice_settings=dict(stability=.45,similarity_boost=.8,style=.2,use_speaker_boost=True))).encode()
                _rq=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{_vid}?output_format=mp3_44100_128',data=_body,headers={'xi-api-key':_key,'Content-Type':'application/json','Accept':'audio/mpeg'})
                open(_mp3,'wb').write(urllib.request.urlopen(_rq,timeout=60).read())
                _u=f'{W}/eleven_usage.json'; _us=json.load(open(_u)) if os.path.exists(_u) else {'chars':0,'lines':0,'model':_mdl}
                _us['chars']+=len(tt); _us['lines']+=1; json.dump(_us,open(_u,'w'))
            subprocess.run(['ffmpeg','-v','error','-y','-i',_mp3,'-ar','44100','-ac','1',raw],check=True); SR=44100; _ok=True; src='eleven:'+_vid
        except Exception as _e:
            print('ElevenLabs fallback:',_e)
        if not _ok:
            fb=vt[3] if len(vt)>3 else ('kokoro:hm_omega',1.12,0.96); v,tp=fb[0],fb[1]; pf=fb[2] if len(fb)>2 else 1.0; src='standin:'+v
            if v.startswith('kokoro:'):
                if 'KK' not in globals():
                    from kokoro_onnx import Kokoro; KK=Kokoro('/tmp/tts/kx/kokoro-v1.0.onnx','/tmp/tts/kx/voices-v1.0.bin')
                import soundfile as _sf; _vn,_,_lg=v.split(':')[1].partition('@'); smp,sr=KK.create(tt,voice=_vn,speed=1.0,lang=_lg or {'a':'en-us','b':'en-gb'}.get(_vn[0],'hi')); _sf.write(raw,smp,sr); SR=sr
    elif v.startswith('file:'):
        import soundfile as _sf0; _x,SR=_sf0.read(fp); _sf0.write(raw,_x,SR)
    elif v.startswith('kokoro:'):
        if 'KK' not in globals():
            from kokoro_onnx import Kokoro; KK=Kokoro('/tmp/tts/kx/kokoro-v1.0.onnx','/tmp/tts/kx/voices-v1.0.bin')
        import soundfile as _sf; _vn,_,_lg=v.split(':')[1].partition('@'); smp,sr=KK.create(tt,voice=_vn,speed=1.0,lang=_lg or {'a':'en-us','b':'en-gb'}.get(_vn[0],'hi')); _sf.write(raw,smp,sr); SR=sr
    else:
        subprocess.run(['python3',f'{here}/tts_piper.py',m,tt,raw,'0.84'],check=True,capture_output=True); SR=22050
    subprocess.run(['ffmpeg','-v','error','-y','-i',raw,'-af',f'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,asetrate={int(SR*pf)},aresample={SR},atempo={tp/pf:.4f},aresample=48000','-ac','2',fin],check=True)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',fin]))
    if prev is not None: t+=GAP_SC if prev!=sc else GAP_LN
    import numpy as _np, soundfile as _sf2
    _a,_r=_sf2.read(fin); _a=_a.mean(1) if _a.ndim>1 else _a; hop=_r//30
    rms=_np.array([_np.sqrt(_np.mean(_a[k:k+hop]**2)) for k in range(0,len(_a),hop)]); rms=_np.clip(rms/(_np.percentile(rms,95)+1e-6),0,1)
    env=''.join(str(int(x*9)) for x in rms)
    out.append(dict(i=i,scene=sc,cap=cap,spk=spk,src=src,file=fin,dur=d,start=round(t,3),env=env,cam=(L[4] if len(L)>4 else ''))); t+=d; prev=sc
json.dump(dict(lines=out,total=t+1.3),open(f'{W}/timeline.json','w'),indent=1)
for x in out: print(x['i'],x['scene'],x['start'],round(x['dur'],2))
print('TOTAL',round(t+1.3,2))
