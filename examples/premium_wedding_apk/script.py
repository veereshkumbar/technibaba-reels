# Morning tutorial 23 Nov 2026: wedding-card APK blocked by "Install unknown apps" OFF (premium look, Hindi). Format 1: result first, then how.
# Facts: wedding-invite APK frauds (Janjgir police arrest, cgkhabar 16 Nov 2026; Bengaluru Rs 9.96 lakh, the420 Jul 2026; Hyderabad advisory, ETV Bharat May 2026:
#  "Genuine invitations are in PDF or JPG formats. Treat APK files as fraud", call the sender, if installed: internet off, uninstall, change PINs, 1930).
# Path: Pixel Help 7391672: Apps > Special app access > Install unknown apps > app > "Allow from this source"; Samsung: Settings search "Install unknown apps".
# Play Protect: Google Android Help 2812853: Play Store > profile icon > Play Protect > Settings > "Scan apps with Play Protect".
LINES=[
('q','बाबा! शादी का कार्ड खोला, फ़ोन बोला, ये ऐप इंस्टॉल नहीं होगा!','Baba! Shaadi ka card khola, phone bola, ye app install nahi hoga!','c',''),
('q','बढ़िया. वो कार्ड नहीं, ए पी के था. एक सेटिंग ने रोका.','Badhiya. Woh card nahi, APK tha. Ek setting ne roka.','b',''),
('q','कौन सी सेटिंग? मेरे पापा तो हर कार्ड खोल देते हैं!','Kaun si setting? Mere papa toh har card khol dete hain!','c',''),
('rule','तो पापा को भेजो. असली कार्ड पी डी एफ या फ़ोटो होता है.','Toh papa ko bhejo. Asli card PDF ya photo hota hai.','b',''),
('how','सेटिंग्स में सर्च करो, इंस्टॉल अननोन ऐप्स. व्हाट्सऐप चुनो, और ऑफ़.','Settings mein search karo, Install unknown apps. WhatsApp chuno, aur OFF.','b',''),
('how','और क्रोम, फ़ाइल्स?','Aur Chrome, Files?','c',''),
('how','सब ऑफ़. फिर प्ले स्टोर में, प्ले प्रोटेक्ट, स्कैन ऑन.','Sab OFF. Phir Play Store mein, Play Protect, scan ON.','b',''),
('trap','पर कार्ड भेजने वाला बोले, सेटिंग्स दबाओ?','Par card bhejne wala bole, Settings dabao?','c',''),
('trap','वहीं रुकना, वही चाल है. पहले कॉल करके पूछो.','Wahin rukna, wahi chaal hai. Pehle call karke poocho.','b',''),
('end','गलती से खुल गया? नेट बंद, बैंक को कॉल, उन्नीस सौ तीस. कमेंट करो गाइड.','Galti se khul gaya? Net band, bank ko call, 1930. Comment karo GUIDE.','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='relieved-shocked',action='full-screen, holds up phone',rule='hook: the result first (install blocked)',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('phone','c','blown','shocked',1)],caps=[('baba','Shaadi ka *card* khola'),('phone','Install *nahi* hoga')]),
 dict(emotion='smug',action='thumbs up, then points',rule='the claim by 6 s: APK + one setting',hit='apk',
      keys=[(None,'b','thumb','smug',1),(None,'c','idle','confused',0),('apk','b','point','explaining',1),('ek','b','count','smug',1)],caps=[('badhiya','Card nahi, *APK* tha'),('ek','*Ek setting* ne roka')]),
 dict(emotion='curious',action='leans in',rule='the planted question',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0),('mere','c','shrug','shocked',1)],caps=[('kaun','Kaun si *setting*?'),('mere','Papa *har card* kholte')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask at 8-12 s',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('asli','b','explain','explaining',1)],caps=[('toh','*Papa* ko bhejo'),('asli','Asli card: *PDF/photo*')]),
 dict(emotion='explaining',action='counts one',rule='step 1',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('whatsapp','b','stop','explaining',1)],caps=[('settings','Search: *Install unknown*'),('whatsapp','WhatsApp: *OFF*')]),
 dict(emotion='curious',action='shrug',rule='listener question',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('aur','*Chrome*, Files?')]),
 dict(emotion='explaining',action='palm, then thumbs up',rule='step 2',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('play','b','point','explaining',1),('scan','c','thumb','happy',1)],caps=[('sab','Sab *OFF*'),('phir','*Play Protect* scan ON')]),
 dict(emotion='worried',action='leans in',rule='the real objection: the scammer coaches you',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('par','"*Settings* dabao"?')]),
 dict(emotion='firm',action='stop hand',rule='step 3, hit on RUKNA',hit='rukna',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','shocked',0),('pehle','b','phone','explaining',1),('poocho','c','thumb','happy',1)],caps=[('wahin','Wahin *RUKO*'),('pehle','Pehle *call* karo')]),
 dict(emotion='firm',action='counts, then waves',rule='step 4 + one ask: GUIDE',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('comment','b','wave','happy',1)],caps=[('galti','Net band, *bank* ko call'),('1930','Turant *1930*'),('comment','Comment karo *GUIDE*')]),
]
