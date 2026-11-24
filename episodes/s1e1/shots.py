# Video 10 — "Zombie Outbreak: 30 Days Trapped On A Bridge | S1E1"
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

# ================= COLD OPEN — DAY 30 =================
V("This is day thirty.", 'busroof', 'brnight', (900, 860, 1.5, 1.7, 0, 0), [Y(900, 950, 1.1, 'sleep', 0, 'fear')], fx=['tlight'], au={'tension': .7, 'wind': .8, 'hit': .8}, day=30, flash='white')
V("You're lying flat on the roof of a city bus, in the exact middle of a bridge.", 'brdeck', 'brnight', (960, 600, 1.6, 1.25, 0, 0), [Y(900, 640, .7, 'sleep', 0, 'fear'), W(1150, 640, .7, 'sleep', 1)], fx=['tlight'], au={'tension': .7, 'wind': .8}, day=30,
  cuts=[CUT('brwide', 'brnight', (960, 500, 2.6, 2.9, 0, 0), fx=['horde'])])
V("On the east end, about two thousand of them.", 'brend', 'brnight', (960, 700, 1.15, 1.3, 0, 0), HORDE_E, au={'tension': .9, 'groan': .6, 'wind': .5}, tilt=-2)
V("On the west end, even more.", 'brend', 'bred', (900, 720, 1.4, 1.2, 0, 0), [Z(400 + i * 220, 1000, .95, f=0, v=i + 2) for i in range(6)], au={'tension': .9, 'groan': .8}, tilt=3)
V("Between you and both of them, six hundred meters of abandoned cars.", 'brwide', 'brnight', (960, 520, 1.0, 1.25, 0, 0), fx=['horde'], au={'tension': .8, 'wind': .6})
V("You have one bottle of water left.", 'card', card=SUP(30, [['WATER', 500, ' ml', 'bottle', 1], food(2400)], 'DAY 30 · ALMOST NOTHING LEFT', 1), au={'tension': .8, 'hit': .6})
V("And across the river, on top of an old water tower, a light is blinking at you.", 'brdeck', 'brnight', (1600, 330, 2.2, 3.0, 0, 0), fx=['tlight'], au={'tension': .9, 'mystery': .8},
  cuts=[CUT(card=TW(), w=1.2)])
