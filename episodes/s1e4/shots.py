# S1E4 — "Zombie Outbreak: 30 Days Trapped In A Flooded Subway | S1E4"
def A(k, x, y=1000, s=1, p='stand', f=0, e=None, mv=0, **kw):
    d = dict(k=k, x=x, y=y, s=s, p=p, f=f, mv=mv); d.update(kw)
    if e: d['e'] = e
    return d
Y = lambda x, y=1000, s=1, p='stand', f=0, e=None, **k: A('you', x, y, s, p, f, e, **k)
W = lambda x, y=1000, s=1, p='stand', f=0, e=None, **k: A('walt', x, y, s, p, f, e, **k)
Z = lambda x, y=1000, s=1, p='shamble', f=1, v=0, **k: A('inf', x, y, s, p, f, None, v=v, **k)
def fc(a, z=2.4, z1=None, shake=0, dx=0):
    return dict(cam=(a['x'] + dx, a['y'] - 210 * a['s'] + 40, z, z1 or z * 1.08, 0, 0, shake), actors=[a])
S = []
def V(text, env, light='brnight', cam=(960, 540, 1, 1.08, 0, 0), actors=(), fx=(), au=None, voice='nar', card=None, gap=.3, fc_=None, cuts=None, **kw):
    if fc_: cam = fc_['cam']; actors = list(fc_['actors']) + list(actors)
    d = dict(text=text, env='card' if card else env, light='' if card else light, cam=list(cam if not card else (960, 540, 1, 1, 0, 0)), actors=list(actors), fx=list(fx), card=card, au=au or {}, gap=gap, voice=voice)
    if cuts: d['cuts'] = cuts
    d.update(kw); S.append(d)
def CUT(env=None, light='brnight', cam=(960, 540, 1, 1.08, 0, 0), actors=(), fx=(), card=None, fc_=None, **kw):
    if fc_: cam = fc_['cam']; actors = list(fc_['actors']) + list(actors)
    d = dict(env='card' if card else env, light='' if card else light, cam=list(cam if not card else (960, 540, 1, 1, 0, 0)), actors=list(actors), fx=list(fx), card=card); d.update(kw); return d
def CARD(c, dur=2.0, au=None, **kw):
    d = dict(text=None, dur=dur, env='card', card=c, cam=[960, 540, 1, 1, 0, 0], actors=[], fx=[], light='', au=au or {'hit': .8, 'drop': 1}, gap=0); d.update(kw); S.append(d)
C = lambda **k: k
TW = lambda **k: dict(t='tower', **k)
ROOF = (900, 640, .7)          # standing on top of the bus in brdeck
HORDE_E = [Z(300 + i * 230, 1000 + (i % 2) * 30, .95 - (i % 3) * .05, v=i, f=i % 2) for i in range(7)]
DECK_INF = [Z(1500 + i * 120, 1000, .85, 'run', 1, v=i, mv=-260) for i in range(4)]
SUP = lambda day, rows, note=None, instant=0: C(t='sup', day=day, rows=rows, note=note, instant=instant)
wat = lambda L: ['WATER', L, ' L', 'bottle', min(10, max(1, int(L / 2)))]
food = lambda cal: ['FOOD', cal, ' cal', 'can', min(10, max(1, int(cal / 2200)))]


# ===== S1E2 additions =====
N = lambda x, y=1000, s=1, p='stand', f=0, e=None, **k: A('nora', x, y, s, p, f, e, **k)
food2 = lambda cal: ['FOOD', cal, ' cal', 'can', min(10, max(1, int(cal / 4500)))]
DAYS = lambda d: ['DAYS LEFT', d, '', 'can', min(10, max(1, d))]
CLIMBER = lambda y, **k: Z(960, y, 1.0, 'climbl', 0, v=1, **k)
CROWD_ST = [Z(250 + i * 70, 1000 + (i % 2) * 20, 1.0, 'shamble', i % 2, v=i) for i in range(6)]
TOWERL = dict(fx=['nlamp'])

# ===== S1E3 additions =====
food3 = lambda cal: ['FOOD', cal, ' cal', 'can', min(10, max(1, int(cal / 14000)))]
wat3 = lambda L: ['WATER', L, ' L', 'bottle', min(10, max(1, int(L / 80)))]
ROPE = lambda a, y, s=1.0, e='fear', **k: A(a, 960, y, s, 'climbl', 0, e, **k)
PIER = dict(fx=['pier'])

# ===== S1E4 additions =====
TY = lambda x, y=1000, s=1.0, p='hold', f=0, e='fear', **k: Y(x, y, s, p, f, e, torch=1, **k)
TW_ = lambda x, y=1000, s=1.0, p='walk', f=0, e='fear', **k: W(x, y, s, p, f, e, **k)
FAR_HEADS = [[1160, 600, .45], [1260, 640, .55], [1380, 690, .7], [1520, 740, .8], [1100, 570, .35], [1450, 650, .5]]
NEAR_HEADS = [[1120, 640, .6], [1300, 700, .8], [1500, 760, 1.0], [1700, 820, 1.15], [1240, 600, .5], [1620, 690, .75], [1420, 620, .55]]
HANDS = [[1180, 880, .9, .2], [1420, 860, .8, .6], [1650, 900, 1.0, 1.0], [520, 890, .9, 1.3], [300, 900, 1.0, 1.7], [1840, 880, .8, 2.0]]
RATIONS = lambda cal: ['FOOD', cal, ' cal', 'bar', min(10, max(1, int(cal / 9000)))]

