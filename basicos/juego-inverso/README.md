# 🔧 Sala de Simulación · Romper y Predecir

Juego de una sola página (HTML + JS vanilla, sin build) para practicar la dirección
**inversa** al `juego-triage`: en lugar de diagnosticar un bug que ya pasó, **predices**
qué romperá un cambio antes de hacerlo.

Es el sitio hermano de `juego-triage`:
- `juego-triage` (Código Azul) → **efecto → causa**: ves el síntoma, encuentras dónde murió.
- Este (Sala de Simulación) → **causa → efecto**: te doy el código sano + el cambio que
  lo rompió, y predices dónde muere y qué síntoma sale.

Son sitios **independientes**: cada uno tiene su propio `index.html` y su propio
progreso en `localStorage`. Ninguno modifica al otro.

## Cómo se juega

1. Lee el código **sano** y el **cambio** que lo rompió (panel "roto").
2. Haz clic en la **estación del pipeline** donde crees que MORIRÁ el request.
3. Elige el **síntoma** (status code / salida) que predices.
4. Pulsa **Ejecutar simulación**. Si aciertas estación + síntoma, se **revela la
   terminal real** y desbloqueas una **frase ancla**.

Feedback en tres niveles: estación mal / estación bien pero síntoma mal / correcto.
La terminal permanece **oculta hasta que aciertas** — el punto es predecir, no leer.

## Los 9 escenarios

| # | Cambio que rompe | Muere en | Síntoma a predecir |
|---|------------------|----------|--------------------|
| 1 | `--host 0.0.0.0` → `127.0.0.1` | Deploy | Connection refused |
| 2 | se quitó `db.commit()` | ORM | 201, luego 404 tras restart |
| 3 | `@app.post` → `@app.get` | Request | 405 Method Not Allowed |
| 4 | el `.env` dejó de cargarse *(engañoso)* | Deploy | 401 con token fresco |
| 5 | se quitó el chequeo de dueño | Authz | 200 con dato ajeno |
| 6 | el cliente mandó `"treinta"` a un `int` | Validación | 422 |
| 7 | JSON a un endpoint `Form(...)` *(engañoso)* | Request | 422 'field required' |
| 8 | duplicado sin try/except (`unique=True`) | SQL | 500 IntegrityError |
| 9 | se quitó `response_model` | Response | 200 que filtra el hash |

Dos escenarios son **engañosos**: el cambio parece tocar una capa pero rompe en otra.
El #8 tiene una trampa de síntoma: un email duplicado *debería* ser `409`, pero el
código crudo lo deja escapar como `500` — solo es `409` si atrapas el `IntegrityError`.

## Correr

No necesita servidor: abre `index.html` en el navegador. O con servidor local:

```bash
cd basicos/juego-inverso
python -m http.server 8003
# luego abre http://localhost:8003
```

---

*Siguiente nivel posible: escribir el fix (tecleas la línea sana que arregla el cambio).*
