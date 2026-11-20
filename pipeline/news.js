// TechniBaba Daily news bulletin (vertical). Load after stage.js. Data-driven from SPEC (pipeline/news_build.py).
// Modes per scene: 'split' (hook: story card on top, Baba reacting below), 'anchor' (Baba at the desk, title overlay),
// 'card' (full-screen story card with Baba picture-in-picture). Every story = a numbered card.
const NEWS = true, NS = {}; SPEC.scenes.forEach((s, k) => { NS[s.id] = s; s.k = k; });
const HOOK_END = 0, spAt = () => 1, camG = () => '';
const TOTAL_STORIES = SPEC.scenes.filter(s => s.story).length;
const T9 = (x, y, s, txt, o = {}) => `<text x="${x}" y="${y}" text-anchor="${o.a || 'start'}" font-family="${o.font || 'Pop'}" font-weight="${o.w || 900}" font-size="${s}" fill="${o.fill || '#fff'}" ${o.extra || ''}>${String(txt).replace(/&/g, '&amp;').replace(/</g, '&lt;')}</text>`;
const wrap9 = (s, n) => { const w = String(s).split(' '), out = ['']; w.forEach(x => { if ((out[out.length - 1] + ' ' + x).trim().replace(/\*/g, '').length > n) out.push(x); else out[out.length - 1] = (out[out.length - 1] + ' ' + x).trim(); }); return out; };
const sceneStartF = n => SCF[n].s, sceneD = (n, f) => f - SCF[n].s;
// ---------- icon library (flat, bold, our own art) ----------
const ICON = {
 gamepad: c => `<rect x="-170" y="-80" width="340" height="170" rx="85" fill="${c}" stroke="#14124a" stroke-width="10"/><rect x="-118" y="-20" width="70" height="22" rx="8" fill="#14124a"/><rect x="-94" y="-44" width="22" height="70" rx="8" fill="#14124a"/><circle cx="80" cy="-24" r="17" fill="#e5383b"/><circle cx="116" cy="10" r="17" fill="#ffd23f"/><circle cx="44" cy="10" r="17" fill="#5de0b0"/>`,
 space: c => `<circle r="120" fill="none" stroke="${c}" stroke-width="6" stroke-dasharray="14 18"/><rect x="-40" y="-26" width="80" height="52" rx="8" fill="#e8e8f0" stroke="#14124a" stroke-width="8"/><path d="M-40,0 L-150,-30 M40,0 L150,30" stroke="#e8e8f0" stroke-width="10"/><circle cx="0" cy="-70" r="42" fill="#ffd23f" stroke="#14124a" stroke-width="8"/><path d="M0,-28 L0,-26" stroke="#14124a" stroke-width="8"/>`,
 forum: c => `<rect x="-160" y="-110" width="250" height="160" rx="30" fill="${c}" stroke="#14124a" stroke-width="10"/><path d="M-110,50 L-130,100 L-60,50Z" fill="${c}" stroke="#14124a" stroke-width="10" stroke-linejoin="round"/><rect x="-60" y="-30" width="230" height="140" rx="30" fill="#fff" stroke="#14124a" stroke-width="10"/><path d="M-10,-0 L120,80 M120,0 L-10,80" stroke="#e5383b" stroke-width="16" stroke-linecap="round"/>`,
 car: c => `<path d="M-180,40 L-150,-40 Q-140,-70 -100,-70 L100,-70 Q140,-70 150,-40 L180,40 Z" fill="${c}" stroke="#14124a" stroke-width="10" stroke-linejoin="round"/><rect x="-200" y="30" width="400" height="70" rx="24" fill="${c}" stroke="#14124a" stroke-width="10"/><circle cx="-120" cy="110" r="38" fill="#14124a"/><circle cx="120" cy="110" r="38" fill="#14124a"/><rect x="-110" y="-56" width="220" height="70" rx="12" fill="#bfe9ff" stroke="#14124a" stroke-width="8"/>`,
 server: c => `${[0, 1, 2].map(k => `<rect x="-150" y="${-120 + k * 84}" width="300" height="68" rx="14" fill="${c}" stroke="#14124a" stroke-width="10"/><circle cx="-110" cy="${-86 + k * 84}" r="10" fill="#5de0b0"/><rect x="-70" y="${-92 + k * 84}" width="150" height="12" rx="6" fill="#14124a" opacity=".5"/>`).join('')}`,
 headphones: c => `<path d="M-120,40 Q-120,-130 0,-130 Q120,-130 120,40" fill="none" stroke="#14124a" stroke-width="26"/><rect x="-160" y="20" width="70" height="120" rx="30" fill="${c}" stroke="#14124a" stroke-width="10"/><rect x="90" y="20" width="70" height="120" rx="30" fill="${c}" stroke="#14124a" stroke-width="10"/>`,
 plane: c => `<path d="M-200,10 L120,-20 Q190,-24 200,0 Q190,24 120,20 L-200,-10Z" fill="#e8e8f0" stroke="#14124a" stroke-width="10"/><path d="M0,-10 L-80,-130 L-40,-130 L60,-14Z M0,10 L-80,130 L-40,130 L60,14Z" fill="${c}" stroke="#14124a" stroke-width="10" stroke-linejoin="round"/>`,
 phone: c => `<rect x="-90" y="-160" width="180" height="320" rx="30" fill="#14124a"/><rect x="-74" y="-136" width="148" height="270" rx="14" fill="${c}"/><rect x="-30" y="-150" width="60" height="10" rx="5" fill="#333"/>`,
 chip: c => `<rect x="-110" y="-110" width="220" height="220" rx="24" fill="${c}" stroke="#14124a" stroke-width="10"/><rect x="-56" y="-56" width="112" height="112" rx="12" fill="#14124a"/>${[-70, -24, 24, 70].map(p => `<path d="M${p},-110 L${p},-150 M${p},110 L${p},150 M-110,${p} L-150,${p} M110,${p} L150,${p}" stroke="#14124a" stroke-width="12" stroke-linecap="round"/>`).join('')}`,
 ai: c => `<circle r="130" fill="${c}" stroke="#14124a" stroke-width="10"/>${T9(0, 40, 120, 'AI', {a: 'middle', fill: '#14124a'})}`,
 cricket: c => `<circle cx="70" cy="-40" r="56" fill="#e5383b" stroke="#14124a" stroke-width="10"/><path d="M30,-80 Q70,-40 110,-2" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="10 8"/><rect x="-170" y="-20" width="70" height="200" rx="20" transform="rotate(-30 -135 80)" fill="${c}" stroke="#14124a" stroke-width="10"/>`,
 film: c => `<rect x="-160" y="-60" width="320" height="200" rx="16" fill="#14124a"/><path d="M-160,-60 L-170,-130 L160,-140 L170,-70Z" fill="${c}" stroke="#14124a" stroke-width="10" stroke-linejoin="round"/>${[0, 1, 2, 3].map(k => `<path d="M${-130 + k * 80},-128 L${-90 + k * 80},-72" stroke="#14124a" stroke-width="18"/>`).join('')}`,
 rupee: c => `<circle r="130" fill="${c}" stroke="#14124a" stroke-width="10"/>${T9(0, 50, 150, '₹', {a: 'middle', fill: '#14124a'})}`,
 globe: c => `<circle r="130" fill="${c}" stroke="#14124a" stroke-width="10"/><ellipse rx="56" ry="130" fill="none" stroke="#14124a" stroke-width="8"/><path d="M-130,0 L130,0 M-110,-66 L110,-66 M-110,66 L110,66" stroke="#14124a" stroke-width="8"/>`,
};
const CAT = {TECH: '#5de0b0', AI: '#9b8cff', GAMING: '#ff6b9a', SPACE: '#4cc9f0', APPS: '#ffd23f', BUSINESS: '#ffb04c', SPORTS: '#7ee081', FILMS: '#ff9b6b', INDIA: '#ffb04c', WORLD: '#4cc9f0'};
// ---------- backgrounds ----------
function studio(f) { const t = f / FPS, R = RIG.R; let o = `<defs><radialGradient id="nbg" cx="50%" cy="35%" r="80%"><stop offset="0" stop-color="#2a2370"/><stop offset=".6" stop-color="#14124a"/><stop offset="1" stop-color="#07061c"/></radialGradient></defs><rect width="1080" height="1920" fill="url(#nbg)"/>`;
  for (let k = 0; k < 7; k++) { const x = 80 + k * 160; o += `<rect x="${x}" y="${380 + 60 * Math.sin(k + t * .3)}" width="90" height="${300 + 120 * Math.sin(k * 1.7)}" rx="8" fill="#4cc9f0" opacity=".06"/>`; }
  for (let r = 0; r < 14; r++) for (let q = 0; q < 10; q++) o += `<circle cx="${50 + q * 110}" cy="${40 + r * 140}" r="3.5" fill="${C.mint}" opacity=".12"/>`;
  o += `<circle cx="540" cy="760" r="${520 + 10 * Math.sin(t * 2)}" fill="${C.mint}" opacity=".05"/>`;
  return o; }
