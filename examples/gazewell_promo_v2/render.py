import json, sys, os, asyncio
W = os.path.dirname(os.path.abspath(__file__)); FPS = 30
tl = json.load(open(f'{W}/timeline.json'))
TOTAL = 50.0; N = int(TOTAL * FPS)
L = [[l['start'], l['start'] + l['dur']] for l in tl['lines']]
# short on-screen captions per line (muted viewers)
CAPS = ['', 'Clear only at 20 to 30 cm', '', 'See it live, at their exact age', '', 'Growth, milestones, memories, reminders', '', '']
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
        sw = w(0, .52)
        cues = [[0.1, 'popin'], [sw, 'whoosh'], [sw + .9, 'subdrop'], [L[1][0], 'swish'], [w(1, .45), 'riser'], [w(1, .45) + .5, 'ding'],
                [L[2][0] - .15, 'whoosh'], [w(2, .36), 'tick'], [w(2, .55), 'tick'], [w(2, .74), 'tick'], [w(2, .93), 'ding'],
                [L[3][0] - .25, 'boom'], [L[4][0] - .2, 'whoosh'], [L[4][0] + .7, 'swish'], [L[5][0] - .2, 'whoosh'],
                [w(5, 0), 'popin'], [w(5, .33), 'popin'], [w(5, .5), 'popin'], [w(5, .68), 'ding'], [L[6][0] - .2, 'whoosh'], [L[6][0] + .15, 'click'],
                [L[7][0] - .2, 'whoosh'], [w(7, .05) + .4, 'type'], [w(7, .55), 'popin'], [L[7][1] + .3, 'sting']]
        json.dump(cues, open(f'{W}/sfx.json', 'w'))
    print('ok', N)
