# Scheduled tasks

Five daily slots (IST). The full playbook every run follows is `SCHEDULED_RUN.md`.

| Slot | Time | Status |
|---|---|---|
| TechniBaba morning tutorial reel | 06:38 | exists (trig_01N9cQ8Chwi8Smpa64zgUJin) |
| TechniBaba 7 AM news bulletin | 06:52 | TO CREATE |
| TechniBaba 10 AM trending tech reel | 09:52 | TO CREATE |
| TechniBaba 2 PM trending sports reel | 13:52 | TO CREATE |
| TechniBaba evening creator guide reel | 17:00 | exists (trig_01FquY2ingpGnaR4zku2d2Q7) |
| TechniBaba 9 PM Bollywood x tech reel | 20:52 | TO CREATE |

## How to create the three missing slots
The chat that built the pipeline cannot create scheduled tasks (it is attached to a private repo). Open a NEW chat with no repo attached and paste:

> Create 3 scheduled tasks from https://github.com/veereshkumbar/technibaba-reels/blob/main/SCHEDULES.md, section "Prompts for the new slots": names, cron expressions and prompts exactly as written there. Push notifications on. Then list my scheduled tasks to confirm.

## Prompts for the new slots

### TechniBaba 10 AM trending tech reel
- cron: `CRON_TZ=Asia/Kolkata 52 9 * * *`

```
You are making today's 10 AM trending tech TechniBaba reel (10:00 IST). Veer is NOT watching while you work: don't ask anything; take the most reasonable choice and note it.
0. SendUserMessage "📱 10 AM trending tech reel: starting. Video in ~45 min." Load PushNotification via ToolSearch "select:PushNotification".
1. Follow SCHEDULED_RUN.md in the repo exactly, step by step: `git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh`, then read SCHEDULED_RUN.md and every file it lists.
2. Your lane: TRENDING TECH: today's most talked-about tech story in India (launch, update, AI, scam wave, app change), explained simply with what it means for the viewer. Attribute every claim.
3. Before writing anything, use every skill that helps (SCHEDULED_RUN.md step 2: technibaba-director, video-making, the research playbooks in vendor/scrapecreators-skills, HyperFrames docs, and any other fitting skill in the session), then do the research in step 3 to pick the topic most likely to be shared and saved and to earn followers. Write down the evidence.
4. Build premium in the split layout, rendered through HyperFrames, per SCHEDULED_RUN.md step 4.
5. POST IT YOURSELF. Veer has told us in chat that scheduled reels post without waiting for his "post". Check every gate in RUNBOOK.md "Auto-post rules for scheduled runs"; if all pass, publish and post per SCHEDULED_RUN.md step 5. If any gate fails, do not post: hold it for Veer and name the failed gate.
6. Report per SCHEDULED_RUN.md step 6 (MP4 + contact sheet, push notification, message with media id, caption, sources, why, skills used).
Instagram only; YouTube is manual; post nowhere else.
```

### TechniBaba 2 PM trending sports reel
- cron: `CRON_TZ=Asia/Kolkata 52 13 * * *`

```
You are making today's 2 PM trending sports TechniBaba reel (14:00 IST). Veer is NOT watching while you work: don't ask anything; take the most reasonable choice and note it.
0. SendUserMessage "🏏 2 PM trending sports reel: starting. Video in ~45 min." Load PushNotification via ToolSearch "select:PushNotification".
1. Follow SCHEDULED_RUN.md in the repo exactly, step by step: `git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh`, then read SCHEDULED_RUN.md and every file it lists.
2. Your lane: TRENDING SPORTS THROUGH TECH: today's big sports moment (cricket first, then football, kabaddi, F1, Olympics sports, esports) told through its tech: ball-tracking/DRS, wearables and stats, broadcast and streaming tech, apps, records in numbers. Verified public facts only; no betting or fantasy-money advice. If nothing fits safely, use trending tech and say so.
3. Before writing anything, use every skill that helps (SCHEDULED_RUN.md step 2: technibaba-director, video-making, the research playbooks in vendor/scrapecreators-skills, HyperFrames docs, and any other fitting skill in the session), then do the research in step 3 to pick the topic most likely to be shared and saved and to earn followers. Write down the evidence.
4. Build premium in the split layout, rendered through HyperFrames, per SCHEDULED_RUN.md step 4.
5. POST IT YOURSELF. Veer has told us in chat that scheduled reels post without waiting for his "post". Check every gate in RUNBOOK.md "Auto-post rules for scheduled runs"; if all pass, publish and post per SCHEDULED_RUN.md step 5. If any gate fails, do not post: hold it for Veer and name the failed gate.
6. Report per SCHEDULED_RUN.md step 6 (MP4 + contact sheet, push notification, message with media id, caption, sources, why, skills used).
Instagram only; YouTube is manual; post nowhere else.
```

