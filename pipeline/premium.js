// Premium look (PREMIUM_STYLE.md). Include after split.js in page_tpl.html as __PREMIUM__ and put an empty file `layout_premium` in WORKDIR.
// Monochrome: near-black, graphite cards, hairline borders, white type. One highlight style: a white pill with black text.
// Colour is a signal, not decoration: mint only for "safe/right", red only for "danger/wrong", never both large on one page.
const PR = {bg: '#0A0A0C', panel: '#0E0E11', card: '#17171B', card2: '#1E1E23', line: '#2A2A31', line2: '#3B3B44', text: '#F4F4F6', muted: '#8C8C96', dim: '#55555E', good: '#6EE7B7', bad: '#FF6B6B', font: 'Inter'};
const pin = (f, a, d = 9) => f < a ? 0 : E.snappy(Math.min(1, (f - a) / d));     // entrance 0..1, no overshoot
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
// text. o: a (anchor), w (weight), fill, ls (letter-spacing), op
const PT = (x, y, size, txt, o = {}) => `<text x="${x}" y="${y}" text-anchor="${o.a || 'middle'}" font-family="Inter" font-weight="${o.w || 600}" font-size="${size}" fill="${o.fill || PR.text}" letter-spacing="${o.ls || -size * .02}" opacity="${o.op ?? 1}" style="white-space:pre">${esc(txt)}</text>`;
const PLABEL = (x, y, txt, o = {}) => PT(x, y, o.size || 24, txt.toUpperCase(), {a: o.a || 'middle', w: 600, fill: o.fill || PR.muted, ls: 3});
// approximate Inter widths (px per em) good enough for layout
const tw = (s, size, w = 600) => { let n = 0; for (const ch of String(s)) n += ch == ' ' ? .27 : /[il.,'!|:;]/.test(ch) ? .27 : /[mwMW]/.test(ch) ? .86 : /[A-Z0-9₹]/.test(ch) ? .66 : .56; return n * size * (w >= 700 ? 1.04 : 1); };
// headline with *keyword* parts drawn as white pills. Words reveal one by one from frame a (every `step` frames); unrevealed words are dim.
function PHEAD(x, y, size, text, f, a, o = {}) {
  const parts = text.split('*'), words = []; parts.forEach((p, k) => p.split(' ').filter(Boolean).forEach(w => words.push({w, kw: k % 2 == 1})));
  const gap = size * .27, widths = words.map(z => tw(z.w, size, 700) + (z.kw ? size * .5 : 0)), W = widths.reduce((s, v) => s + v, 0) + gap * (words.length - 1);
  let cx = o.a == 'start' ? x : x - W / 2, out = ''; const step = o.step ?? 3;
  words.forEach((z, k) => { const p = o.instant ? 1 : pin(f, a + k * step, 6), wv = widths[k];
    if (z.kw) out += `<g opacity="${.25 + .75 * p}"><rect x="${cx}" y="${y - size * .86}" width="${wv}" height="${size * 1.14}" rx="${size * .18}" fill="${PR.text}" opacity="${p}"/>${PT(cx + wv / 2, y, size, z.w, {w: 700, fill: p > .5 ? PR.bg : PR.dim})}</g>`;
    else out += PT(cx + wv / 2, y, size, z.w, {w: 700, fill: p > .5 ? PR.text : PR.dim, op: .35 + .65 * p});
    cx += wv + gap; });
  return out; }
// card: centre x,y. o.on = highlighted (white hairline + soft glow), o.state = 'good'|'bad' for a coloured hairline
function PCARD(x, y, w, h, p, inner, o = {}) {
  if (p <= 0) return '';
  const st = o.state == 'good' ? PR.good : o.state == 'bad' ? PR.bad : o.on ? PR.text : PR.line, sw = o.on || o.state ? 2.5 : 2;
  return `<g transform="translate(${x},${y + (1 - p) * 26}) scale(${.965 + .035 * p})" opacity="${p}">` +
    (o.on ? `<rect x="${-w / 2 - 6}" y="${-h / 2 - 6}" width="${w + 12}" height="${h + 12}" rx="${(o.r || 26) + 6}" fill="${PR.text}" opacity=".07" filter="url(#pglow)"/>` : '') +
    `<rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h}" rx="${o.r || 26}" fill="${o.fill || PR.card}" stroke="${st}" stroke-width="${sw}"/>` +
    `<rect x="${-w / 2 + 2}" y="${-h / 2 + 2}" width="${w - 4}" height="${Math.min(60, h / 3)}" rx="${(o.r || 26) - 2}" fill="url(#psheen)"/>` + inner + `</g>`; }
const PPILL = (x, y, txt, p = 1, o = {}) => { const s = o.size || 30, w = tw(txt, s, 700) + s * 1.1; return `<g opacity="${p}" transform="translate(${x},${y})"><rect x="${-w / 2}" y="${-s * .95}" width="${w}" height="${s * 1.5}" rx="${s * .75}" fill="${o.solid ? PR.text : 'none'}" stroke="${o.col || PR.line2}" stroke-width="2"/>${PT(0, s * .08, s, txt, {w: 700, fill: o.solid ? PR.bg : (o.col || PR.text)})}</g>`; };
const PARROW = (x1, y, x2, p = 1, col = PR.dim) => p <= 0 ? '' : `<g opacity="${p}"><line x1="${x1}" y1="${y}" x2="${x1 + (x2 - x1) * p}" y2="${y}" stroke="${col}" stroke-width="3"/><path d="M${x1 + (x2 - x1) * p - 12},${y - 9} l12,9 l-12,9" fill="none" stroke="${col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>`;
const PSTRIKE = (x1, y, x2, p, col = PR.bad) => p <= 0 ? '' : `<line x1="${x1}" y1="${y}" x2="${x1 + (x2 - x1) * p}" y2="${y}" stroke="${col}" stroke-width="5" stroke-linecap="round"/>`;
// thin line icons, 100-unit box centred on 0,0; s = scale (1 = 100 px)
const ICONS = {
  phone: '<rect x="-24" y="-44" width="48" height="88" rx="10"/><line x1="-8" y1="-34" x2="8" y2="-34"/><circle cx="0" cy="33" r="3"/>',
  lock: '<rect x="-30" y="-6" width="60" height="46" rx="8"/><path d="M-18,-6 v-14 a18,18 0 0 1 36,0 v14"/><circle cx="0" cy="16" r="5"/>',
  shield: '<path d="M0,-42 L34,-28 V2 C34,24 18,38 0,44 C-18,38 -34,24 -34,2 V-28Z"/><path d="M-13,1 l9,10 l18,-20"/>',
  user: '<circle cx="0" cy="-18" r="17"/><path d="M-32,40 C-32,14 -16,6 0,6 C16,6 32,14 32,40"/>',
  hacker: '<path d="M-34,40 C-34,10 -20,-4 0,-4 C20,-4 34,10 34,40"/><path d="M-26,-6 C-30,-40 30,-40 26,-6"/><line x1="-14" y1="-16" x2="-4" y2="-16"/><line x1="4" y1="-16" x2="14" y2="-16"/>',
  app: '<rect x="-34" y="-34" width="68" height="68" rx="16"/><path d="M-12,-2 l10,10 l14,-16"/>',
  rupee: '<path d="M-18,-30 H20 M-18,-14 H20 M-6,-30 C14,-30 14,2 -6,2 H-18 L16,34"/>',
  arrowIn: '<path d="M0,-34 V24 M-20,6 L0,26 L20,6"/><line x1="-30" y1="38" x2="30" y2="38"/>',
  arrowOut: '<path d="M0,26 V-32 M-20,-14 L0,-34 L20,-14"/><line x1="-30" y1="38" x2="30" y2="38"/>',
  pin: '<rect x="-34" y="-40" width="68" height="80" rx="10"/>' + [0, 1, 2].map(r => [0, 1, 2].map(c => `<circle cx="${-16 + c * 16}" cy="${-20 + r * 16}" r="3"/>`).join('')).join('') + '<line x1="-16" y1="30" x2="16" y2="30"/>',
  bell: '<path d="M-26,18 V-4 a26,26 0 0 1 52,0 V18 L32,26 H-32Z"/><path d="M-8,34 a8,8 0 0 0 16,0"/>',
  chat: '<path d="M-38,-26 H38 V18 H-6 L-22,34 V18 H-38Z"/>',
  call: '<path d="M-30,-34 L-14,-34 L-6,-14 L-16,-6 C-10,8 0,18 14,24 L22,14 L40,22 V36 C10,40 -36,0 -30,-34Z"/>',
  check: '<path d="M-24,2 l16,16 l32,-36"/>',
  cross: '<path d="M-20,-20 L20,20 M20,-20 L-20,20"/>',
  warn: '<path d="M0,-38 L40,32 H-40Z"/><line x1="0" y1="-10" x2="0" y2="10"/><circle cx="0" cy="21" r="2.5"/>',
  wifi: '<path d="M-40,-8 a58,58 0 0 1 80,0 M-26,8 a36,36 0 0 1 52,0 M-12,23 a16,16 0 0 1 24,0"/><circle cx="0" cy="36" r="3"/>',
  code: '<path d="M-16,-22 L-38,0 L-16,22 M16,-22 L38,0 L16,22"/>',
};
const PICON = (name, x, y, s = 1, col = PR.text, sw = 4) => `<g transform="translate(${x},${y}) scale(${s})" fill="none" stroke="${col}" stroke-width="${sw / s}" stroke-linecap="round" stroke-linejoin="round">${ICONS[name] || ''}</g>`;
// round icon badge used inside cards
const PBADGE = (name, x, y, col = PR.text, r = 40) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${PR.card2}" stroke="${PR.line2}" stroke-width="2"/>` + PICON(name, x, y, r / 62, col, 3.5);
// panel backdrop: hairline grid + viewfinder corners (drawn in full-frame coordinates)
function PGRID(x0, y0, x1, y1, op = .045) { let o = ''; for (let x = x0; x <= x1; x += 54) o += `<line x1="${x}" y1="${y0}" x2="${x}" y2="${y1}" stroke="#fff" stroke-width="1" opacity="${op}"/>`; for (let y = y0; y <= y1; y += 54) o += `<line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="#fff" stroke-width="1" opacity="${op}"/>`; return o; }
function PCORNERS(x0, y0, x1, y1, L = 34, op = .55) { const c = (x, y, dx, dy) => `<path d="M${x},${y + dy * L} V${y} H${x + dx * L}" fill="none" stroke="#fff" stroke-width="3" opacity="${op}"/>`; return c(x0, y0, 1, 1) + c(x1, y0, -1, 1) + c(x0, y1, 1, -1) + c(x1, y1, -1, -1); }
const PDEFS = `<filter id="pglow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="14"/></filter><linearGradient id="psheen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><radialGradient id="pspot" cx=".5" cy=".55" r=".6"><stop offset="0" stop-color="#26262E"/><stop offset="1" stop-color="${PR.bg}"/></radialGradient>`;
// default bottom stage: dark studio with a soft spotlight (reels may override strip())
function strip(f) { return `<rect x="-700" y="-1500" width="2500" height="4000" fill="${PR.bg}"/><ellipse cx="540" cy="1520" rx="760" ry="560" fill="url(#pspot)"/>` + PGRID(-700, 1060, 1800, 2600, .03); }
// old-engine (page.html) versions of the panel and caption, matching hf_premium.html
function panelLayer(f, contentFn) {
  if (f < HOOK_END) return '';
  const pp = E.smooth(Math.min(1, (f - HOOK_END) / 12)), ty = (1 - pp) * 60, n = sceneAt(f);
  let o = `<g transform="translate(0,${ty})" opacity="${pp}"><rect x="-40" y="-1300" width="1160" height="${SEAM + 1300}" fill="${PR.bg}"/>` + PGRID(0, 0, 1080, SEAM - 4) + `<rect x="0" y="${SEAM - 1}" width="1080" height="2" fill="#fff" opacity=".12"/>`;
  o += `<rect x="${PAN.x0}" y="${PAN.y0}" width="${PAN.x1 - PAN.x0}" height="${PAN.y1 - PAN.y0}" rx="36" fill="${PR.panel}" stroke="${PR.line}" stroke-width="2"/><g clip-path="url(#pclip)">${contentFn(n, f)}</g>` + PCORNERS(PAN.x0 + 18, PAN.y0 + 18, PAN.x1 - 18, PAN.y1 - 18);
  return o + `</g>`; }
function caption(f, y = 1440) { let c = null; for (const x of CAPS) if (f >= x.f && f < x.end) c = x; if (!c) return '';
  const p = pin(f, c.f, 6), raw = c.text.replace(/\*/g, ''), size = Math.min(58, 760 / Math.max(1, tw(raw, 1, 700)));
  return `<g opacity="${p}" transform="translate(0,${(1 - p) * 14})">` + PHEAD(540, y + size * .3, size, c.text, f, c.f, {instant: true}) + `</g>`; }
function wipe() { return ''; }
