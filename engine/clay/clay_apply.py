"""Run inside Blender (execute_blender_code):  ANIM='/path/anim.json'; WALL_JOKE='WORKS ON MY MACHINE'; exec(open('/path/clay_apply.py').read())
Keys the clay set from anim.json: camera cuts, host lip-sync, coin (Baba) motion, host nod, ending head drop. Then call clay_render(out_path)."""
import bpy, json, math, random
from mathutils import Vector
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
# ---- camera angle library (tested on the set, 28 Nov 2026) -------------------------------------------------
# Veer's rule: never the same angle every episode. Each episode picks a different mix, seeded by ANGLE_SEED
# (set ANGLE_SEED=<int> before exec to force a plan; default is derived from the episode).
HEAD = Vector((-0.3, 0.55, 1.247)); COIN = Vector((0.2, -0.04, 1.06)); MIDP = Vector((-0.05, 0.3, 1.15))
ANG = {  # name: (location, look-at target, lens mm, roll rad)
    'ANG_W_DUTCH': ((-0.1, -2.2, 1.2), MIDP, 38, 0.17),                  # wide, tilted: punchlines and chaos
    'ANG_W_HIGH':  ((-0.1, -1.9, 2.3), Vector((-0.05, 0.3, 0.9)), 36, 0),  # wide from above: host looks small
    'ANG_W_L':     ((-1.3, -1.9, 1.4), Vector((0, 0.2, 1.1)), 36, 0),
    'ANG_W_R':     ((1.3, -1.9, 1.4), Vector((0, 0.2, 1.1)), 36, 0),
    'ANG_H_HIGH':  ((-0.05, -0.95, 2.15), HEAD, 40, 0),                  # looking down on the host
    'ANG_H_3Q_L':  ((-1.15, -1.0, 1.5), HEAD, 45, 0),
    'ANG_H_3Q_R':  ((0.75, -1.0, 1.5), HEAD, 45, 0),                     # coin in the foreground
    'ANG_H_LOW':   ((0.55, -1.0, 0.9), HEAD, 40, 0),                     # hero angle looking up, wall text behind
    'ANG_H_MOUTH': ((-0.3, -1.0, 1.2), HEAD + Vector((0, 0, -0.015)), 85, 0),  # extreme close-up on the mouth
    'ANG_B_LOW':   ((0.15, -0.55, 0.82), COIN, 40, 0),                   # coin as a hero
    'ANG_B_HIGH':  ((0.25, -0.7, 1.8), COIN, 40, 0),
    'ANG_B_3Q':    ((0.6, -0.9, 1.15), COIN, 50, 0),
    'ANG_B_DUTCH': ((0.2, -0.85, 1.1), COIN, 45, -0.2),
}
for o in [o for o in D if o.name.startswith(('ANG_', 'T_', 'U_')) and o.type == 'CAMERA']:
    cd = o.data; bpy.data.objects.remove(o, do_unlink=True); bpy.data.cameras.remove(cd)
for n, (loc, tgt, lens, roll) in ANG.items():
    cd = bpy.data.cameras.new(n); cd.lens = lens; cd.sensor_width = 36
    o = bpy.data.objects.new(n, cd); S.collection.objects.link(o)
    o.location = Vector(loc); d = (Vector(tgt) - Vector(loc))
    o.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    if roll: o.rotation_euler.rotate_axis('Z', roll)
    o['base_loc'] = list(o.location); o['dir'] = list(d.normalized())
FAM = {'wide': ['CAM_Wide', 'ANG_W_DUTCH', 'ANG_W_HIGH', 'ANG_W_L', 'ANG_W_R'],
       'h': ['CAM_Host', 'ANG_H_HIGH', 'ANG_H_3Q_L', 'ANG_H_3Q_R', 'ANG_H_LOW', 'ANG_H_MOUTH'],
       'b': ['CAM_Baba', 'ANG_B_LOW', 'ANG_B_HIGH', 'ANG_B_3Q', 'ANG_B_DUTCH']}
OPEN = ['CAM_Wide', 'ANG_W_DUTCH', 'ANG_W_R']          # frame 0 must show the wall text
PUNCH = {'h': ['ANG_H_HIGH', 'ANG_H_MOUTH', 'ANG_H_LOW'], 'b': ['ANG_B_LOW', 'ANG_B_DUTCH', 'ANG_B_HIGH']}
ENDW = ['CAM_Wide', 'ANG_W_HIGH', 'ANG_W_DUTCH']       # last shot shows the head drop
# camera cuts: varied opener, angle by speaker, a wide at the middle line, a punch angle on the last line, varied end shot
def fr(t): return int(round(t * FPS))
rng = random.Random(ANGLE_SEED if 'ANGLE_SEED' in globals() else N * 31 + len(segs) * 7 + sum(s['i'] * ord(s['who']) for s in segs))
used = {}; last_by = {}; prev = [None]
def pick(pool, key):
    ex = (prev[0], last_by.get(key))
    opts = [c for c in pool if c not in ex] or [c for c in pool if c != prev[0]] or pool
    fresh = [c for c in opts if not used.get(c)]
    c = rng.choice(fresh or opts); used[c] = used.get(c, 0) + 1; prev[0] = c; last_by[key] = c
    return c
mid = len(segs) // 2
cuts = [(0, pick(OPEN, 'wide'))]
for s in segs:
    if s['i'] == 0: continue
    who = s['who']
    if s['i'] == len(segs) - 1: pool, key = PUNCH[who], who
    elif s['i'] == mid: pool, key = FAM['wide'], 'wide'
    else: pool, key = FAM[who], who
    cuts.append((fr(s['start']) - 2, pick(pool, key)))
    if s['dur'] > 2.4 and s['i'] != len(segs) - 1:     # long line: change angle mid-line for energy
        cuts.append((fr(s['start'] + s['dur'] * 0.55), pick(FAM[who], who)))
cuts.append((fr(segs[-1]['start'] + segs[-1]['dur']) + 6, pick(ENDW, 'end')))
for k, (f, c) in enumerate(cuts):
    mk = S.timeline_markers.new(f'cut{k:02d}', frame=f); mk.camera = D[c]
# slow push-in on each camera (original three: location y; angle cameras: dolly along the view direction)
for n in ('CAM_Baba', 'CAM_Host', 'CAM_Wide'):
    o = D[n]; b = o['base_loc']
    for f in range(0, N, 15):
        o.location = (b[0], b[1] + 0.06 * math.sin(f / N * math.pi), b[2]); o.keyframe_insert('location', frame=f)
for n in ANG:
    o = D[n]; b = Vector(o['base_loc']); dv = Vector(o['dir'])
    for f in range(0, N, 15):
        o.location = b + dv * 0.07 * math.sin(f / N * math.pi); o.keyframe_insert('location', frame=f)
print('camera plan:', ' '.join(f'{f}:{c.replace("ANG_", "")}' for f, c in cuts))
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
