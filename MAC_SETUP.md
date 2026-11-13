# MacBook Pro M1 setup (one time, ~45 min) — custom voice + original music

Both tools run locally on Apple Silicon (Metal/MPS). Nothing to pay.

## 1. VoiceStudio — Techni Baba's own voice (and Chotu's)
1. Download the macOS (Apple Silicon) installer from the latest release: https://github.com/debpalash/VoiceStudio/releases/latest
2. Open it → Model Manager → keep the default engine (OmniVoice). It downloads the model once.
3. Record the reference voice: 20–40 s, quiet room, phone close, natural Hinglish, e.g. read a TechniBaba script calmly (Baba). Optionally a second person for Chotu (faster, higher, excited).
4. In VoiceStudio: Clone → add the recording → test with one Hinglish line in Devanagari and one in Roman script; keep whichever sounds better.
5. Export the voice/profile and the two reference WAVs and send them to Claude. Claude adds them to the engine (`voices/`) so every reel uses them.
   - Licence: the app is AGPL-3.0; each model shows its own licence in Model Manager — pick one that allows commercial use.
   - Only clone voices you own or have permission for.

## 2. ACE-Step 1.5 — original TechniBaba music
1. Download the macOS portable package (pre-installed dependencies): https://files.acemusic.ai/acemusic/mac/ACE-Step-1.5.zip (linked from https://github.com/ace-step/ACE-Step-1.5)
2. Unzip, run the start script, open http://127.0.0.1:7860.
3. On an M1 use the 2B **turbo** model with the LM off if memory is tight (8 GB Macs), LM on for 16 GB.
4. Make a starter pack (each 60–90 s, instrumental unless noted):
   - `theme_main` — "upbeat Indian lo-fi hip hop, tabla + soft synth, playful, 92 bpm, loopable"
   - `funny_chase` — "comedic quirky pizzicato + kazoo, fast, cartoon chase"
   - `doc_serious` — "cinematic documentary underscore, warm piano and strings, curious"
   - `tension_scam` — "suspense, low pulses, ticking, thriller"
   - `jingle` — 5 s sung "Techni Baba!" sting in Hindi (vocals on)
5. Send the WAVs to Claude → they go into `music/` with mood tags, and `audio.py` picks one per reel.

## 3. Later (optional)
- FLUX.2 [klein] 4B (Apache-2.0) for thumbnail/cover frames — slower on M1; try only if the above works well.
