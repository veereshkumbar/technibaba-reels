# Morning tutorial 24 Nov 2026: stop strangers adding you (Papa) to WhatsApp stock-tip / scam groups. Premium look, Hindi.
# Format 5: won't work (exit), unless (one setting). Question at 6 s: "Kaun si setting? Exit se kyun nahi rukega?"
# Paths: WhatsApp Settings > Privacy > Groups > Everyone / My contacts / My contacts except (WhatsApp blog 'New privacy settings for groups';
#  Bitdefender Jul 2026; TalkAndroid Sep 2026). Non-allowed adder can only send a private invite, expires in 3 days (WhatsApp blog).
#  Settings > Privacy > Calls > Silence unknown callers (Bitdefender). Unknown-group safety overview (Fox News / WhatsApp, Aug 2025).
LINES=[
('q','बाबा! पापा को फिर किसी ने स्टॉक टिप्स वाले ग्रुप में डाल दिया!','Baba! Papa ko phir kisi ne stock tips wale group mein daal diya!','c',''),
('q','एग्ज़िट करने से कुछ नहीं होगा. जब तक ये एक सेटिंग नहीं बदलोगे.','Exit karne se kuch nahi hoga. Jab tak ye ek setting nahi badloge.','b',''),
('q','कौन सी सेटिंग? वो तो रोज़ नए ग्रुप में जुड़ जाते हैं!','Kaun si setting? Woh toh roz naye group mein jud jaate hain!','c',''),
('share','पहले ये रील पापा को भेजो. फिर व्हाट्सऐप, सेटिंग्स, प्राइवेसी.','Pehle ye reel Papa ko bhejo. Phir WhatsApp, Settings, Privacy.','b',''),
('how','ग्रुप्स पे टैप करो. एवरीवन हटाओ, माय कॉन्टैक्ट्स चुनो.','Groups pe tap karo. Everyone hatao, My contacts chuno.','b',''),
('invite','और अनजान नंबर वाला फिर भी जोड़े तो?','Aur anjaan number wala phir bhi jode toh?','c',''),
('invite','जोड़ ही नहीं पाएगा. बस इनवाइट भेजेगा, आप मत खोलना.','Jod hi nahi paayega. Bas invite bhejega, aap mat kholna.','b',''),
('calls','और अनजान कॉल्स?','Aur anjaan calls?','c',''),
('calls','प्राइवेसी, कॉल्स, साइलेंस अननोन कॉलर्स, ऑन.','Privacy, Calls, Silence unknown callers, ON.','b',''),
('end','अब पापा के ग्रुप्स सिर्फ़ अपनों के. कमेंट करो गाइड.','Ab Papa ke groups sirf apnon ke. Comment karo GUIDE.','b',''),
]
VOICES={'c':('eleven:pHG3exaXQt8bmTWbaVOs',1.0,1.0,('kokoro:hm_psi',1.2,1.03)),'b':('eleven:QO2wwSVI9F7DwU5uUXDX',1.0,1.0,('kokoro:hm_omega',1.2,0.9))}
BEATS=[
 dict(emotion='annoyed-panic',action='full-screen, holds up phone',rule='hook: the problem + scam group on screen',
      keys=[(None,'c','phone','shocked',1),(None,'b','idle','neutral',0),('group','c','blown','shocked',1)],caps=[('baba','Papa phir *group* mein'),('stock','*Stock tips* wala')]),
 dict(emotion='calm-smug',action='stop hand, then counts one',rule='the claim by 6 s: exit wont work, unless one setting',hit='setting',
      keys=[(None,'b','stop','smug',1),(None,'c','idle','confused',0),('jab','b','count','explaining',1)],caps=[('exit','*Exit* se kuch nahi'),('jab','Jab tak *1 setting*')]),
 dict(emotion='curious',action='leans in, shrug',rule='the planted question',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','neutral',0),('woh','c','shrug','shocked',1)],caps=[('kaun','Kaun si *setting*?'),('roz','*Roz* naya group')]),
 dict(emotion='warm',action='points out of frame, then phone',rule='mid-video share ask at 8-12 s',
      keys=[(None,'b','point','happy',1),(None,'c','thumb','happy',0),('phir','b','phone','explaining',1)],caps=[('pehle','*Papa* ko bhejo'),('phir','Settings > *Privacy*')]),
 dict(emotion='explaining',action='counts one, palm',rule='step 1: Groups > My contacts',
      keys=[(None,'b','count','explaining',1),(None,'c','idle','neutral',0),('my','b','palm','explaining',1)],caps=[('groups','*Groups* pe tap'),('my','*My contacts*')]),
 dict(emotion='doubtful',action='leans in',rule='listener objection',
      keys=[(None,'c','leanin','confused',1),(None,'b','idle','smug',0)],caps=[('aur','*Anjaan* number?')]),
 dict(emotion='firm',action='stop hand',rule='step 2: invite only, hit on NAHI',hit='nahi',
      keys=[(None,'b','stop','angry',1),(None,'c','idle','shocked',0),('bas','b','explain','explaining',1),('mat','c','thumb','happy',1)],caps=[('jod','Jod *nahi* paayega'),('bas','Sirf *invite*, mat kholo')]),
 dict(emotion='curious',action='shrug',rule='listener question',
      keys=[(None,'c','shrug','confused',1),(None,'b','idle','neutral',0)],caps=[('aur','Anjaan *calls*?')]),
 dict(emotion='explaining',action='points, thumbs up',rule='step 3: silence unknown callers',
      keys=[(None,'b','point','explaining',1),(None,'c','idle','neutral',0),('on','b','thumb','happy',1)],caps=[('privacy','Privacy > *Calls*'),('silence','Silence unknown: *ON*')]),
 dict(emotion='happy',action='waves',rule='payoff + one ask: GUIDE (loops to the hook)',
      keys=[(None,'b','thumb','happy',1),(None,'c','thumb','happy',0),('comment','b','wave','happy',1)],caps=[('ab','Sirf *apnon* ke groups'),('comment','Comment karo *GUIDE*')]),
]
