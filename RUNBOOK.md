# TechniBaba Reels — daily run (scheduled task)

Each run makes ONE reel, sends it to Veer for review, and posts to Instagram only after he says "post".

## Quality bar (Veer, 13 Nov 2026)
Every reel ships in the PREMIUM look (`examples/chat_premium`, see CHAT_FORMAT.md). The two-friends chat is the default format; docs at most 2 evenings a week. The old flat explainer style is retired unless upgraded with `engine/premium_patch.py`. Music: `engine/lofi.py`.

## Rules for scheduled (unattended) runs
- Nobody is watching. Never stop to ask a question before the MP4 is sent; pick the best option and say which you picked.
- First action: SendUserMessage "Starting <slot> reel…" so Veer knows the run is alive.
- Keep going until the MP4 is delivered. A full run takes 25–45 minutes; rendering alone takes ~8.
- If any step fails twice, do not quit silently: SendUserMessage + PushNotification with the step and the error, then try the fallback (simpler scene, fewer lines, built-in music).
- PushNotification is a deferred tool: load it first with ToolSearch "select:PushNotification".
- Never post without Veer's "post" reply.

## 0. Setup (every fresh session)
```bash
git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh
```
Work folder for today: `W=/tmp/reel-$(date +%Y%m%d-%H%M)`; `mkdir -p $W`.

## 1. Topic
- Check `posted.md` — never repeat a topic or angle from the last 30 days.
- Search what's trending today (web search, several queries). Mix: ~70% tech (launches, AI tools, phone/app tricks, scams & safety, big-tech news), ~30% Bollywood / sports / gaming **through a tech lens** (AI deepfakes of stars, DRS/ball-tracking, gaming news, streaming tech).
- Morning slot: news / trending. Evening slot: funny explainer or "how does X work".

**Format choice:** three formats: fast funny explainer (STYLE_GUIDE), two-friends chat (`CHAT_FORMAT.md`; good for relatable tech problems, office/HR/AI-job jokes, app tricks), and docs (`DOC_FORMAT.md`). Mix them; don't use the same format three runs in a row. Evening runs may use the documentary format (`DOC_FORMAT.md`) 2–3 times a week, for history/"how X happened" topics. Check `posted.md` so docs don't run on back-to-back evenings. Mornings stay the fast funny format.

## 2. Research and fact-check
- At least 3 independent sources; dates and numbers checked.
- Claims about real people or companies = attributed ("reports ke mutabik", "US officials ka daava") and labelled ALLEGED on screen; include the other side's denial.
- Never show real photos, match footage, film clips or brand logos. Real people never appear as characters; Techni Baba narrates and reacts.

## 3. Script (`$W/script.py`)
`LINES = [(scene, devanagari_tts_text, roman_hinglish_caption), ...]` — 9–12 lines, **35–45 s total** (data, Nov 12: 60 s reels had 55–59% 3-second skip and only 7–12 s average watch).
- Line 1 = hook (shocking fact / question) in the first 2 s. Frame 0 must already show the payoff visual + 3–5 word headline (no slow intros, no logo first).
- Last lines = a comment question (A ya B? / aapka take?) + "Follow karo TechniBaba!".
- Write TTS lines in Devanagari (Piper Hindi reads Devanagari), captions in Roman Hinglish.

## 4. Visuals (`$W/page_tpl.html`)
- Start from the closest example in `examples/` (honey_trap = news explainer with 8 styles; day_sample = characters + objects; character_styles = 6 skins; romeo_90s = comparison/comedy).
- One scene per beat; pick styles by meaning (see STYLE_GUIDE.md). Techni Baba / Bit / Chotu act out each line (poses: walk, wave, drive, type, eat, blown, thumb, tray).
- Safe zone: all text and key art between y=168 and y=1330 (1080x1920). Captions 2–4 words per chunk at y≈1186.

## 5. Build, check, render
```bash
cd /tmp/tb/engine
python3 voice.py $W pratham 1.18
python3 build.py $W
python3 shots.py $W 2 10 20 30 40 50 60     # LOOK at $W/qa/sheet.jpg, fix overlaps, re-run
python3 render.py $W
python3 audio.py $W $W/final.mp4 [/tmp/tb/music/<track>.mp3 0.25]   # '-' for built-in beat
```
Sample 8–10 frames of final.mp4 and look at them before sending.

## 6. Review with Veer
- SendUserFile the MP4 + a push notification: "Reel ready: <title>. Reply post or skip."
- Include the caption + hashtags and the comment question in the message.
- Wait for his reply. No reply = do not post.

## 7. Post (only after "post")
Publish the MP4 to the public media repo (GitHub Pages, branch gh-pages of veereshkumbar/technibaba-reels). Keep only the newest 4 videos and force-push a single orphan commit so the repo never grows:
```bash
F=$(date +%Y%m%d)-<morning|evening>.mp4
git clone --depth 1 -b gh-pages https://github.com/veereshkumbar/technibaba-reels /tmp/media && cd /tmp/media
mkdir -p v && cp $W/final.mp4 v/$F && ls -t v/*.mp4 | tail -n +5 | xargs -r rm
git checkout -q --orphan fresh && git add -A && git -c user.name=Claude -c user.email=noreply@anthropic.com commit -qm "media $F" && git push -q -f origin fresh:gh-pages
```
Wait ~90 s for Pages to rebuild, then post with `video_url = https://veereshkumbar.github.io/technibaba-reels/v/$F`.
(The session's network can't open github.io itself — that's fine, Instagram fetches it.)
If Instagram rejects the URL: wait 60 s and retry once; then try `https://raw.githubusercontent.com/veereshkumbar/technibaba-reels/gh-pages/v/$F`; last resort, ask Veer to upload via the Higgsfield upload widget and use `https://d2ol7oe51mr4n9.cloudfront.net/user_3DPRsARcZSBdHzJnbbgRN5iuBGL/<media_id>.mp4`.

Windsor: `execute_action(connector=instagram, action=create_video_post, account=17841461825179329, params={video_url, caption, share_to_feed:true, thumb_offset:<ms of hook frame>})`
Append to `posted.md`: date, slot, topic, media id, which URL type worked. Commit + push to `main` of technibaba-reels.
Also send the MP4 for Veer's manual YouTube Shorts upload.

## 8. Learn from the numbers (each run)
Before choosing a topic, pull the last 30 days from Windsor (`get_data`, connector instagram, fields: timestamp, media_caption, media_reach, media_views, media_reel_skip_rate, media_reel_avg_watch_time, media_shares, media_saved). Note what worked (low skip rate, high watch time, shares) in `posted.md` and lean the next topics/hooks that way.
