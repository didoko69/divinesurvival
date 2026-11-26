# S1E3 — "Zombie Outbreak: Nobody Answered The Ferry Horn | S1E3"
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

# ================= COLD OPEN — DAY 90 =================
V("This is day ninety.", 'fwheel', 'brnight', (1150, 800, 1.8, 2.0, 0, 0), [Y(1150, 1000, 1.1, 'stand', 1, 'fear')], fx=['vign'], au={'tension': .7, 'ocean': .6, 'hit': .8}, day=90, flash='white')
V("You're in the wheelhouse of a ferry, anchored a hundred and fifty meters off the harbor pier.", 'harbor', 'brnight', (1300, 640, 1.9, 1.5, -200, 80), fx=['pier'], gn=.5, au={'tension': .7, 'ocean': .8, 'groan': .3})
V("It's nine o'clock at night. And nobody is touching the horn.", 'fwheel', 'brnight', (1420, 600, 2.6, 3.0, 0, 0), au={'tension': .9, 'silence': .6})
V("But it's blowing anyway.", 'card', card=C(t='horn', n=3, label='DAY 90 · 21:00'), au={'tension': 1, 'horn': 3, 'hit': .8})
V("Three blasts. The loudest sound in Harbor City.", 'fdeck', 'brnight', (1600, 300, 2.2, 2.6, 0, 0), fx=['swing'], au={'tension': 1, 'horn': 1, 'wind': .6})
V("On the pier, every head turns toward the ship.", 'harbor', 'bred', (420, 700, 2.0, 2.3, 0, 0, 2), fx=['pier'], gn=1, au={'tension': 1, 'groan': 1, 'growl': .8}, tilt=-2)
V("Five hundred of them. And they're walking into the water.", 'harbor', 'bred', (800, 760, 1.6, 1.9, 0, 0), fx=['pier', 'wade'], gn=1, au={'tension': 1, 'water': 1, 'groan': .8})
V("Kid. Nobody on this ship pulls that cord but us. So who's pulling it?", 'fwheel', 'brnight', fc_=fc(W(800, 1000, 1.1, 'stand', 0, 'fear'), 2.5, 2.8), au={'tension': 1}, voice='walt', gap=.6)
V("And somewhere below your feet, something made of metal hits the deck.", 'fcar', 'brnight', (960, 700, 1.3, 1.6, 0, 0, 2), fx=['chain'], rattle=1, au={'tension': 1, 'chainclink': 1, 'thud': 1})
V("Thirty days ago, this ferry looked like the way out. Tonight, it might be a trap.", 'fwheel', 'bred', fc_=fc(Y(1100, 1000, 1.1, 'stand', 1, 'fear'), 2.5, 3.0, shake=2), fx=['vign'], au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=1.0)
CARD(C(t='title', a='30 DAYS EARLIER'), 2.0, {'hit': .8, 'drop': 1, 'rewind': 1}, flash='white')

