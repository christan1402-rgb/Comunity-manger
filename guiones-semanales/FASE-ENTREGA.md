# FASE DE ENTREGA — DRIVE, IMÁGENES Y GOOGLE CALENDAR

Estas instrucciones empiezan **después** de que el guion esté terminado.
No escribas, revises ni modifiques el guion en esta fase.

El guion se escribe con [`PROMPT-REEL-NOTICIA.md`](PROMPT-REEL-NOTICIA.md).
Esta fase solamente entrega lo que ya está escrito.

> Los IDs reales de las carpetas de Drive **no están en este archivo**: este
> repositorio es público. Van en el prompt de cada rutina, que es privado.
> Acá las carpetas se nombran con marcadores como `{{VIDEO_N_ID}}`.

---

## Variables que llegan de la fase anterior

| Variable | Qué es |
|---|---|
| `videoNumber` | Número del uno al cinco |
| `guionGrabable` | La versión ElevenLabs: el guion corrido, un solo párrafo, sin marcas de bloque ni acotaciones |
| `documentContent` | Lo que va dentro del Google Doc (ver abajo) |
| `documentTitle` | Nombre del Google Doc |
| `sourceUrls` | Páginas utilizadas para la noticia |
| `reportId` | ID del informe original de Drive |
| `storyKey` | Identificador de la historia, para evitar repeticiones |
| `recordingWeekStart` | Lunes de la semana de grabación (AAAA-MM-DD) |

### `documentContent` — qué va dentro del Doc

El Doc es lo que abre Cristián para grabar y lo que abre el editor para montar.
Lleva, en este orden:

1. El guion en sus 6 bloques, con los segundos de cada uno.
2. El reparto: palabras y porcentaje de noticia vs negocio, total y duración.
3. La versión para grabar (`guionGrabable`), completa y en un solo párrafo.
4. Las notas de actuación, línea por línea.

**No lleva** verificación de datos, fuentes, riesgos, auditorías ni notas
técnicas. Eso queda en el chat, no en el Doc.

### `documentTitle` — convención

`Video N — PALABRA CLAVE — tema corto (semana AAAA-MM-DD)`

Ejemplo: `Video 1 — FUGA — perro robot de Coca-Cola (semana 2026-08-03)`

La semana va en el título porque el conector de Drive no puede borrar ni
renombrar archivos: si no lleva fecha, el paquete nuevo se confunde con el de
la semana pasada dentro de la misma carpeta.

---

## Herramientas

Herramientas nativas. **Nunca** automatización visual del navegador.

### Google Drive — lo que el conector sí puede hacer

| Necesidad | Herramienta |
|---|---|
| Listar los hijos directos de una carpeta | `search_files` con `parentId = '<id>'` |
| Leer un Doc o un informe | `read_file_content` |
| Metadatos (tamaño, tipo, fecha, padres) | `get_file_metadata` |
| Crear un Google Doc nativo | `create_file` con `contentMimeType: text/plain` y **sin** `disableConversionToGoogleType` |
| Subir una imagen | `create_file` con `base64Content` + `contentMimeType: image/jpeg` + `disableConversionToGoogleType: true` |
| Archivar el informe en Procesados | `copy_file` con `parentId = {{PROCESADOS_ID}}` |

### Google Drive — lo que el conector NO puede hacer

Esto no es opcional ni se puede rodear. **El conector no tiene ninguna
operación de escritura sobre archivos existentes:**

- ✗ No puede mover archivos (no existe `update_file` ni cambio de padres).
- ✗ No puede borrar ni mandar a la papelera.
- ✗ No puede renombrar.
- ✗ No puede editar el contenido de un Doc ya creado.

Consecuencias, ya resueltas más abajo:

- El informe **no se mueve**: se copia a Procesados y el original se deja para
  que Cristián lo saque a mano (paso 6).
- Los paquetes viejos **no se borran**: se avisa y los borra Cristián (paso 2).
- Un Doc mal creado **no se corrige**: se crea otro. Por eso el contenido se
  arma completo antes de crear el Doc, nunca por partes.

### Otras herramientas

