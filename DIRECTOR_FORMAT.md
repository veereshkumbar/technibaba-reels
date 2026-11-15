# Director format (Motion Harness)

A two-friends reel built from a **voice-timed beat sheet** and the **layered rigs**, instead of hand-timed scenes.
Example: `examples/director_wifi` ("Free airport WiFi = jaal", 32 s).

## What is in the repo
| Path | What it is |
|---|---|
| `brand/tokens.json` | The only colours, fonts, eases (`snappy`, `smooth`, `bouncy`) and motion numbers. |
| `brand/dynamics.md` | House animation rules and the beat-scoring checklist. |
| `rigs/core.js` | Rig engine: `pose(name, frame, {big})`, `express(name, frame, {big})`, `say(viseme, frame)`, `draw(frame, {x,y,flip})`. Big keys get anticipation, a bouncy landing, squash and follow-through. Also `timeWarp` (hit-stop), `impact`, `arc`. |
| `rigs/face.js` | Shared eyes (6 states), brows, 8 mouth visemes, arms. |
| `rigs/baba/rig.js`, `rigs/friend/rig.js` | The two characters. Same art as the premium chat; do not redraw. |
| `pipeline/beats.py` | `timeline.json` + `script.BEATS` → `beats.json` (30 fps frames, word frames, viseme track, rig keys, captions, camera keys, hit-stops, checks). |
| `pipeline/stage.js` | Shared stage: keys the rigs from the beats, eased camera, hit-stop, keyword captions in the title-safe box, scene wipes, SFX cues. |
| `pipeline/check.py` | Checks + contact sheet (`qa/contact.png`). |

## Build
```
W=$PWD/examples/director_wifi
python3 engine/voice.py $W          # voices + timeline.json
python3 pipeline/beats.py $W        # beats.json, prints the checks
python3 engine/build.py $W          # page.html (injects tokens, rigs, stage, beats)
python3 engine/shots.py $W 1 5 9.3  # look at frames first
python3 engine/render.py $W         # video_only.mp4 (run with nohup; about 5 min)
python3 engine/lofi.py $W/bed.wav 34 92 7 bright
python3 engine/audio.py $W OUT.mp4 $W/bed.wav 0.20
python3 pipeline/check.py $W OUT.mp4
```

## Writing a reel
`script.py` has `LINES` (as in the chat format) and `BEATS`, one dict per line:
- `keys`: `(anchor word or None, who, pose, expression, big)`. Each line needs at least one key so nobody is a static talking head.
- `caps`: `(anchor word, 'short caption with one *keyword*')`. Keep under about 22 characters.
- `cams`: extra camera keys inside a line, `(anchor word, 'cu'|'boom'|'wide', who)`.
- `hit`: the punchline word. It gets a 4-frame hit-stop, an impact frame and a camera shake. Use at most two per reel.
- `emotion`, `action`, `rule`: the story tags and the `dynamics.md` rule the beat applies.
Poses: idle, talk, explain, point, count, shrug, up, blown, palm, thumb, wave, cross, stop, phone, leanin.
Expressions: neutral, happy, shocked, smug, confused, angry, explaining, sideeye.
Scene art (`bg`, `props`) lives in the reel's `page_tpl.html`. Props are drawn in screen space inside the title-safe box (x 108–972, y 192–1536) so close-ups never crop them.

## Voice
- Friend: Kokoro `hm_psi` (cloud).
- Baba: Veer's cloned voice. `VOICES['b']=('file:vo_in/b_{i:02d}.wav',1.0,1.0,(fallback voice))`. Put one WAV per Baba line in `WORKDIR/vo_in/` (made on the Mac with Voicebox, profiles "TechniBaba Calm" / "TechniBaba Energy"). When a file is missing the Kokoro stand-in is used and `timeline.json` marks the line `src: standin:...`.
- Lip-sync needs no word timestamps: words are spread across the measured line by length, mapped to the 8 visemes, and closed where the loudness envelope is silent.

## Differences from the `technibaba-director` skill (as of 2026-11-15)
- Renderer: the split layout renders through HyperFrames (`pipeline/hf_build.py`, see SPLIT_FORMAT.md). The older full-screen director example still uses the repo's own engine.
- Voicebox runs only on Veer's Mac, so scheduled cloud runs cannot use the cloned voice. They keep Kokoro.
- Voicebox `/transcribe` returns no word timestamps; timing comes from `beats.py` as above.
- Music: Instagram library tracks cannot be added through Windsor. A quiet built-in lo-fi bed is mixed in, ducked under speech.
- The old Shotstack / ElevenLabs / catbox notes in the plan are obsolete: posting is GitHub Pages + Windsor.