V("It has blinked every night at nine o'clock. For thirty nights.", 'card', card=TW(n=30, show=None, count=False), au={'tension': .9, 'mystery': .9, 'tick': .6})
V("Counting down.", 'card', card=TW(n=1), au={'tension': 1, 'hit': .8})
V("Tonight, it reaches zero.", 'busroof', 'brnight', fc_=fc(Y(900, 950, 1.1, 'sleep', 0, 'fear'), 2.4, 2.8, dx=-110), fx=['tlight'], au={'tension': 1, 'riser': 1}, slam='ZERO')
V("And you still don't know if zero means rescue...", 'card', card=TW(steady=1), au={'tension': 1, 'silence': .5})
V("...or the end of the bridge.", 'brwide', 'bred', (960, 560, 1.6, 2.1, 0, 0), fx=['charges', 'fast', 'horde'], au={'tension': 1, 'hit': 1, 'drop_after': 1}, gap=1.0, tilt=-4)
CARD(C(t='title', a='THE DAY BEFORE'), 2.0, {'hit': .8, 'drop': 1, 'rewind': 1}, flash='white')
# ================= THE DAY BEFORE =================
V("The day before it started, the news called it a flu.", 'home', 'brdusk', (440, 500, 1.6, 1.8, 0, 0), [Y(1230, 820, 1.0, 'sofa', 1, 'det')], fx=['newsTV'], au={'tension': .3, 'cityamb': .6})
V("A bad one. In the hospital district, on the other side of the river.", 'card', card=C(t='news'), au={'tension': .4, 'static': .2})
V("You didn't think much of it. Nobody did.", 'home', 'brdusk', fc_=fc(Y(1230, 820, 1.0, 'sofa', 1, 'soft'), 2.2), fx=['newsTV'], au={'tension': .3, 'cityamb': .6})
V("But on your way home, you had stopped at the store anyway.", 'aisle', 'afternoon', (960, 560, 1.0, 1.12, 0, 0), [Y(500, 1000, 1.0, 'walk', 0, 'det', mv=120)], au={'tension': .3, 'steps': 1})
V("One case of water. Twenty-four small bottles. Bread, peanut butter, crackers, and six cans of beans.", 'card', card=SUP(0, [wat(12), food(9400)], 'ONE BAG · ONE CASE'), au={'tension': .3, 'pops': 1})
V("It felt like too much. It was nowhere near enough.", 'home', 'brdusk', (960, 540, 1.3, 1.0, 0, 0), [Y(1230, 820, 1.0, 'sofa', 1, 'det')], fx=['newsTV'], au={'tension': .7, 'hit': .8, 'drop_after': 1}, gap=.9)
CARD(C(t='day', n=1), 1.6)
# ================= DAY 1 =================
V("The next morning, you take the bus to work. Bus forty-two. Across the Harbor Bridge.", 'brdeck', 'brday', (960, 600, 1.0, 1.12, 0, 0), au={'tension': .3, 'cityamb': .6, 'engine': .7, 'birds': .4}, day=1)
V("Halfway across, the traffic stops.", 'busin', 'brday', fc_=fc(Y(900, 980, 1.1, 'sit', 0, 'det'), 2.2), au={'tension': .4, 'engine': .5, 'brake': 1}, day=1)
V("Twenty minutes later, people start getting out of their cars.", 'brdeck', 'brday', (1200, 800, 1.5, 1.6, -100, 0), [A('pax', 1350, 1000, .85, 'stand', 1, v=2), A('pax', 1550, 1000, .85, 'stand', 0, v=4)], au={'tension': .5, 'cityamb': .4}, day=1)
V("Then you hear the screaming.", 'busin', 'brday', fc_=fc(Y(900, 980, 1.1, 'sit', 0, 'fear'), 2.6, 3.0), au={'tension': .9, 'scream': .6, 'hit': .8}, tilt=-3, flash='white')
V("From the east end, people are running toward you. Hundreds of them.", 'brdeck', 'brday', (960, 820, 1.25, 1.35, -150, 0), [A('pax', 1500 + i * 160, 1000, .85, 'run', 1, v=i, mv=-420) for i in range(5)], fx=['smoke'], au={'tension': .9, 'crowdpanic': 1, 'run': 1}, hand=4, day=1)
V("And behind them... something else.", 'brdeck', 'brday', (1600, 820, 1.8, 2.0, 0, 0), [Z(1700, 1000, .9, 'shamble', 1, v=1), Z(1860, 1000, .9, 'shamble', 1, v=2)], fx=['smoke'], au={'tension': 1, 'groan': 1, 'silence': .4})
V("They don't run like people. They run like something is pulling them.", 'brdeck', 'bred', (1300, 820, 1.4, 1.5, -200, 0, 4), DECK_INF, fx=['smoke'], au={'tension': 1, 'run': 1, 'growl': 1}, tilt=4, flash='red')
V("The bus driver is a big, grey-haired man named Walter.", 'busin', 'brday', fc_=fc(W(1500, 980, 1.15, 'stand', 1, 'det'), 2.2), au={'tension': .8}, hl='WALTER')
V("He does the only smart thing anyone does that day. He shuts the doors.", 'busin', 'brday', (1700, 560, 1.6, 1.8, 0, 0), [W(1550, 980, 1.15, 'pull', 0, 'det')], au={'tension': .9, 'doorslide': 1, 'slam': 1}, flash='white')
V("Everybody down. Nobody makes a sound.", 'busin', 'brday', fc_=fc(W(1500, 980, 1.15, 'shh', 1, 'det'), 2.6), au={'tension': .9}, voice='walt', gap=.6)
V("For three hours, you lie on the floor of the bus and listen to the bridge.", 'busin', 'bred', (900, 900, 1.5, 1.7, 0, 0), [Y(900, 1010, 1.1, 'sleep', 0, 'fear')], au={'tension': 1, 'groan': .7, 'hb': .8, 'pound': .6})
V("When it finally goes quiet, you look out of the window.", 'busin', 'brdusk', fc_=fc(Y(900, 980, 1.1, 'peek', 0, 'fear'), 2.3), au={'tension': .8, 'silence': .6})
V("The bridge is full of empty cars. And at both ends, they're just... standing there. Waiting.", 'brwide', 'brdusk', (960, 520, 1.3, 1.0, 0, 0), fx=['horde'], au={'tension': .9, 'wind': .7, 'mystery': .7})
V("Soldiers had blocked both ends of the bridge, to stop the infection crossing the river.", 'brend', 'brdusk', (960, 700, 1.0, 1.15, 0, 0), HORDE_E[:4], au={'tension': .8, 'wind': .6}, cuts=[CUT(card=C(t='bmap', day=1, hosp=1))])
V("It didn't stop it. It just trapped everyone in the middle.", 'brend', 'bred', (960, 780, 1.4, 1.6, 0, 0), HORDE_E, au={'tension': 1, 'groan': .7}, tilt=-3)
V("Out of thirty people on that bus, only two are left by nightfall. You. And Walter.", 'busroof', 'brnight', (960, 800, 1.3, 1.5, 0, 0), [Y(800, 920, 1.1, 'sit', 0, 'sad'), W(1100, 920, 1.15, 'sit', 1, 'sad')], au={'tension': .8, 'wind': .8, 'drop_after': 1}, gap=1.0, day=1)
CARD(C(t='day', n=2), 1.6)
# ================= DAY 2 — WATER =================
V("First problem: water.", 'card', card=C(t='prob', n=1, icon='drop', a='WATER', b='12 liters. Two people.'), au={'tension': .5, 'hit': .6})
V("A person needs about three liters a day to stay healthy. Two of you need six.", 'busroof', 'brday', fc_=fc(Y(900, 920, 1.1, 'hold', 0, 'det'), 2.2), au={'tension': .4, 'wind': .5}, day=2)
V("You have twelve liters. That's two days.", 'card', card=SUP(2, [wat(12), ['DAYS LEFT', 2, '', 'bottle', 2]], '6 L PER DAY FOR TWO PEOPLE'), au={'tension': .6, 'pops': 1})
V("But the bridge is one long parking lot. Over four hundred abandoned cars.", 'brwide', 'brday', (960, 500, 2.2, 1.4, 0, 0), au={'tension': .4, 'wind': .6})
V("So you search them. Quietly. One car at a time.", 'brdeck', 'brday', (700, 820, 1.4, 1.55, 0, 0), [Y(560, 1000, .9, 'crouchwalk', 0, 'det', mv=60), W(330, 1000, .95, 'crouchwalk', 0, 'det', mv=60)], au={'tension': .5, 'stepssoft': 1}, day=2)
V("Half-empty bottles. A cooler with melted ice. Soda. Juice boxes from a child's school bag.", 'card', card=C(t='loot', title='FOUND IN CARS · DAY 2', items=[['bottle', 'half bottles'], ['drop', 'cooler water'], ['can', 'soda'], ['cracker', 'juice boxes']]), au={'tension': .4, 'pops': 1})
V("By the end of the day, you've found nine more liters.", 'card', card=SUP(2, [wat(21), food(9400)], '+9 LITERS'), au={'tension': .4, 'pops': 1})
V("Walter warns you about one thing.", 'busroof', 'brdusk', fc_=fc(W(1000, 920, 1.15, 'point', 1, 'det'), 2.2), au={'tension': .5}, day=2)
V("Never drink from the windscreen washer tank. That's methanol. It'll blind you before it kills you.", 'busroof', 'brdusk', fc_=fc(W(1000, 920, 1.15, 'point', 1, 'det'), 2.6, 2.8), au={'tension': .6}, voice='walt', gap=.6)
V("Rule number one on the bridge: if you don't know what it is, you don't drink it.", 'card', card=C(t='rule', n=1, icon='skull', a="DON'T KNOW IT? DON'T DRINK IT.", b='Washer fluid, coolant, radiator water = poison'), au={'tension': .5, 'hit': .6})
# ---- the light ----
V("That night, at exactly nine o'clock, you see it for the first time.", 'brdeck', 'brnight', (1250, 450, 1.3, 1.6, 200, -100), [Y(*ROOF, 'stand', 1, 'det'), W(1080, 640, .72, 'stand', 1, 'det')], fx=['tlight'], au={'tension': .7, 'wind': .6, 'mystery': .6}, day=2)
V("A light. On top of an old water tower, across the river.", 'card', card=TW(), au={'tension': .7, 'mystery': .8})
V("It blinks. And blinks. And blinks.", 'card', card=TW(n=8, count=False), au={'tension': .8, 'tick': 1})
V("You count. Twenty-nine flashes. Then darkness.", 'card', card=TW(n=29, label='NIGHT 2 · 21:00'), au={'tension': .9, 'tick': 1}, hl='29')
V("Walter says it's probably nothing. Somebody signalling for help.", 'busroof', 'brnight', (960, 780, 1.4, 1.5, 0, 0), [Y(800, 920, 1.1, 'sit', 0, 'det'), W(1100, 920, 1.15, 'sit', 1, 'soft')], fx=['tlight'], au={'tension': .6, 'wind': .6})
V("But the next night, the light blinks twenty-eight times.", 'card', card=TW(n=28, show=28, label='NIGHT 3 · 21:00'), au={'tension': .8, 'tick': 1}, day=3)
V("And the night after that, twenty-seven.", 'card', card=TW(n=27, show=27, label='NIGHT 4 · 21:00'), au={'tension': .9, 'tick': 1}, day=4)
V("Someone over there is counting down. And they want you to see it.", 'busroof', 'brnight', fc_=fc(Y(900, 920, 1.1, 'stand', 0, 'fear'), 2.4, 2.8, dx=60), fx=['tlight'], au={'tension': 1, 'mystery': 1, 'drop_after': 1}, gap=1.0)
CARD(C(t='day', n=6), 1.6)
# ================= FOOD + THEM =================
V("Second problem: food.", 'card', card=C(t='prob', n=2, icon='can', a='FOOD', b='4,000 calories a day for two'), au={'tension': .5, 'hit': .6})
V("Two adults burn around four thousand calories a day, just staying alive.", 'busroof', 'brday', (960, 780, 1.4, 1.5, 0, 0), [Y(800, 920, 1.1, 'sit', 0, 'sad'), W(1100, 920, 1.15, 'sit', 1, 'sad')], au={'tension': .4, 'wind': .5}, day=6)
V("Your groceries were nine thousand four hundred calories. Barely two days.", 'card', card=SUP(6, [food(9400), ['DAYS', 2, '', 'can', 2]]), au={'tension': .5, 'pops': 1})
V("The cars give you more. Granola bars. Chips. A box of donuts from a delivery van. And a ten kilo sack of rice from the back of a minivan.", 'card', card=C(t='loot', title='FOUND IN CARS · DAY 6', items=[['bar', 'granola bars'], ['cracker', 'chips'], ['can', 'donuts'], ['rice', '10 kg rice']]), au={'tension': .4, 'pops': 1})
V("Without a stove, the rice is useless. But everything else adds up to twenty-two thousand calories.", 'card', card=SUP(6, [food(22000), ['DAYS', 9, '', 'can', 9]], '1,200 CAL EACH PER DAY = 9 DAYS'), au={'tension': .4, 'pops': 1})
V("You're hungry all the time. But you're alive.", 'busroof', 'brdusk', fc_=fc(Y(900, 920, 1.1, 'sit', 0, 'sad'), 2.3), au={'tension': .5, 'wind': .5})
V("Third problem: them.", 'card', card=C(t='prob', n=3, icon='ear', a='THEM', b='They hear everything'), au={'tension': .8, 'hit': 1}, flash='white')
V("The infected don't climb well. They can't open doors. But they hear everything.", 'brend', 'brday', (960, 760, 1.2, 1.4, 0, 0), HORDE_E, au={'tension': .8, 'groan': .6})
V("On day eight, a car alarm goes off near the east end.", 'brdeck', 'brday', (1650, 860, 1.6, 1.8, 0, 0), fx=['carlights'], au={'tension': .9, 'alarm': 1}, day=8)
V("Within a minute, two hundred of them pour onto the bridge, toward the sound.", 'brwide', 'bred', (1500, 480, 2.4, 2.0, 0, 0), fx=['horde', 'hordemove'], au={'tension': 1, 'alarm': .6, 'run': 1, 'growl': 1}, hand=4, tilt=-3,
  cuts=[CUT('brdeck', 'bred', (1300, 820, 1.3, 1.4, -150, 0, 5), DECK_INF + [Y(*ROOF, 'crouch', 1, 'fear'), W(1080, 640, .72, 'crouch', 1, 'fear')], fx=['carlights'])])
