# 11:00 tutorial, 26 Nov 2026: "Virus detected" alerts on Papa's phone = website notifications he allowed in Chrome. Premium look, Hindi.
# Format 2 (not A, not B, actually C). Question at 6 s: "Allow dabane se virus wala alert kaise aata hai, aur band kaise hoga?"
# Paths verified today: Chrome (Android) > More (three dots) > Settings > Site settings > Notifications > tap the site > Block
#  (Malwarebytes "Why scammers want you to allow notifications", 12 Nov 2026; Digital Citizen guide; Android Authority 11 Aug 2026
#  also gives Chrome > three dots > Settings > Notifications). Chrome auto-revokes for some low-engagement sites (Google blog, 10 Oct 2025).
# Facts: the permission lets a site push alerts even when you are not on it, incl. fake virus / payment / legal warnings; a malware
#  scan finds nothing because the permission is not malware (Malwarebytes, 12 Nov 2026).
# Gate 3: no named company or person accused; generic site names only; no money/medical/legal advice.
LINES=[
('nota','बाबा! पापा के फ़ोन पे रोज़ वायरस डिटेक्टेड!','Baba! Papa ke phone pe roz Virus Detected!','c',''),
('nota','वायरस नहीं है. हैकर भी नहीं. पापा ने किसी वेबसाइट पे अलाउ दबाया था.','Virus nahi hai. Hacker bhi nahi. Papa ne kisi website pe Allow dabaya tha.','b',''),
('share','ये रील पापा को भेजो, जिनका फ़ोन वायरस चिल्लाता है.','Ye reel Papa ko bhejo, jinka phone virus chillata hai.','b',''),
('allow','सिर्फ़ अलाउ? उससे क्या होता है?','Sirf Allow? Usse kya hota hai?','c',''),
('allow','वो साइट अब जब चाहे नकली अलर्ट भेजती है. वायरस, बिल, पुलिस.','Woh site ab jab chahe nakli alert bhejti hai. Virus, bill, police.','b',''),
('path','क्रोम खोलो. तीन डॉट, सेटिंग्स, साइट सेटिंग्स, नोटिफ़िकेशन्स.','Chrome kholo. Teen dot, Settings, Site settings, Notifications.','b',''),
('path','अरे, यहाँ तो दस साइट्स हैं!','Arre, yahan toh das sites hain!','c',''),
('block','हर अनजान साइट पे टैप करो. ब्लॉक. ख़त्म.','Har anjaan site pe tap karo. Block. Khatam.','b',''),
('next','आगे से कोई साइट पूछे, अलाउ? दबाओ ब्लॉक.','Aage se koi site poochhe, Allow? Dabao Block.','b',''),
('end','वायरस नहीं था, अलाउ था. कमेंट करो गाइड.','Virus nahi tha, Allow tha. Comment karo GUIDE.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up the phone',rule='hook: the alert the viewer has seen, frame 0',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('virus','c','blown','shocked',1)],
      caps=[('papa','*Papa* ka phone'),('virus','*Virus detected*?')]),
 dict(emotion='calm-firm',action='stop hand, then points',rule='format 2: not A, not B, actually C by ~6 s, hit on ALLOW',hit='allow',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('hacker','b','count','explaining',1),('allow','b','point','smug',1)],
      caps=[('virus','*Virus* nahi'),('hacker','*Hacker* bhi nahi'),('allow','*Allow* dabaya tha')]),
 dict(emotion='warm',action='points out of frame',rule='share ask in the middle, one named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('chillata','b','explain','explaining',1)],
      caps=[('ye','*Papa* ko bhejo'),('jinka','Jinka phone *virus* bole')]),
 dict(emotion='confused',action='shrug',rule='the planted question, in the viewer words',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],
      caps=[('sirf','Sirf *Allow*?')]),
 dict(emotion='explaining',action='explains, counts three',rule='the mechanism, three fake alerts',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','shocked',0),('virus','b','count','explaining',1)],
      caps=[('woh','Jab chahe *alert*'),('virus','Virus, *bill*, police')],cams=[('police','cu','b')]),
 dict(emotion='explaining',action='counts the taps, palm open',rule='step 1: the exact path',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('site','b','palm','explaining',1)],
      caps=[('chrome','*Chrome* > 3 dot'),('site','*Site settings*')]),
 dict(emotion='shocked',action='leans in, hands blown',rule='listener reaction keeps the loop open',
      keys=[(None,'c','leanin','shocked',1),(None,'b','idle','smug',0)],
      caps=[('das','*10 sites*?')]),
 dict(emotion='decisive',action='taps, then stop hand',rule='step 2: block, hit on BLOCK',hit='block',
      keys=[(None,'b','point','angry',1),(None,'c','idle','shocked',0),('block','b','stop','smug',1),('khatam','c','thumb','happy',1)],
      caps=[('har','*Anjaan site* pe tap'),('block','*Block*')]),
 dict(emotion='explaining',action='explains, thumbs up',rule='step 3: the habit',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('dabao','b','thumb','happy',1)],
      caps=[('aage','Aage se *Allow*?'),('dabao','Dabao *Block*')]),
 dict(emotion='happy',action='waves',rule='payoff + one ask: GUIDE, loops back to the hook',
      keys=[(None,'b','thumb','happy',1),(None,'c','thumb','happy',0),('comment','b','wave','happy',1),('guide','c','thumb','happy',1)],
      caps=[('virus','Virus nahi, *Allow*'),('comment','Comment karo *GUIDE*')]),
]
