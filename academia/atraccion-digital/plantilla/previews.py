#!/usr/bin/env python3
"""Convierte el PDF en una PNG por página dentro de .previews/ para revisarlo antes de entregar.

Uso: python3 plantilla/previews.py [escala] [--hoja]
Requiere: pip install pypdfium2 pillow
"""
import sys
from pathlib import Path

try:
    import pypdfium2 as pdfium
    from PIL import Image
except ImportError:
    sys.exit("Falta una librería: pip install pypdfium2 pillow")

root = Path(__file__).resolve().parent.parent
pdf = pdfium.PdfDocument(str(root / "guia-instructor-atraccion-digital.pdf"))
out = root / ".previews"
out.mkdir(exist_ok=True)
for old in out.glob("*.png"):
    old.unlink()

args = [a for a in sys.argv[1:] if not a.startswith("--")]
scale = float(args[0]) if args else 1.4
pages = []
for i, page in enumerate(pdf, 1):
    img = page.render(scale=scale).to_pil()
    img.save(out / f"pg{i:02d}.png")
    pages.append(img)
print(f"{len(pages)} páginas en {out}")

if "--hoja" in sys.argv:
    cols = 4
    thumbs = [p.resize((p.width // 3, p.height // 3)) for p in pages]
    w, h = thumbs[0].size
    rows = -(-len(thumbs) // cols)
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 8, rows * h + (rows + 1) * 8), "#777")
    for k, t in enumerate(thumbs):
        sheet.paste(t, (8 + (k % cols) * (w + 8), 8 + (k // cols) * (h + 8)))
    sheet.save(out / "hoja.png")
    print(f"Hoja de contacto: {out / 'hoja.png'}")
