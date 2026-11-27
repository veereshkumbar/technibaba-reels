# 11:00 tutorial, 27 Nov 2026: hidden UPI AutoPay mandates on Papa's phone. Premium look, Hindi.
# Format 3 (common belief "ek PIN = ek payment" -> contradicted: AutoPay PIN = har mahine). Question at 6 s:
#  "Kaise pata karun mere phone pe kaunse AutoPay chal rahe hain, aur band kaise karun?"
# Paths verified today: Google Pay: profile picture > Autopay > Live tab > tap mandate > Cancel autopay > UPI PIN
#  (support.google.com/pay/india/answer/10840624). PhonePe: profile picture > Payment Management > AutoPay > select > Remove AutoPay
#  (PhonePe help centre). Generic: Profile/Settings > AutoPay/Mandates > Active/Live > Cancel/Revoke > UPI PIN (HDFC Bank).
#  Scam sign: one-time 'bill'/'KYC' approval request that says "Recurring" (PhonePe Trust & Safety blog, 4 Mar 2026).
# Gate 3: no named company/person accused; no investment/legal advice.
LINES=[
('hook','बाबा! पापा ने एक बार पिन डाला, अब हर महीने पैसे कट रहे हैं!','Baba! Papa ne ek baar PIN daala, ab har mahine paise kat rahe hain!','c',''),
('hook','सब सोचते हैं, एक पिन, एक पेमेंट. पर ऑटोपे पे, कटौती हर महीने.','Sab sochte hain, ek PIN, ek payment. Par AutoPay pe, katauti har mahine.','b',''),
('share','ये रील पापा को भेजो, जो हर रिक्वेस्ट पे पिन डालते हैं.','Ye reel Papa ko bhejo, jo har request pe PIN daalte hain.','b',''),
('share','पर पता कैसे चले, कौन सा ऑटोपे चल रहा है?','Par pata kaise chale, kaunsa AutoPay chal raha hai?','c',''),
('gpay','गूगल पे में: प्रोफ़ाइल फ़ोटो, ऑटोपे, लाइव टैब.','Google Pay mein: profile photo, Autopay, Live tab.','b',''),
('ppe','फ़ोनपे में: प्रोफ़ाइल, पेमेंट मैनेजमेंट, ऑटोपे.','PhonePe mein: profile, Payment Management, AutoPay.','b',''),
('ppe','अरे, ये तीन तो पापा ने कभी लिए ही नहीं!','Arre, ye teen toh Papa ne kabhi liye hi nahi!','c',''),
('cancel','अनजान वाले पे टैप करो. कैंसल, यूपीआई पिन. ख़त्म.','Anjaan wale pe tap karo. Cancel, UPI PIN. Khatam.','b',''),
('next','बिल की रिक्वेस्ट पे रिकरिंग लिखा? तो डिक्लाइन.','Bill ki request pe Recurring likha? Toh Decline.','b',''),
('end','एक पिन, हर महीने. ऑटोपे चेक करो. कमेंट करो गाइड.','Ek PIN, har mahine. AutoPay check karo. Comment karo GUIDE.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up the phone',rule='hook: the monthly debit the viewer fears, frame 0',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('mahine','c','blown','shocked',1)],
      caps=[('ek','Ek baar *PIN*'),('mahine','Har *mahine* kat raha')]),
 dict(emotion='calm-firm',action='counts, then points',rule='format 3: common belief then contradiction by ~6 s, hit on AUTOPAY',hit='autopay',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','confused',0),('autopay','b','point','smug',1),('katauti','b','palm','explaining',1)],
      caps=[('sab','Ek PIN = *ek payment*?'),('autopay','*AutoPay* = har mahine')]),
 dict(emotion='warm',action='points out of frame',rule='share ask in the middle, one named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('request','b','explain','explaining',1)],
      caps=[('ye','*Papa* ko bhejo'),('request','Jo har *request* pe PIN')]),
 dict(emotion='confused',action='shrug',rule='the planted question, in the viewer words',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0),('autopay','c','phone','confused',1)],
      caps=[('par','Kaunsa *AutoPay* chalu?')]),
 dict(emotion='explaining',action='counts the taps',rule='step 1a: exact Google Pay path',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('live','b','palm','explaining',1)],
      caps=[('google','*Google Pay*'),('autopay','Autopay > *Live*')]),
 dict(emotion='explaining',action='counts the taps',rule='step 1b: exact PhonePe path',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('payment','b','count','explaining',1)],
      caps=[('phonepe','*PhonePe*'),('payment','Payment Mgmt > *AutoPay*')]),
 dict(emotion='shocked',action='leans in',rule='listener reaction keeps the loop open',
      keys=[(None,'c','leanin','shocked',1),(None,'b','idle','smug',0)],
      caps=[('teen','*3* anjaan AutoPay')]),
 dict(emotion='decisive',action='taps, then stop hand',rule='step 2: cancel, hit on CANCEL',hit='cancel',
      keys=[(None,'b','point','angry',1),(None,'c','idle','shocked',0),('cancel','b','stop','smug',1),('khatam','c','thumb','happy',1)],
      caps=[('anjaan','*Anjaan* pe tap'),('cancel','*Cancel* + UPI PIN')]),
 dict(emotion='explaining',action='explains, stop hand',rule='step 3: the scam sign',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('decline','b','stop','smug',1)],
      caps=[('bill','Bill pe *Recurring*?'),('decline','*Decline*')]),
 dict(emotion='happy',action='waves',rule='payoff + one ask: GUIDE, loops back to the hook',
      keys=[(None,'b','thumb','happy',1),(None,'c','thumb','happy',0),('comment','b','wave','happy',1),('guide','c','thumb','happy',1)],
      caps=[('ek','Ek PIN, *har mahine*'),('comment','Comment karo *GUIDE*')]),
]
