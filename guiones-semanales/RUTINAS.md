# LAS CINCO RUTINAS

Cinco tareas programadas, una por video. Todas los domingos, hora de Chile.

| Tarea | Hora Santiago | Cron UTC (invierno, UTC−4) | Cron UTC (verano, UTC−3) | Historia | Día que agenda |
|---|---|---|---|---|---|
| `guion 1` | 10:00 | `0 14 * * 0` | `0 13 * * 0` | 1 | lunes |
| `guion 2` | 10:30 | `30 14 * * 0` | `30 13 * * 0` | 2 | martes |
| `guion 3` | 11:00 | `0 15 * * 0` | `0 14 * * 0` | 3 | miércoles |
| `guion 4` | 11:30 | `30 15 * * 0` | `30 14 * * 0` | 4 | jueves |
| `guion 5` | 12:00 | `0 16 * * 0` | `0 15 * * 0` | 5 | viernes |

Cada rutina abre una sesión nueva y termina con una notificación al teléfono.

## Cómo se encadenan sin compartir archivos

Cada rutina arranca en un contenedor limpio, sin nada de lo que dejó la
anterior. El encadenado no depende de eso: es determinista.

- Las cinco leen **el mismo informe**: el archivo directo más reciente de la
  carpeta de Informes. Nosotros nunca modificamos el informe, así que las cinco
  llegan al mismo.
- `guion N` toma **la historia número N**, en el orden original del informe.
  Ninguna necesita saber qué hizo otra.
- La semana de grabación sale de la fecha de ejecución: si corre domingo, es el
  lunes siguiente. Las cinco corren el mismo domingo, así que coinciden.

Media hora entre tareas es holgura, no dependencia. Si `guion 2` se atrasa o
falla, `guion 3` sigue siendo correcto.

## El cambio de hora de Chile

El cron se guarda en UTC y Chile cambia de hora dos veces al año. Cuando pasa,
las cinco rutinas se corren una hora y hay que ajustarlas.

- **Primer domingo de septiembre** — empieza el horario de verano, UTC−4 → UTC−3.
  Los cinco cron bajan una hora (`0 14` → `0 13`).
- **Primer domingo de abril** — termina, UTC−3 → UTC−4.
  Los cinco cron suben una hora (`0 13` → `0 14`).

Hay una rutina de una sola vez para cada cambio que lo hace sola y avisa. Es el
mismo mecanismo que usa el informe diario de opciones para el cambio de hora de
Nueva York.

## Verificar o cambiar las rutinas

- `list_triggers` — ver las cinco, su cron y su próxima ejecución.
- `update_trigger` — cambiar cron o prompt sin perder el historial. Es lo que
  hay que usar para corregir; no borrar y volver a crear.
- `fire_trigger` — dispararla ahora, fuera de horario, para probar.
- `delete_trigger` — solo para eliminarla de verdad.

Los IDs de las carpetas de Drive viven **dentro del prompt de cada rutina**, no
en este repositorio, porque el repositorio es público. Para cambiar una carpeta:
`update_trigger` sobre las cinco rutinas.

## Probar antes del domingo

`fire_trigger` sobre `guion 1` la dispara al instante. Con eso se comprueba de
una pasada: que encuentra el informe, que crea el Doc, que las cinco imágenes
suben, y que el evento queda en el calendario del lunes.

Sale un paquete real en Drive y un evento real en el calendario. El conector no
puede borrar ninguno de los dos, así que lo que salga de una prueba hay que
sacarlo a mano.
