// ---------- S1E4: Zombie Outbreak — 30 Days Trapped In A Flooded Subway ----------
// Carries over all S1E2 locations (tower, river, Nora, cards) + new S1E3 harbor/ferry/raft/rope locations at the end.

// ===== NORA: radio engineer, yellow raincoat, glasses, dark bob =====
const _torsoN = torso, _hatN = hat;
torso = function (kind, v, ps) { if (kind === 'nora') { const n = ps.neck, h = ps.hip;
    return P(`M${n[0] - 30} ${n[1] + 4} L${n[0] + 30} ${n[1] + 4} L${h[0] + 34} ${h[1] + 30} L${h[0] - 34} ${h[1] + 30}Z`, '#e8b62a', 5) +
      `<path d="M${n[0]} ${n[1] + 8} L${h[0]} ${h[1] + 26}" stroke="#b88a14" stroke-width="4"/>` + [0, 1, 2].map(k => `<circle cx="${n[0] + 7}" cy="${n[1] + 22 + k * ((h[1] - n[1]) / 3)}" r="4" fill="#5a4410"/>`).join('') +
      `<path d="M${n[0] - 30} ${n[1] + 2} Q${n[0]} ${n[1] - 18} ${n[0] + 30} ${n[1] + 2}" stroke="#d4a020" stroke-width="12" fill="none"/>`; }
  return _torsoN(kind, v, ps); };
hat = function (kind, v, e) { if (kind === 'nora') {
    const hair = `<path d="M-56 24 Q-62 -70 0 -70 Q62 -70 56 24 Q50 -10 40 -34 Q0 -50 -40 -34 Q-50 -10 -56 24Z" fill="#2a1c16" stroke="${INK}" stroke-width="5"/><path d="M-44 -40 Q-10 -26 30 -48" stroke="#2a1c16" stroke-width="14" fill="none"/>`;
    const gl = e === 'back' ? '' : `<circle cx="-13" cy="-8" r="14" fill="#cfe6ff" fill-opacity=".18" stroke="${INK}" stroke-width="4"/><circle cx="15" cy="-8" r="14" fill="#cfe6ff" fill-opacity=".18" stroke="${INK}" stroke-width="4"/><path d="M1 -8h0" stroke="${INK}" stroke-width="4"/><path d="M-27 -10 l-18 -4 M29 -10 l18 -4" stroke="${INK}" stroke-width="3"/>`;
    return hair + gl; }
  return _hatN(kind, v, e); };

// ===== drawing helpers =====
const isNw = L => L === 'brnight' || L === 'bred';
function wsky(L) { return brSky(L); }
function brokenBridge(y, sc, L) { const n = isNw(L), c = n ? '#3a3e46' : '#8a8f96'; let s = '';
  for (const x of [520, 1400]) s += `<rect x="${x - 26 * sc}" y="${y - 260 * sc}" width="${52 * sc}" height="${300 * sc}" fill="${c}" stroke="${INK}" stroke-width="4"/>`;
  s += `<path d="M-40 ${y - 20 * sc} L${720} ${y - 20 * sc} L${760} ${y + 30 * sc}" stroke="${c}" stroke-width="${18 * sc}" fill="none"/><path d="M1960 ${y - 20 * sc} L${1220} ${y - 20 * sc} L${1170} ${y + 40 * sc}" stroke="${c}" stroke-width="${18 * sc}" fill="none"/>`;
  s += `<path d="M-40 ${y - 20 * sc} L720 ${y - 20 * sc} M1960 ${y - 20 * sc} L1220 ${y - 20 * sc}" stroke="${INK}" stroke-width="3"/>`;
  for (let k = 0; k < 3; k++) s += `<path d="M${800 + k * 130} ${y + 20} q-30 -${120 + k * 40} 30 -${220 + k * 50}" stroke="${n ? '#1a1a22' : '#5a5458'}" stroke-width="${40 + k * 10}" fill="none" opacity=".45" stroke-linecap="round"/>`;
  return s; }
function roofs(y0, y1, L, seed) { const n = isNw(L); let s = `<rect y="${y0}" width="1920" height="${y1 - y0}" fill="${n ? '#10141c' : '#5a6270'}"/>`;
  for (let i = 0; i < 30; i++) { const x = rnd(seed + i) * 1920, w = 80 + rnd(seed + i + 9) * 140, yy = y0 + rnd(seed + i + 20) * (y1 - y0 - 40);
    s += `<rect x="${x}" y="${yy}" width="${w}" height="${40 + rnd(i + seed) * 60}" fill="${n ? '#1a1e28' : '#7a808c'}" stroke="${INK}" stroke-width="3"/>`;
    if (n && rnd(seed * 7 + i) > .8) s += `<rect x="${x + 10}" y="${yy + 10}" width="14" height="10" fill="#d8a04a" opacity=".6"/>`; }
  return s; }
function bigTower(cx, base, top, sc, L) { // full water tower, ladder on front-left leg
  const n = isNw(L), leg = n ? '#2a2e36' : '#7a7e84', tank = n ? '#3a3e46' : '#a8a29a'; const w = 300 * sc; let s = '';
  for (const dx of [-1, 1]) s += `<path d="M${cx + dx * w * .55} ${base} L${cx + dx * w * .38} ${top}" stroke="${leg}" stroke-width="${22 * sc}"/><path d="M${cx + dx * w * .55} ${base} L${cx + dx * w * .38} ${top}" stroke="${INK}" stroke-width="3" fill="none"/>`;
  for (let k = 0; k < 4; k++) { const y = base - (base - top) * (k + .5) / 4.2; const hw = w * (.55 - .17 * (k + .5) / 4.2); s += `<path d="M${cx - hw} ${y} L${cx + hw} ${y - 60 * sc} M${cx + hw} ${y} L${cx - hw} ${y - 60 * sc}" stroke="${leg}" stroke-width="${8 * sc}"/>`; }
  // ladder on left leg
  const lx = cx - w * .2; s += `<path d="M${lx - 16 * sc} ${base} V${top} M${lx + 16 * sc} ${base} V${top}" stroke="${n ? '#5a5e66' : '#4a4e56'}" stroke-width="${5 * sc}"/>`;
  for (let y = base - 10; y > top; y -= 18 * sc) s += `<path d="M${lx - 16 * sc} ${y} h${32 * sc}" stroke="${n ? '#5a5e66' : '#4a4e56'}" stroke-width="${3 * sc}"/>`;
  // catwalk + tank + roof
  s += `<rect x="${cx - w * .62}" y="${top - 14 * sc}" width="${w * 1.24}" height="${14 * sc}" fill="${leg}" stroke="${INK}" stroke-width="4"/>`;
  for (let k = 0; k <= 10; k++) s += `<path d="M${cx - w * .62 + k * w * .124} ${top - 14 * sc} v-${34 * sc}" stroke="${leg}" stroke-width="${4 * sc}"/>`;
  s += `<path d="M${cx - w * .62} ${top - 48 * sc} H${cx + w * .62}" stroke="${leg}" stroke-width="${5 * sc}"/>`;
  s += `<path d="M${cx - w * .5} ${top - 14 * sc} V${top - 240 * sc} Q${cx} ${top - 262 * sc} ${cx + w * .5} ${top - 240 * sc} V${top - 14 * sc}Z" fill="${tank}" stroke="${INK}" stroke-width="7"/>`;
  s += `<path d="M${cx - w * .56} ${top - 236 * sc} L${cx} ${top - 330 * sc} L${cx + w * .56} ${top - 236 * sc}Z" fill="${n ? '#2a2e36' : '#8a847a'}" stroke="${INK}" stroke-width="7"/>`;
  s += `<text x="${cx}" y="${top - 120 * sc}" font-size="${44 * sc}" font-weight="900" fill="${n ? '#5a5e66' : '#6a645a'}" text-anchor="middle" font-family="DejaVu Sans">HARBOR CITY</text>`;
  s += `<rect x="${cx + w * .25}" y="${top - 100 * sc}" width="${60 * sc}" height="${70 * sc}" fill="${n ? '#4a3a2a' : '#8a6a4a'}" stroke="${INK}" stroke-width="4"/>`; // nora's shack door
  return s; }
function fence(y, L) { const n = isNw(L); let s = `<path d="M0 ${y - 110} H1920" stroke="${n ? '#4a4e56' : '#8a8f96'}" stroke-width="6"/><path d="M0 ${y} H1920" stroke="${n ? '#4a4e56' : '#8a8f96'}" stroke-width="6"/>`;
  for (let x = 0; x < 1920; x += 26) s += `<path d="M${x} ${y} l26 -110 M${x + 26} ${y} l-26 -110" stroke="${n ? '#3a3e46' : '#9a9fa6'}" stroke-width="2" opacity=".7"/>`;
  for (let x = 0; x < 1920; x += 240) s += `<path d="M${x} ${y + 4} V${y - 120}" stroke="${n ? '#4a4e56' : '#8a8f96'}" stroke-width="9"/>`;
  return s; }

// ===== ENVIRONMENTS =====
// catwalk on top of the tower, looking out at the river and the broken bridge
ENV.wtop = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 520, .8, 31) + `<rect y="520" width="1920" height="150" fill="${n ? '#0a1220' : '#4a6a80'}"/>` + brokenBridge(560, 1, L);
  s += Array.from({ length: 16 }, (_, i) => `<path d="M${rnd(i + 2) * 1900} ${590 + rnd(i + 5) * 70} h${40 + rnd(i + 3) * 60}" stroke="${n ? '#22324e' : '#8ab0c8'}" stroke-width="3"/>`).join('');
  s += roofs(670, 900, L, 5);
  // tank wall on the left
  s += `<path d="M-40 -40 H560 Q640 400 600 1080 H-40Z" fill="${n ? '#3a3e46' : '#a8a29a'}" stroke="${INK}" stroke-width="8"/>` + Array.from({ length: 9 }, (_, k) => `<path d="M-40 ${60 + k * 110} Q300 ${80 + k * 110} ${560 + k * 6} ${70 + k * 110}" stroke="${INK}" stroke-width="3" opacity=".35" fill="none"/>`).join('') + Array.from({ length: 24 }, (_, k) => `<circle cx="${40 + (k % 6) * 100}" cy="${100 + Math.floor(k / 6) * 220}" r="6" fill="${INK}" opacity=".35"/>`).join('');
  // shack
  s += `<rect x="80" y="560" width="380" height="440" fill="${n ? '#3a2e24' : '#8a6a4a'}" stroke="${INK}" stroke-width="7"/><path d="M60 560 L270 470 L480 560Z" fill="${n ? '#2a2420' : '#6a5038'}" stroke="${INK}" stroke-width="7"/><rect x="290" y="700" width="130" height="300" fill="${n ? '#241c16' : '#5a4430'}" stroke="${INK}" stroke-width="6"/><rect x="120" y="620" width="120" height="90" fill="${n ? '#d8a04a' : '#9ab4c6'}" stroke="${INK}" stroke-width="5" opacity=".9"/>`;
  s += `<path d="M250 480 V380 M230 400 h40 M236 420 h28" stroke="${INK}" stroke-width="5"/>`; // antenna
  // signal lamp on a tripod
  s += `<path d="M640 1000 L680 860 L720 1000 M680 860 V840" stroke="${INK}" stroke-width="6"/><rect x="640" y="800" width="90" height="56" rx="12" fill="#5a5e52" stroke="${INK}" stroke-width="5"/><circle cx="728" cy="828" r="22" fill="#e9e2cc" stroke="${INK}" stroke-width="5"/><rect x="730" y="950" width="80" height="50" fill="#2a2c32" stroke="${INK}" stroke-width="4"/>`;
  // catwalk floor + far railing
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#2a2c32' : '#6a6e74'}" stroke="${INK}" stroke-width="6"/>` + Array.from({ length: 30 }, (_, k) => `<path d="M${k * 70} 1000 v80" stroke="${INK}" stroke-width="3" opacity=".4"/>`).join('');
  s += `<path d="M600 860 H1920 M600 930 H1920" stroke="${n ? '#5a5e66' : '#8a8f96'}" stroke-width="10"/>` + Array.from({ length: 12 }, (_, k) => `<path d="M${640 + k * 120} 860 V1000" stroke="${n ? '#5a5e66' : '#8a8f96'}" stroke-width="9"/>`).join('');
  return s; };
// the tower from street level, fenced lot
ENV.wwide = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 760, .9, 44, 0);
  s += `<rect x="0" y="560" width="330" height="440" fill="${n ? '#1a1e26' : '#7a808a'}" stroke="${INK}" stroke-width="6"/><rect x="1600" y="520" width="320" height="480" fill="${n ? '#1a1e26' : '#7a808a'}" stroke="${INK}" stroke-width="6"/>`;
  for (let k = 0; k < 8; k++) s += `<rect x="${30 + (k % 3) * 100}" y="${600 + Math.floor(k / 3) * 120}" width="60" height="70" fill="${n ? '#0e1016' : '#9ab4c6'}" stroke="${INK}" stroke-width="3"/><rect x="${1640 + (k % 3) * 95}" y="${570 + Math.floor(k / 3) * 120}" width="60" height="70" fill="${n ? '#0e1016' : '#9ab4c6'}" stroke="${INK}" stroke-width="3"/>`;
  s += bigTower(960, 1000, 420, 1.25, L);
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#1c1e22' : '#5a5c60'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>` + fence(1000, L);
  return s; };
