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

Total actual: **85 tarjetas** (27 Eje Clínico + 58 Integrador).

## Áreas

- **Frontend**, **Backend**, **Análisis de datos (Python)** — conceptos base.
- **Flask** — derivada del tutorial *"Python Website Full Tutorial - Flask,
  Authentication, Databases & More"* (Tech With Tim, `youtu.be/dam0GPOAvVI`):
  rutas, app factory, blueprints, Jinja/herencia, formularios + `request`,
  flash, SQLAlchemy (ORM, relaciones, `create_all`), hashing de contraseñas y
  Flask-Login (`login_user`, `@login_required`, `current_user`, `user_loader`).