V("It takes them three hours to lose interest and drift back.", 'brwide', 'brdusk', (960, 500, 1.2, 1.1, 0, 0), fx=['horde'], au={'tension': .7, 'groan': .4, 'clock': .5})
V("So you make rule number two. No noise. Ever.", 'card', card=C(t='rule', n=2, icon='ear', a='NO NOISE. EVER.', b='No alarms, no horns, no shouting'), au={'tension': .5, 'hit': .6})
V("And rule number three. After dark, you sleep on the roof.", 'card', card=C(t='rule', n=3, icon='moon', a='AFTER DARK: THE ROOF', b='They are worse at night'), au={'tension': .5, 'hit': .6})
V("Then Walter has an idea. The cars around you aren't locked. And most of them are in neutral.", 'brdeck', 'brday', fc_=fc(W(700, 1000, .95, 'point', 0, 'det'), 2.2), au={'tension': .5}, day=9)
V("So you push them.", 'brdeck', 'brday', (500, 820, 1.4, 1.5, 0, 0), [Y(420, 1000, .9, 'push', 0, 'det', mv=40), W(560, 1000, .95, 'push', 0, 'det', mv=40)], au={'tension': .5, 'strain': 1, 'drag': 1})
V("A small car weighs about a ton. On a flat road, two people can roll one.", 'brdeck', 'brday', (420, 860, 2.0, 2.2, 0, 0), [Y(380, 1000, .9, 'push', 0, 'det', mv=30)], au={'tension': .4, 'strain': 1})
V("In four days, you build a wall of cars, twenty meters out on each side of the bus.", 'brwide', 'brday', (960, 500, 3.0, 3.4, 0, 0), fx=['carwall'], au={'tension': .4, 'wind': .5}, day=12)
V("It won't stop a horde. But it might slow one down long enough to climb.", 'brdeck', 'brdusk', (960, 700, 1.2, 1.35, 0, 0), [Y(*ROOF, 'stand', 0, 'det')], au={'tension': .6, 'wind': .6, 'drop_after': 1}, gap=.8)
CARD(C(t='day', n=13), 1.6)
# ================= RAIN =================
V("On day thirteen, the water runs low again. Four liters left.", 'card', card=SUP(13, [wat(4), ['DAYS', 0, '', 'bottle', 1]], 'LESS THAN ONE DAY', 1), au={'tension': .8, 'hit': .6})
V("And then, it rains.", 'busroof', 'brnight', (960, 600, 1.0, 1.15, 0, 0), [Y(800, 920, 1.1, 'lookup', 0, 'soft')], fx=['rainfx'], au={'tension': .3, 'rain': 1, 'thunder': .8}, day=13)
V("Walter takes a plastic tarp from a pickup truck, spreads it across the roof, and folds the edges into a funnel.", 'busroof', 'brnight', (960, 860, 1.3, 1.45, 0, 0), [W(450, 920, 1.15, 'pull', 0, 'det')], fx=['tarp', 'rainfx'], au={'rain': 1, 'tarp': 1, 'tension': .3})
V("Here's the math. One millimeter of rain on one square meter gives you one liter.", 'card', card=C(t='rain'), au={'tension': .3, 'rain': .6})
V("The tarp is six square meters. That storm drops eleven millimeters. Sixty-six liters.", 'card', card=C(t='rain', big=[6, 11], note='Every bottle you own, full.'), au={'tension': .3, 'rain': .6, 'pops': 1})
V("You fill every bottle you have. For the first time in two weeks, you laugh.", 'busroof', 'brnight', fc_=fc(Y(1200, 920, 1.1, 'lift', 0, 'soft'), 2.0), fx=['tarp', 'rainfx'], au={'rain': 1, 'tension': .2, 'warm': .6})
V("That night, the light blinks seventeen times.", 'card', card=TW(n=17, show=17, label='NIGHT 13 · 21:00'), au={'tension': .8, 'tick': 1, 'rain': .3}, day=13)
# ================= DAY 14 — RADIO =================
V("On day fourteen, Walter gets a car radio working, wired to a truck battery.", 'brdeck', 'brday', fc_=fc(W(700, 1000, .95, 'radio', 0, 'det'), 2.2), au={'tension': .5, 'static': .8}, day=14)
V("Most stations are just static. One isn't.", 'card', card=C(t='dradio', mode='crackle', ch='FM 88.1'), au={'tension': .7, 'static': 1})
V("The quarantine zone is now sealed. All river crossings will be closed in sixteen days. Repeat. Sixteen days.", 'card', card=C(t='dradio', mode='voice', ch='EMERGENCY'), au={'tension': .9, 'static': .5}, voice='radio', gap=.8)
V("Sixteen days. Exactly the same as the light.", 'card', card=TW(n=16, show=16, label='NIGHT 14 · 21:00'), au={'tension': 1, 'hit': 1}, slam='16')
V("Walter goes quiet for a long time. Then he asks the question.", 'busroof', 'brdusk', fc_=fc(W(1000, 920, 1.15, 'sit', 1, 'sad'), 2.3), au={'tension': .8, 'wind': .5})
V("Closed. How do you close a bridge?", 'busroof', 'brdusk', fc_=fc(W(1000, 920, 1.15, 'sit', 1, 'det'), 2.7), au={'tension': .9}, voice='walt', gap=.6)
V("Neither of you answers.", 'busroof', 'brnight', (960, 780, 1.3, 1.2, 0, 0), [Y(800, 920, 1.1, 'sit', 0, 'sad'), W(1100, 920, 1.15, 'sit', 1, 'sad')], fx=['tlight'], au={'tension': .9, 'drop_after': 1}, gap=1.0)
CARD(C(t='day', n=20), 1.6)
# ================= DAY 20 — THE CHARGES =================
V("On day twenty, you lean over the railing to look at the river. And you see something on the pillar below you.", 'brdown', 'brday', (960, 540, 1.0, 1.15, 0, 120), fx=['charges'], au={'tension': .7, 'wind': .8, 'water': .5}, day=20)
V("A grey box, strapped to the concrete. With a small red light.", 'charge', 'brday', (960, 540, 1.0, 1.2, 0, 0), au={'tension': .9, 'beep': 1, 'sting': 1})
V("Walter stares at it for a long time.", 'brdeck', 'brday', fc_=fc(W(600, 1000, .95, 'still', 0, 'fear'), 2.4), au={'tension': .9, 'silence': .5})
V("I did nine years in the army, kid. That's a demolition charge.", 'brdeck', 'brday', fc_=fc(W(600, 1000, .95, 'still', 0, 'det'), 2.8, 3.0), au={'tension': 1}, voice='walt', gap=.7)
V("There are more. One on every pillar.", 'brwide', 'brday', (960, 600, 1.5, 1.2, 0, 0), fx=['charges'], au={'tension': 1, 'beep': .6})
V("They aren't going to close the bridge. They're going to drop it into the river.", 'brdown', 'bred', (960, 420, 1.6, 2.2, 0, 0), fx=['charges'], au={'tension': 1, 'hit': 1}, hl='THEY WILL DESTROY THE BRIDGE', tilt=4, flash='red')
V("With you on it.", 'busroof', 'bred', fc_=fc(Y(900, 920, 1.1, 'stand', 0, 'fear'), 3.0, 3.4, shake=3), au={'tension': 1, 'hb': 1, 'drop_after': 1}, gap=1.1, tilt=-4)
# ================= DAYS 21-29 =================
V("Now the countdown makes sense. Whoever is on that water tower isn't calling you home.", 'card', card=TW(steady=1, label='NIGHT 20 · 21:00'), au={'tension': .9, 'mystery': 1}, day=20)
V("They're telling you how much time you have left.", 'card', card=TW(n=10, show=10, label='NIGHT 20 · 21:00'), au={'tension': 1, 'tick': 1})
V("You look for a way off. Walking is impossible. Two thousand infected on one end. More on the other.", 'card', card=C(t='bmap', day=21, tower=1), au={'tension': .9, 'pops': 1}, day=21)
V("The river is forty meters down. From that height, hitting water is like hitting concrete.", 'brdown', 'brnight', (960, 700, 1.1, 1.5, 0, 200), fx=['charges'], au={'tension': 1, 'water': .7, 'wind': .8})
V("You look for another way. You don't find one.", 'busroof', 'brnight', (960, 800, 1.4, 1.25, 0, 0), [Y(800, 920, 1.1, 'sit', 0, 'sad'), W(1100, 920, 1.15, 'sit', 1, 'sad')], fx=['tlight'], au={'tension': .9, 'wind': .6})
V("Day twenty-five. Five.", 'card', card=TW(n=5, show=5, label='NIGHT 25 · 21:00'), au={'tension': 1, 'tick': 1}, day=25)
V("Day twenty-eight. Two.", 'card', card=TW(n=2, show=2, label='NIGHT 28 · 21:00'), au={'tension': 1, 'tick': 1}, day=28)
V("Day twenty-nine. One.", 'card', card=TW(n=1, show=1, label='NIGHT 29 · 21:00'), au={'tension': 1, 'hit': 1, 'drop_after': 1}, day=29, gap=.9)
CARD(C(t='day', n=30), 1.8, {'hit': 1, 'drop': 1}, flash='red')
# ================= DAY 30 =================
V("Which brings you back to tonight.", 'busroof', 'brnight', (900, 860, 1.4, 1.6, 0, 0), [Y(900, 950, 1.1, 'sleep', 0, 'fear')], fx=['tlight'], au={'tension': .8, 'wind': .8}, day=30)
V("Half a liter of water. A sack of rice you can't cook. And a wall of cars that won't stop what's coming.", 'card', card=SUP(30, [['WATER', 500, ' ml', 'bottle', 1], food(2400)], 'DAY 30', 1), au={'tension': .8})
V("At nine o'clock, you both sit up and stare at the water tower.", 'busroof', 'brnight', (1250, 650, 1.0, 1.3, 150, -100), [Y(800, 920, 1.1, 'sit', 0, 'fear'), W(1100, 920, 1.15, 'sit', 0, 'fear')], au={'tension': 1, 'silence': .6, 'hb': .8})
V("The light comes on.", 'card', card=TW(steady=1, label='NIGHT 30 · 21:00'), au={'tension': 1, 'hit': .8}, flash='white')
V("But this time, it doesn't count. The flashes are long and short.", 'card', card=TW(morse=1, dur=6, label='NIGHT 30 · 21:00'), au={'tension': 1, 'tick': .4})
V("Walter grabs your arm. That's Morse code.", 'busroof', 'brnight', fc_=fc(W(1100, 920, 1.15, 'sit', 0, 'fear'), 2.5), au={'tension': 1})
V("J. U. M. P.", 'card', card=TW(morse=1, dur=4, label='MORSE'), au={'tension': 1, 'hit': .6}, voice='walt', gap=.8)
V("Jump.", 'card', card=C(t='bnote', lines=['J U M P'], red=1), au={'tension': 1, 'hit': 1}, flash='white', gap=.9)
V("Below you, every red light on every pillar starts blinking faster.", 'brdown', 'bred', (960, 450, 1.4, 1.9, 0, 0), fx=['charges', 'fast'], au={'tension': 1, 'beep': 1, 'alarm': .5}, tilt=3)
V("At the east end, the infected hear it. All of them turn.", 'brend', 'bred', (960, 760, 1.2, 1.4, 0, 0, 3), [Z(300 + i * 230, 1000 + (i % 2) * 30, .95, 'turn', 1, v=i) for i in range(7)], au={'tension': 1, 'groan': 1})
V("And for the first time in thirty days, they start walking onto the bridge.", 'brwide', 'bred', (960, 500, 1.4, 1.8, 0, 0), fx=['horde', 'hordemove', 'charges', 'fast'], au={'tension': 1, 'groan': 1, 'stepsmany': 1, 'riser': 1}, hand=4)
V("Walter looks at the black water, forty meters below. Then he looks at you.", 'brdown', 'brnight', (960, 700, 1.2, 1.5, 0, 0), fx=['charges', 'fast'], au={'tension': 1, 'water': .7, 'silence': .4},
  cuts=[CUT('busroof', 'bred', fc_=fc(W(1000, 920, 1.15, 'stand', 1, 'fear'), 2.6, 3.0))])
V("Kid. Can you swim?", 'busroof', 'bred', fc_=fc(W(1000, 920, 1.15, 'stand', 1, 'det'), 3.0, 3.3), au={'tension': 1, 'silence': .8, 'drop_after': 1}, voice='walt', gap=1.2)
CARD(C(t='blackend'), 1.4, {'silence': 1})
V("To be continued. Day thirty-one. The Water Tower.", 'card', card=C(t='title', a='S1E2 · THE WATER TOWER'), au={'tension': .5, 'mystery': 1})
V("Would you jump? Tell me in the comments. And subscribe, so you don't miss what's waiting on that tower.", 'card', card=TW(steady=1), au={'tension': .4, 'mystery': .8, 'endtail5': 1}, gap=1.4)
CARD(C(t='blackend'), 2.5, {'silence': 1, 'tension': .2})