// side view on the ladder, mid-height, city below
ENV.wladder = L => { const n = isNw(L); let s = wsky(L) + roofs(640, 1080, L, 12) + skyline(L, 640, .7, 18, 0);
  s += `<rect x="1180" y="-40" width="110" height="1160" fill="${n ? '#2a2e36' : '#7a7e84'}" stroke="${INK}" stroke-width="7"/>` + Array.from({ length: 10 }, (_, k) => `<circle cx="1235" cy="${40 + k * 110}" r="7" fill="${INK}" opacity=".5"/>`).join('');
  s += `<path d="M1290 200 L1920 40 M1290 760 L1920 600" stroke="${n ? '#2a2e36' : '#7a7e84'}" stroke-width="22"/>`;
  s += `<path d="M880 -40 V1120 M1040 -40 V1120" stroke="${n ? '#6a6e76' : '#4a4e56'}" stroke-width="16"/><path d="M880 -40 V1120 M1040 -40 V1120" stroke="${INK}" stroke-width="3"/>`;
  for (let y = 20; y < 1080; y += 90) s += `<rect x="880" y="${y}" width="160" height="12" fill="${n ? '#6a6e76' : '#4a4e56'}" stroke="${INK}" stroke-width="3"/><path d="M1040 ${y + 6} H1180" stroke="${n ? '#4a4e56' : '#5a5e66'}" stroke-width="6"/>`;
  return s; };
// looking straight down the ladder (vertigo)
ENV.wdown = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#0a0c12' : '#5a5c60'}"/>`;
  s += `<ellipse cx="960" cy="900" rx="520" ry="150" fill="${n ? '#14161c' : '#6a6c70'}"/>` + crowd(560, 1360, 840, .5, 70, 51, L);
  s += `<path d="M560 -40 L900 880 M1360 -40 L1020 880" stroke="${n ? '#6a6e76' : '#4a4e56'}" stroke-width="26"/><path d="M560 -40 L900 880 M1360 -40 L1020 880" stroke="${INK}" stroke-width="4"/>`;
  for (let k = 0; k < 22; k++) { const u = Math.pow(k / 22, .55), y = -40 + u * 920, x0 = 560 + u * 340, x1 = 1360 - u * 340; s += `<path d="M${x0} ${y} H${x1}" stroke="${n ? '#6a6e76' : '#4a4e56'}" stroke-width="${22 - u * 18}"/>`; }
  s += `<path d="M0 0 L520 -40 L860 900 L0 1080Z M1920 0 L1400 -40 L1060 900 L1920 1080Z" fill="${n ? '#1a1c22' : '#6a6e74'}" opacity=".35"/>`;
  return s; };
// Nora's radio shack (inside)
ENV.wroom = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#3a2e26' : '#7a6248'}"/>` + Array.from({ length: 16 }, (_, k) => `<path d="M${k * 130} 0 V880" stroke="${n ? '#2e241e' : '#6a5440'}" stroke-width="8"/>`).join('');
  s += `<rect x="1300" y="160" width="420" height="300" fill="${n ? '#0a1224' : '#9ab4c6'}" stroke="${INK}" stroke-width="10"/><path d="M1510 160 V460 M1300 310 H1720" stroke="${INK}" stroke-width="8"/>` + (n ? Array.from({ length: 14 }, (_, i) => `<circle cx="${1310 + rnd(i + 7) * 400}" cy="${170 + rnd(i + 70) * 280}" r="2" fill="#fff" opacity=".6"/>`).join('') : '');
  // wall map
  s += `<rect x="160" y="140" width="520" height="360" fill="#e9e2cc" stroke="${INK}" stroke-width="6"/><path d="M160 300 Q420 270 680 320 V380 Q420 330 160 360Z" fill="#7ab0d8" stroke="${INK}" stroke-width="3"/><circle cx="560" cy="250" r="16" fill="#c33a2f"/><path d="M260 300 v60" stroke="#8a8f96" stroke-width="10"/><path d="M620 400 l30 -10 l10 20 l-40 6Z" fill="#c33a2f"/>` + T(420, 470, 28, 'WEST BANK', '#222', 900);
  // desk + radio
  s += `<rect x="120" y="720" width="1100" height="40" fill="${n ? '#4a3a2a' : '#8a6a4a'}" stroke="${INK}" stroke-width="7"/><path d="M160 760 V1000 M1180 760 V1000" stroke="${INK}" stroke-width="12"/>`;
  s += `<rect x="200" y="560" width="420" height="160" rx="10" fill="#3a3e36" stroke="${INK}" stroke-width="6"/>` + [0, 1, 2].map(k => C(260 + k * 80, 650, 22, '#1d1d21', 4)).join('') + `<rect x="470" y="590" width="120" height="50" fill="#7dffb0" opacity=".7" stroke="${INK}" stroke-width="4"/><path d="M600 560 V420" stroke="${INK}" stroke-width="5"/>`;
  s += `<rect x="680" y="660" width="220" height="60" fill="#e9e2cc" stroke="${INK}" stroke-width="5" transform="rotate(-4 790 690)"/><path d="M700 680 h160 M700 696 h140" stroke="#6a6a6a" stroke-width="3" transform="rotate(-4 790 690)"/>`; // log book
  s += `<rect x="960" y="620" width="70" height="100" rx="8" fill="#c9a03a" stroke="${INK}" stroke-width="5"/><circle cx="995" cy="650" r="18" fill="#fff4c0" opacity="${n ? .9 : .5}"/>`; // lantern
  if (n) s += `<circle cx="995" cy="650" r="260" fill="#ffcf7a" opacity=".12"/>`;
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#2a2018' : '#5a4430'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="7"/>`;
  return s; };
// night river after the jump
ENV.river = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 600, .9, 61) + brokenBridge(600, 1, L);
  for (let k = 0; k < 4; k++) s += `<circle cx="${700 + k * 160}" cy="${600}" r="${50 + k * 20}" fill="#ff7a2a" opacity=".25"/>`;
  s += `<rect y="600" width="1920" height="480" fill="${n ? '#06101c' : '#3e6078'}"/>` + Array.from({ length: 60 }, (_, i) => `<path d="M${rnd(i + 4) * 1900} ${620 + rnd(i + 40) * 460} q40 -8 80 0" stroke="${n ? '#1a2a44' : '#8ab0c8'}" stroke-width="4" fill="none" opacity=".7"/>`).join('');
  s += `<path d="M300 700 l120 -20 l30 30 l-140 10Z M1500 760 l160 -10 l10 40 l-170 0Z" fill="#3a3e46" stroke="${INK}" stroke-width="4"/>`;
  return s; };
// muddy west bank at dawn, tower in the distance
ENV.bank = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 560, .8, 71, 0) + `<g transform="translate(1500 560) scale(.55) translate(-960 -1000)">${bigTower(960, 1000, 420, 1, L)}</g>`;
  s += `<rect y="560" width="1920" height="200" fill="${n ? '#0a1220' : '#4a6a80'}"/>` + brokenBridge(600, .6, L).replace(/opacity=".45"/g, 'opacity=".25"');
  s += `<path d="M-20 760 Q600 700 1200 760 T1940 740 V1100 H-20Z" fill="${n ? '#2a2620' : '#6a5a44'}" stroke="${INK}" stroke-width="6"/>`;
  for (let k = 0; k < 40; k++) { const x = rnd(k + 3) * 1920, y = 760 + rnd(k + 9) * 60; s += `<path d="M${x} ${y} q-6 -60 4 -110 M${x + 10} ${y} q8 -50 -2 -90" stroke="${n ? '#3a4030' : '#6a7a4a'}" stroke-width="5" fill="none"/>`; }
  return s; };
// street at the foot of the tower: corner market
ENV.wstreet = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 520, .8, 81, 0);
  s += `<rect x="760" y="300" width="900" height="560" fill="${n ? '#2a2420' : '#9a7a5a'}" stroke="${INK}" stroke-width="7"/><rect x="760" y="300" width="900" height="80" fill="#2f6a4a" stroke="${INK}" stroke-width="6"/>` + T(1210, 356, 50, 'RIVERSIDE MARKET', '#f1ece2', 900);
  s += `<rect x="820" y="440" width="380" height="300" fill="${n ? '#0c0e12' : '#4a5a64'}" stroke="${INK}" stroke-width="6"/><path d="M840 460 l80 90 l-30 40 l120 60 M1100 460 l-60 120 l90 40" stroke="#cfe6ff" stroke-width="4" opacity=".6"/><rect x="1300" y="480" width="160" height="380" fill="${n ? '#14120e' : '#5a4430'}" stroke="${INK}" stroke-width="6"/>`;
  s += `<rect y="860" width="1920" height="220" fill="${n ? '#1c1e22' : '#5a5c60'}"/><path d="M0 860 H1920" stroke="${INK}" stroke-width="6"/>` + Array.from({ length: 8 }, (_, i) => `<rect x="${i * 260}" y="960" width="130" height="12" fill="#d9c96a" opacity=".5"/>`).join('');
  s += `<rect x="120" y="-40" width="90" height="900" fill="${n ? '#2a2e36' : '#7a7e84'}" stroke="${INK}" stroke-width="6"/><path d="M230 -40 V860 M300 -40 V860" stroke="${n ? '#6a6e76' : '#4a4e56'}" stroke-width="10"/>` + Array.from({ length: 12 }, (_, k) => `<path d="M230 ${k * 75} H300" stroke="${n ? '#6a6e76' : '#4a4e56'}" stroke-width="7"/>`).join('');
  s += fence(860, L).replace(/H1920/g, 'H560');
  return s; };

// ===== FX =====
const _fxN = fxSVG;
fxSVG = function (shot, lt, p, t, front) { const f = shot.fx || [], E = shot.env; const has = k => f.includes(k); let s = _fxN(shot, lt, p, t, front);
  if (!front) {
    if (has('nlamp')) { const pos = { wwide: [1080, 160], wtop: [728, 828], bank: [1560, 330] }[E] || [960, 200]; const on = shot.steady || Math.floor(lt * 2.4) % 2 === 0; if (on) s += `<circle cx="${pos[0]}" cy="${pos[1]}" r="${E === 'wtop' ? 140 : 60}" fill="#fff4c0" opacity=".3"/><circle cx="${pos[0]}" cy="${pos[1]}" r="${E === 'wtop' ? 26 : 10}" fill="#fff"/>`; }
    if (has('gather') && (E === 'wwide' || E === 'wstreet')) { const g = shot.gn != null ? shot.gn : .3, k = Math.round(10 + g * 120); s += crowd(E === 'wwide' ? 560 : 160, E === 'wwide' ? 1360 : 640, E === 'wwide' ? 900 : 780, E === 'wwide' ? .9 : 1.1, k, 23, shot.light); }
    if (has('boom') && E === 'brwide') { const q = clamp(lt / 2.5, 0, 1);
      s += `<rect x="560" y="470" width="800" height="${100}" fill="#0a1220"/>`; // middle span gone
      for (let k = 0; k < 7; k++) { const x = 600 + k * 110, dy = q * (300 + k * 40), r = (k % 2 ? -1 : 1) * q * (30 + k * 6); s += `<rect x="${x}" y="${500 + dy}" width="100" height="40" fill="#3a3e46" stroke="${INK}" stroke-width="4" transform="rotate(${r} ${x + 50} ${520 + dy})"/>`; }
      for (const x of [480, 1440]) { const r = 60 + 150 * clamp(lt / .6, 0, 1); s += `<circle cx="${x}" cy="540" r="${r}" fill="#ff7a2a" opacity="${.65 * (1 - q * .8)}"/><circle cx="${x}" cy="560" r="${r * .5}" fill="#ffe08a" opacity="${.8 * (1 - q)}"/>`; }
      s += `<path d="M560 ${900 + Math.sin(t * 3) * 10} q400 -80 800 0" stroke="#e9f2ff" stroke-width="14" fill="none" opacity="${q * .6}"/>`; }
    if (has('gap') && E === 'wladder') { const gy = shot.gy || 380; s += `<svg x="860" y="-40" width="200" height="${gy + 40}" viewBox="860 -40 200 ${gy + 40}" preserveAspectRatio="none">${brSky(shot.light)}</svg><rect x="870" y="${gy - 14}" width="30" height="22" fill="#5a5e66" stroke="${INK}" stroke-width="3"/><rect x="1020" y="${gy - 14}" width="30" height="22" fill="#5a5e66" stroke="${INK}" stroke-width="3"/>`; }
    if (has('torch') && (E === 'river' || E === 'bank' || E === 'wwide')) { const x = { river: 1700, bank: 1560, wwide: 1080 }[E], y = { river: 300, bank: 300, wwide: 120 }[E]; s += `<path d="M${x} ${y} L${x - 500 + Math.sin(t * 2) * 80} ${1080} L${x - 260 + Math.sin(t * 2) * 80} 1080Z" fill="#fff4c0" opacity=".14"/><circle cx="${x}" cy="${y}" r="10" fill="#fff"/>`; }
  }
  if (front) {
    if (E === 'river') { const wl = shot.wlv || 860; let w = `<path d="M-300 ${wl} ` + Array.from({ length: 30 }, (_, k) => `q40 ${(k % 2 ? 1 : -1) * 10} 80 0`).join(' ') + ` V1400 H-300Z" fill="#06101c" opacity=".93" transform="translate(${Math.sin(t * 1.5) * 20} 0)"/>`; s += w + `<path d="M-300 ${wl} H2300" stroke="#2a4a6a" stroke-width="4" opacity=".7"/>`; }
    if (has('vign')) s += `<radialGradient id="vgN"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient><rect x="-300" y="-300" width="2520" height="1680" fill="url(#vgN)"/>`;
  }
  return s; };

