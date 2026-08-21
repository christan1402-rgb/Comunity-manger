# PLAYBOOK DEL ANALISTA — Informe diario de opciones AAPL · QQQ · SPY

> **Principio rector:** el movimiento implícito es tu **punto de equilibrio**, no tu objetivo.
> Comprar opciones no es apostar dirección; es apostar a que la magnitud supere lo ya cobrado
> en la prima. Se puede acertar la dirección y aun así perder dinero.

---

## 1. Rutina de la mañana (orden exacto)

1. **Fijar la fecha real** con el reloj del sistema (`TZ=America/New_York date`). Nunca asumirla.
2. **Consultar el calendario del día:** ¿hay FOMC? ¿resultados hoy o mañana? ¿dato macro a las 8:30?
   Esto define el régimen antes de mirar un solo precio.
3. **Cierres de ayer** de AAPL, QQQ, SPY + índices (S&P 500, NDX, Dow).
4. **Premarket actual** de los tres, con marca horaria al minuto.
5. **Contexto:** VIX, US10Y, US2Y, futuros ES/NQ, petróleo si hay shock energético.
6. **Aplicar las 18 reglas** de la sección 3.
7. **Decidir:** CALL / PUT / NO OPERAR para cada instrumento.
8. **Redactar** con la plantilla y enviar.

---

## 2. Los tres instrumentos no son intercambiables

| | AAPL | QQQ | SPY |
|---|---|---|---|
| Qué es | Acción individual | ETF Nasdaq-100 | ETF S&P 500 |
| Reporta resultados | **Sí** (trimestral, AMC) | No (lo hacen sus componentes) | No (íd.) |
| Vencimientos de opciones | **Lun, mié y vie** (desde 26-ene-2026) | **Los 5 días hábiles** | **Los 5 días hábiles** |
| Cierre de negociación | 16:00 ET | 16:15 ET | 16:15 ET |
| Fricción ida y vuelta (ATM 2d) | ~3,2% (hasta 8% a un strike) | ~2,4% | **~1,2%** |
| Sensibilidad a tasas | Media | **Alta** | Media |
| Peso de AAPL dentro | — | ~8,26% | ~7,76% |

**SPY es el vehículo por defecto.** Tiene los spreads más estrechos y la mayor liquidez;
la misma tesis cuesta menos de ejecutar. Solo se prefiere QQQ cuando la tesis es
específicamente sobre tecnología o tasas, y AAPL solo cuando hay catalizador propio de Apple.

**QQQ y SPY no tienen earnings, pero sí los tienen sus dueños.** Cuando Microsoft, Apple,
Amazon, Meta o Nvidia reportan, el ETF se revalúa por peso. OptionSlam no aplica a los ETF:
para ellos se mira el calendario de resultados de sus mayores componentes.

---

## 3. Las 18 reglas de decisión

### Lectura del premarket

**R1 — Umbral de significancia del gap, por instrumento.** El mismo porcentaje significa
cosas distintas en cada uno:

| | Ruido | Marginal | Empieza a importar | Significativo | Evento |
|---|---|---|---|---|---|
| **AAPL** | <0,30% | 0,30–0,75% | 0,75–1,50% | 1,50–3,00% | >3% |
| **QQQ** | <0,20% | 0,20–0,40% | 0,40–0,80% | 0,80–1,25% | >1,25% |
| **SPY** | <0,15% | 0,15–0,30% | 0,30–0,50% | 0,50–1,00% | >1,00% |

**Si los tres están bajo umbral, el sesgo del día es NEUTRAL por defecto.**

**R2 — Aislar el movimiento propio de AAPL antes de opinar.**
`AAPL idiosincrático = %AAPL − (1,15 × %SPY)`.
Si el residuo es menor a 0,15 puntos porcentuales, **Apple no tiene noticia propia**: no
construyas una tesis específica sobre ella, solo se está moviendo con el mercado.

**R3 — El premarket dice dónde hay una oferta, no dónde va a abrir.** AAPL negocia el 2–5%
de su volumen diario antes de las 9:30; los spreads son 10–30 veces más anchos, solo hay
órdenes limitadas y no hay flujo institucional real. **Un dato de las 07:10 vale mucho menos
que el mismo dato a las 09:25.** Y nunca uses el listado de *gainers* premarket como señal
direccional: suele estar copado por microcaps sin relación con el mercado amplio.

**R4 — Esperar los primeros 15–30 minutos.** El rango de 9:30–10:00 es más informativo que
todo el premarket junto. Los gaps se rellenan por descubrimiento de precio en la subasta de
apertura, toma de beneficio de quien compró de madrugada y *fade* sistemático de los
creadores de mercado. Solo asume continuación si se dan las tres: catalizador fundamental
duro, volumen de apertura muy superior a la media, y el precio no vuelve a entrar en el
rango del día previo en 30–60 minutos.

