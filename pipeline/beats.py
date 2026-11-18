"""Voice-timed beat sheet.  usage: python3 pipeline/beats.py WORKDIR   (after engine/voice.py)
Reads WORKDIR/timeline.json + script.BEATS, writes WORKDIR/beats.json at 30 fps:
per line: frame range, word frames, an 8-viseme lip-sync track (one letter per frame), rig keys, captions, camera keys, hit-stop.
Word timing is proportional to word length inside the measured line, gated by the loudness envelope (no word timestamps needed)."""
import sys, json, re
W=sys.argv[1]; sys.path.insert(0,W); import script
FPS=30; tl=json.load(open(f'{W}/timeline.json')); B=script.BEATS
CODE={'rest':'r','AI':'A','E':'E','O':'O','U':'U','MBP':'M','FV':'F','L':'L'}
norm=lambda w: re.sub(r"[^a-z0-9]",'',w.lower())
def visemes(w):
    w=re.sub('[^a-z]','',w.lower()); out=[]; i=0
    while i<len(w):
        c=w[i]; n=w[i+1] if i+1<len(w) else ''
        v='AI' if c in 'ai' else 'E' if c=='e' else 'O' if c=='o' else 'U' if c in 'uw' else 'MBP' if c in 'mbp' else 'FV' if c in 'fv' else 'L' if c in 'ltdn' else 'E'
        if c==n and c in 'ae': i+=1
        if c=='o' and n=='o': v='U'; i+=1
        if not out or out[-1]!=v: out.append(v)
        i+=1
    return out or ['E']
beats=[]; events=[0]
for l,b in zip(tl['lines'],B):
    f0=round(l['start']*FPS); n=max(1,round(l['dur']*FPS)); words=l['cap'].split(); wt=[len(norm(w))+1.5 for w in words]; tot=sum(wt); c=0; wf=[]
    for w,x in zip(words,wt): wf.append(dict(w=norm(w),f=f0+round(n*c/tot),n=max(1,round(n*x/tot)))); c+=x
    def at(word):
        if word is None: return f0
        for x in wf:
            if x['w'].startswith(word): return x['f']
        raise SystemExit(f"line {l['i']}: anchor '{word}' not in '{l['cap']}'")
    vis=['r']*n; env=l.get('env','')
    for x in wf:
        vs=visemes(x['w']); k0=x['f']-f0
        for k in range(x['n']):
            if k0+k<n: vis[k0+k]=CODE[vs[min(len(vs)-1,int(k/x['n']*len(vs)))]]
    for k in range(n):                       # closed mouth where the voice is silent
        if k<len(env) and int(env[k])<=1: vis[k]='r'
    hit=None
    if b.get('hit'): hit=dict(f=at(b['hit']),hold=4)
    bt=dict(i=l['i'],who=l['spk'],scene=l['scene'],cam=l.get('cam',''),emotion=b['emotion'],action=b['action'],rule=b['rule'],f0=f0,f1=f0+n,
        words=[dict(w=x['w'],f=x['f']) for x in wf],vis=''.join(vis),
        keys=[dict(f=at(a),who=w,pose=p,expr=e,big=bool(g)) for a,w,p,e,g in b['keys']],
        caps=[dict(f=at(a),text=t) for a,t in b['caps']],cams=[dict(f=at(a),cam=c2,who=w) for a,c2,w in b.get('cams',[])],hit=hit)
    beats.append(bt); events+= [f0]+[k['f'] for k in bt['keys']]+[c['f'] for c in bt['caps']]+[c['f'] for c in bt['cams']]
total=round(tl['total']*FPS); events=sorted(set(events)); gaps=[(b2-a)/FPS for a,b2 in zip(events,events[1:]+[total])]
checks=dict(hook_frame=beats[0]['f0'],hook_ok=beats[0]['f0']/FPS<=1.5 and beats[0]['caps'][0]['f']/FPS<=1.5,max_gap_s=round(max(gaps),2),cadence_ok=max(gaps)<=(6.0 if getattr(script,'LONG',False) else 3.0),
    hits=[b['hit']['f'] for b in beats if b['hit']],duration_s=round(tl['total'],2),duration_ok=(30<=tl['total']<=60) if getattr(script,'NEWS',False) else (60<=tl['total']<=900) if getattr(script,'LONG',False) else (22<=tl['total']<=36))
json.dump(dict(fps=FPS,total_frames=total,checks=checks,beats=beats),open(f'{W}/beats.json','w'),indent=1)
print(json.dumps(checks))
