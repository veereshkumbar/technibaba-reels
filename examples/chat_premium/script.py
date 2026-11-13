# (scene, devanagari TTS, roman caption, speaker c=Chotu b=Baba, camera)
# camera: '' wide | cu = close-up on speaker | boom = dramatic zoom + vine boom on speaker | lis = close-up on the listener
LINES=[
('bed',   'बाबाआ! ये फ़ोन फिर से चिल्ला रहा है... स्टोरेज फ़ुल!', 'Babaaa! Ye phone phir se chilla raha hai... STORAGE FULL!', 'c', 'cu'),
('bed',   'अच्छा? गैलरी में कितनी फ़ोटो हैं?', 'Achha? Gallery mein kitni photos hain?', 'b', ''),
('bed',   'ज़्यादा नहीं... बस बारह हज़ार.', 'Zyada nahi... bas barah hazaar.', 'c', ''),
('bed',   'बारह हज़ार?!', 'BARAH HAZAAR?!', 'b', 'boom'),
('chai',  'और उनमें गुड मॉर्निंग वाली कितनी?', 'Aur unme Good Morning wali kitni?', 'b', ''),
('chai',  'वो... चार हज़ार. फ़ैमिली ग्रुप से आती हैं ना!', 'Woh... chaar hazaar. Family group se aati hain na!', 'c', 'cu'),
('chai',  'मतलब फ़ोन फ़ुल नहीं है... फ़ैमिली ग्रुप ने भर दिया है!', 'Matlab phone full nahi hai... FAMILY GROUP ne bhar diya hai!', 'b', 'lis'),
('office','पर यार, मैंने तो कुछ डाउनलोड ही नहीं किया!', 'Par yaar, maine toh kuch download hi nahi kiya!', 'c', ''),
('office','तूने नहीं, व्हाट्सऐप के ऑटो डाउनलोड ने किया. हर फ़ॉरवर्ड सीधा फ़ोन में.', 'Tune nahi, WhatsApp ke AUTO-DOWNLOAD ne kiya. Har forward seedha phone mein.', 'b', 'cu'),
('office','मतलब... चुपके से?!', 'Matlab... CHUPKE SE?!', 'c', 'boom'),
('park',  'तो नया फ़ोन ले लूँ?', 'Toh naya phone le loon?', 'c', ''),
('park',  'रुक भाई! स्टोरेज एंड डेटा में जा, ऑटो डाउनलोड बंद कर.', 'Ruk bhai! Storage and data mein ja, auto-download BAND kar.', 'b', 'cu'),
('park',  'फिर मैनेज स्टोरेज से बड़ी फ़ाइलें डिलीट.', 'Phir Manage storage se BADI FILES DELETE.', 'b', ''),
('free',  'अरे वाह! दस जीबी खाली!', 'Arre waah! 10 GB KHAALI!', 'c', 'cu'),
('free',  'और सुन, गुड मॉर्निंग का जवाब फ़ोटो से मत देना.', 'Aur sun, Good Morning ka jawab photo se MAT DENA.', 'b', ''),
('free',  'तो किससे दूँ?', 'Toh kisse doon?', 'c', 'lis'),
('free',  'बस जी एम लिख दे.', 'Bas "GM" likh de. 😎', 'b', 'boom'),
('end',   'आपके फ़ोन में कितनी गुड मॉर्निंग हैं? कमेंट करो!', 'Aapke phone mein kitni Good Morning? COMMENT karo!', 'b', ''),
]
VOICES={'c':('kokoro:hm_psi',1.24,1.06),'b':('kokoro:hm_omega',1.16,0.95)}
