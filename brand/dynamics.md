# TechniBaba dynamics — house rules for motion

Read this before writing any motion. Every value comes from `brand/tokens.json`. The rigs in `rigs/` already implement rules 1–6; the director's job is to *place* them on the right frames.

## Animation principles
1. **Anticipation.** Every big move (a `pose()` or `express()` key marked `big`) winds up 4–8 frames in the opposite direction first. The key frame is the frame the move *lands its start*, on the spoken word.
2. **Arcs.** Arms, heads and props travel on arcs. Arm poses blend in joint-angle space (never straight-line hand paths); props use gravity arcs.
3. **Overlap and follow-through.** Top-knot, hair and beard lag the head by 3 frames and settle over ~14 frames after it stops. Hands settle after the arm.
4. **Squash and stretch.** On reactions and landings only, max 7%, volume preserved.
5. **Hit-stop.** Freeze the picture 3–5 frames on every punchline or impact, with an impact frame (burst lines + 1 bright frame), then catch up over 6 frames. Audio never stops.
6. **Ease everything.** `snappy` for pops/hits/whips, `smooth` for moves and camera, `bouncy` for landings and reactions. No linear tweens.

## Reel rules
- Hook lands by 1.5 s, in the picture and in the voice. Frame 0 is the thumbnail.
- Something changes every 2–3 s: cut, camera push, prop, pose or expression. One *major* move per beat.
- Captions: short keyword lines (not the full sentence), inside the title-safe box, one keyword in caption yellow.
- Speaker always does something: lean, gesture or expression change each beat. The listener reacts.
- End on a payoff plus a comment prompt.

## Avoid
| Instead of | Use |
|---|---|
| straight-line paths | gravity arcs |
| linear tweens | eased keys from tokens |
| fade on a hit | impact frame + hit-stop |
| static talking heads | lean, gesture or expression change each beat |
| caption repeating the voice word for word | short keyword caption |
| 3D models / new character art | the 2D rigs |

## Scoring a beat (for the review)
For each beat still, answer yes/no: anticipation present before the big move · arc not straight · overlap visible after head moves · hit-stop on the punchline · a visual change within 3 s · hook by 1.5 s · caption in safe box with one keyword.