// ===== CARDS =====
function hornCard(c, p, lt) { let s = `<rect width="1920" height="1080" fill="#0a1020"/>` + Array.from({ length: 60 }, (_, i) => `<circle cx="${rnd(i + 3) * 1920}" cy="${rnd(i + 90) * 500}" r="${1 + rnd(i + 7) * 2}" fill="#fff" opacity="${.3 + rnd(i) * .5}"/>`).join('');
  s += `<rect y="700" width="1920" height="380" fill="#06101c"/>` + skyline('brnight', 700, .6, 91, 0);
  s += `<g transform="translate(1250 760)"><path d="M-260 0 L260 0 L220 70 L-230 70Z" fill="#1a1e26" stroke="${INK}" stroke-width="5"/><rect x="-170" y="-90" width="300" height="90" fill="#22262e" stroke="${INK}" stroke-width="5"/><rect x="-80" y="-150" width="150" height="60" fill="#22262e" stroke="${INK}" stroke-width="5"/><rect x="0" y="-210" width="40" height="60" fill="#2a2e36" stroke="${INK}" stroke-width="5"/></g>`;
  const NN = c.n != null ? c.n : 3; const per = 2.3, k = Math.min(NN, Math.floor(Math.max(0, lt - .4) / per) + 1), on = ((lt - .4) % per) < 1.6 && lt > .4 && lt < .4 + NN * per;
  if (on) for (let r = 0; r < 4; r++) { const rr = 80 + ((lt * 260 + r * 90) % 360); s += `<path d="M${1270 - rr} ${560 - rr * .4} A${rr} ${rr} 0 0 1 ${1270 + rr} ${560 - rr * .4}" stroke="#ffd56a" stroke-width="8" fill="none" opacity="${1 - rr / 440}"/>`; }
  if (c.count !== false && lt > .4) s += `<text x="300" y="420" font-size="260" font-weight="900" fill="#ffd56a" font-family="DejaVu Sans" stroke="#000" stroke-width="10" paint-order="stroke">${k}</text>`;
  if (c.label) s += TM(960, 120, 40, c.label, '#e9e2cc', 900, 'middle');
  return s; }
function logCard(c, p) { let s = `<rect width="1920" height="1080" fill="#3a2e26"/><g transform="rotate(-2 960 540)"><rect x="300" y="80" width="1320" height="920" fill="#efe8d4" stroke="${INK}" stroke-width="8"/>`;
  for (let k = 0; k < 14; k++) s += `<path d="M330 ${200 + k * 58} H1590" stroke="#9ab4c6" stroke-width="2"/>`; s += `<path d="M420 90 V990" stroke="#d89a9a" stroke-width="3"/>` + T(960, 160, 46, c.title || 'RADIO LOG · N. PARK', '#2a2a2a', 900);
  c.lines.forEach((ln, i) => { const q = clamp(p * (c.lines.length + .5) - i, 0, 1); if (q <= 0) return; const red = (c.red || []).includes(i);
    s += `<text x="450" y="${250 + i * 116}" font-size="42" font-weight="700" fill="${red ? '#b02a1f' : '#2a3a5a'}" font-family="DejaVu Sans" font-style="italic" opacity="${q}">${ln}</text>`;
    if (red && q >= 1) s += `<path d="M440 ${266 + i * 116} H${450 + ln.length * 22}" stroke="#b02a1f" stroke-width="5"/>`; });
  return s + `</g>`; }
function mathCard(c, p) { let s = `<rect width="1920" height="1080" fill="${CREAM}"/>` + T(960, 160, 62, c.title, '#222', 900, 'middle', 'letter-spacing="3"');
  if (c.icon) s += `<g opacity="${clamp(p * 4, 0, 1)}">${icon(c.icon, 960, 300, 1.2)}</g>`;
  const y0 = c.icon ? 470 : 360; c.lines.forEach((ln, i) => { const q = clamp(p * (c.lines.length + .6) - i * 1.0, 0, 1); const [txt, col, sz] = typeof ln === 'string' ? [ln, '#222', 76] : ln;
    s += T(960, y0 + i * 150, sz || 76, txt, col || '#222', 900, 'middle', `opacity="${q}"`); });
  return s; }
function tankCard(c, p) { let s = `<rect width="1920" height="1080" fill="${CREAM}"/>` + T(960, 140, 62, 'THE TANK', '#222', 900, 'middle', 'letter-spacing="4"');
  const lv = c.level == null ? .92 : c.level, q = ease(clamp(p * 2, 0, 1));
  s += `<path d="M300 280 V860 Q560 900 820 860 V280 Q560 240 300 280Z" fill="#d9d4c7" stroke="${INK}" stroke-width="8"/>`;
  const top = 860 - (580 * lv * q); s += `<path d="M308 ${top} Q560 ${top + 20} 812 ${top} V856 Q560 894 308 856Z" fill="#69b3ee" opacity=".85"/>`;
  s += T(560, 620, 64, Math.round(200000 * ease(clamp(p * 2, 0, 1))).toLocaleString('en-US') + ' L', '#1b3d66', 900);
  (c.lines || []).forEach((ln, i) => { const qq = clamp(p * 4 - 1 - i, 0, 1); s += T(1370, 420 + i * 150, i === c.lines.length - 1 ? 84 : 60, ln, i === c.lines.length - 1 ? '#c33a2f' : '#222', 900, 'middle', `opacity="${qq}"`); });
  return s; }
function countCard(c, p, t) { let s = `<rect width="1920" height="1080" fill="#14161c"/>` + T(960, 150, 52, c.title || 'UNDER THE LADDER', '#e9e2cc', 900, 'middle', 'letter-spacing="4"');
  const n = Math.round((c.n || 0) * ease(clamp(p * 1.8, 0, 1))); const shown = Math.min(160, Math.round(n / (c.per || 2)));
  for (let k = 0; k < shown; k++) { const x = 220 + (k % 20) * 75 + (Math.floor(k / 20) % 2) * 36, y = 360 + Math.floor(k / 20) * 66; s += `<circle cx="${x}" cy="${y}" r="24" fill="#b9beb6" stroke="${INK}" stroke-width="4"/><circle cx="${x - 8}" cy="${y - 2}" r="5" fill="#3b3f33"/><circle cx="${x + 8}" cy="${y - 4}" r="5" fill="#3b3f33"/>`; }
  s += `<text x="960" y="980" font-size="120" font-weight="900" fill="#ff5a4a" text-anchor="middle" font-family="DejaVu Sans" stroke="#000" stroke-width="8" paint-order="stroke">${n}</text>`;
  if (c.label) s += T(960, 1050, 34, c.label, '#9a9a9a', 800);
  return s; }
function wmapCard(c, p) { let s = `<rect width="1920" height="1080" fill="#e9e2cc"/>` + T(960, 100, 52, c.title || 'HARBOR CITY', '#222', 900, 'middle', 'letter-spacing="3"');
  s += `<path d="M0 380 Q700 330 1200 420 Q1500 470 1920 400 V640 Q1500 700 1200 650 Q700 580 0 620Z" fill="#7ab0d8" stroke="${INK}" stroke-width="6"/>` + T(300, 520, 40, 'RIVER', '#2f5a7a', 900, 'middle', 'font-style="italic"');
  s += `<rect x="560" y="340" width="40" height="110" fill="#8a8f96" stroke="${INK}" stroke-width="5"/><rect x="560" y="560" width="40" height="110" fill="#8a8f96" stroke="${INK}" stroke-width="5"/>` + T(680, 520, 30, 'BRIDGE (GONE)', '#c33a2f', 900);
  s += `<rect x="400" y="160" width="200" height="110" fill="#f1ece2" stroke="${INK}" stroke-width="5"/>` + T(500, 240, 56, '+', '#c33a2f', 900) + T(500, 300, 28, 'EAST BANK · HOSPITAL', '#222', 800);
  s += `<g transform="translate(760 880) scale(.5)">${waterTower(0, 0, 1, 'brday')}</g>` + T(760, 920, 32, 'WATER TOWER · YOU', '#222', 900);
  if (c.swim) { const q = clamp(p * 2, 0, 1); s += `<path d="M580 500 Q640 600 700 ${560 + 100 * q} L760 ${700 + 120 * q}" stroke="#c33a2f" stroke-width="8" fill="none" stroke-dasharray="20 14"/>` + T(820, 640, 30, '200 m SWIM · 400 m RUN', '#c33a2f', 900, 'start', `opacity="${q}"`); }
  if (c.harbor) { s += `<path d="M1500 680 L1760 680 L1740 720 L1520 720Z" fill="#3a3e46" stroke="${INK}" stroke-width="4"/><rect x="1560" y="640" width="120" height="40" fill="#5a5e66" stroke="${INK}" stroke-width="4"/>` + T(1630, 790, 32, 'HARBOR · FERRY', '#222', 900) + T(1200, 860, 34, '3.2 km', '#c33a2f', 900, 'middle', `opacity="${clamp((p - .3) * 3, 0, 1)}"`) + `<path d="M840 880 Q1200 830 1540 740" stroke="#c33a2f" stroke-width="6" fill="none" stroke-dasharray="16 12" opacity="${clamp((p - .3) * 3, 0, 1)}"/>`; }
  return s; }
const _cardN = cardSVG;
cardSVG = function (c, p, t, dur) { const lt = p * dur;
  if (c.t === 'horn') return hornCard(c, p, lt);
  if (c.t === 'log') return logCard(c, p);
  if (c.t === 'math') return mathCard(c, p);
  if (c.t === 'tank') return tankCard(c, p);
  if (c.t === 'count') return countCard(c, p, t);
  if (c.t === 'wmap') return wmapCard(c, p);
  return _cardN(c, p, t, dur); };

// ===== thumbnail helper env (chroma key layer for tools/thumb.py v2) =====
ENV.tgreen = L => `<rect width="1920" height="1080" fill="#00ff00"/>`;

// =====================================================================
// ===== S1E3 additions: rope descent, raft, harbor, the Harbor Queen ferry
// =====================================================================
const RIV = L => isNw(L) ? '#06101c' : (L === 'brdusk' ? '#3a3448' : '#3e6078');
function ripples(y0, y1, L, seed, n = 50) { let s = ''; for (let i = 0; i < n; i++) s += `<path d="M${rnd(i + seed) * 1900} ${y0 + 10 + rnd(i + seed + 40) * (y1 - y0 - 10)} q40 -8 80 0" stroke="${isNw(L) ? '#1a2a44' : (L === 'brdusk' ? '#6a5a70' : '#8ab0c8')}" stroke-width="4" fill="none" opacity=".7"/>`; return s; }
function crane(x, y, sc, L) { const c = isNw(L) ? '#1a1e26' : (L === 'brdusk' ? '#3a2e36' : '#c9a03a');
  return `<g transform="translate(${x} ${y}) scale(${sc})"><path d="M-60 0 L-40 -420 M60 0 L40 -420 M-50 -100 L50 -200 M50 -100 L-50 -200 M-46 -260 L46 -360 M46 -260 L-46 -360" stroke="${c}" stroke-width="14"/><rect x="-200" y="-470" width="520" height="50" fill="${c}" stroke="${INK}" stroke-width="5"/><rect x="-60" y="-520" width="120" height="50" fill="${c}" stroke="${INK}" stroke-width="5"/><path d="M240 -420 V-300" stroke="${INK}" stroke-width="4"/><rect x="225" y="-300" width="30" height="24" fill="${INK}"/></g>`; }
function ferry(x, y, sc, L, o = {}) { const n = isNw(L), hull = n ? '#c8ccd0' : '#eceae4', sup = n ? '#b4b8bc' : '#f4f2ec', win = n ? '#141a24' : '#6a8aa4';
  let g = `<g transform="translate(${x} ${y}) scale(${sc})">`;
  g += P('M-620 -170 L640 -170 L580 0 L-560 0 Q-600 -70 -620 -170Z', hull, 7) + `<path d="M-612 -120 L626 -120 L620 -100 L-606 -100Z" fill="#1f3c6a"/><path d="M-590 -40 L606 -40" stroke="#b0302a" stroke-width="10"/>`;
  g += `<text x="-200" y="-60" font-size="44" font-weight="900" fill="#1f3c6a" font-family="DejaVu Sans" letter-spacing="4">HARBOR QUEEN</text>`;
  for (let i = 0; i < 22; i++) g += C(-520 + i * 50, -144, 9, win, 2);
  g += R(-500, -300, 900, 130, sup, 6); for (let i = 0; i < 14; i++) g += `<rect x="${-480 + i * 62}" y="-270" width="44" height="40" rx="6" fill="${win}" stroke="${INK}" stroke-width="3"/>`;
  g += R(-380, -400, 620, 100, sup, 6); for (let i = 0; i < 9; i++) g += `<rect x="${-360 + i * 66}" y="-380" width="46" height="36" rx="6" fill="${win}" stroke="${INK}" stroke-width="3"/>`;
  g += R(100, -490, 260, 90, sup, 6) + `<path d="M116 -470 H344 V-430 H116Z" fill="${win}" stroke="${INK}" stroke-width="3"/>`; // wheelhouse
  g += `<path d="M300 -490 v-26 M286 -516 h40" stroke="${INK}" stroke-width="6"/><path d="M290 -530 l40 -8 v24 l-40 -8z" fill="#c9a03a" stroke="${INK}" stroke-width="3"/>`; // air horn
  g += R(-260, -520, 90, 120, '#1f3c6a', 6) + `<rect x="-260" y="-520" width="90" height="26" fill="#b0302a" stroke="${INK}" stroke-width="5"/>`; // funnel
  g += `<rect x="-300" y="-338" width="150" height="40" rx="18" fill="#e0702a" stroke="${INK}" stroke-width="4"/><path d="M-300 -336 v-30 h150 v30" stroke="#8a9094" stroke-width="5" fill="none"/><path d="M-110 -336 v-30 h150 v30" stroke="#8a9094" stroke-width="5" fill="none"/>`; // one lifeboat + one empty davit
  g += `<path d="M-600 -170 L-600 40" stroke="#c9a77a" stroke-width="6"/>` + Array.from({ length: 9 }, (_, k) => `<path d="M-612 ${-150 + k * 22} h24" stroke="#c9a77a" stroke-width="5"/>`).join('') + `<path d="M-588 -170 L-588 40" stroke="#c9a77a" stroke-width="6"/>`; // rope ladder at stern
  g += `<path d="M600 -60 Q680 40 720 160" stroke="${INK}" stroke-width="8" stroke-dasharray="14 8" fill="none"/>`; // anchor chain
  if (o.lit) g += `<rect x="116" y="-470" width="228" height="40" fill="#ffd98a" opacity=".7"/>`;
  return g + `</g>`; }

