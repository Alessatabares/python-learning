# 🔧 Sala de Simulación · Datos — Romper y Predecir

Juego de una sola página (HTML + JS vanilla, sin build) para practicar la dirección
**inversa** del pipeline de datos: en lugar de limpiar paso a paso, **predices** qué
romperá un cambio —y, en la parte estadística, qué conclusión es tramposa— *antes* de
ver la terminal.

## El tablero

Un solo pipeline, clicable:

```
Carga → Tipos → Faltantes → Transformar → Unir → Resumen → Inferencia
```

Cada escenario te da el **código (o la lectura) sano** y el **cambio** que lo rompió.
Tú predices **dónde muere** (qué etapa) y **qué síntoma** sale. La terminal queda
**oculta hasta que aciertas** etapa + síntoma.

## La dirección que entrena

| Juego | Dirección | Qué entrena |
|-------|-----------|-------------|
| `juego-data` | guiado | ves cómo cada comando transforma la tabla |
| `juego-comandos-data` | reconocer → teclear | escribes los comandos de memoria |
| **este** | **causa → efecto** | te doy el cambio; predices dónde muere y qué síntoma |

## Contenido: 9 escenarios

- **🩺 Limpieza:** `astype` vs `to_numeric` (ValueError), `fillna(0)` que hunde la media
  (bug silencioso), `dropna()` que arrasa, `merge` inner que pierde pacientes, `if` sobre
  una Series (truth value ambiguous).
- **📊 Análisis:** promediar texto (parece Resumen, es Tipos), IC que cruza el nulo,
  I² alto con efectos fijos, saltar de la muestra a la población sin IC.

## Las trampas (a propósito)

- **Engañosos:** el error aparece en `Resumen` pero la causa está en `Tipos`; un `merge`
  que parece conservarlo todo y pierde filas.
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
