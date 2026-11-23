"""Mix voice + music + SFX and mux.  usage: python3 audio.py WORKDIR OUT.mp4|- [music_file] [music_gain=0.30]   (OUT "-" = only write WORKDIR/mix_n.wav)
- voice from WORKDIR/timeline.json, SFX cues from WORKDIR/sfx.json ([[t,'whoosh'|'thud'|'pop'|'ding'|'type'|'cash'|'crack'|'blip'|'gameover'|'fall'|'tick'],...])
- music: a royalty-free file (looped, ducked under voice) or, if none, a built-in synth beat."""
import sys, os, json, subprocess, numpy as np, soundfile as sf
W=sys.argv[1]; OUT=sys.argv[2]; MUSIC=sys.argv[3] if len(sys.argv)>3 and sys.argv[3]!='-' else None; MG=float(sys.argv[4]) if len(sys.argv)>4 else .30
SR=48000; tl=json.load(open(f'{W}/timeline.json')); total=tl['total']; N=int(total*SR)+SR; rng=np.random.default_rng(1)
def env(n,a=.005,d=None):
    t=np.arange(n)/SR; e=np.minimum(1,t/a); return e*(np.exp(-t/d) if d else 1)
def sine(f,dur,d=.2,a=.003):
    n=int(dur*SR); t=np.arange(n)/SR; ph=2*np.pi*np.cumsum(f(t) if callable(f) else np.full(n,float(f)))/SR; return np.sin(ph)*env(n,a,d)
def noise(dur,d=.1): n=int(dur*SR); return rng.standard_normal(n)*env(n,.002,d)
def M(*xs):
    n=max(len(x) for x in xs); o=np.zeros(n)
    for x in xs: o[:len(x)]+=x
    return o
def sq(f,dur,d=.15): n=int(dur*SR); t=np.arange(n)/SR; return np.sign(np.sin(2*np.pi*f*t))*env(n,.002,d)*.5
def add(b,x,t,g=1):
    i=int(t*SR)
    if i>=len(b) or i<0: return
    x=x[:len(b)-i]; b[i:i+len(x)]+=x*g
vo=np.zeros(N)
for l in tl['lines']:
    x,_=sf.read(l['file']); x=x.mean(1) if x.ndim>1 else x; add(vo,x,l['start'])
vo=vo/(np.abs(vo).max()+1e-9); vo=np.tanh(vo*2.2)/np.tanh(2.2)*.95   # gentle compression: voice sits louder and steadier (Veer, 16 Nov)
# studio voice chain (20 Nov, matched to a premium reference voice: less low-end mud, +presence 3.6 kHz, air shelf,
# compression, de-ess, a touch of room). Measured on the reference: 2-5 kHz at -13 dB of total, < 150 Hz at -9 dB.
VCHAIN='highpass=f=100:poles=2,lowshelf=f=160:g=-4,equalizer=f=260:t=o:w=1.2:g=-3,equalizer=f=3600:t=o:w=1.6:g=5.5,highshelf=f=8500:g=4.5,acompressor=threshold=-22dB:ratio=3.2:attack=4:release=90:makeup=4,deesser=i=0.45,aecho=0.8:0.6:18:0.05,alimiter=limit=0.89'
sf.write(f'{W}/vo_raw.wav',vo,SR)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/vo_raw.wav','-af',VCHAIN,'-ar',str(SR),'-ac','1',f'{W}/vo_chain.wav'],check=True)
_v,_=sf.read(f'{W}/vo_chain.wav'); _v=_v[:N] if len(_v)>=N else np.pad(_v,(0,N-len(_v))); vo=_v/(np.abs(_v).max()+1e-9)*.95
if MUSIC:
    if os.path.abspath(MUSIC)==os.path.abspath(f'{W}/music.wav'):   # guard: input == output would truncate it and hang ffmpeg
        import shutil as _sh; _sh.copy(MUSIC,f'{W}/bed_in.wav'); MUSIC=f'{W}/bed_in.wav'
    subprocess.run(['ffmpeg','-v','error','-y','-stream_loop','-1','-i',MUSIC,'-t',str(total+1),'-ac','1','-ar',str(SR),f'{W}/music.wav'],check=True)
    mus,_=sf.read(f'{W}/music.wav'); mus=np.pad(mus,(0,max(0,N-len(mus))))[:N]
