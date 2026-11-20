"""Photo-puppet host: a single front-facing portrait (assets/host/veer_3d.png) lip-synced to the voice.
Per frame: continuous jaw drop (chin, beard and lower cheeks move together), upper lip lifts a little, corners widen
(ee/s sounds) or pucker (o/u), mouth interior with depth, upper and lower teeth, tongue; head nods on stressed syllables.
usage: from puppet import Host; h=Host(); h.track(wav_path_or_array, sr, fps) -> per-frame params; h.frame(i) -> PIL RGB
"""
import numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates, gaussian_filter

CFG = dict(img='assets/host/veer_3d.png', MY=651, CX=623, LW=80, box=(360, 560, 900, 960), jaw=36)


class Host:
    def __init__(self, root='.', cfg=CFG):
        self.c = cfg
        self.src = np.asarray(Image.open(f"{root}/{cfg['img']}").convert('RGB')).astype(np.float32)
        x0, y0, x1, y1 = cfg['box']
        self.yy, self.xx = np.mgrid[y0:y1, x0:x1].astype(np.float32)
        self.patch_src = self.src[y0:y1, x0:x1]

    # ---------------------------------------------------------------- audio -> visemes
    def track(self, audio, sr, fps, n):
        hop = sr / fps
        op, rnd, wid = np.zeros(n), np.zeros(n), np.zeros(n)
        win = int(sr * .04)
        for k in range(n):
            a = audio[int(k * hop):int(k * hop) + win]
            if len(a) < 64: continue
            rms = np.sqrt(np.mean(a ** 2))
            S = np.abs(np.fft.rfft(a * np.hanning(len(a))))
            f = np.fft.rfftfreq(len(a), 1 / sr)
            c = (S * f).sum() / (S.sum() + 1e-9)
            op[k] = rms; rnd[k] = np.clip((1300 - c) / 700, 0, 1); wid[k] = np.clip((c - 2200) / 1500, 0, 1)
        op = op / (np.percentile(op[op > 0], 92) + 1e-9) if (op > 0).any() else op
        op = np.clip((op - .07) / .85, 0, 1)
        # attack fast, release slower (lips close more gently than they open)
        sm = np.zeros(n); v = 0
        for k in range(n):
            v = v + (op[k] - v) * (.7 if op[k] > v else .38); sm[k] = v
        self.op = sm
        self.rnd = np.convolve(rnd, np.ones(3) / 3, 'same') * (sm > .12)
        self.wid = np.convolve(wid, np.ones(3) / 3, 'same') * (sm > .08)
        # stress = rising edge of loudness -> small nod
        d = np.maximum(0, np.diff(sm, prepend=0))
        self.nod = np.convolve(d, np.exp(-np.arange(12) / 4), 'full')[:n]
        return self

    # ---------------------------------------------------------------- one mouth patch
    def mouth(self, op, rnd, wid):
        c, yy, xx = self.c, self.yy, self.xx
        MY, CX, LW = c['MY'], c['CX'], c['LW']
        d = c['jaw'] * op
        hw = LW * (1 + .14 * wid - .3 * rnd) * (1 - .22 * op)
        # lower face: jaw drop with a wide soft falloff (cheeks move a little, chin fully)
        wx = np.clip(1 - ((xx - CX) / 300) ** 2, 0, 1) ** 1.3
        below = np.clip((yy - MY + 3) / 8, 0, 1) * np.clip((950 - yy) / 70, 0, 1)
        dy = d * wx * below
        # upper lip lifts ~18 % of the drop, fading upward into the mustache
        above = np.clip((MY + 3 - yy) / 6, 0, 1) * np.exp(-((MY - yy) / 22) ** 2)
        lipw = np.exp(-((xx - CX) / (hw * 1.1)) ** 2)
        dy = dy - .14 * d * above * lipw * np.exp(-((xx - CX) / (hw * .9)) ** 2)
        # corners: widen (ee) or pucker (oo) around the mouth only
        reg = np.exp(-((xx - CX) / (LW * 1.5)) ** 2) * np.exp(-((yy - MY - d * .45) / 40) ** 2)
        sx = xx - (xx - CX) * (.12 * wid - .22 * rnd) * reg
        out = np.stack([map_coordinates(self.src[..., k], [yy - dy, sx], order=1, mode='nearest') for k in range(3)], -1)
        if d < .6: return out
        # interior lens between the lifted upper lip and the dropped lower lip
        t = np.clip(1 - ((xx - CX) / hw) ** 2, 0, 1)
        top = MY - 1 - .18 * d * t ** .6
        bot = MY + .9 * d * t ** (.55 - .15 * rnd)
        inside = (yy > top) & (yy < bot) & (t > .02)
        m = gaussian_filter(inside.astype(np.float32), 1.1)
        depth = np.clip((yy - top) / np.maximum(bot - top, 1), 0, 1)
        edge = np.clip(np.abs(xx - CX) / hw, 0, 1)
        dark = (1 - .55 * np.sin(np.pi * depth) * (1 - edge)) * (1 - .35 * edge)
        inter = np.stack([92 * dark, 30 * dark, 28 * dark], -1)
        # tongue at the bottom of a big opening
        tg = np.exp(-((yy - bot + d * .2) / (d * .22 + 1)) ** 2) * np.exp(-((xx - CX) / (hw * .5)) ** 2) * np.clip(op - .35, 0, 1) * 1.6
        inter = inter * (1 - tg[..., None] * .8) + np.array([168, 70, 66]) * (tg[..., None] * .8)
        # upper teeth (shaded, occluded at the corners), a glimpse of lower teeth on wide openings
        th = min(11.0, (d * .9) * .36)
        tu = ((yy > top + .5) & (yy < top + .5 + th) & (edge < .66)).astype(np.float32)
        tu = gaussian_filter(tu, 1.3) * (1 - rnd * .85) * np.clip((1 - edge / .7), 0, 1) ** .5
        tcol = np.stack([236 - 46 * edge, 224 - 50 * edge, 204 - 52 * edge], -1) * (1 - .18 * np.clip((yy - top) / (th + 1), 0, 1) ** 2)[..., None]
        inter = inter * (1 - tu[..., None]) + tcol * tu[..., None]
        tl = ((yy < bot - .5) & (yy > bot - .5 - th * .55) & (edge < .5)).astype(np.float32)
        tl = gaussian_filter(tl, 1.3) * np.clip(op - .7, 0, 1) * 2.5 * (1 - rnd)
        inter = inter * (1 - tl[..., None] * .7) + np.array([190, 182, 172]) * (tl[..., None] * .7)
        # soft shadow under the upper lip
        sh = np.exp(-((yy - top - 1) / 3.2) ** 2) * .5
        inter = inter * (1 - sh[..., None])
        out = out * (1 - m[..., None]) + inter * m[..., None]
        # contact shadow under the lower lip deepens as it drops
        cs = np.exp(-((yy - bot - 10) / 7) ** 2) * np.exp(-((xx - CX) / (hw * .9)) ** 2) * .16 * op
        return out * (1 - cs[..., None])

    def frame(self, k):
        img = self.src.copy()
        x0, y0, x1, y1 = self.c['box']
        img[y0:y1, x0:x1] = self.mouth(self.op[k], self.rnd[k], self.wid[k])
        return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
