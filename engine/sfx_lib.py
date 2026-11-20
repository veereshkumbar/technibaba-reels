"""TechniBaba sound-effect library, v2 (20 Nov 2026).

Every sound is our own code, written to the measured targets in earshot's study of professional motion-design films
(github.com/Leonxlnx/earshot, MIT: docs/motion-sfx-study.md, docs/launch-video-sound.md). See SOUND_DESIGN.md.
Each entry: (samples, anchor_s, role). anchor_s = the point inside the sound that must sit ON the cue time
(attack for clicks/pops, peak for whooshes and impacts, end for risers and zips), so placement is frame-accurate.
"""
import numpy as np
from scipy.signal import butter, sosfilt

SR = 48000
_rng = np.random.default_rng(7)


def _t(d): return np.arange(int(d * SR)) / SR
def _f(x, kind, f, o=4): return sosfilt(butter(o, f, kind, fs=SR, output='sos'), x)
def bp(x, lo, hi, o=4): return _f(x, 'band', [lo, hi], o)
def hp(x, f, o=4): return _f(x, 'high', f, o)
def lp(x, f, o=4): return _f(x, 'low', f, o)
def noise(d): return _rng.standard_normal(int(d * SR))


def sweep(f0, f1, d, exp=True):
    """sine glide, exponential (constant octaves/second) like the pro zips and chirps"""
    t = _t(d)
    f = f0 * (f1 / f0) ** (t / d) if exp else f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def convex(n, attack, hold, rel):
    """hold then stop: the 'hard end' pro UI sounds have (attack, hold, release in seconds)"""
    t = np.arange(n) / SR
    e = np.clip(t / max(attack, 1e-4), 0, 1)
    return e * np.clip(1 - (t - attack - hold) / max(rel, 1e-4), 0, 1) ** 1.5


def expdec(n, attack, t20):
    """attack then straight-in-dB decay reaching -20 dB at t20"""
    t = np.arange(n) / SR
    return np.clip(t / max(attack, 1e-4), 0, 1) * 10 ** (-np.maximum(0, t - attack) / t20)


def norm(x, peak=1.0): return x / (np.abs(x).max() + 1e-9) * peak


# ---------------------------------------------------------------- recipes
def whoosh():
    """designed swell into a cut: mostly < 150 Hz with a thin air layer, centroid falls ~2 oct, accelerating rise,
    fast fall. 0.7 s, peak at 0.45 s (anchor = peak, placed within +-150 ms of the cut)."""
    d, pk = .7, .45
    t = _t(d); n = len(t)
    rise = np.clip(t / pk, 0, 1) ** 2.2
    fall = 10 ** (-np.maximum(0, t - pk) / .11)
    env = np.where(t < pk, rise, fall)
    body = lp(noise(d), 160) * 1.0 + sweep(110, 45, d) * .35
    # air layer whose band slides down 2 octaves across the pass
    air = np.zeros(n); seg = 6
    for k in range(seg):
        a, b = int(k * n / seg), int((k + 1) * n / seg)
        fc = 2400 * 2 ** (-2 * k / (seg - 1))
        piece = bp(noise(d), fc * .6, fc * 1.6)[a:b]
        w = np.hanning(b - a) if seg > 1 else 1
        air[a:b] += piece * w
    x = body + air * .12
    return norm(x * env), pk, 'whoosh'


def swish():
    """thin flick / text slide: band noise 2-8 kHz sliding down, 0.25 s, peak 0.14 s"""
    d, pk = .25, .14
    t = _t(d)
    env = np.where(t < pk, (t / pk) ** 2, 10 ** (-(t - pk) / .05))
    x = bp(noise(d), 1800, 7500) * .7 + bp(noise(d), 700, 2000) * .3 * (1 - t / d)
    return norm(x * env), pk, 'whoosh'


def riser(d=1.0):
    """three layers: low drone, tonal glide 2->8 kHz, stutter gate speeding up 24->20 ms; concave level (most of the
    rise in the last third); hard end. anchor = END on the cut."""
    t = _t(d); n = len(t)
    drone = lp(noise(d), 400) * .5 + np.sin(2 * np.pi * 55 * t) * .25
    tone = sweep(2000, 8000, d) * .35
    hiss = bp(noise(d), 4000, 11000) * .4
    # accelerating gate: pulse period 24 ms -> 20 ms
    per = .024 - .004 * (t / d)
    ph = np.cumsum(1 / per) / SR
    gate = (np.mod(ph, 1) < .55).astype(float)
    gate = np.convolve(gate, np.ones(48) / 48, 'same')
    lvl = (t / d) ** 3
    x = (drone + tone + hiss * gate) * lvl
    x[-int(.004 * SR):] *= np.linspace(1, 0, int(.004 * SR))
    return norm(x), d, 'riser'


