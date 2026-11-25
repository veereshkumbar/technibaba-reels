# 7 PM trending 25 Nov 2026: World Chess Championship Game 2 tonight (Gukesh vs Sindarov, 7:30 PM IST) -> what the eval bar really means.
# Format 2 (not A "Gukesh haar raha", not B "jeet ka chance", actually C "computer ka score, pyaadon mein").
# Question at 6 s: "Pyaadon mein score? Kaise? Aur phir +1 wala jeetega kyun nahi?"
# Facts: Chess.com Help (eval numbers = advantage in pawn units; + White, - Black; near 0 = even; slight edge doesn't guarantee a win,
#  especially in human play; engines like Stockfish); chess.com blog (+1.00 = White roughly a pawn up); lichess blog (+3 = White ahead
#  by three pawns). Match: Chess.com 24 Nov (Game 2 Wed 25 Nov 7:30 PM IST, Gukesh 0.5 Sindarov 0.5 after G1, 14 games, first to 7.5),
#  ESPN 25 Nov (Gukesh White in Game 2; Game 1 a draw), Wikipedia schedule (G1 24 Nov, G2 25 Nov, Geneva).
LINES=[
('q','बाबा! बार सिंदारोव की तरफ़! मतलब गुकेश हार रहा?','Baba! Bar Sindarov ki taraf! Matlab Gukesh haar raha?','c',''),
('q','नहीं. जीत का चांस भी नहीं. ये कंप्यूटर का स्कोर है, प्यादों में.','Nahi. Jeet ka chance bhi nahi. Ye computer ka score hai, pyaadon mein.','b',''),
('q','प्यादों में? कैसे?','Pyaadon mein? Kaise?','c',''),
('share','उस दोस्त को भेजो, जो बार देखकर चिल्लाता है, गुकेश गया!','Us dost ko bhejo, jo bar dekhkar chillata hai, Gukesh gaya!','b',''),
('eng','इंजन हर पोज़ीशन को नंबर देता है. प्लस एक, सफ़ेद करीब एक प्यादा आगे.','Engine har position ko number deta hai. Plus 1, White kareeb ek pyaada aage.','b',''),
('eng','माइनस, काला आगे. ज़ीरो के पास, बराबर.','Minus, Black aage. Zero ke paas, barabar.','b',''),
('human','तो प्लस एक वाला जीतेगा ना?','Toh plus 1 wala jeetega na?','c',''),
('human','ज़रूरी नहीं. इंसान को वो चाल घड़ी के दबाव में ढूँढनी है.','Zaroori nahi. Insaan ko woh chaal ghadi ke dabaav mein dhoondhni hai.','b',''),
('tonight','पहला गेम ड्रॉ. आज गेम दो, साढ़े सात बजे.','Pehla game draw. Aaj Game 2, 7:30 baje.','b',''),
('end','तो बार स्कोर है, हार नहीं. आज कौन जीतेगा? गुकेश या सिंदारोव?','Toh bar score hai, haar nahi. Aaj kaun jeetega? GUKESH ya SINDAROV?','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='panic',action='full-screen, holds up phone',rule='hook: the obvious guess (A), payoff pill on frame 0',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('gukesh','c','blown','shocked',1)],caps=[('baba','Bar *Sindarov* ki taraf'),('matlab','Gukesh *haar* raha?')]),
 dict(emotion='calm-smug',action='stop hand, then counts',rule='not A, not B, actually C by 6 s; hit on SCORE',hit='score',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('jeet','b','count','explaining',1),('computer','b','point','explaining',1)],caps=[('nahi','*Nahi*'),('jeet','Jeet ka *chance*? Nahi'),('ye','Computer ka *score*')]),
 dict(emotion='curious',action='leans in',rule='the planted question',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0)],caps=[('pyaadon','Pyaadon mein? *Kaise*?')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask at 8-12 s',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('us','Us *dost* ko bhejo'),('jo','jo bole *Gukesh gaya*')]),
 dict(emotion='explaining',action='explains, then counts one',rule='mechanism: engine number in pawns',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('plus','b','count','explaining',1)],caps=[('engine','Engine deta *number*'),('plus','+1 = *1 pyaada* aage')]),
 dict(emotion='explaining',action='palm, then thumb',rule='minus and zero',
      keys=[(None,'b','palm','explaining',1),(None,'c','idle','neutral',0),('zero','b','thumb','happy',1)],caps=[('minus','Minus = *Black* aage'),('zero','Zero = *barabar*')]),
 dict(emotion='doubtful',action='shrug',rule='listener objection',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','smug',0)],caps=[('toh','+1 wala *jeetega*?')]),
 dict(emotion='firm',action='stop hand, then explains',rule='answer: human under the clock; hit on NAHI',hit='nahi',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','neutral',0),('insaan','b','explain','explaining',1),('ghadi','c','blown','shocked',1)],caps=[('zaroori','Zaroori *nahi*'),('insaan','Insaan ko woh *chaal*'),('ghadi','*Ghadi* ke dabaav mein')]),
 dict(emotion='excited',action='points, then thumbs up',rule='tonight: the peg',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('aaj','b','count','explaining',1)],caps=[('pehla','Game 1 *draw*'),('aaj','Aaj *7:30 PM*')]),
 dict(emotion='happy',action='crosses arms, then waves',rule='loop to the hook + one ask',
      keys=[(None,'b','cross','smug',1),(None,'c','idle','neutral',0),('aaj','b','wave','happy',1),('gukesh','c','thumb','happy',1)],caps=[('toh','Bar = *score*'),('aaj','*GUKESH* ya SINDAROV?')]),
]
