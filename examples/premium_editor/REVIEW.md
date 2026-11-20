Review 20 Nov 2026 17:00 Creator Guide (CapCut ban -> VN / Edits)
Frames checked: engine shots 0.3/1.5/4.5/5.8/6.5/9.8/10.5/11/13/13.5/15.6/17/19.5/21.5/24.5/26.5/28.5/31.5 s, HyperFrames snapshot 0.5/9.6/16.5/22/26/31 s, seam frames 15.9/16.1 s, final contact sheet (9 beats).
- t=0-1.5s · hook phone overlapped Chotu's cap → replaced with a wide 'CapCut · India mein nahi milta' card above the characters. Fixed.
- t=4.5s · 'capcut i .com' had gaps (width estimate) → one text with a red tspan for the extra i. Fixed.
- t=8/17s · caption 'Free, *no watermark*' made two keyword boxes → one keyword. Fixed.
- Stranger read per beat: CapCut banned, what now / fake APK site = password stolen / VN good, but best? / send to the friend hunting the APK / name? / EDITS free, no watermark, auto captions / music library, export to Instagram / 4 steps / comment GUIDE.
Render: the one-shot HyperFrames render needed >10 min (shell limit 600 s) and a detached render is cancelled when the shell exits, so it was rendered as two HyperFrames segments (0-16 s, 16-32.08 s; 480 + 483 = 963 frames, same settings), joined with concat -c copy, and the full mix.wav muxed once. Same renderer and look, no fallback.
check.py: ALL CHECKS PASS (32.08 s, hook 0.13 s, max gap 2.5 s, peak -6.4 dB measured, not heard). 99 SFX cues; hits at 9.4 s (BEST) and 16.0 s (EDITS). Weakest shot: 16.1 s (empty panel mid page-change, 1-2 frames).
