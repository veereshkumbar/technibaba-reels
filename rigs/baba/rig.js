// Techni Baba rig — layered parts, drawn to match the logo: top-knot bun, long navy hair, full beard,
// red laptop on the forehead, mint glow ring.  API (from rigs/core.js): pose(), express(), say(), draw(frame, {x,y,s,flip,glow,ring}).
function makeBaba() {
  const rig = RIG.makeRig('baba'), C = TOKENS.color, INK = C.ink, NAVY = 'url(#gNavy)', SKIN = 'url(#gSkin)';
  rig.draw = (f, o = {}) => {
    const st = rig.state(f), glow = o.glow || 0, ring = o.ring || 0, s = o.s || 1;
    const L = FACE.limb(-62, -318, -1, st.arms.L[0], st.arms.L[1] + st.handLag, 95, 88), Rr = FACE.limb(62, -318, 1, st.arms.R[0], st.arms.R[1] + st.handLag, 95, 88);
    const sy = 1 + st.sq, sx = 1 - st.sq * .6, jaw = ['AI', 'L', 'O'].includes(st.viseme) ? 9 : ['E', 'FV', 'U'].includes(st.viseme) ? 4 : 0;
    let g = `<g transform="translate(${o.x || 0},${(o.y || 0) - st.hop}) scale(${o.flip ? -s : s},${s})">`;
    g += `<ellipse cx="0" cy="8" rx="${130 - st.hop * .6}" ry="24" fill="#000" opacity=".3" filter="url(#fRigSoft)"/>`;
    g += `<g transform="scale(${sx},${sy})">`;
    [-30, 30].forEach(x => { g += `<path d="M${x},-160 L${x},-18" stroke="${INK}" stroke-width="44" stroke-linecap="round"/><path d="M${x},-160 L${x},-18" stroke="${NAVY}" stroke-width="32" stroke-linecap="round"/><ellipse cx="${x + 14}" cy="-6" rx="34" ry="17" fill="#7a4b2a" stroke="${INK}" stroke-width="6"/>`; });
    g += `<g transform="translate(0,-150) rotate(${st.lean}) translate(0,150)">`;       // upper body leans from the hips
    g += FACE.arm(L, C.mint, SKIN);
    g += `<g transform="translate(0,-150) scale(1,${st.breath}) translate(0,150)"><path d="M-72,-330 Q0,-352 72,-330 L88,-150 Q0,-128 -88,-150Z" fill="url(#gTopB)" stroke="${INK}" stroke-width="5.5" stroke-linejoin="round"/><path d="M30,-340 Q58,-336 72,-330 L88,-150 Q60,-140 40,-138Z" fill="${C.mintDark}" opacity=".55"/><path d="M-58,-336 Q-10,-250 40,-140" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round"/><path d="M-14,-342 L0,-300 L14,-342" fill="none" stroke="${INK}" stroke-width="5"/></g>`;
    // ---- head group (pivot at neck) ----
    g += `<g transform="translate(0,-360) rotate(${st.headTilt}) translate(0,-110)">`;
    if (ring) g += `<circle cx="0" cy="0" r="${205 + 10 * ring}" fill="none" stroke="${C.mint}" stroke-width="${8 + 6 * ring}" opacity="${.35 + .55 * ring}"/><circle cx="0" cy="0" r="215" fill="${C.mint}" opacity="${.12 * ring}" filter="url(#fRigGlow)"/>`;
    g += `<g transform="translate(0,-118) rotate(${st.drag * 1.7}) translate(0,118)"><circle cx="0" cy="-152" r="34" fill="${NAVY}" stroke="${INK}" stroke-width="5.5"/><ellipse cx="-10" cy="-162" rx="12" ry="8" fill="#fff" opacity=".12"/></g>`;   // top-knot: follow-through
    g += `<g transform="rotate(${st.drag * .35})"><path d="M-120,10 C-130,-120 -60,-138 0,-138 C60,-138 130,-120 120,10 C122,70 110,120 90,150 L-90,150 C-110,120 -122,70 -120,10Z" fill="${NAVY}" stroke="${INK}" stroke-width="5.5"/></g>`;  // hair
    g += `<path d="M-86,-70 C-80,-110 80,-110 86,-70 L92,30 C60,50 -60,50 -92,30Z" fill="url(#gFace)" stroke="${INK}" stroke-width="5.5"/>`;
    g += `<g transform="translate(0,-82)">${glow ? `<rect x="-44" y="-34" width="88" height="64" rx="10" fill="${C.laptopRed}" opacity="${.5 * glow}" filter="url(#fRigGlow)"/>` : ''}<rect x="-30" y="-20" width="60" height="36" rx="4" fill="${C.face}" stroke="${C.laptopRed}" stroke-width="5"/><rect x="-21" y="-12" width="42" height="21" fill="${C.laptopRed}" opacity="${.18 + .6 * glow}"/><path d="M-8,5 L4,-8 M2,5 L14,-8" stroke="${glow > .5 ? '#fff' : C.laptopRed}" stroke-width="3.5"/><path d="M-38,18 L38,18 L32,26 L-32,26Z" fill="${C.laptopRed}"/></g>`;
    g += FACE.eyes(st, C.face) + FACE.brows(st, C.navy);
    g += `<g transform="translate(0,${10 + jaw * .5}) rotate(${st.drag * .9}) translate(0,-10)"><path d="M-96,10 C-104,90 -84,160 -60,220 L-46,198 L-30,246 L-14,214 L0,${262 + jaw} L14,214 L30,246 L46,198 L60,220 C84,160 104,90 96,10 C70,40 40,30 0,32 C-40,30 -70,40 -96,10Z" fill="${NAVY}" stroke="${INK}" stroke-width="5.5" stroke-linejoin="round"/></g>`;  // beard: overlap, settles after the jaw
    g += `<g transform="translate(0,22)"><ellipse cx="0" cy="${48 + jaw * .4}" rx="${38 + jaw * .5}" ry="${21 + jaw}" fill="${C.face}"/>${FACE.mouth(st)}</g>`;
    g += `<path d="M-50,30 C-30,16 -10,22 0,28 C10,22 30,16 50,30 C30,40 12,40 0,38 C-12,40 -30,40 -50,30Z" fill="${NAVY}" stroke="#2a2870" stroke-width="3"/>`;
    g += `</g>`;
    g += FACE.arm(Rr, C.mint, SKIN, FACE.handExtra(st.pose, Rr[2], SKIN));
    return g + `</g></g></g>`;
  };
  return rig;
}
