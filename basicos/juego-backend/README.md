# 🏥 Clínica API — Simulador de Backend

Juego de una sola página para **visualizar y aplicar** el flujo de un backend: desde
la petición HTTP hasta identidad/seguridad. Operás el backend de una clínica
(pacientes, médicos, citas) y cada misión te hace *usar* un concepto y verlo
encenderse en un **pipeline** siempre visible:

```
Frontend → Request → Auth → Authz → Validación → ORM → SQL → Response
```

Es la contraparte interactiva del deck de Anki **Básicos Dev · Backend · Integrador**:
los conceptos que ahí memorizás, acá los hacés trabajar juntos.

## Cómo abrirlo

- **Local:** doble clic en `index.html` (no necesita servidor ni instalación; es HTML + JS vanilla).
- **Como sitio:** activá GitHub Pages en el repo y entrá a
  `…/basicos/juego-backend/index.html`.

El progreso se guarda solo en el navegador (`localStorage`).

## Misiones

| # | Misión | Concepto |
|---|---|---|
| 1 | 📨 Habla HTTP | método=intención · ruta=recurso · body solo en POST/PUT/PATCH · stateless (sin token → 401) |
| 2 | 🩺 Sala de diagnóstico | status codes: 2xx/4xx/5xx · 401 vs 403 vs 404 vs 422 |
| 3 | 💾 RAM vs Base de datos | persistencia · ORM · `add`/`commit` · sin commit el reinicio se lo lleva |
| 4 | 🗂️ El plano de la base | PK · FK · JOIN (FK → PK) |
| 5 | 🔐 Bóveda de contraseñas | hashing one-way · salt · login = comparar hashes |
| 6 | 🛂 ¿Quién y qué? | autenticación (401) vs autorización (403) |
| 7 | 🎫 Anatomía del JWT | HEADER.PAYLOAD.SIGNATURE · firma ≠ secreto · tamper rompe la firma |
| 8 | 🎬 La película completa | el pipeline integrado, compuerta por compuerta |

Cada misión superada desbloquea su **frase ancla** (las mismas del deck), que se
coleccionan abajo.

> Nota: las funciones de hash y firma del juego son *demostrativas* (un hash
> simple para visualizar), no criptografía real. Sirven para ver el comportamiento
> (irreversibilidad, salt, detección de alteración), no para producción.
