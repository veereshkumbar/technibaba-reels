function eyes(e,t,look,blinkSeed){const bl=((t+blinkSeed)%3.4)<.11;let o='';
 [-42,42].forEach((x,k)=>{let ry=e=='shock'?32:24,rx=e=='shock'?24:20;if(bl)ry=3;
  if(e=='happy'&&!bl){o+=`<path d="M${x-18},-6 Q${x},-28 ${x+18},-6" fill="none" stroke="${OUT}" stroke-width="5.5" stroke-linecap="round"/>`;return}
  o+=`<ellipse cx="${x}" cy="-10" rx="${rx}" ry="${ry}" fill="#fff" stroke="${OUT}" stroke-width="5"/>`;
  if(!bl){const pr=e=='shock'?8:11;o+=`<circle cx="${x+look*8}" cy="${-6}" r="${pr}" fill="${OUT}"/><circle cx="${x+look*8+3}" cy="-10" r="3.5" fill="#fff"/>`}
  if((e=='annoyed'||e=='smug')&&!bl)o+=`<path d="M${x-rx-3},-12 L${x+rx+3},-12 L${x+rx+3},${-10-ry-4} L${x-rx-3},${-10-ry-4}Z" fill="${blinkSeed>1?'#f7f3ea':SKIN}" stroke="${OUT}" stroke-width="5"/>`;
 });return o}
function brows(e,col){const B={neutral:[-6,6],shock:[-14,14],annoyed:[16,-16],smug:[-14,10],worried:[-16,16],happy:[-8,8],shy:[-12,12]}[e]||[0,0];
 const y0=e=='shock'?-62:-48;let o='';[-1,1].forEach(s=>{const inner=s<0?B[0]*(e=='worried'?-1:1):B[1]*(e=='worried'?-1:1);
  // inner end raised for worried, lowered for annoyed
  const yi=y0+(e=='annoyed'?10:e=='worried'?-10:0),yo=y0+(e=='annoyed'?-6:e=='worried'?6:0)+(e=='smug'&&s>0?-10:0);
  o+=`<path d="M${s*16},${yi} L${s*60},${yo}" stroke="${col}" stroke-width="11" stroke-linecap="round"/>`});return o}
function mouth(e,open,inBeard){const cy=48;
 if(open>.08){const h=8+34*open,w=34-6*open;return `<ellipse cx="0" cy="${cy}" rx="${w}" ry="${h/2}" fill="#5a1a22" stroke="${OUT}" stroke-width="5"/><ellipse cx="0" cy="${cy+h/2-7}" rx="${w*.55}" ry="${Math.min(8,h/4)}" fill="#e76f6f"/>`}
 if(e=='shock')return `<ellipse cx="0" cy="${cy}" rx="14" ry="18" fill="#5a1a22" stroke="${OUT}" stroke-width="5"/>`;
 if(e=='happy')return `<path d="M-30,${cy-8} Q0,${cy+30} 30,${cy-8} Z" fill="#5a1a22" stroke="${OUT}" stroke-width="5" stroke-linejoin="round"/>`;
 if(e=='smug')return `<path d="M-22,${cy+4} Q4,${cy+10} 26,${cy-8}" fill="none" stroke="${OUT}" stroke-width="6" stroke-linecap="round"/>`;
 if(e=='annoyed')return `<path d="M-20,${cy+4} L20,${cy+4}" stroke="${OUT}" stroke-width="6" stroke-linecap="round"/>`;
 if(e=='worried'||e=='shy')return `<path d="M-20,${cy+8} Q0,${cy-6} 20,${cy+8}" fill="none" stroke="${OUT}" stroke-width="6" stroke-linecap="round"/>`;
 return `<path d="M-22,${cy} Q0,${cy+14} 22,${cy}" fill="none" stroke="${OUT}" stroke-width="6" stroke-linecap="round"/>`}
