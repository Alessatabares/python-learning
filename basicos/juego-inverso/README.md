# 🔧 Sala de Simulación · Romper y Predecir

Juego de una sola página (HTML + JS vanilla, sin build) para practicar la dirección
**inversa** a los juegos de diagnóstico: en lugar de diagnosticar un bug que ya pasó,
**predices** qué romperá un cambio antes de hacerlo.

Cubre los **mismos 22 escenarios** que `juego-comandos` (Manos al Teclado), repartidos
en los **dos tableros**:

- **🚨 Pipeline · request** (9) — del `juego-triage`: `Deploy → Request → Auth → Authz →
  Validación → ORM → SQL → Response`.
- **🚢 Sala de Máquinas · deploy** (13) — del `juego-triage-deploy`: `Build → Image →
  Registry → Run → Network → Env → Volumes → Boot → Logs`.

El tablero de arriba **cambia solo** según el escenario que elijas en la barra lateral.

## La dirección que entrena

| Juego | Dirección | Qué entrena |
|-------|-----------|-------------|
| `juego-triage` / `juego-triage-deploy` | efecto → causa | ves el síntoma, encuentras dónde murió |
| `juego-comandos` | reconocer → teclear | escribes los comandos de memoria |
| **este** | **causa → efecto** | te doy el código sano + el cambio que lo rompió; predices dónde muere y qué síntoma sale |

Es un sitio **independiente**: su propio `index.html` y su propio progreso en
`localStorage` (`simInversoProgress`). No modifica a ningún otro juego.

## Cómo se juega

1. Elige un escenario en la barra lateral (agrupados por tablero).
2. Lee el código **sano** y el **cambio** que lo rompió (panel "roto").
3. Haz clic en la **estación del tablero** donde crees que MORIRÁ.
4. Elige el **síntoma** (status code / salida) que predices.
5. Pulsa **Ejecutar simulación**. Si aciertas estación + síntoma, se **revela la
   terminal real** y desbloqueas una **frase ancla**.

Feedback en tres niveles: estación mal / estación bien pero síntoma mal / correcto.
La terminal permanece **oculta hasta que aciertas** — el punto es predecir, no leer.

## Las trampas (a propósito)

- Varios escenarios son **engañosos**: el cambio parece tocar una capa pero rompe en
  otra (`.env` no cargado, JSON vs Form, volumen faltante, `depends_on` sin readiness).
- Y hay trampas de **síntoma**: un email duplicado *debería* ser `409`, pero el código
  crudo lo deja escapar como `500`; un `Empty reply` no es lo mismo que `Connection
  refused`; un `Exited (0)` no es un `Restarting (137)`.

## Correr

No necesita servidor: abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-inverso
python -m http.server 8003
# luego abre http://localhost:8003
```

---

*Siguiente nivel posible: escribir el fix (tecleas la línea sana que arregla el cambio).*
