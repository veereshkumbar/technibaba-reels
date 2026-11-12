"""Inject timeline into template.  usage: python3 build.py WORKDIR  (needs WORKDIR/page_tpl.html with __TL__)"""
import sys, json
W=sys.argv[1]; tl=json.load(open(f'{W}/timeline.json'))
tl2={'total':tl['total'],'lines':[{k:l[k] for k in ('i','scene','cap','start','dur')} for l in tl['lines']]}
import os
html=open(f'{W}/page_tpl.html').read().replace('__TL__',json.dumps(tl2))
if '__CHARS__' in html: html=html.replace('__CHARS__',open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'chars.js')).read())
open(f'{W}/page.html','w').write(html)
print('built',f'{W}/page.html')
