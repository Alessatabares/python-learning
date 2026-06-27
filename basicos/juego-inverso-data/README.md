# 🔧 Sala de Simulación · Datos — Romper y Predecir

Juego de una sola página (HTML + JS vanilla, sin build) para practicar la dirección
**inversa** del pipeline de datos: en lugar de limpiar paso a paso, **predices** qué
romperá un cambio —y, en la parte estadística, qué conclusión es tramposa— *antes* de
ver la terminal.

## El tablero

El **mismo pipeline del `juego-data`**, clicable, con su dataset (Ana · Luis · Sofía · Marco):

```
Signos vitales → Tipos → Faltantes → Transformar → Inferir
```

Cada escenario te da el **código (o la lectura) sano** y el **cambio** que lo rompió.
Tú predices **en qué estación muere** y **qué síntoma** sale. La terminal queda
**oculta hasta que aciertas** estación + síntoma.

## La dirección que entrena

| Juego | Dirección | Qué entrena |
|-------|-----------|-------------|
| `juego-data` | guiado | ves cómo cada comando transforma la tabla |
| `juego-comandos-data` | reconocer → teclear | escribes los comandos de memoria |
| **este** | **causa → efecto** | te doy el cambio; predices dónde muere y qué síntoma |

## Contenido: 9 escenarios (las 5 estaciones del juego-data)

- **🩺 Limpieza (1–3):** `astype` vs `to_numeric` (la edad "unknown" → ValueError),
  `fillna(0)` que hunde la media de glucosa (bug silencioso), `dropna()` que borra a Luis
  por un solo hueco.
- **📊 Transformar e inferir (4–5):** `merge` inner que pierde a Marco, `if` sobre una
  Series (truth value ambiguous), promediar texto (parece Transformar, es Tipos), IC que
  cruza el nulo, I² alto con efectos fijos, saltar de la muestra a la población sin IC.

## Las trampas (a propósito)

- **Engañosos:** el error aparece en `Transformar` (el groupby) pero la causa está en
  `Tipos`; un `merge` que parece conservarlo todo y pierde a Marco.
- **Bugs silenciosos:** `fillna(0)` no lanza error, pero corrompe la media.
- **Trampas estadísticas:** un IC que cruza 0 NO es `p<0.05`; I² alto no significa "no
  sirve"; la media muestral no es la poblacional.

## Correr

Abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-inverso-data
python -m http.server 8005
# luego abre http://localhost:8005
```
