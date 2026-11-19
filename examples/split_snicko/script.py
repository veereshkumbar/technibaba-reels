# Split-layout reel, 14:00 sports through tech (19 Nov 2026): "Awaaz aayi, phir bhi NOT OUT? Snicko ke 3 check"  c = Chotu, b = Techni Baba.
LINES=[
('q','बाबा! बॉल पे आवाज़ आई, अंपायर ने आउट दिया, फिर नॉट आउट?!','Baba! Ball pe awaaz aayi, umpire ne OUT diya, phir NOT OUT?!','c',''),
('news','आज वेलिंगटन टेस्ट में कॉनवे ने रिव्यू लिया. आवाज़, बॉल पहुँचने से पहले आई. नॉट आउट!','Aaj Wellington Test mein Conway ne review liya. Awaaz, ball pahunchne se PEHLE aayi. NOT OUT!','b',''),
('share','मेरा दोस्त तो हर आवाज़ पे आउट चिल्लाता है!','Mera dost toh har awaaz pe OUT chillata hai!','c',''),
('share','उसको ये भेजो! स्निको के तीन चेक.','Usko ye bhejo! Snicko ke teen check.','b',''),
('spike','पहला: स्पाइक. स्टंप में माइक है. बॉल बैट को छुए, तो ग्राफ़ पे तेज़ स्पाइक.','Pehla: spike. Stump mein mic hai. Ball bat ko chhue, toh graph pe tez spike.','b',''),
('frame','दूसरा: फ़्रेम. स्पाइक उसी फ़्रेम में, जब बॉल बैट के पास हो. पहले या बाद में? नॉट आउट!','Doosra: frame. Spike usi frame mein, jab ball bat ke paas ho. Pehle ya baad mein? NOT OUT!','b',''),
('shape','और आवाज़ पैड की हो तो?','Aur awaaz pad ki ho toh?','c',''),
('shape','तीसरा: शेप. बैट पे बॉल, पतला तेज़. पैड या ज़मीन, मोटा.','Teesra: shape. Bat pe ball, patla tez. Pad ya zameen, mota.','b',''),
('end','तो सिर्फ़ आवाज़ पे मत चिल्लाना! स्निको पे भरोसा, हाँ या ना?','Toh sirf awaaz pe mat chillana! Snicko pe bharosa, HAAN ya NA?','c',''),
]
VOICES={'c':('kokoro:hm_psi',1.26,1.06),'b':('file:vo_in/b_{i:02d}.wav',1.0,1.0,('kokoro:hm_omega',1.22,0.95))}
BEATS=[
 dict(emotion='confused',action='hands on head, then shrug',rule='hook by 1.5s, full-screen payoff before the split',
      keys=[(None,'c','blown','shocked',1),(None,'b','idle','neutral',0),('umpire','c','point','angry',1),('phir','c','shrug','confused',1)],caps=[('baba','*Awaaz* aayi...'),('umpire','Umpire: *OUT*'),('phir','Phir *NOT OUT*?!')]),
 dict(emotion='calm',action='palm, then points at the graph',rule='payoff by 10s: sound before the ball',hit='pehle',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','neutral',0),('conway','b','explain','explaining',0),('awaaz','b','point','explaining',1),('pehle','c','blown','shocked',1),('not','b','thumb','happy',1)],caps=[('aaj','*Wellington Test*'),('conway','Conway ka *review*'),('awaaz','Awaaz *PEHLE* aayi'),('not','*NOT OUT*')]),
 dict(emotion='sheepish',action='points sideways, laughs',rule='share ask on screen at 8-12s',
      keys=[(None,'c','point','happy',1),(None,'b','idle','smug',0),('out','c','up','happy',1)],caps=[('mera','Mera *dost*...'),('out','Har awaaz pe *OUT!*')]),
 dict(emotion='warm',action='thumbs up, then counts three',rule='share ask + list promise',
      keys=[(None,'b','thumb','happy',1),(None,'c','idle','happy',0),('snicko','b','count','explaining',1)],caps=[('usko','Usko *BHEJO*'),('snicko','Snicko: *3 check*')]),
 dict(emotion='explaining',action='explains, points up at the graph',rule='one visual: mic + flat line then sharp spike',
      keys=[(None,'b','explain','explaining',0),(None,'c','idle','neutral',0),('stump','b','point','explaining',1),('tez','c','leanin','shocked',0)],caps=[('pehla','Check 1: *SPIKE*'),('stump','Stump mein *mic*'),('tez','Bat chhua = *tez spike*')]),
 dict(emotion='stern',action='explains, then stop hand on NOT OUT',rule='hit-stop on NOT (the twist)',hit='not',
      keys=[(None,'b','explain','explaining',0),(None,'c','idle','confused',0),('usi','b','point','explaining',1),('pehle','c','shrug','confused',0),('not','b','stop','angry',1),('not','c','blown','shocked',1)],caps=[('doosra','Check 2: *FRAME*'),('usi','*Usi frame* mein?'),('pehle','Pehle/baad = *NOT OUT*')]),
 dict(emotion='curious',action='leans in, shrug',rule='short reaction beat',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('aur','Awaaz *pad* ki?')]),
 dict(emotion='explaining',action='counts, palm',rule='two shapes side by side, each cued on its word',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('patla','b','point','explaining',1),('pad','b','palm','smug',0),('mota','c','thumb','happy',1)],caps=[('teesra','Check 3: *SHAPE*'),('patla','Bat = *patla, tez*'),('mota','Pad/zameen = *mota*')]),
 dict(emotion='proud',action='wags finger, then points at the comment box',rule='one ask at the end, loops to the hook',
      keys=[(None,'c','stop','smug',1),(None,'b','idle','happy',0),('snicko','c','point','happy',1),('haan','b','wave','happy',1)],caps=[('toh','Sirf awaaz pe *mat chillao*'),('snicko','*Snicko* pe bharosa?'),('haan','*HAAN ya NA?*')]),
]
