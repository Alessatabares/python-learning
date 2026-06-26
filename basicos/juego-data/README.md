# Juego Data — Pipeline de Datos Clínicos

Sitio interactivo (HTML + JS vanilla, sin backend) para recorrer un pipeline de datos:
del dato crudo a la conclusión honesta.

## Idea

El dato entra crudo y sale analizable. Cada estación es un nodo de decisión —como en
el juego de triage—, y la tabla muta frente a ti mientras avanzas.

```
1 · Signos vitales → 2 · Tipos → 3 · Faltantes → 4 · Transformar → 5 · Inferir
   info()            to_numeric   dropna/fillna   groupby/merge      IC · I²
```

## Lo que ya está

- **Estación 2 · Tipos:** traducción literal *código ↔ tabla*. `to_numeric(errors="coerce")`
  corre de verdad sobre el array: `"unknown"` → `NaN`, y el `dtype` pasa de `object 🚩`
  a `float64 ✓`.
- **Estación 3 · Faltantes:** a Luis le falta la glucosa. Botones que corren `fillna(mediana)`
  (rellena el hueco, resaltado en verde) o `dropna(subset=["glucosa"])` (borra su fila).
- **Estación 4 · Transformar:** `groupby("sexo")["glucosa"].mean()` **colapsa** la tabla a un
  resumen por grupo; `merge(resultados, on="nombre", how="left")` la **ensancha** con una
  columna nueva (Marco no está en `resultados` → su hba1c queda `NaN`).
- **Estación 5 · Inferir:** contraste *descriptiva vs inferencial* + mazo de cartas de
  escenario para entender qué nos dicen el **IC** y el **I²** en contexto
  (🔧 *algo falla, corrígelo* · 💡 *¿para qué sirve?*).

El dato **fluye**: las estaciones 3 y 4 parten de lo que ya limpió la 2.

## Arquitectura

- La tabla es un **array**; cada comando es una **función real** que la transforma.
- Las cartas son **datos** (`cartas[]`): agregar un caso = agregar un objeto.

## Pendiente

- Estación 1 (`info()` / signos vitales) interactiva.
- Ampliar el mazo de cartas de la estación 5.

## Verlo

Abre `index.html` en el navegador.
