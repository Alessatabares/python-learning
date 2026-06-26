# ⌨️ Manos al Teclado · Pandas

Juego de una sola página (HTML + JS vanilla, sin build) para **memorizar el pipeline
de datos tecleándolo**, no reconociéndolo. Es la contraparte de **destreza** del
`juego-data` (el pipeline visual): ahí ves cómo cada comando transforma la tabla; aquí
lo escribes de memoria.

> Saber *qué* hace `to_numeric` ≠ saber *teclearlo* sin mirar. Aquí entrenas las manos.

## Las 4 capas (de la pieza al procedimiento)

| Capa | Qué es | Ejemplo |
|------|--------|---------|
| **1 · Vocabulario** | una pieza suelta | `errors="coerce"`, `how="left"`, `subset=["glucosa"]` |
| **2 · El comando** | una línea completa | `df["edad"] = pd.to_numeric(df["edad"], errors="coerce")` |
| **3 · La secuencia** | un flujo de varios comandos | `df.shape → df.info() → df.isna().sum()` |
| **4 · El arreglo** | código roto → lo reescribes bien | `df.dropna()` → `df.dropna(subset=["glucosa"])` |

En **todas tecleas tú**. Al acertar sin ver la solución desbloqueas la **frase ancla** +
el **eje** (concepto). El progreso se guarda en `localStorage`.

## Contenido: 7 escenarios

- **🩺 Limpieza:** signos vitales (`info`/`isna`), número atrapado como texto
  (`to_numeric`/`coerce` vs `astype`), el hueco que no es cero (`fillna` media/mediana/0),
  borrar vs imputar (`dropna(subset=...)`).
- **📊 Análisis:** resumen por grupo (`groupby`), unir tablas (`merge`, `how`),
  toda la columna de golpe (vectorización vs `for`).

## Cómo se juega

1. Elige un escenario en la barra lateral (marca `n/total`).
2. En cada capa, lee **🎯 lo que quiero** y tecléalo.
3. **Comprobar ▶**. Verde = dominado.
   - **ver solución**: te la enseña pero NO cuenta (tecléala tú luego).
   - **¿qué estaba mal?** (capa 4): explica el bug antes de arreglarlo.

El corrector es indulgente con **comillas y espacios** (`'` = `"`), estricto con las
**piezas**: si falta un `coerce` o un `subset`, no pasa.

## Correr

Abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-comandos-data
python -m http.server 8004
# luego abre http://localhost:8004
```
