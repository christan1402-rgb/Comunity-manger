#!/usr/bin/env python3
"""Deja una imagen lista para subirla al conector de Google Drive.

El conector sube el archivo en base64 dentro de la propia llamada, así que una
foto de prensa sin tocar no cabe. Este script descarga (si le pasas una URL),
reescala, comprime hasta caber en un presupuesto de bytes y escribe al lado un
`.b64` que se pega directo en `base64Content`.

    python3 preparar-imagen.py \
      --entrada "https://ejemplo.com/foto.jpg" \
      --salida  "video-1-assets/final-images/01-perro-robot-2026-08-03.jpg"

Sale con código 1 si no logra bajar del presupuesto, para que la rutina se dé
cuenta en vez de subir algo que va a fallar.
"""

import argparse
import base64
import io
import os
import ssl
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps

# El entorno remoto sale por un proxy con su propia CA. urllib lee el proxy de
# las variables de entorno solo; el certificado hay que pasarlo a mano.
CA_BUNDLE = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")

NAVEGADOR = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def descargar(url: str, tiempo_limite: int) -> bytes:
    contexto = ssl.create_default_context(cafile=CA_BUNDLE) if CA_BUNDLE else None
    peticion = urllib.request.Request(url, headers={"User-Agent": NAVEGADOR})
    with urllib.request.urlopen(peticion, timeout=tiempo_limite, context=contexto) as r:
        return r.read()


def leer_entrada(entrada: str, tiempo_limite: int) -> bytes:
    if entrada.startswith(("http://", "https://")):
        return descargar(entrada, tiempo_limite)
    return Path(entrada).read_bytes()


def comprimir(imagen: Image.Image, formato: str, calidad: int) -> bytes:
    buffer = io.BytesIO()
    if formato == "PNG":
        imagen.save(buffer, format="PNG", optimize=True)
    else:
        imagen.save(buffer, format="JPEG", quality=calidad, optimize=True,
                    progressive=True)
    return buffer.getvalue()


def ajustar(imagen: Image.Image, formato: str, max_bytes: int, ancho_max: int,
            calidad_min: int) -> tuple[bytes, dict]:
    """Baja calidad primero, dimensiones después, hasta caber en max_bytes."""
    ancho = min(ancho_max, imagen.width)
    while True:
        escalada = imagen
        if imagen.width > ancho:
            alto = round(imagen.height * ancho / imagen.width)
            escalada = imagen.resize((ancho, alto), Image.LANCZOS)

        for calidad in range(88, calidad_min - 1, -4):
            datos = comprimir(escalada, formato, calidad)
            if len(datos) <= max_bytes:
                return datos, {
                    "ancho": escalada.width,
                    "alto": escalada.height,
                    "calidad": calidad if formato == "JPEG" else "n/a",
                }
            if formato == "PNG":
                break  # PNG no tiene calidad: solo queda encoger

        if ancho <= 480:
            return datos, {
                "ancho": escalada.width,
                "alto": escalada.height,
                "calidad": "mínima",
                "excedido": True,
            }
        ancho = int(ancho * 0.8)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", required=True, help="URL o ruta local de la imagen")
    p.add_argument("--salida", required=True, help="Ruta del archivo final (.jpg/.png)")
    p.add_argument("--max-bytes", type=int, default=70_000,
                   help="Presupuesto de tamaño. Por defecto 70000")
    p.add_argument("--ancho-max", type=int, default=1280,
                   help="Ancho máximo en píxeles. Por defecto 1280")
    p.add_argument("--calidad-min", type=int, default=64,
                   help="Calidad JPEG mínima aceptable. Por defecto 64. Por "
                        "debajo de eso se prefiere encoger: para B-roll una "
                        "imagen chica y nítida rinde más que una grande sucia")
    p.add_argument("--timeout", type=int, default=45, help="Segundos de descarga")
    args = p.parse_args()

    try:
        crudo = leer_entrada(args.entrada, args.timeout)
    except Exception as e:  # red, 403, ruta inexistente
        print(f"ERROR al obtener la imagen: {e}", file=sys.stderr)
        return 1

    if len(crudo) < 4_000:
        print(f"ERROR: {len(crudo)} bytes. Es una miniatura o una página de error, "
              f"no una imagen de apoyo.", file=sys.stderr)
        return 1

    try:
        imagen = Image.open(io.BytesIO(crudo))
        imagen.load()
    except Exception as e:
        print(f"ERROR: no se pudo abrir como imagen: {e}", file=sys.stderr)
        return 1

    origen = f"{imagen.width}x{imagen.height} {imagen.format} {len(crudo)} bytes"

    if imagen.width < 640 or imagen.height < 360:
        print(f"ERROR: {imagen.width}x{imagen.height} es muy chica para B-roll. "
              f"Busca la versión grande o descártala.", file=sys.stderr)
        return 1

    imagen = ImageOps.exif_transpose(imagen)
    salida = Path(args.salida)
    formato = "PNG" if salida.suffix.lower() == ".png" else "JPEG"
    if formato == "JPEG" and imagen.mode not in ("RGB", "L"):
        imagen = imagen.convert("RGB")

    datos, info = ajustar(imagen, formato, args.max_bytes, args.ancho_max,
                          args.calidad_min)

    print(f"origen   {origen}")
    print(f"final    {info['ancho']}x{info['alto']} {formato} calidad "
          f"{info['calidad']} · {len(datos)} bytes")

    if info.get("excedido"):
        # No dejamos el .b64 escrito: si existe, alguien lo va a subir.
        print(f"ERROR: no bajó de {args.max_bytes} bytes ni encogiendo hasta "
              f"{info['ancho']} px.", file=sys.stderr)
        if formato == "PNG":
            print("Es una foto guardada como PNG. Cambia la extensión de "
                  "--salida a .jpg y vuelve a correrlo: PNG solo conviene "
                  "para gráficos, capturas y logos.", file=sys.stderr)
        else:
            print("Usa otra imagen.", file=sys.stderr)
        return 1

    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_bytes(datos)
    b64 = base64.b64encode(datos).decode("ascii")
    ruta_b64 = salida.with_suffix(salida.suffix + ".b64")
    ruta_b64.write_text(b64)

    print(f"base64   {len(b64)} caracteres")
    print(f"imagen   {salida}")
    print(f"b64      {ruta_b64}")

    print("LISTA para create_file con disableConversionToGoogleType: true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
