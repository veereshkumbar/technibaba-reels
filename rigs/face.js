// Shared face parts for the TechniBaba rigs: eyes (6 states), brows, 8 mouth visemes. Colours come from TOKENS.
const FACE = (() => {
  const C = TOKENS.color, INK = C.ink;
  const DEFS = `<radialGradient id="gSkin" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="${C.skinLight}"/><stop offset=".7" stop-color="${C.skin}"/><stop offset="1" stop-color="${C.skinDark}"/></radialGradient>
<radialGradient id="gFace" cx="40%" cy="35%" r="80%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e6ddcb"/></radialGradient>
<linearGradient id="gNavy" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${C.navy2}"/><stop offset="1" stop-color="#0c0a30"/></linearGradient>
<linearGradient id="gTopB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8ff5cf"/><stop offset="1" stop-color="${C.mintDark}"/></linearGradient>
<linearGradient id="gTopC" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffbd7f"/><stop offset="1" stop-color="${C.friendTopDark}"/></linearGradient>
<linearGradient id="gPantC" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4c6c9a"/><stop offset="1" stop-color="#2b4366"/></linearGradient>
<filter id="fRigSoft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="fRigGlow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="14"/></filter>`;
  // eyes: st.expr.eye in open | wide | arc | lid | side ; st.blink ; st.look (-1..1)
  function eyes(st, lidFill) {
    const e = st.blink ? 'blink' : st.expr.eye, look = st.look; let o = '';
    [-42, 42].forEach(x => {
      if (e == 'blink') { o += `<path d="M${x - 20},-8 Q${x},2 ${x + 20},-8" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`; return; }
      if (e == 'arc') { o += `<path d="M${x - 19},-4 Q${x},-28 ${x + 19},-4" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>`; return; }
      const ry = e == 'wide' ? 33 : 24, rx = e == 'wide' ? 25 : 20, pr = e == 'wide' ? 8 : 11, px = x + (e == 'side' ? 11 : look * 8), py = e == 'side' ? -4 : -6;
      o += `<ellipse cx="${x}" cy="-10" rx="${rx}" ry="${ry}" fill="#fff" stroke="${INK}" stroke-width="5"/><circle cx="${px}" cy="${py}" r="${pr}" fill="${INK}"/><circle cx="${px + 3}" cy="${py - 4}" r="3.5" fill="#fff"/>`;
      if (e == 'lid' || e == 'side') o += `<path d="M${x - rx - 3},${e == 'side' ? -16 : -12} L${x + rx + 3},${e == 'side' ? -16 : -12} L${x + rx + 3},${-10 - ry - 4} L${x - rx - 3},${-10 - ry - 4}Z" fill="${lidFill}" stroke="${INK}" stroke-width="5"/>`;
    });
    return o;
  }
  // brows: st.brow = [left angle, right angle, lift]
  function brows(st, col) {
    const [aL, aR, lift] = st.brow, y = -50 + lift; let o = '';
    [[-1, aL], [1, aR]].forEach(([s, a]) => { o += `<g transform="translate(${s * 40},${y}) rotate(${s * a})"><path d="M-24,0 Q0,-7 24,0" fill="none" stroke="${col}" stroke-width="11" stroke-linecap="round"/></g>`; });
    return o;
  }
  // mouth: 8 visemes + resting shapes per expression
  function mouth(st, cy = 48) {
    const v = st.viseme, D = '#5a1a22', TG = '#e76f6f', W = '#fff';
    const open = (rx, ry, o = {}) => `<ellipse cx="0" cy="${cy}" rx="${rx}" ry="${ry}" fill="${D}" stroke="${INK}" stroke-width="5"/>${o.teeth ? `<rect x="${-rx * .7}" y="${cy - ry + 2}" width="${rx * 1.4}" height="${Math.min(8, ry * .5)}" rx="3" fill="${W}"/>` : ''}${o.tongue ? `<ellipse cx="0" cy="${cy + ry * (o.tongue == 'up' ? -.15 : .45)}" rx="${rx * .55}" ry="${Math.max(4, ry * .35)}" fill="${TG}"/>` : ''}`;
    switch (v) {
      case 'AI': return open(30, 22, {teeth: 1, tongue: 'down'});
      case 'E': return open(32, 12, {teeth: 1});
      case 'O': return open(17, 21, {});
      case 'U': return open(11, 13, {});
      case 'MBP': return `<path d="M-22,${cy} L22,${cy}" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`;
      case 'FV': return open(25, 9, {teeth: 1}) + `<path d="M-20,${cy + 7} Q0,${cy + 13} 20,${cy + 7}" fill="none" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>`;
      case 'L': return open(24, 15, {teeth: 1, tongue: 'up'});
    }
    switch (st.expr.mouth) {
      case 'grin': return `<path d="M-30,${cy - 8} Q0,${cy + 30} 30,${cy - 8} Z" fill="${D}" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/><rect x="-20" y="${cy - 6}" width="40" height="7" rx="3" fill="${W}"/>`;
      case 'o': return open(14, 18, {});
      case 'smirk': return `<path d="M-22,${cy + 4} Q4,${cy + 10} 26,${cy - 8}" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
      case 'flat': return `<path d="M-20,${cy + 4} L20,${cy + 4}" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
      case 'wavy': return `<path d="M-22,${cy + 4} q11,-10 22,0 t22,0" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
      default: return `<path d="M-22,${cy} Q0,${cy + 14} 22,${cy}" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>`;
    }
  }
  const limb = (sx, sy, s, a1, a2, l1, l2) => { const R = RIG.R, ex = sx + s * Math.sin(R(a1)) * l1, ey = sy + Math.cos(R(a1)) * l1, hx = ex + s * Math.sin(R(a2)) * l2, hy = ey + Math.cos(R(a2)) * l2; return [[sx, sy], [ex, ey], [hx, hy]]; };
  // arm drawn as an arc through the elbow (never a straight stick)
  const arm = (P, sleeve, hand, extra = '') => { const d = `M${P[0][0]},${P[0][1]} Q${P[1][0]},${P[1][1]} ${P[2][0]},${P[2][1]}`, d2 = `M${P[0][0]},${P[0][1]} L${P[1][0]},${P[1][1]} L${P[2][0]},${P[2][1]}`; return `<path d="${d2}" fill="none" stroke="${INK}" stroke-width="31" stroke-linecap="round" stroke-linejoin="round"/><path d="${d2}" fill="none" stroke="${sleeve}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/><circle cx="${P[2][0]}" cy="${P[2][1]}" r="19" fill="${hand}" stroke="${INK}" stroke-width="6"/>${extra}`; };
  const handExtra = (pose, h, hand) => pose == 'thumb' ? `<rect x="${h[0] - 9}" y="${h[1] - 48}" width="18" height="36" rx="9" fill="${hand}" stroke="${INK}" stroke-width="5"/>` : pose == 'stop' ? `<rect x="${h[0] - 22}" y="${h[1] - 40}" width="44" height="50" rx="14" fill="${hand}" stroke="${INK}" stroke-width="5"/>` : pose == 'count' ? [-14, 0, 14].map((dx, k) => `<rect x="${h[0] + dx - 6}" y="${h[1] - 46 + Math.abs(dx) * .4}" width="12" height="34" rx="6" fill="${hand}" stroke="${INK}" stroke-width="4"/>`).join('') : pose == 'point' ? `<rect x="${h[0] + 8}" y="${h[1] - 7}" width="38" height="14" rx="7" fill="${hand}" stroke="${INK}" stroke-width="4"/>` : '';
  return {DEFS, eyes, brows, mouth, limb, arm, handExtra};
})();
