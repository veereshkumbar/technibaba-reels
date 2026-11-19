"""Build a HyperFrames project from a split-layout reel.  usage: python3 pipeline/hf_build.py WORKDIR [music.wav] [gain]
Needs WORKDIR/page.html (engine/build.py) and beats.json. Writes WORKDIR/hf/ (index.html + assets) ready for:
  HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome npx hyperframes render WORKDIR/hf -o OUT.mp4
The GSAP timeline owns the panel drop-in, page transitions, caption pops, hit shakes and the progress bar; the rigs and panel art
are drawn by a time-driven setter on the same timeline, so every frame is seekable."""
import sys, os, json, re, shutil, subprocess, asyncio, html as H
from playwright.async_api import async_playwright
W=os.path.abspath(sys.argv[1]); MUSIC=sys.argv[2] if len(sys.argv)>2 else '-'; GAIN=sys.argv[3] if len(sys.argv)>3 else '0.20'
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B=json.load(open(f'{W}/beats.json')); T=json.load(open(f'{root}/brand/tokens.json')); C=T['color']
FPS=30; NF=B['total_frames']; DUR=NF/FPS; BT=B['beats']; hf=f'{W}/hf'; os.makedirs(f'{hf}/assets',exist_ok=True)
# 1. sound: SFX cues from the page, then voice + music + SFX mix
async def cues():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files']); pg=await b.new_page()
        await pg.goto(f'file://{W}/page.html'); s=await pg.evaluate("typeof SFX!=='undefined'?SFX:[]"); await b.close(); return s
sfx=asyncio.run(cues()); json.dump(sfx,open(f'{W}/sfx.json','w'))
subprocess.run(['python3',f'{root}/engine/audio.py',W,'-',MUSIC,GAIN],check=True); shutil.copy(f'{W}/mix_n.wav',f'{hf}/assets/mix.wav')
# 2. fonts + gsap
F='/tmp/fonts/node_modules/@fontsource'; fonts={'pop600':f'{F}/poppins/files/poppins-latin-600-normal.woff2','pop800':f'{F}/poppins/files/poppins-latin-800-normal.woff2','pop900':f'{F}/poppins/files/poppins-latin-900-normal.woff2','mono700':f'{F}/jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2'}
PREM=os.path.exists(f'{W}/layout_premium')
if PREM: fonts.update({f'inter{w}':f'{F}/inter/files/inter-latin-{w}-normal.woff2' for w in (400,600,700,800)})
for k,v in fonts.items(): shutil.copy(v,f'{hf}/assets/{k}.woff2')
gsap=open('/tmp/fonts/node_modules/gsap/dist/gsap.min.js').read()
# 3. reel script (everything before the old engine's render function)
page=open(f'{W}/page.html').read(); js=page[page.index('<script>')+8:page.index('\nconst DEFS=')]
# 4. static clips: panel pages and captions
order=[]; [order.append(b['scene']) for b in BT if b['scene'] not in order]
scs={n:(0 if k==0 else next(b for b in BT if b['scene']==n)['f0']-5) for k,n in enumerate(order)}
LONG=os.path.exists(f'{W}/layout_long'); NEWSL=json.load(open(f'{W}/layout_news')) if os.path.exists(f'{W}/layout_news') else None
hook_end=0 if (LONG or NEWSL) else BT[1]['f0']-3
pages=''
for k,n in enumerate(order):
    s=max(scs[n],hook_end) if k==0 else scs[n]; e=scs[order[k+1]] if k<len(order)-1 else NF
    pages+=f'<div class="page clip" id="page-{n}" data-scene="{n}" data-start="{s/FPS:.3f}" data-duration="{(e-s)/FPS+(0.4 if k<len(order)-1 else 0):.3f}" data-track-index="2" style="z-index:{10+k}"></div>\n'
caps=[dict(f=c['f'],text=c['text'],end=b['f1']+10,scene=b['scene']) for b in BT for c in b['caps']]
for k,c in enumerate(caps):
    if k+1<len(caps): c['end']=min(c['end'],caps[k+1]['f'])
capsh=''
for k,c in enumerate(caps):
    raw=c['text'].replace('*',''); size=min(56,780/(len(raw)*.56)) if PREM else min(72,800/(len(raw)*.6)); parts=c['text'].split('*')
    inner=''.join(f'<span class="{"kw" if i%2 else ""}">{H.escape(s)}</span>' for i,s in enumerate(parts)) if not PREM else ''.join((f'<span class="w kw">{H.escape(s)}</span>' if i%2 else ''.join(f'<span class="w">{H.escape(w)}</span>' for w in re.split(r'(\s+)',s) if w)) for i,s in enumerate(parts) if s)
    top=(1110 if NEWSL[c['scene']]=='split' else (1290 if NEWSL[c['scene']]=='card' else 1470)) if NEWSL else (990 if LONG else ((1780 if PREM else 1440) if c['f']<hook_end else 1082))
    capsh+=f'<div class="cap clip" id="cap-{k}" data-start="{c["f"]/FPS:.3f}" data-duration="{max(.2,(c["end"]-c["f"])/FPS):.3f}" data-track-index="4" style="top:{top-size*.95:.0f}px;font-size:{size:.1f}px;height:{size*1.5:.0f}px;border-radius:{size*.4:.0f}px"><span class="capt">{inner}</span></div>\n'
tpl=open(f'{root}/pipeline/'+('hf_news.html' if NEWSL else ('hf_long.html' if LONG else ('hf_premium.html' if PREM else 'hf_split.html')))).read()
out=tpl.replace('__GSAP__',gsap).replace('__SCRIPT__',js).replace('__PAGES__',pages).replace('__CAPS__',capsh).replace('__DUR__',f'{DUR:.3f}').replace('__NCAPS__',str(len(caps)))
for k in ('ink','navy','mint','captionKeyword','captionText','captionPlate'): out=out.replace('__C_'+k+'__',C[k])
open(f'{hf}/index.html','w').write(out)
json.dump({"$schema":"https://hyperframes.heygen.com/schema/hyperframes.json","registry":"https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry","paths":{"blocks":"compositions","components":"compositions/components","assets":"assets"}},open(f'{hf}/hyperframes.json','w'),indent=1)
json.dump({"name":os.path.basename(W),"private":True,"type":"module"},open(f'{hf}/package.json','w'))
print('hyperframes project',hf,'| sfx cues',len(sfx),'| pages',len(order),'| captions',len(caps))