# ================= COLD OPEN — DAY 120 =================
V("This is day one hundred and twenty.", 'stunnel', 'subdark', fc_=fc(TY(800, 1000, 1.1, 'hold', 0, 'fear', ta=6), 2.2, 2.5), fx=['torch', 'heads'], hd=FAR_HEADS[:3], au={'tension': .8, 'drip': .6, 'hit': .8}, day=120, flash='white')
V("You're waist-deep in black water, in a subway tunnel. Under the river.", 'stunnel', 'subdark', (960, 640, 1.0, 1.15, 0, 0), [TY(640, 1000, 1.0, 'hold', 0, 'fear', ta=6), W(1180, 1000, 1.0, 'walk', 1, 'fear')], fx=['torch', 'farbeam'], steady=1, au={'tension': .8, 'slosh': .6})
V("The water is twelve degrees. You stopped feeling your legs an hour ago.", 'stunnel', 'subdark', fc_=fc(TY(800, 1000, 1.1, 'hold', 0, 'sad', ta=10), 2.6, 2.8), fx=['torch'], au={'tension': .8, 'drip': .5})
V("Somewhere under this water, there are hundreds of them. Standing on the bottom. Waiting for a sound.", 'stunnel', 'subdark', (1300, 680, 1.6, 1.9, 0, 0), fx=['heads'], hd=FAR_HEADS, au={'tension': .9, 'groan': .3})
V("And Walter just slipped.", 'stunnel', 'subred', (1000, 760, 1.5, 1.7, 0, 0, 4), [W(1000, 935, 1.0, 'fallen', 1, 'fear')], fx=['splash'], sx=1000, sy=900, au={'tension': 1, 'bigsplash': 1, 'hit': 1}, flash='white', tilt=-3)
V("Behind you, pale hands rise out of the water. One. Three. Ten.", 'stunnel', 'subred', (1100, 760, 1.2, 1.4, 0, 0), [TY(700, 1000, 1.0, 'hold', 1, 'fear', ta=12)], fx=['hands', 'torch'], hn=HANDS, au={'tension': 1, 'slosh': 1, 'growl': .6, 'hb': .8})
V("Don't move, kid. Don't even breathe.", 'stunnel', 'subred', fc_=fc(W(960, 1000, 1.1, 'stand', 0, 'fear'), 2.6, 2.9), au={'tension': 1}, voice='walt', gap=.6)
V("And in two hours, the army is going to blow this tunnel apart. With you inside it.", 'stunnel', 'subred', (960, 300, 1.8, 2.1, 0, 0), fx=['tcharge'], au={'tension': 1, 'tick': .8})
V("Thirty days ago, a child told you to go under the river. So you did.", 'stunnel', 'subred', fc_=fc(TY(800, 1000, 1.1, 'hold', 0, 'fear', ta=6), 2.6, 3.1, shake=2), fx=['torch'], au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=1.0)
CARD(C(t='title', a='30 DAYS EARLIER'), 2.0, {'hit': .8, 'drop': 1, 'rewind': 1}, flash='white')

# ================= DAY 90: OFF THE SHIP =================
V("Day ninety. Nine p.m. The car deck door is open. And forty-one of them are coming up the stairs.", 'fcar', 'bred', (1050, 600, 1.4, 1.7, 0, 0, 2), fx=['chainopen', 'ajar'], wide=4, eyes=1, eyey=[440, 600, 760], au={'tension': 1, 'groan': 1, 'stepsmany': 1}, day=90)
V("Walter slams the stairwell door and jams the fire axe through the handles.", 'fcar', 'bred', (700, 760, 1.6, 1.8, 0, 0, 3), [W(700, 1000, 1.0, 'push', 0, 'fear')], au={'tension': 1, 'slam': 1, 'doorhits': 1}, flash='red')
V("There's one way off this ship. The second lifeboat.", 'harbor', 'brnight', (1250, 680, 2.6, 2.9, 0, 0), fx=['pier'], gn=.6, au={'tension': .9, 'water': .6})
V("Nora pulls the release. The boat drops four meters and hits the water like a car crash.", 'lboat', 'brnight', (960, 860, 1.4, 1.6, 0, 0, 5), [Y(760, 1000, 1.0, 'sit', 0, 'fear'), W(960, 1000, 1.0, 'sit', 0, 'fear'), N(1160, 1000, 1.0, 'sit', 1, 'fear')], au={'tension': 1, 'bigsplash': 1, 'hit': 1}, flash='white', tilt=3)
V("Rule five. No lights. No voices. You row.", 'lboat', 'brnight', (960, 860, 1.3, 1.45, 0, 0), [Y(760, 1000, 1.0, 'sit', 0, 'det'), W(960, 1000, 1.0, 'sit', 0, 'det'), N(1160, 1000, 1.0, 'sit', 1, 'det')], oar=1, au={'tension': .8, 'water': 1})
V("On the pier, five hundred of them are wading toward the ferry. Not toward you.", 'harbor', 'bred', (800, 760, 1.6, 1.9, 0, 0), fx=['pier', 'wade'], gn=1, au={'tension': 1, 'water': 1, 'groan': .8})
V("Go under the river. There's only one thing in Harbor City that goes under the river. The Harbor Line.", 'lboat', 'brnight', fc_=fc(N(1160, 1000, 1.0, 'sit', 1, 'det'), 2.4, 2.7), oar=1, au={'tension': .7, 'water': .6}, voice='nora')
V("Two hundred meters of rowing. Then thirty steps down. Into the dark.", 'sentry', 'brnight', (960, 860, 1.2, 1.4, 0, 0), [Y(820, 1000, .9, 'walk', 0, 'fear', mv=60), N(1060, 1000, .9, 'walk', 1, 'fear', mv=-40), W(1300, 1000, .9, 'limp', 1, 'det', mv=-80)], au={'tension': .8, 'stepssoft': 1})
V("Behind you, searchlights sweep the quay. You don't look back.", 'sentry', 'brnight', (1200, 760, 1.3, 1.5, 0, 0), fx=['tlights'], au={'tension': 1, 'helicopterfar': 1, 'drop_after': 1}, gap=.8)
CARD(C(t='day', n=91), 1.6)

