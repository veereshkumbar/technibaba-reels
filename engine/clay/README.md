# engine/clay: clay comedy episode pipeline
1. `clay_audio.py WORKDIR`: script.py (VOICES + LINES) to ElevenLabs voices, Rhubarb lip-sync cues, anim.json, mix_final.wav, caption filter. Needs `rhubarb` (download the Linux release from github.com/DanielSwaenberg/rhubarb-lip-sync, v1.13.0, set RHUBARB) and ELEVENLABS_API_KEY (or existing vo/lNN.mp3).
2. On the Mac, in Blender (execute_blender_code): `ANIM='.../anim.json'; WALL_JOKE='...'; exec(open('.../clay_apply.py').read()); clay_render('.../clay_silent.mp4')`. About 3.5 s per frame, about 28 min for 481 frames. Poll `bpy.app.is_job_running('RENDER')`.
3. `clay_assemble.sh WORKDIR clay_silent.mp4`: 30 fps, captions, mix, final MP4.
4. Post: RUNBOOK.md section 7 for Instagram (gh-pages + Windsor create_video_post + first comment); YouTube via the built-in browser (see the clay-comedy-reel skill).
Scene: `technibaba_clay/clay_set.blend` on Veer's Mac (objects Host, H_*, Baba coin, Wall_Follow1, Wall_Joke, CAM_Wide/Host/Baba). Backup of the pilot scene: clay_set_pilot01_backup.blend.
