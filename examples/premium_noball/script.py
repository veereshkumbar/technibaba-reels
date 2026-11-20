# 14:00 trending sports 20 Nov 2026: front-foot no-ball rule + TV umpire tech (premium look, Hindi). Format 2: not A (foot on line), not B (heel in the air), actually C (no part of the foot behind the line).
# Match (20 Nov, Wellington Test day 2): NZ 368 all out, India 159/1 at stumps (PTI via DT Next/OrissaPOST, IANS via Telangana Today, myKhel, m9). Duffy "overstepped repeatedly" after tea (IANS); NZ six no-balls post-tea (myKhel).
# Law: front foot must land with some part of the foot, grounded or raised, behind the popping crease (ICC playing conditions clause 21.5.2; Wikipedia Crease / No-ball: foot on the line is fine if part is behind).
# Tech: front-foot no-balls called by the third umpire, who sees the landing in slow motion, frozen (ICC Feb 2020, Wisden Aug 2019, ESPNcricinfo Jul 2020, ANI Eng-Pak Tests 2020). Late no-ball call -> dismissal rescinded (ICC Dec 2019, ESPNcricinfo Feb 2020, Wikipedia).
LINES=[
('q','बाबा! आज डफी ने बार बार नो-बॉल डाले. पैर लाइन पे था ना?','Baba! Aaj Duffy ne baar baar no-ball daale. Pair line pe tha na?','c',''),
('q','लाइन पे पैर? नो-बॉल नहीं. एड़ी हवा में? वो भी नहीं.','Line pe pair? No-ball nahi. Edi hawa mein? Woh bhi nahi.','b',''),
('q','नो-बॉल तब, जब पैर का एक भी हिस्सा लाइन के पीछे ना हो.','No-ball tab, jab pair ka ek bhi hissa line ke peeche na ho.','b',''),
('rule','ये उस दोस्त को भेजो, जो हर विकेट पे नो-बॉल चिल्लाता है.','Ye us dost ko bhejo, jo har wicket pe no-ball chillata hai.','b',''),
('how','पर इतना छोटा फ़र्क, अंपायर देखता कैसे है?','Par itna chhota farak, umpire dekhta kaise hai?','c',''),
('how','मैदान वाला नहीं. फ्रंट फुट नो-बॉल टीवी अंपायर पकड़ता है, हर बॉल पे.','Maidan wala nahi. Front foot no-ball TV umpire pakadta hai, har ball pe.','b',''),
('frame','पैर ज़मीन पे आते ही रीप्ले रुकता है. उसी फ्रेम में फैसला.','Pair zameen pe aate hi replay rukta hai. Usi frame mein faisla.','b',''),
('wkt','और उस बॉल पे विकेट गिरा? नो-बॉल निकली, तो बैटर वापस.','Aur us ball pe wicket gira? No-ball nikli, toh batter wapas.','b',''),
('end','तो बताओ, लाइन पे पैर, नो-बॉल? हाँ या ना?','Toh batao, line pe pair, no-ball? HAAN ya NA?','b',''),
]
VOICES={'c':('kokoro:hm_psi',1.2,1.03),'b':('kokoro:hm_omega',1.2,0.9)}
BEATS=[
 dict(emotion='excited',action='full-screen, points down at the line',rule='hook: today\'s match + the gully belief',
      keys=[(None,'c','point','shocked',1),(None,'b','idle','neutral',0),('pair','c','leanin','confused',1)],caps=[('baba','Duffy: baar baar *no-ball*'),('pair','Pair *line pe* tha?')]),
 dict(emotion='calm',action='palm, palm again',rule='not A, not B: one line each',
      keys=[(None,'b','palm','smug',1),(None,'c','idle','confused',0),('edi','b','stop','explaining',1),('woh','c','shrug','confused',1)],caps=[('line','Line pe pair? *Legal*'),('edi','Edi hawa mein? *Legal*')]),
 dict(emotion='firm',action='counts one, hit on PEECHE',rule='actually C, the claim by ~7 s',hit='peeche',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('peeche','b','point','angry',1),('na','c','blown','shocked',1)],caps=[('noball','*No-ball* tab, jab'),('ek','Ek bhi hissa *peeche* nahi')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask, named person',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('har','c','wave','happy',1)],caps=[('ye','Us *dost* ko bhejo'),('har','Har wicket pe *NO-BALL*')]),
 dict(emotion='curious',action='leans in',rule='the stay: how is it judged',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],caps=[('par','Itna chhota *farak*')]),
 dict(emotion='explaining',action='stop hand, then explains',rule='who calls it',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','neutral',0),('front','b','explain','explaining',1),('har','b','count','happy',1)],caps=[('maidan','Maidan wala *nahi*'),('front','*TV* umpire pakadta'),('har','Har *ball* pe')]),
 dict(emotion='explaining',action='explains, points at the frame',rule='one visual: frames roll then freeze',
      keys=[(None,'b','explain','explaining',1),(None,'c','phone','neutral',0),('rukta','b','point','explaining',1),('usi','c','idle','happy',1)],caps=[('pair','Pair *zameen* pe aaya'),('rukta','Replay *ruka*'),('usi','Ek *frame* mein faisla')]),
 dict(emotion='surprised',action='palm, hit on WAPAS',rule='the payoff of the tech, hit',hit='wapas',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('noball','b','point','smug',1),('wapas','c','blown','shocked',1)],caps=[('aur','Us ball pe *wicket*?'),('noball','No-ball = batter *wapas*')]),
 dict(emotion='happy',action='waves, asks',rule='one ask, loops to the hook',
      keys=[(None,'b','explain','happy',1),(None,'c','idle','happy',0),('haan','b','wave','happy',1)],caps=[('toh','Line pe pair, *no-ball?*'),('haan','*HAAN* ya NA?')]),
]
