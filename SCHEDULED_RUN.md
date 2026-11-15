# Scheduled run playbook (all 5 daily slots)

Every scheduled reel follows this file. The slot's own prompt only says which slot it is and what its topic lane is.

| Slot (IST) | Lane | Notes |
|---|---|---|
| 06:38 morning | Tutorial: everyday tech how-to (phone, apps, settings, safety, money apps, travel tech) | Comment keyword + DM checklist |
| 10:00 | Trending TECH | Today's tech story, explained simply |
| 14:00 | Trending SPORTS through a tech angle | Tech behind the sport, the stat, the app, the broadcast |
| 17:00 evening | Tutorial: Creator Guides (CREATOR_GUIDES.md) | How we make our videos, free tools, repos, skills |
| 21:00 | Trending BOLLYWOOD / OTT / gaming through a tech angle | VFX, AI, streaming, box-office data, game tech |
If nothing in the lane is trending and safe today, use trending tech and say so.

## 1. Setup
`git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh` and fix every ERROR line.
Read: RUNBOOK.md (all of it, especially "Rules for scheduled runs" and "Auto-post rules"), this file, RESEARCH.md, CRAFT.md, SPLIT_FORMAT.md, DIRECTOR_FORMAT.md, brand/dynamics.md, brand/tokens.json, posted.md, research/topic_bank.md. Tutorial slots also read STEPS_FORMAT.md; the evening slot reads CREATOR_GUIDES.md.

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
5. Pick the topic. Write 3 storylines (CRAFT.md) and 3 hooks; pick the one most likely to be SHARED ("send this to the friend who…"). Write down why in one line, with the evidence.
No repeats from posted.md (30 days), no keyword reuse (30 days), different topic from today's other slots (check posted.md and today's commits).

## 4. Build (premium, split layout, HyperFrames)
Exactly as SPLIT_FORMAT.md "Render with HyperFrames", starting from a copy of `examples/split_wifi2`:
script.py (LINES + BEATS, every line has a rig key) → engine/voice.py → pipeline/beats.py (all checks true) → engine/build.py → engine/shots.py (fix overlaps, keep everything inside the title-safe box) → engine/lofi.py (new seed/mood) → pipeline/hf_build.py (≥40 sfx cues; every panel element has a cue) → in hf/: hyperframes lint (0 errors) and snapshot (look at it, fix problems) → hyperframes render -q looks (nohup, poll) → pipeline/check.py (ALL CHECKS PASS).
Reel rules: 30–45 s, full-screen hook that shows the payoff first and lands by 1.5 s, one visual per idea in the panel, a visual change every 2–3 s, at most two hit-stops, captions with one highlighted keyword, ending with recap + comment keyword or question + "dost ko bhejo" / "save karo".
Tutorial slots: 3–4 steps, exact menu paths verified today, a comment keyword (ALL CAPS, 4–7 letters) and a DM guide text under 900 characters.
Trending slots: the news in one line, then the tech explanation; attribute every claim ("report ke hisaab se…"); no real photos, footage, logos or lookalikes of real people.
Fallbacks: HyperFrames fails twice → engine/render.py + engine/audio.py. Split build fails twice → STEPS_FORMAT.md (tutorials) or examples/director_wifi (trending). A fallback means gate 2 fails, so the reel waits for Veer.

## 5. Post (auto) or hold
Go through RUNBOOK.md "Auto-post rules" gate by gate and write each result in your notes.
- All pass → add_repo veereshkumbar/technibaba-reels (push) → publish to gh-pages (orphan commit, keep the newest 6 videos) → wait 3 minutes → Windsor create_video_post (account 17841461825179329, share_to_feed true, thumb_offset on the hook frame; caption with the hook line, 3–5 lines of value, the comment/save/share prompt, 6–10 hashtags) → on a media error wait 2 more minutes and retry once → `git pull --rebase` then log in posted.md with "AUTO-POSTED", slot, lane, format, hook, keyword, why → push.
- Any gate fails → do not post; hold for Veer as below.

## 6. Report
SendUserFile the MP4 (for the manual YouTube upload) and qa/contact.png (proactive) → PushNotification "<Slot> reel posted: <title>" or "<Slot> reel needs your OK: <title> — reply post or skip" → SendUserMessage with: media id (if posted), caption, hashtags, keyword, sources, why this topic, skills used, and for tutorials the DM guide text. If held, name the failed gate; only on "post" publish as in step 5; "skip" → confirm skipped.
On a twice-failed step: SendUserMessage + PushNotification with the error, simplify, still finish premium.
Instagram only; YouTube is manual; post nowhere else.
