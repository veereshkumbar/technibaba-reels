// Anime "Veer" host character (from Veer's 20 Nov 2026 reference video). Bust rig drawn in SVG, cel-shaded.
// VEER.draw({x, y, s, outfit:'tee'|'hoodie', cap:false|true, expr, mouth, blink, look, tilt}) -> SVG string, origin = chin.
// expr: neutral | happy | surprised | smug | explaining ; mouth: rest | smile | A | E | O | M
const VEER = (() => {
  const C = {
    line: '#2A1A12', skin: '#C88A5C', skinSh: '#A66C44', skinHi: '#DDA172', blush: '#D9785F',
    hair: '#24170F', hairHi: '#4B3424', beard: '#22160F', beardHi: '#3D2A1D', brow: '#1E130C',
    iris: '#3A2414', irisHi: '#7A5236', white: '#FBF7F2', frame: '#141218', lens: '#8F7BFF', teeth: '#FFFFFF', mouth: '#5A2320', tongue: '#C9524A',
    tee: '#C8C8CC', teeSh: '#A6A6AD', teeHi: '#DADADD',
    hood: '#211E66', hoodSh: '#16134A', hoodHi: '#2E2A80', mint: '#5DE0B0', mintSh: '#3FB88E',
    cap: '#14132B', capSh: '#0B0A1C', capHi: '#26244A'
  };
  const L = (w = 5) => `stroke="${C.line}" stroke-width="${w}" stroke-linejoin="round" stroke-linecap="round"`;

  function shoulders(o) {
    if (o.outfit == 'hoodie') {
      return `
      <path d="M-150,-40 C-190,-30 -250,10 -300,60 L-330,260 L330,260 L300,60 C250,10 190,-30 150,-40 Z" fill="${C.hood}" ${L(6)}/>
      <path d="M-300,60 C-260,30 -230,25 -200,30 L-215,260 L-330,260 Z" fill="${C.hoodSh}" opacity=".7"/>
      <path d="M300,60 C280,50 260,45 240,48 L250,260 L330,260 Z" fill="${C.hoodSh}" opacity=".45"/>
      <!-- hood bunched around the neck -->
      <path d="M-175,-55 C-215,-10 -205,40 -150,62 C-90,86 -40,70 0,72 C40,70 90,86 150,62 C205,40 215,-10 175,-55 C150,-20 100,10 0,14 C-100,10 -150,-20 -175,-55 Z" fill="${C.hoodHi}" ${L(6)}/>
      <path d="M-120,4 C-70,24 70,24 120,4" fill="none" stroke="${C.hoodSh}" stroke-width="6" stroke-linecap="round"/>
      <!-- drawstrings -->
      <path d="M-42,40 C-48,90 -40,140 -50,190" fill="none" stroke="${C.mint}" stroke-width="9" stroke-linecap="round"/>
      <path d="M42,40 C48,92 44,130 52,176" fill="none" stroke="${C.mint}" stroke-width="9" stroke-linecap="round"/>
      <rect x="-58" y="186" width="16" height="30" rx="5" fill="#D9DCE6" ${L(3)}/>
      <rect x="44" y="172" width="16" height="30" rx="5" fill="#D9DCE6" ${L(3)}/>
      <circle cx="-42" cy="40" r="7" fill="#D9DCE6" ${L(3)}/><circle cx="42" cy="40" r="7" fill="#D9DCE6" ${L(3)}/>
      <!-- small chest mark -->
      <text x="150" y="150" text-anchor="middle" font-family="Poppins,Arial" font-weight="800" font-size="34" fill="${C.mint}" opacity=".95">TB</text>`;
    }
    return `
      <path d="M-120,-30 C-170,-20 -240,10 -290,60 L-320,260 L320,260 L290,60 C240,10 170,-20 120,-30 Z" fill="${C.tee}" ${L(6)}/>
      <path d="M-290,60 C-250,35 -220,30 -190,34 L-200,260 L-320,260 Z" fill="${C.teeSh}" opacity=".8"/>
      <path d="M-30,120 C-10,135 20,140 50,128" fill="none" stroke="${C.teeSh}" stroke-width="4" stroke-linecap="round" opacity=".7"/>
      <!-- crew neck -->
      <path d="M-105,-34 C-80,30 80,30 105,-34" fill="none" stroke="${C.teeSh}" stroke-width="20" stroke-linecap="round"/>
      <path d="M-105,-34 C-80,30 80,30 105,-34" fill="none" ${L(5)}/>
`;
  }

  function neck() {
    return `<path d="M-62,-150 L-66,-20 C-30,10 30,10 66,-20 L62,-150 Z" fill="${C.skinSh}" ${L(5)}/>
            <path d="M-62,-70 C-20,-40 20,-40 62,-70 L62,-150 L-62,-150 Z" fill="${C.line}" opacity=".18"/>`;
  }

  function ears() {
    const ear = sx => `<g transform="scale(${sx},1)"><path d="M118,-300 C150,-318 168,-280 160,-248 C154,-222 138,-206 120,-210" fill="${C.skin}" ${L(5)}/>
      <path d="M132,-284 C146,-284 150,-262 142,-244" fill="none" stroke="${C.skinSh}" stroke-width="5" stroke-linecap="round"/></g>`;
    return ear(-1) + ear(1);
  }

  // head: forehead/cheeks; the beard covers the lower face
  function face() {
    return `<path d="M-122,-330 C-128,-410 -80,-458 0,-460 C80,-458 128,-410 122,-330 L120,-250 C118,-200 100,-150 70,-118 C45,-92 20,-80 0,-80 C-20,-80 -45,-92 -70,-118 C-100,-150 -118,-200 -120,-250 Z" fill="${C.skin}" ${L(6)}/>
      <path d="M90,-330 C100,-280 98,-220 78,-170 C96,-190 112,-240 116,-300 Z" fill="${C.skinSh}" opacity=".55"/>
      <ellipse cx="-62" cy="-232" rx="22" ry="10" fill="${C.blush}" opacity=".25"/><ellipse cx="62" cy="-232" rx="22" ry="10" fill="${C.blush}" opacity=".25"/>`;
  }

  function beard(o) {
    // full, neat beard: sideburns -> jaw -> slightly pointed chin, mustache joined
    return `<path d="M-121,-268 C-118,-205 -104,-150 -72,-104 C-50,-72 -24,-46 0,-42 C24,-46 50,-72 72,-104 C104,-150 118,-205 121,-268
                     C110,-232 98,-210 84,-196 C70,-180 52,-176 36,-182 C20,-188 -20,-188 -36,-182 C-52,-176 -70,-180 -84,-196 C-98,-210 -110,-232 -121,-268 Z" fill="${C.beard}" ${L(5)}/>
      <path d="M-100,-170 C-92,-140 -78,-118 -58,-98" fill="none" stroke="${C.beardHi}" stroke-width="5" stroke-linecap="round" opacity=".8"/>
      <path d="M100,-170 C92,-140 78,-118 58,-98" fill="none" stroke="${C.beardHi}" stroke-width="5" stroke-linecap="round" opacity=".8"/>
      <path d="M-20,-70 l8,-14 l6,14 M10,-66 l8,-14 l6,14" fill="none" stroke="${C.beardHi}" stroke-width="4" stroke-linecap="round" opacity=".7"/>
      <!-- mustache -->
      <path d="M-58,-170 C-40,-196 -12,-196 0,-186 C12,-196 40,-196 58,-170 C40,-176 16,-172 0,-166 C-16,-172 -40,-176 -58,-170 Z" fill="${C.beard}" ${L(4)}/>`;
  }

  function mouth(o) {
    const m = o.mouth || 'rest', y = -148;
    const lip = `<path d="M-40,${y - 10} C-20,${y - 4} 20,${y - 4} 40,${y - 10} C34,${y + 22} -34,${y + 22} -40,${y - 10} Z" fill="${C.skinSh}" opacity=".9"/>`;
    const shapes = {
      rest: `<path d="M-28,${y} C-10,${y + 7} 10,${y + 7} 28,${y}" fill="none" stroke="${C.mouth}" stroke-width="7" stroke-linecap="round"/>`,
      M: `<path d="M-24,${y + 2} C-8,${y - 2} 8,${y - 2} 24,${y + 2}" fill="none" stroke="${C.mouth}" stroke-width="7" stroke-linecap="round"/>`,
      smile: `<path d="M-46,${y - 8} C-30,${y + 34} 30,${y + 34} 46,${y - 8} C20,${y + 2} -20,${y + 2} -46,${y - 8} Z" fill="${C.mouth}" ${L(4)}/>
              <path d="M-40,${y - 5} C-20,${y + 6} 20,${y + 6} 40,${y - 5} L36,${y + 6} C14,${y + 13} -14,${y + 13} -36,${y + 6} Z" fill="${C.teeth}"/>`,
      A: `<path d="M-30,${y - 6} C-30,${y + 40} 30,${y + 40} 30,${y - 6} C14,${y - 2} -14,${y - 2} -30,${y - 6} Z" fill="${C.mouth}" ${L(4)}/>
          <path d="M-24,${y - 4} C-8,${y} 8,${y} 24,${y - 4} L22,${y + 4} C8,${y + 7} -8,${y + 7} -22,${y + 4} Z" fill="${C.teeth}"/>
          <ellipse cx="0" cy="${y + 24}" rx="15" ry="7" fill="${C.tongue}"/>`,
      E: `<path d="M-40,${y - 6} C-26,${y + 26} 26,${y + 26} 40,${y - 6} C18,${y - 2} -18,${y - 2} -40,${y - 6} Z" fill="${C.mouth}" ${L(4)}/>
          <path d="M-32,${y - 2} C-14,${y + 3} 14,${y + 3} 32,${y - 2} L30,${y + 6} C12,${y + 10} -12,${y + 10} -30,${y + 6} Z" fill="${C.teeth}"/>`,
      O: `<ellipse cx="0" cy="${y + 8}" rx="17" ry="22" fill="${C.mouth}" ${L(4)}/><ellipse cx="0" cy="${y + 20}" rx="9" ry="6" fill="${C.tongue}"/>`,
    };
    return lip + (shapes[m] || shapes.rest);
  }

  function nose() {
    return `<path d="M6,-268 C12,-246 14,-232 6,-224" fill="none" stroke="${C.skinSh}" stroke-width="7" stroke-linecap="round"/>
            <path d="M-8,-222 C-2,-218 4,-218 8,-222" fill="none" stroke="${C.line}" stroke-width="4" stroke-linecap="round" opacity=".55"/>`;
  }

  function eyes(o) {
    const e = o.expr || 'neutral', look = o.look || 0, bl = o.blink || 0;
    const eye = (cx, side) => {
      if (e == 'happy' || bl > .8) {
        // closed / happy arcs
        const up = e == 'happy' ? -1 : 1;
        return `<path d="M${cx - 30},${-300 + (up < 0 ? 6 : 0)} C${cx - 14},${-300 - 16 * up} ${cx + 14},${-300 - 16 * up} ${cx + 30},${-300 + (up < 0 ? 6 : 0)}" fill="none" stroke="${C.line}" stroke-width="7" stroke-linecap="round"/>`;
      }
      const big = e == 'surprised' ? 1.18 : 1, lid = e == 'smug' && side > 0 ? 12 : 0;
      const ix = cx + look * 8;
      return `<g><path d="M${cx - 32},-300 C${cx - 26},${-330 * big + (lid ? 6 : 0)} ${cx + 26},${-330 * big + lid} ${cx + 32},-300 C${cx + 26},-280 ${cx - 26},-280 ${cx - 32},-300 Z" fill="${C.white}" ${L(3)}/>
        <clipPath id="ec${side}"><path d="M${cx - 32},-300 C${cx - 26},${-330 * big + lid} ${cx + 26},${-330 * big + lid} ${cx + 32},-300 C${cx + 26},-280 ${cx - 26},-280 ${cx - 32},-300 Z"/></clipPath>
        <g clip-path="url(#ec${side})"><ellipse cx="${ix}" cy="-302" rx="${18 * big}" ry="${22 * big}" fill="${C.iris}"/><ellipse cx="${ix}" cy="-296" rx="${9 * big}" ry="${10 * big}" fill="${C.irisHi}" opacity=".7"/>
          <circle cx="${ix}" cy="-302" r="${6 * big}" fill="#120A06"/><circle cx="${ix + 5}" cy="-309" r="5" fill="#fff"/><circle cx="${ix - 6}" cy="-294" r="2.4" fill="#fff" opacity=".85"/></g>
        <path d="M${cx - 34},-300 C${cx - 26},${-334 * big + lid} ${cx + 26},${-334 * big + lid} ${cx + 34},-298" fill="none" stroke="${C.line}" stroke-width="8" stroke-linecap="round"/>
        <path d="M${cx + 34 * side},-298 l${10 * side},-6" stroke="${C.line}" stroke-width="6" stroke-linecap="round"/></g>`;
    };
    return eye(-56, -1) + eye(56, 1);
  }

  function brows(o) {
    const e = o.expr || 'neutral';
    const lift = {neutral: 0, happy: -6, surprised: -18, smug: 0, explaining: -4}[e] || 0;
    const lr = e == 'smug' ? -16 : lift, ll = e == 'smug' ? 4 : lift;
    const b = (cx, dy0, sx) => { const dy = dy0 - 22; return `<path d="M${cx - 38 * sx},${-344 + dy + 6} C${cx - 14 * sx},${-360 + dy} ${cx + 14 * sx},${-362 + dy} ${cx + 38 * sx},${-352 + dy} L${cx + 36 * sx},${-342 + dy} C${cx + 12 * sx},${-348 + dy} ${cx - 14 * sx},${-346 + dy} ${cx - 38 * sx},${-336 + dy} Z" fill="${C.brow}"/>`; };
    return b(-56, ll, 1) + b(56, lr, -1);
  }

  function glasses() {
    const lens = cx => `<rect x="${cx - 52}" y="-338" width="104" height="70" rx="14" fill="${C.lens}" fill-opacity=".16" stroke="${C.frame}" stroke-width="11"/>
       <path d="M${cx - 34},-326 L${cx - 2},-326 L${cx - 26},-280 L${cx - 44},-280 Z" fill="#fff" opacity=".22"/>
       <circle cx="${cx < 0 ? cx - 40 : cx + 40}" cy="-330" r="2.6" fill="#C9CCD6"/><circle cx="${cx < 0 ? cx - 32 : cx + 32}" cy="-330" r="2.6" fill="#C9CCD6"/>`;
    return lens(-58) + lens(58) + `<path d="M-6,-312 C-2,-318 2,-318 6,-312" fill="none" stroke="${C.frame}" stroke-width="9"/>
      <path d="M-110,-322 L-124,-318 M110,-322 L124,-318" stroke="${C.frame}" stroke-width="9" stroke-linecap="round"/>`;
  }

  function hairBack(o) {
    if (o.cap) return '';
    return `<path d="M-128,-300 C-140,-380 -120,-440 -60,-466 C-10,-486 60,-482 104,-452 C140,-426 140,-360 128,-300 C120,-340 110,-370 96,-384 L-96,-384 C-110,-368 -120,-340 -128,-300 Z" fill="${C.hair}" ${L(6)}/>`;
  }

  function hairFront(o) {
    const shade = `<path d="M-118,-330 C-100,-366 -60,-380 -20,-372 C20,-380 70,-372 104,-344 C112,-330 118,-318 120,-306 C100,-340 60,-356 20,-352 C-20,-350 -70,-352 -118,-330 Z" fill="${C.skinSh}" opacity=".55"/>`;
    if (o.cap) {
      // only the short sides show under the cap
      return shade + `<path d="M-124,-300 C-126,-330 -122,-356 -112,-372 L-96,-372 C-104,-350 -108,-326 -110,-296 Z" fill="${C.hair}" ${L(4)}/>
              <path d="M124,-300 C126,-330 122,-356 112,-372 L96,-372 C104,-350 108,-326 110,-296 Z" fill="${C.hair}" ${L(4)}/>`;
    }
    // short sides, longer top swept to his left (viewer's right), spiky anime fringe
    return shade + `<path d="M-126,-318 C-132,-370 -112,-420 -70,-444 C-30,-466 30,-470 74,-454 C110,-440 138,-404 134,-352 C130,-330 126,-318 124,-306
              C118,-338 108,-360 92,-372 L104,-344 C80,-372 60,-384 34,-388 L44,-360 C20,-380 -6,-390 -34,-386 L-22,-362 C-50,-378 -76,-376 -96,-366 C-108,-352 -118,-336 -126,-318 Z" fill="${C.hair}" ${L(6)}/>
      <path d="M-70,-430 C-30,-450 30,-452 70,-438" fill="none" stroke="${C.hairHi}" stroke-width="8" stroke-linecap="round" opacity=".9"/>
      <path d="M-40,-410 C0,-424 40,-422 80,-406" fill="none" stroke="${C.hairHi}" stroke-width="5" stroke-linecap="round" opacity=".6"/>
      <path d="M96,-470 C112,-486 128,-480 132,-466 C120,-470 108,-466 96,-458 Z" fill="${C.hair}" ${L(4)}/>
      <path d="M-20,-440 C10,-420 30,-400 40,-372 M30,-446 C60,-424 80,-404 92,-376" fill="none" stroke="${C.line}" stroke-width="4" stroke-linecap="round" opacity=".6"/>`;
  }

  function cap(o) {
    if (!o.cap) return '';
    // flat-brim snapback, worn straight with a slight tilt; mint TB on the front panel, mint brim edge
    return `<g transform="rotate(-4 0 -380)">
      <path d="M-136,-360 C-150,-430 -100,-500 0,-504 C100,-500 150,-430 136,-360 Z" fill="${C.cap}" ${L(6)}/>
      <path d="M-30,-500 C-40,-460 -42,-410 -40,-362 M30,-500 C40,-460 42,-410 40,-362" fill="none" stroke="${C.capHi}" stroke-width="4"/>
      <path d="M-136,-360 C-150,-430 -120,-480 -60,-498 C-100,-460 -112,-410 -110,-360 Z" fill="${C.capSh}" opacity=".8"/>
      <circle cx="0" cy="-503" r="9" fill="${C.mint}" ${L(3)}/>
      <text x="0" y="-412" text-anchor="middle" font-family="Poppins,Arial" font-weight="900" font-size="60" fill="${C.mint}" letter-spacing="-2">TB</text>
      <!-- flat brim -->
      <path d="M-158,-366 C-100,-382 100,-382 158,-366 L170,-338 C100,-352 -100,-352 -170,-338 Z" fill="${C.cap}" ${L(6)}/>
      <path d="M-170,-338 C-100,-352 100,-352 170,-338" fill="none" stroke="${C.mint}" stroke-width="6"/>
      <path d="M-150,-358 C-90,-372 90,-372 150,-358" fill="none" stroke="${C.capHi}" stroke-width="3" stroke-dasharray="6 7"/>
    </g>`;
  }

  function draw(o = {}) {
    const x = o.x || 0, y = o.y || 0, s = o.s || 1, tilt = o.tilt || 0;
    const head = `<g transform="rotate(${tilt} 0 -150)">${hairBack(o)}${ears()}${face()}${beard(o)}${mouth(o)}${nose()}${eyes(o)}${brows(o)}${glasses()}${hairFront(o)}${cap(o)}</g>`;
    return `<g transform="translate(${x},${y}) scale(${s})">${shoulders(o)}${neck()}${head}</g>`;
  }
  return {draw, C};
})();
if (typeof module !== 'undefined') module.exports = VEER;
