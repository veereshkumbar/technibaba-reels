# 17:00 evening Creator Guide 20 Nov 2026: CapCut is banned in India -> which free editor for reels? (premium look, Hindi). Format 4: better way (VN) -> best way (Edits).
# CapCut banned in India since 29 Jun 2020 (Sec 69A IT Act), still banned in 2026, not on Play Store / App Store in India (videowizardtools Jul 2026, kripeshadwani Aug 2026, fluxnote Nov 2026).
# Fake CapCut sites: ESET WeLiveSecurity (May 2025, capcuti.com -> malware, credential theft); TechRadar/Cofense (Jul 2025, CapCut phishing steals Apple ID).
# VN: free, no watermark (videoeditorguide Mar 2026, imagine.art Feb 2026, fluxnote Nov 2026).
# Edits: free, iOS + Android, Instagram login, watermark-free export, auto captions, licensed audio, share directly to Instagram (Business Standard Apr 2025, 9to5Google Apr 2025, Later Apr 2025, MacRumors + TNW 5 Nov 2026).
LINES=[
('q','बाबा! कैपकट तो बैन है. अब रील्स किस पे बनाऊँ?','Baba! CapCut toh ban hai. Ab reels kispe banaun?','c',''),
('apk','ए पी के मत ढूँढो. नकली साइट्स, पासवर्ड चुराती हैं.','APK mat dhoondho. Nakli sites, password churaati hain.','b',''),
('better','वी एन अच्छा है, फ्री, बिना वॉटरमार्क. पर बेस्ट, इंस्टाग्राम का अपना है.','VN achha hai, free, bina watermark. Par best, Instagram ka apna hai.','b',''),
('share','उस दोस्त को भेजो, जो अभी भी ए पी के ढूँढ रहा है.','Us dost ko bhejo, jo abhi bhi APK dhoondh raha hai.','b',''),
('reveal','नाम क्या है?','Naam kya hai?','c',''),
('reveal','एडिट्स. फ्री, बिना वॉटरमार्क, और ऑटो कैप्शन, एक टैप में.','Edits. Free, bina watermark, aur auto captions, ek tap mein.','b',''),
('why','गाने लाइब्रेरी से, और एक्सपोर्ट सीधा इंस्टाग्राम पे.','Gaane library se, aur export seedha Instagram pe.','b',''),
('steps','एडिट्स लो, इंस्टाग्राम से लॉगिन, वीडियो डालो, एक्सपोर्ट.','Edits lo, Instagram se login, video daalo, export.','b',''),
('end','तो रील्स किस पे? कमेंट करो गाइड, पूरा रास्ता डी एम में.','Toh reels kispe? Comment karo GUIDE, poora rasta DM mein.','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='worried',action='full-screen, palms up',rule='hook: the pain every Indian creator has',
      keys=[(None,'c','shrug','shocked',1),(None,'b','idle','neutral',0),('ab','c','leanin','confused',1)],caps=[('baba','CapCut toh *BAN* hai'),('ab','Ab reels *kispe?*')]),
 dict(emotion='firm',action='stop hand, then points',rule='caution first: no APK',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','shocked',0),('nakli','b','point','explaining',1),('password','c','blown','shocked',1)],caps=[('apk','*APK* mat dhoondho'),('nakli','Nakli site = *password* chori')]),
 dict(emotion='smug',action='thumb up, then leans in, hit on BEST',rule='better way, then re-hook: the best way exists (claim ~9 s)',hit='best',
      keys=[(None,'b','thumb','happy',1),(None,'c','idle','neutral',0),('free','b','count','explaining',1),('par','b','leanin','smug',1),('best','b','point','smug',1),('instagram','c','blown','shocked',1)],
      caps=[('vn','Accha option: *VN*'),('free','Free, no *watermark*'),('par','Par *BEST*?'),('instagram','Instagram ka *apna*')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask, named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('abhi','c','wave','happy',1)],caps=[('us','Us *dost* ko bhejo'),('abhi','Jo abhi bhi *APK* dhoondhe')]),
 dict(emotion='curious',action='leans in',rule='the stay: what is it called',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('naam','*Naam* kya hai?')]),
 dict(emotion='proud',action='palm, hit on EDITS, counts',rule='best way revealed, hit',hit='edits',
      keys=[(None,'b','palm','happy',1),(None,'c','idle','neutral',0),('free','b','count','explaining',1),('auto','c','thumb','happy',1)],caps=[('edits','*EDITS*'),('free','Free, no *watermark*'),('auto','Auto *captions*, 1 tap')]),
 dict(emotion='explaining',action='explains, points',rule='why it is best for reels',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('export','b','point','happy',1),('instagram','c','thumb','happy',1)],caps=[('gaane','Gaane: *library* se'),('export','Export: seedha *Instagram*')]),
 dict(emotion='explaining',action='counts the steps',rule='the steps close the loop',
      keys=[(None,'b','count','explaining',1),(None,'c','phone','neutral',0),('instagram','b','explain','explaining',1),('video','c','idle','happy',1)],caps=[('edits','*Edits* lo'),('instagram','Instagram se *login*'),('video','Video daalo, *export*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('comment','b','wave','happy',1),('poora','c','thumb','happy',1)],caps=[('toh','Toh reels *kispe?*'),('comment','Comment karo *GUIDE*'),('poora','Guide *DM* mein')]),
]