# ================= DAY 61: THE ROPE =================
V("Day sixty-one. The morning after the ferry horn.", 'wtop', 'brday', (1000, 800, 1.5, 1.6, 0, 0), [W(700, 1000, 1.1, 'sit', 0, 'sad'), Y(980, 1000, 1.1, 'stand', 0, 'sad'), N(1250, 1000, 1.1, 'stand', 1, 'det')], au={'tension': .5, 'wind': .8}, day=61)
V("The top of the ladder is lying on the catwalk. Three hundred of them are still standing under the rest of it.", 'wdown', 'brday', (960, 700, 1.3, 1.6, 0, 0), au={'tension': .7, 'groan': .6, 'wind': .5})
V("You haven't eaten in three days. Walter can't climb. And the ground is forty meters down.", 'wtop', 'brday', fc_=fc(Y(980, 1000, 1.1, 'sit', 0, 'sad'), 2.3, 2.6), au={'tension': .6, 'wind': .6})
V("We don't need the ladder. We need forty meters of rope. And the other side of the tower.", 'wtop', 'brday', fc_=fc(W(700, 1000, 1.1, 'sit', 0, 'det'), 2.5, 2.8), au={'tension': .6}, voice='walt', gap=.6)
V("So you collect everything up here that bends.", 'wroom', 'brday', (960, 820, 1.4, 1.55, 0, 0), [Y(700, 1000, 1.1, 'crouch', 0, 'det'), N(1100, 1000, 1.1, 'kneel', 1, 'det')], au={'tension': .5, 'rustle': 1, 'tear': .6})
V("Three nylon guy ropes off Nora's antenna. Two tarps, cut into strips and braided. Every sheet and sleeping bag you have.", 'card', card=C(t='math', title='THE ROPE', lines=['3 guy ropes · 24 m', '2 braided tarps · 12 m', 'sheets + sleeping bags · 6 m', ['= 42 m', '#c33a2f', 110]]), au={'tension': .5, 'pops': 1})
V("Forty-two meters. The tower is forty.", 'wwide', 'brday', (960, 600, 1.3, 1.5, 0, 0), au={'tension': .6, 'rope': 1, 'wind': .6}, slam='42 M')
V("Walter teaches you one knot, over and over, until you can tie it with your eyes shut. The bowline.", 'wroom', 'brday', (900, 820, 1.6, 1.75, 0, 0), [W(800, 1000, 1.1, 'sit', 0, 'det'), Y(1050, 1000, 1.1, 'hold', 1, 'det')], au={'tension': .4, 'rope': .8})
V("The rabbit comes out of the hole, round the tree, and back down the hole. It won't slip, and it won't jam.", 'wroom', 'brday', fc_=fc(W(800, 1000, 1.1, 'point', 0, 'soft'), 2.6, 2.8), au={'tension': .3}, voice='walt', gap=.6)
V("Rule number four: one person on the rope at a time. And everyone ties in with a bowline.", 'card', card=C(t='rule', n=4, icon='skull', a='ONE ON THE ROPE', b='Everyone ties in with a bowline'), au={'tension': .5, 'hit': .6})
V("The ladder is on the north leg. So you'll go down the south leg, over the river side. A hundred and twenty meters from the crowd.", 'wwide', 'brdusk', (960, 700, 1.2, 1.35, 0, 0), fx=['gather'], gn=.7, au={'tension': .7, 'groan': .5, 'wind': .5})
V("And you'll go at four in the morning, when most of them are lying still.", 'wwide', 'brnight', (960, 860, 1.5, 1.7, 0, 0), fx=['gather', 'nlamp'], gn=.7, au={'tension': .8, 'wind': .6}, gap=.8)
CARD(C(t='day', n=62), 1.6)