# ================= DAY 91: HARBOR STREET STATION =================
V("Day ninety-one. Harbor Street station.", 'splat', 'sub', (900, 600, 1.0, 1.12, 0, 0), [W(820, 1000, 1.0, 'stand', 0, 'det'), Y(1000, 1000, 1.0, 'stand', 0, 'fear'), N(1180, 1000, 1.0, 'stand', 1, 'det')], au={'tension': .6, 'drip': .8, 'hum': .3}, day=91)
V("The power is dead. The escalators are dead. And the tracks are gone, under black water.", 'stunnel', 'sub', (960, 640, 1.0, 1.15, 0, 0), au={'tension': .7, 'drip': .6, 'slosh': .4})
V("When the river got in, it flooded the whole line. From here, all the way to the east bank.", 'card', card=C(t='tprof'), au={'tension': .6, 'pops': 1})
V("On the last track, a train sits with its doors shut. Car four is dry, empty, and it still locks from the inside.", 'scar', 'sub', (960, 640, 1.1, 1.2, 0, 0), [Y(700, 1000, 1.0, 'walk', 0, 'det', mv=60), N(1200, 1000, 1.0, 'stand', 1, 'soft')], au={'tension': .4, 'doorslide': 1})
V("Home, sweet home.", 'scar', 'sub', fc_=fc(W(960, 1000, 1.0, 'sit', 0, 'soft'), 2.5, 2.7), au={'tension': .3}, voice='walt', gap=.5)
V("First problem: water. Which is funny, because you're surrounded by it.", 'card', card=C(t='prob', n=1, icon='drop', a='WATER', b='Water everywhere. None to drink.'), au={'tension': .6, 'hit': .6})
V("But the water in the tunnel is river, sewage, and them. You don't drink that. Not even with bleach.", 'splat', 'sub', (1400, 980, 2.2, 2.5, 0, 0), fx=['heads'], hd=[[1500, 1068, .5]], au={'tension': .8, 'slosh': .5})
V("So you listen. Drip. Drip. Drip.", 'splat', 'sub', (640, 500, 1.6, 1.8, 0, 0), fx=['drips'], au={'tension': .4, 'drip': 1})
V("The ceiling is leaking. Rainwater, soaking down from the street through three meters of soil.", 'splat', 'sub', (900, 560, 1.1, 1.25, 0, -80), [N(640, 1000, 1.0, 'lookup', 0, 'det'), Y(1060, 1000, 1.0, 'lookup', 1, 'det')], fx=['drips'], au={'tension': .4, 'drip': 1})
V("Nora does the math.", 'card', card=C(t='math', title='THE LEAKS', lines=['1 drop ≈ 0.05 mL', '1 drop a second = 4.3 L a day', ['4 leaks = 17 L a day', '#2f6a4a', 96]]), au={'tension': .4, 'pops': 1})
V("One drop a second is four liters a day. Four leaks, seventeen liters. Three people need nine.", 'splat', 'sub', fc_=fc(N(640, 1000, 1.0, 'point', 0, 'det'), 2.3, 2.5), fx=['drips'], au={'tension': .4, 'drip': .6})
V("And Nora still has half a liter of bleach. That's ten thousand drops. At two drops per liter, five thousand liters of clean water.", 'card', card=C(t='math', title='THE BLEACH', lines=['0.5 L bleach ≈ 10,000 drops', '2 drops per liter · 30 min', ['= 5,000 L', '#2f6a4a', 110]]), au={'tension': .3, 'pops': 1})
V("Rule one survives the river.", 'card', card=SUP(91, [wat3(40), DAYS(30)], '+17 L A DAY', 1), au={'tension': .3, 'pops': 1})
V("Second problem: food. Your last can of soup was three days ago.", 'card', card=C(t='prob', n=2, icon='can', a='FOOD', b='Day 3 with nothing'), au={'tension': .7, 'hit': .6})
V("Walter opens the vending machines with the fire axe. One swing each.", 'splat', 'sub', (420, 760, 1.4, 1.55, 0, 0), [W(560, 1000, 1.0, 'lift', 1, 'det'), Y(860, 1000, 1.0, 'stand', 1, 'fear')], au={'tension': .7, 'glass': 1, 'hit': 1}, flash='white')
V("Ninety-six snacks. Forty-eight drinks. And at the newsstand, forty chocolate bars.", 'card', card=C(t='loot', title='HARBOR STREET · DAY 91', items=[['bar', '96 snacks'], ['bottle', '48 drinks'], ['bar', '40 chocolate bars'], ['cracker', 'crackers']]), au={'tension': .4, 'pops': 1})
V("About thirty thousand calories.", 'card', card=SUP(91, [food3(30000), DAYS(8)], '3 × 1,200 = 3,600 CAL A DAY', 1), au={'tension': .5, 'pops': 1})
V("Twelve hundred calories a day each. Eight days. Then nothing.", 'scar', 'sub', fc_=fc(Y(900, 1000, 1.0, 'sit', 0, 'sad'), 2.4, 2.6), au={'tension': .5, 'sad': .4}, gap=.8)
CARD(C(t='day', n=93), 1.6)

