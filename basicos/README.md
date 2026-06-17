# Básicos Dev — Anki (Frontend · Backend · Análisis de datos)

Decks de Anki para memorizar los **conceptos e infraestructuras indispensables** de las
tres áreas, construidos con la metodología de los *ejes diagnósticos* del repo
`examen-ecoe-anki`: cada concepto se indexa por **dos ejes complementarios**.

## Los dos ejes

| Eje | Dirección de recall | Para qué |
|---|---|---|
| **Eje Clínico** | del **problema** → al concepto que lo resuelve | construir el **mapa**: "tengo este dolor, ¿qué herramienta nace?" |
| **Integrador** | de las **señales** → al concepto + cómo verbalizarlo | **dominio**: reconocer un concepto por sus rasgos y saber explicarlo |

El campo *"Dilo así"* del Integrador es la verbalización (analogía / porqué profundo),
el equivalente del tip `ECOE: «...»` del repo médico.

## Estructura

```
basicos/
├── _parts/              # FUENTE ÚNICA de contenido (editar aquí)
│   ├── frontend.py      # NAME, EJES (eje clínico), ESTACIONES (integrador)
│   ├── backend.py
│   └── data.py
├── data_eje_clinico.py  # loader: importa _parts, extrae EJES
├── data_integrador.py   # loader: importa _parts, extrae ESTACIONES
├── build/
│   ├── _common.py       # registro de áreas + esquema de deck_id + modelo
│   ├── build_eje_clinico.py
│   └── build_integrador.py
└── output/              # los .apkg generados (importar en Anki)
```

Árbol de decks en Anki: `Basicos Dev::<Área>::Eje Clinico` y `::Integrador`.

## Regenerar

```bash
source ../.venv/bin/activate   # genanki instalado aquí
python build/build_eje_clinico.py
python build/build_integrador.py
```

## Reglas de diseño (heredadas de la metodología ECOE)

- **Datos separados del render:** la medicina/contenido vive en `_parts/`; los builders solo pintan HTML.
- **GUID estable por posición** (`basdev:ec:<area>:<i>`): corregir un texto y reimportar
  **actualiza** la carta en su sitio, nunca la duplica.
- **deck_id determinista** (`1500_AA_C`): sin colisión con el repo ECOE.

Total actual: **204 tarjetas** (68 Eje Clínico + 136 Integrador).

## Áreas

- **Frontend**, **Backend**, **Análisis de datos (Python)** — conceptos base.
- **Flask** — derivada del tutorial *"Python Website Full Tutorial - Flask,
  Authentication, Databases & More"* (Tech With Tim, `youtu.be/dam0GPOAvVI`):
  rutas, app factory, blueprints, Jinja/herencia, formularios + `request`,
  flash, SQLAlchemy (ORM, relaciones, `create_all`), hashing de contraseñas y
  Flask-Login (`login_user`, `@login_required`, `current_user`, `user_loader`).
- **Python** — el curso completo *"The Complete Python Course"* (Tech With Tim,
  `youtu.be/sxTmJE4k0ho`): de fundamentos (tipos, operadores, condiciones,
  bucles, listas/tuplas, slicing, strings, funciones, archivos, módulos,
  try/except, ámbito) → POO (clases, `self`, herencia, dunder/`__init__`,
  static/classmethod, privado) → intermedio (map/filter/lambda, `collections`)
  → experto (compilación/bytecode, decoradores, generadores `yield`, context
  managers `with`, metaclases).
- **Pandas** — del tutorial de pandas (Tech With Tim, `youtu.be/EXIgjIBu4EU`):
  `DataFrame` vs `Series`, `read_csv`, explorar (`head`/`tail`/`info`/`describe`),
  indexar (`df["col"]` vs `iloc` vs `loc`), filtrar (`&`/`|`, `.str`, `isin`, `~`),
  actualizar/limpiar (`drop`/`dropna`/`fillna`, `inplace`), analizar
  (`value_counts`, `groupby`, `sort_values`) y guardar (`to_csv`).
- **FastAPI** — del proyecto real de fotos/videos (Tech With Tim,
  `youtu.be/SR5NYCdzKkc`): teoría web (URL, request/response, métodos, status
  codes), `@app.get`/`uvicorn`/`/docs`, entrada (path/query/body Pydantic,
  `File`/`Form`), validación (type hints, response model, `HTTPException`),
  ORM async (SQLAlchemy, `Depends`, `add`/`commit`/`refresh`, `select`),
  media con ImageKit + `.env`, y auth JWT con `fastapi-users` (login, `SECRET`,
  `current_active_user`, relaciones `ForeignKey`, proteger/autorizar rutas).
