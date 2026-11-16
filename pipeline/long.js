// Long-form 16:9 guide video layout (load after stage.js). Content panel on the left, Baba and Chotu full-body on the right,
// captions under the panel. The panel content is data-driven from SPEC (made by pipeline/long_build.py from a spec.json),
// so a scheduled run only writes the spec, never drawing code.
const LONG = true, W16 = 1920, H16 = 1080;
const PAN = {x0: 60, y0: 60, x1: 1260, y1: 900}, SEAM = 1000, HOOK_END = 0, PW = PAN.x1 - PAN.x0, PH = PAN.y1 - PAN.y0;
const spAt = () => 1, capY = () => 990, camG = () => '';
const SPOS16 = {c: {x: 1420, y: 1068}, b: {x: 1700, y: 1068}};
const talkAmt = (who, f) => { let a = 0; for (const b of BT) if (b.who == who) a = Math.max(a, Math.min(sm(f, b.f0 - 3, 6), 1 - sm(f, b.f1, 8))); return a; };
const hitAmt = (who, f) => { let a = 0; BT.forEach(b => { if (b.hit && b.who == who) { const d = f - b.hit.f; if (d >= -2 && d < 30) a = Math.max(a, d < 22 ? E.bouncy((d + 2) / 7) : 1 - sm(f, b.hit.f + 22, 8)); } }); return a; };
function charLayer(f) {
  let o = '';
  const order = ['c', 'b'].sort((a, b) => (talkAmt(a, f) + 2 * hitAmt(a, f)) - (talkAmt(b, f) + 2 * hitAmt(b, f)));
  order.forEach(w => { const s = (w == 'b' ? 1.12 : 1.0) * (1 + .04 * talkAmt(w, f) + .1 * hitAmt(w, f)); o += CAST[w].draw(f, {x: SPOS16[w].x, y: SPOS16[w].y, s, flip: w == 'b', phone: false, glow: w == 'b' ? hitAmt('b', f) : 0}); });
  return o; }
function strip(f) { const t = f / FPS, R = RIG.R; let o = `<defs><radialGradient id="lbg" cx="78%" cy="45%" r="75%"><stop offset="0" stop-color="#2a2370"/><stop offset=".55" stop-color="${C.navy}"/><stop offset="1" stop-color="#090822"/></radialGradient><radialGradient id="spot" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="${C.mint}" stop-opacity=".28"/><stop offset="1" stop-color="${C.mint}" stop-opacity="0"/></radialGradient></defs><rect width="1920" height="1080" fill="url(#lbg)"/>`;
  for (let r = 0; r < 9; r++) for (let q = 0; q < 17; q++) o += `<circle cx="${40 + q * 118}" cy="${40 + r * 128}" r="4" fill="${C.mint}" opacity=".10"/>`;
  for (let k = 0; k < 10; k++) o += `<path d="M1560,520 L${1560 + Math.cos(R(k * 36 + t * 6)) * 900},${520 + Math.sin(R(k * 36 + t * 6)) * 900} L${1560 + Math.cos(R(k * 36 + 14 + t * 6)) * 900},${520 + Math.sin(R(k * 36 + 14 + t * 6)) * 900}Z" fill="#fff" opacity=".025"/>`;
  o += `<ellipse cx="1560" cy="640" rx="420" ry="420" fill="url(#spot)"/><ellipse cx="1560" cy="1072" rx="380" ry="34" fill="#000" opacity=".35"/><rect x="1290" y="1066" width="630" height="14" fill="${C.mint}" opacity=".6"/>`;
  o += `<text x="1890" y="58" text-anchor="end" font-family="Pop" font-weight="900" font-size="30" fill="#fff" opacity=".85">Techni<tspan fill="${C.mint}">Baba</tspan></text><text x="1890" y="88" text-anchor="end" font-family="Pop" font-weight="600" font-size="20" fill="#fff" opacity=".55">technibaba.com/guides</text>`;
  return o; }
