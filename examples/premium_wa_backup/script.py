# 10:00 trending tech 20 Nov 2026: WhatsApp's own cloud backup (premium look, Hindi). Format 3: common belief (backup = Google Drive, full = band) -> contradict.
# Facts (17 Nov 2026): WhatsApp testing its own cloud backup on Android beta 2.26.46.4, 2 GB free, gradual rollout (Beebom, NewsBytes, Tbreak, Nokiamob, Digit).
# Path per WhatsApp Help Centre as quoted by Tbreak: Settings > Chats > Chat backup > Cloud backup > WhatsApp or Google.
# Always end-to-end encrypted: passkey by default or 64-digit key (Beebom, Nokiamob, Tbreak). Drive backups count against Google storage (Tbreak, WABetaInfo).
LINES=[
('q','गूगल स्टोरेज फुल! अब व्हाट्सऐप का बैकअप गया?','Google storage full! Ab WhatsApp ka backup gaya?','c',''),
('q','ये सोच पुरानी है. रिपोर्ट्स के हिसाब से व्हाट्सऐप अपना क्लाउड ला रहा है. दो जीबी फ्री.','Ye soch purani hai. Reports ke hisaab se WhatsApp apna cloud la raha hai. 2 GB free.','b',''),
('rule','ये पापा को भेजो, जिनका फोन रोज़ स्टोरेज फुल बोलता है.','Ye papa ko bhejo, jinka phone roz storage full bolta hai.','b',''),
('how','पर मेरे फोन में कहाँ मिलेगा?','Par mere phone mein kahan milega?','c',''),
('how','सेटिंग्स, चैट्स, चैट बैकअप. क्लाउड बैकअप में व्हाट्सऐप चुनो.','Settings, Chats, Chat backup. Cloud backup mein WhatsApp chuno.','b',''),
('beta','मुझे तो ऑप्शन दिख ही नहीं रहा!','Mujhe toh option dikh hi nahi raha!','c',''),
('beta','अभी कुछ बीटा यूज़र्स को मिला है. धीरे धीरे सबको आएगा.','Abhi kuch beta users ko mila hai. Dheere dheere sabko aayega.','b',''),
('key','और ध्यान दो: ये बैकअप लॉक रहता है. पासकी या चौंसठ अंक की की. भूले, तो बैकअप गया.','Aur dhyaan do: ye backup lock rehta hai. Passkey ya 64 ank ki key. Bhoole, toh backup gaya.','b',''),
('end','तो आप कौनसा रखोगे, गूगल या व्हाट्सऐप?','Toh aap kaunsa rakhoge, Google ya WhatsApp?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='panic',action='full-screen, phone up',rule='hook: the common belief in one line',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('ab','c','blown','shocked',1)],caps=[('google','Google storage *full*'),('ab','Backup *gaya?*')]),
 dict(emotion='calm',action='palm, then points',rule='contradict: the claim, hit on FREE',hit='free',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','confused',0),('whatsapp','b','explain','explaining',1),('2','b','point','happy',1),('free','c','thumb','happy',1)],caps=[('ye','Soch *purani* hai'),('reports','WhatsApp ka apna *cloud*'),('2','*2 GB* free')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('ye','*Papa* ko bhejo'),('jinka','Roz storage *full*')]),
 dict(emotion='curious',action='shrug',rule='the stay',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('par','*Kahan* milega?')]),
 dict(emotion='explaining',action='counts, then points',rule='the path',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('cloud','b','point','explaining',1),('chuno','c','thumb','happy',0)],caps=[('settings','Settings > *Chats*'),('chat','*Chat backup*'),('cloud','Cloud: *WhatsApp*')]),
 dict(emotion='confused',action='leans in, phone',rule='the real objection',
      keys=[(None,'c','phone','confused',1),(None,'b','idle','smug',0)],caps=[('mujhe','Option *nahi* dikha?')]),
 dict(emotion='calm',action='palm, then explains',rule='honest status: beta',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('dheere','b','explain','happy',1)],caps=[('abhi','Abhi *beta* mein'),('dheere','Dheere dheere *sabko*')]),
 dict(emotion='serious',action='stop hand, hit on GAYA',rule='the catch, hit',hit='gaya',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','neutral',0),('passkey','b','count','explaining',1),('bhoole','b','palm','angry',1),('gaya','c','blown','shocked',1)],caps=[('aur','Backup *lock* rehta'),('passkey','*Passkey* ya 64 ank'),('bhoole','Bhoole = backup *gaya*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('google','b','wave','happy',1)],caps=[('toh','Aap kaunsa *rakhoge?*'),('google','Google ya *WhatsApp?*')]),
]
