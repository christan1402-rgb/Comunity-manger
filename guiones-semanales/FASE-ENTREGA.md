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

### `documentContent` — SOLO el guion para leer

Pedido explícito de Cristián, y no es negociable: el Doc lleva **únicamente el
guion corrido, tal como se lee en voz alta.** Nada más.

**NO va en el Doc:**

- ✗ Los 6 bloques ni sus nombres (GANCHO, HISTORIA, REMATE…).
- ✗ Los segundos ni el conteo de palabras de cada bloque.
- ✗ El reparto de noticia vs negocio.
- ✗ Las notas de actuación.
- ✗ Verificación, fuentes, riesgos, auditorías, notas técnicas.

O sea: `documentContent` es exactamente `guionGrabable`. Un solo párrafo, sin
títulos, sin encabezados, sin la palabra clave arriba. El Doc se abre y se lee.

El análisis no se pierde: los bloques, el reparto y las notas de actuación van
en la respuesta del chat, que es donde Cristián los revisa si los quiere. Al
Doc no entran, porque el Doc es el atril.

### `documentTitle` — convención

`Video N — PALABRA CLAVE — guion para grabar`

Ejemplo: `Video 1 — PLANILLA — guion para grabar`

La palabra clave va en el título para distinguir un video de otro de un vistazo,
sin abrir nada.

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
| Archivar el informe en Procesados | `copy_file` con `parentId = {{PROCESADOS_ID}}` |

### Google Drive — lo que el conector NO puede hacer

Esto no es opcional ni se puede rodear. **El conector no tiene ninguna
operación de escritura sobre archivos existentes:**

- ✗ No puede mover archivos (no existe `update_file` ni cambio de padres).
- ✗ No puede borrar ni mandar a la papelera.
- ✗ No puede renombrar.
- ✗ No puede editar el contenido de un Doc ya creado.
- ✗ **No puede subir imágenes en la práctica.** `create_file` acepta
  `base64Content`, pero el parámetro de una imagen usable no cabe en una sola
  respuesta. Medido dos veces. Ver el paso 4.

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

Esta carpeta es **temporal** para las descargas. El Doc y el evento se entregan
en Drive y Calendar; las cinco imágenes se entregan a Cristián como archivos y
las arrastra él (paso 4).
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
| Informes procesados (dentro de Informes) | `{{PROCESADOS_ID}}` |
| Contenedor de las carpetas `video N`, confusamente llamado PROCESADOS | `{{PROCESADOS_ENTREGA_ID}}` |

No crees carpetas con fecha, ni carpetas semanales, ni ningún otro contenedor.
Trabaja directamente en la carpeta `video N`.

### Las carpetas `video N` van en la RAÍZ de entrega

Regla dada por Cristián: las cinco carpetas `video N` tienen que estar
**directamente dentro de la raíz de entrega**, la que él abre. Si no existen, se
crean ahí con `create_file` y `mimeType` `application/vnd.google-apps.folder`.
Dentro de cada una van su Doc y sus cinco imágenes, y nada más.

Existe una estructura VIEJA que **no se usa**: unas carpetas `video 1..5`
enterradas dentro de la carpeta `PROCESADOS` de la raíz. Cristián no las ve, y
por eso creía que no se generaba nada. Quedaron ahí porque el conector no puede
moverlas ni borrarlas. La estructura vieja era:

```
Raíz de entrega  {{RAIZ_ENTREGA_ID}}
└── PROCESADOS   {{PROCESADOS_ENTREGA_ID}}
    ├── video 1
    ├── video 2
    ├── video 3
    ├── video 4
    └── video 5
```

Las cinco `video N` son hijas de esa carpeta llamada `PROCESADOS`, la que está
dentro de la raíz de entrega. Si Cristián abre el enlace de la raíz, solo ve
`PROCESADOS` y cree que no se hizo nada.

Dos consecuencias:

1. **En la respuesta final, nunca le mandes el enlace de la raíz de entrega.**
   Manda el enlace directo de la carpeta `video N`, que es donde están las cosas.
2. El nombre `PROCESADOS` de esa carpeta es un accidente histórico: **no es** la
   carpeta de informes procesados. Para archivar el informe se usa
   `{{PROCESADOS_ID}}`, que es otra y está dentro de Informes. No las confundas.

El conector no puede mover carpetas, así que esta estructura no se puede
aplanar desde acá. Si molesta, Cristián arrastra las cinco a la raíz a mano y
los IDs siguen siendo los mismos.