- **Web** (`WebSearch`, `WebFetch`, `curl`): abrir las páginas originales,
  localizar imágenes, obtener la URL directa.
- **Generador de imágenes** (`mcp__higgsfield__generate_image`): solo cuando
  las páginas no tengan suficientes imágenes auténticas.
- **Google Calendar**: `list_events`, `create_event`, `update_event`,
  `get_event`.
- **Archivo de estado**: `estado-activo.json` (ver abajo).

---

## Rutas de trabajo

Según dónde corra el proceso:

| | Base de trabajo |
|---|---|
| En el Mac de Cristián | `/Users/christanhernandezhair/Documents/GUIONES PERSONALES/.codex_tmp/guiones-semanales/` |
| Como rutina en el entorno remoto | `/home/user/guiones-semanales-tmp/` |

Dentro de esa base:

- `estado-activo.json`
- `video-N-assets/` — descargas y candidatas
- `video-N-assets/final-images/` — las cinco elegidas, ya comprimidas

Esta carpeta es **temporal**. La entrega final siempre es Drive.
El archivo de estado **nunca** se sube a Drive ni se commitea al repositorio.

### El estado no es un requisito, es un registro

En el entorno remoto cada rutina arranca en un contenedor nuevo: el archivo de
estado de `guion 1` **no existe** cuando corre `guion 2`. Por eso el encadenado
de las cinco tareas no depende del archivo. Se apoya en cosas que se pueden
volver a deducir de Drive en cualquier momento:

| Dato | Cómo se deduce, sin estado previo |
|---|---|
| `reportId` | El archivo directo más reciente de Informes. Las cinco tareas llegan al mismo, porque nosotros nunca modificamos el informe |
| La historia | `guion N` toma **la historia número N** del informe, en el orden original. Determinista, sin coordinación |
| `recordingWeekStart` | Se calcula de la fecha de ejecución (ver paso 5) |
| `docId`, `docUrl` | Listando la carpeta `video N` |
| `storyKey` | La posición N dentro de ese informe |

`estado-activo.json` sirve dentro de una misma corrida y para dejar rastro de
lo que pasó. Si falta, no se bloquea nada: se vuelve a deducir.

---

## Carpetas oficiales

| Carpeta | Marcador |
|---|---|
| Informes pendientes | `{{INFORMES_ID}}` |
| Raíz de entrega | `{{RAIZ_ENTREGA_ID}}` |
| Video 1 | `{{VIDEO_1_ID}}` |
| Video 2 | `{{VIDEO_2_ID}}` |
| Video 3 | `{{VIDEO_3_ID}}` |
| Video 4 | `{{VIDEO_4_ID}}` |
| Video 5 | `{{VIDEO_5_ID}}` |
| Informes procesados | `{{PROCESADOS_ID}}` |

No crees carpetas con fecha, ni carpetas semanales, ni ningún otro contenedor.
Trabaja directamente en la carpeta `video N`.

`{{PROCESADOS_ID}}` es la única carpeta autorizada para archivar el informe.
Existe otra carpeta llamada `PROCESADOS` dentro de la raíz de entrega:
**no la uses.** Su ID también está en el prompt de la rutina, marcado como
prohibido, para que no se confunda con la correcta.

---

## Paso 1 · Seleccionar el informe

1. Lee `estado-activo.json` si existe. Si hay un proceso `IN_PROGRESS` y su
   `reportId` sigue en Informes, continúa con ese mismo informe.
2. Si no hay estado, lista los hijos directos de Informes:
   `search_files` con `parentId = '{{INFORMES_ID}}'`.
3. Ignora las carpetas — `mimeType != 'application/vnd.google-apps.folder'` —
   especialmente la llamada `PROCESADOS`.
4. Elige el archivo directo con la fecha de modificación más reciente.
5. Si ese `reportId` ya aparece en la lista `procesados` del estado, ya se
   trabajó: responde `SIN INFORME SEMANAL NUEVO` y no crees nada.
6. Si no hay ningún archivo directo, responde `SIN INFORME SEMANAL NUEVO` y no
   crees nada.
