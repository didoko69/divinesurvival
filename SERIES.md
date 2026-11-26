# Divine survival — series bible

Channel: "Divine survival" (@qonvo2, channel id UCQTdFsi_EEy8zQKUw0zrjNw). Animated 2D survival stories modeled on @BeanieSurvives.
Upload rhythm: Monday, Wednesday, Friday. Long-form 7–10 min.

## Format rules (every episode)
- Second person, present tense ("You're lying flat on the roof…"). Short, punchy sentences. Calm, serious narrator.
- COLD OPEN in the middle of the danger at the episode's last day, 6–12 lines, ends on a question/threat → title card "THE DAY BEFORE" or "N DAYS EARLIER".
- Survival problems framed "First problem: water." / "Second problem: food." / "Third problem: them." with REAL numbers
  (liters per day, calories, kg, distances, days left). Show them on `sup`, `prob`, `rule`, `loot`, `rain` cards. Running counters go down/up between days.
- 2–3 numbered RULES the characters adopt.
- One planted MYSTERY per episode, paid off at the end, plus a CLIFFHANGER that sets up the next episode.
- Yellow "DAY N" stamp (shot key day=N), black "DAY N" title cards between days, slow camera moves, a cut every 2–5 s.
- End: "To be continued" card with next episode title, then a one-line comments question + subscribe ask.
- Length target: 95–125 narration lines, ~1,100–1,300 words → 7–10 minutes.
- Every episode must be a genuinely new story beat (new location, new problem, new reveal). Never reuse a script.

## Characters
- YOU (`Y`, kind 'you'): white round head, navy beanie with grey pompom, red scarf, green backpack. The viewer.
- WALTER (`W`, kind 'walt'): ~60, grey hair + moustache, navy bus-driver cap and uniform. Ex-army (9 years), knows Morse and demolition, calls you "kid". Voice: bm_george (voice='walt').
- Infected (`Z`, kind 'inf'): shamble/run, react to sound, poor climbers, can't open doors, worse at night.

## Season 1 — "The Bridge" (zombie outbreak, Harbor City)
Running facts: outbreak started in the hospital district (east bank). Soldiers sealed river crossings. Radio: "all river crossings closed".
Season mystery: who is signalling from the water tower, and why does the military want the east bank erased?

| Ep | Title | Status |
|----|-------|--------|
| S1E1 | Zombie Outbreak: 30 Days Trapped On A Bridge | POSTED 2026-11-23 |
| S1E2 | Zombie Outbreak: I Survived 30 Days In A Water Tower | POSTED 2026-11-25 |
| S1E3 | Zombie Outbreak: Nobody Answered The Ferry Horn | POSTED 2026-11-26 |
| S1E4 | Zombie Outbreak: 30 Days In A Flooded Subway | planned |
| S1E5 | Zombie Outbreak: The Hospital Where It Started | planned |
| S1E6 | Zombie Outbreak: The Last Boat Out (season finale) | planned |

LOCKED titles + thumbnail beats for the next episodes (incl. Season 2 "Winter"): see UPCOMING.md — it overrides this table.

Planned beats (adapt freely, but keep continuity):
- S1E2 (Day 31–60): You and Walter jump as the bridge falls; Walter hurts his leg. You reach the water tower on the WEST bank. The signaller is NORA (30s, radio engineer, glasses, yellow raincoat). The tank holds ~200,000 L of water — enough, but the ladder is the only way up and the infected learn to gather under it. Mystery: Nora's radio log mentions a second survivor group that answers only with a ferry horn. Cliffhanger: day 60, a ferry horn sounds three times from the harbor.
- S1E3 (Day 61–90): Raft/boat trip to the harbor; abandoned ferry; supplies on board; the horn was automatic — or was it? Cliffhanger: a child's drawing of the water tower in the ferry cabin.
  Continuity from S1E2 as made: Walter's ankle is broken (splinted, can't climb); the top 3 m ladder section was unbolted and is lying on the catwalk (no way down → they must build a rope). Food is at zero on day 60. Water = 200,000 L tank + bleach rule. Rules so far: 1) 2 drops bleach/L, 30 min; 2) down at noon, up by 12:20, never after dark; 3) never cut the ladder. Nora's radio log: day 3 military "East bank asset must NOT cross the river" (season mystery thread); ferry horn 3 blasts on day 12 and day 19 (reply to her ch.16 call), silence after day 25; day 60 horn 3 short blasts = "my engines are going astern" (a ship leaving). Nora flashed W-A-I-T, no answer. Harbor is ~3.2 km from the tower. Infected: ~300 under the ladder, now able to climb a few rungs.
- S1E4 (Day 91–120): Continuity from S1E3 as made: day 61 rope (42 m: guy ropes + braided tarps + sheets), down the river side at 4 a.m.; raft of 6 blue 200-L drums + 4 pallets, 3.2 km downstream (53 min). Ferry HARBOR QUEEN anchored 150 m off the pier since day 4; rope ladder at the stern; one lifeboat gone (crew left day 25). Log: day 9 car deck chained, 41 infected inside; day 12 horn "not one of us"; day 25 soldiers searched every cabin, "Nobody leaves the harbor", batteries dead. Rules added: 4) one on the rope, everyone ties a bowline; 5) no lights, no voices on the water; 6) nobody touches the car-deck chain. Food ran out day 88 (cans went missing at night). Water: rain off the 40 m² awning, ~780 L. Day 82 helicopter + military radio: "Harbor sweep on day ninety. East bank asset still unaccounted for." Day 90: the air horn (pull cord on the wheelhouse roof) blows with nobody there; cabin 9 = a hidden CHILD's nest; crayon drawing of the tower + you/Walter/Nora dated DAY 89; on the back: "I'm sorry I made the horn. They are coming for me. Go under the river." Cliffhanger: car-deck chain on the floor, padlock open, door open a crack (red eyes); Walter: "We're leaving. Now." Walter's ankle can take weight (limps). The child is very likely the "east bank asset" — keep it a hint until S1E6. S1E4 = flooded subway tunnel under the river.
- S1E5–S1E6: decide when you get there; keep the mystery threads alive, pay off the military secret in S1E6.
When Season 1 ends, start Season 2 with a fresh location and premise (check PERFORMANCE.md for what worked).

## Thumbnail rules (every episode — tools/thumb.py v2)
- Dedicated engine render, never a video frame. 1280x720 JPEG < 2 MB. Channel look: dark desaturated night scene, YOU large on the left with a warm rim glow and a fear face, threat on the right partly hidden in black with RED glowing eyes, yellow Anton headline top-right with thick black stroke, optional white second line.
- 2–4 words total, never the title (e.g. "THEY CLIMB / DAY 60"). Max 3 elements: hero, threat, text. Optional red arrow/circle on the key detail.
- Bottom ~30% fades to black: nothing important in the bottom-right corner (timestamp).
- Always check the 320x180 preview (work/<ep>/thumb_320.jpg) before upload; redo if face, threat or text is unclear.
- Variants that work in the engine: S1E2 threat on a ladder/catwalk; S1E3 black door gap with 2 pairs of red eyes + grey fingers on the edge (thumb_shots fields wide/eyes/eyey/grab — never call a field "hand", that is camera shake). Raise bg_dim to ~0.75 for interiors so the threat's shape separates from the wall.
- Save design notes in episodes/<ep>/thumbnail.md. Update these rules from PERFORMANCE.md (CTR) learnings.
