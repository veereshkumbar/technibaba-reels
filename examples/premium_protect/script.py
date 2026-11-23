# 17:00 evening Creator Guide 23 Nov 2026: someone reposted my reel -> Instagram Content Protection (premium look, Hindi). Format 4: better way (report it yourself) -> best way (Instagram finds copies itself).
# Content Protection announced 17 Nov 2026 (TechCrunch 17 Nov; ProductNation 18 Nov; TechBriefly 18 Nov; CineD 19 Nov): scans for copies of a creator's videos,
# eligible creators get a notification in their activity feed; found under "Your professional tools"; after enrolling, original videos posted from then on are protected automatically;
# match actions: Track, Hide from everyone, Add credit link ("original by"), Release; allow list; AI spoken-word matching tested with a small group in the coming weeks.
LINES=[
('q','बाबा! मेरी रील किसी और ने डाल दी. व्यूज़ उसको मिल रहे!','Baba! Meri reel kisi aur ne daal di. Views usko mil rahe!','c',''),
('report','रिपोर्ट करना ठीक है. पर अब बेस्ट तरीका, इंस्टाग्राम खुद ढूँढेगा.','Report karna theek hai. Par ab best tareeka, Instagram khud dhoondhega.','b',''),
('share','उस दोस्त को भेजो, जिसकी रील रोज़ चोरी होती है.','Us dost ko bhejo, jiski reel roz chori hoti hai.','b',''),
('reveal','कैसे? नाम क्या है?','Kaise? Naam kya hai?','c',''),
('reveal','कंटेंट प्रोटेक्शन. सत्रह नवंबर को आया, और कॉपी रील्स खुद स्कैन करता है.','Content Protection. Satrah November ko aaya, aur copy reels khud scan karta hai.','b',''),
('how','सबको अभी नहीं मिला. नोटिफिकेशन आए, या प्रोफेशनल टूल्स में दिखे, तो ऑन करो.','Sabko abhi nahi mila. Notification aaye, ya Professional tools mein dikhe, toh on karo.','b',''),
('match','फिर नई रील्स अपने आप प्रोटेक्टेड. कॉपी मिली, तो छुपाओ, या क्रेडिट लिंक लगाओ.','Phir nayi reels apne aap protected. Copy mili, toh chhupao, ya credit link lagao.','b',''),
('end','आपकी रील कभी चोरी हुई? कमेंट करो गाइड, पूरा रास्ता डी एम में.','Aapki reel kabhi chori hui? Comment karo GUIDE, poora rasta DM mein.','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='upset',action='full-screen, palms up',rule='hook: the pain every small creator has',
      keys=[(None,'c','shrug','angry',1),(None,'b','idle','neutral',0),('views','c','leanin','shocked',1)],caps=[('baba','Meri reel *chori*'),('views','Views usko *mil* rahe')]),
 dict(emotion='calm, then smug',action='thumb, then leans in, hit on KHUD',rule='better way, then re-hook: the best way exists (claim ~7 s)',hit='khud',
      keys=[(None,'b','thumb','neutral',1),(None,'c','idle','confused',0),('par','b','leanin','smug',1),('khud','b','point','smug',1),('dhoondhega','c','blown','shocked',1)],
      caps=[('report','Report: *theek* hai'),('par','Par *BEST*?'),('khud','Instagram *khud* dhoondhe')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask, named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('roz','c','wave','happy',1)],caps=[('us','Us *dost* ko bhejo'),('roz','Jiski reel *roz* chori')]),
 dict(emotion='curious',action='leans in',rule='the stay: what is it called',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('kaise','*Naam* kya hai?')]),
 dict(emotion='proud',action='palm, hit on PROTECTION, explains',rule='best way revealed, hit',hit='protection',
      keys=[(None,'b','palm','happy',1),(None,'c','idle','neutral',0),('satrah','b','count','explaining',1),('scan','c','thumb','happy',1)],
      caps=[('content','Content *Protection*'),('satrah','Bilkul *naya* tool'),('copy','Copy *scan* khud')]),
 dict(emotion='honest',action='shrug, then explains',rule='honest caveat + where to find it',
      keys=[(None,'b','shrug','neutral',1),(None,'c','idle','confused',0),('notification','b','explain','explaining',1),('professional','c','phone','neutral',1),('on','b','thumb','happy',1)],
      caps=[('sabko','Sabko *abhi* nahi'),('notification','*Notification* dekho'),('professional','Ya *Professional* tools')]),
 dict(emotion='explaining',action='counts the options',rule='the how closes the loop',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('copy','b','explain','explaining',1),('chhupao','c','stop','smug',1),('credit','b','point','happy',1)],
      caps=[('phir','Nayi reels *auto*'),('copy','Copy? *Chhupao*'),('credit','Ya *credit* link')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('comment','b','wave','happy',1),('poora','c','thumb','happy',1)],caps=[('aapki','Reel kabhi *chori*?'),('comment','Comment karo *GUIDE*'),('poora','Guide *DM* mein')]),
]