7. Lee el informe con `read_file_content` y localiza sus cinco historias en el
   orden original.
8. Toma **la historia número `videoNumber`**. Si el informe trae menos de cinco
   historias, no inventes: responde qué falta y no crees nada.
9. Guarda en el estado: `reportId`, nombre, URL y las cinco historias.

Las tareas dos a cinco no pueden elegir otro informe.

### Cómo viene el informe

Comprobado sobre los informes reales de la carpeta. El archivo se llama por
fecha (`2026-07-26`, `2026-07-21.md`) y llega como Google Doc **o** como
markdown. `read_file_content` lee los dos; en el markdown devuelve los
caracteres escapados (`\#\#`, `\*\*`), así que al buscar los títulos cuenta con
esa forma además de la limpia.

Estructura, siempre la misma:

```
# Radar semanal de automatización empresarial
## <titular de la historia 1>
**Titular:** …
**Historia:** …
**Cómo gana o ahorra dinero:** …
**Estado:** ANUNCIADO | IMPLEMENTADO | MEDIDO
**Fuente y material visual:** [enlace] · [enlace]
## <titular de la historia 2>
…
```

De ahí sale todo lo que necesitas:

- **Las cinco historias** son los cinco `##`, en ese orden. `guion N` toma el
  N-ésimo.
- **`sourceUrls`** son los enlaces de «Fuente y material visual» de tu historia,
  y nada más. No mezcles los de otras historias.
- **«Cómo gana o ahorra dinero»** suele traer justo lo que la empresa NO publicó
  («CCEP no publicó ahorro ni retorno financiero»). Eso es material privado para
  responder comentarios. **No entra al guion.**
- **«Estado»** te dice cuánto peso tiene el dato. `ANUNCIADO` es una promesa, no
  un resultado: no lo cuentes como si ya hubiera pasado.

Ojo con las fuentes: muchas son publicaciones de LinkedIn, que pide sesión y no
suelta las imágenes. Cuenta con caer en el orden de reintento de más abajo y con
generar alguna imagen.

---

## Paso 2 · Preparar el Google Doc

Trabaja exclusivamente en la carpeta `video {{videoNumber}}`.

1. Lista primero el contenido actual: `search_files` con `parentId`.
2. Identifica lo que ya está ahí: el Doc anterior, las cinco imágenes
   anteriores, videos grabados, `PROCESADO.txt`, archivos del editor.
3. Crea **un único Google Doc nativo**:
   `create_file` con `parentId = {{VIDEO_N_ID}}`, `title = documentTitle`,
   `textContent = documentContent`, `contentMimeType = 'text/plain'`.
   No pases `disableConversionToGoogleType`: la conversión a Doc nativo es
   justamente lo que queremos.
4. Nada de PDF ni DOCX.
5. No insertes las imágenes dentro del documento.
6. Relee el Doc desde Drive con `read_file_content` y confirma que el contenido
   está completo — que el último bloque de las notas de actuación llegó.
7. Guarda en el estado: `docId`, `docUrl`, `documentTitle`.

**Si ya había un paquete anterior:** primero crea y verifica el Doc nuevo y las
imágenes nuevas. El conector no puede borrar los viejos, así que después
enumera en la respuesta final los archivos antiguos con su nombre y su enlace,
para que Cristián los borre en un par de clics. La fecha en el título y en el
nombre de las imágenes hace que mientras tanto no haya confusión.

Nunca pidas borrar la carpeta `video N`, videos grabados, `PROCESADO.txt`,
marcadores ni archivos del editor.

---

## Paso 3 · Conseguir las cinco imágenes

Cada video recibe exactamente cinco imágenes.

### Orden de búsqueda

1. Abre cada enlace de `sourceUrls`.
2. Busca primero imágenes originales en la noticia oficial, la web de la
   empresa, el comunicado de prensa, el caso de estudio, las galerías o los
   videos oficiales.
3. Si existe la imagen directa, descarga el archivo original en vez de hacer
   una captura de pantalla.
4. Si la página solo tiene video, captura un fotograma representativo y claro.
5. Evita miniaturas pequeñas, imágenes repetidas, gráficos ilegibles o
   imágenes que no expliquen la historia.
