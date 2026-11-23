import json, sys, os, asyncio
W = os.path.dirname(os.path.abspath(__file__)); FPS = 30
tl = json.load(open(f'{W}/timeline.json'))
TOTAL = 50.0; N = int(TOTAL * FPS)
L = [[l['start'], l['start'] + l['dur']] for l in tl['lines']]
# short on-screen captions per line (muted viewers)
CAPS = ['How your newborn sees you', 'Blurry, black & white, close up', 'Clearer every month', 'Live, at your baby\'s exact age',
        'Send this to a parent', 'Growth vs WHO charts', 'Milestones, memories, reminders', 'Camera never leaves your phone', '']
caps = [[a, b + .25, c] for (a, b), c in zip(L, CAPS) if c]
TJS = 'window.T={total:%s,lines:%s,w:(i,u)=>window.T.lines[i][0]+(window.T.lines[i][1]-window.T.lines[i][0])*u};window.CAPS=%s;' % (TOTAL, json.dumps(L), json.dumps(caps))

async def run(a, z, out):
    from playwright.async_api import async_playwright
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.add_init_script(TJS)
        await pg.goto(f'file://{W}/page.html')
        for f in range(a, min(z, N)):
            await pg.evaluate(f'frame({f})')
            await pg.screenshot(path=f'{out}/{f:04d}.jpg', type='jpeg', quality=92)
        await b.close()

if __name__ == '__main__':
    if sys.argv[1] == 'frames': asyncio.run(run(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]))
    elif sys.argv[1] == 'sfx':
        def w(i, u): return L[i][0] + (L[i][1] - L[i][0]) * u
        cues = [[0.12, 'popin'], [w(1, .02), 'tick'], [w(1, .18), 'tick'], [w(1, .42), 'tick'],
                [L[2][0], 'whoosh'], [w(2, .33), 'ding'], [w(2, .55), 'ding'], [w(2, .72), 'ding'], [w(2, .92), 'ding'],
                [L[3][0] - .3, 'whoosh'], [L[3][0] - .1, 'popin'], [L[4][0] - .2, 'swish'], [L[5][0] - .2, 'whoosh'],
                [L[5][0] + 1.0, 'tick'], [L[5][0] + 1.7, 'tick'], [L[6][0] - .2, 'whoosh'], [w(6, 0) + .5, 'click'], [w(6, 0) + .95, 'click'], [w(6, 0) + 1.4, 'click'],
                [w(6, .72), 'ding'], [L[7][0] - .2, 'whoosh'], [L[8][0] - .2, 'boom'], [L[8][0] + .3, 'sting']]
        json.dump(cues, open(f'{W}/sfx.json', 'w'))
    print('ok', N)