function desk(f, y = 1600) { return `<path d="M-40,${y} L1120,${y} L1120,1940 L-40,1940Z" fill="#0d0b2e"/><rect x="-40" y="${y - 8}" width="1160" height="16" fill="${C.mint}"/><rect x="330" y="${y + 60}" width="420" height="96" rx="18" fill="#14124a" stroke="${C.mint}" stroke-width="4"/>` + T9(540, y + 122, 44, 'TECHNIBABA DAILY', {a: 'middle', fill: '#fff', extra: 'letter-spacing="3"'}); }
function mic(x, y, s) { return `<g transform="translate(${x},${y}) scale(${s})"><path d="M60,260 L20,120 L-10,40" fill="none" stroke="#1a1a24" stroke-width="18" stroke-linecap="round"/><rect x="-46" y="-110" width="92" height="170" rx="46" fill="#22222e" stroke="#000" stroke-width="6"/>${[0, 1, 2, 3, 4, 5].map(k => `<line x1="-36" y1="${-84 + k * 22}" x2="36" y2="${-84 + k * 22}" stroke="#3a3a4a" stroke-width="5"/>`).join('')}<rect x="-54" y="40" width="108" height="26" rx="10" fill="#111"/></g>`; }
function baba(f, mode, k) { // k = 0..1 blend toward 'card' pip
  let s = lerp(2.4, 1.05, k), x = lerp(540, 930, k), y = lerp(2230, 2010, k);
  if (mode == 'split') { s = 1.75; x = 540; y = 2240; }
  let o = CAST.b.draw(f, {x, y, s, flip: false, glow: 0});
  if (mode == 'split') o += mic(700, 1560, .8); else if (k < .99) o += `<g opacity="${1 - k}">` + mic(lerp(770, 980, k), lerp(1330, 1700, k), lerp(1.05, .5, k)) + `</g>`;
  return o; }
