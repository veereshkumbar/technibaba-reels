# Director-format reel: "Free airport WiFi = jaal".  c = Chotu (friend), b = Techni Baba.
# LINES: (scene, devanagari for TTS, roman, speaker, camera)
LINES=[
('airport','बाबा! एयरपोर्ट पे फ़्री वाईफ़ाई मिल गया!','Baba! Airport pe FREE WiFi mil gaya!','c','cu'),
('airport','अच्छा? नाम क्या है उसका?','Achha? Naam kya hai uska?','b','cu'),
('airport','फ़्री एयरपोर्ट वाईफ़ाई फ़ास्ट... पासवर्ड भी नहीं!','Free Airport WiFi Fast... password bhi nahi!','c',''),
('airport','पासवर्ड नहीं?! बेटा, वो वाईफ़ाई नहीं, जाल है.','Password nahi?! Beta, wo WiFi nahi, JAAL hai.','b','cu'),
('airport','जाल? मतलब?','Jaal? Matlab?','c','cu'),
('trap','कोई भी सेम नाम का हॉटस्पॉट बना सकता है. फिर नकली लॉगिन पेज दिखा के पासवर्ड ले लेता है.','Koi bhi same naam ka hotspot bana sakta hai. Phir nakli login page dikha ke password le leta hai.','b',''),
('trap','मेरा बैंक पासवर्ड भी?!','Mera bank password bhi?!','c','cu'),
('fix','इसलिए बाहर बैंकिंग सिर्फ़ मोबाइल डेटा पे. फ़्री वाईफ़ाई पे सिर्फ़ रील्स.','Isliye bahar banking sirf mobile data pe. Free WiFi pe sirf reels.','b',''),
('fix','मतलब टेक्नी बाबा की रील्स सेफ़ हैं!','Matlab TechniBaba ki reels safe hain!','c','cu'),
('end','बिल्कुल. कमेंट करो वाईफ़ाई, पार्ट टू में असली नकली पहचानना सिखाऊँगा.','Bilkul. Comment karo WIFI, part 2 mein asli-nakli pehchanna sikhaunga.','b',''),
]
# Baba: Veer's cloned voice when vo_in/b_NN.wav exists (made on the Mac with Voicebox), else the Kokoro stand-in.
VOICES={'c':('kokoro:hm_psi',1.24,1.06),'b':('file:vo_in/b_{i:02d}.wav',1.0,1.0,('kokoro:hm_omega',1.16,0.95))}
# BEATS: one per line. keys = (anchor word, who, pose, expression, big?) ; caps = (anchor word, caption with one *keyword*)
# cams = extra camera keys inside a line (anchor, cam, who) ; hit = word that gets the hit-stop ; rule = dynamics.md rule applied
BEATS=[
 dict(emotion='excited',action='jumps, phone up',rule='hook by 1.5s + anticipation into the jump',
      keys=[(None,'c','up','happy',1),(None,'b','idle','neutral',0)],caps=[('baba','Airport pe *FREE WiFi*!')]),
 dict(emotion='suspicious',action='arms crossed, side-eye',rule='expression change, no static head',
      keys=[(None,'b','cross','sideeye',0),(None,'c','phone','happy',0)],caps=[('achha','*Naam* kya hai?')]),
 dict(emotion='proud',action='shows phone, thumbs up',rule='prop arcs out of the phone',
      keys=[(None,'c','phone','happy',0),('password','c','thumb','happy',1)],caps=[('free','*Free*_Airport_WiFi_Fast'),('password','*Password* bhi nahi!')]),
 dict(emotion='shocked then stern',action='recoils, then points',rule='hit-stop + impact frame on JAAL',hit='jaal',
      keys=[(None,'b','blown','shocked',1),(None,'c','idle','neutral',0),('beta','b','point','angry',1),('jaal','c','idle','shocked',1)],
      caps=[('password','Password *NAHI*?!'),('beta','WiFi nahi... *JAAL* hai!')],cams=[('beta','boom','b')]),
 dict(emotion='confused',action='shrug',rule='overlap: cap and hands settle late',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],caps=[('jaal','*Jaal*? Matlab?')]),
 dict(emotion='explaining',action='explains with both hands, points at the fake page',rule='visual change every 2-3s: three diagram steps',
      keys=[(None,'b','explain','explaining',0),(None,'c','idle','confused',0),('phir','b','point','smug',1),('password','c','blown','shocked',1),('password','b','leanin','smug',0)],
      caps=[('koi','*Same naam* ka hotspot'),('phir','*Nakli* login page'),('password','*Password* chori!')]),
 dict(emotion='panic',action='hands on head',rule='hit-stop on the punchline',hit='password',
      keys=[(None,'c','blown','shocked',1),(None,'b','cross','smug',0)],caps=[('mera','*Bank* password bhi?!')],cams=[('password','boom','c')]),
 dict(emotion='calm',action='counts the rule, open palm',rule='payoff: two cards land with a bounce',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('free','b','palm','smug',1),('reels','c','idle','happy',0)],
      caps=[('isliye','Banking = *Mobile data*'),('free','Free WiFi = sirf *Reels*')],cams=[('free','wide','b')]),
 dict(emotion='cheeky',action='thumbs up',rule='squash and stretch on the reaction',
      keys=[(None,'c','thumb','happy',1),(None,'b','idle','happy',0)],caps=[('matlab','TechniBaba ki reels *SAFE*!')]),
 dict(emotion='warm',action='thumbs up, then points at the comment box',rule='comment prompt + payoff',
      keys=[(None,'b','thumb','happy',1),(None,'c','wave','happy',0),('comment','b','point','happy',1),('part','b','explain','explaining',0),('asli','c','up','happy',1),('sikhaunga','b','wave','happy',1)],
      caps=[('bilkul','Comment karo *"WIFI"*'),('part','*Part 2*: asli vs nakli')]),
]
