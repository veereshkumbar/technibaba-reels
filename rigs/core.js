// TechniBaba rig core. Pure functions of the frame number: deterministic, renderer-agnostic.
// Usage:  const baba = makeRig('baba');  baba.pose('point', 44, {big:true});  baba.express('smug', 60);
//         baba.say('AI', 45);  ...  svg += baba.draw(frame, {x, y, s, flip});
const RIG = (() => {
  const T = (typeof TOKENS !== 'undefined') ? TOKENS : {fps: 30, motion: {anticipationFrames: [4, 8], anticipationAmount: .16, overlapLagFrames: 3, settleFrames: 14, squash: .07}};
  const M = T.motion, clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x)), lerp = (a, b, f) => a + (b - a) * f, R = d => d * Math.PI / 180;
  // ---- eases (tokens.ease.*) ----
  const ease = {
    snappy: x => x >= 1 ? 1 : 1 - Math.pow(2, -10 * clamp(x)),                       // easeOutExpo
    smooth: x => { x = clamp(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }, // easeInOutCubic
    bouncy: x => { x = clamp(x); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); } // easeOutBack
  };
  // ---- pose library: joint angles in degrees, [upperArm, forearm] per side; lean = body lean; hop = lift ----
  const POSES = {
    idle:    {L: [10, 6],    R: [10, 6],    lean: 0,  hop: 0},
    talk:    {L: [14, 10],   R: [55, 100],  lean: 2,  hop: 0},
    explain: {L: [40, 110],  R: [50, 115],  lean: 3,  hop: 0},
    point:   {L: [14, 10],   R: [92, 90],   lean: 6,  hop: 0},
    count:   {L: [14, 10],   R: [30, 172],  lean: 2,  hop: 0},
    shrug:   {L: [55, -60],  R: [55, -60],  lean: 0,  hop: 0},
    up:      {L: [160, 165], R: [160, 165], lean: 0,  hop: 26},
    blown:   {L: [120, 150], R: [120, 150], lean: -7, hop: 0},
    palm:    {L: [14, 10],   R: [20, 175],  lean: -2, hop: 0},
    thumb:   {L: [14, 10],   R: [60, 170],  lean: 3,  hop: 0},
    wave:    {L: [14, 10],   R: [150, 195], lean: 2,  hop: 0},
    cross:   {L: [-25, -105], R: [-25, -105], lean: -3, hop: 0},
    stop:    {L: [14, 10],   R: [80, 150],  lean: -3, hop: 0},
    phone:   {L: [35, 150],  R: [10, 6],    lean: 4,  hop: 0},
    leanin:  {L: [14, 10],   R: [30, 60],   lean: 11, hop: 0}
  };
  // ---- expression presets: eyes, brows, resting mouth, head tilt ----
  const EXPR = {
    neutral:    {eye: 'open',   brow: [0, 0, 0],      mouth: 'smile', tilt: 0,  look: .6},
    happy:      {eye: 'arc',    brow: [-6, 0, -4],    mouth: 'grin',  tilt: -3, look: .6},
    shocked:    {eye: 'wide',   brow: [0, 0, -16],    mouth: 'o',     tilt: 2,  look: .2},
    smug:       {eye: 'lid',    brow: [-10, 12, -2],  mouth: 'smirk', tilt: -5, look: 1},
    confused:   {eye: 'open',   brow: [14, -10, -4],  mouth: 'wavy',  tilt: 7,  look: -.2},
    angry:      {eye: 'lid',    brow: [16, 16, 6],    mouth: 'flat',  tilt: 0,  look: .8},
    explaining: {eye: 'open',   brow: [-6, -6, -6],   mouth: 'smile', tilt: -2, look: .8},
    sideeye:    {eye: 'side',   brow: [8, -6, 0],     mouth: 'flat',  tilt: 3,  look: 1}
  };
  const VISEMES = ['rest', 'AI', 'E', 'O', 'U', 'MBP', 'FV', 'L'];
  // letters -> viseme (Roman Hinglish). Returns one viseme per letter group.
  function wordVisemes(w) {
    const out = []; w = w.toLowerCase().replace(/[^a-z]/g, '');
    for (let i = 0; i < w.length; i++) {
      const c = w[i], n = w[i + 1] || '';
      let v = null;
      if ('ai'.includes(c)) v = 'AI'; else if (c == 'e') v = 'E'; else if (c == 'o') v = 'O'; else if (c == 'u') v = 'U';
      else if ('mbp'.includes(c)) v = 'MBP'; else if ('fv'.includes(c)) v = 'FV';
      else if ('ltdn'.includes(c)) v = 'L'; else if (c == 'w') v = 'U'; else if (c == 'y') v = 'E'; else v = 'E';
      if (c == 'a' && n == 'a') i++; if (c == 'e' && n == 'e') i++; if (c == 'o' && n == 'o') { v = 'U'; i++; }
      if (out[out.length - 1] !== v) out.push(v);
    }
    return out.length ? out : ['E'];
  }
  // ---- keyframe channel with anticipation + eased landing ----
  function channel() { return []; }
  function keyAt(ch, f) { let k = -1; for (let i = 0; i < ch.length; i++) if (ch[i].f - (ch[i].ant || 0) <= f) k = i; return k; }
  // progress of key i at frame f: negative during anticipation, then 0..1 (may overshoot with bouncy)
  function prog(k, f) {
    const ant = k.ant || 0, d = k.dur || 10;
    if (f < k.f) { const u = clamp((f - (k.f - ant)) / Math.max(1, ant)); return -M.anticipationAmount * Math.sin(u * Math.PI / 2); }
    const u = clamp((f - k.f) / d), e = ease[k.ease || 'snappy'](u);
    return -M.anticipationAmount * (1 - clamp(u * 3)) * (ant ? 1 : 0) * (1 - e) + e;
  }
  // decaying wobble after a key lands: follow-through for secondary parts
  function wobble(ch, f, gain = 1) { let w = 0; for (const k of ch) { const d = f - k.f; if (d >= 0 && d < 40) w += (k.amp || 1) * Math.exp(-d / (M.settleFrames / 2.6)) * Math.sin(d * .75) * gain; } return w; }

  function makeRig(kind) {
    const pose = channel(), expr = channel(), mouth = [], look = channel();
    const api = {
      kind, poseCh: pose, exprCh: expr, mouthTrack: mouth,
      // pose(name, frame, {big, dur, ease}) — big moves get anticipation + follow-through
      pose(name, f, o = {}) { pose.push({f, v: name, big: !!o.big, ant: o.big ? (o.ant || 6) : 0, dur: o.dur || (o.big ? 9 : 12), ease: o.ease || (o.big ? 'bouncy' : 'smooth'), amp: o.big ? 1 : .35}); pose.sort((a, b) => a.f - b.f); return api; },
      express(name, f, o = {}) { expr.push({f, v: name, big: !!o.big, ant: o.big ? 4 : 0, dur: o.dur || 6, ease: 'snappy', amp: o.big ? 1 : .4}); expr.sort((a, b) => a.f - b.f); return api; },
      say(viseme, f) { mouth[Math.round(f)] = viseme; return api; },
      sayTrack(arr, f0 = 0) { arr.forEach((v, i) => { mouth[f0 + i] = v; }); return api; },
      // ---- evaluated state at frame f ----
      state(f) {
        const pi = keyAt(pose, f), pk = pi >= 0 ? pose[pi] : {v: 'idle', f: -99}, pp = pi > 0 ? pose[pi - 1].v : 'idle';
        const a = POSES[pp] || POSES.idle, b = POSES[pk.v] || POSES.idle, p = pi >= 0 ? prog(pk, f) : 1;
        const mix = (x, y) => x + (y - x) * p;
        const sec = f / T.fps, talkWag = (pk.v == 'talk' || pk.v == 'explain') ? 1 : 0, waveWag = pk.v == 'wave' ? 1 : 0;
        const arms = {
          L: [mix(a.L[0], b.L[0]) + 2 * Math.sin(sec * 1.7), mix(a.L[1], b.L[1]) + talkWag * (pk.v == 'explain' ? 14 * Math.sin(sec * 6.2) : 0)],
          R: [mix(a.R[0], b.R[0]) + talkWag * 9 * Math.sin(sec * 5.4) - 2 * Math.sin(sec * 1.7), mix(a.R[1], b.R[1]) + talkWag * 18 * Math.sin(sec * 7.3) + waveWag * 24 * Math.sin(sec * 11)]
        };
        // hands settle after the arm (follow-through)
        const handLag = wobble(pose, f, 7);
        const ei = keyAt(expr, f), ek = ei >= 0 ? expr[ei] : {v: 'neutral', f: -99}, ep = ei > 0 ? expr[ei - 1].v : 'neutral';
        const ea = EXPR[ep] || EXPR.neutral, eb = EXPR[ek.v] || EXPR.neutral, q = ei >= 0 ? clamp(prog(ek, f), -.3, 1.2) : 1;
        const tiltBase = lerp(ea.tilt, eb.tilt, q), lean = mix(a.lean, b.lean), hop = mix(a.hop, b.hop) * (pk.v == 'up' ? .55 + .45 * Math.abs(Math.sin(sec * 8)) : 1);
        const speaking = mouth[Math.round(f)] && mouth[Math.round(f)] != 'rest';
        const nod = speaking ? 2.2 * Math.sin(sec * 5.1) : .8 * Math.sin(sec * .9 + (kind == 'baba' ? 1 : 0));
        const headTilt = tiltBase + nod + wobble(expr, f, 2.2) + lean * .25;
        // overlap: secondary parts lag the head
        const lagF = f - M.overlapLagFrames, prevTilt = (() => { const i2 = keyAt(expr, lagF), k2 = i2 >= 0 ? expr[i2] : {v: 'neutral', f: -99}, p2 = i2 > 0 ? expr[i2 - 1].v : 'neutral'; const q2 = i2 >= 0 ? clamp(prog(k2, lagF), -.3, 1.2) : 1; return lerp((EXPR[p2] || EXPR.neutral).tilt, (EXPR[k2.v] || EXPR.neutral).tilt, q2); })();
        const drag = (prevTilt - tiltBase) * 1.1 + wobble(expr, f - 2, 5) + wobble(pose, f - 2, 3.5);
        // squash & stretch on big reactions and landings
        let sq = 0; for (const k of expr.concat(pose)) { if (!k.big) continue; const d = f - k.f; if (d >= 0 && d < 16) sq += M.squash * Math.exp(-d / 3.5) * Math.cos(d * .9); if (d < 0 && d >= -(k.ant || 0)) sq -= M.squash * .7 * Math.sin((d + k.ant) / k.ant * Math.PI / 2); }
        const blink = (((f + (kind == 'baba' ? 37 : 0)) % 97) < 3) || (((f + (kind == 'baba' ? 11 : 60)) % 211) < 3);
        return {arms, handLag, lean, hop, headTilt, drag, sq, blink, pose: pk.v, expr: q > .5 ? eb : ea, exprName: q > .5 ? ek.v : ep,
          brow: [0, 1, 2].map(i => lerp(ea.brow[i], eb.brow[i], clamp(q, 0, 1.15))), look: lerp(ea.look, eb.look, clamp(q)),
          viseme: mouth[Math.round(f)] || 'rest', breath: 1 + .012 * Math.sin(sec * 2.1 + (kind == 'baba' ? 1 : 0)), f};
      }
    };
    return api;
  }
  // ---- stage helpers ----
  // hit-stop: freeze the picture `hold` frames at frame h, then catch up over tokens.motion.catchUpFrames
  function timeWarp(hits) { const cu = M.catchUpFrames || 6; return f => { for (const [h, hold] of hits) { if (f >= h && f < h + hold) return h; if (f >= h + hold && f < h + hold + cu) { const u = (f - h - hold) / cu; return h + (hold + cu) * ease.smooth(u) * 1 + 0 * u; } } return f; }; }
  // impact frame overlay (burst lines + bright frame) for the first 2 frames of a hit
  function impact(f, hits, cx, cy) { for (const [h, hold] of hits) { const d = f - h; if (d >= 0 && d < hold) { let o = d < 1 ? `<rect width="1080" height="1920" fill="#fff" opacity=".55"/>` : ''; for (let k = 0; k < 14; k++) { const a = k / 14 * 2 * Math.PI + .2, r0 = 250 + (k % 3) * 40, r1 = r0 + 260 + (k % 2) * 120; o += `<path d="M${cx + Math.cos(a) * r0},${cy + Math.sin(a) * r0} L${cx + Math.cos(a) * r1},${cy + Math.sin(a) * r1}" stroke="#fff" stroke-width="${10 + (k % 3) * 6}" stroke-linecap="round" opacity="${.9 - d * .12}"/>`; } return o; } } return ''; }
  // gravity arc for props: from p0 to p1 over [f0,f1], apex lift h
  function arc(f, f0, f1, p0, p1, h = 160) { const u = clamp((f - f0) / (f1 - f0)), e = ease.smooth(u); return [lerp(p0[0], p1[0], e), lerp(p0[1], p1[1], e) - h * 4 * e * (1 - e)]; }
  return {makeRig, ease, POSES, EXPR, VISEMES, wordVisemes, timeWarp, impact, arc, clamp, lerp, R};
})();
