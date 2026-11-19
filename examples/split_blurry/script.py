# Split-layout reel, 17:00 Creator Guide 19 Nov 2026: "Reel upload karte hi dhundhli? 3 fix"  c = Chotu, b = Techni Baba.
LINES=[
('q','बाबा! फ़ोन में रील एकदम साफ़, इंस्टाग्राम पे डालते ही धुंधली!','Baba! Phone mein reel ekdum saaf, Instagram pe daalte hi DHUNDHLI!','c',''),
('q','एक सेटिंग: अपलोड ऐट हाईएस्ट क्वालिटी. ऑन करो.','Ek setting: Upload at highest quality. ON karo.','b',''),
('set','प्रोफ़ाइल, मेन्यू, मीडिया क्वालिटी, टॉगल ऑन.','Profile, Menu, Media quality, toggle ON.','b',''),
('share','रुको! ये उस दोस्त को भेजता हूँ, जिसकी हर रील धुंधली आती है!','Ruko! Ye us dost ko bhejta hoon, jiski har reel dhundhli aati hai!','c',''),
('export','दूसरा: टेन एटी बाय नाइनटीन ट्वेंटी, थर्टी फ़्रेम. फ़ोर के का फ़ायदा नहीं.','Doosra: 1080 x 1920, 30 frame. 4K ka fayda nahi.','b',''),
('wifi','तीसरा: अच्छा वाईफ़ाई, और ओरिजिनल फ़ाइल. व्हाट्सऐप वाली नहीं, वो दबा देता है.','Teesra: achha WiFi, aur original file. WhatsApp wali nahi, woh daba deta hai.','b',''),
('recap','सेटिंग, साइज़, वाईफ़ाई. कमेंट करो गाइड, पूरा रास्ता डीएम में भेजूँगा.','Setting, size, WiFi. Comment karo GUIDE, poora rasta DM mein bhejunga.','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.24,1.06),'b':('file:vo_in/b_{i:02d}.wav',1.0,1.0,('kokoro:hm_omega',1.18,0.95))}
BEATS=[
 dict(emotion='shocked',action='phone up, then blown',rule='hook by 1.5s, full-screen payoff (saaf vs dhundhli) before the split',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('instagram','b','leanin','confused',0),('dhundhli','c','blown','shocked',1)],caps=[('baba','Phone mein *SAAF*'),('instagram','Instagram pe *DHUNDHLI*!')]),
 dict(emotion='calm',action='raises finger, thumb on ON',rule='payoff by 6s: the toggle; hit-stop on ON',hit='on',
      keys=[(None,'b','explain','smug',1),(None,'c','idle','confused',0),('upload','b','point','explaining',0),('on','b','thumb','happy',1)],caps=[('ek','Ek *SETTING*'),('upload','*HIGHEST* quality'),('on','*ON* karo!')]),
 dict(emotion='explaining',action='points at each row',rule='one visual: settings path, rows light on each word',
      keys=[(None,'b','point','explaining',1),(None,'c','phone','neutral',0),('media','b','explain','explaining',0),('toggle','c','leanin','happy',1)],caps=[('profile','Profile > *MENU*'),('media','*MEDIA* quality'),('toggle','Toggle *ON*')]),
 dict(emotion='excited',action='points out at viewer, phone',rule='share ask at ~10s with a named person',
      keys=[(None,'c','point','happy',1),(None,'b','idle','happy',0),('dost','c','phone','happy',0),('dhundhli','b','thumb','happy',1)],caps=[('ruko','Us *DOST* ko bhejo'),('jiski','Jiski reel *DHUNDHLI*')]),
 dict(emotion='explaining',action='counts, then palm on 4K',rule='one visual: spec card ticks; 4K shrinks to 1080',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('30','b','point','explaining',0),('fayda','b','palm','explaining',1),('nahi','c','idle','shocked',0)],caps=[('doosra','2 · *1080x1920*'),('30','*30* frame'),('fayda','4K = *FAYDA NAHI*')]),
 dict(emotion='explaining',action='points, then stop on WhatsApp',rule='hit-stop on DABA',hit='daba',
      keys=[(None,'b','point','explaining',1),(None,'c','phone','neutral',0),('original','b','explain','explaining',0),('whatsapp','b','stop','angry',1),('daba','c','blown','shocked',0)],caps=[('teesra','3 · Achha *WIFI*'),('original','*ORIGINAL* file'),('whatsapp','WhatsApp *NAHI*')]),
 dict(emotion='warm',action='counts, points, waves',rule='recap ticks + one ask: GUIDE',
      keys=[(None,'b','count','happy',1),(None,'c','idle','happy',0),('comment','b','point','happy',1),('guide','c','thumb','happy',1),('dm','b','wave','happy',0)],caps=[('setting','Setting · Size · *WIFI*'),('comment','Comment *GUIDE*')]),
]
