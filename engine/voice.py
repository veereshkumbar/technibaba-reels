"""Make voiceover + timeline.  usage: python3 voice.py WORKDIR [voice=pratham] [tempo=1.18]
WORKDIR/script.py must define LINES = [(scene, devanagari_tts_text, roman_caption), ...]"""
import sys, json, subprocess, os
GAP_SC=float(os.environ.get('GAP_SC',0.38)); GAP_LN=float(os.environ.get('GAP_LN',0.14))
W=sys.argv[1]; voice=sys.argv[2] if len(sys.argv)>2 else 'pratham'; tempo=float(sys.argv[3]) if len(sys.argv)>3 else 1.18
sys.path.insert(0,W); from script import LINES
m=f'/tmp/tts/vits-piper-hi_IN-{voice}-medium/hi_IN-{voice}-medium.onnx'; os.makedirs(f'{W}/vo',exist_ok=True)
here=os.path.dirname(os.path.abspath(__file__)); out=[]; t=0.12; prev=None
for i,(sc,tt,cap) in enumerate(LINES):
    raw=f'{W}/vo/r{i:02d}.wav'; fin=f'{W}/vo/f{i:02d}.wav'
    subprocess.run(['python3',f'{here}/tts_piper.py',m,tt,raw,'0.84'],check=True,capture_output=True)
    subprocess.run(['ffmpeg','-v','error','-y','-i',raw,'-af',f'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo={tempo},aresample=48000','-ac','2',fin],check=True)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',fin]))
    if prev is not None: t+=GAP_SC if prev!=sc else GAP_LN
    out.append(dict(i=i,scene=sc,cap=cap,file=fin,dur=d,start=round(t,3))); t+=d; prev=sc
json.dump(dict(lines=out,total=t+1.3),open(f'{W}/timeline.json','w'),indent=1)
for x in out: print(x['i'],x['scene'],x['start'],round(x['dur'],2))
print('TOTAL',round(t+1.3,2))
