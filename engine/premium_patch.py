import sys
p=sys.argv[1];s=open(p).read()
def rep(a,b):
    global s
    if a not in s: print('MISS',a[:70]); return
    s=s.replace(a,b,1)
rep("html,body{","@font-face{font-family:Pop;font-weight:600;src:url(file:///tmp/fonts/node_modules/@fontsource/poppins/files/poppins-latin-600-normal.woff2)}\n@font-face{font-family:Pop;font-weight:800;src:url(file:///tmp/fonts/node_modules/@fontsource/poppins/files/poppins-latin-800-normal.woff2)}\n@font-face{font-family:Pop;font-weight:900;src:url(file:///tmp/fonts/node_modules/@fontsource/poppins/files/poppins-latin-900-normal.woff2)}\nhtml,body{")
rep("text{font-family:Inter,'Noto Color Emoji'}","text{font-family:Pop,Inter,'Noto Color Emoji'}")
rep("const OUT='#1b1b2f'","const OUT='#2b2140'")
rep("SKIN='#f6c79e'","SKIN='url(#gSkin)'")
s=s.replace('stroke="${OUT}" stroke-width="7"','stroke="${OUT}" stroke-width="5.5"')
s=s.replace('stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}"','stroke-width="31" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}"')
rep("const C=who=='c'?{top:'#f4a261',top2:'#d98543',pants:'#3d5a80'","const C=who=='c'?{top:'url(#gTopC)',top2:'#c9702e',pants:'url(#gPantC)'")
rep("{top:MINT,top2:MINT2,pants:NAVY,","{top:'url(#gTopB)',top2:'#2a9e74',pants:'url(#gNavy)',")
rep('<circle r="115" fill="${SKIN}" stroke="${OUT}" stroke-width="5.5"/>','<circle r="115" fill="${SKIN}" stroke="${OUT}" stroke-width="5.5"/><ellipse cx="-40" cy="-30" rx="46" ry="30" fill="#fff" opacity=".16"/>')
s=s.replace('C-110,120 -122,70 -120,10Z" fill="${NAVY}"','C-110,120 -122,70 -120,10Z" fill="url(#gNavy)"')
rep('`<ellipse cx="0" cy="6" rx="${120-hop*.6}" ry="20" fill="#000" opacity=".22"/>`','`<ellipse cx="0" cy="8" rx="${130-hop*.6}" ry="24" fill="#000" opacity=".32" filter="url(#fSoft)"/>`')
rep("return `<g transform=\"${bTr}\">${loc(n,t)}</g><g transform=\"${tr}\">","const dof=C.z>1.2?'fDof2':'fDof1';\n return `<g transform=\"${bTr}\"><g filter=\"url(#${dof})\">${loc(n,t)}</g>${light(n,t)}</g><g transform=\"${tr}\" filter=\"url(#fChar)\">")
rep("// ================= UI: phone card =================","""function light(n,t){const L={bed:['#6b7cff',.25,240,560],free:['#ffd27a',.35,240,560],chai:['#fff1c1',.35,820,520],office:['#ffffff',.3,770,600],park:['#ffd166',.4,540,1000],end:['#5de0b0',.2,540,800]}[n]||['#fff',.2,540,600];
 let o=`<circle cx="${L[2]}" cy="${L[3]}" r="520" fill="${L[0]}" opacity="${L[1]}" filter="url(#fBloom)"/>`;
 for(let k=0;k<14;k++){const x=(k*137+t*(8+k%5*3))%1300-110,y=380+((k*251)%800)+Math.sin(t*.7+k)*20,r=6+(k*7)%18;o+=`<circle cx="${x}" cy="${y}" r="${r}" fill="#fff" opacity="${.05+.05*(k%3)}" filter="url(#fSoft)"/>`}
 return o}
// ================= UI: phone card =================""")
rep('<rect x="-150" y="-180" width="300" height="370" rx="34" fill="#000" opacity=".25" transform="translate(10,14)"/><rect x="-150" y="-185" width="300" height="370" rx="34" fill="${OUT}"/>',
    '<rect x="-150" y="-185" width="300" height="370" rx="40" fill="#000" opacity=".45" filter="url(#fShadow)" transform="translate(0,20)"/><rect x="-152" y="-187" width="304" height="374" rx="42" fill="url(#gBezel)"/><rect x="-146" y="-181" width="292" height="362" rx="37" fill="#0b0b10"/>')
