# Long YouTube guide videos (16:9)

Every tutorial reel (morning + evening slots) also gets a 1.5–4 minute YouTube video of the same guide: content panel on the left, Baba and Chotu full-body on the right, captions under the panel, HyperFrames transitions and SFX. Example: `examples/long_wifi_check` (117 s).

The panel is data-driven: you write only `spec.json`, never drawing code.

## spec.json
```
{"guide": "<slug in guides/guides.json>", "title": "<YouTube title>",
 "scenes": [{"id": "intro", "type": "title|points|compare|browser|phone|recap|outro", "chip": "CHECK 1", "head": "header text", ...,
             "lines": [{"who": "b"|"c", "hi": "<Devanagari for TTS>", "en": "<roman Hinglish>", "pose": "...", "expr": "...", "big": 0|1,
                        "cap": "short *keyword* caption (≤22 chars)", "show": <items visible after this line>, "show_new": <how many appear now>,
                        "hit": "<word for a hit-stop, max 2 per video>", "react": "<listener expression>", "react_pose": "<listener pose>"}]}]}
```
Scene types and their extra fields:
- `title`: `title`, `sub`, `chips` ["text|label", "text|label"].
- `points`: `items` (strings, ≤46 chars; items with NAKLI/KHATRA/chor/BHAAG turn red), `color`.
- `compare`: `left`, `right` labels, `items` [{"side": "L"|"R", "text": "≤20 chars"}].
- `browser`: `url`; `show` 1 = warning, 2 = Go back, 3 = Proceed crossed.
- `phone`: `app`, `path` (menu taps, highlighted one by one), `items` (≤2 extra steps shown beside the phone, counted after the path in `show`).
- `recap`: `items` ticked as `show` grows.
- `outro`: `sub`; `show` 1 = Subscribe, 2 = Instagram.
Poses and expressions: see DIRECTOR_FORMAT.md. Every scene starts with a line, ~2 min total = ~25 lines.

## Build
```
W=$PWD/examples/long_<topic>
python3 pipeline/long_build.py $W/spec.json $W
python3 engine/voice.py $W && python3 pipeline/beats.py $W && python3 engine/build.py $W     # beats: all checks true
python3 engine/lofi.py $W/bed.wav <seconds+3> 88 <seed> warm
python3 pipeline/hf_build.py $W $W/bed.wav 0.16
export HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome
(cd $W/hf && npx -y hyperframes@0.9.52 lint && npx -y hyperframes@0.9.52 snapshot --at <5 times> --timeout 120000)   # look at the contact sheet
(cd $W/hf && nohup npx -y hyperframes@0.9.52 render -q looks -o OUT.mp4 > ../hf_render.log 2>&1 &)                # ~12 min per minute of video; poll
```
Deliver: the MP4 plus a YouTube title (≤70 chars, Hinglish, keyword first), a description (2-line summary, the steps, "Poora guide: https://technibaba.com/guides?g=<slug>", Instagram @technibaba, sources) and 10 tags. YouTube upload is manual (Veer). When Veer replies with the YouTube link, put it in that guide's `youtube` field in guides/guides.json and push: the guides page then embeds the video.