const PBG = () => '';
function overlay(f) { return ''; }
// ---------- data-driven panel ----------
const T16 = (x, y, s, txt, o = {}) => `<text x="${x}" y="${y}" text-anchor="${o.a || 'start'}" font-family="${o.font || 'Pop'}" font-weight="${o.w || 900}" font-size="${s}" fill="${o.fill || INK}" ${o.extra || ''}>${String(txt).replace(/&/g, '&amp;').replace(/</g, '&lt;')}</text>`;
const card16 = (x, y, w, h, p, inner, o = {}) => p <= 0 ? '' : `<g transform="translate(${x + w / 2},${y + h / 2}) rotate(${(1 - Math.min(p, 1)) * -5}) scale(${p}) translate(${-w / 2},${-h / 2})" opacity="${clamp(p * 2)}"><rect x="6" y="9" width="${w}" height="${h}" rx="${o.r || 22}" fill="#000" opacity=".16"/><rect width="${w}" height="${h}" rx="${o.r || 22}" fill="${o.fill || '#fff'}" stroke="${o.stroke || INK}" stroke-width="${o.sw || 5}"/>${inner}</g>`;
const wrap16 = (s, n) => { const w = String(s).split(' '), out = ['']; w.forEach(x => { if ((out[out.length - 1] + ' ' + x).trim().length > n) out.push(x); else out[out.length - 1] = (out[out.length - 1] + ' ' + x).trim(); }); return out; };
const SCN = {}; SPEC.scenes.forEach((s, k) => { SCN[s.id] = s; s.k = k; });
// reveal frame of item j in scene s: first line of the scene whose `show` exceeds j
function revealF(s, j) { let show = 0; for (const i of s.lines) { const L = SPEC.lines[i]; if (L.show != null) show = L.show; if (show > j) return BT[i].f0 + (L.show != null ? 8 + 4 * Math.max(0, j - (show - (L.show_new || 1))) : 0); } return 1e9; }
SPEC.scenes.forEach(s => (s.items || []).forEach((_, j) => { const r = revealF(s, j); if (r < 1e8) sfx(r, s.type == 'recap' ? 'ding' : 'pop'); }));
SPEC.scenes.forEach(s => { if (s.type == 'phone') (s.path || []).forEach((_, j) => { const r = revealF(s, j); if (r < 1e8) sfx(r, 'tick'); }); });
function head16(s, f) { const n = SPEC.scenes.length; let o = `<rect x="${PAN.x0}" y="${PAN.y0}" width="${PW}" height="${PH}" fill="${s.bg || '#f6f4ff'}"/><rect x="${PAN.x0}" y="${PAN.y0}" width="${PW}" height="116" fill="${C.navy}"/>`;
  let x = PAN.x0 + 44; if (s.chip) { const w = s.chip.length * 21 + 56; o += `<rect x="${x}" y="${PAN.y0 + 30}" width="${w}" height="58" rx="29" fill="${s.color || C.mint}"/>` + T16(x + w / 2, PAN.y0 + 71, 30, s.chip, {a: 'middle'}); x += w + 24; }
  o += T16(x, PAN.y0 + 74, 40, s.head || s.title, {fill: '#fff'});
  for (let k = 0; k < n; k++) o += `<circle cx="${PAN.x1 - 40 - (n - 1 - k) * 26}" cy="${PAN.y0 + 58}" r="8" fill="${k <= s.k ? C.mint : '#4b4a86'}"/>`;
  return o; }
