"""QA screenshots.  usage: python3 shots.py WORKDIR t1 t2 ...  -> WORKDIR/qa/shot_T.jpg + contact sheet"""
import sys, asyncio, os, subprocess
from playwright.async_api import async_playwright
W=sys.argv[1]; ts=[float(x) for x in sys.argv[2:]]; os.makedirs(f'{W}/qa',exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(f'file://{W}/page.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        for t in ts:
            await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'{W}/qa/shot_{t:06.2f}.jpg',type='jpeg',quality=80)
        print('page errors:',errs); await b.close()
asyncio.run(main())
fs=sorted(f'{W}/qa/'+f for f in os.listdir(f'{W}/qa') if f.startswith('shot_'))[-len(ts):]
args=sum([['-i',f] for f in fs],[]); subprocess.run(['ffmpeg','-v','error','-y',*args,'-filter_complex',f'hstack={len(fs)},scale=1900:-1' if len(fs)>1 else 'scale=600:-1',f'{W}/qa/sheet.jpg'])
print('sheet',f'{W}/qa/sheet.jpg')
