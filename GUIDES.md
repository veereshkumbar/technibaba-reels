# Guides: technibaba.com/guides + "Comment GUIDE" automation

## How it works
1. Tutorial reels end with: "Comment karo GUIDE" (always the same word).
2. Instagram (Meta Business Suite "Comment to message" automation, set up once by Veer) DMs everyone who comments GUIDE: "Here is your guide: https://technibaba.com/guides". Newest guide is always on top.
3. Every scheduled run also posts a public reply "Check your DMs" under new GUIDE comments (see below).
4. technibaba.com/guides reads `guides/guides.json` from this public repo at page load, so adding a guide needs only a push here, never a website deploy.

## Language
Everything on the website is in plain English: titles, summaries, steps, tips and notes. The reels and their spoken lines stay in Hinglish. No emojis anywhere on the site, in guide text or in comment replies.

## Adding a guide (tutorial runs, before posting the reel)
Add an entry at the top of `guides/guides.json` and push:
```
{"slug": "kebab-case-unique", "date": "YYYY-MM-DD", "title": "...", "lane": "Tutorial" | "Creator Guide",
 "summary": "1–2 lines", "steps": [{"title": "...", "body": "exact menu path / command, verified today"}],
 "tip": "...", "caution": "...", "youtube": "", "reel": "<Instagram permalink, add after posting>", "sources": [{"title": "...", "url": "..."}]}
```
After posting, put the reel's permalink in `reel` (Windsor field media_permalink) and push again. Keep the file valid JSON (`python3 -c "import json;json.load(open('guides/guides.json'))"`).
Link to one guide: https://technibaba.com/guides?g=<slug>

## "Check DM" public replies (every scheduled run, first thing after setup)
1. Windsor get_data (connector instagram, account 17841461825179329, date_preset last_7d): fields comment_id, comment_text, comment_timestamp, media_id.
2. For each comment whose text contains "guide" (any case), whose comment_id is not in `guides/replied.txt`, posted in the last 7 days: Windsor execute_action reply_to_comment {comment_id, message: "Check your DMs, the guide is on its way. technibaba.com/guides"}. Append the comment_id to guides/replied.txt. Max 30 replies per run; vary the message slightly (3 variants) so it is not spammy.
3. Commit replied.txt with the run's other changes.
Never reply to other comments automatically, never DM from here.
