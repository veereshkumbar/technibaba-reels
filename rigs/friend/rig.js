// Friend rig ("Chotu") — same part list as Baba, contrasting silhouette: round head, red cap, orange tee, no beard.
function makeFriend() {
  const rig = RIG.makeRig('friend'), C = TOKENS.color, INK = C.ink, SKIN = 'url(#gSkin)', HAIR = '#3b2316';
  rig.draw = (f, o = {}) => {
    const st = rig.state(f), s = o.s || 1;
    const L = FACE.limb(-62, -318, -1, st.arms.L[0], st.arms.L[1] + st.handLag, 95, 88), Rr = FACE.limb(62, -318, 1, st.arms.R[0], st.arms.R[1] + st.handLag, 95, 88);
    const sy = 1 + st.sq, sx = 1 - st.sq * .6;
    let g = `<g transform="translate(${o.x || 0},${(o.y || 0) - st.hop}) scale(${o.flip ? -s : s},${s})">`;
    g += `<ellipse cx="0" cy="8" rx="${130 - st.hop * .6}" ry="24" fill="#000" opacity=".3" filter="url(#fRigSoft)"/><g transform="scale(${sx},${sy})">`;
    [-30, 30].forEach(x => { g += `<path d="M${x},-160 L${x},-18" stroke="${INK}" stroke-width="44" stroke-linecap="round"/><path d="M${x},-160 L${x},-18" stroke="url(#gPantC)" stroke-width="32" stroke-linecap="round"/><ellipse cx="${x + 14}" cy="-6" rx="34" ry="17" fill="#f1f1f1" stroke="${INK}" stroke-width="6"/>`; });
    g += `<g transform="translate(0,-150) rotate(${st.lean}) translate(0,150)">`;
    g += FACE.arm(L, C.friendTop, SKIN, (o.phone && ['idle', 'talk', 'phone'].includes(st.pose)) ? `<g transform="translate(${L[2][0] + 4},${L[2][1] - 30}) rotate(${-8 + st.handLag})"><rect x="-18" y="-34" width="36" height="64" rx="7" fill="${INK}"/><rect x="-13" y="-28" width="26" height="50" rx="3" fill="#9fe3ff"/></g>` : '');
    g += `<g transform="translate(0,-150) scale(1,${st.breath}) translate(0,150)"><path d="M-72,-330 Q0,-352 72,-330 L88,-150 Q0,-128 -88,-150Z" fill="url(#gTopC)" stroke="${INK}" stroke-width="5.5" stroke-linejoin="round"/><path d="M30,-340 Q58,-336 72,-330 L88,-150 Q60,-140 40,-138Z" fill="#c9702e" opacity=".55"/><path d="M-26,-342 Q0,-318 26,-342" fill="none" stroke="${INK}" stroke-width="6"/><rect x="-36" y="-280" width="72" height="40" rx="8" fill="#fff" opacity=".85" stroke="${INK}" stroke-width="4"/><text x="0" y="-252" text-anchor="middle" font-family="Mono" font-weight="700" font-size="20" fill="${C.laptopRed}">404</text></g>`;
    g += `<g transform="translate(0,-360) rotate(${st.headTilt}) translate(0,-110)">`;
    g += `<ellipse cx="-112" cy="6" rx="20" ry="28" fill="${SKIN}" stroke="${INK}" stroke-width="6"/><ellipse cx="112" cy="6" rx="20" ry="28" fill="${SKIN}" stroke="${INK}" stroke-width="6"/><circle r="115" fill="${SKIN}" stroke="${INK}" stroke-width="5.5"/><ellipse cx="-40" cy="-30" rx="46" ry="30" fill="#fff" opacity=".16"/>`;
    g += `<g transform="rotate(${st.drag * .5})"><path d="M-112,-20 C-120,-110 -40,-130 0,-128 C50,-128 118,-110 112,-20 C90,-60 40,-70 0,-66 C-40,-70 -90,-60 -112,-20Z" fill="${HAIR}" stroke="${INK}" stroke-width="6"/></g>`;
    g += `<g transform="translate(0,-70) rotate(${st.drag * 1.4}) translate(0,70)"><path d="M-92,-70 C-90,-150 90,-150 92,-70 Z" fill="${C.cap}" stroke="${INK}" stroke-width="6"/><path d="M60,-74 C110,-78 150,-66 160,-56 C130,-50 90,-52 50,-58Z" fill="#b51f2c" stroke="${INK}" stroke-width="6"/><circle cx="0" cy="-138" r="9" fill="#b51f2c" stroke="${INK}" stroke-width="4"/></g>`;  // cap: follow-through
    g += `<ellipse cx="-62" cy="30" rx="18" ry="10" fill="#ff8f8f" opacity=".5"/><ellipse cx="62" cy="30" rx="18" ry="10" fill="#ff8f8f" opacity=".5"/>`;
    g += FACE.eyes(st, SKIN) + FACE.brows(st, HAIR) + `<path d="M-6,8 Q4,22 -4,26" fill="none" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>`;
    g += `<g transform="translate(0,14)">${FACE.mouth(st)}</g></g>`;
    g += FACE.arm(Rr, C.friendTop, SKIN, FACE.handExtra(st.pose, Rr[2], SKIN));
    return g + `</g></g></g>`;
  };
  return rig;
}