// rope down the river side of the tower (side view, mid-height)
ENV.wrope = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 820, .7, 52, 0) + `<rect y="820" width="1920" height="260" fill="${RIV(L)}"/>` + ripples(830, 1080, L, 7, 30);
  s += `<path d="M-40 -40 H1500 V60 Q760 140 -40 60Z" fill="${n ? '#3a3e46' : '#a8a29a'}" stroke="${INK}" stroke-width="8"/><rect x="-40" y="40" width="1600" height="40" fill="${n ? '#2a2c32' : '#6a6e74'}" stroke="${INK}" stroke-width="6"/>`;
  s += `<path d="M380 60 L560 1140" stroke="${n ? '#2a2e36' : '#7a7e84'}" stroke-width="70"/><path d="M380 60 L560 1140" stroke="${INK}" stroke-width="4" opacity=".6"/><path d="M1620 60 L1440 1140" stroke="${n ? '#2a2e36' : '#7a7e84'}" stroke-width="70"/>`;
  s += `<path d="M420 300 L1580 520 M1580 300 L420 520" stroke="${n ? '#2a2e36' : '#7a7e84'}" stroke-width="20" opacity=".9"/>`;
  const cols = ['#e0a020', '#3a6ab0', '#d9d4c7']; for (let y = 80; y < 1100; y += 34) s += `<path d="M${958 + ((y / 34) % 2 ? 4 : -4)} ${y} L${962 - ((y / 34) % 2 ? 4 : -4)} ${y + 34}" stroke="${cols[Math.floor(y / 340) % 3]}" stroke-width="14" stroke-linecap="round"/>`;
  s += `<path d="M952 80 V1100 M968 80 V1100" stroke="${INK}" stroke-width="2" opacity=".5"/>`;
  return s; };
// raft on the river (pallets on blue drums). Raft deck top = y 1000
ENV.raft = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 640, .8, 63, 0) + `<rect y="640" width="1920" height="440" fill="${RIV(L)}"/>` + ripples(650, 1080, L, 11, 60);
  for (let k = 0; k < 6; k++) s += `<rect x="${600 + k * 125}" y="1000" width="110" height="74" rx="30" fill="#2f6fb5" stroke="${INK}" stroke-width="5"/><path d="M${612 + k * 125} 1036 h86" stroke="#1b3d66" stroke-width="5"/>`;
  s += `<rect x="560" y="984" width="820" height="22" fill="${n ? '#5a4632' : '#a07a4a'}" stroke="${INK}" stroke-width="5"/>` + Array.from({ length: 9 }, (_, k) => `<path d="M${560 + k * 102} 984 v22" stroke="${INK}" stroke-width="3"/>`).join('');
  s += `<rect x="1180" y="940" width="70" height="46" rx="8" fill="#e9e2cc" stroke="${INK}" stroke-width="4"/><rect x="1260" y="944" width="60" height="42" rx="8" fill="#e9e2cc" stroke="${INK}" stroke-width="4"/>`; // water jugs
  return s; };
// the harbor from the water: pier + cranes (left), ferry at anchor (right)
ENV.harbor = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 700, .8, 77, 0);
  s += crane(260, 760, .9, L) + crane(600, 760, .75, L);
  s += `<rect y="700" width="1920" height="380" fill="${RIV(L)}"/>` + ripples(710, 1080, L, 21, 50);
  s += `<rect x="-20" y="740" width="820" height="50" fill="${n ? '#2a2620' : '#7a6a54'}" stroke="${INK}" stroke-width="6"/>` + Array.from({ length: 9 }, (_, k) => `<rect x="${20 + k * 90}" y="790" width="22" height="120" fill="${n ? '#1e1a16' : '#5a4a38'}" stroke="${INK}" stroke-width="4"/>`).join('');
  s += ferry(1380, 900, .72, L);
  return s; };
// ferry wheelhouse
ENV.fwheel = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#2a2e36' : '#c9c4b8'}"/>`;
  s += `<svg x="120" y="110" width="1680" height="400" viewBox="0 340 1920 460" preserveAspectRatio="none">${wsky(L)}${skyline(L, 700, .8, 77, 0)}<rect y="700" width="1920" height="200" fill="${RIV(L)}"/>${crane(300, 760, .7, L)}<rect x="0" y="730" width="900" height="30" fill="${n ? '#2a2620' : '#7a6a54'}"/></svg>`;
  for (const x of [120, 680, 1240, 1800]) s += `<rect x="${x - 14}" y="100" width="28" height="420" fill="${n ? '#3a3e46' : '#e9e6de'}" stroke="${INK}" stroke-width="6"/>`;
  s += `<rect x="106" y="96" width="1708" height="428" fill="none" stroke="${INK}" stroke-width="8"/>`;
  s += `<rect x="200" y="660" width="1520" height="140" fill="${n ? '#3a3e46' : '#8a8f96'}" stroke="${INK}" stroke-width="7"/><rect x="200" y="640" width="1520" height="30" fill="${n ? '#4a4e56' : '#a8adb4'}" stroke="${INK}" stroke-width="6"/>`;
  s += `<g transform="translate(960 600)"><circle r="120" fill="none" stroke="#6a4a2a" stroke-width="22"/><circle r="120" fill="none" stroke="${INK}" stroke-width="3"/>` + Array.from({ length: 8 }, (_, k) => `<path d="M0 0 L${Math.cos(k * Math.PI / 4) * 150} ${Math.sin(k * Math.PI / 4) * 150}" stroke="#6a4a2a" stroke-width="12" stroke-linecap="round"/>`).join('') + `<circle r="24" fill="#4a3a2a" stroke="${INK}" stroke-width="5"/></g>`;
  s += `<rect x="380" y="560" width="160" height="90" rx="10" fill="#2a2c32" stroke="${INK}" stroke-width="5"/><path d="M460 600 L500 530" stroke="#c9a03a" stroke-width="12" stroke-linecap="round"/>` + T(460, 640, 22, 'ENGINE', '#e9e2cc', 800);
  s += `<rect x="1300" y="560" width="300" height="90" rx="8" fill="#20242a" stroke="${INK}" stroke-width="5"/>` + C(1360, 605, 22, '#b02a1f', 4) + T(1490, 595, 24, 'HORN', '#e9e2cc', 900) + T(1490, 630, 18, 'AUTO SIGNAL', '#9aa', 700);
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#1e2026' : '#6a6458'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  if (n) s += `<circle cx="1360" cy="605" r="160" fill="#ff4a3a" opacity=".08"/>`;
  return s; };
// passenger saloon + cafe counter
ENV.fsaloon = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#2e3038' : '#d8d2c4'}"/><rect y="0" width="1920" height="70" fill="${n ? '#24262c' : '#ece6da'}" stroke="${INK}" stroke-width="5"/>`;
  for (let i = 0; i < 6; i++) s += `<rect x="${60 + i * 200}" y="200" width="150" height="190" rx="22" fill="${n ? '#0a1020' : '#8ab0c8'}" stroke="${INK}" stroke-width="6"/>`;
  s += `<rect x="1280" y="380" width="640" height="40" fill="${n ? '#3a2e24' : '#8a6a4a'}" stroke="${INK}" stroke-width="5"/>` + T(1600, 300, 70, 'CAFÉ', n ? '#c9a03a' : '#b0302a', 900);
  for (let r = 0; r < 2; r++) for (let k = 0; k < 6; k++) s += `<rect x="${1320 + k * 95}" y="${440 + r * 80}" width="70" height="60" rx="6" fill="${['#c33a2f', '#e9c47a', '#3a6ab0'][(k + r) % 3]}" stroke="${INK}" stroke-width="3" opacity="${n ? .6 : .9}"/>`;
  s += `<rect x="1260" y="640" width="680" height="360" fill="${n ? '#4a3a2a' : '#9a7a5a'}" stroke="${INK}" stroke-width="7"/><rect x="1240" y="620" width="720" height="34" fill="${n ? '#5a4a3a' : '#b89a72'}" stroke="${INK}" stroke-width="6"/>`;
  for (let row = 0; row < 3; row++) for (let k = 0; k < 5; k++) { const x = 60 + k * 230, y = 700 + row * 110; s += `<path d="M${x} ${y} q0 -80 20 -90 h120 q20 10 20 90z" fill="${n ? '#8a4a24' : '#e07a2a'}" stroke="${INK}" stroke-width="5"/><path d="M${x + 10} ${y} v${40}" stroke="${INK}" stroke-width="5"/>`; }
  s += `<path d="M300 610 l30 -6 l4 14 l-30 6z M780 720 l40 0 l0 10 l-40 0z" fill="#e9e2cc" stroke="${INK}" stroke-width="3"/>`; // plates / coat
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#262a34' : '#6a7a8a'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  if (n) s += `<rect width="1920" height="1080" fill="#0a1020" opacity=".2"/>`;
  return s; };
