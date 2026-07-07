# Hospital Tycoon — juego para aprender POO

Mini-juego web para *sentir* los 4 conceptos de programación orientada a objetos
sin teoría suelta. Cada acción del juego enciende la línea de código Python que
acabas de "jugar".

| Acción en el juego | Concepto | Código |
|--------------------|----------|--------|
| El molde de la izquierda | **Clase** | `class Paciente:` |
| Botón ESTAMPAR | **Objeto** | `p1 = Paciente(...)` |
| Escribir en una ranura | **Atributo** | `p1.edad = 30` |
| Botón `cumplir_anios()` | **Método** | `p1.cumplir_anios()` |

## Cómo correrlo
No necesita instalar nada (es HTML + CSS + JS puro).

    cd hospital-tycoon
    python3 -m http.server 8000
    # abrir http://localhost:8000

## Archivos (una responsabilidad cada uno)
- `index.html` — qué hay en pantalla (las cajas).
- `style.css` — cómo se ve.
- `game.js` — qué hace (la lógica; también usa una clase `Paciente`).

## Nivel 1 (MVP)
Molde `Paciente` → estampar fichas → rellenar atributos → apretar métodos.
Los 4 logros de arriba se encienden al usar cada concepto por primera vez.

## Siguientes niveles (ideas)
- Molde `Doctor` con método `asignar(paciente)` → objetos que contienen objetos.
- Guardar fichas en "el archivero" (localStorage) → analogía de SQL/persistencia.
- Aduana antes de estampar → analogía de Pydantic.
