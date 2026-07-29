# PLANTILLA DEL INFORME DIARIO

Objetivo: **leíble en 3–4 minutos**, sin jerga innecesaria, y que termine en acciones
concretas ejecutables en Interactive Brokers. Todo en español. Horas siempre en Nueva York.

**Asunto del correo:**
`Informe {AAPL·QQQ·SPY} — {día} {DD} de {mes} — {🟢 verde | 🟡 ámbar | 🔴 rojo}`

---

## Estructura

### 1. Termómetro del día (2–3 líneas)
El semáforo y por qué. Si hay un evento que domina la sesión, va aquí y en negrita.
Si la conclusión es no operar, se dice **en la primera línea**, no al final.

| | Significado |
|---|---|
| 🟢 **Verde** | Sesión legible, sin evento binario. Se puede operar direccional |
| 🟡 **Ámbar** | Hay un factor que exige tamaño reducido o esperar la primera media hora |
| 🔴 **Rojo** | Evento mayor o apilamiento de catalizadores. No abrir direccional nuevo |

### 2. Cómo cerró ayer
Tabla corta: AAPL, QQQ, SPY con cierre y variación. Una frase que explique **qué pasó de
verdad** (no «sesión mixta»: decir si fue rotación, si un sector arrastró al resto, etc.).

### 3. Cómo viene la mañana
Tabla de premarket con **marca horaria explícita**. Debajo, la lectura según el umbral de
significancia de cada instrumento (R1) y el residuo idiosincrático de AAPL (R2).
Si están todos bajo umbral, decirlo con estas palabras: **«el mercado no se ha pronunciado»**.

### 4. El contexto en cuatro números
VIX · bono a 10 años · futuros ES/NQ · un cuarto dato si hay shock (petróleo, divisas).
Cada uno con una frase de qué implica, no solo el número.

### 5. La agenda de hoy
Solo lo que ocurre **hoy y mañana**, con hora. Marcar qué es lo que realmente importa.
Si hay resultados después del cierre, decir que el movimiento llega **al día siguiente**.

### 6. Los tres instrumentos, uno por uno

Para cada uno — AAPL, QQQ, SPY:

- **Sesgo:** CALL / PUT / NO OPERAR
- **Por qué**, en dos o tres frases sin jerga
- **Niveles** que invalidan la idea
- Si hay operación concreta: **tipo · strike · vencimiento · delta aproximado · prima
  estimada · punto de equilibrio en el subyacente**
- La **línea de traducción obligatoria**:
  > «Si {instrumento} sube un 1%, esta posición gana ~X USD; si baja un 1%, pierde ~Y USD;
  > si no se mueve en 5 días, pierde ~Z USD solo por el paso del tiempo. Pérdida máxima: la
  > prima completa, W USD.»
- Si el contrato tiene la volatilidad implícita inflada, publicar **IV del contrato frente a
  su IV normal a 30 días**.

### 7. Lo que hoy NO se hace
Sección corta y explícita. Las trampas concretas de la sesión: qué no comprar, qué no vender,
qué no operar antes de qué hora. Aquí es donde el informe ahorra dinero.

### 8. Gestión de riesgo
Exposición agregada sugerida en % del capital, número máximo de ideas abiertas, y aviso
explícito si alguna idea **no cabe** en una cuenta pequeña.

### 9. Lo que no se pudo verificar
Lista honesta. Si un dato no se confirmó, va aquí como **NO VERIFICADO** con lo que el
lector debe abrir a mano. Nunca se rellena con una estimación presentada como hecho.

### 10. Aviso
> Documento de análisis de mecánica de mercado y calendario. No constituye recomendación
> personalizada de inversión. Las opciones compradas pueden perder el 100% de la prima.
> Precios con corte a la hora indicada; estarán desactualizados a la apertura.

---

## Reglas de redacción

- **Nunca inventar una cifra.** Sin fuente, va como NO VERIFICADO.
- Toda cifra de precio lleva **hora**. Un premarket sin marca horaria no sirve.
- Prima siempre traducida a dólares reales: `prima 4,26 = **426 USD**`.
- Nada de «podría subir o podría bajar». Si no hay sesgo, la respuesta es **NO OPERAR**, y
  eso es una conclusión, no una evasiva.
- Prohibido recomendar 0DTE y prohibido delta <0,20.
- Si el implícito supera el movimiento real histórico, decirlo con todas las letras:
  **no hay ventaja en comprar**.
- Negritas solo en lo accionable. Si todo está en negrita, nada lo está.
