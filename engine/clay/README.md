# engine/clay: clay comedy episode pipeline
1. `clay_audio.py WORKDIR`: script.py (VOICES + LINES) to ElevenLabs voices, Rhubarb lip-sync cues, anim.json, mix_final.wav, caption filter. Needs `rhubarb` (download the Linux release from github.com/DanielSwaenberg/rhubarb-lip-sync, v1.13.0, set RHUBARB) and ELEVENLABS_API_KEY (or existing vo/lNN.mp3).
2. On the Mac, in Blender (execute_blender_code): `ANIM='.../anim.json'; WALL_JOKE='...'; exec(open('.../clay_apply.py').read()); clay_render('.../clay_silent.mp4')`. About 3.5 s per frame, about 28 min for 481 frames. Poll `bpy.app.is_job_running('RENDER')`.
3. `clay_assemble.sh WORKDIR clay_silent.mp4`: 30 fps, captions, mix, final MP4.
4. Post: RUNBOOK.md section 7 for Instagram (gh-pages + Windsor create_video_post + first comment); YouTube via the built-in browser (see the clay-comedy-reel skill).
Scene: `technibaba_clay/clay_set.blend` on Veer's Mac (objects Host, H_*, Baba coin, Wall_Follow1, Wall_Joke, CAM_Wide/Host/Baba). Backup of the pilot scene: clay_set_pilot01_backup.blend.

## Camera angles (28 Nov 2026, Veer: never the same angle every episode)
`clay_apply.py` holds an angle library (`ANG`, 13 cameras added to the scene each run, plus the original CAM_Wide, CAM_Host, CAM_Baba):
- wide: tilted (W_DUTCH), from above (W_HIGH), left and right three-quarter (W_L, W_R)
- host: from above (H_HIGH), three-quarter left and right (H_3Q_L, H_3Q_R, coin in the foreground), low hero angle (H_LOW), extreme mouth close-up (H_MOUTH)
- coin Baba: low (B_LOW), high (B_HIGH), three-quarter (B_3Q), tilted (B_DUTCH)

Each episode gets a seeded random plan: varied opener that shows the wall text, angle by speaker (never the same camera twice in a row or twice in a row for the same speaker), a wide at the middle line, a punch angle on the last line, a varied end shot, and a mid-line cut on lines longer than 2.4 s. The script prints `camera plan:` with frame:camera pairs. Set `ANGLE_SEED=<int>` before `exec` to force another plan. Timeline markers drive the camera, so test stills must render at cut frames and must not set `scene.camera`.
Tip: `device_commit_files` once delivered a stale copy when the staged file was overwritten at the same path; stage a new filename and check the file size on the Mac.
