# Professional thumbnails — Gemini (Zapier "Google AI Studio (Gemini)", action generate_image)

Daniel wants PROFESSIONAL thumbnails (he rejected the code-drawn ones). Every video gets an AI-illustrated thumbnail:

1. Write the prompt from the template below (fill the [..] parts from the episode's most dramatic beat). Keep text to 2–4 words.
2. Run Zapier `generate_image` (selected_api GoogleMakerSuiteCLIAPI, model: newest Gemini image model offered — prefer a "pro"/"flash-image" model; check with inspect_zapier_actions enum_property "model").
   Generate 2 variants (different composition/text) and pick the better one.
3. Get the image: the result contains a file URL. Download it with curl into out/<ep>/thumbnail_ai.png. If the shell can't reach that host, pass the URL straight to the YouTube upload `thumbnail` field instead.
4. If downloaded: resize to 1280x720 JPEG < 2 MB (PIL), view it full size AND at 320x180 — text spelled correctly? face/threat readable? bottom-right empty? Then use it as out/<ep>/thumbnail.jpg (host on the media branch as usual).
   If the text came out misspelled, generate again with "no text" and add the text yourself with PIL (fonts/Anton-Regular.ttf, yellow #ffd400 + 16px black stroke).
5. If Gemini fails (no connection, quota, safety block): fall back to the engine thumbnail and mention it in the email to Daniel.
6. Never draw a real person's likeness or a real company logo — use generic cartoon characters and generic buildings/money.

Prompt rules that make thumbnails look pro: one focal character close-up (35–45% of frame) with an exaggerated readable emotion; one clear threat or object partly hidden (curiosity);
strong contrast (dark desaturated background + one saturated accent + rim light on the character); max 3 elements; big bold 2–4 word text with thick black outline;
16:9; nothing important in the bottom-right corner; consistent channel look.

## Divine survival prompt template
YouTube thumbnail, 16:9 widescreen, 1280x720. Polished 2D cartoon illustration in the style of top animated survival-story YouTube channels: clean thick black outlines, cel shading with soft gradients, cinematic lighting, high contrast, very detailed painted background.
Main character (always the same): a simple cartoon person with a big perfectly round white head, two small black dot eyes, small eyebrows, a navy-blue knitted beanie with a grey pom-pom, a red scarf, a green backpack, thin black stick-figure body. Expression: [terrified / shocked, mouth open, sweat drop].
Scene: [e.g. a rusty ferry car deck at night lit by red emergency light]. Threat: [e.g. a dark doorway open a crack with several pairs of glowing red eyes and grey zombie fingers curling round the edge] — partly hidden.
Composition: the character's head and shoulders big on the left (about 40% of the frame) with a warm rim light, looking toward the threat on the right; dark desaturated background with one saturated red accent.
Text: huge bold condensed letters "[2–4 WORDS]" in bright yellow with a thick black outline at the top right, and smaller white "[DAY N]" under it. No other text, no logos, no watermark. Keep the bottom-right corner empty.
