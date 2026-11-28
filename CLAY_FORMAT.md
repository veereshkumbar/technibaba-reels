# Clay comedy series (3D, Hindi)

Goal: skits a viewer recognises as their own job, so they laugh, tag a colleague and follow. Each reel is one workplace pain, played by the Host (human) and Baba (our logo coin, the voice of the AI, the software or the "client"). 25-35 s, 12-16 short lines.

## Pick the role first (rotate; never the same role twice in a row)
Developer, designer, manager, QA tester, freelancer, video editor, startup founder, intern, HR/recruiter, sales/client-facing.
Each skit has a tag line the viewer sends to a named colleague: "Ye apne designer ko bhejo", "Is manager ko tag karo".

## Script rules
1. Frame 0 is the problem in one line the role has said or heard ("Baba, client ne bola, bas thoda sa change").
2. Escalate three times (v3, v17, v61), each beat shorter than the last; the twist lands in the last 4 seconds and reverses who was right.
3. Under 8 words per line, plain Hinglish, no jargon the role would not already use; no real company, person or product names, nothing about a real employer.
4. Humour punches at the situation (deadlines, scope creep, "works on my machine"), never at a caste, religion, gender, region or a person.
5. Ending asks one thing: a one-word comment ("aapka sabse bada version number?") plus a share ask naming the role.
6. Caption: no emojis, hook line, 2 lines, the share ask naming the role, 5-8 hashtags (include the role tag, e.g. #developerlife #designerlife #managerlife).

## Wall text (top empty space of the back wall)
- Line 1, neon mint, always on: "FOLLOW KARO  @technibaba" (object Wall_Follow1).
- Line 2, cream clay letters, changes per episode: the role's in-joke on ONE line, 19 characters or fewer (object Wall_Joke, set `data.body`). Examples: Developer "WORKS ON MY MACHINE", Designer "BAS EK PIXEL HILA DO", Manager "KAL TAK KAR DENA", QA "BUG NAHI FEATURE HAI", Freelancer "ADVANCE KAB AAYEGA", Editor "FINAL_V9 REAL_FINAL".
- Both sit above the string lights, centred, so they never touch the window or the characters. The old poster board is hidden.
- The joke is visible for the whole reel, so it must work before the viewer reads any caption.

## Queue file (scheduled runs write it; chat renders it)
`clay_queue/YYYY-MM-DD.json`: `{ "role": "...", "wall_joke": "ONE LINE", "lines": [{"who":"h|b","text":"..."}], "caption": "...", "comment_question": "..." }`

## Render notes
Blender set at `technibaba_clay/clay_set.blend` on Veer's Mac. Output media_type VIDEO then file_format FFMPEG; keep resolution at 1080x1920. Animation on twos at 15 fps, doubled to 30 in the final ffmpeg step. Voices ElevenLabs: Host = Viraj, coin Baba = Shivank. Keep the first-version audio mix (loudnorm about -16 LUFS), Veer preferred it.

## Camera angles
Veer's rule (28 Nov 2026): the same angle every time does not work. The engine now varies angles automatically (see engine/clay/README.md, "Camera angles"). Aim for at least six distinct cameras per episode, a wall-text opener, and a punch angle (low, high, tilted or mouth close-up) on the last line.