# ================= DAY 93: THEM =================
V("Third problem: them.", 'card', card=C(t='prob', n=3, icon='ear', a='THEM', b='Under the water'), au={'tension': .8, 'hit': 1}, flash='white')
V("Day ninety-three. You haven't seen a single one since you came down here. Walter doesn't like that.", 'splat', 'sub', (1300, 800, 1.4, 1.6, 0, 0), [W(1400, 1000, 1.0, 'stand', 0, 'det'), Y(1100, 1000, 1.0, 'stand', 0, 'fear')], au={'tension': .7, 'drip': .5}, day=93)
V("He throws an empty can into the tunnel. Ten meters out.", 'stunnel', 'sub', (960, 600, 1.2, 1.35, 0, 0), fx=['splash'], sx=980, sy=600, au={'tension': .8, 'splash': 1})
V("Eight seconds. Nothing. Then the water starts to move.", 'stunnel', 'sub', (960, 620, 1.6, 1.8, 0, 0), au={'tension': 1, 'slosh': .8, 'hb': .7})
V("Six hands come up out of the water. Right where the can went in.", 'stunnel', 'subred', (960, 600, 1.7, 1.9, 0, 0), fx=['hands'], hn=[[900, 610, .4, .1], [960, 600, .35, .4], [1020, 615, .42, .7], [940, 640, .5, 1.0], [1060, 650, .5, 1.2], [880, 660, .55, 1.5]], au={'tension': 1, 'slosh': 1, 'growl': .5})
V("They're not swimming. They're standing on the bottom, two meters down. And they heard it.", 'stunnel', 'subred', (1200, 660, 1.5, 1.7, 0, 0), fx=['heads'], hd=FAR_HEADS, au={'tension': 1, 'groan': .5})
V("They don't need to breathe. They just wait in the cold, for a sound.", 'splat', 'sub', fc_=fc(W(1400, 1000, 1.0, 'stand', 0, 'fear'), 2.4, 2.7), au={'tension': .9})
V("Rule number seven: don't splash. Slide your feet. Never lift them out of the water.", 'card', card=C(t='rule', n=7, icon='ear', a="DON'T SPLASH", b='Slide your feet. Never lift them.'), au={'tension': .7, 'hit': .6})
V("Rule number eight: if a hand comes up, freeze. And count to sixty.", 'card', card=C(t='rule', n=8, icon='skull', a='FREEZE. COUNT TO 60.', b='If a hand comes up, nobody moves'), au={'tension': .7, 'hit': .6})
V("That night you sleep in car four. Nobody talks above a whisper.", 'scar', 'subdark', (960, 860, 1.4, 1.55, 0, 0), [Y(700, 1000, 1.0, 'sleep', 0, 'soft'), N(1000, 1000, 1.0, 'sit', 0, 'soft'), W(1260, 1000, 1.0, 'sleep', 1, 'soft')], au={'tension': .4, 'drip': .4}, gap=.8)
CARD(C(t='day', n=96), 1.6)

# ================= DAY 96: THE CHALK (MYSTERY) =================
V("Day ninety-six. Nora wakes you at six.", 'scar', 'sub', (960, 800, 1.4, 1.55, 0, 0), [Y(800, 1000, 1.0, 'sit', 0, 'fear'), N(1100, 1000, 1.0, 'stand', 1, 'fear')], au={'tension': .6, 'whisper': 1}, day=96)
V("On the tile wall, right next to the tunnel, someone has drawn something in chalk.", 'splat', 'sub', (1400, 600, 1.6, 1.8, 0, 0), fx=['chalk'], ch=[[1460, 500, 1.0, '100']], au={'tension': .8, 'mystery': 1})
V("An arrow, pointing into the tunnel. And a number. One hundred.", 'card', card=C(t='chalk', n=100, label='HARBOR STREET · DAY 96'), au={'tension': .8, 'mystery': 1, 'chalk': 1})
V("It wasn't there last night. I was awake until three.", 'splat', 'sub', fc_=fc(N(1200, 1000, 1.0, 'stand', 0, 'fear'), 2.4, 2.7), fx=['chalk'], ch=[[1460, 500, 1.0, '100']], au={'tension': .8}, voice='nora', gap=.5)
V("The chalk is still wet.", 'splat', 'sub', (1460, 520, 3.0, 3.3, 0, 0), fx=['chalk'], ch=[[1460, 500, 1.0, '100']], au={'tension': .9, 'drip': .6})
V("Nobody came down the stairs. You'd have heard. Whoever drew this came out of the water.", 'splat', 'sub', fc_=fc(Y(1000, 1000, 1.0, 'stand', 0, 'fear'), 2.5, 2.9), au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=.8)
CARD(C(t='day', n=99), 1.6)

