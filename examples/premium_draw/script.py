# 14:00 trending sports 23 Nov 2026: Wellington Test draw (NZ 368, IND 720/9d, NZ 239/5 in 120 overs) told through pitch + ball science.
# Format 2: not A (bowlers ki galti), not B (Kiwi batting ka jaadu), actually C (pitch + ball ne seam ka kaam band kar diya).
# Sources: CricTracker + Open Magazine + india.com (scores, draw, Gill/Latham/Nicholls quotes), France24 headline (239-5 draw), ESPN day-4 report ('little seam movement or pace in the pitch'),
# ICC day-1 report (green pitch; coach Sitanshu Kotak: sun dried it quicker; Kookaburra seam 'a little tight' after 30-35 overs), Tribune explainer (Kookaburra machine-stitched, seam flattens faster), Wikipedia Seam bowling.
LINES=[
('q','बाबा! इंडिया ने सात सौ बीस रन बनाए, फिर भी टेस्ट ड्रॉ?','Baba! India ne 720 run banaye, phir bhi Test draw?','c',''),
('q','बॉलर्स की गलती? नहीं. कीवी जादू? वो भी नहीं.','Bowlers ki galti? Nahi. Kiwi jaadu? Woh bhi nahi.','b',''),
('q','असली विलेन, पिच और बॉल. सीम का काम ही बंद.','Asli villain: pitch aur ball. Seam ka kaam hi band.','b',''),
('share','ये उस दोस्त को भेजो, जो कहता है ज़्यादा रन, जीत पक्की.','Ye us dost ko bhejo, jo kehta hai zyada run, jeet pakki.','b',''),
('how','पर पिच तो हरी थी ना? बॉल हिली क्यों नहीं?','Par pitch toh hari thi na? Ball hili kyun nahi?','c',''),
('sun','कोच कोटक के हिसाब से, धूप ने पिच जल्दी सुखा दी. सूखी पिच पे सीम पकड़ती नहीं.','Coach Kotak ke hisaab se, dhoop ne pitch jaldi sukha di. Sookhi pitch pe seam pakadti nahi.','b',''),
('ball','और कूकाबुरा बॉल की सिलाई मशीन वाली. तीस ओवर बाद सीम चपटी.','Aur Kookaburra ball ki silai machine wali. Tees over baad seam chapti.','b',''),
('proof','नतीजा, एक सौ बीस ओवर, सिर्फ पाँच विकेट. जीत को बीस विकेट चाहिए, रन नहीं.','Nateeja: 120 over, sirf 5 wicket. Jeet ko 20 wicket chahiye, run nahi.','b',''),
('end','तो बताओ, ड्रॉ का विलेन कौन? पिच या बॉलर्स?','Toh batao, draw ka villain kaun? PITCH ya BOWLERS?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='shocked',action='full-screen, arms up at the scoreboard',rule='hook: the 720 vs draw contradiction by 1.5 s',
      keys=[(None,'c','up','shocked',1),(None,'b','idle','neutral',0),('draw','c','blown','shocked',1)],caps=[('baba','India: *720* run'),('phir','Phir bhi *DRAW?*')]),
 dict(emotion='calm',action='palm, then stop hand',rule='not A, not B: one line each',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','confused',0),('kiwi','b','stop','explaining',1),('woh','c','shrug','confused',1)],caps=[('bowlers','Bowlers ki galti? *Nahi*'),('kiwi','Kiwi jaadu? *Nahi*')]),
 dict(emotion='firm',action='points, hit on BAND',rule='actually C, the claim by ~8 s',hit='band',
      keys=[(None,'b','point','explaining',1),(None,'c','idle','neutral',0),('band','b','cross','angry',1),('seam','c','blown','shocked',1)],caps=[('asli','Villain: *pitch + ball*'),('seam','Seam ka kaam *band*')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask, named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('zyada','c','wave','happy',1)],caps=[('ye','Us *dost* ko bhejo'),('zyada','Zyada run = *jeet pakki?*')]),
 dict(emotion='curious',action='leans in',rule='the stay: why did a green pitch die',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],caps=[('par','Pitch toh *hari* thi'),('ball','Ball *hili* kyun nahi?')]),
 dict(emotion='explaining',action='explains, counts',rule='one visual: wet vs dry pitch, ball path',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('dhoop','b','up','explaining',1),('sookhi','b','count','explaining',1),('pakadti','c','idle','confused',1)],caps=[('coach','Coach *Kotak*:'),('dhoop','*Dhoop* ne sukha di'),('sookhi','Seam *pakadti* nahi')]),
 dict(emotion='explaining',action='phone, points at ball',rule='one visual: machine seam flattening with overs',
      keys=[(None,'b','explain','explaining',1),(None,'c','phone','neutral',0),('tees','b','count','explaining',1),('chapti','c','idle','shocked',1)],caps=[('kookaburra','*Kookaburra* ball'),('silai','Silai *machine* wali'),('tees','30 over baad *chapti*')]),
 dict(emotion='firm',action='counts, hit on BEES',rule='the answer closes the loop, hit',hit='20',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('jeet','b','point','smug',1),('20','c','blown','shocked',1)],caps=[('nateeja','120 over, *5 wicket*'),('jeet','Jeet = *20 wicket*'),('run','Run *nahi*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('pitch','b','wave','happy',1)],caps=[('toh','Draw ka *villain?*'),('pitch','*PITCH* ya BOWLERS?')]),
]