# ================= DAY 62: DOWN =================
V("Day sixty-two. Four a.m. Walter goes first, sitting in a loop of rope, with a broken ankle.", 'wrope', 'brnight', (960, 600, 1.4, 1.6, 0, 120), [ROPE('walt', 760, 1.0, 'fear')], au={'tension': .9, 'rope': 1, 'wind': 1}, day=62)
V("You and Nora lower him, half a meter at a time.", 'wtop', 'brnight', (1000, 860, 1.6, 1.8, 0, 0), [Y(900, 1000, 1.1, 'pull', 0, 'fear'), N(1150, 1000, 1.1, 'pull', 1, 'fear')], au={'tension': .9, 'strain': 1, 'rope': 1})
V("Twenty meters. Twenty-five. Then the rope makes a new sound.", 'wrope', 'brnight', (960, 700, 1.6, 1.9, 0, 0), [ROPE('walt', 900, 1.0, 'fear')], au={'tension': 1, 'rope': 1, 'silence': .5})
V("The tarp is tearing on the steel edge of the catwalk.", 'wtop', 'bred', (900, 1000, 2.4, 2.8, 0, 0, 2), [Y(900, 1000, 1.1, 'pull', 0, 'fear')], au={'tension': 1, 'tear': 1, 'hb': .8}, flash='red')
V("Nora pulls off her yellow raincoat and jams it under the rope. The tearing stops.", 'wtop', 'brnight', (1050, 860, 1.7, 1.9, 0, 0), [N(1050, 1000, 1.1, 'kneel', 1, 'det')], au={'tension': .9, 'cloth': 1, 'rope': .6})
V("Walter's feet touch the mud. Under the ladder, not one of them turns around.", 'wwide', 'brnight', (960, 860, 1.5, 1.6, 0, 0), fx=['gather'], gn=.7, au={'tension': .9, 'groan': .4, 'wind': .6})
V("Then Nora. Then you. Forty meters of shaking rope, in the dark.", 'wrope', 'brnight', (960, 500, 1.5, 1.7, 0, 200, 2), [ROPE('you', 760, 1.0, 'fear')], au={'tension': 1, 'rope': 1, 'wind': 1, 'hb': .7})
V("At the bottom, you leave behind two hundred thousand liters of water. Because you can't carry it.", 'bank', 'brnight', (900, 860, 1.4, 1.6, 0, 0), [Y(700, 1000, 1.0, 'walk', 0, 'sad', mv=60), N(900, 1000, 1.0, 'walk', 0, 'sad', mv=60), W(1100, 1000, 1.0, 'limp', 0, 'sad', mv=60)], fx=['nlamp'], au={'tension': .7, 'steps': 1, 'wind': .5})
V("First problem: water. You can carry sixty liters. Three jugs.", 'card', card=C(t='prob', n=1, icon='drop', a='WATER', b='60 liters is all you can carry'), au={'tension': .7, 'hit': .6})
V("Three people, nine liters a day. Sixty liters lasts less than seven days.", 'card', card=SUP(62, [wat3(60), DAYS(6)], '3 × 3 L = 9 L A DAY', 1), au={'tension': .7, 'pops': 1})
V("Four hundred meters away, on the riverbank, there's a boat repair yard. No boats. But there are pallets, and blue plastic drums.", 'bank', 'brnight', (900, 800, 1.3, 1.5, 0, 0), [Y(800, 1000, 1.0, 'crouch', 0, 'det'), W(1100, 1000, 1.0, 'sit', 1, 'det')], au={'tension': .7, 'water': .5, 'wind': .5})
V("Walter does the math in the dark.", 'card', card=C(t='math', title='THE RAFT', lines=['1 drum · 200 L = floats 200 kg', '6 drums = 1,200 kg', ['3 people + bags = 260 kg', '#2f6a4a', 76]]), au={'tension': .5, 'pops': 1})
V("Every two-hundred-liter drum holds up two hundred kilos. Six drums, twelve hundred. Three people and their bags, two hundred sixty.", 'bank', 'brnight', fc_=fc(W(1100, 1000, 1.0, 'point', 1, 'det'), 2.4, 2.6), au={'tension': .5, 'water': .4})
V("You lash four pallets on top with the last of the rope. Forty minutes. Two of them shuffle past, and never look down.", 'bank', 'brnight', (900, 820, 1.4, 1.6, 0, 0), [Y(800, 1000, 1.0, 'crouch', 0, 'fear'), N(1000, 1000, 1.0, 'kneel', 0, 'fear'), Z(1450, 990, .9, 'shamble', 1, v=2, mv=-120), Z(1620, 990, .9, 'shamble', 1, v=4, mv=-120)], au={'tension': .9, 'rope': .8, 'groan': .5, 'hb': .6})
V("The harbor is three point two kilometers downstream.", 'card', card=C(t='wmap', title='DAY 62 · 4:50 AM', harbor=1), au={'tension': .6, 'water': .5})
V("The current runs at about one meter per second. Fifty-three minutes. If you don't hit anything.", 'card', card=C(t='math', title='THE RIVER', lines=['3,200 m', '÷ 1 m per second', ['= 53 minutes', '#c33a2f', 110]]), au={'tension': .7, 'water': .6})
V("Rule number five: no lights and no voices on the water. Sound carries over a river.", 'card', card=C(t='rule', n=5, icon='ear', a='NO LIGHTS. NO VOICES.', b='Not on the water. Not ever.'), au={'tension': .6, 'hit': .6})
V("You push off.", 'raft', 'brnight', (960, 860, 1.3, 1.5, 0, 0), [Y(760, 1000, 1.0, 'pull', 0, 'det'), W(960, 1000, 1.0, 'sit', 0, 'det'), N(1180, 1000, 1.0, 'pull', 1, 'det')], au={'tension': .7, 'water': 1}, gap=.6)

