# 11:00 tutorial, 25 Nov 2026: who is still logged into your WhatsApp — Linked devices check + Log out. Premium look, Hindi.
# Format 1 (result first). Question at 6 s: "Mere WhatsApp mein kiska laptop juda hua hai, aur usko nikalta kaise hoon?"
# Paths verified today: WhatsApp > more options (Android three dots) / Settings (iPhone) > Linked devices > tap the device > Log out
#  (WhatsApp help "About linked devices", faq.whatsapp.com/378279804439436; Gulf News 1 Oct 2026; Beebom).
# Facts: linked devices keep working with the phone offline; disconnected only after 30 days of inactivity (or 14 days of
#  the phone being unused); up to 4 devices at a time (WhatsApp help). NCTAU/I4C advisory "Safe Use of WhatsApp Web",
#  18 Nov 2026: log out manually, closing the tab is not enough, review linked devices (CIOL 23 Nov, Lapaas Voice 24 Nov).
# Gate 3: no espionage/political framing, no named person or company accused — only the advisory and the official paths.
LINES=[
('res','ये देखो. एक अनजान लैपटॉप मेरे व्हाट्सऐप से बाहर. दो टैप में.','Ye dekho. Ek anjaan laptop mere WhatsApp se bahar. Do tap mein.','b',''),
('res','अनजान लैपटॉप?! मेरे व्हाट्सऐप में भी कोई जुड़ा होगा?','Anjaan laptop?! Mere WhatsApp mein bhi koi juda hoga?','c',''),
('why','टैब बंद किया? व्हाट्सऐप वहाँ तीस दिन तक लॉगिन रहता है.','Tab band kiya? WhatsApp wahan 30 din tak login rehta hai.','b',''),
('share','ये रील उस दोस्त को भेजो जो दूसरे के लैपटॉप पे व्हाट्सऐप खोले.','Ye reel us dost ko bhejo jo dusre ke laptop pe WhatsApp khole.','b',''),
('path','एंड्रॉइड में तीन डॉट, आईफ़ोन में सेटिंग्स. लिंक्ड डिवाइसेस.','Android mein teen dot, iPhone mein Settings. Linked devices.','b',''),
('path','लिस्ट में कोई अनजान डिवाइस दिखा तो?','List mein koi anjaan device dikha toh?','c',''),
('out','उस डिवाइस पे टैप करो. लॉग आउट. ख़त्म.','Us device pe tap karo. Log out. Khatam.','b',''),
('keep','और आगे से?','Aur aage se?','c',''),
('keep','हर महीने ये लिस्ट देख लो. चार डिवाइस तक जुड़ सकते हैं.','Har mahine ye list dekh lo. Char device tak jud sakte hain.','b',''),
('end','अब व्हाट्सऐप सिर्फ़ आपके फ़ोन में. कमेंट करो गाइड.','Ab WhatsApp sirf aapke phone mein. Comment karo GUIDE.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='calm-proud',action='full-screen, holds up the phone with the empty list',rule='hook: the finished result at frame 0',
      keys=[(None,'b','phone','smug',1),(None,'c','idle','neutral',0),('bahar','b','thumb','happy',1)],
      caps=[('dekho','Kisi aur ka *laptop*'),('bahar','*2 tap* mein bahar')]),
 dict(emotion='alarmed',action='leans in, hands blown up',rule='the planted question, in the viewer words',
      keys=[(None,'c','leanin','shocked',1),(None,'b','idle','smug',0),('bhi','c','blown','shocked',1)],
      caps=[('anjaan','*Mere* phone mein bhi?')]),
 dict(emotion='firm',action='stop hand, then counts',rule='the claim by ~7 s, hit on 30',hit='30',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','confused',0),('30','b','count','smug',1)],
      caps=[('tab','*Tab band* = logout nahi'),('30','*30 din* tak login')]),
 dict(emotion='warm',action='points out of frame',rule='share ask in the middle, one named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('laptop','b','explain','explaining',1)],
      caps=[('ye','Us *dost* ko bhejo'),('dusre','Jo *dusre ke laptop* pe')]),
 dict(emotion='explaining',action='counts two, palm open',rule='step 1: the exact path, both phones',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('linked','b','palm','explaining',1)],
      caps=[('android','*3 dot* ya Settings'),('linked','*Linked devices*')]),
 dict(emotion='curious',action='shrug',rule='listener question keeps the loop open',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],
      caps=[('koi','*Anjaan device* dikha?')]),
 dict(emotion='decisive',action='taps, then stop hand',rule='step 2: the two taps, hit on OUT',hit='out',
      keys=[(None,'b','point','angry',1),(None,'c','idle','shocked',0),('log','b','stop','smug',1),('khatam','c','thumb','happy',1)],
      caps=[('us','Us device pe *tap*'),('log','*Log out* = khatam')]),
 dict(emotion='curious',action='leans in',rule='listener sets up the last step',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],
      caps=[('aur','Aur *aage* se?')]),
 dict(emotion='explaining',action='explains, thumbs up',rule='step 3: the habit + the 4-device limit',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('char','b','thumb','happy',1)],
      caps=[('har','*Har mahine* list dekho'),('char','Sirf *4 device* jud sakte')]),
 dict(emotion='happy',action='waves',rule='payoff + one ask: GUIDE, loops back to the hook',
      keys=[(None,'b','thumb','happy',1),(None,'c','thumb','happy',0),('comment','b','wave','happy',1)],
      caps=[('ab','Sirf *aapka phone*'),('comment','Comment karo *GUIDE*')]),
]
