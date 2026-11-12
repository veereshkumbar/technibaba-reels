"""Mix voice + music + SFX and mux.  usage: python3 audio.py WORKDIR OUT.mp4 [music_file] [music_gain=0.30]
- voice from WORKDIR/timeline.json, SFX cues from WORKDIR/sfx.json ([[t,'whoosh'|'thud'|'pop'|'ding'|'type'|'cash'|'crack'|'blip'|'gameover'|'fall'|'tick'],...])
- music: a royalty-free file (looped, ducked under voice) or, if none, a built-in synth beat."""
import sys, json, subprocess, numpy as np, soundfile as sf
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
vo=vo/(np.abs(vo).max()+1e-9)*.92
if MUSIC:
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
e2=np.convolve(np.abs(vo),np.ones(int(.15*SR))/int(.15*SR),'same'); duck=1-0.55*np.clip(e2/0.08,0,1)
mus=mus*fade/(np.abs(mus).max()+1e-9)*MG*duck
def whoosh():
    n=int(.45*SR); x=np.convolve(rng.standard_normal(n),np.ones(16)/16,'same'); t=np.arange(n)/SR; return x*np.sin(np.pi*t/.45)**2*2.0
LIB={'whoosh':whoosh()*.5,'thud':M(sine(lambda t:70+60*np.exp(-t*25),.4,.12),noise(.05,.01)*.4),
 'type':np.concatenate([np.concatenate([np.diff(noise(.012,.004),prepend=0),np.zeros(int(.055*SR))]) for _ in range(6)])*.5,
 'cash':M(sine(2093,.5,.18),sine(2637,.5,.2)*.7)*.35,'crack':M(noise(.25,.05)*.6,sine(lambda t:400-300*t/.4,.4,.15)*.4),
 'gameover':np.concatenate([sq(f,.16,.12) for f in (523,392,330,262,196)])*.5,'blip':sq(220,.12,.08)*.6,
 'pop':sine(lambda t:500+900*t/.1,.1,.05)*.6,'ding':M(sine(1320,1.0,.4),.5*sine(2640,1.0,.25),.3*sine(3960,1.0,.15))*.45,
 'tick':np.diff(noise(.02,.005),prepend=0)*.5,'fall':sine(lambda t:900-700*t/1.2,1.2,.6)*.5}
fx=np.zeros(N)
try:
    for t,typ in json.load(open(f'{W}/sfx.json')):
        if typ in LIB: add(fx,LIB[typ],t,.55)
except FileNotFoundError: pass
mix=np.tanh((vo+mus+fx*.8)*1.1)*.95; mix=mix[:int(total*SR)]
sf.write(f'{W}/mix.wav',np.stack([mix,mix],1),SR)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/mix.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-ar','48000',f'{W}/mix_n.wav'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/video_only.mp4','-i',f'{W}/mix_n.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',OUT],check=True)
print('final',OUT)
