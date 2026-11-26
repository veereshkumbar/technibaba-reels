# Scheduled run playbook (2 daily slots, from 24 Nov 2026)

Every scheduled reel follows this file. The slot's own prompt only says which slot it is and what its topic lane is.

| Slot (IST) | Run starts | Lane | Notes |
|---|---|---|---|
| 11:00 | 10:25 | Tutorial: everyday tech how-to (phone, apps, settings, safety, payments, travel tech); Sunday = Creator Guide (CREATOR_GUIDES.md) + weekly brief | Comment keyword + DM guide |
| 19:00 | 18:25 | Today's biggest story through tech: tech, sports (cricket first) or Bollywood/OTT/gaming | Verified facts, attribute every claim |

Paused (not deleted, 23 Nov 2026): 7 AM news, 10 AM trending tech, 2 PM sports, 5 PM creator guide. Only two reels a day now, so each run picks the strongest topic of the day; quality over volume.
If nothing in the lane is trending and safe today, use trending tech and say so.

## Target
Veer's target: grow @technibaba from 36 followers (15 Nov 2026) to 20,000 by mid-December 2026. Every run optimises for follows: shares and saves first, then watch-through. Each Sunday's weekly brief reports followers now vs the target, the week's top 3 reels by follows/shares/saves, what they had in common, and what the next week's runs will do more and less of (written into research/topic_bank.md so every slot picks it up).

## Content plan v2 (26 Nov 2026, from the 30-day Windsor analysis)
Data (56 reels, 12-26 Nov): median views by lane: cricket/sports 1,197; AI/subscriptions 818; gaming 342; scam/phone safety 267 (but about 3 saves per reel vs 1 elsewhere); phone how-to 182 (skip rate 50%, zero saves or shares). 98% of views come from non-followers. Median views fell from about 1,170 (17-20 Nov) to about 134 (21-26 Nov) and the 3-second skip rate rose from 33% to 51%; that coincides with the move to the brand-premium split layout and Kokoro voices, but also with 5 posts a day dropping to 2, so it is a suspect, not a conclusion.
Rules for every run:
1. **7 PM slot lead lane = cricket and sports through tech** (DRS, ball tracking, stats, streaming lag, broadcast tech). If there is no live sport that day, use AI/subscription changes. Hooks that worked: a relatable "dost bolta hai..." claim, or a ruling that looks wrong ("ball stumps pe lagi, phir bhi NOT OUT").
2. **11 AM slot = safety "run this check on your phone now"** (SIM in your name, auto-lock after snatching, pension/life-certificate, UPI limits). Stop plain phone how-to reels (settings walkthroughs with no urgency). Keep the GUIDE keyword.
3. **Skip-rate rule:** read media_reel_skip_rate for the last 10 reels in step 3. If the median is above 45%, make the hook more extreme (payoff or a surprising claim in the first 1.5 s) and cut the first scene to 1 idea.
4. **Layout test (27, 28, 29 Nov 7 PM slots only):** build the 7 PM reel in the pre-20-Nov look (plain split layout from SPLIT_FORMAT.md, not the PREMIUM_STYLE kit), cricket/sports lane. Log "TEST old-look" in posted.md. After 29 Nov, compare median views and skip rate of the 3 test reels against the last 6 premium reels and write the verdict in research/topic_bank.md. If the old look wins, drop the premium kit for trending slots.
5. **Clay comedy series (3D, Blender, Hindi):** 2 a week (Wed and Sat). The scheduled run only prepares the clay script: write `clay_queue/YYYY-MM-DD.json` (14 short Hinglish lines alternating host and coin Baba, a relatable client/dev/creator vs AI or software joke, each line under 8 words, an ending twist, caption, one-word comment question) and push it; the 7 PM run still posts a normal reel. The clay reel itself is rendered on Veer's Mac in a chat session (about 30 min, see clay_pilot notes in PREMIUM_STYLE.md) and posted manually, so a sleeping Mac never blocks the schedule. Compare clay vs normal reels on skip rate, shares and non-follower views after 48 hours.

## 1. Setup
`git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh` and fix every ERROR line.
Read: FORMATS.md, PREMIUM_STYLE.md, SOUND_DESIGN.md, GUIDES.md, LONG_FORMAT.md (tutorial slots), RUNBOOK.md (all of it, especially "Rules for scheduled runs" and "Auto-post rules"), this file, RESEARCH.md, CRAFT.md, SPLIT_FORMAT.md, DIRECTOR_FORMAT.md, brand/dynamics.md, brand/tokens.json, posted.md, research/topic_bank.md. Tutorial slots also read STEPS_FORMAT.md; the evening slot reads CREATOR_GUIDES.md.

