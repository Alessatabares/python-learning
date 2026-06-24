# 🚨 Código Azul en la API · Triage del Pipeline

Juego de una sola página (HTML + JS vanilla, sin build) para **practicar depuración**:
el request es el paciente, el status code es el motivo de consulta, y tú haces el
diagnóstico diferencial de dónde y por qué colapsó.

Es la contraparte de **diagnóstico** de tus otros dos juegos:
- `juego-backend` (Clínica API) te enseñó a *operar* el pipeline.
- `juego-deploy` te enseñó a *desplegarlo*.
- Este te enseña a **encontrar qué falló** cuando algo se rompe en código real.

## El sistema: dos anillos anidados

```
INFRA (🐳 Deploy) ⟶ Request → Auth → Authz → Validación → ORM → SQL → Response
```

Si falla el anillo de infra, el request ni entra (connection refused, SECRET=None).
Si entra pero muere en una compuerta, es un bug del pipeline.

## Cómo se juega (tier "Localizar + diagnosticar")

1. Lee la **terminal** (síntoma) y el **código** (el cuerpo).
2. Haz clic en la **estación del pipeline** donde crees que murió el request.
3. Elige el **diagnóstico** correcto.
4. Pulsa **Estabilizar paciente**. Si aciertas las dos cosas, el request reanima
   en verde hasta `200` y desbloqueas una **frase ancla**.

Feedback en tres niveles: estación equivocada / estación bien pero diagnóstico
mal / resuelto. El progreso se guarda en `localStorage`.

## Los 9 escenarios

| # | Caso | Muere en | Concepto |
|---|------|----------|----------|
| 1 | Llamo a la puerta y nadie abre | Deploy | `--host 0.0.0.0` vs puerto publicado |
| 2 | El paciente fantasma | ORM | `add` → `commit` → `refresh` (RAM vs disco) |
| 3 | La puerta correcta, método equivocado | Request | 404 vs 405 (ruta vs verbo) |
| 4 | Todos los tokens fallan *(engañoso)* | Deploy | `.env` no cargado disfraza un 401 de Auth |
| 5 | El médico A ve al paciente de B | Authz | 401 vs 403 · chequeo de pertenencia |
| 6 | Edad: 'treinta' | Validación | Pydantic rechaza por tipo (422) |
| 7 | JSON donde pedían formulario *(engañoso)* | Request | `Form(...)` vs body JSON |
| 8 | Ese email ya existe | SQL | constraints `unique`/FK → IntegrityError |
| 9 | La respuesta filtra el hash | Response | `response_model` como filtro de salida |

Dos escenarios son **engañosos** a propósito: el síntoma apunta a una estación
pero la raíz está en otra. Eso te obliga a *trazar la cadena*, no a memorizar
un mapeo síntoma → respuesta.

## Correr

No necesita servidor: abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-triage
python -m http.server 8001
# luego abre http://localhost:8001
```

---

*Siguiente nivel posible: escribir el fix (tecleas la línea que arregla el bug) y
el modo inverso sandbox (tú rompes una compuerta y predices el síntoma).*
