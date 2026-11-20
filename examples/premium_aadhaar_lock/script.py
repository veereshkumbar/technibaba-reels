# Morning tutorial 20 Nov 2026: Aadhaar Biometric Lock (premium look, Hindi). Format 5: won't work (fingerprint safe), unless (Biometric Lock on).
# Facts: AePS cash withdrawal needs only Aadhaar no. + bank + fingerprint; cloned prints, no OTP (Deccan Herald / Karnataka CID, india.com, Axis Bank).
# Lock path: myaadhaar.uidai.gov.in > login (Aadhaar + captcha + OTP to Aadhaar-linked mobile) > Lock/Unlock Biometrics > tick > Lock (Paisabazaar Oct 2026, CitizenNest Jun 2026, Groww, BankBazaar, Smartprix).
# Temporary unlock 10 min then re-locks (Paisabazaar, BankBazaar, Groww). 1930 / cybercrime.gov.in.
LINES=[
('q','आधार का नकली अंगूठा, बिना ओटीपी के पैसे निकाल सकता है.','Aadhaar ka nakli angootha, bina OTP ke paise nikaal sakta hai.','b',''),
('q','तो अब क्या, कुछ नहीं हो सकता?','Toh ab kya, kuch nahi ho sakta?','c',''),
('q','होगा. बस बायोमेट्रिक लॉक ऑन करो. फिर नकली अंगूठा बेकार.','Hoga. Bas Biometric LOCK on karo. Phir nakli angootha bekaar.','b',''),
('rule','ये पापा को भेजो, जिनका आधार बैंक से जुड़ा है.','Ye papa ko bhejo, jinka Aadhaar bank se juda hai.','b',''),
('how','पर लॉक करते कैसे हैं?','Par lock karte kaise hain?','c',''),
('how','माय आधार साइट खुद खोलो. आधार नंबर, कैप्चा, और ओटीपी से लॉगिन.','myAadhaar site khud kholo. Aadhaar number, captcha, aur OTP se login.','b',''),
('how','फिर लॉक अनलॉक बायोमेट्रिक्स. बॉक्स पे टिक, और लॉक.','Phir Lock Unlock Biometrics. Box pe tick, aur Lock.','b',''),
('unlock','पर बैंक में अंगूठा लगाना हो तो?','Par bank mein angootha lagaana ho toh?','c',''),
('unlock','वहीं से दस मिनट का अनलॉक. फिर अपने आप लॉक.','Wahin se das minute ka unlock. Phir apne aap lock.','b',''),
('end','पैसे कटे? तुरंत उन्नीस सौ तीस. पूरी गाइड चाहिए? कमेंट करो गाइड.','Paise kate? Turant 1930. Poori guide chahiye? Comment karo GUIDE.','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='serious',action='full-screen, palm out',rule='hook: the risk in one line',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('bina','b','palm','angry',1),('paise','c','blown','shocked',1)],caps=[('aadhaar','Nakli *angootha*'),('bina','Bina OTP, *paise gaye*')]),
 dict(emotion='worried',action='leans in',rule='won\'t work',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],caps=[('toh','Kuch *nahi* ho sakta?')]),
 dict(emotion='firm',action='stop hand, then thumbs up',rule='unless: the claim, hit on LOCK',hit='lock',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','confused',0),('lock','b','point','smug',1),('bekaar','c','thumb','happy',1)],caps=[('hoga','*Hoga.*'),('bas','Biometric *LOCK* on'),('phir','Nakli angootha *bekaar*')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('ye','*Papa* ko bhejo'),('jinka','Aadhaar *bank se* juda')]),
 dict(emotion='curious',action='shrug',rule='the stay',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('par','Lock *kaise*?')]),
 dict(emotion='explaining',action='counts one',rule='step 1',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('aadhaar','b','explain','explaining',0)],caps=[('myaadhaar','*myAadhaar* khud kholo'),('aadhaar','Aadhaar, captcha, *OTP*')]),
 dict(emotion='explaining',action='points, then thumbs up',rule='step 2',
      keys=[(None,'b','point','explaining',1),(None,'c','idle','neutral',0),('box','b','thumb','happy',1)],caps=[('phir','*Lock/Unlock* Biometrics'),('box','Tick, aur *Lock*')]),
 dict(emotion='confused',action='leans in',rule='the real objection',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('par','Bank mein *angootha*?')]),
 dict(emotion='calm',action='counts, then palm',rule='step 3, hit on LOCK',hit='lock',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('phir','b','palm','smug',1),('apne','c','thumb','happy',1)],caps=[('wahin','*10 minute* ka unlock'),('phir','Phir apne aap *lock*')]),
 dict(emotion='firm',action='stop hand, then waves',rule='step 4 + one ask: GUIDE',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','neutral',0),('poori','b','explain','happy',1),('comment','b','wave','happy',1)],caps=[('paise','Paise kate? *1930*'),('comment','Comment karo *GUIDE*')]),
]
