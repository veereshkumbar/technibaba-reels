# Sound design (every reel, every slot) — from 20 Nov 2026

Sources:
- **aevyvideoschool reel "better sound design with Claude"** (Instagram, Nov 2026). Its points: Claude can make great
  animation but can't hear, so it fakes sound effects in code and they sound fake; give it **real sounds** instead;
  **pick the music first** so the animation is built on the beat; use tools that let the agent *measure* sound.
  The three free tools it shows: **Openverse** (WordPress/openverse, a free Creative Commons sound library),
  **Real SFX** (Clipwing/skills, a Claude Code skill that places sounds from your own library on the exact frame) and
  **earshot** (Leonxlnx/earshot, MIT: "ears for coding agents").
- **earshot's measured study of professional launch / motion films** (`docs/motion-sfx-study.md`,
  `docs/launch-video-sound.md` in that repo). Our sound recipes and placement rules below are written from its numbers.

## What we use
- `engine/sfx_lib.py`: our own sound recipes, written to the measured pro targets (shape, band, length, attack, tail).
  Each sound has an **anchor**: the point that sits on the cue (attack for clicks and pops, peak for whooshes and
  impacts, end for risers and zips). Templates keep calling `sfx(frame, 'name')`; old names map to the new sounds.
- `engine/audio.py` places them, enforces restraint, keeps them out of the voice band, writes `sfx_report.json`
  (what was placed or dropped and why).

| name in `sfx()` | sound | use it for | anchor |
|---|---|---|---|
| `whoosh` | low designed swell, air layer sliding down 2 octaves, 0.7 s | a page/scene change (max 1 per 1.4 s) | peak on the cut |
| `swish` | thin 2-8 kHz flick, 0.25 s | text slide, a card sliding in | peak |
| `riser` | drone + 2→8 kHz glide + speeding stutter gate, 1 s | the build before the ONE big reveal | **end** on the cut |
| `boom` / `impact` | sub body ~80 Hz, transient, gated rumble tail | the reveal / punchline (1-2 per reel) | body peak on the cut |
| `subdrop` | 64→44 Hz bloom | a heavy reveal under a cut | onset |
| `thud` / `popin` | 105 Hz thump + faint tick | an element/card appearing | onset (25-40 ms after it appears) |
| `pop` | falling chirp 9.8 kHz→350 Hz | a badge/sticker popping | onset |
| `blip` | soft gated tone | small UI change | onset |
| `ding` | struck 1.9 kHz tone + 3.4x partial; repeats step up a semitone | a check / tick / list item done | onset |
| `tick` | 2-12 kHz noise tick | counters, hovers, small steps | onset |
| `click` | bright "tink" | a tap on a button | onset (on the press frame) |
| `type` | real-style key run, jittered | typing on screen | onset |
| `zip` / `zipdown` (`crack`) | tonal sweep up into a cut / fast sweep down | transitions; the twist | end / peak |
| `sting` | falling chirp into a low hum | the logo / follow-card ending | onset |
| `cash` | two dings a fifth apart | money, a win | onset |
| `glitch` | crackle then speeding stutter | an error, a scam reveal | end on the cut |

## Rules (apply in every reel)
1. **Voice first.** Voice is the loudest thing. SFX duck under speech and their 1-4 kHz is cut 75% while anyone talks
   (automatic). Never put a big hit on top of a key word; put it in the breath just before or after.
2. **Restraint: accents on meaning, not on every element.** About 1 sound per 1-1.5 s overall in a voice reel.
   Impacts: 1-2 per reel (the reveal / punchline). Whooshes: page changes only, never closer than 1.4 s. One sound per
   moment (no pop + ding + whoosh on the same frame); the mixer drops stacked extras and logs them.
3. **Timing like the pros.** Attacks of impacts/taps/clicks lead the cut by 30-200 ms with the peak within ~80 ms of
   it; whoosh peaks within ±150 ms of the cut; risers, zips-up and glitches END on the cut and hand over; pop-ins land
   25-40 ms after the element appears. (Handled by each sound's anchor: put the cue on the visual frame.)
4. **Shapes that read as designed, not synthetic:** one gesture each (a pitch move or a gate), band-limited (UI sounds
   have nothing below 500 Hz-2 kHz, swells and impacts live below 150-250 Hz), hard ends (hold, then stop), mono.
5. **Music is a bed, ducked under the voice** (gain 0.16 with our generated bed). Better: choose a trending Instagram
   audio track in the app when posting manually; for code-made music, pick the tempo first and land section changes
   and the reveal on downbeats.
6. **Master for the web:** about -14 LUFS integrated, true peak ≤ -1.5 dBTP (the mixer's last step). Start with sound in
   the first 0.15 s (no silent cold open). Land the ending at body level with a short sting; no long fade.
7. **Check before posting:** read `sfx_report.json` (count per role, anything dropped) and confirm: ≤ 2 impacts, no
   whoosh closer than 1.4 s, nothing stacked, LUFS ≈ -14.

## Not adopted yet (needs Veer)
- **earshot itself** (its bank of 252 tuned sounds and its `critique` scorecard): running third-party code in the
  workspace needs Veer's explicit OK. Our `sfx_lib.py` follows its published measurements instead.
- **Real recordings** (Openverse / Freesound CC0 / Pixabay / Mixkit): the workspace can't reach those sites. If Veer
  downloads a pack to the Mac (e.g. a free CC0 whoosh/impact/UI pack), put it in `assets/sfx_real/<name>.wav`; the
  library can prefer real recordings over recipes per name.
