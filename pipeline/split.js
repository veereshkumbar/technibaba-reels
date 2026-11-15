// Split layout (load after stage.js): content panel on top, characters waist-up below, captions on the seam.
// The hook (line 1) plays full-screen on the speaker, then the panel drops in. On a hit-stop the speaker grows across the seam.
const PAN = {x0: 72, y0: 150, x1: 1008, y1: 985}, SEAM = 1040, CS = 1.7, FACE_Y = 1400;
const SPOS = {c: {x: 285, y: 2199}, b: {x: 795, y: 2199}};
const HOOK_END = BT[1] ? BT[1].f0 - 3 : 45; sfx(HOOK_END, 'whoosh');
const spAt = f => sn(f, HOOK_END, 10);                       // 0 = full-screen hook, 1 = split
const capY = f => lerp(1440, 1082, spAt(f));
const talkAmt = (who, f) => { let a = 0; for (const b of BT) if (b.who == who) a = Math.max(a, Math.min(sm(f, b.f0 - 3, 6), 1 - sm(f, b.f1, 8))); return a; };
const hitAmt = (who, f) => { let a = 0; BT.forEach(b => { if (b.hit && b.who == who) { const d = f - b.hit.f; if (d >= -2 && d < 30) a = Math.max(a, d < 22 ? E.bouncy((d + 2) / 7) : 1 - sm(f, b.hit.f + 22, 8)); } }); return a; };
const shakeAt = f => { let x = 0, y = 0; for (const [h] of HITS) { const d = f - h; if (d >= 0 && d < 16) { const a = 14 * Math.exp(-d / 4); x += a * Math.sin(d * 2.4); y += a * Math.cos(d * 3.1); } } return [x, y]; };
function charLayer(f, stripFn) {
  const sp = spAt(f), who = BT[0].who, z = lerp(1.08, 1, sp), cx = lerp(SPOS[who].x, 540, sp), cy = lerp(FACE_Y + 20, 960, sp), CY = lerp(1010, 960, sp);
  let o = `<g transform="translate(540,${CY}) scale(${z}) translate(${-cx},${-cy})">` + stripFn(f);
  const order = ['c', 'b'].sort((a, b) => (talkAmt(a, f) + 2 * hitAmt(a, f)) - (talkAmt(b, f) + 2 * hitAmt(b, f)));
  order.forEach(w => { const s = CS * (1 + .05 * talkAmt(w, f) + .14 * hitAmt(w, f)); o += CAST[w].draw(f, {x: SPOS[w].x, y: SPOS[w].y, s, flip: w == 'b', phone: false, glow: w == 'b' ? hitAmt('b', f) : 0}); });
  return o + `</g>`; }
const SPLIT_DEFS = `<clipPath id="pclip"><rect x="${PAN.x0}" y="${PAN.y0}" width="${PAN.x1 - PAN.x0}" height="${PAN.y1 - PAN.y0}" rx="40"/></clipPath>`;
function panelLayer(f, contentFn) {
  if (f < HOOK_END) return '';
  const pp = E.bouncy((f - HOOK_END) / 12), ty = -(1 - pp) * 1150, [sx, sy] = shakeAt(f), n = sceneAt(f), k = ORDER.indexOf(n), d = f - SCF[n].s;
  let inner; if (k > 0 && d < 10) { const e = E.smooth(d / 10); inner = `<g transform="translate(${-1000 * e},0)">${contentFn(ORDER[k - 1], f)}</g><g transform="translate(${1000 * (1 - e)},0)">${contentFn(n, f)}</g>`; } else inner = contentFn(n, f);
  let o = `<g transform="translate(${sx},${ty + sy})"><rect x="-40" y="-1300" width="1160" height="${SEAM + 1300}" fill="${C.navy}"/>`;
  for (let r = 0; r < 9; r++) for (let q = 0; q < 10; q++) o += `<circle cx="${30 + q * 113}" cy="${40 + r * 122}" r="5" fill="${C.mint}" opacity=".13"/>`;
  o += `<rect x="-40" y="${SEAM - 7}" width="1160" height="14" fill="${C.mint}"/><rect x="${PAN.x0 + 10}" y="${PAN.y0 + 14}" width="${PAN.x1 - PAN.x0}" height="${PAN.y1 - PAN.y0}" rx="40" fill="#000" opacity=".35"/>`;
  o += `<g clip-path="url(#pclip)">${inner}</g><rect x="${PAN.x0}" y="${PAN.y0}" width="${PAN.x1 - PAN.x0}" height="${PAN.y1 - PAN.y0}" rx="40" fill="none" stroke="${INK}" stroke-width="7"/>`;
  return o + `</g>`; }
