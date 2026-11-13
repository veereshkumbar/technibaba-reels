const DEFS=`<defs>
<radialGradient id="gSkin" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#ffe0bf"/><stop offset=".7" stop-color="#f4c193"/><stop offset="1" stop-color="#df9f72"/></radialGradient>
<radialGradient id="gFace" cx="40%" cy="35%" r="80%"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e6ddcb"/></radialGradient>
<linearGradient id="gTopC" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffbd7f"/><stop offset="1" stop-color="#e07a38"/></linearGradient>
<linearGradient id="gTopB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8ff5cf"/><stop offset="1" stop-color="#2fae80"/></linearGradient>
<linearGradient id="gNavy" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2e2a80"/><stop offset="1" stop-color="#0c0a30"/></linearGradient>
<linearGradient id="gPantC" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4c6c9a"/><stop offset="1" stop-color="#2b4366"/></linearGradient>
<linearGradient id="gBezel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d8d8e0"/><stop offset=".5" stop-color="#6d6d78"/><stop offset="1" stop-color="#c4c4cc"/></linearGradient>
<filter id="fDof1" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="fDof2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="fSoft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="fBloom" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="90"/></filter>
<filter id="fShadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="fChar" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".28"/></filter>
<filter id="fWhip" x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur stdDeviation="46 0"/></filter>
<filter id="fGrain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="SEED" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .06 0"/></filter>
<radialGradient id="vg" cx="50%" cy="46%" r="72%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#05030f" stop-opacity=".55"/></radialGradient>
<linearGradient id="gLeak" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff9a5a" stop-opacity=".3"/><stop offset=".4" stop-color="#ff9a5a" stop-opacity="0"/></linearGradient>
</defs>`;
const TINT={bed:'#3a46c8',free:'#ffb347',chai:'#ff8a5c',office:'#7fb2ff',park:'#ff6b6b',end:'#2b2f6b'};
function grade(t,n){return `<rect width="1080" height="1920" fill="${TINT[n]||'#888'}" opacity=".14" style="mix-blend-mode:soft-light"/><rect width="1080" height="1920" fill="url(#gLeak)" opacity="${.5+.3*Math.sin(t*.8)}"/><rect width="1080" height="1920" fill="url(#vg)"/><rect width="1080" height="1920" filter="url(#fGrain)"/>`}
function boomFX(t){const l=lineAt(t);if(!l||l.cam!='boom')return'';const p=prog(t,l.start,l.start+.3);if(p>=1)return'';return `<rect width="1080" height="1920" fill="#fff" opacity="${.35*(1-p)}"/>`}
function render(t){const k=sceneIdx(t),n=ORDER[k],S=SCN[n];let o=DEFS.replace('SEED',Math.floor(t*24)%60);
 const wp=k>0?prog(t,S.s-.14,S.s+.2):1;
 if(wp<1){const e=eio(wp),prev=ORDER[k-1],bl=Math.sin(Math.PI*wp)>.15;o+=`<g transform="translate(${-1080*e},0)" ${bl?'filter="url(#fWhip)"':''}>${world(prev,t)}</g><g transform="translate(${1080*(1-e)},0)" ${bl?'filter="url(#fWhip)"':''}>${world(n,t)}</g>`}
 else o+=world(n,t);
 o+=grade(t,n)+banner(t)+phoneUI(n,t)+kw(t)+caption(t)+boomFX(t);
 if(t>TOTAL-1.2){const p=eo(prog(t,TOTAL-1.2,TOTAL-.5));o+=`<g opacity="${p}"><defs><radialGradient id="gEnd" cx="50%" cy="42%" r="70%"><stop offset="0" stop-color="#1f2a5c"/><stop offset="1" stop-color="#07081a"/></radialGradient></defs><rect width="1080" height="1920" fill="url(#gEnd)"/><circle cx="540" cy="800" r="330" fill="${MINT}" opacity=".18" filter="url(#fBloom)"/><circle cx="540" cy="800" r="250" fill="none" stroke="${MINT}" stroke-width="10"/><g transform="translate(540,820) scale(${1.25+.08*p})">${babaHead('happy',t,0,0)}</g><text x="540" y="1170" text-anchor="middle" font-weight="900" font-size="64" fill="#fff">@technibaba</text><text x="540" y="1236" text-anchor="middle" font-weight="600" font-size="34" fill="${MINT}" letter-spacing="2">FOLLOW FOR DAILY TECH HACKS</text></g>`}
 document.getElementById('root').innerHTML=`<svg width="1080" height="1920" viewBox="0 0 1080 1920">${o}</svg>`}
