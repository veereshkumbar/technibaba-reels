"""Generate a royalty-free lo-fi / chill-hop bed (original, synthesized).
usage: python3 lofi.py OUT.wav SECONDS [bpm=88] [seed=1] [mood=warm|bright|night]"""
import sys, numpy as np, soundfile as sf
OUT, DUR = sys.argv[1], float(sys.argv[2]); BPM = float(sys.argv[3]) if len(sys.argv) > 3 else 88
SEED = int(sys.argv[4]) if len(sys.argv) > 4 else 1; MOOD = sys.argv[5] if len(sys.argv) > 5 else 'warm'
SR = 44100; rng = np.random.default_rng(SEED); N = int((DUR + 1) * SR); beat = 60 / BPM
L = np.zeros(N); Rt = np.zeros(N)
def put(x, t, g=1.0, pan=0.0):
    i = int(t * SR); j = min(N, i + len(x))
    if j <= i: return
    L[i:j] += x[:j - i] * g * (1 - max(0, pan)); Rt[i:j] += x[:j - i] * g * (1 + min(0, pan))
def adsr(n, a=.01, r=.3):
    e = np.ones(n); na = max(1, int(a * SR)); e[:na] = np.linspace(0, 1, na)
    nr = min(n, int(r * SR)); e[-nr:] *= np.linspace(1, 0, nr) ** 2; return e
def epiano(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * h * t * (1 + d)) for h, a, d in [(1, 1, 0), (1, .5, .003), (2, .35, 0), (3, .12, 0), (4, .05, 0)])
    x *= np.exp(-t * 1.6) * (1 + .15 * np.sin(2 * np.pi * 4.5 * t))  # decay + tremolo
    return x * adsr(n, .008, .25) * .16
def kick():
    n = int(.35 * SR); t = np.arange(n) / SR; f = 50 + 90 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * .9
def snare():
    n = int(.25 * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    x = np.convolve(x, np.ones(6) / 6, 'same') * np.exp(-t * 18) * .35 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 25) * .2
    return x
def hat():
    n = int(.08 * SR); x = rng.standard_normal(n); x = x - np.convolve(x, np.ones(4) / 4, 'same')
    return x * np.exp(-np.arange(n) / SR * 60) * .12
def bass(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + .25 * np.sin(4 * np.pi * f * t)) * adsr(n, .02, .15) * .32
CH = {'warm': [[57, 60, 64, 67, 71], [53, 57, 60, 64, 67], [55, 59, 62, 65, 69], [52, 55, 59, 62, 67]],   # Am9 Fmaj7 G7 Em7
      'bright': [[60, 64, 67, 71, 74], [57, 60, 64, 67, 71], [53, 57, 60, 64, 69], [55, 59, 62, 65, 69]],
      'night': [[50, 53, 57, 60, 64], [46, 50, 53, 57, 60], [48, 52, 55, 58, 62], [45, 48, 52, 55, 60]]}[MOOD]
mf = lambda m: 440 * 2 ** ((m - 69) / 12)
bar = 4 * beat; t = 0.0; k = 0
while t < DUR + 1:
    ch = CH[k % 4]
    for q, m in enumerate(ch):  # slightly strummed chord, held 1 bar
        put(epiano(mf(m), bar * .98), t + q * .012 + rng.uniform(0, .006), 1, pan=(q - 2) * .15)
    for b in range(4):
        bt = t + b * beat
        if b in (0, 2) or (b == 3 and k % 2): put(kick(), bt + (beat / 2 if b == 3 else 0), .8)
        if b in (1, 3): put(snare(), bt + .012, .7)
        for e in range(2):  # swung 8th hats
            put(hat(), bt + e * beat * .58, .9 if e == 0 else .6, pan=.3)
    put(bass(mf(ch[0] - 12), beat * 1.6), t, 1); put(bass(mf(ch[0] - 12), beat * 1.2), t + beat * 2.5, .8)
    t += bar; k += 1
# sidechain pump + vinyl crackle + soft lowpass
pump = np.ones(N); kb = int(beat * SR)
for i in range(0, N, kb): seg = min(kb, N - i); pump[i:i + seg] = 1 - .25 * np.exp(-np.arange(seg) / SR * 7)
crackle = (rng.random(N) > .9993) * rng.standard_normal(N) * .08 + rng.standard_normal(N) * .004
mix = np.stack([L * pump + crackle, Rt * pump + crackle], 1)
for c in range(2): mix[:, c] = np.convolve(mix[:, c], np.ones(3) / 3, 'same')
n = int(DUR * SR); mix = mix[:n]; f = int(1.5 * SR); mix[-f:] *= np.linspace(1, 0, f)[:, None]
mix /= np.abs(mix).max() + 1e-9; sf.write(OUT, mix * .8, SR); print('music', OUT, round(DUR, 1), 's')
