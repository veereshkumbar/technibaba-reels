# TechniBaba Chat — two-friends conversation format

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
