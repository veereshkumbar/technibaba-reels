# Split-layout reel, 21:00 Bollywood/OTT/gaming x tech (19 Nov 2026): "GTA 6 sirf 30 FPS? PS5 Pro pe bhi? FPS ke 3 sach"  c = Chotu, b = Techni Baba.
LINES=[
('q','बाबा! जी टी ए सिक्स आया, पर सिर्फ़ थर्टी एफ़ पी एस?! प्रो पे भी?!','Baba! GTA 6 aaya, par sirf 30 FPS?! Pro pe bhi?!','c',''),
('news','हाँ. रॉकस्टार के मुताबिक़, प्रो पे भी थर्टी. वजह ग्राफ़िक्स नहीं, सी पी यू है!','Haan. Rockstar ke mutabik, Pro pe bhi 30. Wajah graphics nahi, CPU hai!','b',''),
('share','मेरा दोस्त तो सिक्सटी का सपना देख रहा था!','Mera dost toh 60 ka sapna dekh raha tha!','c',''),
('share','उसको ये भेजो! एफ़ पी एस के तीन सच.','Usko ye bhejo! FPS ke teen sach.','b',''),
('fps','पहला: एफ़ पी एस. एक सेकंड में थर्टी तस्वीर. हर तस्वीर को तैंतीस मिलीसेकंड.','Pehla: FPS. Ek second mein 30 tasveer. Har tasveer ko 33 millisecond.','b',''),
('cpu','दूसरा: सी पी यू. हर तस्वीर से पहले पूरा शहर चलाओ. सिक्सटी पे सिर्फ़ सोलह मिलीसेकंड!','Doosra: CPU. Har tasveer se pehle poora shehar chalao. 60 pe sirf 16 millisecond!','b',''),
('gpu','तो प्रो का फ़ायदा क्या?','Toh Pro ka fayda kya?','c',''),
('gpu','तीसरा: जी पी यू. प्रो पे तस्वीर साफ़, रे ट्रेस्ड शैडो. पर स्पीड थर्टी ही.','Teesra: GPU. Pro pe tasveer saaf, ray-traced shadows. Par speed 30 hi.','b',''),
('end','तो थर्टी एफ़ पी एस चलेगा? हाँ या ना?','Toh 30 FPS chalega? HAAN ya NA?','c',''),
]
VOICES={'c':('kokoro:hm_psi',1.26,1.06),'b':('file:vo_in/b_{i:02d}.wav',1.0,1.0,('kokoro:hm_omega',1.22,0.95))}
BEATS=[
 dict(emotion='shocked',action='hands on head, then points at the counter',rule='hook by 1.5s, full-screen payoff before the split',
      keys=[(None,'c','blown','shocked',1),(None,'b','idle','neutral',0),('sirf','c','point','angry',1),('pro','c','shrug','confused',1)],caps=[('baba','*GTA 6* aaya...'),('sirf','Sirf *30 FPS*?!'),('pro','*Pro* pe bhi?!')]),
 dict(emotion='calm',action='palm, then points on CPU',rule='payoff by 10s: the limit is the CPU',hit='cpu',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','neutral',0),('rockstar','b','explain','explaining',0),('graphics','b','stop','explaining',1),('cpu','b','point','explaining',1),('cpu','c','blown','shocked',1)],caps=[('haan','*Rockstar*: Pro pe bhi 30'),('graphics','Graphics *nahi*...'),('cpu','Wajah: *CPU*')]),
 dict(emotion='sheepish',action='points sideways, laughs',rule='share ask on screen at 8-12s',
      keys=[(None,'c','point','happy',1),(None,'b','idle','smug',0),('sapna','c','up','happy',1)],caps=[('mera','Mera *dost*...'),('sapna','*60 FPS* ka sapna!')]),
 dict(emotion='warm',action='thumbs up, then counts three',rule='share ask + list promise',
      keys=[(None,'b','thumb','happy',1),(None,'c','idle','happy',0),('fps','b','count','explaining',1)],caps=[('usko','Usko *BHEJO*'),('fps','FPS ke *3 sach*')]),
 dict(emotion='explaining',action='explains, points up at the film strip',rule='one visual: 30 frames in one second, 33 ms each',
      keys=[(None,'b','explain','explaining',0),(None,'c','idle','neutral',0),('second','b','point','explaining',1),('har','b','count','explaining',0),('millisecond','c','leanin','shocked',0)],caps=[('pehla','Sach 1: *FPS*'),('ek','1 sec = *30 tasveer*'),('millisecond','Har tasveer: *33 ms*')]),
 dict(emotion='stern',action='points at the city, then stop hand on 16',rule='hit-stop on solah (the squeeze)',hit='16',
      keys=[(None,'b','explain','explaining',0),(None,'c','idle','confused',0),('shehar','b','point','explaining',1),('chalao','c','shrug','confused',0),('16','b','stop','angry',1),('16','c','blown','shocked',1)],caps=[('doosra','Sach 2: *CPU*'),('har','Har tasveer se *pehle*'),('shehar','Poora *shehar* chalao'),('16','60 = sirf *16 ms*!')]),
 dict(emotion='curious',action='leans in, shrug',rule='short reaction beat',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('toh','Pro ka *fayda*?')]),
 dict(emotion='explaining',action='counts, palm',rule='blurry vs sharp side by side, each cued on its word',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('saaf','b','point','explaining',1),('shadows','c','thumb','happy',1),('speed','b','palm','smug',0)],caps=[('teesra','Sach 3: *GPU*'),('saaf','Tasveer *saaf*'),('shadows','*Ray-traced* shadows'),('speed','Speed: *30* hi')]),
 dict(emotion='proud',action='points at the comment box, waves',rule='one ask at the end, loops to the hook',
      keys=[(None,'c','point','happy',1),(None,'b','idle','happy',0),('haan','b','wave','happy',1)],caps=[('toh','*30 FPS* chalega?'),('haan','*HAAN ya NA?*')]),
]
