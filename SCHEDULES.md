# Scheduled tasks (recreate from a fresh chat if needed)

Two scheduled tasks, Asia/Kolkata, push notifications on:
- **TechniBaba morning reel** — `CRON_TZ=Asia/Kolkata 38 6 * * *`
- **TechniBaba evening reel** — `CRON_TZ=Asia/Kolkata 38 17 * * *`

Create them from a chat whose only repo is `technibaba-reels` (or none). A chat that has a repo Claude has lost access to cannot create scheduled tasks.

## Prompt (replace SLOT/EMOJI; evening adds the format choice)
Veer is NOT watching while you work. Don't ask anything until the video is delivered.
0. SendUserMessage "EMOJI SLOT reel: starting. Video in ~30–40 min." Load PushNotification via ToolSearch "select:PushNotification".
1. `git clone --depth 1 https://github.com/veereshkumbar/technibaba-reels /tmp/tb && cd /tmp/tb && ./setup.sh` — fix any ERROR line of the self-check. Read RUNBOOK.md (incl. "Rules for scheduled runs"), STYLE_GUIDE.md, DOC_FORMAT.md, posted.md; follow RUNBOOK in order.
2. Windsor stats: connector instagram, account 17841461825179329, last_30dT (continue if it fails).
3. Topic. Morning: today's most trending story, ~70% tech, else Bollywood/sports/gaming via tech. Evening: (a) funny explainer 35–45s, or (b) TechniBaba Docs 45–55s per DOC_FORMAT.md, 2–3 evenings/week, never two evenings in a row. No repeats from posted.md (30 days). ≥3 sources; attribute allegations. No real photos/footage/logos/lookalikes.
4. Script → voice → page → QA screenshots (fix overlaps, weakest scene) → render (~8 min) → audio. On a twice-failed step: SendUserMessage + PushNotification with the error, use the simpler fallback, still finish.
5. SendUserFile MP4 (proactive) → PushNotification "SLOT reel ready: <title> — reply post or skip" → SendUserMessage with caption, hashtags, comment question, sources.
6. Only on "post": add_repo veereshkumbar/technibaba-reels (push), publish to gh-pages, post via Windsor create_video_post (account 17841461825179329, share_to_feed true, thumb_offset on hook) per RUNBOOK step 7, log in posted.md on main. "skip" → confirm skipped. YouTube manual; post nowhere else.