### TechniBaba 9 PM Bollywood x tech reel
- cron: `CRON_TZ=Asia/Kolkata 52 20 * * *`

```
You are making today's 9 PM Bollywood x tech TechniBaba reel (21:00 IST). Veer is NOT watching while you work: don't ask anything; take the most reasonable choice and note it.
0. SendUserMessage "🎬 9 PM Bollywood x tech reel: starting. Video in ~45 min." Load PushNotification via ToolSearch "select:PushNotification".
1. Follow SCHEDULED_RUN.md in the repo exactly, step by step: `git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh`, then read SCHEDULED_RUN.md and every file it lists.
2. Your lane: TRENDING BOLLYWOOD / OTT / GAMING THROUGH TECH: today's film, trailer, OTT release or game buzz told through its tech: VFX and CGI, AI in films and music, de-ageing, streaming tech, box-office data, game engines. Verified public facts only; no gossip, rumours or private life; no real photos or lookalikes. If nothing fits safely, use trending tech and say so.
3. Before writing anything, use every skill that helps (SCHEDULED_RUN.md step 2: technibaba-director, video-making, the research playbooks in vendor/scrapecreators-skills, HyperFrames docs, and any other fitting skill in the session), then do the research in step 3 to pick the topic most likely to be shared and saved and to earn followers. Write down the evidence.
4. Build premium in the split layout, rendered through HyperFrames, per SCHEDULED_RUN.md step 4.
5. POST IT YOURSELF. Veer has told us in chat that scheduled reels post without waiting for his "post". Check every gate in RUNBOOK.md "Auto-post rules for scheduled runs"; if all pass, publish and post per SCHEDULED_RUN.md step 5. If any gate fails, do not post: hold it for Veer and name the failed gate.
6. Report per SCHEDULED_RUN.md step 6 (MP4 + contact sheet, push notification, message with media id, caption, sources, why, skills used).
Instagram only; YouTube is manual; post nowhere else.
```

### TechniBaba 7 AM news bulletin
- cron: `CRON_TZ=Asia/Kolkata 52 6 * * *`

```
You are making today's 7 AM TechniBaba Daily news bulletin reel (07:00 IST). Veer is NOT watching while you work: don't ask anything; take the most reasonable choice and note it.
0. SendUserMessage "7 AM news bulletin: starting. Video in ~45 min." Load PushNotification via ToolSearch "select:PushNotification".
1. Follow SCHEDULED_RUN.md in the repo exactly, step by step: `git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh`, then read SCHEDULED_RUN.md, NEWS_FORMAT.md and every file they list.
2. Your lane: NEWS BULLETIN per NEWS_FORMAT.md. Research the last 24-48 hours: mostly tech (India first, then global), plus at most two from gaming, space, films/OTT, sports or business. Pick the single most shareable story for the hook. Verify every story with at least 2 sources in this run; skip anything unverified, older, or in the excluded categories. Do not repeat stories from posted.md (7 days) or from yesterday's bulletin.
3. Before writing, use every skill that helps (SCHEDULED_RUN.md step 2) and check which of our past bulletins got the most shares and saves (Windsor), then write spec.json in the NEWS_FORMAT.md structure.
4. Build with pipeline/news_build.py and render through HyperFrames per NEWS_FORMAT.md. Check frames before the full render; pipeline/check.py must pass.
5. POST IT YOURSELF. Check every gate in RUNBOOK.md "Auto-post rules for scheduled runs"; if all pass, publish and post per SCHEDULED_RUN.md step 5 (caption: no emojis, numbered story list, comment question, 5-8 hashtags). If any gate fails, do not post: hold it for Veer and name the failed gate.
6. Report per SCHEDULED_RUN.md step 6 (MP4 + contact sheet, push notification, message with media id, caption, the stories with their sources).
Instagram only; YouTube is manual; post nowhere else.
```
