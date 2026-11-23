# 21:00 Bollywood x tech 23 Nov 2026: Drishyam 3 hits Netflix 27 Nov -> why your new 4K TV still plays HD. Format 5: won't work, unless (the whole chain is 4K).
# Facts: Netflix Help "Plans and Pricing" India (help.netflix.com/en/node/24926/in): Mobile 149 / Basic 199 (720p) / Standard 499 (1080p) / Premium 649 = only plan with 4K (Ultra HD) + HDR.
# Netflix Help "How to get the best video quality" (help.netflix.com/en/node/13444): check the title's details page for a 4K label; every device in the chain (TV, streaming stick, receiver) must support 4K;
# use an HDMI port with HDCP 2.2 or later (usually HDMI 1) and Premium High Speed / Ultra High Speed HDMI cables; if any part falls short Netflix plays the highest quality that part supports; Netflix adapts to connection speed.
# Drishyam: The Conclusion (Drishyam 3, Hindi) on Netflix 27 Nov (Esquire India 23 Nov, Koimoi 23 Nov). We do NOT claim the film itself is in 4K.
LINES=[
('q','बाबा! दृश्यम तीन के लिए नया फोर के टीवी लिया. फिर भी एच डी!','Baba! Drishyam 3 ke liye naya 4K TV liya. Phir bhi HD!','c',''),
('claim','फोर के नहीं चलेगा, जब तक पूरी चेन फोर के ना हो.','4K nahi chalega, jab tak poori chain 4K na ho.','b',''),
('share','उस दोस्त को भेजो, जो प्रीमियम भर के भी एच डी देख रहा है.','Us dost ko bhejo, jo Premium bhar ke bhi HD dekh raha hai.','b',''),
('chain','कौन सी चेन?','Kaun si chain?','c',''),
('plan','एक, प्लान. नेटफ्लिक्स पे फोर के सिर्फ प्रीमियम में, छह सौ उनचास.','Ek, plan. Netflix pe 4K sirf Premium mein, 649.','b',''),
('label','दो, फिल्म के पेज पे फोर के लिखा हो.','Do, film ke page pe 4K likha ho.','b',''),
('port','तीन, स्टिक को एच डी सी पी दो पॉइंट दो वाले पोर्ट में लगाओ, अक्सर एच डी एम आई वन.','Teen, stick ko HDCP 2.2 wale port mein lagao, aksar HDMI 1.','b',''),
('rule','एक भी कड़ी कमज़ोर, तो नेटफ्लिक्स उसी की क्वालिटी पे चलेगा.','Ek bhi kadi kamzor, toh Netflix usi ki quality pe chalega.','b',''),
('end','आपका टीवी, फोर के या एच डी?','Aapka TV, 4K ya HD?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='frustrated',action='full-screen, palms up at the TV',rule='hook: the payoff problem on frame 0',
      keys=[(None,'c','shrug','angry',1),(None,'b','idle','neutral',0),('naya','c','up','happy',1),('phir','c','leanin','shocked',1)],caps=[('baba','Naya *4K* TV'),('phir','Phir bhi *HD*')]),
 dict(emotion='calm, certain',action='stop hand, then counts, hit on KAMZOR',rule='format 5 claim by ~5 s: won\'t work unless the whole chain is 4K',hit='chain',
      keys=[(None,'b','stop','neutral',1),(None,'c','idle','confused',0),('jab','b','explain','explaining',1),('chain','b','point','smug',1),('na','c','blown','shocked',1)],
      caps=[('4k','4K *nahi* chalega'),('jab','Jab tak *chain* 4K na ho')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask, named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('premium','c','wave','happy',1),('dekh','b','thumb','happy',1)],caps=[('us','Us *dost* ko bhejo'),('premium','Premium, phir bhi *HD*')]),
 dict(emotion='curious, excited',action='leans in',rule='the stay: which chain? + the film hook',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0),],caps=[('kaun','Kaun si *chain*?')]),
 dict(emotion='explaining',action='counts one',rule='link 1',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('netflix','b','explain','explaining',1),('sirf','b','point','smug',1),('649','c','thumb','neutral',1)],
      caps=[('ek','Kadi 1: *plan*'),('netflix','4K sirf *Premium*'),('649','Rs *649*')]),
 dict(emotion='explaining',action='counts two',rule='link 2',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('page','b','explain','explaining',1),('likha','c','thumb','happy',1)],
      caps=[('do','Kadi 2: *film*'),('page','Page pe *4K* label')]),
 dict(emotion='smug reveal',action='points, hit on PORT',rule='link 3, the one nobody checks',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','confused',0),('stick','b','point','smug',1),('aksar','c','blown','shocked',1)],
      caps=[('teen','Kadi 3: *port*'),('stick','*HDCP 2.2* port'),('port','Stick *yahan* lagao'),('aksar','Aksar *HDMI 1*')]),
 dict(emotion='explaining',action='palm, then shrug',rule='the why closes the loop (hit)',hit='kamzor',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('kamzor','b','point','smug',1),('quality','c','thumb','happy',1)],
      caps=[('ek','Ek kadi *kamzor*'),('netflix','Usi ki *quality*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('4k','b','wave','happy',1),('hd','c','thumb','happy',1)],caps=[('aapka','Aapka TV: *4K* ya HD?')]),
]
