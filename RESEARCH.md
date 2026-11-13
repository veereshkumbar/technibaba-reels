# Growth research loop (what to make next, and why)

Method adapted from ScrapeCreators' MIT-licensed research skills (`vendor/scrapecreators-skills/`). Their data API is optional: everything below works with free sources first.

## Every run (5 minutes, before choosing a topic)
1. **Our own outliers.** Pull the last 30 days of @technibaba reels from Windsor (instagram, account 17841461825179329). For each reel: views (or reach), likes, comments, shares, saves.
   - Baseline = median views of the last 15 reels. **Outlier = views ≥ 2× baseline**; underperformer = ≤ 0.5×.
   - Write one line per outlier/underperformer: topic · format · hook (first line) · why it beat/missed the baseline.
   - Shares + saves per 1,000 views matter more than likes: they mean "useful" and "send to a friend".
2. **Comment mining** on our last 5 reels (when the connector returns comment text): sort into questions, confusions, requests ("make one on X"), objections, jokes. A repeated question = next topic. Quote the audience's exact words in the script.
3. **Trend check** with web search: today's Indian tech news + what is viral on Reels/Shorts in tech India (search "trending reels tech India today", Google Trends India tech, X trending India). Keep only trends with evidence (a link, a number, a date).
4. Pick the topic that scores best on: trending now × useful/funny × fits Chotu–Baba chat × not posted in 30 days. Log the reason in `posted.md`.

## Every Sunday morning run (extra 10 minutes): weekly brief
Write `research/weekly-YYYY-MM-DD.md` and commit it with the posted.md log:
- **Competitor outliers** (`outlier-post-finder` method) for 5–8 tech/explainer accounts. Candidates to verify: @techburner, @technicalguruji, @trakintech, @geekyranjit, @sharmajitechnical, @techwiser, @mrwhosetheboss, @marquesbrownlee. Use the ScrapeCreators API if `SCRAPECREATORS_API_KEY` is set and `api.scrapecreators.com` is reachable; otherwise use web search and public pages.
- **Swipe file**: the 10 best hooks of the week (first line + first-frame idea), rewritten in our voice — never copied word for word.
- **Formats that won** (chat, explainer, doc, list, myth-vs-fact, "X vs Y", scam alert) and runtime.
- **Topic bank**: add 10 ideas to `research/topic_bank.md` with the evidence link for each.
- **What we change next week** (max 3 bullet decisions), e.g. "hooks with a number in the first 2 s did 2.4× — use more".

## Hook rules (from outlier patterns)
- Frame 0 is the thumbnail and the hook: a face reacting + one bold line. Never black, never a logo.
- The question or conflict arrives in the first second; the payoff before 80% of the runtime.
- Strong openers: a shocking number, "Ye galti mat karna", a relatable problem ("Phone bola storage full"), a myth to bust, a "X vs Y" fight.
- End with a question people can answer in one word (comments) + a reason to send it to a friend (shares).
