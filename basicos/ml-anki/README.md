# Machine Learning aplicado — 4 decks de Anki

Lo práctico para levantar un proyecto de visión por computador en medicina
(caso de trabajo: clasificador de OCT retiniana en 4 clases — CNV, DME, drusas, normal).

No enseña la teoría de redes neuronales: enseña **cómo se monta y se protege el proyecto**,
qué librería hace qué, de dónde salen los datos, y qué decisiones hay que tomar.

## Las cuatro corridas (estúdialas en este orden)

Anki introduce las tarjetas nuevas en el orden en que se añadieron, así que el orden
importa: se va de menos información a más.

| # | Deck | Front → Back | Notas |
|---|------|--------------|-------|
| 1 | `Machine Learning::Eje Clinico` | "tengo este problema" → la herramienta que nace | 7 (59 pares) |
| 2 | `Machine Learning::Integrador` | 3 señales → el concepto + *"Dilo así"* | 22 |
| 3 | `Machine Learning::Comandos` | el comando literal → qué hace, cuándo, la trampa | 48 |
| 4 | `Machine Learning::Pares Minimos` | ancla + **una** pieza que cambia → qué se rompe | 21 |

**Corrida 1 — Eje Clínico.** Siete ejes: el entorno · qué librería hace qué · cómo se instala ·
de dónde salen los datos etiquetados · cómo se bajan y se verifican · cómo se protege el repo ·
qué decisiones hay sobre el modelo.

**Corrida 4 — Pares mínimos.** Es la corrida que de verdad enseña: cada tarjeta toma el caso
correcto, cambia **una sola** pieza, y pregunta qué se rompe y cómo se arregla. Cubre las
trampas que no dan error visible (olvidar `zero_grad()`, fuga de datos entre pacientes,
accuracy alto con clases desbalanceadas, Grad-CAM apuntando al aparato en vez de a la retina).

## Dónde vive el contenido

- Corridas 1 y 2 → `../_parts/machine_learning.py` (`EJES` y `ESTACIONES`), construidas por
  los builders compartidos `../build/build_eje_clinico.py` y `../build/build_integrador.py`.
- Corridas 3 y 4 → `build_comandos_ml.py` y `build_pares_minimos_ml.py` (contenido y builder
  en el mismo archivo).

Para cambiar contenido: editar los datos, nunca el render.

## Regenerar

```bash
cd basicos
../.venv/bin/python build/build_eje_clinico.py
../.venv/bin/python build/build_integrador.py
../.venv/bin/python ml-anki/build_comandos_ml.py
../.venv/bin/python ml-anki/build_pares_minimos_ml.py
```

Los `.apkg` salen en `basicos/output/Basicos_MachineLearning_*.apkg`.

Los GUID son estables por posición: reimportar un deck corregido **actualiza** las tarjetas
en su sitio y conserva tu historial de repasos, nunca duplica.

## IDs (para no colisionar al añadir decks)

Área `Machine Learning` = idx 14 en `../build/_common.py`.
Deck IDs `1500014001` (Eje Clínico) · `1500014002` (Integrador) · `1500014003` (Comandos) ·
`1500014004` (Pares Mínimos). Modelos propios: `1607392351` y `1607392352`.