# ================= DAY 99: INTO THE WATER =================
V("Day ninety-nine. The last chocolate bar, split three ways.", 'scar', 'sub', (960, 860, 1.4, 1.5, 0, 0), [Y(700, 1000, 1.0, 'sit', 0, 'sad'), W(960, 1000, 1.0, 'sit', 0, 'sad'), N(1220, 1000, 1.0, 'sit', 1, 'sad')], au={'tension': .6, 'sad': .6}, day=99)
V("Halfway under the river, the line map shows a little box. Pump Station Two.", 'card', card=C(t='tprof', note='PUMP STATION 2 · 700 m'), au={'tension': .6, 'pops': 1})
V("Pump rooms have emergency lockers. For crews who get trapped down here. Like us.", 'scar', 'sub', fc_=fc(W(960, 1000, 1.0, 'sit', 0, 'det'), 2.4, 2.6), au={'tension': .5}, voice='walt', gap=.5)
V("Seven hundred meters into the water, at the deepest point. Walter's ankle can't take the cold yet. So it's you.", 'splat', 'subdark', fc_=fc(Y(1100, 1000, 1.0, 'stand', 0, 'det'), 2.4, 2.6), au={'tension': .7})
V("Four a.m. You step down off the platform. Rule seven.", 'stunnel', 'subdark', (800, 700, 1.3, 1.45, 0, 0), [TY(700, 1000, 1.0, 'hold', 0, 'fear', ta=12)], fx=['torch'], wl=960, au={'tension': .9, 'slosh': .6})
V("Knee-deep. Then thigh-deep. Then the cold reaches your stomach, and your breath just stops.", 'stunnel', 'subdark', fc_=fc(TY(800, 1000, 1.1, 'hold', 0, 'fear', ta=10), 2.4, 2.6), fx=['torch'], au={'tension': .9, 'slosh': .5, 'breath': 1})
V("A hundred meters in, your light finds the next arrow. And the arrow points at the wall.", 'stunnel', 'subdark', (500, 600, 1.6, 1.8, 0, 0), fx=['chalk'], ch=[[420, 560, 1.0, '200', -1]], au={'tension': .8, 'mystery': .8})
V("You slide your foot over. There's a ledge under the water. The maintenance walkway, seventy centimeters above the tracks.", 'stunnel', 'subdark', (700, 760, 1.4, 1.55, 0, 0), [TY(560, 1000, 1.0, 'walk', 0, 'det', ta=14)], fx=['torch'], wl=960, au={'tension': .7, 'slosh': .5})
V("On the walkway, the water only reaches your knees. And there's nobody on it.", 'stunnel', 'subdark', (960, 700, 1.2, 1.35, 0, 0), [TY(560, 1000, 1.0, 'walk', 0, 'det', ta=10, mv=40)], fx=['torch'], wl=960, au={'tension': .6, 'slosh': .4})
V("Someone is showing you the way.", 'stunnel', 'subdark', fc_=fc(TY(800, 1000, 1.1, 'hold', 0, 'fear', ta=8), 2.6, 2.8), fx=['torch'], wl=960, au={'tension': .8, 'mystery': 1})
V("Every hundred meters, another arrow. Three hundred. Four hundred. Five hundred.", 'stunnel', 'subdark', (500, 560, 1.4, 1.6, 0, 0), fx=['chalk'], ch=[[260, 620, 1.2, '300'], [560, 540, .8, '400'], [760, 500, .55, '500']], au={'tension': .7, 'slosh': .4})
V("At five hundred meters, your flashlight finds them.", 'stunnel', 'subdark', (1300, 680, 1.4, 1.7, 0, 0), fx=['heads'], hd=NEAR_HEADS, au={'tension': 1, 'hit': .7, 'hb': .8}, flash='red')
V("Thirty of them, standing in the deep water by the rails. Up to their eyes. Not moving.", 'stunnel', 'subdark', (1400, 720, 2.0, 2.3, 0, 0), fx=['heads'], hd=NEAR_HEADS, au={'tension': 1, 'groan': .3, 'hb': .7})
V("You slide past them, a meter and a half away. Your heart is the loudest thing in the tunnel.", 'stunnel', 'subdark', (960, 700, 1.1, 1.25, 0, 0), [TY(560, 1000, 1.0, 'walk', 0, 'fear', ta=4, mv=50)], fx=['torch', 'heads'], hd=NEAR_HEADS, wl=960, au={'tension': 1, 'hb': 1, 'slosh': .4})
V("Seven hundred meters. Pump Station Two.", 'spump', 'sub', (960, 600, 1.0, 1.12, 0, 0), [TY(600, 1000, 1.0, 'hold', 0, 'det', ta=-10)], fx=['torch'], au={'tension': .6, 'drip': .8})
V("The locker is orange. And it opens.", 'spump', 'sub', (1500, 700, 1.4, 1.6, 0, 0), [Y(1340, 1000, 1.0, 'pull', 1, 'det')], au={'tension': .5, 'unlock': 1, 'creak': 1})
V("Twenty-four emergency ration packs. Thirty-six hundred calories each. Batteries. A first-aid kit.", 'card', card=C(t='loot', title='PUMP STATION 2 · LOCKER', items=[['bar', '24 ration packs'], ['bar', '3,600 cal each'], ['bottle', 'batteries'], ['can', 'first-aid kit']]), au={'tension': .3, 'pops': 1})
V("Eighty-six thousand calories. Enough to get the three of you to day one hundred and twenty-three.", 'card', card=SUP(99, [RATIONS(86400), DAYS(24)], '3 × 1,200 = 3,600 CAL A DAY', 1), au={'tension': .3, 'pops': 1})
V("Then you read the pump log on the wall. The last entry is from day two.", 'card', card=C(t='log', title='PUMP STATION 2 · LOG', lines=['Day 1 - 3 of 3 pumps running.', 'Day 2 - MILITARY ORDER: ALL PUMPS OFF.', 'Day 2 - "Flood the Harbor Line."', 'Day 2 - "East bank must not reach west."', 'Day 2 - Crew out. Water rising 40 cm/h.'], red=[1, 3]), au={'tension': .8, 'paper': 1, 'mystery': 1})
V("They didn't lose this tunnel. They drowned it. On purpose.", 'spump', 'sub', fc_=fc(Y(900, 1000, 1.0, 'stand', 0, 'fear'), 2.4, 2.7), au={'tension': .9, 'mystery': 1})
V("On the way back, there's a new arrow on the wall. Drawn after you passed. And it points the other way. East.", 'stunnel', 'subdark', (500, 600, 1.6, 1.8, 0, 0), fx=['chalk'], ch=[[440, 580, 1.1, None, -1]], au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=.8)
CARD(C(t='day', n=105), 1.6)