# ================= THE RIVER =================
V("Under the broken bridge, the river is full of everything that fell with it.", 'raft', 'brnight', (960, 640, 1.0, 1.15, 0, 0), [Y(760, 1000, 1.0, 'pull', 0, 'fear'), W(960, 1000, 1.0, 'sit', 0, 'fear'), N(1180, 1000, 1.0, 'pull', 1, 'fear')], fx=['debris'], au={'tension': .9, 'water': 1, 'metalcreak': .5})
V("Concrete. Cars. And them.", 'raft', 'brnight', (1500, 820, 2.0, 2.3, 0, 0), [Z(1300, 1190, .9, 'stand', 1, v=1), Z(1720, 1180, .9, 'stand', 1, v=4)], fx=['debris'], au={'tension': 1, 'water': 1, 'groan': .6})
V("One of them is caught on a steel cable, up to its chin in the water. Its head turns toward the sound of the drums.", 'raft', 'bred', (1420, 900, 2.2, 2.6, 0, 0), [Z(1420, 1250, 1.0, 'stand', 1, v=3)], fx=['debris'], au={'tension': 1, 'water': 1, 'growl': .7})
V("A gray hand slaps onto the edge of the raft.", 'raft', 'bred', (1300, 960, 2.2, 2.6, 0, 0, 4), [N(1180, 1000, 1.0, 'crouch', 1, 'fear'), Z(1440, 1175, 1.0, 'reach', 1, v=3)], fx=['debris'], au={'tension': 1, 'hit': 1, 'splash': 1}, flash='red', tilt=3)
V("Nora doesn't scream. She just pushes it off with her paddle. Rule five.", 'raft', 'bred', (1250, 900, 1.8, 2.0, 0, 0), [N(1180, 1000, 1.0, 'push', 1, 'det'), Z(1460, 1260, 1.0, 'stand', 1, v=3, mv=120)], fx=['debris'], au={'tension': .9, 'splash': 1, 'water': 1})
V("Fifty minutes later, the sky turns gray. And you see the harbor.", 'harbor', 'brdusk', (960, 600, 1.1, 1.25, 0, 0), au={'tension': .6, 'water': .8, 'wind': .5}, gap=.6)

# ================= THE HARBOR =================
V("The pier is full of them. Hundreds, standing between the cranes, like they're waiting for a ship.", 'harbor', 'brdusk', (420, 680, 1.8, 2.0, 0, 0), fx=['pier'], gn=.8, au={'tension': .9, 'groan': .8})
V("And a hundred and fifty meters out, on its anchor, a white ferry. The Harbor Queen.", 'harbor', 'brdusk', (1380, 700, 1.4, 1.7, 0, 0), fx=['pier'], gn=.8, au={'tension': .7, 'water': .6, 'mystery': .7}, hl='HARBOR QUEEN')
V("No lights. No smoke. Nobody on deck.", 'harbor', 'brdusk', (1500, 620, 2.0, 2.2, 0, 0), au={'tension': .8, 'silence': .5})
V("But over the back, a rope ladder hangs all the way down to the water.", 'harbor', 'brdusk', (980, 830, 2.6, 2.9, 0, 0), au={'tension': .8, 'mystery': .8})
V("Somebody wanted to be able to get back on board.", 'raft', 'brdusk', fc_=fc(W(960, 1000, 1.0, 'sit', 0, 'det'), 2.4, 2.7), au={'tension': .8}, voice='walt', gap=.6)
V("You climb. Walter climbs with his arms again.", 'harbor', 'brdusk', (960, 840, 3.2, 3.5, 0, 0), [A('walt', 948, 880, .22, 'climbl', 0), A('you', 948, 925, .22, 'climbl', 0)], au={'tension': .7, 'rope': 1, 'strain': 1})
V("The Harbor Queen is empty. Plates still on the tables. Coats still on the seats.", 'fsaloon', 'brday', (700, 700, 1.2, 1.35, 0, 0), [Y(600, 1000, 1.0, 'walk', 0, 'fear', mv=80)], au={'tension': .7, 'stepssoft': 1, 'ocean': .5})
V("One of the two lifeboats is gone. Whoever was on this ship, they left in a hurry.", 'harbor', 'brday', (1220, 650, 3.0, 3.3, 0, 0), [], au={'tension': .7, 'wind': .6, 'mystery': .6})
CARD(C(t='day', n=62), 1.4, {'hit': .5})

