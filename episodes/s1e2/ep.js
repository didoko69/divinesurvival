// ---------- S1E2: Zombie Outbreak — I Survived 30 Days In A Water Tower ----------
// New locations (west bank water tower), Nora, new cards + fx. Loaded after main10.js.

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
