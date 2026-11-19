# Split-layout reel, 06:38 morning tutorial: "Courier wale ne code dial karwaya? ##002#: call forwarding scam se bachne ke 4 step"  c = Chotu, b = Techni Baba.
LINES=[
('q','बाबा! कूरियर वाले का कोड डायल किया, अब कॉल आना बंद!','Baba! Courier wale ka code dial kiya, ab call aana BAND!','c',''),
('q','तुम्हारे कॉल और ओ टी पी, चोर के फ़ोन पे! अभी डायल करो, हैश हैश, ज़ीरो ज़ीरो टू, हैश!','Tumhare call aur OTP, chor ke phone pe! Abhi dial karo, ##002#!','b',''),
('send','ये पापा को भेजो, जो कूरियर वाले की हर बात मानते हैं!','Ye PAPA ko bhejo, jo courier wale ki har baat maante hain!','c',''),
('code','पहला: अनजान का कोड मत डायल करो. स्टार इक्कीस? खतरा!','Pehla: anjaan ka code mat dial karo. Star 21? KHATRA!','b',''),
('check','दूसरा: सेटिंग्स में कॉल फ़ॉरवर्डिंग देखो. ऑन है? गड़बड़.','Doosra: settings mein Call forwarding dekho. ON hai? Gadbad.','b',''),
('off','तीसरा: हैश हैश, ज़ीरो ज़ीरो टू, हैश. सब बंद. जियो पे, स्टार चार सौ दो.','Teesra: ##002#. Sab band. Jio pe, star 402.','b',''),
('off','और मेरे कॉल वापस!','Aur mere call WAPAS!','c',''),
('help','चौथा: पैसे कटे? तुरंत उन्नीस सौ तीस.','Chautha: paise kate? Turant 1930.','b',''),
('end','कमेंट करो गाइड. और देखो, तुम्हारे कॉल कहीं और तो नहीं जा रहे?','Comment karo GUIDE. Aur dekho, tumhare call kahin aur toh nahi ja rahe?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.26,1.06),'b':('file:vo_in/b_{i:02d}.wav',1.0,1.0,('kokoro:hm_omega',1.22,0.95))}
BEATS=[
 dict(emotion='panicked',action='phone up, then hands on head',rule='hook by 1.5s, full-screen payoff before the split',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('call','c','blown','shocked',1)],caps=[('baba','Courier ka *CODE*'),('call','Call aana *BAND*!')]),
 dict(emotion='urgent',action='points, stop hand',rule='panel drops in; payoff ##002# said by 8s',
      keys=[(None,'b','point','explaining',1),(None,'c','idle','shocked',0),('chor','b','stop','angry',0),('dial','b','phone','explaining',1)],caps=[('tumhare','Call + OTP → *CHOR*'),('abhi','Dial: *##002#*')]),
 dict(emotion='excited',action='points at viewer, phone',rule='share ask at 8-12s, big text + SFX',
      keys=[(None,'c','point','happy',1),(None,'b','idle','happy',0),('papa','c','phone','happy',1)],caps=[('ye','*PAPA* ko bhejo'),('courier','Courier = *har baat*')]),
 dict(emotion='stern',action='stop hand, counts',rule='one visual: dial pad with a red code',hit='khatra',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','confused',0),('star','b','point','explaining',0),('khatra','c','blown','shocked',1)],caps=[('pehla','1 · *MAT DIAL*'),('star','*STAR 21*... ?'),('khatra','*KHATRA*')]),
 dict(emotion='explaining',action='explains, points up',rule='one visual: settings screen, forwarding row ON',
      keys=[(None,'b','explain','explaining',1),(None,'c','phone','neutral',0),('on','c','leanin','confused',0),('gadbad','b','palm','smug',1)],caps=[('doosra','2 · *CHECK*'),('call','*Call forwarding*'),('on','ON = *gadbad*')]),
 dict(emotion='confident',action='phone, thumb',rule='code types in, toggle flips OFF',
      keys=[(None,'b','phone','explaining',1),(None,'c','idle','neutral',0),('band','b','thumb','happy',1),('jio','b','count','explaining',0)],caps=[('teesra','3 · *##002#*'),('sab','Sab *BAND*'),('jio','Jio: *STAR 402*')]),
 dict(emotion='relieved',action='hands up',rule='hit-stop on WAPAS',hit='wapas',
      keys=[(None,'c','up','happy',1),(None,'b','idle','smug',0)],caps=[('aur','Call *WAPAS*!')]),
 dict(emotion='serious',action='point',rule='one visual: 1930 card',
      keys=[(None,'b','point','explaining',1),(None,'c','idle','neutral',0),('1930','c','thumb','neutral',0)],caps=[('chautha','4 · *Paise kate?*'),('turant','Turant *1930*')]),
 dict(emotion='warm',action='points, waves, loops to the hook',rule='one ask: GUIDE, last line loops',
      keys=[(None,'b','point','happy',1),(None,'c','idle','happy',0),('guide','b','thumb','happy',1),('guide','c','wave','happy',0),('dekho','b','leanin','smug',0),('kahin','c','shrug','confused',1),('nahi','b','point','smug',0)],caps=[('comment','Comment *GUIDE*'),('dekho','Aapke call *kahan*?')]),
]