# ================= FOOD =================
V("Second problem: food. You haven't eaten in four days.", 'card', card=C(t='prob', n=2, icon='can', a='FOOD', b='Day 4 with nothing'), au={'tension': .7, 'hit': .6})
V("Behind the café counter there's a storeroom, locked. Walter opens it with the fire axe.", 'fsaloon', 'brday', (1450, 760, 1.4, 1.55, 0, 0), [W(1400, 1000, 1.0, 'lift', 1, 'det'), Y(1100, 1000, 1.0, 'stand', 1, 'fear')], au={'tension': .7, 'hit': 1, 'wood': 1}, flash='white')
V("A hundred and forty cans of soup. Twenty-two kilos of rice. Three hundred packets of sugar.", 'card', card=C(t='loot', title='STOREROOM · DAY 62', items=[['can', '140 cans of soup'], ['rice', '22 kg rice'], ['bar', '300 sugar packs'], ['cracker', 'crackers']]), au={'tension': .4, 'pops': 1})
V("About a hundred and forty thousand calories.", 'card', card=SUP(62, [food3(140000), DAYS(26)], '3 × 1,800 = 5,400 CAL A DAY', 1), au={'tension': .4, 'pops': 1})
V("At eighteen hundred a day each, that's twenty-six days. Enough to get you to day eighty-eight.", 'fsaloon', 'brday', fc_=fc(N(1100, 1000, 1.0, 'hold', 1, 'soft'), 2.3, 2.5), au={'tension': .4})
V("That night you eat hot soup, sitting on the floor of the café. Walter falls asleep with the spoon in his hand.", 'fsaloon', 'brnight', (900, 860, 1.5, 1.65, 0, 0), [Y(700, 1000, 1.0, 'sit', 0, 'soft'), W(950, 1000, 1.0, 'sleep', 0, 'soft'), N(1180, 1000, 1.0, 'sit', 1, 'soft')], au={'tension': .2, 'warm': .8, 'ocean': .5}, gap=.8)
CARD(C(t='day', n=63), 1.6)

# ================= WATER =================
V("The ferry has a twelve-thousand-liter freshwater tank. The gauge reads zero.", 'sengine', 'dim', (1100, 760, 1.4, 1.55, 0, 0), [W(1150, 1000, 1.0, 'stand', 1, 'det')], au={'tension': .6, 'hum': .4, 'drip': .6}, day=63)
V("Somebody opened the drain valve. On purpose.", 'sengine', 'dim', fc_=fc(W(1150, 1000, 1.0, 'point', 1, 'det'), 2.4, 2.6), au={'tension': .8, 'mystery': .7})
V("So you look up at the sky.", 'fdeck', 'brday', (900, 700, 1.3, 1.4, 0, -100), [Y(800, 1000, 1.0, 'lookup', 0, 'det')], au={'tension': .4, 'wind': .7})
V("The top deck has a canvas awning. Forty square meters.", 'fdeck', 'brday', (700, 300, 1.4, 1.5, 0, 0), au={'tension': .4, 'wind': .7})
V("One millimeter of rain on one square meter is one liter of water. Ten millimeters on this awning is four hundred liters.", 'card', card=C(t='rain', big=[40, 10], note='Every bucket, pot and bin on the ship'), au={'tension': .4, 'rain': .4})
V("Day sixty-six. It rains for eleven hours straight.", 'fdeck', 'brnight', (900, 760, 1.3, 1.5, 0, 0), [Y(700, 1000, 1.0, 'hold', 0, 'soft'), N(1000, 1000, 1.0, 'hold', 1, 'soft')], fx=['rainfx'], au={'tension': .3, 'rain': 1, 'thunder': .6}, day=66)
V("Eighteen millimeters. Seven hundred and twenty liters.", 'card', card=SUP(66, [wat3(780), DAYS(86)], '+720 L', 1), au={'tension': .3, 'pops': 1, 'rain': .5})
V("And rule one still stands. Two drops of bleach per liter. Thirty minutes.", 'fdeck', 'brday', fc_=fc(N(1000, 1000, 1.0, 'hold', 1, 'det'), 2.4, 2.6), au={'tension': .3, 'water': .5}, gap=.8)
CARD(C(t='day', n=64), 1.6)

