# FUENTES — verificadas el 29 de julio de 2026

Todas estas URLs fueron probadas una a una. Las de nivel 1 respondieron con datos reales y
marca horaria. Las bloqueadas devolvieron error, CAPTCHA o HTML vacío.

---

## Nivel 1 — funcionan, se usan a diario

### Precios y premarket

| Necesidad | URL | Nota |
|---|---|---|
| Premarket AAPL | `https://stockanalysis.com/stocks/aapl/` | **La mejor.** Precio, cambio, % y **marca horaria al minuto**. Sin CAPTCHA ni JavaScript |
| Premarket QQQ / SPY | `https://stockanalysis.com/etf/qqq/` · `/etf/spy/` | Ídem |
| Screener premarket | `https://stockanalysis.com/markets/premarket/gainers/` · `/losers/` | Columnas: Symbol · Company · %Change · **Premkt. Price** · **Pre. Volume** · Market Cap |
| Verificación cruzada | `https://finviz.com/quote.ashx?t=AAPL` (QQQ, SPY) | Sello horario propio + titulares |
| Histórico OHLC | `https://query2.finance.yahoo.com/v8/finance/chart/AAPL?range=4y&interval=1d` | **query2**, no query1 (query1 devuelve 429) |

### Volatilidad y tasas

| Necesidad | URL | Nota |
|---|---|---|
| **VIX en tiempo real** | `https://www.investing.com/indices/volatility-s-p-500` | Marcado "Real-time Data" |
| **Bono 10 años** | `https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield` | Marcado "Real-time Data" |
| Futuros ES / NQ | `https://www.investing.com/indices/us-spx-500-futures` · `/indices/nq-100-futures` | **Retraso de ~10 min**, marcados *Delayed* |

### Reserva Federal

| Necesidad | URL | Nota |
|---|---|---|
| **Calendario FOMC (primaria)** | `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` | Fechas + asterisco de proyecciones + enlaces a documentos |
| Tasa vigente (primaria) | `https://www.federalreserve.gov/monetarypolicy/openmarket.htm` | Historial de decisiones |
| Probabilidades de tasas | `https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html` | Widget JavaScript: **abrir en navegador, no se puede leer por programa** |

### Calendarios macro (todos primarios)

- PIB y PCE — `https://www.bea.gov/news/schedule`
- Empleo, CPI, PPI, ECI, JOLTS — `https://www.bls.gov/schedule/`
- Nóminas no agrícolas — `https://www.bls.gov/schedule/news_release/empsit.htm`
- Peticiones de desempleo — `https://oui.doleta.gov/unemploy/claims.asp`

### Opciones y resultados

| Necesidad | URL | Nota |
|---|---|---|
| **Cadenas de opciones + griegas** | `https://cdn.cboe.com/api/global/delayed_quotes/options/SPY.json` (QQQ, AAPL) | JSON completo: bid/ask, IV, delta, theta, vega, interés abierto. **Retrasado** |
| Fechas oficiales de Apple | `https://data.sec.gov/submissions/CIK0000320193.json` | Los 8-K con las fechas reales |
| Movimiento implícito | `https://www.optionslam.com/earnings/stocks/AAPL` · `/earnings/straddle/AAPL` | Gratis: implícito semanal/mensual, EVR, 1–2 trimestres |
| Definiciones OptionSlam | `/help/implied_move/` · `/help/track_rating/` · `/help/volatility_filter/` | Fórmula, EVR, Inside/Outside |
| Composición de los ETF | `https://stockanalysis.com/etf/qqq/holdings/` · `/etf/spy/holdings/` | Con fecha de corte trazable |
| IBKR | `ibkrguides.com/clientportal/optionstradingpermissions.htm` · `interactivebrokers.com/en/pricing/commissions-options.php` | Descarga directa |

---

## Bloqueadas — y con qué se sustituyen

| Bloqueada | Motivo | Sustituto |
|---|---|---|
| **marketwatch.com** (screener premarket y cotizaciones) | HTTP 401 + CAPTCHA DataDome + `robots.txt: Disallow: /` de Dow Jones. **No se intenta evadir: violaría sus condiciones de uso** | **stockanalysis.com** — da lo mismo y además publica volumen premarket |
| cnbc.com/pre-markets y `/quotes/*` | HTTP 403 | investing.com + stockanalysis. Los artículos con fecha en la URL sí son accesibles |
| marketchameleon.com | Bloqueo anti-bot | Reconstruir el histórico con SEC EDGAR + Yahoo query2 |
| finviz.com/futures.ashx | Carga pero sin cifras (JavaScript) | investing.com |
| stooq.com (CSV) | Reto JavaScript | Yahoo query2 |
| unusualwhales · optioncharts.io · oquants | Datos por JavaScript, HTML vacío | Cboe JSON |
| slickcharts.com/nasdaq100 | HTTP 403 | stockanalysis holdings |
| invesco.com (holdings) | Aplicación de página única, no carga | stockanalysis holdings |
| bls.gov/schedule/news_release/cpi.htm y ppi.htm | 503 intermitente | `usinflationcalculator.com/inflation/consumer-price-index-release-schedule/` + `bls.gov/schedule/2026/08_sched.htm` |
| nasdaq.com/../aapl/earnings · investor.apple.com · earningswhispers | JavaScript / "Data not available" | Nota de prensa de la empresa + stockanalysis |

---

## Sobre MarketWatch

Es una de las tres fuentes originalmente pedidas, así que conviene ser explícito: **su
screener premarket no es accesible por programa.** Dow Jones lo protege con `Disallow: /`
en robots.txt, autenticación y CAPTCHA comercial. Se puede consultar perfectamente **a mano
en un navegador** — y merece la pena hacerlo —, pero una rutina automática no puede leerlo
sin saltarse sus condiciones de uso, y eso no se hace.

El sustituto, `stockanalysis.com/markets/premarket/gainers/`, entrega exactamente los mismos
campos y además el **volumen premarket por ticker**, que MarketWatch no siempre muestra.

---

## Dos trampas comprobadas

1. **`optionslam.com/earnings/stocks/ZZZZ` devuelve HTTP 200 con un ticker inventado.**
   El código de estado no sirve como validación: hay que validar el ticker antes de creerse
   la página.
2. **El formato `optionslam.com/earnings/AAPL` no existe** (redirige 301 a un 404).
   La ruta correcta lleva `/stocks/` en medio.