## 1b. Comments (every run, before anything else)
1. Do the "Check DM" public replies in GUIDES.md.
2. Then reply to EVERY other new comment on our last 10 reels (Windsor instagram, last_7d, fields comment_id, comment_text, comment_timestamp, media_id, same as GUIDES.md; skip ids already in guides/replied.txt and our own comments). Reply in short Hinglish as TechniBaba: answer the question or react to their answer, and end with a small question back when it fits, so the thread continues. No emojis, no links except technibaba.com/guides, never argue, never share personal data. Hide (do not delete) spam or abuse with hide_comment. Log each replied id in guides/replied.txt and push.

## 2. Skills (use every one that helps, before writing anything)
- `technibaba-director` skill: follow its story → spec → proof stages, its reel rules and its avoid table.
- `video-making` skill: before rendering.
- The repo's research playbooks in `vendor/scrapecreators-skills/`: outlier-post-finder, comment-mining, trend-discovery, competitor-social-research, creator-profile-teardown, transcript-intelligence. Use their methods with Windsor data and web search (we have no ScrapeCreators key; do not sign up for anything).
- `vendor/hyperframes-refs/` and the HyperFrames CLI docs (`npx hyperframes docs <topic>`) for motion and transitions.
- Any other skill listed in the session that fits (search with SearchSkills for "reels", "instagram", "growth", "video" if available). Write one line per skill used in your notes: what it changed in the plan.

## 3. Research → decide what will grow the channel
Goal: followers. What earns them on Instagram: shares (DMs) and saves first, then watch-through and comments. Every decision below serves those.
1. Windsor (connector instagram, account 17841461825179329, last_30dT): reach, plays, shares, saves, follows per reel. Find our outliers vs our median (outlier-post-finder). Note which hook, lane and format they used.
2. Comment mining on the last 5 reels: questions people ask become topics.
3. Web trend check for the slot's lane (trend-discovery): what is trending in India today, plus one global angle. ≥3 sources.
4. Look at 2-3 top creators in the lane (competitor research, creator teardown): note hook patterns and formats only; never copy their content, footage or wording.
5. Pick the topic and ONE of the 5 formats in FORMATS.md (rotate; no format twice on the same day, check posted.md). Write down the format number and the question the viewer will have at 6 s; the claim lands by 6–10 s, the why/how is the body and is fully answered only in the last 20%. Write 3 storylines (CRAFT.md) in that format and 3 hooks; pick the one most likely to be SHARED ("send this to the friend who…"). Write down why in one line, with the evidence.
No repeats from posted.md (30 days), no keyword reuse (30 days), different topic from today's other slots (check posted.md and today's commits).

## 4. Build (premium, split layout, HyperFrames)
Look: PREMIUM_STYLE.md (monochrome, Inter, graphite cards, white keyword box, calm motion). Start from a copy of `examples/premium_upi_en` (keep `layout_premium`), write the script in Hinglish unless Veer says otherwise, and build the panel only with the `pipeline/premium.js` kit. Then exactly as SPLIT_FORMAT.md "Render with HyperFrames":
script.py (LINES + BEATS, every line has a rig key) → engine/voice.py (VOICES per PREMIUM_STYLE.md: ElevenLabs Shivank/Viraj with Kokoro fallback; report eleven_usage.json chars) → pipeline/beats.py (all checks true) → engine/build.py → engine/shots.py (fix overlaps, keep everything inside the title-safe box) → engine/lofi.py (new seed/mood) → pipeline/hf_build.py WORKDIR WORKDIR/bed.wav 0.16 (the music input must NOT be named music.wav: audio.py writes music.wav and would overwrite its own input) (sound per SOUND_DESIGN.md: accents on meaning moments, 1-2 impacts, whooshes only on page changes; then check WORKDIR/sfx_report.json) → in hf/: hyperframes lint (0 errors) and snapshot (look at it, fix problems) → hyperframes render -q looks (run it in the foreground with a 600 s timeout; a backgrounded render gets cancelled when the shell call ends) → pipeline/check.py (ALL CHECKS PASS).
Reel rules: 25–35 s (hard gate in beats.py: 22–36 s), full-screen hook that shows the payoff first and lands by 1.5 s, one visual per idea in the panel, a visual change every 2–3 s, at most two hit-stops, captions with one highlighted keyword. See "Engagement rules" below; they decide the script.