# ================= THEM: THE CAR DECK =================
V("Third problem: them.", 'card', card=C(t='prob', n=3, icon='ear', a='THEM', b='Under your feet'), au={'tension': .8, 'hit': 1}, flash='white')
V("On your second night aboard, you hear it. Somewhere under the café. A slow knocking on steel.", 'fsaloon', 'brnight', (960, 900, 1.6, 1.9, 0, 60), [Y(800, 1000, 1.0, 'crouch', 0, 'fear')], au={'tension': .9, 'knock3metal': 1}, day=64)
V("The stairs go down to the car deck. The door at the bottom is wrapped in a chain. Padlocked. From the outside.", 'fcar', 'brnight', (960, 600, 1.1, 1.35, 0, 0), [Y(500, 1000, 1.0, 'stand', 0, 'fear')], fx=['chain'], au={'tension': 1, 'chainclink': .6, 'knock3metal': .7})
V("Through the little round window, you count them.", 'card', card=C(t='count', n=41, per=1, title='BEHIND THE CAR DECK DOOR', label='DAY 64'), au={'tension': 1, 'pops': 1, 'groan': .6})
V("Forty-one. Passengers. Crew. Some of them still in their life jackets.", 'fcar', 'bred', (960, 450, 2.6, 3.0, 0, 0, 2), fx=['chain', 'porthole'], au={'tension': 1, 'groan': 1, 'pound': .6})
V("Somebody locked them in down there, so the rest of the ship would stay safe.", 'fcar', 'brnight', fc_=fc(W(560, 1000, 1.0, 'stand', 0, 'sad'), 2.3, 2.5), fx=['chain'], au={'tension': .9})
V("Rule number six: nobody touches the chain.", 'card', card=C(t='rule', n=6, icon='skull', a="DON'T TOUCH THE CHAIN", b='Forty-one of them behind one door'), au={'tension': .8, 'hit': .6}, gap=.8)
CARD(C(t='day', n=70), 1.6)

# ================= THE HORN (MYSTERY) =================
V("Day seventy. Nora finally gets the wheelhouse door open.", 'fwheel', 'brday', (960, 800, 1.3, 1.45, 0, 0), [N(1300, 1000, 1.1, 'stand', 1, 'det'), Y(700, 1000, 1.1, 'stand', 0, 'det')], au={'tension': .6, 'unlock': 1}, day=70)
V("Next to the wheel there's a switch marked auto signal. Nine p.m. Three blasts. For a second, everyone breathes out. It was just a machine.", 'card', card=C(t='hpanel', bat=1), au={'tension': .4, 'click': 1})
V("Then Nora taps the battery gauge. Zero. The power's been dead for weeks.", 'card', card=C(t='hpanel', bat=0, off=1), au={'tension': .8, 'powerdown': 1})
V("The ship's log says exactly when.", 'card', card=C(t='log', title='SHIP LOG · HARBOR QUEEN', lines=['Day 4 - Anchored 150 m off. Gangway up.', 'Day 9 - Car deck chained. 41 inside.', 'Day 12 - 21:00 HORN. Not one of us.', 'Day 25 - Soldiers on pier. Searched cabins.', 'Day 25 - "Nobody leaves the harbor."', 'Day 25 - Batteries dead. Crew to lifeboat.'], red=[2, 5]), au={'tension': .8, 'paper': 1, 'mystery': 1})
V("Day twenty-five. The same day the horn went silent.", 'fwheel', 'brday', fc_=fc(N(1300, 1000, 1.1, 'stand', 1, 'fear'), 2.3, 2.6), au={'tension': .9, 'mystery': 1})
V("So on day sixty, somebody climbed onto the wheelhouse roof and pulled the air horn. By hand.", 'fdeck', 'brday', (1640, 360, 2.0, 2.3, 0, 0), au={'tension': .9, 'mystery': 1, 'wind': .6})
V("Three short blasts doesn't mean leaving. Not if the one pulling the cord doesn't know the rules.", 'fwheel', 'brday', fc_=fc(W(900, 1000, 1.1, 'stand', 0, 'det'), 2.5, 2.8), au={'tension': .9}, voice='walt', gap=.5)
V("Somebody heard Nora's radio on day twelve. Somebody answered. And somebody never left.", 'fwheel', 'brday', fc_=fc(Y(700, 1000, 1.1, 'stand', 0, 'fear'), 2.5, 3.0), au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=1.0)
CARD(C(t='day', n=74), 1.6)

