# Split layout

Content panel on top, characters below, captions on the seam. Example: `examples/split_wifi2` ("Asli vs nakli WiFi: 3 check", 36 s).
It is the director format (read `DIRECTOR_FORMAT.md` first) with one extra include, `pipeline/split.js`.

## Layout (1080x1920)
- **Top panel** x 72–1008, y 150–985: one clear visual per spoken idea (a screen, a list, two cards to compare). Navy header bar with `CHECK n` chip, title and three progress dots (`head(step, title, colour, fill)`).
- **Seam** at y 1040. Captions sit on it (`caption(f, capY(f))`), so they never cover the content or the faces.
- **Bottom**: Baba and Chotu waist-up at scale 1.7, faces around y 1400 (inside the title-safe box). The location is one simple strip (`strip(f)`).
- **Hook**: line 1 plays full-screen on its speaker with a sticker (`overlay(f)`); the panel drops in with a bounce when line 2 starts (`HOOK_END`).
- **Punchlines**: on a `hit` word the picture freezes 4 frames, the panel shakes and the speaker grows across the seam. Put the punchline stamp in the panel. At most two per reel.
- The speaker is drawn in front and 5% larger.

## Writing one
1. Copy `examples/split_wifi2`. `script.py` is the same as the director format; the `cam` field is ignored.
2. Scenes = panel pages. Each scene name in `LINES` gets one `if(n=='...')` block in `content(n,f)`; pages slide sideways on a scene change.
3. Cue every panel element from a spoken word: `WF(line, 'word')` gives its frame; use `pop(f, frame)` for the entrance and add an `sfx`.
4. Keep panel text big: 40 px and up, Mono for names and code, at most about 22 characters per row.
5. Build and check exactly as in `DIRECTOR_FORMAT.md`.
