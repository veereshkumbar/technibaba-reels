# Premium style (default look from 20 Nov 2026)

**Update 19 Nov night (Veer): brand colours, not monochrome.** The kit now uses our navy + mint the premium way: deep navy studio with a spotlight and slow bokeh, glass panel with a mint hairline and dotted grid, cards in navy with hairlines, ONE mint keyword box (navy text), yellow only for numbers, red only for danger. Characters get a soft shadow + mint rim glow (`charfx`). Motion graphics (adapted from the HyperFrames registry, CSS/GSAP only, no WebGL): brand light-leak sweep on every page change and hit, blur-through page transitions, captions that build word by word with the keyword popping in, and an animated Instagram follow card ("Follow" → tap → "Following") in the last 2.4 s. The monochrome notes below are kept for history; where they say white highlight / grey cards, read mint highlight / navy cards.
More registry items to try (`npx hyperframes catalog`): badge-pop, mk-callout-highlight, notification-cascade, message-thread-reveal, apple-money-count, camcorder-hud, news-ticker. Avoid the WebGL "shader transition" blocks (they stall in our headless render).

Reference: the left-hand explainer panel in anshmehra.in's AI inference reel (24 Oct 2026): near-black background, hairline grid, viewfinder corner marks, graphite cards with thin borders, white line icons, one highlight style (a white box behind the keyword, black text), words revealed one by one. No rainbow colours, no thick outlines, no bouncy stickers.
Example: `examples/premium_upi_en` (English test, "It wasn't a hacker", 34 s).

## Use it
- Put an empty file `layout_premium` in WORKDIR. `pipeline/hf_build.py` then renders with `pipeline/hf_premium.html` (Inter font, quiet cross-fade page transitions, a short push-in instead of a shake on hits, dark captions with a white keyword box, thin white progress bar).
- In `page_tpl.html` include `__PREMIUM__` right after `__SPLIT__`, add the Inter @font-face lines and `${PDEFS}` to DEFS (copy the head of `examples/premium_upi_en/page_tpl.html`).
- Build the panel only with the kit in `pipeline/premium.js`: `PHEAD` (headline, *keyword* in a white box, word-by-word reveal), `PCARD` (graphite card; `on` = white hairline + glow, `state:'good'|'bad'`), `PBADGE`/`PICON` (line icons), `PPILL`, `PLABEL` (small spaced caps), `PARROW`, `PSTRIKE`, `pin(f,frame)` for entrances (no overshoot). Palette is `PR`.

## Rules
- **Colours:** background `#0A0A0C`, cards `#17171B`, lines `#2A2A31`, text `#F4F4F6`, muted `#8C8C96`. Colour only as a signal: `PR.good` (mint) for safe/right, `PR.bad` (soft red) for danger/wrong, at most one of them big on a page. Never yellow, purple, orange or gradients in the panel.
- **Type:** Inter 700 for headlines (56–80 px), 600 labels, 500 sub-text (24–28 px). Sentence case. One keyword box per line, at most two per page.
- **Layout:** one idea per page, 1–3 cards, generous empty space. Cards 800 px wide in a single column, or two 380 px cards side by side for a comparison.
- **Motion:** entrances fade + rise 26 px (`pin`), word-by-word headline reveal, cross-fade between pages. No wobble, rotation, stamps or shakes.
- **Sound:** soft cues only: `blip`, `tick`, `ding`, one `crack` for the twist; the hit still gets riser + boom. Music gain 0.16.
- **Words:** short, exact, calm. "Decline the request", not "BHAAG!!". No exclamation marks on screen; no emojis anywhere.
- **Characters** (Baba and Chotu) stay as they are, at 70% of the old split size (`PCS` in premium.js), on a dark studio floor with a soft spotlight (`strip()` default). Voices: Hindi Kokoro only (Veer: the American voices sound wrong in Hindi). Baba `kokoro:hm_omega` tempo 1.2, pitch 0.9 (deep, clear); Chotu `kokoro:hm_psi` 1.2, 1.03. See `examples/premium_upi_hi`.
