# CALENDARIO — eventos que mueven AAPL, QQQ y SPY

Verificado el 29 de julio de 2026 contra fuentes primarias.

---

## 1. Reuniones del FOMC

Fuente primaria: `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`
(confirmado carácter por carácter en el HTML crudo, por tres verificadores independientes).

### 2026

| Reunión | Proyecciones (dot plot) |
|---|---|
| 27–28 enero | — |
| 17–18 marzo | **Sí** |
| 28–29 abril | — |
| 16–17 junio | **Sí** |
| **28–29 julio** | — |
| 15–16 septiembre | **Sí** |
| 27–28 octubre | — |
| 8–9 diciembre | **Sí** |

### 2027 (tentativo, ya publicado)

| Reunión | Proyecciones |
|---|---|
| 26–27 enero | — |
| 16–17 marzo | **Sí** |
| 27–28 abril | — |
| 8–9 junio | **Sí** |
| 27–28 julio | — |
| 14–15 septiembre | **Sí** |
| 26–27 octubre | — |
| 7–8 diciembre | **Sí** |

Nota al pie literal de la Fed: *"\* Meeting associated with a Summary of Economic Projections."*

### Mecánica de un día de decisión (hora de Nueva York)

| Hora | Qué pasa |
|---|---|
| 10:00–13:00 | Rango comprimido, poco volumen |
| **13:50–13:59** | **Trampa de ejecución:** el libro se adelgaza, los spreads se ensanchan |
| **14:00** | Comunicado + nota de implementación (+ proyecciones si la reunión lleva asterisco) |
| 14:00–14:15 | Spike algorítmico que **se revierte con frecuencia** cuando los humanos leen el texto completo |
| **14:30** | Rueda de prensa del presidente de la Fed |
| 14:38–15:30 | Turno de preguntas — **donde suele vivir la volatilidad real** con comunicados cortos |
| 15:30–16:00 | Colapso final de volatilidad |

Las actas de cada reunión se publican **tres semanas exactas después**.

**Las horas 14:00 / 14:30 no figuran en el calendario de la Fed** (esa página solo lista
fechas). Son el estándar desde 2013, confirmado contra las reuniones previas.

---

## 2. Resultados de Apple

Apple reporta **después del cierre** (AMC), con conferencia telefónica a las 17:00 ET.

- **Q3 fiscal 2026: jueves 30 de julio de 2026, AMC.** Confirmado en el anuncio oficial de
  Apple del 2 de julio y contrastado con stockanalysis.com.
- El movimiento se materializa en la **sesión del día siguiente**, no en la del reporte.
- Ritmo histórico: finales de octubre (Q4), finales de enero (Q1), finales de abril (Q2),
  finales de julio (Q3).

### Comportamiento histórico de AAPL ante sus propios resultados

Reconstruido desde los 8-K de la SEC + precios OHLC de Yahoo, validado contra la fila
gratuita de OptionSlam:

| Métrica | Valor |
|---|---|
| Movimiento real **mediano** (12 trimestres) | **1,01%** |
| Movimiento real **medio** (12 trimestres) | 2,07% |
| Últimos 8 trimestres (media) | **1,63%** — se está calmando |
| Trimestres que superaron el implícito semanal (3,79%) | **2 de 12** (17%) |
| Trimestres que superaron el implícito mensual (6,08%) | **0 de 12** |
| **EVR de OptionSlam** | **1,4 sobre 10** |

**Lectura:** AAPL es estructuralmente **poco reactiva** a sus propios resultados. El mercado
cobra sistemáticamente más movimiento del que entrega. Comprar su volatilidad antes del
reporte es, con este histórico, una operación con ventaja negativa.

---

## 3. Componentes que mueven QQQ y SPY

Los ETF no reportan; sus dueños sí. Pesos aproximados (cortes del 24 y 27 de julio de 2026 —
verificar el archivo de composición del día antes de dimensionar):

| Empresa | Peso en QQQ | Peso en SPY |
|---|---|---|
| **Apple** | 8,26% | 7,76% |
| **Microsoft** | 4,82% | 4,53% |
| **Amazon** | 4,15% | 3,55% |
| **AMD** | 3,72% | 1,27% |
| **Meta** | 2,93% | 2,05% |
| Walmart | 2,51% | — |
| Eli Lilly | — | 1,49% |

Distintos proveedores dan cifras algo diferentes para AAPL en QQQ (8,26% / 8,13% / 6,66%
según la fuente y la fecha de corte).

### Aritmética de contagio

`Δ Índice = Peso × Δ Componente`

- **AAPL ±5% → QQQ ±0,41%, SPY ±0,39%** (piso mecánico)
- Multiplicar por **1,5x–2,5x** si el reporte cambia la narrativa del sector

---

## 4. Datos macro — próximas semanas

| Fecha | Hora ET | Dato | Fuente |
|---|---|---|---|
| Jue 30 jul | 8:30 | **PIB 2T (avance)** + **PCE de junio** + peticiones de desempleo | BEA / DOL |
| Vie 31 jul | 8:30 | Índice de Costo del Empleo (ECI) 2T | BLS |
| Mar 4 ago | 8:30 / 10:00 | Balanza comercial + **JOLTS** | BEA / BLS |
| Jue 6 ago | 8:30 | Productividad y costos 2T + peticiones | BLS / DOL |
| **Vie 7 ago** | 8:30 | **Nóminas no agrícolas (NFP) de julio** | BLS |
| **Mié 12 ago** | 8:30 | **CPI de julio** — el dato del mes | BLS |
| **Jue 13 ago** | 8:30 | **PPI de julio** + peticiones | BLS / DOL |
| Mar 18 ago | 8:30 | Precios de importación y exportación | BLS |
| Jue 20 ago | 8:30 | Peticiones + **Walmart** Q2 (antes de la apertura) | DOL / Walmart |

El **PCE** es la medida de inflación preferida por la Fed: pesa más que el CPI en sus decisiones.

---

## 5. Fechas NO confirmadas en fuente primaria

No se opera sobre ellas sin verificar antes:

- **NVIDIA** ~26 de agosto AMC — varios calendarios coinciden, sin nota de prensa de la empresa
- Cisco ~19 de agosto · Broadcom ~3 de septiembre · Micron y Costco ~finales de septiembre
- Berkshire ~primer sábado de agosto · Exxon ~1 de agosto
- Ventas minoristas de julio ~14 de agosto
- Actas del FOMC de la reunión de julio: **~miércoles 19 de agosto** (inferido de la regla de
  tres semanas, no dato oficial)

---

## 6. Dos vacíos de calendario que cambian el régimen

**Concentración.** Entre la tarde del 29 y la del 30 de julio se revalúa el **20,16% de QQQ**
y el **17,89% de SPY** (Microsoft y Meta el miércoles; Apple y Amazon el jueves). Dos días
deciden una quinta parte del índice.

**Sequía.** Después del 5 de agosto no hay resultados de megacapitalización relevantes hasta
NVIDIA (~26 de agosto). Del 6 al 25 de agosto el mando pasa **íntegramente a la macro**:
nóminas el 7, CPI el 12, PPI el 13.
