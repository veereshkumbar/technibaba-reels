// Shared stage for director-format reels. Needs TOKENS, RIG, makeBaba/makeFriend, BEATS (beats.json).
// Gives: rigs keyed from the beat sheet, eased camera, hit-stop time warp, keyword captions in the title-safe box, scene bounds, SFX cues.
const FPS = TOKENS.fps, C = TOKENS.color, INK = C.ink, E = RIG.ease, clamp = RIG.clamp, lerp = RIG.lerp;
const BT = BEATS.beats, NF = BEATS.total_frames, TOTAL = NF / FPS;
const SFX = []; const sfx = (f, ty) => SFX.push([+(f / FPS).toFixed(3), ty]);
const ORDER = []; BT.forEach(b => { if (!ORDER.includes(b.scene)) ORDER.push(b.scene); });
const SCF = {}; ORDER.forEach((n, k) => { SCF[n] = {s: k == 0 ? 0 : BT.find(b => b.scene == n).f0 - 5}; }); ORDER.forEach((n, k) => { SCF[n].e = k < ORDER.length - 1 ? SCF[ORDER[k + 1]].s : NF; });
const SC = {}; ORDER.forEach(n => { SC[n] = {s: SCF[n].s / FPS, e: SCF[n].e / FPS}; });
const sceneAt = f => { for (let k = ORDER.length - 1; k >= 0; k--) if (f >= SCF[ORDER[k]].s) return ORDER[k]; return ORDER[0]; };
const WF = (i, w) => { const x = BT[i].words.find(x => x.w.startsWith(w)); return x ? x.f : BT[i].f0; };
const pop = (f, a, d = 10) => f < a ? 0 : E.bouncy((f - a) / d), sm = (f, a, d = 12) => E.smooth((f - a) / d), sn = (f, a, d = 10) => f < a ? 0 : E.snappy((f - a) / d);
// ---- rigs, keyed from the beat sheet ----
const CAST = {c: makeFriend(), b: makeBaba()};
BT.forEach(b => { b.keys.forEach(k => { CAST[k.who].pose(k.pose, k.f, {big: k.big}).express(k.expr, k.f, {big: k.big}); if (k.big) sfx(k.f, 'whoosh'); });
  const r = CAST[b.who], V = {r: 'rest', A: 'AI', E: 'E', O: 'O', U: 'U', M: 'MBP', F: 'FV', L: 'L'}; [...b.vis].forEach((ch, k) => r.say(V[ch], b.f0 + k));
  const nx = BT[b.i + 1]; if (!nx || !nx.keys.some(k => k.who == b.who && k.f <= nx.f0)) r.pose('idle', b.f1 + 4); });
// ---- hit-stop ----
const HITS = BT.filter(b => b.hit).map(b => [b.hit.f, b.hit.hold]); HITS.forEach(h => sfx(h[0], 'thud'));
const warp = RIG.timeWarp(HITS);
// ---- camera: eased keys, never linear ----
const POS = {c: {x: 300, y: 1180}, b: {x: 780, y: 1180}}, WIDE = {x: 540, y: 890, z: 1};
const camOf = (cam, who) => cam == 'cu' ? {x: POS[who].x + (who == 'c' ? 40 : -40), y: 820, z: 1.42} : cam == 'boom' ? {x: POS[who].x, y: 760, z: 1.95} : WIDE;
const CAMK = [{f: -99, t: WIDE, d: 1, e: 'smooth'}];
BT.forEach(b => { CAMK.push({f: b.f0 - 2, t: camOf(b.cam, b.who), d: b.cam ? 9 : 12, e: b.cam ? 'snappy' : 'smooth'}); b.cams.forEach(c => CAMK.push({f: c.f - (c.cam == 'boom' ? 2 : 0), t: camOf(c.cam, c.who), d: c.cam == 'boom' ? 5 : 12, e: c.cam == 'boom' ? 'snappy' : 'smooth'})); });
ORDER.slice(1).forEach(n => CAMK.push({f: SCF[n].s, t: WIDE, d: 1, e: 'smooth'}));
CAMK.sort((a, b) => a.f - b.f);
function camAt(f) { let k = 0; for (let i = 0; i < CAMK.length; i++) if (CAMK[i].f <= f) k = i; const K = CAMK[k], P = k ? camRest(k - 1) : WIDE, p = E[K.e]((f - K.f) / K.d);
  let c = {x: lerp(P.x, K.t.x, p), y: lerp(P.y, K.t.y, p), z: lerp(P.z, K.t.z, p)};
  for (const [h] of HITS) { const d = f - h; if (d >= 0 && d < 16) { const a = 16 * Math.exp(-d / 4); c.x += a * Math.sin(d * 2.4); c.y += a * Math.cos(d * 3.1); } }   // impact shake
  c.z *= 1 + .012 * Math.sin(f / FPS * .7); return c; }
function camRest(k) { return CAMK[k].t; }
const camT = c => `translate(540,960) scale(${c.z}) translate(${-c.x},${-c.y})`;
// ---- captions: short keyword lines, one highlighted keyword, inside the title-safe box ----
const CAPS = []; BT.forEach(b => b.caps.forEach(c => CAPS.push({f: c.f, text: c.text, end: b.f1 + 10}))); CAPS.forEach((c, k) => { if (CAPS[k + 1]) c.end = Math.min(c.end, CAPS[k + 1].f); });
function caption(f, y = 1440) { let c = null; for (const x of CAPS) if (f >= x.f && f < x.end) c = x; if (!c) return '';
  const raw = c.text.replace(/\*/g, ''), size = Math.min(72, 800 / (raw.length * .6)), parts = c.text.split('*'), p = pop(f, c.f, 8);
  const w = raw.length * size * .6 + 70, S = TOKENS.frame.safe, x0 = Math.max(S.x0, 540 - w / 2), ww = Math.min(w, S.x1 - S.x0);
  const tsp = parts.map((s, k) => `<tspan fill="${k % 2 ? C.captionKeyword : C.captionText}">${s.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</tspan>`).join('');
  return `<g transform="translate(540,${y}) scale(${.6 + .4 * p}) translate(-540,${-y})" opacity="${clamp(p * 2)}"><rect x="${x0}" y="${y - size * .95}" width="${ww}" height="${size * 1.5}" rx="${size * .4}" fill="${C.captionPlate}" opacity=".86" stroke="${C.mint}" stroke-width="4"/><text x="540" y="${y + size * .13}" text-anchor="middle" font-family="Pop" font-weight="900" font-size="${size}" style="white-space:pre">${tsp}</text></g>`; }
// scene wipe: a mint+navy diagonal band crossing in 10 frames
function wipe(f) { let o = ''; ORDER.slice(1).forEach(n => { const d = f - SCF[n].s + 5; if (d >= 0 && d < 11) { const x = lerp(-1500, 1500, E.smooth(d / 10)); o += `<g transform="translate(${x},0) skewX(-18)"><rect x="-300" y="-100" width="1500" height="2200" fill="${C.navy}"/><rect x="1200" y="-100" width="120" height="2200" fill="${C.mint}"/><rect x="-420" y="-100" width="120" height="2200" fill="${C.laptopRed}"/></g>`; } }); return o; }
ORDER.slice(1).forEach(n => sfx(SCF[n].s - 5, 'whoosh'));
// swap picture at the wipe's midpoint
const sceneShown = f => sceneAt(f + 0);
