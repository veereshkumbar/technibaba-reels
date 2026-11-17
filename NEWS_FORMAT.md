# TechniBaba Daily: 7 AM news bulletin

One reel every morning: the day's biggest story first, then "chalo dekhte hain kya kya hua", then 5–7 short stories one by one. Mostly tech; one or two from gaming, space, films/OTT, sports or business are fine. Example: `examples/news_daily` (80 s).

## Structure (what the reference reel does, in our style)
1. **Hook, 0–8 s, `split`:** the most shareable story as a card on top, Baba reacting below, a short Hinglish banner ("GTA 6 bas 2 din door!"). First words land in the first second.
2. **Bridge, ~3 s, `anchor`:** Baba at the desk, big title ("Is hafte|*kya hua*?" or "Aaj ki|*7 khabrein*"), riser + boom.
3. **Stories, 7–10 s each, `card`:** full-screen card (kicker, number n/N, our own icon art, an optional big stat, an English headline with 1–2 *highlighted* phrases, source line), Baba picture-in-picture bottom right, one spoken line starting "Number do..." Whoosh + ding on every card.
4. **Outro, `anchor`:** "Kaunsi khabar sabse badi lagi? Comment karo" + "Roz subah 7 baje ke liye follow karo".
Total 60–90 s. Story 1 is the hook story; cards count up from 2.

## Rules
- Baba is the only speaker. Spoken lines Hinglish; card headlines plain English.
- Every story verified in this run with at least 2 sources (1 is allowed only for a company's own announcement). Use "report ke mutabik" for anything reported, not confirmed.
- Only stories from the last 48 hours, or clearly upcoming dates ("in 2 din"). Never call older news "aaj".
- No crime, politics, elections, deaths, disasters, communal or medical stories; no allegations about people. Skip anything doubtful.
- No real photos, footage, logos or likenesses: cards use the icon library (gamepad, space, forum, car, server, headphones, plane, phone, chip, ai, cricket, film, rupee, globe) and our colours. Company and product names appear only as text.
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