function chotuHead(e,t,open,look){let o=`<ellipse cx="-112" cy="6" rx="20" ry="28" fill="${SKIN}" stroke="${OUT}" stroke-width="6"/><ellipse cx="112" cy="6" rx="20" ry="28" fill="${SKIN}" stroke="${OUT}" stroke-width="6"/>`;
 o+=`<circle r="115" fill="${SKIN}" stroke="${OUT}" stroke-width="5.5"/><ellipse cx="-40" cy="-30" rx="46" ry="30" fill="#fff" opacity=".16"/><path d="M60,-90 A115,115 0 0 1 60,92 A130,130 0 0 0 60,-90Z" fill="${SKIN2}" opacity=".55"/>`;
 o+=`<path d="M-112,-20 C-120,-110 -40,-130 0,-128 C50,-128 118,-110 112,-20 C90,-60 40,-70 0,-66 C-40,-70 -90,-60 -112,-20Z" fill="#3b2316" stroke="${OUT}" stroke-width="6"/>`;
 o+=`<path d="M-92,-70 C-90,-150 90,-150 92,-70 Z" fill="#e63946" stroke="${OUT}" stroke-width="6"/><path d="M60,-74 C110,-78 150,-66 160,-56 C130,-50 90,-52 50,-58Z" fill="#b51f2c" stroke="${OUT}" stroke-width="6"/><circle cx="0" cy="-138" r="9" fill="#b51f2c" stroke="${OUT}" stroke-width="4"/>`;
 o+=`<ellipse cx="-62" cy="30" rx="18" ry="10" fill="#ff8f8f" opacity=".5"/><ellipse cx="62" cy="30" rx="18" ry="10" fill="#ff8f8f" opacity=".5"/>`;
 o+=eyes(e,t,look,0.7)+brows(e,'#3b2316')+`<path d="M-6,8 Q4,22 -4,26" fill="none" stroke="${OUT}" stroke-width="5" stroke-linecap="round"/>`;
 o+=`<path d="M-46,34 C-30,18 -8,24 0,30 C8,24 30,18 46,34 C30,36 12,38 0,36 C-12,38 -30,36 -46,34Z" fill="#3b2316" stroke="${OUT}" stroke-width="4"/>`;
 o+=`<g transform="translate(0,14)">${mouth(e,open)}</g>`;return o}
function babaHead(e,t,open,look){let o=`<circle cx="0" cy="-150" r="34" fill="${NAVY}" stroke="${OUT}" stroke-width="6"/>`;
 o+=`<path d="M-120,10 C-130,-120 -60,-138 0,-138 C60,-138 130,-120 120,10 C122,70 110,120 90,150 L-90,150 C-110,120 -122,70 -120,10Z" fill="url(#gNavy)" stroke="${OUT}" stroke-width="6"/>`;
 o+=`<path d="M-86,-70 C-80,-110 80,-110 86,-70 L92,30 C60,50 -60,50 -92,30Z" fill="url(#gFace)" stroke="${OUT}" stroke-width="6"/>`;
 // laptop third eye
 o+=`<g transform="translate(0,-82)"><rect x="-30" y="-20" width="60" height="36" rx="4" fill="#f7f3ea" stroke="${RD}" stroke-width="5"/><rect x="-21" y="-12" width="42" height="21" fill="${RD}" opacity=".18"/><path d="M-8,5 L4,-8 M2,5 L14,-8" stroke="${RD}" stroke-width="3.5"/><path d="M-38,18 L38,18 L32,26 L-32,26Z" fill="${RD}"/></g>`;
 o+=eyes(e,t,look,1.9)+brows(e,NAVY);
 // beard
 o+=`<path d="M-96,10 C-104,90 -84,160 -60,220 L-46,198 L-30,246 L-14,214 L0,262 L14,214 L30,246 L46,198 L60,220 C84,160 104,90 96,10 C70,40 40,30 0,32 C-40,30 -70,40 -96,10Z" fill="${NAVY}" stroke="${OUT}" stroke-width="6" stroke-linejoin="round"/>`;
 o+=`<path d="M-50,30 C-30,16 -10,22 0,28 C10,22 30,16 50,30 C30,40 12,40 0,38 C-12,40 -30,40 -50,30Z" fill="${NAVY}" stroke="#2a2870" stroke-width="3"/>`;
 o+=`<g transform="translate(0,22)"><ellipse cx="0" cy="48" rx="${36+6*open}" ry="${20+16*open}" fill="#f7f3ea"/>${mouth(e,open)}</g>`;return o}