// open top deck: awning, railing, harbor + distant water tower, wheelhouse with air horn (right)
ENV.fdeck = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 640, .75, 91, 0) + `<g transform="translate(330 640) scale(.55)">${waterTower(0, 0, 1, L)}</g>` + `<rect y="640" width="1920" height="440" fill="${RIV(L)}"/>` + ripples(650, 900, L, 31, 30);
  s += `<rect x="1380" y="260" width="600" height="760" fill="${n ? '#9a9ea4' : '#f4f2ec'}" stroke="${INK}" stroke-width="7"/><rect x="1420" y="320" width="460" height="130" fill="${n ? '#141a24' : '#6a8aa4'}" stroke="${INK}" stroke-width="5"/>`;
  s += `<path d="M1620 260 v-60 M1590 200 h70" stroke="${INK}" stroke-width="8"/><path d="M1600 186 l90 -18 v52 l-90 -18z" fill="#c9a03a" stroke="${INK}" stroke-width="5"/><path d="M1650 180 Q1640 ${400} 1660 620" stroke="#d9d4c7" stroke-width="5" fill="none"/>`; // air horn + pull cord
  s += `<path d="M-40 60 L1380 140 L1380 180 L-40 110Z" fill="#2f6a4a" stroke="${INK}" stroke-width="6"/>` + Array.from({ length: 6 }, (_, k) => `<path d="M${k * 270} ${66 + k * 15} v${60}" stroke="${INK}" stroke-width="3" opacity=".5"/>`).join('') + `<path d="M100 110 V1000 M1300 180 V1000" stroke="${n ? '#4a4e56' : '#8a8f96'}" stroke-width="12"/>`;
  s += `<path d="M0 860 H1380 M0 920 H1380" stroke="${n ? '#6a6e76' : '#e9e6de'}" stroke-width="10"/>` + Array.from({ length: 12 }, (_, k) => `<path d="M${k * 120} 860 V1000" stroke="${n ? '#6a6e76' : '#e9e6de'}" stroke-width="9"/>`).join('');
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#2a2c32' : '#7a8088'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  return s; };
// stairwell landing in front of the car-deck door (chain drawn in fx)
ENV.fcar = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#2a2c30' : '#6a6e70'}"/>` + Array.from({ length: 60 }, (_, k) => `<circle cx="${40 + (k % 15) * 130}" cy="${60 + Math.floor(k / 15) * 260}" r="6" fill="${INK}" opacity=".4"/>`).join('');
  for (let k = 0; k < 9; k++) s += `<rect x="${0}" y="${280 + k * 80}" width="${560 - k * 60}" height="80" fill="${n ? '#3a3c42' : '#80848a'}" stroke="${INK}" stroke-width="4"/>`; s += `<path d="M40 260 L560 1000" stroke="#c9a03a" stroke-width="10"/>`;
  s += `<rect x="740" y="260" width="440" height="740" rx="30" fill="${n ? '#4a4e44' : '#7a8270'}" stroke="${INK}" stroke-width="10"/><rect x="740" y="260" width="440" height="740" rx="30" fill="none" stroke="#c9a03a" stroke-width="4" stroke-dasharray="30 30" opacity=".5"/>`;
  s += C(960, 440, 70, n ? '#06080a' : '#141618', 10) + `<rect x="1110" y="560" width="30" height="120" rx="10" fill="#8a8f96" stroke="${INK}" stroke-width="5"/>`;
  s += `<rect x="760" y="180" width="400" height="60" fill="#e0b020" stroke="${INK}" stroke-width="5"/>` + T(960, 228, 44, 'CAR DECK', '#1d1d21', 900);
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#1a1c20' : '#4a4e54'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  return s; };
// crew cabin nine: bunk, porthole, blanket nest, taped drawings, air vent
ENV.fcabin = L => { const n = isNw(L); let s = `<rect width="1920" height="1080" fill="${n ? '#3a3630' : '#cfc4ae'}"/>`;
  s += C(1500, 380, 110, n ? '#0a1020' : '#8ab0c8', 14) + C(1500, 380, 124, 'none', 6);
  s += `<rect x="80" y="300" width="640" height="50" fill="${n ? '#4a3a2a' : '#8a6a4a'}" stroke="${INK}" stroke-width="6"/><rect x="80" y="640" width="640" height="60" fill="${n ? '#4a3a2a' : '#8a6a4a'}" stroke="${INK}" stroke-width="6"/><path d="M90 300 V1000 M710 300 V1000" stroke="${INK}" stroke-width="12"/><rect x="100" y="600" width="600" height="40" fill="#3a5a8a" stroke="${INK}" stroke-width="4"/>`;
  s += Array.from({ length: 7 }, (_, k) => `<rect x="${1630 + k * 26}" y="${236 - (k % 2) * 4}" width="18" height="12" fill="#e9c47a" stroke="${INK}" stroke-width="2"/>`).join('') + `<rect x="1600" y="248" width="240" height="10" fill="#5a5a5a"/><rect x="1620" y="120" width="200" height="110" fill="#8a8f96" stroke="${INK}" stroke-width="6" transform="rotate(-8 1620 230)"/>` + Array.from({ length: 5 }, (_, k) => `<path d="M1640 ${140 + k * 18} h160" stroke="${INK}" stroke-width="5"/>`).join('');
  const pics = [[880, 250, -4], [1080, 300, 5], [900, 470, 3]]; for (const [x, y, r] of pics) s += `<g transform="rotate(${r} ${x + 80} ${y + 60})"><rect x="${x}" y="${y}" width="160" height="120" fill="#f4f0e4" stroke="${INK}" stroke-width="4"/><path d="M${x + 20} ${y + 100} q40 -60 80 -10 q20 20 40 -30" stroke="#3a6ab0" stroke-width="5" fill="none"/><circle cx="${x + 120}" cy="${y + 30}" r="14" fill="#e0b020"/><rect x="${x + 60}" y="${y - 8}" width="40" height="16" fill="#e9e2cc" opacity=".8"/></g>`;
  s += `<path d="M780 1000 q60 -110 200 -90 q140 -40 220 40 q60 30 40 50z" fill="#8a5a6a" stroke="${INK}" stroke-width="6"/><path d="M840 990 q80 -60 180 -40" stroke="#5a3a4a" stroke-width="5" fill="none"/>`;
  s += Array.from({ length: 6 }, (_, k) => `<rect x="${1280 + k * 34}" y="${980 - (k % 2) * 6}" width="22" height="14" fill="#e9c47a" stroke="${INK}" stroke-width="2"/>`).join('');
  s += `<rect y="1000" width="1920" height="80" fill="${n ? '#2a2620' : '#6a5a44'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  if (n) s += `<rect width="1920" height="1080" fill="#0a1020" opacity=".2"/>`;
  return s; };

// ===== S1E3 FX =====
const _fxS13 = fxSVG;
fxSVG = function (shot, lt, p, t, front) { const f = shot.fx || [], E = shot.env, L = shot.light; const has = k => f.includes(k); let s = _fxS13(shot, lt, p, t, front);
  if (!front) {
    if (has('pier') && E === 'harbor') { const g = shot.gn != null ? shot.gn : .6; s += crowd(10, 790, 690, 1.0, Math.round(20 + g * 110), 41, L); }
    if (has('wade') && E === 'harbor') { const q = clamp(p * 1.4, 0, 1); s += crowd(780, 1000, 720 + q * 30, .9, 22, 57, L) + `<rect x="760" y="${770 + 0}" width="300" height="200" fill="${RIV(L)}" opacity=".92"/>`; }
    if (has('heli') && (E === 'harbor' || E === 'fdeck')) { const hx = (shot.hx0 != null ? shot.hx0 : 300) + (shot.hdx != null ? shot.hdx : 500) * p, hy = 180;
      s += `<path d="M${hx} ${hy} L${hx - 220} 1080 L${hx + 220} 1080Z" fill="#fff4c0" opacity=".16"/><ellipse cx="${hx}" cy="${hy}" rx="60" ry="24" fill="#14161c"/><path d="M${hx + 50} ${hy} h80" stroke="#14161c" stroke-width="10"/><path d="M${hx - 90 + Math.sin(t * 40) * 30} ${hy - 30} h${180}" stroke="#14161c" stroke-width="5"/><circle cx="${hx}" cy="${hy + 20}" r="10" fill="#fff"/><circle cx="${hx + 120}" cy="${hy - 6}" r="5" fill="#ff3a2a" opacity="${Math.floor(t * 2) % 2}"/>`; }
    if (has('farlight') && (E === 'harbor' || E === 'fdeck')) s += `<circle cx="160" cy="260" r="8" fill="#fff"/><path d="M160 260 L${60 + Math.sin(t) * 60} 700 L${260 + Math.sin(t) * 60} 700Z" fill="#fff4c0" opacity=".12"/>`;
    if (has('debris') && E === 'raft') s += `<path d="M-40 0 H1960 V140 H-40Z" fill="${isNw(L) ? '#1a1c22' : '#5a5e66'}" stroke="${INK}" stroke-width="6"/><path d="M200 140 L240 700 M1700 140 L1660 700" stroke="${isNw(L) ? '#1a1c22' : '#5a5e66'}" stroke-width="60"/><path d="M120 760 l220 -40 l40 50 l-250 20z M1420 740 l200 -30 l30 60 l-240 0z" fill="#3a3e46" stroke="${INK}" stroke-width="5"/><path d="M1500 800 q60 -70 140 -6 l0 20 h-150z" fill="#a83a2f" stroke="${INK}" stroke-width="5"/><path d="M300 400 L760 940" stroke="#5a5e66" stroke-width="6"/>`;
    if (has('hornpull') && E === 'fdeck') {} // cord swing handled in front
    if (has('blankets') && E === 'fcabin') {}
  }
  if (front) {
    if (E === 'raft') { const wl = shot.wlv || 1046; s += `<path d="M-300 ${wl} ` + Array.from({ length: 30 }, (_, k) => `q40 ${(k % 2 ? 1 : -1) * 8} 80 0`).join(' ') + ` V1400 H-300Z" fill="${RIV(L)}" opacity=".9" transform="translate(${Math.sin(t * 1.5) * 20} 0)"/>`; }
    if (has('chain') && E === 'fcar') { const a = shot.rattle ? Math.sin(t * 38) * 6 : 0; s += `<path d="M770 ${470 + a} Q960 ${560 + a} 1150 ${470 - a} M770 ${640 - a} Q960 ${540 - a} 1150 ${650 + a}" stroke="#9aa0a6" stroke-width="18" stroke-dasharray="26 8" fill="none"/><path d="M770 ${470 + a} Q960 ${560 + a} 1150 ${470 - a} M770 ${640 - a} Q960 ${540 - a} 1150 ${650 + a}" stroke="${INK}" stroke-width="3" stroke-dasharray="26 8" fill="none"/><rect x="930" y="${560 + a}" width="60" height="70" rx="8" fill="#c9a03a" stroke="${INK}" stroke-width="5"/><path d="M940 ${560 + a} q20 -40 40 0" stroke="#8a8f96" stroke-width="8" fill="none"/>`; }
    if (has('porthole') && E === 'fcar') { for (const [dx, dy] of [[-22, 10], [26, 22]]) s += `<circle cx="${960 + dx + Math.sin(t * 2 + dx) * 6}" cy="${440 + dy}" r="26" fill="#8a9284" stroke="${INK}" stroke-width="4"/><circle cx="${952 + dx + Math.sin(t * 2 + dx) * 6}" cy="${436 + dy}" r="5" fill="#ff3a1a"/><circle cx="${968 + dx + Math.sin(t * 2 + dx) * 6}" cy="${434 + dy}" r="5" fill="#ff3a1a"/>`; s += `<circle cx="960" cy="440" r="66" fill="none" stroke="${INK}" stroke-width="10"/>`; }
    if (has('chainopen') && E === 'fcar') { s += `<path d="M700 1000 q60 -30 120 -4 q60 26 120 -6 q60 -20 100 10 q40 -24 90 0" stroke="#9aa0a6" stroke-width="18" stroke-dasharray="26 8" fill="none"/><rect x="1060" y="960" width="60" height="70" rx="8" fill="#c9a03a" stroke="${INK}" stroke-width="5"/><path d="M1070 960 q30 -60 54 -40" stroke="#8a8f96" stroke-width="8" fill="none"/>`; }
    if (has('ajar') && E === 'fcar') { const w = 18 + 30 * ease(clamp(p * 1.5, 0, 1)) * (shot.wide || 1); s += `<path d="M${1180 - w} 290 L1180 280 L1180 1000 L${1180 - w} 1000Z" fill="#020203"/>`;
      if (shot.grab) { const hx = 1180 - w, hy = shot.grab; s += [0, 1, 2, 3].map(k => `<path d="M${hx + 6} ${hy + k * 26} q-34 -6 -40 14 q0 8 10 8 q16 -6 30 0" fill="#9aa092" stroke="${INK}" stroke-width="4"/>`).join(''); }
      if (shot.eyes) { const ex = 1180 - w / 2; for (const ey of (shot.eyey || [520, 700])) s += `<circle cx="${ex - 13}" cy="${ey}" r="7" fill="#ff3a1a"/><circle cx="${ex + 13}" cy="${ey - 2}" r="7" fill="#ff3a1a"/><circle cx="${ex}" cy="${ey}" r="22" fill="#ff3a1a" opacity=".25"/>`; } }
    if (has('swing') && E === 'fdeck') { const a = Math.sin(t * 4) * 40 * Math.exp(-lt * .3); s += `<path d="M1650 180 Q${1640 + a} 400 ${1660 + a * 1.6} 620" stroke="#f4f0e4" stroke-width="7" fill="none"/>`; }
  }
  return s; };

// ===== S1E3 CARDS =====
function hpanelCard(c, p, lt) { let s = `<rect width="1920" height="1080" fill="#1a1c20"/><rect x="260" y="140" width="1400" height="800" rx="30" fill="#2a2e34" stroke="${INK}" stroke-width="10"/>` + T(960, 240, 56, 'HORN · SIGNAL PANEL', '#e9e2cc', 900, 'middle', 'letter-spacing="4"');
  s += `<rect x="360" y="330" width="420" height="220" rx="16" fill="#1d1f22" stroke="${INK}" stroke-width="6"/>` + T(570, 400, 36, 'AUTO SIGNAL', '#9aa', 900) + `<rect x="520" y="430" width="100" height="90" rx="12" fill="#3a3e46" stroke="${INK}" stroke-width="5"/><path d="M570 475 L${c.off ? 540 : 600} 440" stroke="#c9a03a" stroke-width="16" stroke-linecap="round"/>`;
  s += TM(570, 610, 40, '21:00 · 3 SHORT', '#ffd56a', 900, 'middle');
  const lev = c.bat == null ? 0 : c.bat, q = ease(clamp(p * 1.6, 0, 1)), v = 1 - q * (1 - lev); const ang = -150 + 120 * v;
  s += `<circle cx="1260" cy="520" r="200" fill="#e9e2cc" stroke="${INK}" stroke-width="8"/><path d="M1100 520 A160 160 0 0 1 1420 520" stroke="#3a9a5a" stroke-width="20" fill="none"/><path d="M1100 520 A160 160 0 0 1 1150 400" stroke="#c33a2f" stroke-width="20" fill="none"/>`;
  s += `<path d="M1260 520 L${1260 + Math.cos(ang * Math.PI / 180) * 170} ${520 + Math.sin(ang * Math.PI / 180) * 170}" stroke="${INK}" stroke-width="10" stroke-linecap="round"/>` + C(1260, 520, 20, INK, 2) + T(1260, 640, 40, 'BATTERY', '#222', 900);
  s += T(1260, 820, 90, Math.round(v * 100) + '%', v < .05 ? '#ff5a4a' : '#e9e2cc', 900, 'middle', 'stroke="#000" stroke-width="4" paint-order="stroke"');
  return s; }
function drawingCard(c, p) { let s = `<rect width="1920" height="1080" fill="#3a3630"/><g transform="rotate(${c.back ? 2 : -2} 960 540)"><rect x="300" y="90" width="1320" height="900" fill="#f6f2e6" stroke="${INK}" stroke-width="6"/>`;
  const cr = (d, col, w = 10) => `<path d="${d}" stroke="${col}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".85"/>`;
  if (!c.back) {
    s += cr('M720 880 L760 520 M900 880 L860 520 M740 700 L880 640 M740 640 L880 700', '#5a5a6a', 12) + cr('M700 520 H920 V400 Q810 360 700 400Z', '#5a5a6a', 12) + `<path d="M700 520 H920 V400 Q810 360 700 400Z" fill="#9aa0b0" opacity=".4"/>`;
    s += `<circle cx="500" cy="260" r="40" fill="#ffd400"/>` + Array.from({ length: 10 }, (_, k) => cr(`M${500 + Math.cos(k * .63) * 56} ${260 + Math.sin(k * .63) * 56} L${500 + Math.cos(k * .63) * 120} ${260 + Math.sin(k * .63) * 120}`, '#f0b400', 7)).join('') + cr('M560 300 L700 420', '#f0b400', 6);
    const fig = (x, col, hatd) => cr(`M${x} 360 v-60 M${x} 340 l-26 30 M${x} 340 l26 30 M${x} 360 l-20 40 M${x} 360 l20 40`, col, 9) + `<circle cx="${x}" cy="${282}" r="22" fill="none" stroke="${col}" stroke-width="8"/>` + hatd;
    s += `<g transform="translate(820 400) scale(1.8) translate(-820 -400)">` + fig(760, '#2a3a8a', cr('M736 270 h48 v-14 h-48z', '#1f3c6a', 9)) + fig(820, '#e0a020', cr('M800 262 q20 -24 40 0', '#2a1c16', 9)) + fig(880, '#2a2a2a', cr('M860 266 q20 -36 40 0', '#1f3c6a', 12) + `<circle cx="880" cy="232" r="8" fill="#9a9a9a"/>` + cr('M864 304 h34', '#c33a2f', 9)) + `</g>`;
    s += `<path d="M300 900 q80 -20 160 0 t160 0 t160 0 t160 0 t160 0 t160 0 t160 0 t160 0 V988 H300Z" fill="#3a6ab0" opacity=".55"/>` + cr('M1180 880 L1520 880 L1490 930 L1210 930Z', '#2a2a2a', 9) + cr('M1260 880 V830 H1420 V880 M1370 830 V790 H1410 V830', '#2a2a2a', 8);
    s += cr('M1330 790 v-40 M1330 770 l-14 14 M1330 770 l14 14', '#b0302a', 7) + `<circle cx="1330" cy="738" r="13" fill="none" stroke="#b0302a" stroke-width="6"/>` + cr('M1316 732 l-12 -10 M1344 732 l12 -10', '#b0302a', 6);
    s += cr('M1330 700 Q1200 560 940 420', '#b0302a', 5).replace('stroke-linecap="round"', 'stroke-linecap="round" stroke-dasharray="12 16"');
    s += `<text x="1520" y="210" font-size="76" font-weight="900" fill="#c33a2f" text-anchor="end" font-family="DejaVu Sans" font-style="italic" transform="rotate(-6 1400 190)">DAY 89</text>`;
    if (c.zoom) s += `<circle cx="1420" cy="190" r="${130 + Math.sin(p * 20) * 4}" fill="none" stroke="#ff2a1a" stroke-width="12" opacity="${clamp(p * 3, 0, 1)}"/>`;
  } else {
    const ln = c.lines || []; ln.forEach((l, i) => { const q = clamp(p * (ln.length + .6) - i, 0, 1); s += `<text x="${400 + (i % 2) * 30}" y="${300 + i * 170}" font-size="80" font-weight="700" fill="#2a2a5a" font-family="DejaVu Sans" font-style="italic" opacity="${q}" transform="rotate(${(i % 2 ? 1 : -1) * 1.5} 960 ${300 + i * 170})">${l}</text>`; });
  }
  return s + `</g>`; }