# ================= DAY 105: THE RADIO =================
V("Day one hundred and five. Nora gets her radio working, with batteries from the locker.", 'scar', 'sub', (960, 800, 1.4, 1.55, 0, 0), [N(960, 1000, 1.0, 'sit', 0, 'det'), Y(700, 1000, 1.0, 'sit', 0, 'det'), W(1220, 1000, 1.0, 'sit', 1, 'det')], au={'tension': .5, 'static': .6}, day=105)
V("The same military channel. Every night at midnight.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY'), au={'tension': .8, 'static': 1})
V("Harbor Line closure confirmed. Charges in place, mid-river section. Detonation, day one two one. Zero six hundred.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY'), au={'tension': 1, 'static': .8}, voice='radio', gap=.4)
V("East bank asset still not recovered. Nobody crosses.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY'), au={'tension': 1, 'static': .8}, voice='radio', gap=.6)
V("Day one twenty-one. Six in the morning. They're going to drop the river into this tunnel.", 'scar', 'sub', fc_=fc(W(1220, 1000, 1.0, 'sit', 1, 'det'), 2.5, 2.8), au={'tension': .9}, voice='walt', gap=.8)
CARD(C(t='day', n=112), 1.6)

# ================= DAY 112: THE CHARGES =================
V("Day one hundred and twelve. Walter's ankle can take the cold now. He goes in with you.", 'stunnel', 'subdark', (960, 700, 1.1, 1.25, 0, 0), [TY(560, 1000, 1.0, 'walk', 0, 'det', ta=10, mv=30), W(1000, 1000, 1.0, 'walk', 0, 'det', mv=30)], fx=['torch'], wl=960, au={'tension': .7, 'slosh': .5}, day=112)
V("At the pump station, he points his light at the ceiling.", 'stunnel', 'subdark', (960, 500, 1.2, 1.5, 0, -150), fx=['tcharge'], au={'tension': .9})
V("Sixteen charges. Taped to the roof of the tunnel, right under the riverbed.", 'stunnel', 'subred', (960, 280, 1.8, 2.0, 0, 0), fx=['tcharge'], au={'tension': 1, 'beep': 1})
V("Walter reads them the way you'd read a menu.", 'card', card=C(t='math', title='THE CHARGES', lines=['16 charges · under the riverbed', 'radio receiver · no timer to cut', ['DAY 121 · 06:00', '#c33a2f', 110]]), au={'tension': .9, 'pops': 1})
V("Nine years in the army, kid. I've set charges like these. You don't touch a remote one you didn't wire yourself.", 'stunnel', 'subred', fc_=fc(W(1000, 1000, 1.0, 'stand', 0, 'det'), 2.5, 2.8), au={'tension': .9}, voice='walt', gap=.5)
V("Behind you, a harbor full of soldiers. In front of you, the hospital where all of this started.", 'card', card=C(t='tprof', note='WEST: SOLDIERS  ·  EAST: THE HOSPITAL'), au={'tension': .9, 'mystery': .8})
V("And the arrows only point one way.", 'card', card=C(t='chalk', label='1,400 m · EAST'), au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=.8)
CARD(C(t='day', n=118), 1.6)

# ================= DAY 118: THE LIGHT IN THE TUNNEL =================
V("Day one hundred and eighteen. Three a.m. You can't sleep. You sit at the edge of the platform, with the light off.", 'splat', 'subdark', (1300, 820, 1.4, 1.6, 0, 0), [Y(1300, 1000, 1.0, 'sit', 0, 'sad')], au={'tension': .6, 'drip': .6}, day=118)
V("Then, far down the tunnel, a light.", 'stunnel', 'subdark', (960, 480, 2.0, 2.4, 0, 0), fx=['farbeam'], bx=60, au={'tension': .9, 'mystery': 1})
V("Small. Low over the water. Moving toward you.", 'stunnel', 'subdark', (980, 500, 2.4, 2.8, 0, 0), fx=['farbeam'], bx=30, steady=1, au={'tension': 1, 'slosh': .3, 'hb': .6})
V("It stops at the wall. And for a few seconds, something small stands in the light, drawing on the tiles.", 'stunnel', 'subdark', (1000, 540, 2.4, 2.7, 0, 0), fx=['farbeam', 'kid'], bx=50, steady=1, kx=1010, ky=590, ks=.5, au={'tension': 1, 'chalk': 1, 'mystery': 1})
V("Then the light goes out.", 'stunnel', 'subdark', (1000, 520, 2.9, 3.0, 0, 0), au={'tension': 1, 'silence': 1}, gap=.6)
V("In the morning, there are footprints on the platform. Wet. Small. A child's shoes.", 'splat', 'sub', (1300, 980, 2.2, 2.5, -100, 0), fx=['prints'], au={'tension': .9, 'mystery': 1})
V("And a new arrow on the wall. No number this time. Just two lines.", 'card', card=C(t='chalk', msg=['DAY 120', '4 AM']), au={'tension': 1, 'chalk': 1, 'hit': .6})
V("Two hours before the blast. The kid knows when the soldiers come. The kid always knows.", 'splat', 'sub', fc_=fc(N(1100, 1000, 1.0, 'stand', 1, 'fear'), 2.4, 2.7), au={'tension': .9}, voice='nora', gap=.8)
CARD(C(t='day', n=120), 1.8, {'hit': 1, 'drop': 1}, flash='red')

# ================= DAY 120: BACK TO TONIGHT =================
V("Which brings you back to tonight. Four a.m. Day one hundred and twenty.", 'stunnel', 'subdark', (960, 640, 1.0, 1.1, 0, 0), [N(1300, 1000, .8, 'walk', 0, 'fear'), TY(700, 1000, 1.0, 'walk', 0, 'fear', ta=6), W(400, 1000, 1.05, 'walk', 0, 'fear')], fx=['torch'], au={'tension': .8, 'slosh': .5}, day=120)
V("Fourteen hundred meters. Sliding your feet, you make about a kilometer an hour.", 'card', card=C(t='math', title='THE CROSSING', lines=['1,400 m', '÷ 1 km an hour', ['= 84 minutes in 12 °C water', '#c33a2f', 80]]), au={'tension': .7, 'pops': 1})
V("Nora goes first. She's the lightest, and the quietest. Then you. Then Walter.", 'stunnel', 'subdark', (960, 700, 1.2, 1.3, 0, 0), [N(1300, 1000, .8, 'walk', 0, 'det', mv=30), TY(760, 1000, 1.0, 'walk', 0, 'det', ta=6, mv=30), W(420, 1000, 1.05, 'walk', 0, 'det', mv=30)], fx=['torch'], au={'tension': .8, 'slosh': .5})
V("Five hundred meters. Past the thirty in the deep water. Nobody breathes.", 'stunnel', 'subdark', (1100, 700, 1.3, 1.45, 0, 0), [TY(640, 1000, 1.0, 'walk', 0, 'fear', ta=4, mv=30)], fx=['torch', 'heads'], hd=NEAR_HEADS, au={'tension': 1, 'hb': 1})
V("Then Walter's bad ankle finds a gap in the walkway. And he goes under.", 'stunnel', 'subred', (1000, 760, 1.5, 1.7, 0, 0, 4), [W(1000, 935, 1.0, 'fallen', 1, 'fear')], fx=['splash'], sx=1000, sy=900, au={'tension': 1, 'bigsplash': 1, 'hit': 1}, flash='white')
V("Rule eight. You freeze.", 'stunnel', 'subred', (1100, 760, 1.2, 1.4, 0, 0), [TY(700, 1000, 1.0, 'hold', 1, 'fear', ta=12)], fx=['hands', 'torch'], hn=HANDS, au={'tension': 1, 'slosh': 1, 'growl': .6})
V("Sixty seconds. Twelve hands out of the water around you. One so close, the water from its fingers drips onto your sleeve.", 'card', card=C(t='timer', title='FREEZE · COUNT TO 60', from_=60, fixed=60, label='DAY 120 · 04:51'), au={'tension': 1, 'tick': 1, 'hb': 1})
V("Forty. Thirty. Ten.", 'card', card=C(t='timer', title='FREEZE · COUNT TO 60', **{'from': 40, 'rate': 14}), au={'tension': 1, 'tick': 1, 'hb': 1})
V("And one by one, the hands sink back under.", 'stunnel', 'subred', (1100, 760, 1.2, 1.35, 0, 0), [TY(700, 1000, 1.0, 'hold', 1, 'fear', ta=12)], fx=['hands', 'torch'], hn=[[h[0], h[1], h[2], h[3] * .6] for h in HANDS], sink=1, au={'tension': .9, 'slosh': .6})
V("Walter comes up without a sound. Soaked to the cap.", 'stunnel', 'subdark', fc_=fc(W(1000, 1000, 1.0, 'stand', 0, 'sad'), 2.5, 2.7), au={'tension': .7, 'drip': .6})
V("Kid. When we get out of here, I'm buying the first round.", 'stunnel', 'subdark', fc_=fc(W(1000, 1000, 1.0, 'stand', 0, 'soft'), 2.7, 2.9), au={'tension': .5}, voice='walt', gap=.5)
V("Eleven hundred meters. The water drops to your knees. Then your ankles.", 'stunnel', 'subdark', (960, 700, 1.1, 1.25, 0, 0), [N(1300, 1000, .8, 'walk', 0, 'det', mv=40), TY(760, 1000, 1.0, 'walk', 0, 'det', ta=6, mv=40), W(420, 1000, 1.05, 'limp', 0, 'det', mv=40)], fx=['torch'], wl=990, au={'tension': .7, 'slosh': .4})
V("Five fifty-eight a.m. Nora pulls you both up onto a platform you've never seen before.", 'shosp', 'sub', (960, 700, 1.0, 1.12, 0, 0), [N(1000, 1000, 1.0, 'pull', 1, 'det'), Y(760, 1000, 1.0, 'crouch', 0, 'fear'), W(520, 1000, 1.0, 'kneel', 0, 'sad')], au={'tension': .8, 'strain': 1, 'tick': .6})
V("Two minutes later, the army keeps its promise.", 'shosp', 'subred', (960, 640, 1.1, 1.3, 0, 0, 8), [Y(760, 1000, 1.0, 'crouch', 0, 'fear'), N(1000, 1000, 1.0, 'crouch', 1, 'fear'), W(520, 1000, 1.0, 'crouch', 0, 'fear')], au={'tension': 1, 'explode': 1, 'rumble': 1, 'hit': 1}, flash='white', tilt=-3)
V("Behind you, the river pours into the tunnel. The way back is gone.", 'stunnel', 'subred', (960, 540, 1.0, 1.2, 0, 0, 6), fx=['tblast'], au={'tension': 1, 'water': 1, 'rumble': 1})
V("When the dust settles, you look up at the sign. Saint Mary's Hospital.", 'shosp', 'sub', (750, 300, 1.8, 2.0, 0, 0), au={'tension': .8, 'mystery': 1, 'drip': .5})
V("Quarantine sheets hang from the ceiling like curtains. Nothing moves behind them.", 'shosp', 'sub', (500, 640, 1.3, 1.45, 0, 0), au={'tension': .9, 'hum': .4})
V("On the bottom step of the stairs, someone has left a teddy bear. Sitting up. Waiting.", 'shosp', 'sub', (1620, 900, 2.4, 2.6, 0, 0), fx=['teddy'], tx=1620, ty=1000, ts=.9, au={'tension': .9, 'mystery': 1})
V("Next to it, in chalk.", 'shosp', 'sub', (1500, 760, 1.8, 2.0, 0, 0), fx=['teddy', 'chalk'], tx=1620, ty=1000, ts=.9, ch=[[1380, 760, .9, None, 1]], au={'tension': .9, 'chalk': 1})
V("I'm sorry about the horn. Come up.", 'card', card=C(t='chalk', msg=["I'M SORRY", 'ABOUT THE HORN.', 'COME UP.']), au={'tension': 1, 'mystery': 1})
V("Then every light in the station comes on. Somebody up there has power.", 'shosp', 'brday', (960, 600, 1.0, 1.1, 0, 0), [Y(760, 1000, 1.0, 'stand', 0, 'fear'), N(1000, 1000, 1.0, 'stand', 1, 'fear'), W(520, 1000, 1.0, 'stand', 0, 'fear')], fx=['teddy'], tx=1620, ty=1000, ts=.9, au={'tension': 1, 'switch': 1, 'hum': 1, 'hit': .8}, flash='white')
V("And at the top of the stairs, small, holding something under one arm, a silhouette.", 'shosp', 'brday', (1720, 300, 2.2, 2.6, 0, 0), fx=['kid'], kx=1720, ky=212, ks=.5, au={'tension': 1, 'riser': 1, 'sting': 1})
V("Kid. Whatever is up there, it's the reason they blew up a river.", 'shosp', 'brday', fc_=fc(W(520, 1000, 1.0, 'stand', 0, 'fear'), 2.6, 3.0), au={'tension': 1, 'drop_after': 1}, voice='walt', gap=1.2)
CARD(C(t='blackend'), 1.4, {'silence': 1})
V("To be continued. Day one hundred and fifty. The Hospital Where It Started.", 'card', card=C(t='title', a='S1E5 · THE HOSPITAL'), au={'tension': .5, 'mystery': 1})
V("Who do you think the kid is? And would you have followed the arrows? Tell me in the comments. And subscribe, so you're here when the stairs go up.", 'card', card=C(t='chalk', msg=['COME UP.']), au={'tension': .4, 'mystery': .8, 'endtail5': 1}, gap=1.4)
CARD(C(t='blackend'), 2.5, {'silence': 1, 'tension': .2})
