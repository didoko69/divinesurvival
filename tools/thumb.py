# Thumbnail: renders episodes/<ep>/thumb_shots.json (shot 0 = inset, shot 1 = main) and adds text from thumb.txt
import json, sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
ep = sys.argv[1]; W = f'work/{ep}'; E = f'episodes/{ep}'
subprocess.run(['cp', f'{E}/thumb_shots.json', f'{W}/th.json'], check=True)
subprocess.run(['cp', 'engine/th.js', W], check=True)
subprocess.run(['node', 'th.js'], cwd=W, check=True)
cfg = json.load(open(f'{E}/thumb.json'))
a = Image.open(f'{W}/th0.png').convert('RGB'); b = Image.open(f'{W}/th1.png').convert('RGB')
im = b
if cfg.get('glow'):
    x, y = cfg['glow']
    for r, al in [(150, 40), (80, 90), (26, 255)]:
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(ov).ellipse((x - r, y - r, x + r, y + r), fill=(255, 244, 192, al))
        im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
d = ImageDraw.Draw(im)
if cfg.get('inset', True):
    c = cfg.get('inset_crop', [180, 380, 1740, 1060]); box = cfg.get('inset_box', [1080, 640, 1880, 989])
    im.paste(a.crop(c).resize((box[2] - box[0], box[3] - box[1])), (box[0], box[1])); d.rectangle(box, outline='#e03a2a', width=10)
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
d.text((50, 40), cfg['line1'], font=ImageFont.truetype(F, 150), fill='#f2c418', stroke_width=14, stroke_fill='black')
d.text((50, 210), cfg['line2'], font=ImageFont.truetype(F, 96), fill='white', stroke_width=14, stroke_fill='black')
im = ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(1.12)).enhance(1.2)
os.makedirs(f'out/{ep}', exist_ok=True); im.resize((1280, 720)).save(f'out/{ep}/thumbnail.jpg', quality=85)
print('thumb ok')