# ================= DAY 74: SOMETHING TAKES FOOD =================
V("Day seventy-four. You count the cans every night now.", 'fsaloon', 'brnight', (1350, 800, 1.5, 1.7, 0, 0), [Y(1350, 1000, 1.0, 'kneel', 1, 'det')], au={'tension': .7, 'cans': .6}, day=74)
V("At nine p.m., a hundred and one. At seven in the morning, ninety-eight.", 'card', card=C(t='math', title='THE STOREROOM', lines=['21:00 · 101 cans', ['07:00 · 98 cans', '#c33a2f', 96]]), au={'tension': .9, 'pops': 1})
V("Rats.", 'fsaloon', 'brday', fc_=fc(W(900, 1000, 1.0, 'sit', 0, 'det'), 2.6), au={'tension': .7}, voice='walt', gap=.4)
V("Rats don't use a can opener.", 'fsaloon', 'brday', fc_=fc(N(1150, 1000, 1.0, 'stand', 1, 'det'), 2.6), au={'tension': .8}, voice='nora', gap=.6)
V("Behind an air vent in the crew corridor, you find cracker wrappers. Each one folded into a tiny, neat square.", 'fcabin', 'brnight', (1720, 200, 2.4, 2.7, 0, 0), au={'tension': .9, 'mystery': 1, 'paper': .6}, gap=.8)
CARD(C(t='day', n=82), 1.6)