// ---------- cards ----------
function headline(x, y, w, txt, size, maxc) { const lines = wrap9(txt, maxc); let o = '', yy = y; lines.forEach(ln => { let xx = x + 26, parts = ln.split('*'); const tw = ln.replace(/\*/g, '').length * size * .56 + 52; o += `<rect x="${x}" y="${yy - size * .95}" width="${Math.min(w, tw)}" height="${size * 1.32}" fill="#0b0b12"/>`; let segs = ''; parts.forEach((p, i) => { const pw = p.length * size * .56; if (i % 2 && p) segs += `<rect x="${xx - 6}" y="${yy - size * .86}" width="${pw + 12}" height="${size * 1.14}" fill="#e5383b"/>`; segs += T9(xx, yy, size, p, {fill: '#fff', extra: 'xml:space="preserve"'}); xx += pw; }); o += segs; yy += size * 1.36; }); return {o, h: yy - y}; }
// the whole headline is drawn as ONE text run per line with tspans, so widths are right
function headline2(x, y, w, txt, size, maxc) { const lines = wrap9(txt, maxc); let o = '', yy = y, open = false;
  lines.forEach(ln => { const plain = ln.replace(/\*/g, ''); o += `<rect x="${x}" y="${yy - size * .98}" width="${Math.min(w, plain.length * size * .61 + size * 1.3)}" height="${size * 1.34}" rx="6" fill="#0b0b12"/>`;
    const parts = ln.split('*'); let ts = ''; parts.forEach((p, i) => { if (i > 0) open = !open; if (p) ts += `<tspan fill="${open ? '#ffd23f' : '#fff'}">${p.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</tspan>`; });
    o += `<text x="${x + 28}" y="${yy}" font-family="Pop" font-weight="900" font-size="${size}" xml:space="preserve">${ts}</text>`; yy += size * 1.4; }); return {o, h: yy - y}; }
