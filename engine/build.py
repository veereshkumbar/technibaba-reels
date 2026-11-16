"""Inject timeline into template.  usage: python3 build.py WORKDIR  (needs WORKDIR/page_tpl.html with __TL__)"""
import sys, json
W=sys.argv[1]; tl=json.load(open(f'{W}/timeline.json'))
tl2={'total':tl['total'],'lines':[{k:l[k] for k in ('i','scene','cap','start','dur','spk','env','cam') if k in l} for l in tl['lines']]}
import os
html=open(f'{W}/page_tpl.html').read().replace('__TL__',json.dumps(tl2))
if '__CHARS__' in html: html=html.replace('__CHARS__',open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'chars.js')).read())
if '__FACE__' in html: html=html.replace('__FACE__',open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'face.js')).read())
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); rd=lambda *a: open(os.path.join(root,*a)).read()
if '__TOKENS__' in html: html=html.replace('__TOKENS__',rd('brand','tokens.json'))
if '__RIGS__' in html: html=html.replace('__RIGS__','\n'.join(rd('rigs',f) for f in ('core.js','face.js','baba/rig.js','friend/rig.js')))
if '__STAGE__' in html: html=html.replace('__STAGE__',rd('pipeline','stage.js'))
if '__LONG__' in html: html=html.replace('__LONG__',rd('pipeline','long.js'))
if '__SPLIT__' in html: html=html.replace('__SPLIT__',rd('pipeline','split.js'))
if '__BEATS__' in html: html=html.replace('__BEATS__',open(f'{W}/beats.json').read())
open(f'{W}/page.html','w').write(html)
print('built',f'{W}/page.html')