def impact():
    """sub body ~80 Hz that swells in ~60 ms under a broadband transient, granular low rumble tail (grains every
    ~28 ms, slowing), then a HARD gate at 0.9 s. anchor = the body peak, on the cut (the attack leads it)."""
    d, pk = 1.0, .07
    t = _t(d); n = len(t)
    body = np.sin(2 * np.pi * np.cumsum(82 * (1 - .12 * t / d)) / SR)
    benv = np.clip(t / pk, 0, 1) ** 1.5 * 10 ** (-np.maximum(0, t - pk) / .55)
    trans = np.zeros(n); k = int(.012 * SR); trans[:k] = noise(.012) * np.linspace(1, 0, k) ** 2
    grains = np.zeros(n); g = 0.0; per = .028
    while g < d - .05:
        i = int((pk + g) * SR)
        if i >= n: break
        L = min(int(.012 * SR), n - i)
        grains[i:i + L] += noise(L / SR)[:L] * np.hanning(L) * 10 ** (-(g) / .9)
        g += per; per *= 1.03
    rumble = lp(grains, 220) * .9
    x = body * benv * 1.0 + trans * .35 + rumble * .5
    gt = int(.9 * SR); x[gt:] *= np.linspace(1, 0, n - gt) ** 3
    return norm(x), pk, 'impact'


def sub_drop():
    """64 -> 44 Hz tone entering on the cut with a bright click, blooms ~0.35 s after, 40 dB/s decay. anchor = onset."""
    d = 1.2; t = _t(d); n = len(t)
    f = 64 * (44 / 64) ** np.clip(t / .75, 0, 1)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR)
    env = np.clip(t / .35, 0, 1) ** .8 * 10 ** (-np.maximum(0, t - .35) * 2)
    click = np.zeros(n); k = int(.006 * SR); click[:k] = hp(noise(.006), 2000)[:k] * np.linspace(1, 0, k)
    return norm(tone * env + click * .25), 0.0, 'impact'


def pop_in():
    """an element popping in: thump at ~105 Hz (almost all < 150 Hz) + a short 1-10 kHz tick 30 dB down,
    0.18 s, attack 14 ms, convex. anchor = onset, landing 25-40 ms after the element appears."""
    d = .18; t = _t(d); n = len(t)
    thump = np.sin(2 * np.pi * np.cumsum(125 * (1 - .25 * t / d)) / SR) * convex(n, .014, .03, .09)
    tick = bp(noise(d), 1000, 10000) * convex(n, .001, .012, .018)
    return norm(thump + tick * .045), 0.0, 'pop'


def pop():
    """chirp pop: 20 ms blip at 3 kHz, then a sine falling 9.8 kHz -> 350 Hz in 110 ms, loudest mid-sweep. anchor = onset"""
    pre = np.sin(2 * np.pi * 3000 * _t(.02)) * np.hanning(int(.02 * SR))
    ch = sweep(9800, 350, .11)
    n = len(ch); tt = np.arange(n) / SR
    e = np.exp(-((tt - .045) / .03) ** 2)
    x = np.concatenate([pre * .45, ch * e])
    return norm(lp(x, 9000)), 0.0, 'pop'


def blip():
    """box-gated tonal blip: 1.2 kHz + harmonics, 70 ms, 2 ms attack, 7 ms release. anchor = onset"""
    d = .07; t = _t(d); n = len(t)
    x = np.sin(2 * np.pi * 1200 * t) + .35 * np.sin(2 * np.pi * 2400 * t) + .15 * np.sin(2 * np.pi * 3600 * t)
    e = np.clip(t / .002, 0, 1) * np.clip((d - t) / .007, 0, 1)
    return norm(x * e), 0.0, 'ui'


def ding(step=0):
    """notification: struck tone 2.0 kHz with an inharmonic partial at 3.4x, 0.3 s, t20 ~35 ms, convex, nothing < 500 Hz.
    successive dings step up a semitone (step). anchor = onset"""
    f = 1900 * 2 ** (step / 12)
    d = .3; t = _t(d); n = len(t)
    x = np.sin(2 * np.pi * f * t) + .45 * np.sin(2 * np.pi * f * 3.4 * t) * expdec(n, .001, .02)
    e = expdec(n, .003, .09) * convex(n, .001, .2, .08)
    return norm(hp(x * e, 600)), 0.0, 'ui'


def tick():
    """hover tick: 2-12 kHz noise, 30 ms, peak falling as it decays, nothing < 500 Hz. anchor = onset"""
    d = .035; n = int(d * SR)
    x = bp(noise(d), 3500, 12000) * .6 + bp(noise(d), 2000, 6000) * .4 * np.linspace(0, 1, n)
    return norm(x * convex(n, .001, .006, .02)), 0.0, 'ui'


def click():
    """bright UI click / 'tink': attack < 3 ms, t20 ~10 ms, centroid 5-10 kHz with a tonal partial. anchor = onset"""
    d = .05; t = _t(d); n = len(t)
    x = bp(noise(d), 4000, 10000) * .6 + np.sin(2 * np.pi * 6200 * t) * .5
    return norm(x * expdec(n, .0008, .012)), 0.0, 'ui'