`{{PROCESADOS_ID}}` es la única carpeta autorizada para archivar el informe, y
está dentro de Informes.
La otra carpeta llamada `PROCESADOS`, `{{PROCESADOS_ENTREGA_ID}}`, está dentro de
la raíz de entrega y **nunca** se usa para archivar informes — pero sí es la que
contiene las cinco carpetas `video N` (ver abajo). Mismo nombre, funciones
distintas: es la trampa más fácil de pisar de todo este proceso.

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

### Las imágenes NO se suben por el conector — la razón verdadera

Este documento culpó dos veces a la causa equivocada. Decía que el
`base64Content` no cabía en una respuesta. **Falso:** se emitieron 34 412
caracteres y llegaron byte-exactos, con `fileSize` idéntico al original. El
límite de salida no es el problema.

El problema real es la **fidelidad al copiar**. Reproducir decenas de miles de
caracteres de base64 exactamente falla, y falla de un modo que no se puede
detectar:

- Tasa medida: **un error cada ~25 000 caracteres**. Un JPEG de 700 px son
  31 000-33 000 caracteres, o sea ~1,3 errores esperados por imagen: alrededor
  de **25% de probabilidad de que una imagen suba limpia.**
- Los errores observados son del tipo peor: un carácter cambiado (`a` → `Y`) o
  un token repetido duplicado (`OkOboO` → `OkOboOboO`). **La longitud no cambia.**
- Drive **no devuelve `md5Checksum`** en `get_file_metadata`. Lo único
  comparable es `fileSize`, y con un error de un carácter el `fileSize` coincide.
  O sea: **una imagen corrupta se reporta como buena.**

### Por qué el md5 antes de subir tampoco alcanza

Se intentó este protocolo: leer el `.b64`, escribirlo a un archivo local,
comparar md5, y solo entonces subir. **No sirve, y conviene entender por qué
para no reinventarlo:** el md5 valida la escritura local, pero la llamada a
`create_file` es una **emisión nueva e independiente** de esos mismos 33 000
caracteres. Nada garantiza que la segunda salga igual que la primera, y ya no
hay forma de comprobarlo después.

Súmale que un archivo corrupto **no se puede borrar** y además **quema su
nombre**: nadie puede volver a usar `01-…jpg` hasta que Cristián lo borre a
mano. Con cinco imágenes, lo esperable es terminar con cuatro archivos rotos,
indetectables y permanentes.

### Entonces: las imágenes se entregan como archivos

`SendUserFile` con las cinco, y Cristián las arrastra a la carpeta `video N`.
Un gesto por video.

Ventaja que compensa el gesto: **sin base64 no hay presupuesto de bytes.** No
comprimas. Baja el original, reescala a 1920 px máximo, calidad 90. Quedan a
1280-1920 px en vez de los ~700 px que permitiría el conector.

En el mensaje de entrega pon el enlace de la carpeta `video N` de destino, para
que arrastrar sea inmediato.

### Si alguien insiste en subirlas por el conector

Que sea decisión explícita de Cristián, dicha por él, sabiendo que lo probable
es dejar la carpeta con archivos rotos que nadie puede borrar. En ese caso:
una imagen por corrida, tamaño mínimo, y avisando que la verificación
post-subida no existe.


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

## Paso 4 · Entregar las imágenes

El conector **no puede** subirlas de forma confiable: ver «Las imágenes NO se suben por el conector» más arriba.
El procedimiento real es este.

1. Deja las cinco en `/tmp/entrega/video-N/` con sus nombres definitivos
   (`01-...-AAAA-MM-DD.jpg` … `05-...-AAAA-MM-DD.jpg`).
2. Sin comprimir para caber: original, máximo 1920 px de ancho, calidad 90.
3. Arma un montaje de contacto con las cinco y **míralo** antes de entregar. Es
   una sola lectura y te ahorra mandar una imagen equivocada.
4. Entrégalas con `SendUserFile`, las cinco juntas, con un pie que diga a qué
   carpeta `video N` van.
5. En la respuesta final di, por cada imagen, de dónde salió y si es auténtica o
   generada.

Cristián las arrastra a la carpeta. Ese paso es manual y no hay forma de
evitarlo desde acá.

Lo que sí queda verificado en Drive es el Google Doc, que se crea sin problema
porque su contenido es texto y pesa poco. `videoN.status = OK` significa
entonces: Doc nativo creado y releído, evento de Calendar verificado, y las cinco
imágenes entregadas a Cristián.

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
3. Cada una tiene sus cinco imágenes de esta semana, o están entregadas
   a Cristián y él avisó que las arrastró. Si no las arrastró todavía, dilo y
   no lo trates como falla del proceso.
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

- carpeta `video N` — este es el enlace que sirve. **No mandes el de la raíz de
  entrega:** ahí Cristián solo ve `PROCESADOS` y parece que no se hizo nada.
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