else:
    mus=np.zeros(N); beat=60/104
    kick=sine(lambda t:50+90*np.exp(-t*30),.35,.12); snare=M(np.convolve(noise(.2,.06),np.ones(3)/3,'same')*.5,sine(190,.12,.05)*.3); hat=np.diff(noise(.06,.015),prepend=0)*.6
    roots=[110,87.31,130.81,98.0]; chords=[[220,261.6,329.6],[174.6,220,261.6],[261.6,329.6,392],[196,246.9,293.7]]
    for b in range(int(total/beat)+2):
        t=b*beat; bar=(b//4)%4
        if b%4 in (0,2): add(mus,kick,t,.9)
        if b%4 in (1,3): add(mus,snare,t,.55)
        add(mus,hat,t+beat/2,.25); add(mus,M(sine(roots[bar],beat*.9,.25),sine(roots[bar]*2,beat*.9,.12)*.25),t,.55)
        if b%2==0:
            for j,f in enumerate(chords[bar]): add(mus,M(sine(f*2,.3,.09),.3*sine(f*4,.3,.05)),t+j*beat/3,.10)
fade=np.ones(N); fi=int(.3*SR); fade[:fi]=np.linspace(0,1,fi); fo=int(1.5*SR); e=int(total*SR); fade[e-fo:e]=np.linspace(1,0,fo); fade[e:]=0
e2=np.convolve(np.abs(vo),np.ones(int(.15*SR))/int(.15*SR),'same'); duck=1-0.72*np.clip(e2/0.06,0,1)
mus=mus*fade/(np.abs(mus).max()+1e-9)*MG*0.65*duck   # music 35% quieter than before, ducked harder under speech
def whoosh():
    n=int(.45*SR); x=np.convolve(rng.standard_normal(n),np.ones(16)/16,'same'); t=np.arange(n)/SR; return x*np.sin(np.pi*t/.45)**2*2.0
LIB={'whoosh':whoosh()*.5,'thud':M(sine(lambda t:70+60*np.exp(-t*25),.4,.12),noise(.05,.01)*.4),
 'type':np.concatenate([np.concatenate([np.diff(noise(.012,.004),prepend=0),np.zeros(int(.055*SR))]) for _ in range(6)])*.5,
 'cash':M(sine(2093,.5,.18),sine(2637,.5,.2)*.7)*.35,'crack':M(noise(.25,.05)*.6,sine(lambda t:400-300*t/.4,.4,.15)*.4),
 'gameover':np.concatenate([sq(f,.16,.12) for f in (523,392,330,262,196)])*.5,'blip':sq(220,.12,.08)*.6,
 'pop':sine(lambda t:500+900*t/.1,.1,.05)*.6,'ding':M(sine(1320,1.0,.4),.5*sine(2640,1.0,.25),.3*sine(3960,1.0,.15))*.45,
 'tick':np.diff(noise(.02,.005),prepend=0)*.5,'fall':sine(lambda t:900-700*t/1.2,1.2,.6)*.5}
def riser():
    n=int(.36*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*np.cumsum(220+1500*(t/.36)**2)/SR)*.5+rng.standard_normal(n)*.25)*(t/.36)**2
LIB['riser']=riser()*.5; LIB['boom']=M(sine(lambda t:46+70*np.exp(-t*18),.7,.22)*1.3,noise(.08,.02)*.5); LIB['swish']=whoosh()[:int(.22*SR)]*.22
fx=np.zeros(N)
# SFX v2 (SOUND_DESIGN.md): pro-spec recipes from engine/sfx_lib.py, each placed by its anchor (attack / peak / end)
# on the cue time, with restraint: accents >= 0.8 s apart, UI detail >= 90 ms apart, successive dings step up a semitone.
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import sfx_lib
try: cues=sorted(json.load(open(f'{W}/sfx.json')),key=lambda c:(round(c[0],2),{'boom':0,'impact':0,'riser':1}.get(c[1],2)))
except FileNotFoundError: cues=[]
last={}; dstep=0; dlast=-9; placed=[]
for t,typ in cues:
    r=sfx_lib.render(typ, dstep if typ=='ding' else 0)
    if r is None:
        if typ in LIB: add(fx,LIB[typ],t,.55); placed.append([t,typ,'legacy'])
        continue
    x,anc,role=r
    gap={'impact':.8,'whoosh':1.4,'riser':1.0}.get(role,.12)
    if t-last.get(role,-9)<gap: placed.append([t,typ,'dropped (too close to the last '+role+')']); continue
    # one accent per moment: no small sound stacked on an impact, no whoosh on top of an impact
    if role in ('ui','pop','zip','whoosh') and abs(t-last.get('impact',-9))<.15: placed.append([t,typ,'dropped (on an impact)']); continue
    if role in ('ui','pop') and any(abs(t-q[0])<.06 for q in placed if len(q)>3 and q[2] in ('ui','pop')): placed.append([t,typ,'dropped (stacked)']); continue
    last[role]=t
    if typ=='ding': dstep=dstep+1 if t-dlast<1.5 else 0; dlast=t
    add(fx,x,t-anc,1.0); placed.append([round(t,3),typ,role,round(t-anc,3)])
json.dump(placed,open(f'{W}/sfx_report.json','w'))
# keep SFX out of the voice's 1-4 kHz while someone speaks (earshot: VO rule)
spk=np.zeros(N)
for l in tl['lines']:
    a0=int(l['start']*SR); spk[a0:a0+int(l['dur']*SR)]=1
spk=np.convolve(spk,np.ones(int(.08*SR))/int(.08*SR),'same')
fx=fx-sfx_lib.bp(fx,1000,4000)*.75*spk
fxduck=1-0.55*np.clip(e2/0.06,0,1)   # SFX also dip under speech
mix=np.tanh((vo*1.4+mus+fx*.42*fxduck)*1.05)*.95   # viewer feedback 19 Nov: voices louder, SFX about half as loud; mix=mix[:int(total*SR)]
sf.write(f'{W}/mix.wav',np.stack([mix,mix],1),SR)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/mix.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-ar','48000',f'{W}/mix_n.wav'],check=True)
if OUT!='-': subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/video_only.mp4','-i',f'{W}/mix_n.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',OUT],check=True)
print('final',OUT)
