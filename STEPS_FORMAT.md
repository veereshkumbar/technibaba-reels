# TechniBaba Steps — step-by-step tutorial format

A calm, clean "follow these N steps" reel that people save, share and comment a keyword on. Use for how-to, settings, checklists, setups ("WhatsApp lock in 60 sec", "UPI fraud se bachne ke 5 settings", "naya phone: pehle ye 5 kaam").

Start from `examples/steps_whatsapp/` (`page_tpl.html` uses `__FACE__`, filled by `engine/build.py` from `engine/face.js`).

## Look
- White grid paper, navy ink, ONE accent (mint green `#10b981`), red only for danger.
- Left **timeline**: a line with one node per step; Techni Baba's face is the marker; a pill names the current step ("02 Linked devices"); finished steps get a tick and scroll up.
- **Captions at the top**, 2–3 words at a time, spoken words dark, upcoming words grey. Write the key word of each line in CAPS in the roman caption: it shows in serif italic inside a green box.
- One white **UI card** per step that acts out the step: breadcrumb rows, toggles, radios, PIN boxes, taps. Draw generic UI; no real app logos or screenshots.
- A small "what it stops" gag under the card on the second line of each step (thief hits the PIN wall, lottery group bounces off, scam call goes silent).

## Script shape (13–16 lines, 45–55 s, one narrator = Techni Baba, `VOICES={'b':('kokoro:hm_omega',1.14,0.96)}`, `GAP_SC=0.34 GAP_LN=0.2`)
1. Hook (frame 0): the scary/annoying fact + Baba's worried face + one prop card.
2. Promise: "60 second do, 5 cheezein…" → title card with 3 chips (steps · time · ₹0).
3. Steps: each = line A "where to tap" (path words appear as rows) + line B "what it stops" (the gag).
4. Recap checklist ticking itself.
5. CTA on a soft mint gradient: comment box types the KEYWORD, "checklist DM mein", then "family group mein bhejo".

Per video, edit: `STEPS`, `EXPR`, `KEYWORD`, the scene functions (`sHook`, `s1…sN`, `sRecap`, `sCta`) and the SFX list.

## Rules
- Every step must be verified against a current source (settings paths change). Put sources in the Instagram caption.
- The comment-keyword promise is real: include in the delivery message the exact checklist text Veer sends to commenters.
- Music quiet (`lofi.py … bright`, gain 0.16). Render takes ~9 minutes (no heavy filters).
