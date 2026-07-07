/* ============================================================
   Hospital Tycoon — lógica del juego.
   Fíjate: este archivo TAMBIÉN usa POO. La clase Paciente de abajo
   es el mismo molde que ves en pantalla, pero en JavaScript.
   ============================================================ */

/* ---------- EL MOLDE (una CLASE, igual que en tu API) ---------- */
class Paciente {
  constructor(nombre, edad, diagnostico) {   // el __init__ de Python
    this.nombre = nombre;                     // ATRIBUTO  (this = self)
    this.edad = edad;                         // ATRIBUTO
    this.diagnostico = diagnostico;           // ATRIBUTO
  }
  cumplir_anios() {                           // MÉTODO
    this.edad = Number(this.edad) + 1;        // toca SU propio atributo
  }
  es_mayor() {                                // MÉTODO
    return Number(this.edad) >= 18;
  }
}

/* ---------- estado del juego ---------- */
let contador = 0;          // cuántas fichas se han estampado (para nombrar p1, p2...)
let estrellas = 0;

/* ---------- atajos al DOM (las cajas del HTML) ---------- */
const $fichas     = document.getElementById("fichas");
const $vacia      = document.getElementById("mesa-vacia");
const $linea      = document.getElementById("linea-actual");
const $log        = document.getElementById("log");
const $countF     = document.getElementById("count-fichas");
const $countE     = document.getElementById("count-estrellas");
const $btnEstampar = document.getElementById("btn-estampar");

/* ---------- helpers de la consola de código ---------- */
function mostrarCodigo(linea) {
  $linea.textContent = linea;                 // línea grande "que se enciende"
  const li = document.createElement("li");
  li.innerHTML = linea.replace(/^(\w+)/, "<b>$1</b>");
  $log.prepend(li);                           // y se apila en el historial
}

function encender(concepto) {                 // prende el logro correspondiente
  const el = document.querySelector('.logro[data-k="' + concepto + '"]');
  if (el && !el.classList.contains("encendido")) {
    el.classList.add("encendido");
    estrellas++;
    $countE.textContent = estrellas;
  }
}

/* ============================================================
   ACCIÓN 1 — ESTAMPAR: nace un OBJETO del molde
   ============================================================ */
$btnEstampar.addEventListener("click", () => {
  contador++;
  const varName = "p" + contador;             // p1, p2, p3...

  // estampamos el objeto (todavía vacío)
  const paciente = new Paciente("", 0, "");

  encender("objeto");
  mostrarCodigo(varName + ' = Paciente("", 0, "")   # nace un OBJETO');
  $vacia.style.display = "none";
  $countF.textContent = contador;

  renderFicha(varName, paciente);
});

/* ---------- dibujar una ficha en la mesa ---------- */
function renderFicha(varName, paciente) {
  const div = document.createElement("div");
  div.className = "ficha";
  div.innerHTML =
    '<div class="ficha-cabecera">#' + varName + ' · Paciente</div>' +
    fila(varName, "nombre", "text") +
    fila(varName, "edad", "number") +
    fila(varName, "diagnostico", "text") +
    '<div class="metodos">' +
      '<button data-m="cumplir_anios">cumplir_anios()</button>' +
      '<button data-m="es_mayor">es_mayor()</button>' +
    '</div>' +
    '<div class="resultado"></div>';

  /* --- ACCIÓN 2 — escribir un ATRIBUTO --- */
  div.querySelectorAll("input").forEach((input) => {
    input.addEventListener("input", () => {
      const attr = input.dataset.attr;
      paciente[attr] = input.value;           // cambiamos el atributo del objeto
      encender("atributo");
      const valor = (input.type === "number") ? input.value : '"' + input.value + '"';
      mostrarCodigo(varName + "." + attr + " = " + valor + "   # un ATRIBUTO");
    });
  });

  /* --- ACCIÓN 3 — apretar un MÉTODO --- */
  div.querySelectorAll(".metodos button").forEach((btn) => {
    btn.addEventListener("click", () => {
      const metodo = btn.dataset.m;
      encender("metodo");

      if (metodo === "cumplir_anios") {
        paciente.cumplir_anios();             // el objeto se modifica a sí mismo
        const inputEdad = div.querySelector('input[data-attr="edad"]');
        inputEdad.value = paciente.edad;      // repintamos el atributo cambiado
        inputEdad.classList.add("pulso");
        setTimeout(() => inputEdad.classList.remove("pulso"), 500);
        mostrarCodigo(varName + ".cumplir_anios()   # un MÉTODO → sube self.edad");
      }

      if (metodo === "es_mayor") {
        const r = paciente.es_mayor();        // el método DEVUELVE algo
        const box = div.querySelector(".resultado");
        box.textContent = "→ " + (r ? "True (mayor de edad)" : "False (menor)");
        box.style.color = r ? "var(--ok)" : "#c0392b";
        mostrarCodigo(varName + ".es_mayor()   # devuelve " + (r ? "True" : "False"));
      }
    });
  });

  $fichas.prepend(div);
}

/* pequeño molde de fila reutilizable (nombre + input) */
function fila(varName, attr, tipo) {
  const val = (tipo === "number") ? "0" : "";
  return '<label>' + attr +
         ' <input data-attr="' + attr + '" type="' + tipo + '" value="' + val + '"></label>';
}
