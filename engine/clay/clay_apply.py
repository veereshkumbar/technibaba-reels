"""Run inside Blender (execute_blender_code):  ANIM='/path/anim.json'; WALL_JOKE='WORKS ON MY MACHINE'; exec(open('/path/clay_apply.py').read())
Keys the clay set from anim.json: camera cuts, host lip-sync, coin (Baba) motion, host nod, ending head drop. Then call clay_render(out_path)."""
import bpy, json, math
S = bpy.context.scene; D = bpy.data.objects
A = json.load(open(ANIM)); FPS = A['fps']; N = A['frames']; segs = A['segs']
S.render.fps = FPS; S.frame_start = 0; S.frame_end = N - 1
SH = {'X': (.85, .07, 0, 0), 'A': (.85, .07, 0, 0), 'B': (.95, .35, .6, .5), 'C': (1.05, .8, 1, .6), 'D': (1.1, 1.3, 1, .5),
      'E': (.7, 1.0, 1, 0), 'F': (.55, .7, 1, 0), 'G': (.95, .3, .5, 1.0), 'H': (1.0, .55, 1, .3)}
# idempotent base transforms
for n in ('CAM_Baba', 'CAM_Host', 'CAM_Wide'):
    o = D[n]
    if 'base_loc' not in o:
        S.frame_set(0); o['base_loc'] = list(o.location); o['base_rot'] = list(o.rotation_euler); o['base_scale'] = list(o.scale)
for n in ('Baba', 'H_HeadRig', 'H_Mouth', 'H_MouthCav', 'H_Teeth', 'CAM_Baba', 'CAM_Host', 'CAM_Wide'):
    D[n].animation_data_clear()
for m in list(S.timeline_markers): S.timeline_markers.remove(m)
for n in ('CAM_Baba', 'CAM_Host', 'CAM_Wide'):
    D[n].location = D[n]['base_loc']
# wall text
if 'WALL_JOKE' in globals() and WALL_JOKE: D['Wall_Joke'].data.body = WALL_JOKE
# camera cuts: wide opener, host/coin by speaker, wide at the middle line and the end
def fr(t): return int(round(t * FPS))
mid = len(segs) // 2
cuts = [(0, 'CAM_Wide')]
for s in segs[:-1] if False else segs:
    cam = 'CAM_Wide' if s['i'] == mid else ('CAM_Host' if s['who'] == 'h' else 'CAM_Baba')
    if s['i'] == 0: continue
    cuts.append((fr(s['start']) - 2, cam))
cuts.append((fr(segs[-1]['start'] + segs[-1]['dur']) + 6, 'CAM_Wide'))
for k, (f, c) in enumerate(cuts):
    mk = S.timeline_markers.new(f'cut{k:02d}', frame=f); mk.camera = D[c]
# slow push-in on each camera (keys on location y)
for n in ('CAM_Baba', 'CAM_Host', 'CAM_Wide'):
    o = D[n]; b = o['base_loc']
    for f in range(0, N, 15):
        o.location = (b[0], b[1] + 0.06 * math.sin(f / N * math.pi), b[2]); o.keyframe_insert('location', frame=f)
# host mouth (stepped). Mouth scale = (w*1.25, 1, h*1.25); cavity = (.05*c, .022, .016*c); teeth = (.06*t, .01, .008*t); closed = cavity/teeth collapsed
ms = [D['H_Mouth'], D['H_MouthCav'], D['H_Teeth']]
for f in range(N):
    if f and A['mouth'][f] == A['mouth'][f - 1]: continue
    w, h, c, t = SH[A['mouth'][f]]
    ms[0].scale = (w * 1.25, 1, h * 1.25); ms[1].scale = (.05 * c, .022, .016 * c); ms[2].scale = (.06 * t, .01, .008 * t)
    for o in ms: o.keyframe_insert('scale', frame=f)
for o in ms:
    for fc in o.animation_data.action.layers[0].strips[0].channelbags[0].fcurves:
        for kp in fc.keyframe_points: kp.interpolation = 'CONSTANT'
# coin Baba: rests yawed toward the host (-0.57), turns to camera (-0.39) while speaking, full spins on every 4th line, tip at the end
b = D['Baba']; bl = (0.2, -0.04, 1.06); bs = 1.25
who_at = ['-'] * N
for s_ in segs:
    for f in range(fr(s_['start']), min(N, fr(s_['start'] + s_['dur']) + 1)): who_at[f] = s_['who']
spin_f = sorted(fr(s_['start']) for s_ in segs if s_['who'] == 'b' and s_['i'] % 4 == 3)
last = fr(segs[-1]['start'] + segs[-1]['dur'])
for f in range(N):
    e = A['env'][f]; yaw = -0.39 if who_at[f] == 'b' else -0.57
    for sf0 in spin_f:
        if f - sf0 >= 8: yaw += math.tau
        elif f >= sf0: yaw += (f - sf0) / 8 * math.tau
    tip = -min(0.22, max(0, f - last) / 10 * 0.22)
    b.location = (bl[0], bl[1], bl[2] + 0.012 * e); b.rotation_euler = (tip, 0, yaw)
    sc = bs * (1 + 0.04 * e); b.scale = (sc, sc, sc)
    for p in ('location', 'rotation_euler', 'scale'): b.keyframe_insert(p, frame=f)
# host head: faces the coin (z 0.12) with a small nod while speaking; drops forward at the end
hh = D['H_HeadRig']
for f in range(N):
    nod = 0.015 * math.sin(f * 0.9) if who_at[f] == 'h' else 0.0
    k = max(0.0, min(1.0, (f - (last + 4)) / 8))
    hh.rotation_euler = (nod + 0.34 * k, 0, 0.12 * (1 - k)); hh.keyframe_insert('rotation_euler', frame=f)
S.camera = D['CAM_Wide']
def clay_render(out):
    r = S.render; im = r.image_settings
    im.media_type = 'VIDEO'; im.file_format = 'FFMPEG'; r.resolution_x = 1080; r.resolution_y = 1920; r.resolution_percentage = 100
    r.ffmpeg.format = 'MPEG4'; r.ffmpeg.codec = 'H264'; r.ffmpeg.constant_rate_factor = 'HIGH'
    r.filepath = out; S.frame_start = 0; S.frame_end = N - 1
    bpy.ops.render.render('INVOKE_DEFAULT', animation=True)
print('clay_apply ok', N, 'frames,', len(cuts), 'cuts')