6. Guarda las URLs de origen en las notas privadas. No van en el Google Doc.

### Qué deben mostrar

1. Empresa o protagonista de la noticia.
2. Lugar donde ocurre la historia.
3. Acción, máquina o proceso principal.
4. Problema, señal o momento importante.
5. Resultado, producto o consecuencia visible.

No es obligatorio seguir esa clasificación si la noticia pide otras imágenes,
pero las cinco tienen que ayudar al editor a contar la historia.

### Cuándo generar imágenes

Solo si después de revisar todas las fuentes no hay cinco imágenes útiles:

1. Conserva todas las auténticas que encontraste.
2. Genera únicamente las que falten.
3. Las generadas son ilustrativas.
4. No inventes resultados, cifras, clientes, contratos, pantallas, documentos
   internos ni situaciones presentadas como evidencia real.
5. No falsifiques fotografías de prensa.
6. Sin texto dentro de la imagen, salvo que sea imprescindible.
7. No inventes ni alteres logos.

Anota en la respuesta final cuáles imágenes son auténticas y cuáles generadas.

### Nombres de archivo

`01-descripcion-breve-AAAA-MM-DD.jpg` … `05-descripcion-breve-AAAA-MM-DD.jpg`

La fecha es `recordingWeekStart`. Empiezan con la numeración, como pide el
formato, y la fecha al final evita que se mezclen con el paquete de la semana
pasada, que no se puede borrar. Se permiten PNG, JPG o JPEG.

### Comprimir antes de subir

El conector sube imágenes en base64 dentro de la llamada. Una foto de prensa
sin tocar no cabe. Usa el script incluido:

```bash
python3 guiones-semanales/scripts/preparar-imagen.py \
  --entrada "<url o ruta>" \
  --salida  "<base>/video-N-assets/final-images/01-perro-robot-2026-08-03.jpg"
```

El script descarga si le pasas una URL, respeta el proxy y el certificado del
entorno, reduce a 1280 px de ancho máximo, baja la calidad JPEG hasta caber en
el presupuesto y deja al lado un `.b64` listo para pegar en `base64Content`.
Rechaza con código 1 lo que no sirve: miniaturas, páginas de error disfrazadas
de imagen, cualquier cosa bajo 640×360 y lo que no logra bajar del presupuesto.
Cuando falla no deja el `.b64` escrito, justamente para que nadie lo suba.

Medido con fotos reales: una de 1920×1080 queda en 1280×720 calidad 80, unos
64 KB, 86 000 caracteres de base64.

### El límite de verdad: el base64 pasa dos veces

Esto se midió en una corrida real y cambia cómo hay que planificar el trabajo.
El base64 no viaja del disco a Drive: pasa por el contexto **dos veces** — una
al leer el archivo y otra al mandarlo como parámetro de `create_file`. Una
imagen de 45 KB son 60 000 caracteres, o sea unos 120 000 caracteres de
contexto. Cinco imágenes son más de medio millón.

Consecuencias prácticas:

- **Un video con sus cinco imágenes es el trabajo de una corrida.** No intentes
  los cinco videos con sus veinticinco imágenes de una sola pasada: no cabe.
  Las cinco tareas existen justamente para repartir eso.
- Si bajas el presupuesto para que quepan más, las imágenes se van a 400-500 px
  de ancho. Eso **no sirve** para B-roll vertical. Antes de entregar una imagen
  de menos de 600 px, no la entregues: busca otra fuente o genérala.
- Orden recomendado dentro de cada corrida: primero el Doc y el evento, que son
  baratos y son el entregable que se lee; las imágenes después.

### Rechaza las imágenes con cifras quemadas

Las imágenes de proveedor suelen traer texto de marketing incrustado: «20x
improved accuracy», «Fully autonomous». Hay dos razones para descartarlas, y la
segunda es la importante:

1. Es texto en inglés dentro de un reel en español.
2. Es una **cifra que no verificaste y que no está en el guion**. Ponerla en
   pantalla al lado de la cara de Cristián es exactamente el riesgo que el paso
   0 existe para evitar: queda como si él la estuviera afirmando.

