# TechniBaba Daily: 7 AM news bulletin

One reel every morning: the day's biggest story first, then "chalo dekhte hain kya kya hua", then 5–7 short stories one by one. Mostly tech; one or two from gaming, space, films/OTT, sports or business are fine. Example: `examples/news_daily` (80 s).

## Structure (updated 18 Nov 2026 after the first two bulletins)
Data: both bulletins stalled at ~112 reach with a ~59% 3-second skip rate and 5–7 s average watch time, while our other reels the same days got ~1,100 reach at 26–30% skip. Instagram stops pushing a reel after the first test audience when most of them swipe away, so the first 3 seconds decide everything. The old opening (a busy story card with small text, one specific story) lost people.
1. **Open, 0–4 s, `anchor` (first scene):** Baba full-screen at the desk, talking from frame 0: "Chalo dekhte hain aaj tech ki duniya mein kya hua... aur last wali khabar aapke phone se judi hai." The title ("Aaj ki|*TECH NEWS*"), the date chip and a preview of up to 4 one-word story chips (`list`) are on screen from frame 0. The opener must promise a payoff at the end (an open loop) so people stay.
2. **Stories, 6–8 s each, `card`:** 4–5 stories, numbered 1..N, one spoken line each, starting "Number ek..." Order: a strong, broad story first, the most shareable or useful one LAST (the payoff promised in the opener). Captions stay on in card mode (most people watch muted).
3. **Outro, `anchor`, 4–6 s:** one comment question about the last story + "roz subah 7 baje". No second ask.
Total 40–55 s. No `split` hook scene any more.

## Rules
- Baba is the only speaker. Spoken lines Hinglish; card headlines plain English.
- Every story verified in this run with at least 2 sources (1 is allowed only for a company's own announcement). Use "report ke mutabik" for anything reported, not confirmed.
- Only stories from the last 48 hours, or clearly upcoming dates ("in 2 din"). Never call older news "aaj".
- No crime, politics, elections, deaths, disasters, communal or medical stories; no allegations about people. Skip anything doubtful.
- No real photos, footage, logos or likenesses: cards use the icon library (gamepad, space, forum, car, server, headphones, plane, phone, chip, ai, cricket, film, rupee, globe) and our colours. Company and product names appear only as text.
- Card headlines: at most 9 words, one highlight; the big `stat` when there is a number.
- Caption: no emojis. Hook line, then the stories as a short numbered list, then "Comment: which story is the biggest?", then 5–8 hashtags.

## Build
```
W=$PWD/examples/news_<date>
python3 pipeline/news_build.py $W/spec.json $W        # spec format: see the docstring in news_build.py and examples/news_daily/spec.json
python3 engine/voice.py $W && python3 pipeline/beats.py $W && python3 engine/build.py $W
python3 engine/lofi.py $W/bed.wav <seconds+3> 112 <seed> bright
python3 pipeline/hf_build.py $W $W/bed.wav 0.14
export HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome
(cd $W/hf && npx -y hyperframes@0.9.52 lint && npx -y hyperframes@0.9.52 snapshot --at <6 times> --timeout 120000)
(cd $W/hf && nohup npx -y hyperframes@0.9.52 render -q looks -o OUT.mp4 > ../hf_render.log 2>&1 &)    # ~12 min per minute; poll
python3 pipeline/check.py $W OUT.mp4
```
