# TechniBaba Chat — two-friends conversation format

**Use v2: start from `examples/chat_v2/`** (v1 in `examples/chat_storage` is outdated).

## v2 standard (what Veer approved as the direction)
- **Voices:** Kokoro (natural): `VOICES={'c':('kokoro:hm_psi',1.24,1.06),'b':('kokoro:hm_omega',1.16,0.95)}`. Fallback to Piper only if Kokoro fails.
- **Talking style:** write it like two friends really talk. Short lines, interjections ("Achha?", "Arre yaar", "Ruk bhai!"), reactions ("BARAH HAZAAR?!"), repeated words for comedy, a twist at the end ("Toh kisse doon?" → "Bas GM likh de"). Line = 1 breath. Never read out lists.
- **Characters:** outlined, shaded, big expressive heads, **lip sync** from the voice (timeline `env`), blinking, breathing, head tilt, smooth pose blending. Per-line `EXPR` (neutral, shock, happy, annoyed, smug, worried, shy) and `POSE` (talk, point, shrug, up, blown, palm, thumb, wave, cross, shy, stop).
- **Locations change every scene** (bedroom night/day, chai tapri, office, park sunset, end). Add new ones in `loc()`, with some motion (steam, clock, stars, leaves).
- **Camera, set per line** (5th field in LINES): '' wide two-shot, `cu` close-up on the speaker, `lis` reaction close-up on the listener, `boom` dramatic zoom + white flash + shake + thud. Whip-pan transitions between locations.
- **Phone screen** shows what's being said; it moves to the corner in close-ups.
- Script shape, 16–18 lines, 40–45s.


The format the channel already posted before (e.g. the "HR Didi vs Rahul" reel), upgraded. Two characters talk about a trending topic. One asks or complains, the other explains with a punchline.

## Cast
- **Chotu** (asks, confused, over-reacts): voice `pratham`, tempo 1.22, pitch 1.1. Yellow captions.
- **Techni Baba** (explains, deadpan jokes): voice `rohan`, tempo 1.12. Mint captions.
- Other topics can recast them (HR Didi, Boss, Mummy…), but keep Techni Baba as the one who knows tech.
Set in `script.py`: `LINES=[(scene, devanagari, roman, 'c'|'b'), ...]` and `VOICES={'c':('pratham',1.22,1.1),'b':('rohan',1.12)}`.
Build voice with `GAP_SC=0.3 GAP_LN=0.22`.

## What makes it more engaging than the old version
1. **Fixed hook banner** at the top for the whole video: a joke with two lines and emoji, e.g. `Phone: "Storage Full" 😩 / (Good Morning photos: 4,000 💀)`.
2. **A screen between them** that changes each scene (storage bar, gallery, chat, settings toggles) and shows what's being said.
3. **Keyword pops** in the gap between them: 2–3 words + emoji, about every 3 seconds.
4. **Reactions:** speaker bounces with speech marks; poses `talk, point, shrug, palm, up, blown, wave, thumb`.
5. **Karaoke captions,** 4-word chunks coloured by speaker, auto-fit width.
6. **Payoff:** a real, useful fix (the viewer learns something) + a final punchline + a comment question.

## Script shape (12–15 lines, 35–42s)
Problem line (funny) → Baba's question → silly answer → the reveal joke → "but why?" → the real reason → "what now?" → 2 fix lines → result → punchline → comment question + follow.

Start from `examples/chat_storage/`.