En una fuente real solo tres de nueve candidatas estaban limpias. Cuenta con
eso: revisa cada imagen mirándola, no solo por su nombre de archivo.

### El `fileSize` de un Doc recién creado miente

`create_file` sobre un Google Doc devuelve `fileSize: "1"`. **No significa que
el Doc esté vacío.** Es un artefacto de la respuesta antes de que Drive indexe
el archivo. Verifica siempre con `read_file_content`, nunca con el tamaño — si
te guías por el tamaño vas a creer que falló y vas a crear un duplicado que
después no se puede borrar.

- Presupuesto por defecto: **70 000 bytes**. Es un margen prudente, no un límite
  medido del conector. Si una subida falla por tamaño, repite con
  `--max-bytes 45000` (queda en 1280×720 calidad 64, ~41 KB) y sube de nuevo.
- Usa `.jpg` para fotos y `.png` solo para gráficos, capturas y logos. Una foto
  en PNG no baja del presupuesto y el script te lo dice con esas palabras.
- Antes de bajar la calidad por debajo de 64, el script prefiere encoger la
  imagen: para B-roll una imagen chica y nítida rinde más que una grande sucia.

### Si la descarga está bloqueada

En el entorno remoto la salida a internet pasa por una política de red que no
permite todos los hosts. Un host bloqueado responde **404 con un cuerpo
diminuto**, que se ve igual que una imagen que no existe. No insistas ni intentes
rodearlo.

Orden de reintento:

1. Prueba la imagen desde otro host: el comunicado de prensa, la web de la
   empresa, el medio que cubrió la noticia.
2. Si la página se puede leer pero la imagen no se puede bajar, captura el
   fotograma o la vista con Chromium (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
   ya instalado; nunca `playwright install`).
3. Si nada de eso resulta, esa imagen entra como generada, con
   `mcp__higgsfield__generate_image`, y se anota como generada en la respuesta
   final.

Nunca entregues menos de cinco imágenes por culpa de la red. Entrega cinco y di
cuáles son auténticas y cuáles generadas.

---

## Paso 4 · Subir las imágenes a Drive

1. Para cada una de las cinco: lee el `.b64` correspondiente y llama a
   `create_file` con:
   - `parentId = {{VIDEO_N_ID}}`
   - `title` = el nombre del archivo
   - `base64Content` = el contenido del `.b64`
   - `contentMimeType = 'image/jpeg'` (o `image/png`)
   - `disableConversionToGoogleType: true`
2. Solo las cinco elegidas. Hijas directas de `video N`.
3. No crees subcarpetas de imágenes en Drive.
4. No insertes las imágenes en el Google Doc.
5. Vuelve a listar la carpeta y confirma que las cinco de esta semana están,
   numeradas del `01` al `05`.
6. Verifica que ninguna esté rota: `read_file_content` sobre cada imagen
   devuelve una descripción de lo que se ve. Sirve para dos cosas a la vez —
   confirmar que el archivo se subió entero y confirmar que la imagen muestra
   lo que creías. Si la descripción no corresponde, cámbiala.
7. Guarda los cinco `imageIds` en el estado.

Marca `videoN.status = OK` solo cuando estén verificados: un Google Doc nativo,
cinco imágenes, enlaces e IDs válidos, y el contenido releído desde Drive.

---

## Paso 5 · Agregar el video a Google Calendar

- Calendario: `primary`
- Zona horaria: `America/Santiago`
- Duración: una hora
- `availability: AVAILABILITY_BUSY`
- Sin Google Meet (`addGoogleMeetUrl: false`)
- Evento único, sin `recurrenceData`

### La semana

`recordingWeekStart`:

- Si la ejecución es domingo → el lunes siguiente.
- Si la ejecución manual es de lunes a sábado → el lunes de esa misma semana.

Calcúlalo con `TZ=America/Santiago date`, nunca lo asumas. Las tareas dos a
cinco llegan al mismo resultado porque corren el mismo domingo.

### El día

| Video | Día |
|---|---|
| 1 | lunes |
| 2 | martes |
| 3 | miércoles |
| 4 | jueves |
| 5 | viernes |