# ================= DAY 82: THE HELICOPTER =================
V("Day eighty-two. Just after midnight, a helicopter crosses the harbor with its searchlight on.", 'harbor', 'brnight', (960, 540, 1.0, 1.1, 0, 0), fx=['heli', 'pier'], gn=.6, hx0=200, hdx=1000, au={'tension': .9, 'helicopterfar': 1}, day=82)
V("It hangs over the ferry for twelve seconds. You lie flat on the deck and don't breathe.", 'fdeck', 'brnight', (900, 900, 1.6, 1.8, 0, 0), [Y(800, 1000, 1.0, 'sleep', 0, 'fear'), N(1100, 1000, 1.0, 'sleep', 1, 'fear')], fx=['heli'], hx0=900, hdx=60, au={'tension': 1, 'helicopterfar': 1, 'hb': 1})
V("Then Nora's radio picks up the same military channel from day three.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY'), au={'tension': .9, 'static': 1})
V("Harbor sweep on day ninety. East bank asset still unaccounted for. Nobody leaves the harbor.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY'), au={'tension': 1, 'static': .8}, voice='radio', gap=.6)
V("Day ninety is eight days away. And the food runs out on day eighty-eight.", 'card', card=SUP(82, [food3(32400), DAYS(6)], 'SWEEP: DAY 90', 1), au={'tension': 1, 'tick': .6}, gap=.8)
CARD(C(t='day', n=88), 1.6)
V("Day eighty-eight. The last can of soup. You split it three ways.", 'fsaloon', 'brnight', (900, 860, 1.5, 1.6, 0, 0), [Y(700, 1000, 1.0, 'sit', 0, 'sad'), W(950, 1000, 1.0, 'sit', 0, 'sad'), N(1180, 1000, 1.0, 'sit', 1, 'sad')], au={'tension': .7, 'sad': .6}, day=88)
V("Walter's ankle can take his weight now. Barely. Every night he walks the ship with the fire axe.", 'scorr', 'dim', (960, 640, 1.2, 1.4, 0, 0), [W(800, 1000, 1.0, 'limp', 0, 'det', mv=120)], au={'tension': .8, 'stepsslow': 1}, gap=.8)
CARD(C(t='day', n=90), 1.8, {'hit': 1, 'drop': 1}, flash='red')

# ================= DAY 90: BACK TO TONIGHT =================
V("Which brings you back to tonight. Nine p.m. The horn.", 'card', card=C(t='horn', n=3, label='DAY 90 · 21:00'), au={'tension': 1, 'horn': 3}, day=90)
V("You're on the wheelhouse roof in eleven seconds. The pull cord is still swinging.", 'fdeck', 'brnight', (1450, 760, 1.4, 1.6, 0, -150), [Y(1250, 1000, 1.0, 'run', 0, 'fear', mv=120)], fx=['swing'], au={'tension': 1, 'run': 1})
V("Nobody is there.", 'fdeck', 'brnight', (1640, 380, 2.4, 2.6, 0, 0), fx=['swing'], au={'tension': 1, 'silence': 1}, gap=.6)
V("On the pier, they're wading into the water. Up to their knees. Up to their waists.", 'harbor', 'bred', (800, 760, 1.7, 2.0, 0, 0), fx=['pier', 'wade'], gn=1, au={'tension': 1, 'water': 1, 'groan': 1})
V("And far up the river, a searchlight. Coming this way.", 'harbor', 'brnight', (500, 400, 1.6, 1.8, 0, 0), fx=['farlight', 'pier'], gn=1, au={'tension': 1, 'helicopterfar': .8})
V("Nora checks the crew cabins one by one. Cabin nine is locked from the inside.", 'scorr', 'dim', (960, 640, 1.3, 1.5, 0, 0), [N(800, 1000, 1.0, 'stand', 0, 'fear'), W(1100, 1000, 1.0, 'stand', 1, 'det')], au={'tension': 1, 'knocks': 1})
V("Walter breaks the lock. Inside, there's a nest of blankets. Cracker wrappers. And a drawing, taped to the wall.", 'fcabin', 'brnight', (1000, 640, 1.2, 1.5, 0, 0), au={'tension': 1, 'hit': .8, 'mystery': 1}, flash='white')
V("A water tower. A light. And three people. A man in a cap. A woman in yellow. And you, in a beanie.", 'card', card=C(t='drawing'), au={'tension': .9, 'mystery': 1, 'paper': .6})
V("In the corner, in red crayon. Day eighty-nine.", 'card', card=C(t='drawing', zoom=1), au={'tension': 1, 'hit': .8})
V("On the back, in a child's handwriting.", 'card', card=C(t='drawing', back=1, lines=["I'm sorry I made the horn."]), au={'tension': 1, 'paper': 1})
V("I'm sorry I made the horn. They're coming for me. Go under the river.", 'card', card=C(t='drawing', back=1, lines=["I'm sorry I made the horn.", "They are coming for me.", "Go under the river."]), au={'tension': 1, 'mystery': 1})
V("A kid. The whole time, it was a kid.", 'fcabin', 'brnight', fc_=fc(N(1100, 1000, 1.0, 'stand', 1, 'fear'), 2.4, 2.7), au={'tension': 1}, voice='nora', gap=.6)
V("Then, from below, a sound you know. Steel chain, sliding over steel.", 'fcabin', 'bred', fc_=fc(Y(800, 1000, 1.0, 'stand', 0, 'fear'), 2.5, 2.9, shake=2), au={'tension': 1, 'chainclink': 1, 'metaldrag': .8})
V("At the bottom of the stairs, the chain is lying on the floor. The padlock is open.", 'fcar', 'bred', (960, 820, 1.4, 1.7, 0, 60), fx=['chainopen'], au={'tension': 1, 'hb': 1, 'silence': .5})
V("And the car deck door is open. Just a crack.", 'fcar', 'bred', (1100, 600, 1.8, 2.3, 0, 0, 2), fx=['chainopen', 'ajar'], eyes=1, au={'tension': 1, 'creak': 1, 'growl': 1, 'riser': 1}, tilt=2)
V("Kid. Get Nora. We're leaving. Now.", 'fcar', 'bred', fc_=fc(W(500, 1000, 1.0, 'stand', 0, 'fear'), 2.6, 3.0), fx=['chainopen', 'ajar'], au={'tension': 1, 'drop_after': 1}, voice='walt', gap=1.2)
CARD(C(t='blackend'), 1.4, {'silence': 1})
V("To be continued. Day ninety-one. Thirty Days In A Flooded Subway.", 'card', card=C(t='title', a='S1E4 · THE FLOODED SUBWAY'), au={'tension': .5, 'mystery': 1})
V("Who do you think the kid is? And who opened that door? Tell me in the comments. And subscribe, so you're here when the helicopter lands.", 'card', card=C(t='drawing'), au={'tension': .4, 'mystery': .8, 'endtail5': 1}, gap=1.4)
CARD(C(t='blackend'), 2.5, {'silence': 1, 'tension': .2})