rep('<rect x="-40" y="-178" width="80" height="10" rx="5" fill="#333"/></g>`}','<rect x="-36" y="-160" width="72" height="18" rx="9" fill="#000"/><path d="M-136,-168 L40,-168 L-136,60Z" fill="#fff" opacity=".07"/></g>`}')
TITLE=open(sys.argv[2]).read().strip().split('\n') if len(sys.argv)>2 else ['TECHNIBABA · TECH HACK','Phone bola: <tspan fill="#ff5a5f">Storage Full</tspan> 😩','Asli culprit: 4,000 Good Morning photos 💀']
s=s[:s.index('function banner(t)')]+'''function banner(t){const p=eo(prog(t,0,.5));return `<g transform="translate(540,${250-40*(1-p)})" opacity="${p}"><rect x="-440" y="-92" width="880" height="184" rx="34" fill="#0f0f1e" opacity=".78" filter="url(#fShadow)"/><rect x="-440" y="-92" width="880" height="184" rx="34" fill="#0f0f1e" opacity=".55"/><rect x="-440" y="-92" width="880" height="184" rx="34" fill="none" stroke="#ffffff" stroke-opacity=".16" stroke-width="2"/><rect x="-160" y="-112" width="320" height="42" rx="21" fill="${MINT}"/><text y="-83" text-anchor="middle" font-weight="800" font-size="20" fill="#0f0f1e" letter-spacing="3">'''+TITLE[0]+'''</text><text y="4" text-anchor="middle" font-weight="900" font-size="52" fill="#fff">'''+TITLE[1]+'''</text><text y="58" text-anchor="middle" font-weight="600" font-size="31" fill="#c9c9e0">'''+TITLE[2]+'''</text></g>`}
'''+s[s.index('const KW='):]
s=s[:s.index('function kw(t)')]+'''function kw(t){let o='';KW.forEach(([i,w,txt,c],k)=>{const a=W(i,w)-.05,nx=KW[k+1]?W(KW[k+1][0],KW[k+1][1])-.1:a+1.6,b=Math.min(nx,a+1.6);if(t<a||t>b)return;const p=pop(t,a,.4),f=1-prog(t,b-.2,b),fs=Math.min(58,640/(txt.length*.62)),w2=txt.length*fs*.32+46;
 o+=`<g transform="translate(540,1130) rotate(${k%2?2.5:-2.5}) scale(${p})" opacity="${f}"><rect x="${-w2}" y="${-fs*.95}" width="${w2*2}" height="${fs*1.5}" rx="${fs*.75}" fill="#000" opacity=".4" filter="url(#fShadow)" transform="translate(0,16)"/><rect x="${-w2}" y="${-fs*.95+8}" width="${w2*2}" height="${fs*1.5}" rx="${fs*.75}" fill="#000" opacity=".35"/><rect x="${-w2}" y="${-fs*.95}" width="${w2*2}" height="${fs*1.5}" rx="${fs*.75}" fill="${c}"/><rect x="${-w2+12}" y="${-fs*.95+6}" width="${w2*2-24}" height="${fs*.55}" rx="${fs*.28}" fill="#fff" opacity=".2"/><text y="${fs*.12}" text-anchor="middle" font-weight="900" font-size="${fs}" fill="#fff">${txt}</text></g>`});return o}
'''+s[s.index('const CH='):]
s=s[:s.index('function caption(t)')]+'''function caption(t){const L=lineAt(t);if(!L)return'';const ch=CH[L.i],ws=words(L.i),st=wordStarts(L.i);let ci=0;ch.forEach((c,k)=>{if(t>=c.s-.05)ci=k});const c=ch[ci];const a=eo(prog(t,c.s-.05,c.s+.18));const plain=c.ks.map(k=>ws[k]).join(' '),fs=Math.min(66,920/(plain.length*.62));
 const col=L.spk=='c'?'#ffc94a':'#6ff2c4';const tsp=c.ks.map(k=>`<tspan fill="${t>=st[k]-.03?col:'#fff'}">${ws[k]}</tspan>`).join(' ');
 const tag=`<g transform="translate(0,${-fs-26})"><rect x="-96" y="-22" width="192" height="40" rx="20" fill="#0f0f1e" opacity=".8"/><circle cx="-70" cy="-2" r="8" fill="${L.spk=='c'?'#f4a261':MINT}"/><text x="10" y="6" text-anchor="middle" font-weight="800" font-size="19" fill="#fff" letter-spacing="2">${L.spk=='c'?'CHOTU':'TECHNI BABA'}</text></g>`;
 return `<g transform="translate(540,${1320+14*(1-a)})" opacity="${a}">${tag}<text text-anchor="middle" font-weight="800" font-size="${fs}" fill="#000" opacity=".6" filter="url(#fSoft)" transform="translate(0,6)">${plain}</text><text text-anchor="middle" font-weight="800" font-size="${fs}" stroke="#0f0f1e" stroke-width="7" stroke-linejoin="round" paint-order="stroke">${tsp}</text></g>`}
'''+s[s.index('// ================= frame'):]
s=s[:s.index('function grade(t)')]+open(''+__import__('os').path.join(__import__('os').path.dirname(__file__),'frame_part.js')+'').read()+s[s.index('// ================= sfx'):]
open(p,'w').write(s);print('patched')
