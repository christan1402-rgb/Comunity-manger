# Comunity-manger

Dos sistemas automatizados que viven en este repositorio:

- **[Guiones semanales de reels](guiones-semanales/)** — cinco reels por semana escritos
  desde el informe de noticias y entregados listos para grabar en Drive y Calendar.
- **Informe diario de opciones** — lo que documenta este archivo, de aquí para abajo.

---

## Informe diario de opciones — AAPL · QQQ · SPY

Sistema de análisis previo a la apertura del mercado estadounidense para operar opciones
call y put en Interactive Brokers sobre tres instrumentos: **AAPL**, **QQQ** y **SPY**.

Cada día hábil, a las **8:00 AM hora de Nueva York**, una rutina automática consulta las
fuentes verificadas, aplica la metodología de este repositorio y envía por correo un
informe resumido, profesional y sin jerga innecesaria.

## Qué hay aquí

| Archivo | Para qué sirve |
|---|---|
| [`PLAYBOOK.md`](PLAYBOOK.md) | La metodología completa: las 18 reglas de decisión, ejecución, gestión de riesgo y glosario |
| [`FUENTES.md`](FUENTES.md) | URLs verificadas que funcionan, cuáles están bloqueadas y con qué se sustituyen |
| [`CALENDARIO-2026.md`](CALENDARIO-2026.md) | Fechas del FOMC, reportes de resultados y datos macro, con su fuente primaria |
| [`plantilla-informe.md`](plantilla-informe.md) | La estructura fija del correo diario |
| [`informes/`](informes/) | Histórico de informes emitidos |

## Cómo se decide

La pregunta que responde el informe no es «¿sube o baja?». Es **«¿el movimiento esperado
supera lo que ya está cobrado en la prima?»**. Comprar una opción no es apostar dirección:
es apostar magnitud contra precio pagado. Se puede acertar la dirección y perder dinero.

Por eso el sistema tiene tres salidas posibles cada mañana — **CALL**, **PUT** o
**NO OPERAR** — y la tercera es una conclusión legítima, no una falta de opinión.

## Verificación de datos

Ninguna cifra entra en un informe sin fuente citada. Los datos críticos (fechas del FOMC,
fechas de resultados, precios) se contrastan contra la fuente primaria y contra al menos
una fuente independiente. Lo que no se puede confirmar se publica como **NO VERIFICADO**,
nunca se rellena con una estimación.

## Aviso

Documento de análisis de mecánica de mercado y calendario. No constituye recomendación
personalizada de inversión. Las opciones compradas pueden perder el 100% de la prima.
Cada decisión de inversión es responsabilidad exclusiva del titular de la cuenta.
