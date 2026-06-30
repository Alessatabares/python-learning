# 🏥 Clínica API · de cero a producción

Un solo archivo (**`index.html`**) con un menú arriba. Hacés clic y cambiás entre las dos vistas del stack sin salir de la página:

| Menú | Qué entrena |
|------|-------------|
| 🏗️ **Construir la API** | De función dormida a producción: la torre del stack, bloque a bloque (función → endpoint → servidor → deploy). |
| ⚙️ **Operar el backend** | El pipeline de un request, de HTTP a JWT: 8 conceptos aislados que terminan integrados. |

## La idea

Las dos pestañas son la misma clínica vista al derecho y al revés:

- **Construir** la armás de **adentro hacia afuera** — la función primero, el deploy al final.
- **Operar** mirás el request recorrerla de **afuera hacia adentro** — internet primero, la base de datos al final.

Esa inversión *es* el stack.

> Antes esto eran dos juegos sueltos (`juego-deploy` y `juego-backend`) y luego dos archivos
> separados. Ahora todo vive en un único `index.html`; cada vista conserva su progreso por
> separado (en `localStorage`).