### Volatilidad

**R5 — Semáforo del VIX.**

| Nivel | Lectura | Acción |
|---|---|---|
| <13 | Complacencia | Cobertura barata; cuidado con vender prima |
| 15–20 | Normal | Operativa habitual |
| **20–22** | **Cambio de régimen** | **Reducir tamaño a la mitad** |
| >25 | Estrés | No abrir direccionales comprados salvo que la tesis *sea* la volatilidad |

Lo que se vigila no es tanto el nivel como **la ruptura** de la zona 20–22 tras un catalizador.

### Días de FOMC

**R6 — Antes de las 14:00: no abrir direccional nuevo.** De 10:00 a 13:00 el rango se
comprime. La ventana **13:50–13:59 es una trampa de ejecución**: el libro se adelgaza y los
spreads se ensanchan justo cuando más gente quiere entrar. Si vas a posicionarte, hazlo
**antes de las 13:30** y siempre con orden límite.

**R7 — Después de las 14:00: no confundir el spike con la dirección.** El movimiento inicial
(algoritmos leyendo titulares en segundos) **se revierte con frecuencia entre 14:00 y 14:15**,
cuando los humanos terminan de leer el comunicado completo. Con comunicados cortos y sin
orientación futura, la volatilidad real migra al turno de preguntas (14:30–15:30). El
colapso final de volatilidad llega entre 15:30 y 16:00.

**R8 — Distinguir reunión con proyecciones y sin ellas.** Las reuniones marcadas con
asterisco en el calendario de la Fed (marzo, junio, septiembre, diciembre) publican el
*Summary of Economic Projections* y el gráfico de puntos: son **dos shocks simultáneos** a
las 14:00, y los puntos suelen mover más que el texto. Sin proyecciones, el potencial del
spike de las 14:00 baja y el peso de la rueda de prensa sube.

**R9 — Regla de asimetría.** Antes de tomar sesgo, pregunta **qué está ya en precio**. Si el
escenario base tiene ~65% y ya está descontado, el alivio al confirmarse es delgado; si la
cola del 35% rompe una premisa estructural, el golpe es desproporcionado. **Cuando la cola
gorda apunta contra tu sesgo, el tamaño se reduce, no se aumenta.**

### Días de resultados

**R10 — Víspera de resultados: la volatilidad implícita NO colapsa.** El manual del *IV crush*
post-evento no aplica a un subyacente con resultados pendientes. Hay que separar instrumento
por instrumento: un ETF sin earnings de componentes esa noche tiene colapso limpio; uno con
componentes reportando lo tiene parcial; y **una acción que reporta esa misma tarde no
colapsa, incluso puede subir**. Vender volatilidad de una acción la víspera de sus
resultados es ponerse corto de vega justo antes del evento: uno de los errores peor pagados.

**R11 — Comprar opciones antes de resultados solo si se cumplen las CUATRO condiciones:**
1. El histórico muestra >50% de *Outside moves* (la acción se movió más de lo implícito).
2. El implícito actual está **por debajo** del movimiento real histórico.
3. El *Earnings Volatility Rating* de OptionSlam es alto (7–10).
4. Hay un catalizador atípico que el mercado no ha valorado.

**Si falla alguna, no se compra volatilidad direccional.** Este es el filtro más importante
del playbook y el que más dinero ahorra.

**R12 — *Movement* no es *Max Move*.** *Movement %* mide del cierre previo al cierre del día
siguiente. *Max %* mide del cierre previo al extremo intradía. Una acción puede superar el
implícito en el extremo (*Outside*) y aun así dejar al comprador del straddle en pérdida,
porque cerró mucho más cerca. **Acertar la magnitud intradía no te salva si no sales en el
extremo exacto.**

**R13 — Preferir la mediana a la media.** La media se infla con dos o tres trimestres
atípicos. La mediana describe el trimestre típico. Mira además la tendencia de los últimos
8 trimestres: dice si la acción se está calmando o acelerando.

**R14 — El día posterior al reporte, el gap no es negociable.** No hay ejecución posible
dentro del hueco: un stop colocado ahí se ejecuta al primer precio del otro lado. Y la
dirección la marca **la guía futura, no el trimestre pasado** — hay compañías que reportan
crecimiento de doble dígito y caen por lo que anuncian sobre el gasto futuro. Los primeros
15–30 minutos son ruido de reposicionamiento. El comprador sufre vega y theta la misma mañana.

### Correlación y macro

