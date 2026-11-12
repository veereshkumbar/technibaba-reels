const NAVY='#12104a',RED='#d9534f',MINT='#5de0b0',SKIN='#f2c49b';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),prog=(t,a,b)=>clamp((t-a)/(b-a)),eo=x=>1-Math.pow(1-x,3),eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const back=x=>{const c1=1.9,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const rad=d=>d*Math.PI/180, lerp=(a,b,f)=>a+(b-a)*f;
function limb(x,y,a1,l1,a2,l2){const x1=x+Math.sin(rad(a1))*l1,y1=y+Math.cos(rad(a1))*l1;const x2=x1+Math.sin(rad(a1+a2))*l2,y2=y1+Math.cos(rad(a1+a2))*l2;return [[x,y],[x1,y1],[x2,y2]]}
const pl=p=>p.map(q=>q.map(v=>v.toFixed(1)).join(',')).join(' ');
// ---------- heads ----------
const HAIR='M-74,-20 C-80,-100 -42,-126 0,-126 C42,-126 80,-100 74,-20 C78,30 72,70 56,92 L-56,92 C-72,70 -78,30 -74,-20 Z';
const FACE='M-50,-56 C-44,-84 44,-84 50,-56 L54,40 C30,52 -30,52 -54,40 Z';
const BEARD='M-62,14 C-66,70 -56,110 -46,140 L-36,128 L-26,160 L-13,142 L0,172 L13,142 L26,160 L36,128 L46,140 C56,110 66,70 62,14 C42,30 20,22 0,26 C-20,22 -42,30 -62,14 Z';
function babaHead(glow){let o=`<circle cx="0" cy="-132" r="22" fill="${NAVY}"/><path d="${HAIR}" fill="${NAVY}"/><path d="${FACE}" fill="#fff"/><path d="${BEARD}" fill="${NAVY}"/><ellipse cx="0" cy="44" rx="27" ry="15" fill="#fff"/><rect x="-5" y="52" width="10" height="12" fill="${NAVY}"/>`;
 if(glow)o+=`<rect x="-34" y="-70" width="68" height="56" rx="10" fill="${MINT}" opacity="${glow*.5}"/>`;
 o+=`<g stroke="${RED}" stroke-width="3" fill="none"><rect x="-26" y="-62" width="52" height="32" rx="3"/><rect x="-19" y="-56" width="38" height="21"/><path d="M-32,-27 L32,-27 L28,-20 L-28,-20 Z"/><path d="M-6,-40 L4,-50 M2,-40 L12,-50" stroke-width="2.5"/></g><g stroke="${NAVY}" stroke-width="2.5" fill="none" stroke-dasharray="5 5"><path d="M26,-50 C50,-50 52,-34 40,-26"/><path d="M-26,-42 C-52,-38 -46,-8 -6,-8 L-6,10"/></g><path d="M-13,10 L1,10 L-6,20 Z" fill="${NAVY}"/><text x="38" y="6" font-family="Mono" font-weight="700" font-size="22" fill="${NAVY}">*</text><text x="-52" y="-58" font-family="Mono" font-weight="700" font-size="20" fill="${RED}">*</text>`;return o}
function chotuHead(t){const bl=(t%3.1)<.12?.1:1;return `<path d="M-58,-30 C-60,-100 60,-100 58,-30 Z" fill="#2a1a12"/><ellipse cx="0" cy="0" rx="58" ry="68" fill="${SKIN}"/><path d="M-60,-28 C-50,-92 50,-92 60,-28 C40,-50 -40,-50 -60,-28Z" fill="#2a1a12"/><rect x="-46" y="-96" width="92" height="30" rx="8" fill="#e63946"/><rect x="-52" y="-72" width="104" height="10" rx="4" fill="#b51f2c"/><ellipse cx="-20" cy="-8" rx="7" ry="${9*bl}" fill="#1a1a1a"/><ellipse cx="20" cy="-8" rx="7" ry="${9*bl}" fill="#1a1a1a"/><path d="M-44,26 C-30,8 -8,16 0,22 C8,16 30,8 44,26 C30,24 12,30 0,28 C-12,30 -30,24 -44,26Z" fill="#2a1a12"/><path d="M-14,40 Q0,52 14,40" stroke="#8a3b2b" stroke-width="5" fill="none" stroke-linecap="round"/><ellipse cx="-62" cy="4" rx="9" ry="14" fill="${SKIN}"/><ellipse cx="62" cy="4" rx="9" ry="14" fill="${SKIN}"/>`}
// ---------- generic person ----------
function arms(pose,t){const p=t*2*Math.PI*1.5;
 if(pose=='walk')return[[-24*Math.sin(p),-22],[24*Math.sin(p),-22]];
 if(pose=='wave')return[[12,-10],[160+18*Math.sin(t*9),25]];
 if(pose=='drive')return[[32+3*Math.sin(t*2),62],[-32+3*Math.sin(t*2),-62]];
 if(pose=='type')return[[12+3*Math.sin(t*21),48],[-12+3*Math.sin(t*25),-48]];
 if(pose=='blown')return[[-150,-20+10*Math.sin(t*10)],[150,20-10*Math.sin(t*10)]];
 if(pose=='tray')return[[-24*Math.sin(p),-22],[150,95]];
 if(pose=='thumb')return[[12,-10],[-150,-70]];
 if(pose=='eat'){const c=(t%1.3)/1.3,f=c<.5?eio(c*2):1-eio((c-.5)*2);return[[28,72],[lerp(11,197,f),0]]}
 return[[10,0],[-10,0]]}
function person(t,o){const p=t*2*Math.PI*1.5,walking=o.pose=='walk'||o.pose=='tray',bob=walking?-7*Math.abs(Math.cos(p)):0;
 let s=`<g transform="translate(${o.x},${o.y+bob}) scale(${o.flip?-o.s:o.s},${o.s})" stroke-linecap="round" stroke-linejoin="round">`;
 const [la,ra]=arms(o.pose,t),c=o.c;
 const LA=limb(-40,-238,la[0],62,la[1],56),RA=limb(40,-238,ra[0],62,ra[1],56);
 const leg=(P)=>`<polyline points="${pl(P)}" fill="none" stroke="${c.pants}" stroke-width="20"/><path d="M${P[2][0]-4},${P[2][1]} l26,0" stroke="${c.shoe||NAVY}" stroke-width="18"/>`;
 let L,R;if(o.sit){L=limb(-18,-130,0,66,0,62);R=limb(18,-130,0,66,0,62)}else if(walking){L=limb(-18,-130,28*Math.sin(p),66,Math.max(0,-Math.sin(p+.6))*-38,62);R=limb(18,-130,-28*Math.sin(p),66,Math.max(0,Math.sin(p+.6))*-38,62)}else{L=limb(-18,-130,-4,66,0,62);R=limb(18,-130,4,66,0,62)}
 const arm=P=>`<polyline points="${pl(P)}" fill="none" stroke="${c.sleeve}" stroke-width="16"/><circle cx="${P[2][0]}" cy="${P[2][1]}" r="9" fill="${c.hand}"/>`;
 if(!o.noLegs)s+=leg(L);s+=arm(LA);
 s+=`<path d="M-40,-246 Q0,-262 40,-246 L50,-120 Q0,-108 -50,-120 Z" fill="${c.top}"/>`;
 if(o.who=='baba')s+=`<path d="M-10,-250 L0,-196 L10,-250" fill="none" stroke="${NAVY}" stroke-width="4"/><path d="M-36,-244 Q-6,-200 30,-128" fill="none" stroke="#fff" stroke-width="12"/>`;
 if(o.who=='chotu')s+=`<path d="M-14,-246 L0,-236 L14,-246 L14,-226 L0,-236 L-14,-226Z" fill="#111"/><rect x="-46" y="-170" width="92" height="50" fill="#fff" opacity=".9"/><line x1="-46" y1="-170" x2="46" y2="-170" stroke="#ddd" stroke-width="3"/>`;
 if(!o.noLegs)s+=leg(R);s+=arm(RA);
 if(o.pose=='walk'&&o.who=='baba'){const hx=RA[2][0],hy=RA[2][1];s+=`<g transform="translate(${hx+6},${hy-6}) rotate(-8)"><rect x="-6" y="-30" width="54" height="34" rx="3" fill="#e8e8ee" stroke="${RED}" stroke-width="4"/><rect x="-10" y="4" width="62" height="6" rx="2" fill="#bbb" stroke="${RED}" stroke-width="3"/></g>`}
 if(o.pose=='tray'){const hx=RA[2][0],hy=RA[2][1];s+=`<g transform="translate(${hx},${hy-8})"><ellipse cx="0" cy="0" rx="78" ry="12" fill="#c0c4cc" stroke="#888" stroke-width="3"/>${dosa(0,-14,.55)}</g>`}
 if(o.pose=='thumb'){const hx=RA[2][0],hy=RA[2][1];s+=`<rect x="${hx-12}" y="${hy-34}" width="14" height="30" rx="7" fill="${c.hand}"/>`}
 s+=`<g transform="translate(0,-388) scale(.84)">${o.who=='baba'?babaHead(o.glow||0):chotuHead(t)}</g></g>`;return s}
const BABA={who:'baba',c:{pants:'#0e0c38',sleeve:SKIN,hand:SKIN,top:MINT}};
const CHOTU={who:'chotu',c:{pants:'#222',sleeve:'#fff',hand:SKIN,top:'#fff',shoe:'#111'}};
