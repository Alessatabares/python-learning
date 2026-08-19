# Básicos Dev — Anki (Frontend · Backend · Análisis de datos)

Decks de Anki para memorizar los **conceptos e infraestructuras indispensables** de las
tres áreas, construidos con la metodología de los *ejes diagnósticos* del repo
`examen-ecoe-anki`: cada concepto se indexa por **dos ejes complementarios**.

> Además de los decks de Anki, esta carpeta incluye **juegos web interactivos**
> para aprender lo mismo de otra forma → ver [🎮 Juegos web](#-juegos-web-interactivos) al final.

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

Nota sobre el conteo: en **Eje Clínico** cada tarjeta es un **grupo-problema completo**
(al frente la lista de situaciones, al reverso los conceptos que nacen), así que hay
1 tarjeta por grupo, no por situación. En **Integrador** hay 1 tarjeta por concepto.

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

Total actual: **321 tarjetas** (101 Eje Clínico + 220 Integrador). Las áreas más recientes:
**Anatomía del Backend** aporta 33 (9 + 24) y **Protocolo HTTP** aporta 69 (20 + 49),
el área más grande del repo.

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
- **Anatomía del Backend** — del video *"What is a backend?"* (`youtu.be/6Ss4dJD9Kzg`):
  el recorrido **físico** de una petición hasta el servidor — DNS (registros A vs
  CNAME, subdominios) → IP pública de la instancia → **firewall** / security group
  (puertos 80, 443, 22) → **nginx** como reverse proxy (`server_name`, reenvío a
  `localhost:3001`, redirección 80→443 con certbot) → el proceso node vivo bajo
  **pm2**. Además: para qué existe un backend (persistir datos, estado centralizado,
  el ejemplo del *like*), cómo carga un frontend (HTML → recursos → pintado →
  hidratación) y las **4 razones** por las que la lógica de backend no puede vivir
  en el navegador (sandbox/seguridad, CORS, drivers y *connection pool* de base de
  datos, poder de cómputo).
- **Protocolo HTTP** — del video *"HTTP protocol"* (`youtu.be/a3C1DMswClQ`), el área más
  extensa: las dos ideas base (**statelessness** y modelo cliente-servidor), HTTP sobre
  TCP y la capa 7 del modelo OSI, la evolución 1.0 → 3.0, **anatomía del mensaje**
  (línea inicial, headers, línea en blanco, body), los **4 tipos de headers**
  (request / general / representation / security) y de qué protege cada header de
  seguridad, métodos e **idempotencia**, **CORS completo** (same-origin policy,
  `Origin` ↔ `Access-Control-Allow-Origin`, las 3 condiciones del **preflight**
  `OPTIONS` y sus permisos), los **status codes** por familias (2xx, 3xx, 4xx, 5xx),
  **caching** (`Cache-Control`, `ETag`, `Last-Modified`, `If-None-Match` → `304`),
  negociación de contenido y compresión (`Accept*`, gzip), `keep-alive`, archivos
  grandes (`multipart` + `boundary`, streaming por chunks) y SSL/TLS/HTTPS.
- **Diagramas** — cómo convertir tus **árboles de decisión médicos** (estilo ECOE)
  en páginas web interactivas. Herramientas que dibujan (**Mermaid** texto→diagrama,
  `graph TD`, nodos/aristas/formas; **Markmap** outline→mindmap colapsable), acceso
  e interacción (click en nodo, colapsar/expandir ramas, `addEventListener`) y
  publicación con **GitHub Pages**. Deck propio: **no se mezcla con Frontend**.

---

# 🎮 Juegos web interactivos

Mini-juegos para aprender los fundamentos detrás de una API (FastAPI + Python +
git/GitHub + redes). No son quizzes sueltos: cada uno está **diseñado con un método
de aprendizaje concreto**, no improvisado.

> **Cómo trabajo esto:** yo diseño la pedagogía (qué se aprende y *cómo* se graba);
> la implementación la hago con ayuda de IA. El criterio de diseño es la parte mía.

## La idea pedagógica

Tres principios guían todos los juegos:

1. **Aprender por discriminación, no por definición.** No memorizas "qué es un puerto";
   discriminas `8000` (FastAPI, habla HTTP, tiene paths) contra `5432` (Postgres, habla
   SQL, sin paths). El contraste es lo que graba.
2. **Pares de contraste deliberados.** Cada concepto se enseña junto a su vecino
   confundible: `Query` ↔ `Path`, `UploadFile` ↔ `FileResponse`, `git clone` ↔ `git pull`,
   `["x"]` ↔ `.get("x")`. Si dos cosas se confunden, van juntas.
3. **Recall activo + frase ancla.** Cada acierto desbloquea una *frase ancla*: el concepto
   destilado en una línea memorizable. Se coleccionan abajo como resumen.

Feedback siempre graduado (🔴🟡🟢) y con el *porqué*, porque se aprende más en el error
explicado que en el acierto.

## Los patrones de aprendizaje

Sobre los 3 principios, la colección usa **varios formatos**, cada uno entrena un músculo
distinto. El mismo concepto se puede atacar desde varios:

| Patrón | Cómo funciona | Qué músculo entrena |
|--------|---------------|---------------------|
| **Discriminación** (síntoma/dato → causa) | lees algo y eliges entre vecinos confundibles | reconocer, distinguir lo parecido |
| **Caza del error** (discriminación inversa) | te dan algo *roto* (una URL incoherente) y detectas qué pieza choca con cuál y por qué | producir el juicio, no solo reconocer la respuesta dada |
| **Recall por tecleo** | lees una situación y escribes el comando de memoria | producir de cero, no solo reconocer |
| **Predicción causal** (inverso) | dado un cambio en el código, predices el fallo *sin ver* la salida | razonar causa → efecto |
| **Construcción de representación mental** | armas el stack bloque a bloque y luego recorres el request | tener el mapa completo en la cabeza |
| **Simulación con estado vivo** | ejecutas y ves la tabla / el estado transformarse frente a ti | intuición de qué hace cada operación |

Un mismo tema suele tener su versión en 2–3 patrones (ej.: el pipeline del request se
*diagnostica* en Triage, se *predice* en Inverso y se *teclea* en Comandos). Eso es a
propósito: ver lo mismo desde ángulos distintos es lo que consolida.

## El patrón técnico

La familia de quiz/tecleo comparte un mismo molde — y eso es lo que la hace **reciclable**
y la base de una futura app que los unifique:

```
        MOTOR  (igual en todos)                 DATOS  (lo único que cambia)
   render + score + frases ancla         +      CASOS = [ {...}, {...} ]
   + progreso en localStorage                   + modo (opción múltiple / tecleo)
   ─────────────────────────────                ────────────────────────────────
                              ↓
        un index.html autónomo por juego (HTML + JS vanilla, sin dependencias)
```

Para un juego nuevo de este tipo: copiar el motor y reescribir el array `CASOS`. Para
unificarlos: un menú que cargue el motor una vez y cada juego como su archivo de datos.

*(Algunos juegos —`data`, `stack` (construir/operar)— son simuladores más a medida: tablas
vivas, dropdowns y animaciones, no solo opción múltiple. No siguen el molde motor/datos,
pero comparten la idea pedagógica y las frases ancla.)*

## Catálogo

**API & backend desde cero**

| Juego | Carpeta | Qué entrena | Patrón |
|-------|---------|-------------|--------|
| 🛂 **Aduana de Red** | [`juego-url/`](juego-url/) | Máquinas, puertos y paths de una URL · **2 niveles** | discriminación → caza-error |
| 🧰 **Caja de Herramientas** | [`juego-imports/`](juego-imports/) | Imports útiles de FastAPI y Pydantic · **2 niveles** | discriminación → tecleo la solución |
| 🐍 **¿Qué devuelve?** | [`juego-python/`](juego-python/) | Python básico de una API: qué devuelve cada línea | discriminación |
| 🐙 **Terminal Git** | [`juego-git/`](juego-git/) | Comandos de git/GitHub, en escenarios | tecleo |

**Diagnóstico del stack (request + deploy)**

| Juego | Carpeta | Qué entrena | Patrón |
|-------|---------|-------------|--------|
| 🩺 **Doble Triage** · request + deploy en un tablero | [`juego-triage-360/`](juego-triage-360/) | Request + deploy unificados (22 casos, nav por sitio) | discriminación síntoma→causa |
| 🔧 **Romper y Predecir** | [`juego-inverso/`](juego-inverso/) | Predecir dónde muere y qué síntoma sale | predicción causal |
| ⌨️ **Manos al Teclado** | [`juego-comandos/`](juego-comandos/) | Teclear los comandos del stack (4 capas) | tecleo |
| 🏥 **Clínica API · de cero a producción** | [`juego-stack/`](juego-stack/) | Dos vistas del stack: construir la torre (deploy) + operar el request (HTTP→JWT), con conmutador | representación mental + simulación |

**Datos y análisis (Pandas + estadística)**

| Juego | Carpeta | Qué entrena | Patrón |
|-------|---------|-------------|--------|
| 📊 **Pipeline de Datos Clínicos** | [`juego-data/`](juego-data/) | Las 5 estaciones del análisis, con tabla viva | simulación estado vivo |
| ⌨️ **Manos al Teclado · Pandas** | [`juego-comandos-data/`](juego-comandos-data/) | Teclear comandos de pandas (4 capas) | tecleo |
| 🔧 **Sala de Simulación · Datos** | [`juego-inverso-data/`](juego-inverso-data/) | Predecir fallos del análisis (fillna, merge…) | predicción causal |

## Cómo abrirlos

Son archivos estáticos: se abren en el navegador, sin instalar nada.

```bash
# WSL → navegador de Windows
wslview basicos/juego-url/index.html
# o pega la ruta del index.html directo en el navegador
```

El progreso se guarda solo en tu navegador (`localStorage`); cada juego tiene su botón
de reiniciar.