const _cardS13 = cardSVG;
cardSVG = function (c, p, t, dur) { const lt = p * dur;
  if (c.t === 'hpanel') return hpanelCard(c, p, lt);
  if (c.t === 'drawing') return drawingCard(c, p);
  return _cardS13(c, p, t, dur); };

// =====================================================================
// ===== S1E4 additions: lifeboat, Harbor Street station, flooded Harbor Line tunnel, pump room, Hospital station
// =====================================================================
const isSD = L => L === 'subdark' || L === 'subred' || L === 'brnight' || L === 'bred';
Object.assign(LIGHT, {
  sub: t => `<rect width="1920" height="1080" fill="#0a1a18" opacity=".22"/>`,
  subdark: t => `<rect width="1920" height="1080" fill="#040a0c" opacity=".3"/>`,
  subred: t => `<rect width="1920" height="1080" fill="#0a0406" opacity=".18"/><rect width="1920" height="1080" fill="#ff2010" opacity="${.06 + .06 * (Math.sin(t * 4) + 1) / 2}"/>`,
});
const WAT = '#0b1a1c';
function tiles(x, y, w, h, c1, c2, step = 46) { let s = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${c1}"/>`;
  for (let yy = y; yy < y + h; yy += step) s += `<path d="M${x} ${yy} H${x + w}" stroke="${c2}" stroke-width="3"/>`;
  for (let xx = x; xx < x + w; xx += step * 1.6) s += `<path d="M${xx} ${y} V${y + h}" stroke="${c2}" stroke-width="2" opacity=".7"/>`;
  return s; }
function stains(x0, x1, y0, seed, n = 10) { let s = ''; for (let i = 0; i < n; i++) { const x = x0 + rnd(seed + i) * (x1 - x0), h = 80 + rnd(seed + i + 7) * 260; s += `<path d="M${x} ${y0} q${-8 + rnd(i) * 16} ${h * .5} ${4} ${h}" stroke="#4a3a22" stroke-width="${10 + rnd(i + 3) * 18}" opacity=".35" stroke-linecap="round" fill="none"/>`; } return s; }
function waterBand(y0, y1, seed, n = 30) { return `<rect x="-40" y="${y0}" width="2000" height="${y1 - y0}" fill="${WAT}"/>` + Array.from({ length: n }, (_, i) => `<path d="M${rnd(i + seed) * 1900} ${y0 + 8 + rnd(i + seed + 50) * (y1 - y0 - 12)} q30 -6 60 0" stroke="#2a4a4e" stroke-width="3" fill="none" opacity=".8"/>`).join(''); }
function vend(x, y, col, lab) { let s = `<rect x="${x}" y="${y}" width="180" height="380" rx="8" fill="${col}" stroke="${INK}" stroke-width="6"/><rect x="${x + 16}" y="${y + 50}" width="110" height="250" fill="#1a2024" stroke="${INK}" stroke-width="4"/>`;
  for (let r = 0; r < 5; r++) for (let k = 0; k < 3; k++) s += `<rect x="${x + 24 + k * 34}" y="${y + 62 + r * 48}" width="26" height="30" rx="4" fill="${['#c33a2f', '#e0a020', '#3a6ab0', '#e9e2cc'][(r + k) % 4]}" opacity=".85"/>`;
  return s + `<rect x="${x + 136}" y="${y + 80}" width="30" height="90" fill="#2a2e34" stroke="${INK}" stroke-width="3"/>` + T(x + 90, y + 36, 24, lab, '#fff', 900) + `<rect x="${x + 16}" y="${y + 316}" width="110" height="40" fill="#0e1012" stroke="${INK}" stroke-width="3"/>`; }

// street-level entrance to Harbor Street station, next to the harbor (night)
ENV.sentry = L => { const n = isNw(L); let s = wsky(L) + skyline(L, 700, .8, 77, 0) + crane(260, 760, .8, L) + `<rect y="700" width="1920" height="120" fill="${RIV(L)}"/>` + ripples(705, 815, L, 21, 20) + ferry(1550, 790, .32, L);
  s += `<rect y="820" width="1920" height="260" fill="${n ? '#1c1e22' : '#5a5c60'}"/><path d="M0 820 H1920" stroke="${INK}" stroke-width="6"/>`;
  s += `<path d="M700 1080 L760 880 L1160 880 L1220 1080Z" fill="#06080a" stroke="${INK}" stroke-width="6"/>`;
  for (let k = 0; k < 7; k++) { const y = 900 + k * 26, w = 400 + k * 17; s += `<path d="M${960 - w / 2} ${y} H${960 + w / 2}" stroke="#2a2e34" stroke-width="${4 + k}" opacity="${.9 - k * .1}"/>`; }
  s += `<path d="M700 1080 L760 880 L760 820 M1220 1080 L1160 880 L1160 820" stroke="#6a6e76" stroke-width="10" fill="none"/><path d="M760 830 H1160" stroke="#6a6e76" stroke-width="8"/>`;
  s += `<path d="M1260 880 V620" stroke="#3a3e46" stroke-width="14"/><circle cx="1260" cy="590" r="44" fill="#3fae6a" stroke="${INK}" stroke-width="6"/>` + T(1260, 608, 50, 'M', '#fff', 900);
  s += `<rect x="760" y="720" width="400" height="70" fill="#1f3c6a" stroke="${INK}" stroke-width="5"/>` + T(960, 768, 38, 'HARBOR ST STATION', '#fff', 900);
  return s; };
// the station platform, side view. Platform floor y=1000, flooded track in front
ENV.splat = L => { const d = isSD(L); let s = `<rect width="1920" height="1080" fill="${d ? '#3a3a32' : '#8a8670'}"/>`;
  s += tiles(0, 130, 1640, 870, d ? '#5a5a4c' : '#c9c4a8', d ? '#4a4a3e' : '#aaa58a');
  s += `<rect x="0" y="0" width="1920" height="130" fill="${d ? '#1e2022' : '#4a4e50'}" stroke="${INK}" stroke-width="6"/>` + Array.from({ length: 5 }, (_, k) => `<rect x="${120 + k * 330}" y="96" width="200" height="18" rx="6" fill="${d ? '#2a2e30' : '#6a7070'}" stroke="${INK}" stroke-width="3"/>`).join('');
  s += stains(0, 1640, 130, 11, 14);
  s += `<rect x="0" y="300" width="1640" height="44" fill="#2f6a4a"/><rect x="520" y="200" width="760" height="110" fill="#1f3c6a" stroke="${INK}" stroke-width="6"/>` + T(900, 278, 66, 'HARBOR STREET', '#fff', 900, 'middle', 'letter-spacing="6"');
  s += `<rect x="900" y="470" width="300" height="190" fill="#efe8d4" stroke="${INK}" stroke-width="5"/><path d="M930 600 H1170" stroke="#c33a2f" stroke-width="8"/>` + [940, 1020, 1100, 1160].map((x, i) => C(x, 600, 10, i === 0 || i === 3 ? '#c33a2f' : '#fff', 4)).join('') + `<path d="M1010 520 q30 40 0 80 M1050 520 q30 40 0 80" stroke="#7ab0d8" stroke-width="16" fill="none" opacity=".8"/>` + T(1050, 500, 22, 'HARBOR LINE', '#222', 900) + T(1050, 640, 15, 'HARBOR ST · · · ST. MARY\'S HOSPITAL', '#222', 800);
  s += vend(80, 620, '#b0302a', 'SNACKS') + vend(290, 620, '#2a5a9a', 'SNACKS') + vend(500, 620, '#3a3e46', 'DRINKS');
  s += `<rect x="1300" y="640" width="280" height="360" fill="${d ? '#4a3a2a' : '#8a6a4a'}" stroke="${INK}" stroke-width="6"/><rect x="1280" y="600" width="320" height="50" fill="#c9a03a" stroke="${INK}" stroke-width="5"/>` + T(1440, 640, 34, 'NEWS', '#1d1d21', 900) + `<rect x="1320" y="680" width="240" height="140" fill="#1a1c20" stroke="${INK}" stroke-width="4"/>`;
  s += `<rect x="760" y="900" width="420" height="22" fill="#6b4a2e" stroke="${INK}" stroke-width="5"/><path d="M790 922 v78 M1150 922 v78" stroke="${INK}" stroke-width="8"/>`;
  s += `<path d="M1640 1080 V560 Q1780 420 1960 430 V1080Z" fill="#050708" stroke="${INK}" stroke-width="8"/><path d="M1640 560 Q1780 420 1960 430" stroke="${d ? '#6a6a5a' : '#c9c4a8'}" stroke-width="18" fill="none"/>`;
  s += `<rect y="1000" width="1920" height="40" fill="${d ? '#3a3c3a' : '#7a7c78'}" stroke="${INK}" stroke-width="5"/><rect y="1030" width="1920" height="12" fill="#d8b52a"/>` + waterBand(1042, 1080, 5, 14);
  return s; };
// inside the stalled subway car at the platform: the shelter
ENV.scar = L => { const d = isSD(L); let s = `<rect width="1920" height="1080" fill="${d ? '#4a5054' : '#b9c0c4'}"/><rect y="0" width="1920" height="120" fill="${d ? '#3a4044' : '#d9dee0'}" stroke="${INK}" stroke-width="5"/>`;
  for (let k = 0; k < 6; k++) s += `<rect x="${60 + k * 310}" y="140" width="250" height="70" fill="${['#c9a03a', '#3a6ab0', '#c33a2f'][k % 3]}" stroke="${INK}" stroke-width="4" opacity=".75"/>`;
  for (let k = 0; k < 4; k++) s += `<rect x="${80 + k * 470}" y="260" width="380" height="300" rx="30" fill="${d ? '#14181a' : '#5a6460'}" stroke="${INK}" stroke-width="8"/>` + tiles(96 + k * 470, 276, 348, 268, d ? '#2a2c26' : '#7a7860', d ? '#22241e' : '#6a6852', 40).replace('<rect', '<rect opacity=".6"');
  for (let k = 0; k < 4; k++) s += `<path d="M${60 + k * 470} 820 q0 -150 30 -170 h360 q30 20 30 170z" fill="#d0682a" stroke="${INK}" stroke-width="6"/>`;
  s += `<path d="M520 120 V1000 M990 120 V1000 M1460 120 V1000" stroke="#c9ccd0" stroke-width="16"/><path d="M520 120 V1000 M990 120 V1000 M1460 120 V1000" stroke="${INK}" stroke-width="3" opacity=".6"/>`;
  s += `<rect y="1000" width="1920" height="80" fill="${d ? '#2a2c30' : '#5a5e64'}"/><path d="M0 1000 H1920" stroke="${INK}" stroke-width="6"/>`;
  if (d) s += `<circle cx="960" cy="900" r="320" fill="#ffcf7a" opacity=".1"/>`;
  return s; };