### Engagement rules (18 Nov 2026 data, apply to every slot)
Data: 18 of our last 32 reels reached 1,000–1,350 people and every one stopped there, whatever the topic. That is Instagram's first test audience; a reel only goes further if those people watch, share, save and comment. Ours: about 2 shares, 4 saves, 12 likes and ~0 comments per 1,000 people reached, and 10–19 s average watch on 40–60 s reels. So most viewers never reached our end-screen "dost ko bhejo" / "comment GUIDE".
1. **Payoff by 10 s** (the format's claim: the result, C, the contradiction, "best way exists", "unless"; the why/how stays open until the end, see FORMATS.md). The single most useful fact or result is said and shown inside the first 10 s (most people are gone by 12–15 s). The rest is support, not build-up.
2. **Share ask in the middle, on screen, at 8–12 s,** tied to one specific person: "Papa ko bhejo jo har link dabate hain", "Us dost ko bhejo jo 140 ka daava karta hai". Big on-screen text plus Baba/Chotu pointing, with an SFX hit. Pick the topic so that a clear "who do I send this to" exists; if you cannot name that person in one line, pick another topic.
3. **One ask only at the end:** a one-word comment question ("HAAN ya NA?", "PAPA ya DADI?") or the GUIDE keyword on tutorials. No recap list; the last line flows back into the first line so the reel loops (e.g. last line ends on the question the hook answers).
4. **Comments:** after posting, add a first comment on the reel (Windsor `create_comment`) with the same one-word question, so the comment section is never empty. Step 1b replies to every new comment.
Tutorial slots: 3–4 steps, exact menu paths verified today. The comment keyword is ALWAYS "GUIDE" ("Comment karo GUIDE, guide DM mein bhejunga"). Before posting, add the guide to guides/guides.json per GUIDES.md (website text in plain English, no emojis) (the DM automation links to technibaba.com/guides, so the guide must be live first). After posting, add the reel permalink.
Tutorial slots also make the long YouTube version per LONG_FORMAT.md (spec.json → render), after the reel is posted. If time or usage runs short, deliver the reel first and say the long video was skipped.
Trending slots: the news in one line, then the tech explanation; attribute every claim ("report ke hisaab se…"); no real photos, footage, logos or lookalikes of real people.
Fallbacks: HyperFrames fails twice → engine/render.py + engine/audio.py. Split build fails twice → STEPS_FORMAT.md (tutorials) or examples/director_wifi (trending). A fallback means gate 2 fails, so the reel waits for Veer.

## 5. Post (auto) or hold
Go through RUNBOOK.md "Auto-post rules" gate by gate and write each result in your notes.
- All pass → add_repo veereshkumbar/technibaba-reels (push) → publish to gh-pages (orphan commit, keep the newest 6 videos) → wait 3 minutes → Windsor create_video_post (account 17841461825179329, share_to_feed true, thumb_offset on the hook frame; caption per RUNBOOK.md "Captions": NO emojis, hook line, 2–4 lines of value, one call to action, 5–8 hashtags) → on a media error wait 2 more minutes and retry once → Windsor create_comment on the new media id with the reel's one-word question (no emojis) → `git pull --rebase` then log in posted.md with "AUTO-POSTED", slot, lane, format, script format (1-5), hook, keyword, why → push.
- Any gate fails → do not post; hold for Veer as below.

## 6. Report
SendUserFile the MP4 (for the manual YouTube upload) and qa/contact.png (proactive) → PushNotification "<Slot> reel posted: <title>" or "<Slot> reel needs your OK: <title> — reply post or skip" → SendUserMessage with: media id (if posted), caption, hashtags, keyword, sources, why this topic, skills used, and for tutorials the guide link (https://technibaba.com/guides?g=<slug>), then the long YouTube MP4 with its title, description and tags, asking Veer to reply with the YouTube link once uploaded (then add it to guides.json and push). If held, name the failed gate; only on "post" publish as in step 5; "skip" → confirm skipped.
On a twice-failed step: SendUserMessage + PushNotification with the error, simplify, still finish premium.
Instagram only; YouTube is manual; post nowhere else.
