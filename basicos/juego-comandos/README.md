# ⌨️ Manos al Teclado · Teclea los comandos de tus dos triages

Juego de una sola página (HTML + JS vanilla, sin build) para **memorizar comandos
tecleándolos**, no reconociéndolos. Es la contraparte de **destreza** de tus dos
juegos de **diagnóstico**:

- `juego-triage` (Código Azul · Pipeline) → diagnosticas dónde murió el request.
- `juego-triage-deploy` (Sala de Máquinas) → diagnosticas dónde se rompió el deploy.
- **este** → tomas **cada escenario de esos dos** y lo **escribes de memoria**.

> Saber *qué* sutura va ≠ saber *suturar con las manos*. Aquí entrenas las manos.

## Las 4 capas (de la pieza al procedimiento)

Cada escenario se practica en capas, como aprender un idioma:

| Capa | Qué es | Analogía | Ejemplo |
|------|--------|----------|---------|
| **1 · Vocabulario** | una pieza suelta y qué significa | palabra | `-d` = el body, `-X` = el método |
| **2 · El comando** | una orden completa con esas piezas | oración | `curl -X POST /pacientes -d '{...}'` |
| **3 · La secuencia** | varias órdenes que logran una acción | párrafo | `build → run → ps → curl` |
| **4 · El arreglo** | el código roto del escenario → lo escribes bien | corregir | `127.0.0.1` → `0.0.0.0` |

En **todas tecleas tú**. Al acertar sin ver la solución, queda como músculo y
desbloqueas la **frase ancla** + el **eje** (concepto), reusados de los juegos
originales para no dejar conceptos huérfanos. El progreso se guarda en `localStorage`.

## Contenido: los 22 escenarios, 70 capas

- **🚨 Pipeline (9 escenarios):** host 0.0.0.0, paciente fantasma (`commit`), 405 GET/POST,
  SECRET/`.env`, authz (pertenencia), 422 tipo, JSON vs form, `unique` duplicado, fuga del hash.
- **🚢 Sala de Máquinas (13 escenarios):** caché de capas, `--platform`, registry/login,
  `:latest` viejo, contenedor que muere, mapeo de puertos, EXPOSE vs `-p`, `--env-file`,
  secreto horneado, volúmenes, readiness, migraciones, OOM (137).

Cada escenario muestra arriba su **síntoma original** (el mismo de los juegos de
diagnóstico) y abajo sus capas. No todos tienen las 4: la capa 3 (secuencia) solo
aparece donde hay un flujo real de varios comandos.

## Cómo se juega

1. Elige un escenario en la barra lateral (agrupados por sitio; cada uno marca `n/total`).
2. En cada tarjeta-capa, lee **🎯 lo que quiero** y tecléalo en el `$`.
3. **Comprobar ▶**. Verde = dominado.
   - **ver solución**: te la enseña pero NO cuenta (tecléala tú luego).
   - **¿qué estaba mal?** (capa 4): explica el bug antes de arreglarlo.

El corrector es indulgente con **comillas y espacios de más**, estricto con las
**piezas**: si falta un `-r` o un `-X`, no pasa.

## Correr

No necesita servidor: abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-comandos
python -m http.server 8002
# luego abre http://localhost:8002
```

---

*Siguiente nivel posible: modo contrarreloj (sin pista) y modo inverso (te doy el
comando, escribes qué hace cada pieza).*