// the flooded tunnel, perspective. vanishing point 960,470. Water plane from y≈760 (edges) to 520 (far)
ENV.stunnel = L => { const d = isSD(L), red = L === 'subred'; const wall = d ? '#26302e' : '#3e4a48', ln = d ? '#1a2220' : '#2e3836';
  let s = `<rect width="1920" height="1080" fill="${wall}"/>`;
  for (let k = 0; k < 12; k++) { const f = Math.pow(.8, k), W = 1150 * f, H = 760 * f; s += `<path d="M${960 - W} ${470 + 420 * f} V${470 - H * .2} Q${960 - W} ${470 - H} 960 ${470 - H} Q${960 + W} ${470 - H} ${960 + W} ${470 - H * .2} V${470 + 420 * f}" stroke="${ln}" stroke-width="${2 + 9 * f}" fill="none"/>`; }
  for (let r = 0; r < 9; r++) { const y = 140 + r * 85; s += `<path d="M0 ${y} L${880} ${430 + (y - 470) * .12}" stroke="${ln}" stroke-width="2" opacity=".8"/><path d="M1920 ${y} L1040 ${430 + (y - 470) * .12}" stroke="${ln}" stroke-width="2" opacity=".8"/>`; }
  s += `<path d="M0 250 L900 445 M0 300 L900 452" stroke="#4a3a2a" stroke-width="22" opacity=".9"/><path d="M0 250 L900 445 M0 300 L900 452" stroke="${INK}" stroke-width="3"/><path d="M1920 210 L1020 440" stroke="#5a5e5a" stroke-width="26"/><path d="M1920 210 L1020 440" stroke="${INK}" stroke-width="3"/>`;
  for (let k = 0; k < 6; k++) { const f = Math.pow(.72, k); s += `<rect x="${960 - 60 * f}" y="${470 - 640 * f}" width="${120 * f}" height="${10 * f + 2}" fill="#3a4240" opacity=".8"/>`; }
  s += `<ellipse cx="960" cy="470" rx="95" ry="80" fill="#020304"/>`;
  s += `<path d="M0 760 L880 515 L1040 515 L1920 760 V1080 H0Z" fill="${WAT}"/>` + Array.from({ length: 40 }, (_, i) => { const u = rnd(i + 3), y = 520 + u * u * 520, w = 20 + u * 80; return `<path d="M${960 + (rnd(i + 40) - .5) * (200 + u * 1900)} ${y} q${w / 2} -${2 + u * 5} ${w} 0" stroke="#2a4a4e" stroke-width="${1 + u * 3}" fill="none" opacity=".8"/>`; }).join('');
  s += `<path d="M0 742 L880 510" stroke="#5a625e" stroke-width="14" opacity=".8"/>`; // submerged walkway edge (left benchwall)
  s += stains(0, 1920, 0, 31, 12);
  if (red) s += `<circle cx="1700" cy="200" r="30" fill="#ff3a1a"/><circle cx="1700" cy="200" r="200" fill="#ff3a1a" opacity=".12"/>`;
  return s; };
// pump station 2, mid-river cross-passage, knee/waist water
ENV.spump = L => { const d = isSD(L); let s = `<rect width="1920" height="1080" fill="${d ? '#2a2e2c' : '#5a605c'}"/>` + Array.from({ length: 30 }, (_, k) => `<path d="M${k * 70} 0 V1080" stroke="${d ? '#242826' : '#4e5450'}" stroke-width="4"/>`).join('');
  s += `<rect x="0" y="0" width="1920" height="90" fill="${d ? '#1a1c1c' : '#3a3e3c'}" stroke="${INK}" stroke-width="5"/>`;
  for (const x of [220, 620]) s += `<rect x="${x}" y="520" width="300" height="420" rx="30" fill="#2f5a7a" stroke="${INK}" stroke-width="7"/><rect x="${x + 40}" y="460" width="220" height="70" fill="#3a3e46" stroke="${INK}" stroke-width="6"/><path d="M${x + 150} 460 V90" stroke="#6a6e76" stroke-width="40"/><path d="M${x + 150} 460 V90" stroke="${INK}" stroke-width="4" fill="none"/>` + C(x + 150, 700, 50, '#1d2a36', 6);
  s += `<rect x="1060" y="200" width="300" height="200" fill="#e9e2cc" stroke="${INK}" stroke-width="5"/>` + T(1210, 250, 30, 'PUMP STATION 2', '#222', 900) + T(1210, 300, 22, 'MID-RIVER · 700 m', '#444', 800) + `<rect x="1100" y="330" width="90" height="40" fill="#c33a2f"/>` + T(1145, 360, 22, 'OFF', '#fff', 900);
  s += `<rect x="1460" y="320" width="320" height="640" fill="#e0702a" stroke="${INK}" stroke-width="7"/><path d="M1620 320 V960" stroke="${INK}" stroke-width="5"/>` + T(1620, 400, 30, 'EMERGENCY', '#fff', 900) + T(1620, 440, 24, 'SUPPLY', '#fff', 900) + `<rect x="1600" y="600" width="40" height="70" fill="#8a8f96" stroke="${INK}" stroke-width="4"/>`;
  s += `<rect y="1000" width="1920" height="80" fill="#1a1c1c"/>` + waterBand(860, 1080, 9, 40).replace(`<rect x="-40" y="860"`, `<rect opacity=".55" x="-40" y="860"`);
  return s; };
// Hospital station (east bank): quarantine sheeting, red emergency light, stairs up on the right
ENV.shosp = L => { const d = isSD(L); let s = `<rect width="1920" height="1080" fill="${d ? '#2e3432' : '#6a706c'}"/>` + tiles(0, 120, 1500, 880, d ? '#4a524e' : '#d8dcd4', d ? '#3e4642' : '#b8beb6');
  s += `<rect x="0" y="0" width="1920" height="120" fill="#1c1e20" stroke="${INK}" stroke-width="6"/><rect x="0" y="300" width="1500" height="40" fill="#b0302a"/><rect x="300" y="190" width="900" height="110" fill="#1f3c6a" stroke="${INK}" stroke-width="6"/>` + T(750, 266, 56, "ST. MARY'S HOSPITAL", '#fff', 900, 'middle', 'letter-spacing="4"');
  s += stains(0, 1500, 120, 51, 10);
  for (let k = 0; k < 5; k++) s += `<path d="M${60 + k * 170} 360 V990 Q${110 + k * 170} 1010 ${160 + k * 170} 990 V360Z" fill="#dfe8e4" opacity=".28" stroke="#9aa6a2" stroke-width="3"/>`;
  s += `<path d="M40 420 L900 460" stroke="#e0c020" stroke-width="26"/><path d="M40 420 L900 460" stroke="${INK}" stroke-width="3" stroke-dasharray="40 40"/>` + T(470, 452, 22, 'QUARANTINE · NO ENTRY', '#1d1d21', 900, 'middle', 'transform="rotate(2.6 470 445)"');
  s += `<rect x="1500" y="120" width="420" height="880" fill="#0e1012"/>`; for (let k = 0; k < 12; k++) s += `<rect x="${1500 + k * 34}" y="${940 - k * 64}" width="${420 - k * 34}" height="60" fill="${d ? '#3a3e3c' : '#6a6e6a'}" stroke="${INK}" stroke-width="4"/>`;
  s += `<path d="M1500 1000 L1920 230" stroke="#8a8f96" stroke-width="10"/>` + `<rect x="1540" y="130" width="340" height="70" fill="#fff4c0" opacity="${d ? .25 : .5}"/>`;
  s += `<circle cx="1380" cy="170" r="26" fill="#ff3a1a" stroke="${INK}" stroke-width="5"/>`;
  s += `<rect y="1000" width="1920" height="40" fill="${d ? '#3a3c3a' : '#8a8c88'}" stroke="${INK}" stroke-width="5"/><rect y="1030" width="1500" height="12" fill="#d8b52a"/>` + waterBand(1042, 1080, 15, 14);
  return s; };
// the ferry's remaining lifeboat on the night harbor (hull drawn in front fx)
ENV.lboat = L => { let s = wsky(L) + skyline(L, 640, .8, 63, 0) + crane(300, 690, .7, L) + `<rect y="640" width="1920" height="440" fill="${RIV(L)}"/>` + ripples(650, 1080, L, 13, 50) + ferry(1500, 760, .45, L, { lit: 0 });
  return s; };

// ===== S1E4 FX =====
function fig_hand(x, y, s, q, t, k) { const L = 130 * s * q, sw = Math.sin(t * 2 + k) * 6 * s; if (q <= 0) return '';
  return `<g transform="translate(${x} ${y})"><ellipse cx="0" cy="4" rx="${46 * s}" ry="${9 * s}" fill="none" stroke="#3a5a5e" stroke-width="${3 * s}" opacity=".8"/><path d="M0 0 L${sw} ${-L}" stroke="#a8ae9e" stroke-width="${20 * s}" stroke-linecap="round"/><path d="M0 0 L${sw} ${-L}" stroke="${INK}" stroke-width="${3 * s}" opacity=".5"/>` +
    (q > .6 ? [-16, -6, 5, 15].map((dx, i) => `<path d="M${sw + dx * s * .6} ${-L} l${dx * s * .5} ${-(26 + (i % 2) * 8) * s}" stroke="#a8ae9e" stroke-width="${8 * s}" stroke-linecap="round"/>`).join('') + `<path d="M${sw - 12 * s} ${-L + 6 * s} l${-22 * s} ${-10 * s}" stroke="#a8ae9e" stroke-width="${8 * s}" stroke-linecap="round"/>` : '') + `</g>`; }
function wHead(x, y, s, t, k, eyes = 1) { const bob = Math.sin(t * 1.3 + k) * 3 * s;
  return `<g transform="translate(${x} ${y + bob})"><circle cx="0" cy="${-18 * s}" r="${40 * s}" fill="#9aa092" stroke="${INK}" stroke-width="${5 * s}"/>` + (eyes ? `<circle cx="${-14 * s}" cy="${-26 * s}" r="${6 * s}" fill="#ff3a1a"/><circle cx="${14 * s}" cy="${-28 * s}" r="${6 * s}" fill="#ff3a1a"/>` : '') + `<path d="M${-30 * s} ${-60 * s} q20 ${10 * s} 30 0 q10 ${-8 * s} 26 ${4 * s}" stroke="#4a4e44" stroke-width="${8 * s}" fill="none"/><ellipse cx="0" cy="${8 * s}" rx="${62 * s}" ry="${20 * s}" fill="${WAT}"/><ellipse cx="0" cy="0" rx="${56 * s}" ry="${10 * s}" fill="none" stroke="#3a5a5e" stroke-width="${3 * s}"/></g>`; }
