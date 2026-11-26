# 19:00 trending, 26 Nov 2026: "Phone pe LIVE, asli live nahi" pegged to NZ vs IND 2nd Test (3:30 AM IST 27 Nov, Sony Sports Network + SonyLIV).
# Format 3 (common belief: LIVE = live -> contradict: 20-30 s behind TV). Question at 6 s: "mera net fast hai, phir peeche kyun?"
# Sources: AWS Media blog (broadcast 3-12 s, OTT 25-30 s, 6 s segments, players buffer 3+ segments); Selectra 2 Nov 2026 (apps 20-45 s,
#  18 s from 3x6 s, low-latency mode / restart after pause help, faster internet does not); DStv (up to 30 s); SI 2018 (20+ s).
# Gate 3: no claim about any specific app's delay; generic "streaming app". No betting.
LINES=[
('live','बाबा! पड़ोसी चिल्लाया आउट, मेरे फ़ोन पे बॉल अभी डली भी नहीं!','Baba! Padosi chillaya OUT, mere phone pe ball abhi dali bhi nahi!','c',''),
('live','फ़ोन पे लाइव, असली लाइव नहीं. रिपोर्ट्स कहती हैं, टीवी से बीस तीस सेकंड पीछे.','Phone pe LIVE, asli live nahi. Reports kehti hain, TV se 20-30 second peeche.','b',''),
('test','कल सुबह साढ़े तीन बजे, दूसरा टेस्ट है.','Kal subah 3:30 baje, doosra Test hai.','b',''),
('test','उस दोस्त को भेजो, जो स्कोर भेज के मैच बिगाड़ता है.','Us dost ko bhejo, jo score bhej ke match bigaadta hai.','b',''),
('why','पर क्यों? मेरा नेट तो फ़ास्ट है!','Par kyun? Mera net toh fast hai!','c',''),
('chunk','नेट नहीं. ऐप वीडियो को अक्सर छह सेकंड के टुकड़ों में काटता है.','Net nahi. App video ko aksar 6 second ke tukdon mein kaat-ta hai.','b',''),
('chunk','प्लेयर तीन टुकड़े जमा करके चलाता है. अठारह सेकंड, यहीं गए.','Player 3 tukde jama karke chalata hai. 18 second, yahin gaye.','b',''),
('fix','तेज़ नेट से भी नहीं जाएगा. ऐप में लो लेटेंसी मोड हो, तो ऑन करो. पॉज़ के बाद, स्ट्रीम दोबारा खोलो.','Tez net se bhi nahi jayega. App mein Low latency mode ho, toh ON karo. Pause ke baad, stream dobara kholo.','b',''),
('end','कल मैच किस पे देखोगे, फ़ोन या टीवी?','Kal match kispe dekhoge, PHONE ya TV?','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up the phone',rule='hook: the spoiler moment, frame 0',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('out','c','blown','shocked',1)],
      caps=[('padosi','Padosi: *OUT!*'),('mere','Phone pe ball *abhi nahi*')]),
 dict(emotion='calm-firm',action='stop hand, then points',rule='format 3: belief LIVE=live, contradicted by ~6 s, hit on PEECHE',hit='peeche',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('reports','b','explain','explaining',1),('peeche','b','point','smug',1)],
      caps=[('phone','Phone pe *LIVE*'),('asli','Asli live *nahi*'),('tv','TV se *20-30 sec* peeche')]),
 dict(emotion='explaining',action='counts, calendar',rule='the peg: why it matters tonight',
      keys=[(None,'b','count','explaining',1),(None,'c','leanin','happy',0)],
      caps=[('kal','Kal subah *3:30*'),('doosra','NZ vs IND *2nd Test*')]),
 dict(emotion='warm',action='points out of frame',rule='share ask in the middle, one named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('score','b','explain','explaining',1)],
      caps=[('us','*Bhejo* us dost ko'),('score','Jo *score* bhej deta hai')]),
 dict(emotion='confused',action='shrug',rule='the planted question in the viewer words',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],
      caps=[('par','Net toh *fast* hai?')]),
 dict(emotion='explaining',action='explains, palm open',rule='mechanism 1: chunks',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','neutral',0),('tukdon','b','explain','explaining',1)],
      caps=[('net','*Net* nahi'),('app','Aksar *6 sec* ke'),('tukdon','*Tukdon* mein video')]),
 dict(emotion='explaining',action='counts three, then points',rule='mechanism 2: buffer, hit on YAHIN',hit='yahin',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','shocked',0),('18','b','palm','smug',1),('yahin','c','blown','shocked',1)],
      caps=[('player','*3 tukde* jama'),('18','*18 sec* yahin gaye')]),
 dict(emotion='firm',action='stop hand, then thumbs up',rule='the real fix, answer completed in the last 30%',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('low','b','explain','explaining',1),('pause','b','thumb','happy',1)],
      caps=[('tez','Tez net? *Nahi*'),('app','*Low latency* ON'),('pause','Pause? *Dobara kholo*')]),
 dict(emotion='happy',action='waves',rule='one ask, loops back to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','thumb','happy',0),('phone','b','wave','happy',1)],
      caps=[('kal','Kal match *kispe*?'),('phone','*PHONE* ya TV?')]),
]
