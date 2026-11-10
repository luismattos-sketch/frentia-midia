"""Uso: python3 modelos/render.py entrada.html saida.jpg  (gera 1080x1350 JPG)"""
import sys
from playwright.sync_api import sync_playwright
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
png = out.rsplit('.',1)[0] + '.png'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350})
    import os; pg.goto('file://' + os.path.abspath(src)); pg.wait_for_timeout(300)
    pg.screenshot(path=png); b.close()
Image.open(png).convert('RGB').save(out, quality=85); os.remove(png)
