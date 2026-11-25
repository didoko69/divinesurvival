# S1E2 — "Zombie Outbreak: I Survived 30 Days In A Water Tower | S1E2"
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

# ================= COLD OPEN — DAY 60 =================
V("This is day sixty.", 'wtop', 'brnight', (1000, 820, 1.5, 1.75, 0, 0), [Y(1000, 1000, 1.1, 'crouch', 1, 'fear')], fx=['vign'], au={'tension': .7, 'wind': 1, 'hit': .8}, day=60, flash='white')
V("You're forty meters in the air, on the catwalk of an old water tower.", 'wwide', 'brnight', (960, 380, 2.2, 1.6, 0, 120), fx=['nlamp', 'gather'], gn=1, au={'tension': .7, 'wind': .9})
V("Below you, around the only ladder, three hundred of them.", 'wdown', 'brnight', (960, 700, 1.2, 1.7, 0, 100), au={'tension': .9, 'groan': .8, 'wind': .6}, tilt=-2)
V("For sixty days, they couldn't climb.", 'card', card=C(t='count', n=300, label='DAY 60 · UNDER THE LADDER'), au={'tension': .8, 'pops': 1})
V("Tonight, one of them is on the ladder.", 'wladder', 'bred', (960, 860, 1.6, 2.0, 0, -100), [CLIMBER(1060)], au={'tension': 1, 'ladder': 1, 'hit': .8}, flash='red', tilt=3)
V("Ten rungs up. Then twenty.", 'wladder', 'bred', (960, 700, 1.4, 1.6, 0, -80, 2), [CLIMBER(940)], au={'tension': 1, 'ladder': 1, 'metalcreak': .8})
V("You haven't eaten in two days. Walter can't stand on his broken ankle.", 'wtop', 'brnight', (1150, 820, 1.6, 1.8, 0, 0), [W(1150, 1000, 1.1, 'sit', 1, 'fear'), Y(900, 1000, 1.1, 'crouch', 1, 'fear')], au={'tension': .9, 'wind': .8})
V("And Nora is holding out a hacksaw.", 'wtop', 'brnight', fc_=fc(N(1300, 1000, 1.1, 'hold', 1, 'det'), 2.3, 2.6), au={'tension': .9, 'metal': .6})
V("If we cut it, nothing comes up. And nothing goes down. Ever.", 'wtop', 'brnight', fc_=fc(N(1300, 1000, 1.1, 'hold', 1, 'fear'), 2.6, 2.9), au={'tension': 1}, voice='nora', gap=.6)
V("Thirty rungs.", 'wdown', 'bred', (960, 560, 1.5, 2.3, 0, 0, 3), au={'tension': 1, 'ladder': 1, 'hb': 1}, slam='30')
V("Thirty days ago, this tower saved your life. Tonight, it might be the thing that kills you.", 'wtop', 'bred', fc_=fc(Y(1000, 1000, 1.1, 'stand', 1, 'fear'), 2.5, 3.0, shake=2), fx=['vign'], au={'tension': 1, 'riser': 1, 'drop_after': 1}, gap=1.0)
CARD(C(t='title', a='30 DAYS EARLIER'), 2.0, {'hit': .8, 'drop': 1, 'rewind': 1}, flash='white')
# ================= DAY 30 → 31: THE JUMP =================
V("Night thirty. The light on the tower spells one word in Morse code. Jump.", 'card', card=TW(morse=1, dur=4, label='NIGHT 30 · 21:00'), au={'tension': .9, 'tick': .5}, day=30)
V("Below you, every charge on the Harbor Bridge is blinking red.", 'brdown', 'bred', (960, 450, 1.3, 1.7, 0, 0), fx=['charges', 'fast'], au={'tension': 1, 'beep': 1})
V("Walter climbs onto the railing first. He tells you how to do it.", 'brdeck', 'bred', fc_=fc(W(700, 1000, .95, 'stand', 0, 'det'), 2.4, 2.6), au={'tension': .9, 'wind': 1})
V("Feet first. Legs together. Arms crossed over your chest. You go in like a pencil, or you don't come up.", 'brdeck', 'bred', fc_=fc(W(700, 1000, .95, 'point', 0, 'det'), 2.7, 3.0), au={'tension': 1, 'wind': .8}, voice='walt', gap=.6)
V("Forty meters. Two point nine seconds of falling. You hit the water at a hundred kilometers an hour.", 'card', card=C(t='math', title='THE JUMP', lines=['40 meters', '2.9 seconds', ['100 km/h', '#c33a2f', 120]]), au={'tension': 1, 'whoosh': 1, 'wind': 1})
V("You jump.", 'brdown', 'bred', (960, 700, 1.0, 1.6, 0, 300), [Y(960, 760, .9, 'dive', 0, 'fear', mv=0)], fx=['charges', 'fast'], au={'tension': 1, 'whoosh': 1, 'bigsplash': 1, 'drop_after': 1}, flash='white', gap=.8)
V("Behind you, the Harbor Bridge explodes.", 'brwide', 'bred', (960, 540, 1.0, 1.25, 0, 0, 6), fx=['boom', 'horde'], au={'tension': 1, 'explode': 1, 'rumble': 1, 'hit': 1}, flash='white', tilt=-3, day=31)
V("The middle span folds into the river. And two thousand of them go with it.", 'brwide', 'bred', (960, 560, 1.4, 1.7, 0, 0, 3), fx=['boom'], au={'tension': 1, 'metalcrash': 1, 'bigsplash': 1, 'rumble': .7})
V("The water is twelve degrees. The cold punches the air out of your lungs.", 'river', 'brnight', fc_=fc(Y(960, 1000, 1.0, 'stand', 0, 'fear'), 2.2, 2.5), wlv=860, au={'tension': 1, 'water': 1, 'breath': 1})
V("Walter taught you this too. The one, ten, one rule.", 'card', card=C(t='math', title='COLD WATER: 1 · 10 · 1', lines=['1 minute to control your breathing', '10 minutes of useful movement', ['1 hour before you pass out', '#c33a2f', 76]]), au={'tension': .8, 'water': .5})
V("One minute to get your breathing back. Ten minutes before your arms stop working. One hour before you black out.", 'river', 'brnight', (960, 780, 1.6, 1.8, 0, 0), [Y(860, 1000, 1.0, 'stand', 0, 'fear'), W(1100, 1000, 1.0, 'stand', 1, 'sad')], wlv=860, au={'tension': .9, 'water': 1}, fx=['torch'])
V("Walter surfaces next to you. He hit something on the way down. He can't kick.", 'river', 'brnight', fc_=fc(W(1100, 1000, 1.0, 'stand', 1, 'sad'), 2.3, 2.6), wlv=860, au={'tension': 1, 'water': 1})
V("So you grab his collar and swim. Two hundred meters, to the west bank.", 'card', card=C(t='wmap', title='NIGHT 31', swim=1), au={'tension': .9, 'water': .8})
V("Somewhere ahead, a flashlight is moving. Showing you where the bank is.", 'river', 'brnight', (1500, 500, 1.6, 2.0, 0, 0), [], fx=['torch'], wlv=860, au={'tension': .8, 'water': 1, 'mystery': .7})
V("You crawl out into the mud. Nine minutes. You had one left.", 'bank', 'brnight', (900, 860, 1.4, 1.6, 0, 0), [Y(760, 1000, 1.0, 'crawl', 0, 'fear'), W(1100, 1000, 1.0, 'sit', 1, 'sad')], fx=['torch'], au={'tension': .8, 'water': .6, 'breath': 1}, day=31)
V("Then a voice. A woman's voice. From somewhere above you.", 'bank', 'brnight', (1500, 400, 1.8, 2.2, 0, 0), fx=['torch', 'nlamp'], au={'tension': .8, 'mystery': 1})
V("The ladder is on the north leg. Climb. Now. They heard the bridge.", 'bank', 'brnight', (1500, 360, 2.4, 2.6, 0, 0), fx=['torch', 'nlamp'], au={'tension': .9, 'groan': .5}, voice='nora', gap=.5)
V("Four hundred meters to the water tower. Walter leans on your shoulder the whole way.", 'wwide', 'brnight', (960, 760, 1.3, 1.5, 0, 0), [Y(500, 1000, 1.0, 'walk', 0, 'fear', mv=80), W(640, 1000, 1.0, 'limp', 0, 'sad', mv=80)], fx=['nlamp'], au={'tension': .9, 'steps': 1, 'groan': .6})
V("A hundred and thirty rungs. Walter climbs every one of them with his arms.", 'wladder', 'brnight', (960, 600, 1.2, 1.5, 0, -150), [W(960, 860, 1.0, 'climbl', 0, 'det'), Y(960, 1220, 1.0, 'climbl', 0, 'fear')], au={'tension': .9, 'ladder': 1, 'strain': 1})
V("At the top, a hand pulls you onto the catwalk. Glasses. A yellow raincoat.", 'wtop', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'reach', 1, 'det'), 2.2, 2.5), fx=['nlamp'], au={'tension': .5, 'wind': .7})
V("Her name is Nora. She's the one who was blinking the light.", 'wtop', 'brnight', (1000, 800, 1.5, 1.6, 0, 0), [N(1250, 1000, 1.1, 'stand', 1, 'soft'), Y(950, 1000, 1.1, 'sit', 0, 'sad'), W(700, 1000, 1.1, 'sit', 0, 'sad')], fx=['nlamp'], au={'tension': .4, 'wind': .6, 'warm': .5}, hl='NORA', gap=.8)
CARD(C(t='day', n=32), 1.6)
# ================= DAY 32: NORA =================
V("Nora was a radio engineer at the harbor. When it started, she climbed up here with a backpack and a radio.", 'wroom', 'brday', fc_=fc(N(1300, 1000, 1.1, 'radio', 1, 'det'), 2.1), au={'tension': .4, 'static': .5}, day=32)
V("On day one, she picked up a military channel. A demolition schedule. Every river crossing. Thirty days.", 'card', card=C(t='dradio', mode='voice', ch='MILITARY · DAY 1'), au={'tension': .7, 'static': .8})
V("She saw you on the bus roof through binoculars. She couldn't call you. So she counted for you.", 'wtop', 'brday', fc_=fc(N(1250, 1000, 1.1, 'point', 0, 'soft'), 2.2, 2.4), fx=['nlamp'], steady=1, au={'tension': .4, 'wind': .6})
V("A car headlight. A truck battery. Thirty nights.", 'card', card=C(t='math', title="NORA'S SIGNAL LAMP", icon='moon', lines=['1 car headlight', '1 truck battery', ['30 nights · 21:00', '#c33a2f', 76]]), au={'tension': .4, 'pops': 1})
V("Walter's ankle is broken. Nora splints it with a broom handle and half a roll of duct tape.", 'wroom', 'brday', (900, 840, 1.6, 1.7, 0, 0), [W(800, 1000, 1.1, 'sit', 0, 'sad'), N(1050, 1000, 1.1, 'kneel', 1, 'det')], au={'tension': .4, 'tear': 1})
V("I've driven a bus with worse.", 'wroom', 'brday', fc_=fc(W(800, 1000, 1.1, 'sit', 0, 'soft'), 2.6), au={'tension': .3}, voice='walt', gap=.6)
# ================= WATER =================
V("First problem: water. For the first time, it isn't a problem.", 'card', card=C(t='prob', n=1, icon='drop', a='WATER', b="You're sitting on top of it"), au={'tension': .4, 'hit': .6})
V("The tank under your feet holds two hundred thousand liters.", 'card', card=C(t='tank', lines=['3 people × 3 L', '= 9 L a day', '60 YEARS']), au={'tension': .3, 'water': .6})
V("Three people, nine liters a day. That's enough water for sixty years.", 'wtop', 'brday', (1000, 820, 1.5, 1.6, 0, 0), [Y(950, 1000, 1.1, 'lift', 0, 'soft'), N(1250, 1000, 1.1, 'stand', 1, 'soft')], au={'tension': .3, 'wind': .6, 'warm': .5})
V("But it's been sitting still for two months. Nora has one rule about it.", 'wroom', 'brday', fc_=fc(N(1250, 1000, 1.1, 'hold', 1, 'det'), 2.3), au={'tension': .4})
V("Rule number one: two drops of bleach per liter. Then you wait thirty minutes. Every time.", 'card', card=C(t='rule', n=1, icon='drop', a='2 DROPS · 30 MINUTES', b='Plain unscented bleach, every liter'), au={'tension': .4, 'hit': .6})
CARD(C(t='day', n=33), 1.6)
# ================= FOOD =================
V("Second problem: food.", 'card', card=C(t='prob', n=2, icon='can', a='FOOD', b='4,500 calories a day for three'), au={'tension': .6, 'hit': .6})
V("Nora carried up twenty-one thousand calories. Enough for one person for two weeks.", 'card', card=SUP(33, [wat(200), food2(21000)], "NORA'S BACKPACK"), au={'tension': .5, 'pops': 1}, day=33)
V("For three people, even at fifteen hundred a day, it's less than five days.", 'card', card=SUP(33, [food2(21000), DAYS(4)], '3 × 1,500 = 4,500 CAL A DAY', 1), au={'tension': .7})
V("Across the street from the tower, sixty meters from the ladder, there's a corner market. Its window is already smashed.", 'wstreet', 'brday', (1100, 560, 1.2, 1.35, 0, 0), au={'tension': .5, 'wind': .5}, fx=['gather'], gn=.05)
V("And Nora has noticed something. At noon, when the sun is high, most of them drift into the shade, two blocks away.", 'wroom', 'brday', fc_=fc(N(1250, 1000, 1.1, 'point', 1, 'det'), 2.2), au={'tension': .5})
V("That gives you about twenty minutes.", 'card', card=C(t='rule', n=2, icon='moon', a='DOWN AT NOON. UP BY 12:20.', b='Nobody on the ladder after dark'), au={'tension': .6, 'hit': .6, 'clock': .6})
V("Day thirty-four. Your first run. A hundred and thirty rungs down.", 'wladder', 'brday', (960, 500, 1.3, 1.45, 0, 200), [Y(960, 700, 1.0, 'climbl', 0, 'det')], au={'tension': .7, 'ladder': 1, 'wind': .6}, day=34)
V("Sixty meters of open street.", 'wstreet', 'brday', (900, 760, 1.4, 1.5, -100, 0), [Y(500, 1000, 1.0, 'run', 0, 'fear', mv=260)], au={'tension': .9, 'run': 1, 'hb': .6})
V("Inside, the shelves are half empty. But nobody thinks to look in the stockroom.", 'aisle', 'afternoon', (960, 560, 1.0, 1.12, 0, 0), [Y(700, 1000, 1.0, 'crouchwalk', 0, 'det', mv=80)], au={'tension': .7, 'stepssoft': 1})
V("Peanut butter. Rice. Pasta. Oats. A camping stove with four gas cans.", 'card', card=C(t='loot', title='STOCKROOM · DAY 34', items=[['bean', 'peanut butter'], ['rice', 'rice + pasta'], ['bar', 'oats'], ['can', 'gas stove']]), au={'tension': .4, 'pops': 1})
V("Twelve kilos in one backpack. About forty thousand calories. Nine more days.", 'card', card=SUP(34, [food2(40000), DAYS(9)], '+40,000 CAL', 1), au={'tension': .4, 'pops': 1})
V("You're back on the catwalk at twelve-eighteen. Two minutes to spare.", 'wtop', 'brday', (1000, 800, 1.5, 1.6, 0, 0), [Y(1000, 1000, 1.1, 'sit', 0, 'soft'), N(1250, 1000, 1.1, 'stand', 1, 'soft')], au={'tension': .4, 'wind': .6, 'warm': .4})
V("That night, for the first time in a month, you eat something hot.", 'wroom', 'brnight', (960, 820, 1.4, 1.55, 0, 0), [Y(700, 1000, 1.1, 'sit', 0, 'soft'), W(950, 1000, 1.1, 'sit', 0, 'soft'), N(1200, 1000, 1.1, 'sit', 1, 'soft')], au={'tension': .2, 'warm': .8, 'campfire': .5}, gap=.8)
CARD(C(t='day', n=36), 1.6)
# ================= THE LOG (MYSTERY) =================
V("On day thirty-six, you find Nora's radio log.", 'wroom', 'brnight', (790, 690, 2.2, 2.5, 0, 0), au={'tension': .6, 'paper': 1, 'mystery': .6}, day=36)
V("She wrote down every signal she's heard since the outbreak.", 'card', card=C(t='log', lines=['Day 1 - Military: bridges blown in 30 days', 'Day 3 - "East bank asset must NOT cross"', 'Day 12 - 21:00 - FERRY HORN. 3 blasts.', 'Day 19 - Ch.16: "anyone at the harbor?"', 'Day 19 - Answer: FERRY HORN. 3 blasts.', 'Day 25 - Nothing. Nothing since.'], red=[1, 4]), au={'tension': .7, 'paper': .6, 'mystery': .8})
V("East bank asset. Must not cross the river. Nora doesn't know what it means either.", 'wroom', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'stand', 1, 'det'), 2.3), au={'tension': .8, 'mystery': 1})
V("But the other entries are worse. Somebody at the harbor heard her on the radio.", 'card', card=C(t='horn', n=3, label='LOG · DAY 19 · 21:00'), au={'tension': .8, 'horn': 3})
V("And they answered the only way they could. Or the only way they wanted to.", 'wtop', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'stand', 1, 'fear'), 2.4, 2.7), fx=['nlamp'], au={'tension': .9, 'mystery': 1, 'wind': .6})
V("Then, after day twenty-five, nothing. No horn. No light. Nothing.", 'wtop', 'brnight', (1250, 640, 1.3, 1.5, 150, -60), [N(1250, 1000, 1.1, 'stand', 1, 'back')], au={'tension': .9, 'wind': .8, 'drop_after': 1}, gap=1.0)
CARD(C(t='day', n=38), 1.6)
# ================= THEM =================
V("Third problem: them.", 'card', card=C(t='prob', n=3, icon='ear', a='THEM', b='They hear the ladder'), au={'tension': .8, 'hit': 1}, flash='white')
V("A steel ladder is a bell. Every step rings all the way down to the ground.", 'wladder', 'brday', (960, 600, 1.8, 2.0, 0, 0), [Y(960, 760, 1.0, 'climbl', 0, 'fear')], au={'tension': .8, 'ladder': 1, 'metal': 1})
V("After your first run, twelve of them were standing under it.", 'wwide', 'brday', (960, 880, 1.6, 1.8, 0, 0), fx=['gather'], gn=.0, au={'tension': .7, 'groan': .5}, day=38)
V("Day forty-one. Your second run. Forty of them.", 'card', card=C(t='count', n=40, per=1, label='DAY 41'), au={'tension': .8, 'pops': 1}, day=41)
V("Day forty-seven. Third run. A hundred and ten.", 'card', card=C(t='count', n=110, label='DAY 47'), au={'tension': .9, 'pops': 1}, day=47)
V("They're not leaving at noon anymore. They're waiting. At the bottom of the ladder.", 'wwide', 'brday', (960, 800, 1.3, 1.5, 0, 0), fx=['gather'], gn=.5, au={'tension': .9, 'groan': .8})
V("Walter watches them for hours. Then he says what all of you are thinking.", 'wtop', 'brdusk', fc_=fc(W(700, 1000, 1.1, 'sit', 0, 'det'), 2.3), au={'tension': .8, 'wind': .6})
V("They're not waiting for us to come down, kid. They're working out how to come up.", 'wtop', 'brdusk', fc_=fc(W(700, 1000, 1.1, 'sit', 0, 'fear'), 2.7, 3.0), au={'tension': 1}, voice='walt', gap=.7)
V("Nora wants to cut the ladder. Walter says no. If you cut it, you starve up here.", 'wtop', 'brdusk', (1000, 800, 1.5, 1.6, 0, 0), [W(700, 1000, 1.1, 'sit', 0, 'det'), Y(980, 1000, 1.1, 'stand', 0, 'sad'), N(1250, 1000, 1.1, 'point', 1, 'det')], au={'tension': .8, 'wind': .6})
V("So rule number three. Nobody cuts the ladder. It's the only way down.", 'card', card=C(t='rule', n=3, icon='skull', a='NEVER CUT THE LADDER', b='No ladder = no food = no way out'), au={'tension': .7, 'hit': .6})
CARD(C(t='day', n=52), 1.6, {'hit': 1, 'drop': 1}, flash='red')
# ================= DAY 52: THE RUN THAT GOES WRONG =================
V("Day fifty-two. The food is almost gone. You go down alone.", 'wladder', 'brday', (960, 500, 1.3, 1.5, 0, 200), [Y(960, 700, 1.0, 'climbl', 0, 'det')], au={'tension': .9, 'ladder': 1, 'hb': .6}, day=52)
V("You make it to the market. You fill the bag. And on the way out, a can slips from the top.", 'wstreet', 'brday', (1200, 800, 1.5, 1.7, 0, 0), [Y(1150, 1000, 1.0, 'run', 1, 'fear')], au={'tension': 1, 'cans': 1, 'hit': 1}, flash='white')
V("It rolls across the street. Ringing like a bell.", 'wstreet', 'brday', (700, 900, 2.0, 2.4, -200, 0), au={'tension': 1, 'cans': 1, 'silence': .4})
V("Every head in the street turns toward you.", 'wstreet', 'bred', (500, 760, 1.6, 1.8, 0, 0, 3), CROWD_ST, fx=['gather'], gn=.6, au={'tension': 1, 'growl': 1, 'groan': 1}, tilt=-3)
V("You run. Sixty meters. You hit the ladder with three of them right behind you.", 'wstreet', 'bred', (900, 800, 1.3, 1.5, -300, 0, 4), [Y(800, 1000, 1.0, 'run', 1, 'fear', mv=-260)] + [Z(1200 + i * 140, 1000, 1.0, 'run', 1, v=i, mv=-300) for i in range(3)], au={'tension': 1, 'run': 1, 'growl': 1}, hand=4)
V("Rung six. A hand closes around your boot.", 'wladder', 'bred', (960, 760, 1.5, 1.8, 0, 0, 3), [Y(960, 760, 1.0, 'climbl', 0, 'fear'), Z(960, 1180, 1.0, 'climbl', 0, v=2)], au={'tension': 1, 'metalgrab': 1, 'hit': 1}, flash='red', tilt=4)
V("You kick. Once. Twice. It lets go.", 'wladder', 'bred', (960, 780, 1.5, 1.7, 0, 0, 5), [Y(960, 760, 1.0, 'climbl', 0, 'fear'), Z(960, 1220, 1.0, 'climbl', 0, v=2, mv=60)], au={'tension': 1, 'thud': 1, 'hit': .8})
V("But it doesn't fall. It grabs the next rung. And the next.", 'wdown', 'bred', (960, 700, 1.3, 1.7, 0, 0), au={'tension': 1, 'ladder': 1, 'metalcreak': 1})
V("Three rungs up. Then it slips, and lands in the crowd.", 'wladder', 'bred', (960, 860, 1.5, 1.7, 0, 0), [CLIMBER(1120, mv=120)], au={'tension': 1, 'thud': 1, 'groan': .8})
V("Three rungs. Last week, it was zero.", 'wtop', 'brdusk', fc_=fc(Y(1000, 1000, 1.1, 'sit', 0, 'fear'), 2.4, 2.8), au={'tension': 1, 'hb': .8, 'drop_after': 1}, gap=1.0)
V("Nobody goes down again.", 'card', card=SUP(52, [food2(18000), DAYS(6)], '1,000 CAL EACH · 6 DAYS', 1), au={'tension': .8})
V("Day fifty-five. A thousand calories each. Day fifty-eight. The last jar of peanut butter.", 'card', card=SUP(58, [food2(1000), DAYS(0)], 'DAY 58 · EMPTY', 1), au={'tension': .9, 'tick': .6}, day=58)
V("Under the ladder, the crowd keeps growing. Two hundred. Then three.", 'wwide', 'brnight', (960, 760, 1.2, 1.5, 0, 0), fx=['gather', 'nlamp'], gn=1, au={'tension': 1, 'groan': 1, 'drop_after': 1}, gap=.9)
CARD(C(t='day', n=60), 1.8, {'hit': 1, 'drop': 1}, flash='red')
# ================= DAY 60: BACK TO TONIGHT =================
V("Which brings you back to tonight. Thirty rungs. Forty.", 'wladder', 'bred', (960, 760, 1.4, 1.7, 0, -120, 2), [CLIMBER(960)], au={'tension': 1, 'ladder': 1, 'metalcreak': .8}, day=60)
V("Nora holds out the hacksaw. And Walter grabs her wrist.", 'wtop', 'bred', (1000, 800, 1.5, 1.7, 0, 0), [W(1000, 1000, 1.1, 'reach', 1, 'det'), N(1250, 1000, 1.1, 'hold', 1, 'fear')], au={'tension': 1, 'hit': .6})
V("Don't cut it. Look at the joints. It's bolted together in three meter sections.", 'wtop', 'bred', fc_=fc(W(1000, 1000, 1.1, 'point', 1, 'det'), 2.6, 2.9), au={'tension': 1}, voice='walt', gap=.5)
V("We don't cut the ladder. We take the top section off.", 'wtop', 'bred', fc_=fc(W(1000, 1000, 1.1, 'point', 1, 'det'), 2.9, 3.2), au={'tension': 1}, voice='walt', gap=.6)
V("Four rusted bolts. One wrench. You lie flat on the catwalk and reach down.", 'wdown', 'bred', (960, 300, 1.8, 2.1, 0, 0), au={'tension': 1, 'metal': 1, 'strain': 1})
V("First bolt. Second bolt. Below you, the ladder is shaking.", 'wladder', 'bred', (960, 640, 1.4, 1.6, 0, 0, 3), [CLIMBER(980)], au={'tension': 1, 'metal': 1, 'ladder': 1, 'hb': 1}, tilt=3)
V("Third bolt. It's a hundred rungs up now.", 'wdown', 'bred', (960, 640, 1.6, 2.2, 0, 0, 4), au={'tension': 1, 'metal': 1, 'hb': 1, 'ladder': 1}, slam='100')
V("The fourth bolt won't move. Nora puts both hands on the wrench next to yours.", 'wtop', 'bred', (1000, 860, 1.8, 2.1, 0, 0), [Y(900, 1000, 1.1, 'pull', 0, 'fear'), N(1100, 1000, 1.1, 'pull', 1, 'fear')], au={'tension': 1, 'strain': 1, 'metalcreak': 1})
V("It snaps. Together, you drag three meters of ladder up onto the catwalk.", 'wtop', 'bred', (1000, 820, 1.4, 1.6, 0, 0, 3), [Y(900, 1000, 1.1, 'pull', 0, 'det'), N(1150, 1000, 1.1, 'pull', 1, 'det')], au={'tension': 1, 'snap': 1, 'metaldrag': 1}, flash='white')
V("Ten seconds later, a gray hand reaches for a rung that isn't there anymore.", 'wladder', 'bred', (960, 420, 1.7, 2.0, 0, 0), [CLIMBER(640)], fx=['gap'], gy=380, au={'tension': 1, 'silence': .7})
V("And then, it falls.", 'wdown', 'bred', (960, 700, 1.6, 1.2, 0, 0), au={'tension': 1, 'whoosh': 1, 'thud': 1, 'drop_after': 1}, gap=1.1)
V("Rule three still stands. You didn't cut the ladder. But there's no way down now.", 'wtop', 'brnight', (1000, 800, 1.4, 1.55, 0, 0), [W(700, 1000, 1.1, 'sit', 0, 'sad'), Y(980, 1000, 1.1, 'sit', 0, 'sad'), N(1250, 1000, 1.1, 'sit', 1, 'sad')], au={'tension': .7, 'wind': .8})
V("And then, at nine o'clock, from the harbor...", 'wtop', 'brnight', (1500, 520, 1.4, 1.8, 0, 0), au={'tension': .9, 'silence': .8, 'mystery': .8})
V("...a ferry horn. Three blasts. The first sound from the harbor in thirty-five days.", 'card', card=C(t='horn', n=3, label='DAY 60 · 21:00'), au={'tension': 1, 'horn': 3, 'mystery': 1})
V("Nora goes white.", 'wtop', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'stand', 1, 'fear'), 2.6, 2.9), au={'tension': 1})
V("Three short blasts. On the water, that means my engines are going astern. A ship pulling away from the dock.", 'wtop', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'point', 1, 'fear'), 2.8, 3.0), au={'tension': 1}, voice='nora', gap=.5)
V("Somebody's leaving.", 'wtop', 'brnight', fc_=fc(N(1250, 1000, 1.1, 'stand', 1, 'fear'), 3.1, 3.3), au={'tension': 1, 'hit': .6}, voice='nora', gap=.7)
V("She flashes the lamp at the harbor. W. A. I. T. Over and over.", 'wtop', 'brnight', (900, 820, 1.6, 1.9, 0, 0), [N(1000, 1000, 1.1, 'hold', 0, 'det')], fx=['nlamp'], au={'tension': 1, 'tick': .5})
V("Nobody answers.", 'card', card=C(t='horn', n=0, count=False, label='DAY 60 · 21:04'), au={'tension': 1, 'silence': 1})
V("Walter looks at the ladder section on the catwalk. Then at you.", 'wtop', 'brnight', (900, 820, 1.4, 1.7, 0, 0), [W(800, 1000, 1.1, 'sit', 0, 'det'), Y(1050, 1000, 1.1, 'stand', 1, 'fear')], au={'tension': 1, 'wind': .7})
V("Kid. How fast can you make a rope?", 'wtop', 'brnight', fc_=fc(W(800, 1000, 1.1, 'sit', 0, 'det'), 3.0, 3.3), au={'tension': 1, 'silence': .8, 'drop_after': 1}, voice='walt', gap=1.2)
CARD(C(t='blackend'), 1.4, {'silence': 1})
V("To be continued. Day sixty-one. Nobody Answered The Ferry Horn.", 'card', card=C(t='title', a='S1E3 · THE FERRY HORN'), au={'tension': .5, 'mystery': 1})
V("Would you have cut the ladder? Tell me in the comments. And subscribe, so you're here when the ferry comes back.", 'card', card=C(t='horn', n=0, count=False), au={'tension': .4, 'mystery': .8, 'endtail5': 1}, gap=1.4)
CARD(C(t='blackend'), 2.5, {'silence': 1, 'tension': .2})
