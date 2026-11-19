# English test reel in the premium look. Format 2 (FORMATS.md): not A (hacker), not B (fake app), actually C (you, typing your PIN to "receive").
# c = Chotu, b = Techni Baba. Fact: a UPI PIN is only ever needed to SEND money or check balance, never to receive (NPCI / bank advisories). 1930 = national cybercrime helpline.
LINES=[
('q','Money vanished from your UPI? It probably was not a hacker.','Money vanished from your UPI? It probably was not a hacker.','b',''),
('q','A fake app, then?','A fake app, then?','c',''),
('q','Not that either. It was you. Typing your PIN to receive money.','Not that either. It was you. Typing your PIN to receive money.','b',''),
('rule','The rule. You never need a PIN to receive money.','The rule. You never need a PIN to receive money.','b',''),
('rule','Send this to the person in your family who taps pay on everything.','Send this to the person in your family who taps pay on everything.','b',''),
('how','But how do they trick you?','But how do they trick you?','c',''),
('how',"A stranger says, I'm sending you money. A request pops up. It looks like receiving. It's actually paying.","A stranger says, I'm sending you money. A request pops up. It looks like receiving. It's actually paying.",'b',''),
('fix','A PIN means money leaves. Decline it. Money gone? Call nineteen thirty.','A PIN means money leaves. Decline it. Money gone? Call 1930.','b',''),
('end','So if someone needs my PIN to send me money?','So if someone needs my PIN to send me money?','c',''),
('end','Not sending. Taking. Has this happened to you? Comment yes or no.','Not sending. Taking. Has this happened to you? Comment yes or no.','b',''),
]
VOICES={'c':('kokoro:am_puck',1.14,1.04),'b':('kokoro:am_michael',1.13,0.97)}
BEATS=[
 dict(emotion='calm',action='full-screen, palm out',rule='hook = the common guess, killed in one line',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('hacker','b','palm','smug',1)],caps=[('money','Money *vanished* from UPI?'),('probably','Probably not a *hacker*')]),
 dict(emotion='curious',action='leans in',rule='second guess',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('a','A *fake app*?')]),
 dict(emotion='serious',action='stop hand, then points at the viewer',rule='actually C, hit on YOU',hit='you',
      keys=[(None,'b','stop','explaining',1),(None,'c','idle','confused',0),('it','b','point','explaining',1),('you','c','blown','shocked',1)],caps=[('not','Not that *either*'),('it','It was *you*'),('typing','PIN typed *to receive*')]),
 dict(emotion='firm',action='counts one',rule='the rule, big and simple',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('never','b','stop','angry',1)],caps=[('the','The *rule*'),('never','Receiving needs *no PIN*')]),
 dict(emotion='warm',action='points out of frame',rule='mid-video share ask by ~12 s',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0)],caps=[('send','*Send this* to the one'),('who','who taps *Pay* on everything')]),
 dict(emotion='curious',action='shrug',rule='the stay: how it happens',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('but','How do they *trick* you?')]),
 dict(emotion='explaining',action='explains, then sideeye',rule='one visual per idea: message, request, flip',
      keys=[(None,'b','explain','explaining',1),(None,'c','idle','neutral',0),('request','b','point','explaining',1),('actually','b','palm','smug',1)],caps=[('a','"I\'m *sending* you money"'),('request','A *request* pops up'),('actually','It\'s actually *paying*')]),
 dict(emotion='firm',action='stop hand, then thumbs up',rule='the fix',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','neutral',0),('decline','b','thumb','happy',1)],caps=[('a','PIN = money *leaves*'),('decline','*Decline* it'),('money','Money gone? Call *1930*')]),
 dict(emotion='thinking',action='leans in',rule='loop question',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('so','Needs *my PIN* to send me?')]),
 dict(emotion='calm',action='crosses arms, then waves',rule='one ask: YES or NO',
      keys=[(None,'b','cross','smug',1),(None,'c','idle','neutral',0),('taking','b','stop','angry',1),('comment','b','wave','happy',1)],caps=[('not','Not sending. *Taking.*'),('comment','Comment *YES* or NO')]),
]