def typing(keys=6):
    """designed typing: each key HP noise 3-12 kHz (nothing < 2 kHz), attack 3 ms, t20 ~15 ms, convex; spacing
    jittered 62-148 ms (~11 keys/s), levels jittered. anchor = onset of the first key"""
    out = []
    for k in range(keys):
        d = .065; n = int(d * SR)
        key = bp(noise(d), 3000, 11500, 6) * convex(n, .003, .01, .03) * _rng.uniform(.7, 1.0)
        gap = int(_rng.uniform(.062, .148) * SR) - n
        out += [key, np.zeros(max(0, gap))]
    return norm(np.concatenate(out)), 0.0, 'ui'


def zip_up():
    """tonal sweep into a cut: ~100 Hz -> 1.5 kHz in 0.2 s (+20 oct/s) with a few harmonics; ends ON the cut.
    sits low (+7..9 dB over the bed, i.e. quieter than hits). anchor = end"""
    d = .2; t = _t(d); n = len(t)
    f = 100 * 15 ** (t / d)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + .3 * np.sin(2 * ph) + .12 * np.sin(3 * ph)
    e = np.clip(t / .03, 0, 1) * np.clip((d - t) / .006, 0, 1)
    return norm(x * e), d, 'zip'


def zip_down():
    """fast downward zip across a cut: 7.2 kHz -> 420 Hz in 60 ms; the 'twist' accent. anchor = its peak on the cut"""
    d = .07; t = _t(d); n = len(t)
    x = sweep(7200, 420, d)
    e = np.clip(t / .008, 0, 1) * np.clip((d - t) / .01, 0, 1)
    return norm(x * e), .02, 'zip'


def sting():
    """logo / end sting: falling chirp 1.5 kHz -> 150 Hz in 85 ms landing on a 72 Hz hum (harmonics to ~160 Hz)
    sinking 0.6 oct, rings ~0.8 s, concave tail. anchor = onset (just after the last cut)"""
    ch = sweep(1500, 150, .085) * np.hanning(int(.085 * SR)) ** .3
    d = .9; t = _t(d); n = len(t)
    f = 72 * 2 ** (-.6 * t / d)
    ph = 2 * np.pi * np.cumsum(f) / SR
    hum = (np.sin(ph) + .5 * np.sin(2 * ph) + .25 * np.sin(3 * ph)) * expdec(n, .01, .35)
    x = np.zeros(len(ch) + n); x[:len(ch)] += ch * .6; x[len(ch) - int(.01 * SR):len(ch) - int(.01 * SR) + n] += hum
    return norm(x), 0.0, 'impact'


def downlifter():
    """energy falling away: noise + tone sliding down over 1 s. anchor = onset"""
    d = 1.0; t = _t(d); n = len(t)
    x = bp(noise(d), 300, 3000) * .5 + sweep(900, 120, d) * .5
    return norm(x * (1 - t / d) ** 2 * np.clip(t / .02, 0, 1)), 0.0, 'riser'


def cash():
    """'cha-ching': two notification dings a fifth apart, the second 70 ms later. anchor = onset"""
    a, _, _ = ding(0); b, _, _ = ding(7)
    x = np.zeros(len(a) + int(.07 * SR)); x[:len(a)] += a; x[int(.07 * SR):] += b * .8
    return norm(x), 0.0, 'ui'


def glitch():
    """sparse crackle then a bright decorrelated stutter speeding up 32 -> 22 ms; ends ON the cut. anchor = end"""
    d = .55; n = int(d * SR); x = np.zeros(n)
    for _ in range(10):
        i = _rng.integers(0, int(.2 * SR)); x[i:i + 60] += hp(noise(60 / SR), 4000)[:60] * .4
    p, per = .2, .032
    while p < d - .01:
        i = int(p * SR); L = int(.012 * SR)
        x[i:i + L] += bp(noise(L / SR), 2000, 14000)[:L] * np.hanning(L)
        p += per; per = max(.022, per - .0015)
    return norm(x), d, 'ui'


# names used by the reel templates -> recipes. Old names keep working with the new sounds.
RECIPES = {
    'whoosh': whoosh, 'swish': swish, 'riser': riser, 'boom': impact, 'impact': impact, 'subdrop': sub_drop,
    'thud': pop_in, 'popin': pop_in, 'pop': pop, 'blip': blip, 'ding': ding, 'tick': tick, 'click': click,
    'type': typing, 'zip': zip_up, 'zipdown': zip_down, 'crack': zip_down, 'sting': sting, 'fall': downlifter,
    'cash': cash, 'glitch': glitch, 'gameover': downlifter,
}
# level of each role relative to the others (accents loudest, UI detail quietest, zips low: earshot study)
ROLE_GAIN = {'impact': 1.0, 'whoosh': .8, 'riser': .7, 'pop': .55, 'zip': .45, 'ui': .4}


def render(name, step=0):
    fn = RECIPES.get(name)
    if fn is None: return None
    x, anchor, role = fn(step) if fn is ding else fn()
    return x * ROLE_GAIN[role], anchor, role
