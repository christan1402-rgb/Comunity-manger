# Guiones semanales de reels — FÁBRICA

Cinco reels por semana, escritos desde el informe semanal de noticias y
entregados listos para grabar: un Google Doc y cinco imágenes de apoyo en la
carpeta de cada video, más el bloque de grabación en el calendario.

## Qué hay aquí

| Archivo | Para qué sirve |
|---|---|
| [`PROMPT-REEL-NOTICIA.md`](PROMPT-REEL-NOTICIA.md) | El formato del guion: los 6 bloques, la palabra clave, las reglas de escritura y el guion de referencia |
| [`FASE-ENTREGA.md`](FASE-ENTREGA.md) | Qué pasa después de escribir: Drive, imágenes y Calendar |
| [`RUTINAS.md`](RUTINAS.md) | Las cinco tareas programadas, sus horarios y el cambio de hora |
| [`scripts/preparar-imagen.py`](scripts/preparar-imagen.py) | Deja una imagen lista para subirla al conector de Drive |

## Las dos mitades

**Escribir** es [`PROMPT-REEL-NOTICIA.md`](PROMPT-REEL-NOTICIA.md). Convierte una
noticia real de tecnología en un reel que suene a chisme entretenido, no a
asesoría. La regla que manda es la proporción: 60-70% noticia, nunca más de 40%
apuntando al espectador.

**Entregar** es [`FASE-ENTREGA.md`](FASE-ENTREGA.md). No toca el guion. Crea el
Doc, consigue las cinco imágenes, las sube y agenda la grabación.

## Versión del formato: FUGA v4

El cambio respecto de la v3: el remate ya no incluye las preguntas que la
empresa no respondió. Antes decía «¿cuántas fugas encontró? No lo dijeron.
¿Cuánta plata ahorraron? Tampoco». Frenaba el video justo antes del giro, que
es donde está la fuerza, así que se eliminó.

El remate ahora es el número grande y su repetición, nada más:

> Ya lo tienen en nueve fábricas de seis países. Nueve fábricas.

Lo que la empresa no publicó **se sigue verificando** en el paso 0. Deja de ir
en el guion y queda en las notas privadas, para responder comentarios.

## El diccionario es el activo

NUDO, COLA y FUGA no son tres reels: son un vocabulario que se está
construyendo. Cada reel suma una palabra, con su verbo, y ninguna se repite. La
tabla está al final de
[`PROMPT-REEL-NOTICIA.md`](PROMPT-REEL-NOTICIA.md).

## Límites que conviene saber

- El conector de Google Drive **no puede mover, borrar ni renombrar** archivos.
  Solo crear, copiar y leer. Por eso el informe se archiva copiándolo y el
  original se saca a mano, y por eso los nombres llevan la fecha de la semana.
- Las imágenes se suben en base64 dentro de la llamada, así que hay que
  comprimirlas antes. Eso hace `scripts/preparar-imagen.py`.
- La política de red del entorno no permite todos los hosts. Un host bloqueado
  responde 404 con un cuerpo diminuto. Cuando una imagen auténtica no se puede
  bajar, entra una generada y se dice que es generada.
