# Scheduled run playbook (all 6 daily slots)

Every scheduled reel follows this file. The slot's own prompt only says which slot it is and what its topic lane is.

| Slot (IST) | Lane | Notes |
|---|---|---|
| 06:38 morning | Tutorial: everyday tech how-to (phone, apps, settings, safety, money apps, travel tech) | Comment keyword + DM checklist |
| 07:00 | TechniBaba Daily news bulletin (NEWS_FORMAT.md) | Biggest story first, then 5–7 stories, mostly tech |
| 10:00 | Trending TECH | Today's tech story, explained simply |
| 14:00 | Trending SPORTS through a tech angle | Tech behind the sport, the stat, the app, the broadcast |
| 17:00 evening | Tutorial: Creator Guides (CREATOR_GUIDES.md) | How we make our videos, free tools, repos, skills |
| 21:00 | Trending BOLLYWOOD / OTT / gaming through a tech angle | VFX, AI, streaming, box-office data, game tech |
If nothing in the lane is trending and safe today, use trending tech and say so.

## Target
Veer's target: grow @technibaba from 36 followers (15 Nov 2026) to 20,000 by mid-December 2026. Every run optimises for follows: shares and saves first, then watch-through. Each Sunday's weekly brief reports followers now vs the target, the week's top 3 reels by follows/shares/saves, what they had in common, and what the next week's runs will do more and less of (written into research/topic_bank.md so every slot picks it up).

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
script.py (LINES + BEATS, every line has a rig key) → engine/voice.py → pipeline/beats.py (all checks true) → engine/build.py → engine/shots.py (fix overlaps, keep everything inside the title-safe box) → engine/lofi.py (new seed/mood) → pipeline/hf_build.py WORKDIR bed.wav 0.16 (sound per SOUND_DESIGN.md: accents on meaning moments, 1-2 impacts, whooshes only on page changes; then check WORKDIR/sfx_report.json) → in hf/: hyperframes lint (0 errors) and snapshot (look at it, fix problems) → hyperframes render -q looks (run it in the foreground with a 600 s timeout; a backgrounded render gets cancelled when the shell call ends) → pipeline/check.py (ALL CHECKS PASS).
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