const X0 = PAN.x0 + 50, Y0 = PAN.y0 + 160, IW = PW - 100;
const tick16 = (x, y, p, col) => p <= 0 ? '' : `<g transform="translate(${x},${y}) scale(${Math.min(1.15, p)})"><circle r="30" fill="${col}" stroke="${INK}" stroke-width="5"/><path d="M-14,1 l10,11 l20,-24" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>`;
const cross16 = (x, y, p) => p <= 0 ? '' : `<g transform="translate(${x},${y}) scale(${Math.min(1.15, p)})"><circle r="30" fill="${C.laptopRed}" stroke="${INK}" stroke-width="5"/><path d="M-12,-12 L12,12 M12,-12 L-12,12" stroke="#fff" stroke-width="8" stroke-linecap="round"/></g>`;
function content(n, f) { const s = SCN[n], t = f / FPS; let o = head16(s, f); const P = j => pop(f, revealF(s, j), 10), it = s.items || [];
  if (s.type == 'title') {
    const p0 = pop(f, SCF[n].s + 4, 12), p1 = pop(f, SCF[n].s + 12, 12), p2 = pop(f, SCF[n].s + 20, 12);
    wrap16(s.title, 20).forEach((ln, k) => o += `<g opacity="${clamp(p0 * 2)}" transform="translate(0,${(1 - p0) * 30})">` + T16(X0, Y0 + 70 + k * 92, 84, ln) + `</g>`);
    if (s.sub) o += `<g opacity="${clamp(p1 * 2)}">` + T16(X0, Y0 + 300, 38, s.sub, {w: 700, fill: '#5b5b78'}) + `</g>`;
    (s.chips || []).forEach((c, k) => o += card16(X0 + k * 540, Y0 + 400, 500, 150, pop(f, SCF[n].s + 20 + k * 8, 12), `<rect x="0" y="0" width="22" height="150" rx="11" fill="${k ? C.laptopRed : C.mint}"/>` + T16(52, 66, 40, c.split('|')[0], {font: 'Mono', w: 700}) + T16(52, 116, 30, c.split('|')[1] || '', {w: 800, fill: k ? C.laptopRed : C.mintDark}), {rot: k ? 2 : -2}));
  }
  if (s.type == 'points') it.forEach((txt, j) => { const p = P(j), y = Y0 + j * 158, bad = /NAKLI|KHATRA|chor|BHAAG/i.test(txt);
    o += card16(X0, y, IW, 132, p, `<circle cx="70" cy="66" r="40" fill="${bad ? C.laptopRed : (s.color || C.mint)}" stroke="${INK}" stroke-width="5"/>` + T16(70, 82, 44, j + 1, {a: 'middle', fill: bad ? '#fff' : INK}) + wrap16(txt, 46).slice(0, 2).map((ln, k, a) => T16(140, 66 + (k - (a.length - 1) / 2) * 48 + 15, 40, ln, {w: 800})).join(''), {stroke: bad && p > 0 ? C.laptopRed : INK}); });
  if (s.type == 'compare') { const cw = (IW - 40) / 2, L = it.filter(x => x.side == 'L'), R2 = it.filter(x => x.side == 'R');
    [[L, 0, s.left || 'THEEK', C.mintDark], [R2, 1, s.right || 'BHAAG', C.laptopRed]].forEach(([arr, c, lab, col]) => { const x = X0 + c * (cw + 40), ph = pop(f, revealF(s, it.indexOf(arr[0])), 10);
      o += card16(x, Y0, cw, 96, ph, `<rect width="${cw}" height="96" rx="22" fill="${col}"/>` + T16(cw / 2, 64, 46, lab, {a: 'middle', fill: '#fff'}));
      arr.forEach((x2, k) => { const j = it.indexOf(x2), p = P(j); o += card16(x, Y0 + 126 + k * 150, cw, 124, p, (c ? cross16(60, 62, p) : tick16(60, 62, p, C.mintDark)) + wrap16(x2.text, 20).slice(0, 2).map((ln, q, a) => T16(110, 62 + (q - (a.length - 1) / 2) * 44 + 14, 38, ln, {w: 800})).join(''), {stroke: c ? C.laptopRed : INK}); }); }); }
  if (s.type == 'browser') { const pb = pop(f, SCF[n].s + 6, 12), warn = P(0), go = P(1), no = P(2);
    o += card16(X0, Y0, IW, 600, pb, `<rect width="${IW}" height="90" rx="22" fill="#e9ebf2"/><rect y="50" width="${IW}" height="40" fill="#e9ebf2"/>${[0, 1, 2].map(k => `<circle cx="${40 + k * 36}" cy="45" r="12" fill="${[C.laptopRed, C.captionKeyword, C.mint][k]}"/>`).join('')}<rect x="170" y="18" width="${IW - 210}" height="56" rx="28" fill="#fff" stroke="${INK}" stroke-width="4"/><rect x="180" y="26" width="200" height="40" rx="20" fill="${C.laptopRed}"/>` + T16(280, 55, 24, 'Not secure', {a: 'middle', fill: '#fff'}) + T16(400, 56, 26, s.url || 'airport-wifi-login.com', {font: 'Mono', w: 700, fill: '#7a7f92'})
      + (warn > 0 ? `<g transform="translate(${IW / 2},210) scale(${Math.min(1.1, warn)})"><path d="M0,-80 L88,66 L-88,66Z" fill="${C.captionKeyword}" stroke="${INK}" stroke-width="8" stroke-linejoin="round"/><rect x="-8" y="-34" width="16" height="56" rx="8" fill="${INK}"/><circle cx="0" cy="44" r="10" fill="${INK}"/></g>` + T16(IW / 2, 350, 46, 'Your connection is not private', {a: 'middle', fill: C.laptopRed}) : '')
      + (go > 0 ? `<g transform="translate(${IW / 2 - 230},470) scale(${(1 + .05 * Math.sin(t * 8)) * Math.min(1, go)})"><rect x="-190" y="-50" width="380" height="100" rx="50" fill="${C.mint}" stroke="${INK}" stroke-width="6"/>` + T16(0, 16, 42, 'Go back', {a: 'middle'}) + `</g>` : '')
      + (no > 0 ? `<g transform="translate(${IW / 2 + 230},470)"><rect x="-170" y="-50" width="340" height="100" rx="50" fill="#e9ebf2" stroke="#9aa0b4" stroke-width="5"/>` + T16(0, 14, 38, 'Proceed', {a: 'middle', fill: '#9aa0b4'}) + cross16(150, -40, no) + `</g>` : ''), {r: 26}); }
  if (s.type == 'phone') { const pp = pop(f, SCF[n].s + 6, 12), path = s.path || [], px = X0 + 10, py = Y0 - 20;
    o += card16(px, py, 420, 680, pp, `<rect x="16" y="16" width="388" height="648" rx="34" fill="#f3f4f8"/><rect x="160" y="28" width="100" height="22" rx="11" fill="${INK}"/>` + T16(46, 110, 34, s.app || 'Settings') + path.map((x, j) => { const a = f >= revealF(s, j), cur = a && !(f >= revealF(s, j + 1)); return `<g transform="translate(36,${150 + j * 108})"><rect width="348" height="88" rx="18" fill="${cur ? (j == path.length - 1 ? C.laptopRed : C.mint) : '#fff'}" stroke="${a ? INK : '#d4d6e0'}" stroke-width="${a ? 4 : 3}"/>` + T16(20, 56, x.length > 16 ? 25 : 30, x, {w: 800, fill: cur && j == path.length - 1 ? '#fff' : (a ? INK : '#9aa0b4')}) + T16(330, 56, 32, j < path.length - 1 ? '›' : '', {a: 'end', fill: '#9aa0b4'}) + `</g>`; }).join(''), {r: 44, sw: 7});
    it.forEach((txt, j) => { const p = P(path.length + j); o += card16(X0 + 480, Y0 + 40 + j * 180, IW - 480, 148, p, `<circle cx="66" cy="74" r="38" fill="${C.mint}" stroke="${INK}" stroke-width="5"/>` + T16(66, 90, 40, j + 2, {a: 'middle'}) + wrap16(txt, 24).slice(0, 2).map((ln, k, a) => T16(128, 74 + (k - (a.length - 1) / 2) * 46 + 14, 38, ln, {w: 800})).join('')); }); }
  if (s.type == 'recap') it.forEach((txt, j) => { const p = pop(f, SCF[n].s + 6 + j * 4, 10), tk = P(j), y = Y0 + j * 150;
    o += card16(X0, y, IW, 124, p, `<rect x="30" y="27" width="70" height="70" rx="16" fill="${tk > 0 ? C.mint : '#f3f4f8'}" stroke="${INK}" stroke-width="5"/>` + (tk > 0 ? `<path d="M46,62 l15,16 l28,-32" fill="none" stroke="${INK}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="70" stroke-dashoffset="${70 * (1 - clamp(tk))}"/>` : '') + T16(130, 78, 44, txt, {w: 800})); });
  if (s.type == 'outro') { const p0 = pop(f, SCF[n].s + 6, 12), p1 = P(0), p2 = P(1);
    o += card16(X0 + 60, Y0 + 30, IW - 120, 190, p0, T16((IW - 120) / 2, 80, 36, 'Poora guide yahan', {a: 'middle', w: 700, fill: '#5b5b78'}) + T16((IW - 120) / 2, 150, 66, 'technibaba.com/guides', {a: 'middle', font: 'Mono', w: 700, fill: C.navy}), {fill: C.captionKeyword});
    o += card16(X0 + 60, Y0 + 280, 480, 130, p1, `<rect width="480" height="130" rx="22" fill="${C.laptopRed}"/><path d="M60,40 L110,65 L60,90Z" fill="#fff"/>` + T16(280, 82, 46, 'SUBSCRIBE', {a: 'middle', fill: '#fff'}), {stroke: INK});
    o += card16(X0 + IW - 540, Y0 + 280, 480, 130, p2, T16(240, 60, 30, 'Instagram', {a: 'middle', w: 700, fill: '#5b5b78'}) + T16(240, 106, 44, '@technibaba', {a: 'middle'}));
    if (s.sub) o += `<g opacity="${clamp(p2 * 2)}">` + T16(X0 + IW / 2, Y0 + 520, 40, s.sub, {a: 'middle', w: 800, fill: C.navy}) + `</g>`; }
  return o; }
