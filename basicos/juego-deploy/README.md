# 🚀 De función dormida a API en producción

Juego de una sola página para **construir** un backend de cero a producción, capa por
capa, sintiendo que vas creando cosas reales. Empezás con una función Python dormida
(`def hello()`) y la despertás, blindás y publicás hasta que el mundo la usa.

Es el **complemento** del otro juego, `juego-backend` (Clínica API):
- Allá **operás** un backend ya hecho y respondés cómo funciona el pipeline.
- Acá lo **construís vos** de adentro hacia afuera y lo llevás a internet.

La idea central es una **torre que se arma bloque por bloque** (la barra de la derecha):
cada acción correcta enciende su capa. Y un detalle clave para entender el stack:

> La construís **de adentro hacia afuera** (función → DB → validación → auth → deploy),
> pero el request la recorre **de afuera hacia adentro**. Esa inversión *es* el stack.

## Cómo abrirlo

- **Local:** doble clic en `index.html` (HTML + JS vanilla, sin servidor ni instalación).
- **Como sitio:** activá GitHub Pages y entrá a `…/basicos/juego-deploy/index.html`.

El progreso se guarda solo en el navegador (`localStorage`). Botón **Reiniciar** para empezar de cero.

## Los 4 actos + película final (15 retos)

| Acto | Qué construís | Conceptos |
|---|---|---|
| 1 · Despertar (local) | función → endpoint → servidor vivo → primer request | FastAPI · `@app.get` · Uvicorn · ASGI · URL (host/puerto/ruta) |
| 2 · Endurecer | validación + datos que sobreviven | método=intención · Pydantic · 400 vs 422 · RAM vs DB · ORM `add/commit` · PK/FK/JOIN · normalización |
| 3 · Proteger | identidad y seguridad | hashing ≠ encriptar · JWT · middleware · 401 vs 403 |
| 4 · Publicar 🌍 | de localhost al mundo | deployment · PaaS (Render/Railway) · env vars · `.env`/`.gitignore` · Docker · logs |
| 🎬 Final | el request recorre tu torre | el pipeline completo, de internet a la base y de vuelta con status code |

Cada reto superado desbloqueá su **frase ancla** (las mismas del deck de Anki
*Básicos Dev · Backend*), que se coleccionan abajo.

> Nota: los comandos y el código que se muestran son *ilustrativos* para fijar el modelo
> mental (qué pieza va dónde y por qué), no un proyecto FastAPI ejecutable.