### La hora

1. Primero lista todos los eventos de ese día (`list_events` con `startTime` y
   `endTime` cubriendo el día completo en `America/Santiago`).
2. Intenta `10:00–11:00`.
3. Si hay conflicto, usa el primer bloque libre de una hora entre `09:00` y
   `18:00`.
4. Nunca superpongas el evento con otro compromiso.

### El título

`Graba el video 1` … `Graba el video 5`. Exacto, sin agregar nada.

### La nota del evento

Exactamente esta estructura:

```
GUION
[guionGrabable completo]

DOCUMENTO
[docUrl]
```

No resumas ni reescribas el guion. Sin fuentes, auditorías, instrucciones
privadas ni notas técnicas.

### Evitar duplicados

Antes de crear:

1. Busca en esa fecha un evento con el mismo título.
2. Revisa `calendarEventId` en el estado.
3. Si ya existe, o si su descripción contiene el mismo `docUrl`, **actualízalo**
   con `update_event`.
4. No crees un segundo evento.

Después de crear o actualizar, relee con `get_event` y confirma: título, fecha,
sesenta minutos, guion completo, enlace correcto, estado ocupado.

Guarda `calendarEventId`, `calendarEventUrl`, `calendarStart`, `calendarEnd` y
`calendarStatus = OK`. Si falla la creación o la lectura, deja
`calendarStatus = PENDING` y dilo en la respuesta.

---

## Paso 6 · Archivar el informe

`guion 1`, `guion 2`, `guion 3` y `guion 4` **nunca** tocan el informe.
Solo `guion 5`, y solo después de verificar todo:

1. Existen las carpetas `video 1` a `video 5`.
2. Cada una tiene un Google Doc nativo válido de esta semana.
3. Cada una tiene las cinco imágenes de apoyo de esta semana.
4. Los cinco Docs fueron releídos desde Drive.
5. Las cinco historias son diferentes.
6. Existen los cinco eventos de Calendar.
7. Cada evento tiene día correcto, una hora de duración, título correcto,
   guion completo y enlace al Doc.

Si falla cualquier control, no archives nada y deja el estado `IN_PROGRESS`.

Si todo está correcto:

1. `copy_file` con `fileId = reportId`, `parentId = {{PROCESADOS_ID}}` y el
   mismo título del original.
2. `get_file_metadata` sobre la copia: confirma que su padre es
   `{{PROCESADOS_ID}}`.
3. Agrega `reportId` a la lista `procesados` del estado. Ese es el candado
   real: aunque el original siga en Informes, `guion 1` no lo va a volver a
   procesar.
4. Marca el proceso `COMPLETE` y guarda `processedAt`, `processedFolderId` y
   `processedFolderUrl`.
5. En la respuesta final, dile a Cristián con el enlace exacto que el informe
   original quedó en Informes y que hay que sacarlo a mano, porque el conector
   no tiene operación de mover.

El original no se mueve porque no se puede, no porque se haya olvidado.

---

## Paso 7 · Respuesta final

Solo enlaces comprobados:

- raíz de entrega
- carpeta `video N`
- Google Doc
- las cinco imágenes
- el evento de Calendar

Más, en dos líneas: qué imágenes son auténticas y cuáles generadas, y qué quedó
pendiente de borrar o mover a mano.

`guion 5` devuelve los enlaces de los cinco videos, los cinco Docs y los cinco
eventos.

**Nunca construyas un enlace suponiendo su ID.** Solo URLs que Drive o Calendar
devolvieron y que verificaste.

---

## Horario de las cinco tareas

Domingos, hora de `America/Santiago`:

| Tarea | Hora |
|---|---|
| `guion 1` | 10:00 |
| `guion 2` | 10:30 |
| `guion 3` | 11:00 |
| `guion 4` | 11:30 |
| `guion 5` | 12:00 |

El cron de las rutinas se guarda en UTC. Chile cambia de hora dos veces al año,
así que en cada cambio hay que correr el cron una hora. Ver
[`RUTINAS.md`](RUTINAS.md).
