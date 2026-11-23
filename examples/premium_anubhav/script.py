# 10:00 trending tech 23 Nov 2026: TRAI Network Anubhav (anubhav.trai.gov.in). Format 3: common belief (ad wala "sabse fast" = mere ghar pe bhi fast) -> contradict (network gali gali badalta hai, apni gali ka speed dekho).
# Facts: launched 4 Nov 2026 (The Week/PTI 4 Nov, tele.net 5 Nov, NCA Academy 6 Nov, Beebom 20 Nov). Web portal anubhav.trai.gov.in; map, pick location, filter provider + cellular/broadband;
# download/upload speed per provider; compare two places (home vs work) (The Week). Data: TRAI MySpeed/MyCall app user tests + TRAI independent drive tests (all four).
# Caveat (TRAI via The Week, tele.net, Beebom): user-test values are not a comprehensive assessment; only places with tests are covered.
LINES=[
('q','बाबा! ऐड बोला सबसे फास्ट. घर पे तो एक डंडी!','Baba! Ad bola sabse fast. Ghar pe toh ek dandi!','c',''),
('q','ऐड देश की बात है, आपकी गली की नहीं. ट्राई की नई साइट पे गली की असली स्पीड देखो.','Ad desh ki baat hai, aapki gali ki nahi. TRAI ki nayi site pe gali ki asli speed dekho.','b',''),
('rule','पापा को भेजो, जो सिम पोर्ट करने वाले हैं.','Papa ko bhejo, jo SIM port karne wale hain.','b',''),
('how','कौनसी साइट? कैसे देखूं?','Kaunsi site? Kaise dekhun?','c',''),
('how','अनुभव डॉट ट्राई डॉट जी ओ वी डॉट इन. मैप पे जगह, फिर कंपनी और मोबाइल.','anubhav.trai.gov.in. Map pe jagah, phir company aur mobile.','b',''),
('cmp','घर और ऑफिस, दोनों?','Ghar aur office, dono?','c',''),
('cmp','हाँ, दो जगह कंपेयर करो. हर कंपनी की डाउनलोड, अपलोड स्पीड.','Haan, do jagah compare karo. Har company ki download, upload speed.','b',''),
('data','ये लोगों के टेस्ट और ट्राई के ड्राइव टेस्ट से आता है. पोर्ट से पहले, अपनी गली देखो.','Ye logon ke test aur TRAI ke drive test se aata hai. Port se pehle, apni gali dekho.','b',''),
('end','आपकी गली में कौन फास्ट? जियो, एयरटेल या वी आई?','Aapki gali mein kaun fast? Jio, Airtel ya Vi?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='frustrated',action='full-screen, phone up',rule='hook: the common belief in one line',
      keys=[(None,'c','phone','angry',1),(None,'b','idle','neutral',0),('ghar','c','blown','shocked',1)],caps=[('baba','Ad: sabse *fast*'),('ghar','Ghar pe *1 dandi*')]),
 dict(emotion='calm',action='palm, then points',rule='contradict: the claim, hit on ASLI',hit='asli',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','confused',0),('trai','b','explain','explaining',1),('asli','b','point','happy',1),('speed','c','thumb','happy',1)],caps=[('ad','Desh ka, *gali* ka nahi'),('trai','TRAI ki *nayi site*'),('asli','*Asli* speed')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('papa','*Papa* ko bhejo'),('jo','SIM *port* wale')]),
 dict(emotion='curious',action='shrug',rule='the stay',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('kaunsi','*Kaunsi* site?')]),
 dict(emotion='explaining',action='counts, then points',rule='the path',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('map','b','point','explaining',1),('mobile','c','thumb','happy',0)],caps=[('anubhav','*anubhav*.trai.gov.in'),('map','Map pe *jagah*'),('phir','Company + *mobile*')]),
 dict(emotion='curious',action='leans in, phone',rule='the real follow-up',
      keys=[(None,'c','phone','confused',1),(None,'b','idle','smug',0)],caps=[('ghar','Ghar + *office?*')]),
 dict(emotion='happy',action='explains, counts',rule='compare two places',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','neutral',0),('har','b','count','explaining',1)],caps=[('haan','Do jagah *compare*'),('har','*Download* + upload')]),
 dict(emotion='serious',action='palm, hit on GALI',rule='where the numbers come from, then the rule, hit',hit='gali',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('trai','b','count','explaining',1),('port','b','stop','explaining',1),('gali','c','thumb','happy',1)],caps=[('ye','Logon ke *test*'),('trai','TRAI *drive test*'),('port','Port se pehle *gali*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('jio','b','wave','happy',1)],caps=[('aapki','Gali mein *kaun fast?*'),('jio','Jio, Airtel ya *Vi?*')]),
]
