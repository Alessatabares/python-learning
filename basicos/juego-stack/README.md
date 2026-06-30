# 🏥 Clínica API · de cero a producción

Un solo sitio que unifica los dos juegos del stack backend. Abrí **`index.html`** y usá el conmutador de arriba para pasar entre las dos vistas.

| Pestaña | Archivo | Qué entrena |
|---------|---------|-------------|
| 🏗️ **Construir la API** | [`construir.html`](construir.html) | De función dormida a producción: la torre del stack, bloque a bloque (función → endpoint → servidor → deploy). Discriminación + representación mental. |
| ⚙️ **Operar el backend** | [`operar.html`](operar.html) | El pipeline de un request, de HTTP a JWT: 8 conceptos aislados que terminan integrados. Simulación. |

## La idea

Las dos pestañas son la misma clínica vista al derecho y al revés:

- **Construir** la armás de **adentro hacia afuera** — la función primero, el deploy al final.
- **Operar** mirás el request recorrerla de **afuera hacia adentro** — internet primero, la base de datos al final.

Esa inversión *es* el stack.

> Antes esto eran dos juegos sueltos (`juego-deploy/` y `juego-backend/`). Se fusionaron aquí; cada uno conserva su motor y su progreso por separado.
