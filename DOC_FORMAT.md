# TechniBaba Docs — documentary format

A slower, story-led reel for tech history and "how X happened" topics. Use on 2–3 evenings a week; mornings stay the fast funny style.

Good topics: how a product or company won or died (UPI, Jio, Nokia, Orkut, Flipkart vs Amazon), a tech decision that changed India, the hidden story behind a trending tech headline.

## The 5 locked style rules
1. **Palette:** cream paper `#efe6d2`, navy ink `#1d2a44`, ONE red accent `#d64527`, muted `#c9bba0`. Nothing else.
2. **Texture:** paper background plus film grain (feTurbulence, seed changes every frame) and a warm vignette.
3. **Visuals:** archival documents, memos, ledgers, cut paper, stamps, simple charts and diagrams. People are silhouettes only. No real photos, logos, banknote designs, maps with borders, or lookalikes of real people.
4. **Type:** Playfair Display (serif) for captions and headlines; JetBrains Mono for dates, labels and stamps; Caveat for handwriting.
5. **Motifs:** a red date stamp on every scene (top right) and a red "payment line" / thread that draws itself between things.

## Script rules
- Fact-check first. Every number needs a source; put sources in the Instagram caption.
- 110–140 words, 9–13 lines, 45–55 seconds. Present tense.
- First 2 seconds: the most surprising fact ("Har second, 9,500 UPI payments…").
- Shape: hook → humble start (date + tiny number) → turning point → how it works (one diagram) → spread → world scale → today's number → ending line people repeat → comment question + follow.
- Use pauses: build voice with `GAP_SC=0.45 GAP_LN=0.22 python3 engine/voice.py WORKDIR rohan 1.17` (longer gaps than the fast format).
- 8–10 scenes; one idea per scene.

## Motion
- Ken Burns on every scene (scale 1→1.06 plus a small pan, alternating direction).
- 0.4s crossfade between scenes (previous scene drawn underneath with fading opacity).
- Stamps "slam" in (scale 2.2→1 in 0.22s) with a `thud`. Scene changes get a soft `whoosh`.
- Captions: serif italic, 5-word chunks, whole-chunk fade, y≈1235.

## Build
Start from `examples/doc_upi/` (copy `page_tpl.html` + `script.py` into the workdir). The template uses `__CHARS__`, which `engine/build.py` fills with `engine/chars.js` (Techni Baba / Chotu `person()`), so Techni Baba can appear at the end.

Then the normal pipeline: `build.py` → `shots.py` (check 6–8 frames, especially stamps vs. headers and caption length) → **fix the weakest scene** → `render.py` → `audio.py WORKDIR OUT.mp4 - 0.18` (soft music under narration).

## Caption template
Title line, 2–3 lines of story, "Sources: …", 5–8 hashtags (#TechniBabaDocs #TechHistory plus topic tags).
