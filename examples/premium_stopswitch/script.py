# 7 PM trending 24 Nov 2026: RBI draft "Stop Switch" + Trusted Person (draft directions issued 23 Nov 2026). Premium look, Hindi.
# Format 3 (common belief: "scam ke baad kuch nahi kar sakte" -> contradicted: RBI draft brings a stop switch).
# Question at 6 s: "Ek button se kya rukega? Kaise kaam karega?"
# Facts (Business Standard 23 + 24 Nov, MediaNama 24 Nov, Republic 23 Nov): draft Responsible Business Conduct amendment directions,
#  23 Nov 2026, comments till 14 Dec; stop switch disables all customer-initiated future debits; incoming credits, existing
#  mandates/standing instructions and bank-initiated debits (loan EMIs) continue; trusted person (18+) approves transfers above a
#  customer-set threshold within 1 hour, else declined; UPI, merchant and recurring payments excluded from TPM; banks to offer by
#  1 Jul 2027 or earlier. It is a DRAFT: not available today.
LINES=[
('q','बाबा! स्कैम में पैसे गए, अब कुछ नहीं हो सकता ना?','Baba! Scam mein paise gaye, ab kuch nahi ho sakta na?','c',''),
('q','ग़लत. आर बी आई के ड्राफ़्ट में एक बटन आ रहा है. स्टॉप स्विच.','Galat. RBI ke draft mein ek button aa raha hai. Stop switch.','b',''),
('q','एक बटन से क्या रुकेगा?','Ek button se kya rukega?','c',''),
('share','पहले ये पापा को भेजो, जिन्हें ओ टी पी कॉल आते हैं.','Pehle ye Papa ko bhejo, jinhe OTP call aate hain.','b',''),
('stop','स्विच दबाओ, खाते से हर नया पेमेंट बंद. पैसे आना चालू.','Switch dabao, khaate se har naya payment band. Paise aana chalu.','b',''),
('stop','और ई एम आई?','Aur EMI?','c',''),
('stop','ई एम आई और ऑटो पे चलते रहेंगे.','EMI aur auto-pay chalte rahenge.','b',''),
('trust','बड़ा ट्रांसफ़र? आपका भरोसे वाला इंसान एक घंटे में हाँ बोले, तभी जाएगा.','Bada transfer? Aapka trusted person ek ghante mein haan bole, tabhi jaayega.','b',''),
('when','अभी ड्राफ़्ट है. बैंक जुलाई दो हज़ार सत्ताईस तक देंगे.','Abhi draft hai. Banks July 2027 tak denge.','b',''),
('end','तो कुछ नहीं हो सकता? जल्द होगा. पापा के लिए चाहिए? हाँ या ना.','Toh kuch nahi ho sakta? Jald hoga. Papa ke liye chahiye? HAAN ya NA.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up phone',rule='hook: the common belief, payoff headline on screen',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('kuch','c','blown','shocked',1)],caps=[('baba','Scam mein *paise* gaye'),('ab','Ab kuch *nahi*?')]),
 dict(emotion='calm-smug',action='stop hand, then counts one',rule='contradiction + claim by 6 s, hit on SWITCH',hit='switch',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('ek','b','count','explaining',1)],caps=[('galat','*Galat*'),('rbi','RBI draft: *1 button*'),('stop','*Stop switch*')]),
 dict(emotion='curious',action='leans in',rule='the planted question',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],caps=[('ek','Kya *rukega*?')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask at 8-12 s',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('pehle','*Papa* ko bhejo'),('jinhe','*OTP* call aate hain')]),
 dict(emotion='explaining',action='stop hand, then palm',rule='what it stops: every new payment out',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','neutral',0),('paise','b','palm','happy',1)],caps=[('switch','Har naya payment *band*'),('paise','Paise aana *chalu*')]),
 dict(emotion='doubtful',action='shrug',rule='listener objection',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],caps=[('aur','Aur *EMI*?')]),
 dict(emotion='calm',action='thumbs up',rule='answer: mandates keep running',
      keys=[(None,'b','thumb','happy',1),(None,'c','idle','neutral',0),('chalte','c','thumb','happy',1)],caps=[('emi','EMI, auto-pay *chalu*')]),
 dict(emotion='explaining',action='explains, counts one',rule='trusted person: 1-hour approval, hit on HAAN',hit='haan',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('ek','b','count','explaining',1),('tabhi','c','thumb','happy',1)],caps=[('bada','Bada *transfer*?'),('aapka','*Trusted person*'),('ek','1 ghante mein *haan*')]),
 dict(emotion='honest',action='palm, then point',rule='honest status: draft, date',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('banks','b','point','explaining',1)],caps=[('abhi','Abhi *draft* hai'),('banks','*July 2027* tak')]),
 dict(emotion='happy',action='crosses arms, then waves',rule='loop to the hook + one ask HAAN ya NA',
      keys=[(None,'b','cross','smug',1),(None,'c','idle','neutral',0),('jald','b','thumb','happy',1),('papa','b','wave','happy',1),('chahiye','c','thumb','happy',1)],caps=[('toh','Kuch *nahi* ho sakta?'),('jald','*Jald* hoga'),('papa','*HAAN* ya NA?')]),
]