**R15 — Aritmética de correlación AAPL → QQQ → SPY.**
`Δ Índice = Peso × Δ Componente`. Con AAPL al ~8,26% de QQQ y ~7,76% de SPY:
**AAPL ±5% mueve mecánicamente QQQ ±0,41% y SPY ±0,39%.**
Eso es el **piso mecánico**. Multiplica por **1,5x–2,5x** si el reporte cambia la narrativa
del sector (contagio a proveedores, lectura de régimen sobre el gasto en IA, correlación del
top 5). **Ningún resultado individual mueve al ETF de forma decisiva solo por peso.**

**R16 — En día FOMC, QQQ se mueve 1,2x–1,5x lo que SPY, en la misma dirección.** Cinco
razones acumulativas: (a) mayor duración —el descuento castiga mucho más los flujos lejanos,
0,5 puntos de tasa cuestan ~0,5% a un flujo a un año y ~7% a uno a quince—; (b) **cero
financieras**, que en SPY pesan ~13% y se benefician de tasas altas; (c) **cero energía**,
relevante en shocks de petróleo; (d) mayor concentración (top 10 ~45,7% vs ~36,7%); (e) sin
colchón de dividendo.

**R17 — Días de datos macro: respetar el apilamiento.** Cuando varios datos salen en el
mismo instante (por ejemplo PIB + PCE + peticiones de desempleo a las 8:30), la reacción
inicial es algorítmica y **suele revertirse parcialmente en la primera media hora**.
**No operar el primer print; esperar 30 minutos.** Aplica a NFP, CPI y PPI por igual.

### La decisión de no operar

**R18 — Checklist de NO OPERAR.** Marca cualquiera de estas y el día es de espera:

- [ ] Los tres instrumentos están bajo su umbral de significancia (R1).
- [ ] Hay un evento binario programado en menos de 6 horas y la posición no lo tiene como tesis.
- [ ] El implícito está en línea o por encima del movimiento real histórico → no hay ventaja en ninguna dirección.
- [ ] El histórico está dominado por *Inside moves*.
- [ ] Se apilan dos catalizadores de distinta naturaleza en menos de 30 horas (Fed + resultados).
- [ ] El sesgo depende de una asimetría direccional con muestra pequeña (n≤12 trimestres no permite afirmar dirección: 8 de 12 en la misma dirección da p≈0,19 bajo azar puro, es **ruido**).
- [ ] El VIX rompe 22 sin catalizador identificable.
- [ ] El contrato candidato falla el filtro de liquidez (ver §4).

> **Sobre el *pre-FOMC drift*:** existió y fue enorme (49 puntos básicos entre 1994 y 2011,
> ~80% de la prima de riesgo anual concentrada en el 3% del tiempo), pero está degradado
> desde 2015 y **es condicional**: funciona en alta volatilidad con asimetría neutra o
> favorable. Invocarlo cuando la asimetría está invertida es aplicar una regla estadística
> fuera de su régimen de validez.

---

## 4. Reglas de ejecución

| Regla | Valor |
|---|---|
| Vencimiento mínimo | **5 días hábiles.** Nada de 0DTE |
| Delta objetivo | **0,40–0,60.** Prohibido por debajo de 0,20 |
| Vehículo por defecto | **SPY** (menor fricción) |
| Prima total por idea | **≤1–2% del capital** |
| Ideas abiertas a la vez | **Máximo 2** |
| Tipo de orden | **Siempre LIMIT**, nunca a mercado |
| Cierre obligatorio | Antes de las **15:45** del día de vencimiento |
| Permiso IBKR necesario | **Nivel 2** (compra de calls/puts sueltas) |

**Filtro de liquidez** — el contrato debe cumplir las cuatro: spread <2% del punto medio ·
interés abierto >1.000 · volumen del día previo >500 · prima >0,20 USD.

**Dimensionar sobre la prima, no sobre el stop.** En opciones compradas el riesgo real es la
**prima entera**: un hueco de apertura o una noticia nocturna la llevan a cero antes de que
exista la posibilidad de vender. Si un solo contrato representa más del 2% del capital, la
idea **no cabe en la cuenta** y hay que decirlo abiertamente.

**Correlación disfrazada de diversificación.** Tres ideas alcistas en SPY, QQQ y AAPL no son
tres operaciones: son **una apuesta apalancada por tres** al mismo factor. El informe indica
siempre la exposición agregada.

**Asignación por olvido.** Los tres liquidan con **entrega física** y la OCC ejerce
automáticamente cualquier opción que venza 0,01 USD o más dentro del dinero. Una call
olvidada puede dejar 100 acciones —decenas de miles de dólares— en la cuenta el lunes.
Los ejercicios son irrevocables.

---

## 5. Los siete errores más caros

1. **Creer que se apuesta la dirección.** Se apuesta la magnitud contra el precio pagado.
   Compras calls con implícito del 4%, la acción sube 2%: acertaste y perdiste.
