"""Proof checks + contact sheet.  usage: python3 pipeline/check.py WORKDIR FINAL.mp4
Checks: duration matches, hook by 1.5s, visual-change cadence, captions inside the title-safe box, audio peak. Writes WORKDIR/qa/contact.png."""
import sys, json, subprocess, os, re
from PIL import Image, ImageDraw, ImageFont
W,OUT=sys.argv[1],sys.argv[2]; root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=json.load(open(f'{W}/beats.json')); T=json.load(open(f'{root}/brand/tokens.json')); S=T['frame']['safe']; ck=dict(B['checks'])
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',OUT])); ck['video_s']=round(dur,2); ck['duration_match']=abs(dur-B['total_frames']/30)<0.25
vd=subprocess.run(['ffmpeg','-i',OUT,'-af','volumedetect','-f','null','-'],capture_output=True,text=True).stderr
ck['peak_db']=float(re.search(r'max_volume: (-?[\d.]+)',vd).group(1)); ck['peak_ok']=ck['peak_db']<=-1.0
caps=[c for b in B['beats'] for c in b['caps']]; bad=[]
for c in caps:
    raw=c['text'].replace('*',''); size=min(72,800/(len(raw)*.6)); w=len(raw)*size*.6   # text width; the plate itself is clamped to the safe box by stage.js
    if 540-w/2<S['x0']-1 or 540+w/2>S['x1']+1 or c['text'].count('*')!=2: bad.append(c['text'])
ck['captions_ok']=not bad; ck['captions_bad']=bad
os.makedirs(f'{W}/qa',exist_ok=True)
# stills come from the finished video, so the sheet shows exactly what was rendered (any renderer)
for bt in B['beats']:
    f=(bt['hit']['f']+6) if bt['hit'] else max(k['f'] for k in bt['keys'])+12; f=min(f,bt['f1']+8,B['total_frames']-2)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{f/30:.3f}','-i',OUT,'-frames:v','1','-q:v','3',f"{W}/qa/beat_{bt['i']:02d}.jpg"],check=True)
n=len(B['beats']); cols=5; rows=(n+cols-1)//cols; tw,th=360,640; pad=16; lab=96
sheet=Image.new('RGB',(cols*(tw+pad)+pad,rows*(th+lab+pad)+pad+70),'#10142a'); d=ImageDraw.Draw(sheet)
def font(sz,bold=True):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
ok=all(ck[k] for k in ('hook_ok','cadence_ok','duration_ok','duration_match','peak_ok','captions_ok'))
d.text((pad,18),f"Contact sheet  |  {ck['video_s']}s  |  hook {ck['hook_frame']/30:.2f}s  |  max gap {ck['max_gap_s']}s  |  peak {ck['peak_db']} dB  |  {'ALL CHECKS PASS' if ok else 'CHECK FAILED'}",fill='#5de0b0' if ok else '#e5383b',font=font(24))
for k,bt in enumerate(B['beats']):
    x=pad+(k%cols)*(tw+pad); y=70+(k//cols)*(th+lab+pad)
    sheet.paste(Image.open(f"{W}/qa/beat_{bt['i']:02d}.jpg").resize((tw,th)),(x,y))
    d.text((x,y+th+6),f"{bt['i']+1}. {'Baba' if bt['who']=='b' else 'Friend'}: {bt['emotion']}  ({bt['f0']}-{bt['f1']})",fill='#ffd23f',font=font(17))
    t=bt['rule']; lines=[t[:44],t[44:88]] if len(t)>44 else [t]
    for j,ln in enumerate(lines): d.text((x,y+th+30+j*20),ln,fill='#ffffff',font=font(15,False))
    d.text((x,y+th+72),'hit-stop' if bt['hit'] else 'ok',fill='#5de0b0',font=font(15))
sheet.save(f'{W}/qa/contact.png'); json.dump(ck,open(f'{W}/qa/checks.json','w'),indent=1); print(json.dumps(ck)); print('sheet',f'{W}/qa/contact.png')
