"""Inject timeline into template.  usage: python3 build.py WORKDIR  (needs WORKDIR/page_tpl.html with __TL__)"""
import sys, json
W=sys.argv[1]; tl=json.load(open(f'{W}/timeline.json'))
tl2={'total':tl['total'],'lines':[{k:l[k] for k in ('i','scene','cap','start','dur')} for l in tl['lines']]}
open(f'{W}/page.html','w').write(open(f'{W}/page_tpl.html').read().replace('__TL__',json.dumps(tl2)))
print('built',f'{W}/page.html')