2. **El IV crush, en aritmética.** Call ATM con delta 0,50 y vega 0,30. El subyacente sube
   2,00 USD: +1,00 por delta, **−1,50 por vega** (5 puntos de caída de IV), −0,10 de theta =
   **−0,60 neto**. Subió y perdiste.
3. **Las OTM baratas son el peor instrumento para un evento.** Son 100% valor extrínseco:
   vega y theta puros, sin nada intrínseco que las sostenga. Una call con prima de 0,01 USD y
   delta 0,003 tiene bid 0,00: se pierde el 100% en el instante de comprar porque no hay a
   quién vendérsela. *(Y el mito de que «el 80–90% de las opciones expiran sin valor» es
   falso: ~10% se ejercen, 55–60% se cierran antes, **30–35%** expira sin valor. La cifra
   honesta está en pantalla y se llama delta.)*
4. **Las 0DTE pierden theta de golpe, no gradualmente.** El mismo strike pierde ~99% de la
   prima al día en vencimiento inmediato, ~21% a 2 días, ~5% a 9 días, ~2% a 23 días. En una
   0DTE hay que acertar dirección, magnitud **y momento** en seis horas y media, con gamma
   violento y un spread que pesa el triple sobre una prima que se evapora.
5. **Dimensionar sobre el stop.** Ver §4.
6. **Fricción invisible.** La comisión de IBKR (0,65 USD por contrato, ida y vuelta
   ~1,40–1,60 USD) es irrelevante sobre una prima de 700 USD (0,2%) y **decisiva** sobre una
   de 20 USD (7%). El spread pesa más que la comisión.
7. **Sacar conclusiones de muestras pequeñas.** La magnitud (Inside/Outside) es la métrica
   fiable del histórico de earnings; **la dirección es la menos fiable del panel**.

---

## 6. Glosario

1. **CALL** — Derecho a comprar 100 acciones a un precio fijo antes de una fecha. Gana si sube.
2. **PUT** — Derecho a vender 100 acciones a un precio fijo. Gana si baja, y es la forma más
   simple de cubrirse sin vender lo que se tiene.
3. **Strike** — El precio fijo pactado; el nivel desde el que la opción tiene valor real al vencer.
4. **Prima** — El precio de la opción, cotizado por acción. **Multiplica siempre por 100**
   para saber los dólares que salen de la cuenta: prima 4,26 = **426 USD**.
5. **Vencimiento** — La fecha en que el contrato deja de existir. Si la tesis no se cumple
   antes, el dinero desaparece con él.
6. **ATM / ITM / OTM** — El strike está pegado al precio (*at the money*), ya es favorable
   (*in*), o todavía no lo es (*out*, barata precisamente porque hoy no vale nada).
7. **Volatilidad implícita (IV)** — El precio del nerviosismo. Cuando está alta, las opciones
   están caras; sube antes de todo evento con fecha conocida.
8. **Delta** — Cuánto se mueve la opción por cada dólar del subyacente (delta 0,50 = 50 USD
   por contrato) y, a la vez, la **probabilidad aproximada** de terminar dentro del dinero.
9. **Theta** — El alquiler diario que paga el comprador solo por el paso del tiempo. Siempre
   negativo, y corre también en fines de semana.
10. **Vega e IV crush** — Vega mide cuánto pierde la opción si la volatilidad cae un punto.
    El *IV crush* es esa caída de golpe en cuanto el evento se conoce. Es lo que hace que
    puedas **acertar la dirección y aun así perder dinero**.

---

## 7. Cómo se leen las métricas de OptionSlam

| Métrica | Qué es | Cómo se usa |
|---|---|---|
| **Implied Move** | El movimiento que el mercado ya está cobrando en la prima | Es tu **punto de equilibrio**, no tu objetivo |
| **Movement %** | Cierre previo → cierre del día siguiente al reporte | La realidad que cobra quien aguanta |
| **Max Move %** | Cierre previo → extremo intradía | Solo la captura quien sale en el extremo exacto |
| **Inside / Outside** | Si el movimiento real quedó dentro o fuera del implícito | **>50% Outside** es condición para comprar volatilidad |
| **EVR** (1–10) | *Earnings Volatility Rating*: cuán reactiva es la acción a sus propios resultados | EVR bajo = la acción apenas reacciona = no pagues por movimiento |

**Regla de oro:** si el implícito es mayor que el movimiento real histórico mediano, el
comprador de opciones parte perdiendo. Ahí la operación no es comprar: es no operar.

---

## 8. Aviso

Documento de análisis de mecánica de mercado y calendario. **No constituye recomendación
personalizada de inversión.** Las opciones compradas pueden perder el 100% de la prima.
Los precios de referencia de cualquier informe tienen corte al momento de su redacción y
estarán desactualizados a la apertura. Cada decisión es responsabilidad exclusiva del
titular de la cuenta.
