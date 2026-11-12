"""Render page.html to WORKDIR/video_only.mp4 (one encoded file per scene, concat).
usage: python3 render.py WORKDIR.  Page must expose render(t), TOTAL, and optionally ORDER + SC{name:{s,e}} and SFX."""
import sys, asyncio, subprocess, json, os
from playwright.async_api import async_playwright
W=sys.argv[1]; FPS=30; os.makedirs(f'{W}/scenes',exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto(f'file://{W}/page.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        total=await pg.evaluate('TOTAL'); sfx=await pg.evaluate('window.SFX||[]'); json.dump(sfx,open(f'{W}/sfx.json','w'))
        order=await pg.evaluate('window.ORDER||null'); n=round(total*FPS)
        if order:
            SC=await pg.evaluate('SC'); bounds=[round(SC[k]['s']*FPS) for k in order]+[n]
        else: order=['all']; bounds=[0,n]
        lst=open(f'{W}/scenes/list.txt','w')
        for k,name in enumerate(order):
            out=f'{W}/scenes/{k}_{name}.mp4'; tmp=out+'.tmp.mp4'
            if not os.path.exists(out):
                ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-f','mp4',tmp],stdin=subprocess.PIPE)
                for f in range(bounds[k],bounds[k+1]):
                    await pg.evaluate(f'render({f/FPS})'); ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
                ff.stdin.close(); assert ff.wait()==0; os.rename(tmp,out)
            lst.write(f"file '{out}'\n"); print(name,bounds[k+1]-bounds[k],'frames',flush=True)
        lst.close(); await b.close()
asyncio.run(main())
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{W}/scenes/list.txt','-c','copy',f'{W}/video_only.mp4'],check=True)
print('video',f'{W}/video_only.mp4')
