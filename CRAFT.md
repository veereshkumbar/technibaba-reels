# Craft rules (from HyperFrames, Apache-2.0; full references in `vendor/hyperframes-refs/`)

Apply these on every reel. They sit on top of CHAT_FORMAT.md / DOC_FORMAT.md.

## Story
- One thing the viewer must remember, said in their words. One concrete example carries the whole reel (e.g. "4,000 Good Morning photos").
- Before scripting, write **3 storylines** (different device: a moment in someone's day, life before/after, a number lands, myth vs fact…) and pick the one a stranger would follow. Save them in the workdir as `STORYLINES.md`.
- Real numbers only, from sources. An illustrative number is labelled as an example.
- Banned words: unlock, seamless, supercharge, game-changer, "Introducing" as the first line.

## Vertical (9:16)
- Frame 0 = hook + thumbnail: characters and the title card already on screen (no fade-in from black).
- Text only between y=168 and y=1330; nothing readable under 28 px; ≤5 English words per caption group.
- New beat every 2–4 s; shots 1–2 s; payoff before the swipe.
- Many watch muted: the picture alone must tell the joke.

## Characters (acting)
- Mood changes go through a take: anticipation → squash → new face → settle. Never snap faces.
- Offset parts: head leads, arms follow; never both arms or both eyes in perfect unison.
- Contact: feet on the ground, props in hands, eyes on what they look at.
- Each action is one read: lead the eye, play the action fast, **hold the reaction** (that's where the laugh is).
- Optional hand-drawn life: redraw outlines ~12 fps with a seeded jitter (`Math.floor(t*12)`).

## Captions
- Groups of 2–3 words for high energy, 3–5 conversational. Break at sentence ends and pauses ≥150 ms.
- One group at a time; start 0.1–0.3 s in, never exactly at 0; hard-hide each group after its end.
- Size each group to fit the width (fit, don't wrap). Never over a face.

## Motion & transitions
- 3–5 transition kinds per reel, each with a cause (whip, zoom-through-the-phone, object-becomes-the-world, colour flood). Worlds never crossfade into each other.
- Tells of a generated film (avoid): every scene entering the same way; titles that keep sliding after they land; floating/pulsing UI loops; glow-and-particles as the main look; side-by-side cards standing in for a scene.

## Sound
- Voice first; music ducked under it; SFX on actions (pop, whoosh, thud), not on every word.
- You cannot hear the mix: measure loudness and say so.

## Review (before render) — write `REVIEW.md` in the workdir
1. Contact sheet of every scene's start + middle, every cut (−0.2 s/+0.2 s), and frames at phone width (360 px).
2. Describe each beat frame in one sentence as a stranger would. Anything you'd have to explain = P0.
3. Notes as `t=4.2s · where · problem → exact change`. Rank P0 (breaks the read), P1 (weakens), P2 (polish). Fix all P0 and worthwhile P1, re-check only what changed.
4. Delivery note: creative calls, weakest shot, what nobody checked (sound was measured, not heard).
