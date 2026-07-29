#!/usr/bin/env python3
"""Reduce las fuentes del informe a los caracteres que realmente usa.

Sin esto, Chromium incrusta DejaVu Sans casi entera (una copia por página) y el
PDF pesa ~150 KB. Con el subconjunto baja a ~105 KB sin ningún cambio visual.

Uso: python3 scripts/slim-fonts.py informes/AAAA-MM-DD.html  ->  ..._slim.html
"""
import base64, os, re, subprocess, sys

REG  = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# Caracteres que deben sobrevivir aunque no aparezcan hoy: si mañana el informe
# dice "Ñ" o "≥" y el glifo no está, se vería una caja vacía.
EXTRA = (" 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
         ".,;:%()[]{}+-−–—·«»¿?¡!/\\|@#$&*'\"°ºªáéíóúÁÉÍÓÚñÑüÜ✓×→≥≤")

def main(src):
    html = open(src, encoding='utf-8').read()
    visible = re.sub(r'<[^>]+>', ' ', html.split('</style>', 1)[-1])
    for a, b in (('&nbsp;',' '), ('&amp;','&'), ('&lt;','<'), ('&gt;','>')):
        visible = visible.replace(a, b)
    chars = sorted(set(visible) | set(EXTRA))
    unicodes = ','.join(f'U+{ord(c):04X}' for c in chars if ord(c) > 31)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(src)), '.fonts')
    os.makedirs(out_dir, exist_ok=True)
    faces = []
    for path, name, weight in ((REG, 'reg', 400), (BOLD, 'bold', 700)):
        dst = os.path.join(out_dir, name + '.ttf')
        subprocess.run(['pyftsubset', path, f'--unicodes={unicodes}',
                        f'--output-file={dst}', '--layout-features=',
                        '--no-hinting', '--desubroutinize'], check=True)
        b64 = base64.b64encode(open(dst, 'rb').read()).decode()
        faces.append("@font-face{font-family:'RepFont';font-style:normal;"
                     f"font-weight:{weight};src:url(data:font/ttf;base64,{b64})"
                     " format('truetype')}")

    html = html.replace('<style>', '<style>' + ''.join(faces), 1)
    html = re.sub(r'font-family:system-ui[^;]*;', "font-family:'RepFont',sans-serif;", html, count=1)
    html = html.replace('svg{display:block}', "svg{display:block;font-family:'RepFont',sans-serif}", 1)
    dst = src.replace('.html', '_slim.html')
    open(dst, 'w', encoding='utf-8').write(html)
    print(f'{len(chars)} glifos conservados -> {dst}')
    return dst

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Uso: slim-fonts.py <informe.html>')
    main(sys.argv[1])
