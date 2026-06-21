# 🚢 Sala de Máquinas · Triage de Deployment

Juego de una sola página (HTML + JS vanilla, sin build) para **practicar depuración de
despliegues con Docker**. Mismo motor que `juego-triage`, pero enfocado en lo que pasa
*entre tu máquina y producción*: el deploy se rompe en alguna etapa del ciclo Docker y
tú diagnosticas dónde y por qué.

Es la pareja del `juego-triage` (que depura el *pipeline del request*). Aquí depuras el
**ciclo de vida del deploy**.

## El sistema: el ciclo de un deploy

```
Build → Image → Registry → Run → Network → Env → Volumes → Boot → Logs
```

De tu Dockerfile a un contenedor corriendo en el servidor. Cada etapa tiene síntomas
firma; tu trabajo es leer la terminal y la config, marcar la etapa rota y elegir el
diagnóstico.

## Cómo se juega

1. Lee la **terminal** (síntoma) y la **config** (Dockerfile / compose / comando).
2. Haz clic en la **etapa del ciclo** donde se rompió el deploy.
3. Elige el **diagnóstico** correcto.
4. Pulsa **Poner en producción**. Si aciertas las dos cosas, el ciclo se enciende en
   verde hasta prod y desbloqueas una **frase ancla**.

Feedback en tres niveles (etapa mal / etapa bien pero diagnóstico mal / resuelto).
Progreso y frases ancla en `localStorage`.

## Los 13 escenarios

| # | Caso | Se rompe en | Concepto |
|---|------|-------------|----------|
| 1 | Agregué la dependencia y no la encuentra | Build | orden de capas + caché |
| 2 | Construí en mi Mac, el servidor no la ejecuta | Image | arquitectura arm64 vs amd64 (`--platform`) |
| 3 | No me deja subir la imagen | Registry | `docker login` + tag `usuario/repo` |
| 4 | Desplegué el fix pero sigue el bug viejo *(engañoso)* | Registry | `:latest` no se re-jala; tags inmutables |
| 5 | El contenedor arranca y se muere | Run | CMD = proceso en primer plano |
| 6 | Respuesta vacía en el puerto publicado | Network | `-p HOST:CONTENEDOR` |
| 7 | Adentro responde, desde afuera no | Network | `EXPOSE` documenta vs `-p` publica |
| 8 | DATABASE_URL llega vacía | Env | inyectar vars en runtime (`--env-file`/`-e`) |
| 9 | El secreto quedó dentro de la imagen | Env | `ENV` horneado vs runtime; secretos fuera |
| 10 | Los datos desaparecen tras `compose down` *(engañoso)* | Volumes | contenedor efímero → named volume |
| 11 | La API no conecta a la base al arrancar *(engañoso)* | Boot | `depends_on` ≠ readiness; healthcheck/retry |
| 12 | La tabla no existe en el entorno nuevo | Boot | migraciones en el deploy |
| 13 | El contenedor reinicia en bucle | Logs | OOM (exit 137) + restart policy |

Tres escenarios son **engañosos**: el síntoma apunta a una etapa pero la raíz está en
otra (#4 parece Build/caché, #10 parece el bug de `commit` del otro juego, #11 parece
red). Te obligan a *trazar la cadena*.

## Correr

No necesita servidor: abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-triage-deploy
python -m http.server 8002
# luego abre http://localhost:8002
```

---

*Siguiente nivel posible: escribir el fix (tecleas la línea del Dockerfile/compose que
arregla el deploy) y el modo inverso sandbox (rompes una etapa y predices el síntoma).*
