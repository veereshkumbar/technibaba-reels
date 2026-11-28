# 11:00 tutorial, 28 Nov 2026: "No Service" can mean your number moved to a scammer's eSIM (SIM-upgrade / eSIM call scam). Premium look, Hindi.
# Format 3 (common belief "No Service = tower ki dikkat" -> contradicted: kabhi kabhi number kisi aur ke phone mein).
# Question at 6 s: "Mera number kisi aur ke phone mein kaise chala jaata hai, aur main kya karun?"
# Facts: I4C eSIM warning (India TV 30 Aug 2025; Digit 3 Sep 2025): call posing as telecom provider, eSIM activation link,
#  physical SIM loses network, calls/SMS/OTPs go to scammer's eSIM. I4C tips: never rely on a third party to convert your SIM,
#  request eSIM yourself via official channels; if the phone suddenly loses network, immediately contact bank + mobile provider.
#  TRAI PR 22/2025: TRAI does not call about disconnection; report via Chakshu on Sanchar Saathi. Sanchar Saathi /sfc page
#  (updated 15 Oct 2026): Report Suspected Fraud; money lost -> 1930 / cybercrime.gov.in. Gizmo Times 28 Nov 2026: fake KYC/SIM
#  disconnection calls ask for OTP, APK, eSIM QR scan.
# Gate 3: no named company/person accused; no legal/investment advice.
LINES=[
('hook','बाबा! पापा के फ़ोन में अचानक नो सर्विस!','Baba! Papa ke phone mein achanak No Service!','c',''),
('hook','सब सोचते हैं, टावर की दिक्कत. पर कभी कभी, नंबर किसी और के फ़ोन में.','Sab sochte hain, tower ki dikkat. Par kabhi kabhi, number kisi aur ke phone mein.','b',''),
('share','पापा को भेजो, जो कस्टमर केयर की हर बात मानते हैं.','Papa ko bhejo, jo customer care ki har baat maante hain.','b',''),
('share','पर नंबर गया कैसे?','Par number gaya kaise?','c',''),
('how','कॉल आता है, सिम अपग्रेड करो. लिंक दबाया, नंबर और ओटीपी, स्कैमर की ई-सिम पे.','Call aata hai, SIM upgrade karo. Link dabaya, number aur OTP, scammer ki eSIM pe.','b',''),
('s1','पहला: सिम अपग्रेड का कॉल? काट दो. ई-सिम सिर्फ़ ख़ुद, ऑफ़िशियल ऐप या स्टोर से.','Pehla: SIM upgrade ka call? Kaat do. eSIM sirf khud, official app ya store se.','b',''),
('s2','दूसरा: नेटवर्क अचानक गया? तुरंत बैंक और कंपनी को कॉल.','Doosra: network achanak gaya? Turant bank aur company ko call.','b',''),
('s3','तीसरा: संचार साथी पे चक्षु रिपोर्ट. पैसे गए, तो उन्नीस तीस.','Teesra: Sanchar Saathi pe Chakshu report. Paise gaye, toh 1930.','b',''),
('end','नो सर्विस, यानी अलर्ट. कमेंट करो गाइड.','No Service, yaani alert. Comment karo GUIDE.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up the phone',rule='hook: the No Service bar, frame 0',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('service','c','blown','shocked',1)],
      caps=[('baba','*Papa* ka phone'),('service','No *Service*')]),
 dict(emotion='calm-firm',action='counts, then points',rule='format 3: common belief then contradiction by ~6 s, hit on NUMBER',hit='number',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','confused',0),('number','b','point','smug',1),('phone','b','palm','explaining',1)],
      caps=[('sab','Tower ki *dikkat*?'),('number','*Number* kisi aur ke paas')]),
 dict(emotion='warm',action='points out of frame',rule='share ask in the middle, one named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('customer','b','explain','explaining',1)],
      caps=[('papa','*Papa* ko bhejo'),('customer','Customer care pe *bharosa*')]),
 dict(emotion='confused',action='shrug',rule='the planted question, in the viewer words',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0),('kaise','c','phone','confused',1)],
      caps=[('par','Gaya *kaise*?')]),
 dict(emotion='explaining',action='phone gesture then palm',rule='mechanism: call, link, eSIM, OTP',
      keys=[(None,'b','phone','explaining',1),(None,'c','idle','neutral',0),('link','b','point','angry',1),('otp','c','blown','shocked',1)],
      caps=[('call','SIM *upgrade* call'),('link','Link = *eSIM* unki'),('otp','*OTP* bhi unka')]),
 dict(emotion='decisive',action='stop hand',rule='step 1: cut the call, hit on KAAT',hit='kaat',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','shocked',0),('kaat','b','stop','smug',1),('esim','b','explain','explaining',1)],
      caps=[('pehla','*Upgrade* call?'),('kaat','*Kaat do*'),('esim','eSIM sirf *khud*')]),
 dict(emotion='urgent',action='phone',rule='step 2: act fast on sudden No Service',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('turant','b','phone','angry',1)],
      caps=[('doosra','Network *gaya*?'),('turant','*Turant* bank + company')]),
 dict(emotion='explaining',action='counts, thumb',rule='step 3: report, 1930',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('paise','b','point','explaining',1)],
      caps=[('teesra','*Chakshu* pe report'),('paise','Paise gaye? *1930*')]),
 dict(emotion='happy',action='waves',rule='payoff + one ask: GUIDE, loops back to the hook',
      keys=[(None,'b','thumb','happy',1),(None,'c','thumb','happy',0),('comment','b','wave','happy',1),('guide','c','thumb','happy',1)],
      caps=[('no','No Service = *alert*'),('comment','Comment karo *GUIDE*')]),
]