function storyCard(s, f, x0, y0, w, h) { const d = sceneD(s.id, f), col = CAT[s.kicker] || C.mint, t = f / FPS;
  let o = `<g><rect x="${x0 + 10}" y="${y0 + 14}" width="${w}" height="${h}" rx="34" fill="#000" opacity=".35"/><rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="34" fill="#f4f1ff" stroke="#0b0b12" stroke-width="8"/>`;
  // illustration panel
  const ih = h * .54; o += `<rect x="${x0 + 24}" y="${y0 + 24}" width="${w - 48}" height="${ih}" rx="24" fill="${col}" opacity=".22"/>`;
  for (let k = 0; k < 9; k++) o += `<path d="M${x0 + w / 2},${y0 + 24 + ih / 2} L${x0 + w / 2 + Math.cos(RIG.R(k * 40 + t * 12)) * 900},${y0 + ih / 2 + Math.sin(RIG.R(k * 40 + t * 12)) * 900} L${x0 + w / 2 + Math.cos(RIG.R(k * 40 + 16 + t * 12)) * 900},${y0 + ih / 2 + Math.sin(RIG.R(k * 40 + 16 + t * 12)) * 900}Z" fill="#fff" opacity=".18" clip-path="url(#illo${s.k})"/>`;
  const ip = pop(f, SCF[s.id].s + 4, 12), bob = 8 * Math.sin(t * 2.2);
  o += `<clipPath id="illo${s.k}"><rect x="${x0 + 24}" y="${y0 + 24}" width="${w - 48}" height="${ih}" rx="24"/></clipPath>`;
  o += `<g transform="translate(${x0 + w * (s.stat ? .3 : .5)},${y0 + 24 + ih / 2 + bob}) scale(${ip * (s.stat ? 1.35 : 1.75)})">${(ICON[s.icon] || ICON.globe)(col)}</g>`;
  if (s.stat) { const sp = pop(f, SCF[s.id].s + 12, 12); o += `<g transform="translate(${x0 + w * .7},${y0 + 24 + ih / 2}) rotate(-4) scale(${sp * 1.15})"><rect x="-190" y="-90" width="380" height="180" rx="26" fill="#0b0b12" stroke="${col}" stroke-width="8"/>` + T9(0, 22, s.stat.length > 7 ? 64 : 84, s.stat, {a: 'middle', fill: col}) + (s.statSub ? T9(0, 70, 28, s.statSub, {a: 'middle', fill: '#fff', w: 700}) : '') + `</g>`; }
  // kicker + counter
  const kp = pop(f, SCF[s.id].s + 2, 10);
  o += `<g transform="translate(${x0 + 44},${y0 + 60}) scale(${kp})"><rect x="0" y="-38" width="${s.kicker.length * 26 + 50}" height="58" rx="29" fill="#0b0b12"/>` + T9(25, 4, 30, s.kicker, {fill: col, extra: 'letter-spacing="2"'}) + `</g>`;
  if (s.story) o += `<g transform="translate(${x0 + w - 44},${y0 + 60}) scale(${kp})"><rect x="-150" y="-38" width="150" height="58" rx="29" fill="#e5383b"/>` + T9(-75, 6, 32, `${s.story}/${TOTAL_STORIES}`, {a: 'middle'}) + `</g>`;
  // headline (words appear fast, like a news graphic)
  const hp = clamp((d - 6) / 8);
  const big = h > 1000, hs = big ? (s.headline.length > 60 ? 64 : 72) : (s.headline.length > 60 ? 50 : 56); const H = headline2(x0 + 30, y0 + 24 + ih + (big ? 130 : 100), w - 60, s.headline, hs, Math.floor((w - 100) / (hs * .57)));
  o += `<g opacity="${hp}" transform="translate(${(1 - E.snappy(hp)) * -40},0)">${H.o}</g>`;
  if (s.source) o += T9(x0 + 34, y0 + h - 30, 24, 'Source: ' + s.source, {fill: '#5b5b78', w: 700});
  return o + `</g>`; }
// ---------- per-frame composition ----------
const MODE = n => NS[n].mode;
function pipK(f) { const n = sceneAt(f), m = MODE(n), d = sceneD(n, f), k = ORDER.indexOf(n), prev = k ? MODE(ORDER[k - 1]) : m;
  const target = m == 'card' ? 1 : 0, from = prev == 'card' ? 1 : 0; return from == target ? target : lerp(from, target, E.smooth(clamp(d / 10))); }