function kidSil(x, y, s, teddy = 1) { return `<g transform="translate(${x} ${y}) scale(${s})"><circle cx="0" cy="-150" r="34" fill="#050607"/><path d="M-24 -116 L24 -116 L30 -40 L-30 -40Z" fill="#050607"/><path d="M-14 -40 V0 M14 -40 V0" stroke="#050607" stroke-width="14"/><path d="M-24 -110 L-40 -60 M24 -110 L40 -70" stroke="#050607" stroke-width="12" stroke-linecap="round"/>` + (teddy ? `<circle cx="46" cy="-66" r="18" fill="#050607"/><circle cx="46" cy="-92" r="13" fill="#050607"/><circle cx="36" cy="-102" r="6" fill="#050607"/><circle cx="56" cy="-102" r="6" fill="#050607"/>` : '') + `</g>`; }
function teddyBear(x, y, s) { return `<g transform="translate(${x} ${y}) scale(${s})"><ellipse cx="0" cy="-34" rx="34" ry="38" fill="#9a6a3a" stroke="${INK}" stroke-width="5"/><circle cx="0" cy="-92" r="28" fill="#9a6a3a" stroke="${INK}" stroke-width="5"/><circle cx="-22" cy="-114" r="11" fill="#9a6a3a" stroke="${INK}" stroke-width="4"/><circle cx="22" cy="-114" r="11" fill="#9a6a3a" stroke="${INK}" stroke-width="4"/><ellipse cx="0" cy="-82" rx="12" ry="9" fill="#d8b48a"/><circle cx="-10" cy="-98" r="4" fill="${INK}"/><circle cx="10" cy="-98" r="4" fill="${INK}"/><path d="M-30 -40 l-20 20 M30 -40 l20 20" stroke="#9a6a3a" stroke-width="16" stroke-linecap="round"/><path d="M-18 -30 h36" stroke="#c33a2f" stroke-width="7"/></g>`; }
function chalkArrow(x, y, s, num, dir = 1) { return `<g transform="translate(${x} ${y}) scale(${s * dir} ${s})" opacity=".9"><path d="M-70 0 H60 M30 -30 L64 0 L30 30" stroke="#f4f4ee" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>` + (num != null ? `<text x="${x}" y="${y + 70 * s}" font-size="${56 * s}" font-weight="700" fill="#f4f4ee" text-anchor="middle" font-family="DejaVu Sans" font-style="italic" opacity=".9">${num}</text>` : ''); }
const _fxS14 = fxSVG;
fxSVG = function (shot, lt, p, t, front) { const f = shot.fx || [], E = shot.env, L = shot.light; const has = k => f.includes(k); let s = _fxS14(shot, lt, p, t, front);
  if (!front) {
    if (has('chalk')) for (const c of (shot.ch || [])) s += chalkArrow(c[0], c[1], c[2] || 1, c[3], c[4] || 1);
    if (has('drips') && E === 'splat') { for (const [x, i] of [[220, 0], [640, 1], [1060, 2], [1480, 3]]) { const yy = 130 + ((t * 420 + i * 230) % 850); s += `<path d="M${x} ${yy} v18" stroke="#9ad0e0" stroke-width="6" stroke-linecap="round"/><path d="M${x - 40} 940 h80 l-8 60 h-64z" fill="#3a6ab0" stroke="${INK}" stroke-width="5"/>`; } }
    if (has('tcharge') && E === 'stunnel') { for (let k = 0; k < 5; k++) { const f = Math.pow(.8, k + 1), x = 960 - 260 * f + k * 0, y = 470 - 690 * f; s += `<rect x="${960 - 300 * f}" y="${y}" width="${600 * f}" height="${46 * f}" fill="#5a6a3a" stroke="${INK}" stroke-width="${3 + 3 * f}"/><path d="M${960 - 300 * f} ${y + 23 * f} Q${700 - 200 * f} ${y + 140 * f} 0 ${300 + k * 30}" stroke="#c33a2f" stroke-width="${2 + 4 * f}" fill="none"/>`; if (Math.floor(t * 2 + k) % 2) s += `<circle cx="${960 + 260 * f}" cy="${y + 23 * f}" r="${4 + 8 * f}" fill="#ff2a1a"/>`; } }
    if (has('kid')) { const kx = shot.kx || 1300, ky = shot.ky || 1000, ks = shot.ks || 1; s += kidSil(kx, ky, ks, shot.ted != null ? shot.ted : 1); }
    if (has('prints') && E === 'splat') { for (let k = 0; k < 9; k++) { const x = 1600 - k * 90, y = 1010 + (k % 2) * 12; s += `<ellipse cx="${x}" cy="${y}" rx="20" ry="8" fill="#1a2224" opacity=".8"/><ellipse cx="${x - 22}" cy="${y}" rx="8" ry="6" fill="#1a2224" opacity=".8"/>`; } }
    if (has('teddy')) s += teddyBear(shot.tx || 1640, shot.ty || 1000, shot.ts || 1);
    if (has('tlights') && E === 'sentry') { for (let k = 0; k < 2; k++) { const x = 1700 + k * 120 + Math.sin(t * 1.4 + k) * 80; s += `<path d="M${1880 - k * 60} 600 L${x - 300} 1080 L${x - 60} 1080Z" fill="#fff4c0" opacity=".13"/>`; } }
    if (has('farbeam') && E === 'stunnel') { const on = shot.steady || (Math.floor(lt * 1.8) % 3 !== 0); if (on) s += `<circle cx="${960 + (shot.bx || 40)}" cy="476" r="9" fill="#fff"/><circle cx="${960 + (shot.bx || 40)}" cy="476" r="46" fill="#fff4c0" opacity=".25"/><path d="M${960 + (shot.bx || 40)} 476 L${700} 560 L${1200} 560Z" fill="#fff4c0" opacity=".07"/>`; }
  }
  if (front) {
    if (E === 'stunnel' || E === 'spump') { const wl = shot.wl || (E === 'spump' ? 930 : 900); s += `<path d="M-300 ${wl} ` + Array.from({ length: 34 }, (_, k) => `q35 ${(k % 2 ? 1 : -1) * 6} 70 0`).join(' ') + ` V1500 H-300Z" fill="${WAT}" opacity=".9" transform="translate(${Math.sin(t * 1.2) * 14} 0)"/><path d="M-300 ${wl} H2300" stroke="#3a5a5e" stroke-width="4" opacity=".7"/>`;
      for (const a of (shot.actors || [])) if (a.k !== 'inf') s += `<ellipse cx="${a.x + (a.mv || 0) * lt}" cy="${wl + 2}" rx="${70 * a.s}" ry="${10 * a.s}" fill="none" stroke="#5a7a7e" stroke-width="3" opacity=".7"/>`; }
    if (E === 'lboat') { s += `<path d="M520 960 L1400 960 Q1380 1060 1300 1070 L620 1070 Q540 1060 520 960Z" fill="#e0702a" stroke="${INK}" stroke-width="7"/><path d="M540 990 H1385" stroke="#f4f0e4" stroke-width="10"/>` + T(960, 1050, 30, 'HARBOR QUEEN · 2', '#1d1d21', 900) + `<path d="M-300 1060 ` + Array.from({ length: 34 }, (_, k) => `q35 ${(k % 2 ? 1 : -1) * 6} 70 0`).join(' ') + ` V1500 H-300Z" fill="${RIV(L)}" opacity=".92"/>`;
      if (shot.oar) { const a = Math.sin(t * 2.4) * 30; s += `<path d="M600 900 L${420 + a} 1080 M1320 900 L${1500 - a} 1080" stroke="#a07a4a" stroke-width="12" stroke-linecap="round"/>`; } }
    if (has('heads')) for (let i = 0; i < (shot.hd || []).length; i++) { const h = shot.hd[i]; if (h[3] != null && lt < h[3]) continue; s += wHead(h[0], h[1], h[2], t, i); }
    if (has('hands')) for (let i = 0; i < (shot.hn || []).length; i++) { const h = shot.hn[i], d0 = h[3] || 0, sink = shot.sink ? clamp((lt - d0) / 2.2, 0, 1) : 0; const q = shot.sink ? 1 - ease(sink) : ease(clamp((lt - d0) / 1.0, 0, 1)); s += fig_hand(h[0], h[1], h[2], q, t, i); }
    if (has('splash')) { const q = clamp(lt / 1.8, 0, 1); if (q < 1) { const x = shot.sx || 960, y = shot.sy || 900; for (let k = 0; k < 9; k++) { const a = -Math.PI * (k + 1) / 10; s += `<circle cx="${x + Math.cos(a) * 120 * q}" cy="${y + Math.sin(a) * 160 * q + 200 * q * q}" r="${10 * (1 - q) + 3}" fill="#bfe0e8" opacity="${1 - q}"/>`; } s += `<ellipse cx="${x}" cy="${y}" rx="${40 + 220 * q}" ry="${10 + 40 * q}" fill="none" stroke="#bfe0e8" stroke-width="5" opacity="${1 - q}"/>`; } }
    if (has('torch')) for (const a of (shot.actors || [])) if (a.torch) { const fl = a.f ? -1 : 1, x = a.x + (a.mv || 0) * lt + fl * 92 * a.s, y = a.y - 150 * a.s, len = 1100, ang = (a.ta || 8) * Math.PI / 180, sp = .2;
      const x1 = x + fl * len * Math.cos(ang - sp), y1 = y + len * Math.sin(ang - sp), x2 = x + fl * len * Math.cos(ang + sp), y2 = y + len * Math.sin(ang + sp);
      s += `<path d="M${x} ${y} L${x1} ${y1} L${x2} ${y2}Z" fill="#fff4c0" opacity=".16"/><path d="M${x} ${y} L${x + fl * len * .5 * Math.cos(ang)} ${y + len * .5 * Math.sin(ang) - 30} L${x + fl * len * .5 * Math.cos(ang)} ${y + len * .5 * Math.sin(ang) + 30}Z" fill="#fff8d8" opacity=".14"/><rect x="${x - (fl > 0 ? 34 : 0) * a.s}" y="${y - 10 * a.s}" width="${34 * a.s}" height="${20 * a.s}" rx="5" fill="#4a4d55" stroke="${INK}" stroke-width="3"/><circle cx="${x}" cy="${y}" r="${12 * a.s}" fill="#fff8d8"/>`; }
    if (has('tblast')) { const q = clamp(lt / 2.5, 0, 1), wy = 1080 - 560 * ease(q); s += `<rect x="-300" y="-300" width="2520" height="1680" fill="#fff4d0" opacity="${Math.max(0, .8 - q * 2)}"/><path d="M-300 ${wy} q240 -70 480 0 t480 0 t480 0 t480 0 t480 0 V1500 H-300Z" fill="#2a5a62" opacity=".95"/>` + Array.from({ length: 14 }, (_, k) => `<path d="M${-200 + k * 170} ${wy + 10 + Math.sin(t * 6 + k) * 12} q40 -30 90 -6" stroke="#e8f4f4" stroke-width="10" fill="none" stroke-linecap="round"/>`).join('') + `<path d="M-300 ${wy + 40} H2300" stroke="#bfe0e8" stroke-width="6" opacity=".6"/>`; }
  }
  return s; };

// ===== S1E4 CARDS =====
function tprofCard(c, p) { let s = `<rect width="1920" height="1080" fill="${CREAM}"/>` + T(960, 110, 54, c.title || 'THE HARBOR LINE · UNDER THE RIVER', '#222', 900, 'middle', 'letter-spacing="3"');
  s += `<path d="M120 300 H1800" stroke="#3a6ab0" stroke-width="6"/><path d="M380 300 Q960 360 1540 300 L1540 420 Q960 520 380 420Z" fill="#7ab0d8" stroke="${INK}" stroke-width="5"/>` + T(960, 360, 34, 'RIVER', '#2f5a7a', 900, 'middle', 'font-style="italic"');
  s += `<path d="M120 300 V560 L380 560 Q960 900 1540 560 L1800 560 V300" fill="none" stroke="${INK}" stroke-width="6"/>`;
  const tube = (y0) => `M200 ${y0} L400 ${y0} Q960 ${y0 + 260} 1520 ${y0} L1720 ${y0}`; s += `<path d="${tube(640)}" stroke="#8a8f96" stroke-width="90" fill="none"/><path d="${tube(640)}" stroke="${INK}" stroke-width="4" fill="none"/>`;
  const q = ease(clamp(p * 2, 0, 1)); s += `<path d="${tube(652)}" pathLength="100" stroke="#1b4a6a" stroke-width="${40 + 24 * q}" fill="none" stroke-dasharray="0 14 72 100" opacity=".9"/>`;
  s += `<rect x="150" y="560" width="160" height="60" fill="#1f3c6a"/>` + T(230, 600, 22, 'HARBOR ST', '#fff', 900) + `<rect x="1610" y="560" width="180" height="60" fill="#b0302a"/>` + T(1700, 600, 22, "ST. MARY'S", '#fff', 900);
  const lab = (x, y, a, b, col, k) => { const o = clamp(p * 5 - k, 0, 1); return `<g opacity="${o}"><path d="M${x} ${y} V${y + 80}" stroke="${col}" stroke-width="4" stroke-dasharray="10 8"/>` + T(x, y + 112, 30, a, col, 900) + T(x, y + 146, 24, b, '#444', 800) + `</g>`; };
  s += lab(470, 690, 'KNEE', '300 m', '#2f6a4a', 1) + lab(720, 740, 'WAIST · 1.1 m', '500 m', '#c9803a', 2) + lab(1010, 770, 'CHEST · 1.4 m', '700 m · PUMP ROOM', '#c33a2f', 3) + lab(1420, 700, 'KNEE', '1,100 m', '#2f6a4a', 4);
  s += T(960, 175, 34, c.note || '1.4 km · 12 °C WATER', '#c33a2f', 900, 'middle', `opacity="${clamp(p * 4 - 1.5, 0, 1)}"`);
  if (c.you != null) { const x = 200 + 1520 * c.you; s += `<circle cx="${x}" cy="${640 + 260 * 4 * (c.you) * (1 - c.you) * .9 - 10}" r="18" fill="#ffd400" stroke="${INK}" stroke-width="5"/>`; }
  return s; }
function chalkCard(c, p) { let s = tiles(0, 0, 1920, 1080, '#3a4440', '#2a3230', 90) + stains(0, 1920, 0, 61, 10);
  const q = clamp(p * 2.5, 0, 1); const ay = c.msg ? 300 + c.msg.length * 150 + 40 : 480; s += `<g opacity="${q}">` + chalkArrow(960, ay, c.msg ? 2.2 : 3.2, null, c.dir || 1) + `</g>`;
  if (c.n != null) s += `<text x="960" y="820" font-size="230" font-weight="700" fill="#f4f4ee" text-anchor="middle" font-family="DejaVu Sans" font-style="italic" opacity="${clamp(p * 3 - .6, 0, 1)}">${c.n}</text>`;
  if (c.msg) c.msg.forEach((m, i) => { s += `<text x="960" y="${300 + i * 150}" font-size="110" font-weight="700" fill="#f4f4ee" text-anchor="middle" font-family="DejaVu Sans" font-style="italic" opacity="${clamp(p * (c.msg.length + .6) - i, 0, 1)}" transform="rotate(-2 960 540)">${m}</text>`; });
  if (c.label) s += TM(960, 1020, 36, c.label, '#e9e2cc', 900, 'middle');
  return s; }
function timerCard(c, p, lt) { let s = `<rect width="1920" height="1080" fill="#0a0c10"/>` + T(960, 200, 52, c.title || 'FREEZE', '#e9e2cc', 900, 'middle', 'letter-spacing="6"');
  const v = Math.max(0, Math.round((c.from || 60) - (c.rate || 10) * lt)); s += `<text x="960" y="700" font-size="380" font-weight="900" fill="${v < 15 ? '#ff5a4a' : '#ffd56a'}" text-anchor="middle" font-family="DejaVu Sans" stroke="#000" stroke-width="10" paint-order="stroke">${c.fixed != null ? c.fixed : v}</text>`;
  if (c.label) s += T(960, 900, 44, c.label, '#9aa', 800);
  return s; }
const _cardS14 = cardSVG;
cardSVG = function (c, p, t, dur) { const lt = p * dur;
  if (c.t === 'tprof') return tprofCard(c, p);
  if (c.t === 'chalk') return chalkCard(c, p);
  if (c.t === 'timer') return timerCard(c, p, lt);
  return _cardS14(c, p, t, dur); };