function frame16(f) { const n = sceneAt(f), s = NS[n], d = sceneD(n, f), t = f / FPS; let o = studio(f);
  if (s.mode == 'split') { // hook: story card on top, Baba below
    o += baba(f, 'split', 0) + desk(f, 1720);
    const cp = E.bouncy(clamp(d / 12)); o += `<g transform="translate(0,${(1 - cp) * -900})">` + storyCard(s, f, 50, 70, 980, 900) + `</g>`;
    if (s.banner) { const bp = pop(f, SCF[n].s + 10, 10); o += `<g transform="translate(540,1010) scale(${bp})"><rect x="-470" y="-50" width="940" height="100" rx="14" fill="#0b0b12"/>` + T9(0, 18, 46, s.banner, {a: 'middle', fill: '#fff'}) + `</g>`; }
    return o; }
  const k = pipK(f);
  if (k < 1) o += `<g opacity="${1 - k}">` + desk(f) + `</g>`;
  if (s.mode == 'card' || k > 0) { const cn = s.mode == 'card' ? s : NS[ORDER[ORDER.indexOf(n) - 1]], cd = sceneD(cn.id, f);
    const slide = s.mode == 'card' ? 1 - E.snappy(clamp(cd / 9)) : E.smooth(clamp(d / 10)) * -1;
    if (cn.mode == 'card') o += `<g transform="translate(${slide * 1100},0)">` + storyCard(cn, f, 50, 140, 980, 1100) + `</g>`; }
  o += baba(f, s.mode, k);
  if (s.mode == 'anchor' && s.title) { const first = s.k == 0, tp = first ? 1 + .04 * Math.sin(t * 3) : pop(f, SCF[n].s + 6, 12), lines = s.title.split('|');
    o += `<g transform="translate(540,330) rotate(-3) scale(${tp})">` + lines.map((ln, i) => { const parts = ln.split('*'); let ts = ''; parts.forEach((p, j) => { if (p) ts += `<tspan fill="${j % 2 ? '#e5383b' : '#ffd23f'}">${p}</tspan>`; }); return `<text x="0" y="${i * 112}" text-anchor="middle" font-family="Pop" font-weight="900" font-size="104" stroke="#0b0b12" stroke-width="14" paint-order="stroke">${ts}</text>`; }).join('') + `</g>`; }
  if (s.mode == 'anchor' && s.list) s.list.forEach((it, i) => { const lp = s.k == 0 ? (f < 2 ? 1 : pop(f, -6 + i * 3, 8)) : pop(f, SCF[n].s + 14 + i * 5, 9); o += `<g transform="translate(${i % 2 ? 560 : 60},${600 + Math.floor(i / 2) * 92}) scale(${lp})"><rect x="0" y="-44" width="${it.length * 24 + 110}" height="70" rx="35" fill="#0b0b12" stroke="${C.mint}" stroke-width="4"/>` + T9(26, 3, 32, `${i + 1}`, {fill: C.mint}) + T9(66, 3, 30, it, {w: 800}) + `</g>`; });
  if (s.mode == 'anchor' && s.k == 0 && SPEC.dateLabel) o += `<g transform="translate(540,505)"><rect x="-170" y="-34" width="340" height="56" rx="28" fill="#e5383b"/>` + T9(0, 6, 30, SPEC.dateLabel, {a: 'middle'}) + `</g>`;
  // lower third (date + handle) except in split
  o += `<g><rect x="0" y="0" width="1080" height="92" fill="#0b0b12" opacity=".75"/>` + T9(40, 60, 34, 'TECHNIBABA DAILY', {fill: C.mint, extra: 'letter-spacing="2"'}) + T9(1040, 60, 30, SPEC.dateLabel || '', {a: 'end', w: 700}) + `</g>`;
  return o; }
// sound: whoosh on card in/out, ding on each new story number, pop on title/list
SPEC.scenes.forEach(s => { const f0 = SCF[s.id].s; if (s.mode == 'card' || s.mode == 'split') { sfx(f0, 'whoosh'); sfx(f0 + 4, 'ding'); if (s.stat) sfx(f0 + 12, 'pop'); }
  if (s.mode == 'anchor' && s.title && s.k > 0) { sfx(f0 + 4, 'riser'); sfx(f0 + 8, 'boom'); } if (s.k == 0) sfx(0, 'boom'); if (s.list) s.list.forEach((_, i) => sfx(f0 + 14 + i * 5, 'pop')); });
// API used by the HyperFrames page
const PAN = {x0: 0, y0: 0, x1: 1080, y1: 1920}, SEAM = 1500;
function strip(f) { return ''; } function overlay(f) { return ''; } function charLayer(f) { return ''; } function content(n, f) { return ''; }
