# -*- coding: utf-8 -*-
"""Deck de comandos/código de la sesión "Git + primer backend (FastAPI)".

Front: el comando o fragmento de código.
Back:  qué hace / qué resuelve / por qué.

Genera Basicos_Comandos_GitFastAPI.apkg en ./output/.
Correr:  ../../.venv/bin/python build_comandos.py
"""
import os
import html
import genanki

MODEL_ID = 1607392325        # propio de este deck, sin colisión
DECK_ID = 1599000001
DECK_NAME = "Basicos Dev::Comandos (Git + primer backend)"

# (seccion, front_codigo, back_explicacion)
CARDS = [
  # ---------- GITHUB (gh) ----------
  ("GitHub (gh)",
   "gh repo create miniproyectos-dev --public --add-readme --gitignore Python --clone",
   "Crea un repositorio en GitHub y lo descarga a tu compu, todo en un paso. "
   "--public lo hace público · --add-readme crea un README inicial · --gitignore Python agrega un .gitignore "
   "para Python (ignora .venv, __pycache__...) · --clone lo clona local. "
   "Resuelve: arrancar un proyecto nuevo ya conectado a GitHub. Ojo: va TODO en una línea; si se parte, falla."),
  ("GitHub (gh)",
   "gh repo clone miniproyectos-dev",
   "Clona (descarga) un repo de GitHub a tu compu: crea la carpeta local y conecta el remoto 'origin'. "
   "Resuelve: traer a tu máquina un repo que ya existe en GitHub."),
  ("GitHub (gh)",
   "gh repo rename miniproyectos-dev",
   "Renombra el repo en GitHub y actualiza tu remoto local (origin) al nombre nuevo. "
   "NO cambia el nombre de la carpeta en tu disco (eso es aparte, con mv). GitHub deja una redirección del nombre viejo."),
  ("GitHub (gh)",
   'gh repo edit --description "Miniproyectos de programación"',
   "Edita la configuración del repo en GitHub; aquí, la descripción. "
   "Resuelve: cambiar metadatos del repo sin entrar a la web."),
  ("GitHub (gh)",
   "gh auth status",
   "Muestra si estás logueada en GitHub desde la terminal (con qué cuenta y protocolo). "
   "Resuelve: confirmar que gh puede actuar en tu nombre antes de crear o subir."),

  # ---------- TERMINAL ----------
  ("Terminal",
   "mkdir registro-estudios",
   "'make directory': crea una carpeta nueva. Resuelve: armar el espacio del proyecto."),
  ("Terminal",
   "cd registro-estudios",
   "'change directory': te mueve dentro de esa carpeta. Importa porque muchos comandos (venv, nano, git) "
   "actúan SOBRE la carpeta donde estás parada."),
  ("Terminal",
   "pwd",
   "'print working directory': muestra en qué carpeta estás ahora. Resuelve: confirmar tu ubicación antes de crear o editar archivos."),
  ("Terminal",
   "ls",
   "Lista los archivos y carpetas del directorio actual. Resuelve: ver qué hay."),
  ("Terminal",
   "ls -a",
   "Lista TODO, incluidos los ocultos (los que empiezan con punto, como .git y .gitignore). "
   "Resuelve: ver archivos de configuración que 'ls' normal esconde."),
  ("Terminal",
   "cat README.md",
   "Muestra en pantalla el contenido completo de un archivo. Resuelve: leer rápido un archivo sin abrir un editor."),
  ("Terminal",
   "rm -rf .venv",
   "Borra una carpeta y todo su contenido (r = recursivo, f = sin preguntar). Resuelve: eliminar algo de una. "
   "PELIGRO: no hay papelera, borra directo."),
  ("Terminal",
   "mv miniproyectos miniproyectos-dev",
   "'move': renombra (o mueve) un archivo/carpeta. Aquí cambia el nombre de la carpeta local. No toca git ni GitHub."),

  # ---------- GIT ----------
  ("Git",
   "git remote -v",
   "Muestra las conexiones remotas del repo (el 'cable' a GitHub). 'origin' es el apodo del remoto; "
   "(fetch)=de dónde bajás, (push)=a dónde subís. Resuelve: verificar que tu carpeta apunta a TU repo."),
  ("Git",
   "git status",
   "Muestra qué archivos cambiaron, cuáles están preparados (staged) y cuáles no. "
   "Resuelve: saber en qué estado está tu trabajo antes de commitear."),
  ("Git",
   "git add main.py README.md",
   "Prepara (staging) esos archivos para el próximo commit. Como session.add del ORM: los dejás listos, "
   "todavía no se guardan. Resuelve: elegir qué entra en el commit."),
  ("Git",
   'git commit -m "Capa 1: CRUD en RAM"',
   "Confirma los cambios preparados en la historia LOCAL de git, con un mensaje (-m) que describe qué hiciste. "
   "Como session.commit. Resuelve: guardar una 'foto' del proyecto."),
  ("Git",
   "git push",
   "Sube tus commits locales a GitHub (el remoto). Resuelve: que tu código quede online y respaldado. "
   "Mapa completo: add (preparar) → commit (confirmar local) → push (subir)."),

  # ---------- ENTORNO (venv + pip) ----------
  ("Entorno (venv + pip)",
   "python3 -m venv .venv",
   "Crea un 'entorno virtual': una caja donde viven las librerías SOLO de este proyecto, sin ensuciar el Python global. "
   "Resuelve: aislar dependencias por proyecto. Puede tardar unos segundos; no cortar con Ctrl+C."),
  ("Entorno (venv + pip)",
   "source .venv/bin/activate",
   "Entra/activa el entorno virtual. A partir de acá, python y pip apuntan a la caja del proyecto. "
   "Lo confirmás porque aparece (.venv) al inicio del prompt."),
  ("Entorno (venv + pip)",
   "deactivate",
   "Sale del entorno virtual y vuelve al Python global. Resuelve: cerrar la caja al terminar o para cambiar de proyecto."),
  ("Entorno (venv + pip)",
   "which python",
   "Muestra la ruta del python que se está usando. Resuelve: verificar que estás en el venv correcto "
   "(la ruta debe terminar en tu_proyecto/.venv/bin/python)."),
  ("Entorno (venv + pip)",
   "pip install fastapi uvicorn",
   "Descarga e instala librerías dentro del venv activo. fastapi = el framework (tu lógica/rutas); "
   "uvicorn = el servidor que escucha la red. Resuelve: traer lo que el proyecto necesita."),
  ("Entorno (venv + pip)",
   "pip list | grep -i fastapi",
   "pip list lista todo lo instalado; el | (pipe) pasa esa lista a grep, que filtra las líneas con 'fastapi' "
   "(-i = sin importar mayúsculas). Resuelve: confirmar que algo quedó instalado."),
  ("Entorno (venv + pip)",
   "python -m py_compile main.py",
   "Compila el archivo SIN ejecutarlo, solo para revisar sintaxis e indentación. Si no dice nada, está bien; "
   "si hay error, marca la línea. Resuelve: chequear el código antes de correrlo."),

  # ---------- EDITOR (nano) ----------
  ("Editor (nano)",
   "nano main.py",
   "Abre el editor de texto nano (dentro de la terminal) con ese archivo; si no existe, lo crea al guardar. "
   "Resuelve: editar archivos sin salir de la terminal. Para código conviene VSCode: respeta la indentación."),
  ("Editor (nano)",
   "Ctrl + O   (y luego Enter)",
   "Guarda el archivo en nano (O = 'write Out'); te confirma el nombre y con Enter aceptás. "
   "En la ayuda de nano, el símbolo ^ significa Ctrl."),
  ("Editor (nano)",
   "Ctrl + X",
   "Sale de nano y te devuelve a la terminal."),

  # ---------- FASTAPI · correr ----------
  ("FastAPI · correr",
   "uvicorn main:app --reload",
   "Levanta el servidor. main:app = la variable 'app' dentro del archivo main.py. --reload reinicia el server "
   "solo cada vez que guardás cambios (útil al desarrollar). Pone tu API a escuchar en http://127.0.0.1:8000."),
  ("FastAPI · correr",
   "Ctrl + C",
   "Frena un proceso que ocupa la terminal (como el server uvicorn) y te devuelve el prompt. "
   "Resuelve: salir de algo que 'se quedó corriendo'."),
  ("FastAPI · correr",
   "http://127.0.0.1:8000/docs",
   "La documentación interactiva que FastAPI genera sola (Swagger): ahí ves tus endpoints y mandás requests "
   "con 'Try it out'. Resuelve: probar la API sin instalar nada extra. Vive en el navegador, no en VSCode."),

  # ---------- CÓDIGO main.py ----------
  ("Código main.py",
   "from fastapi import FastAPI, HTTPException",
   "Importa el framework (FastAPI, para crear la app) y HTTPException (para devolver errores con su status code, "
   "ej. 404). Resuelve: traer las herramientas del framework."),
  ("Código main.py",
   "from pydantic import BaseModel",
   "Importa BaseModel, la base para definir el 'schema' (contrato) del dato que entra. "
   "Resuelve: poder validar automáticamente el body de las requests."),
  ("Código main.py",
   "app = FastAPI()",
   "Crea la aplicación. 'app' es el objeto al que le colgás las rutas y el que uvicorn busca (main:app)."),
  ("Código main.py",
   "registros = []",
   "Una lista vacía en RAM (memoria) donde se guardan los registros. Resuelve (provisorio): tener dónde meter "
   "los datos en la capa 1. Límite: se borra al reiniciar el server."),
  ("Código main.py",
   "contador = 1",
   "Variable para asignar un id único a cada registro nuevo. Imita una PK autoincremental "
   "(en la capa 2 eso lo hará la base de datos sola)."),
  ("Código main.py",
   "class RegistroIn(BaseModel):",
   "Define el contrato del dato que ENTRA (qué campos y de qué tipo). Al heredar de BaseModel, FastAPI valida "
   "el body solo (si falta algo o el tipo no calza → 422). No incluye 'id' porque el id lo pone el servidor."),
  ("Código main.py",
   "paciente: str",
   "Un campo del schema, de tipo texto (str): declara que el body debe traer 'paciente' como string. "
   "Criterio de tipos: str para texto, int para números, date/time para fechas/horas."),
  ("Código main.py",
   '@app.post("/registros", status_code=201)',
   "Decorador que conecta un POST a la ruta /registros con la función de abajo. POST = crear; "
   "status_code=201 = 'Created', el código correcto al crear algo."),
  ("Código main.py",
   "def crear(reg: RegistroIn):",
   "La función del endpoint. El parámetro tipado con el schema (reg: RegistroIn) le dice a FastAPI: "
   "leé el body y validámelo como RegistroIn. 'reg' llega ya limpio y validado."),
  ("Código main.py",
   "global contador",
   "Permite MODIFICAR la variable 'contador' (definida afuera) dentro de la función. Sin esto, Python la trataría "
   "como una variable local nueva y 'contador += 1' fallaría."),
  ("Código main.py",
   'nuevo = { "id": contador, "paciente": reg.paciente, ... }',
   "Arma el registro completo, ahora SÍ con su id (tomado del contador). Resuelve: construir el objeto final "
   "que se guarda y se devuelve, con el id que asigna el servidor (no el cliente)."),
  ("Código main.py",
   "registros.append(nuevo)",
   "Agrega el registro nuevo al final de la lista. Resuelve: guardarlo (en RAM, por ahora)."),
  ("Código main.py",
   "contador += 1",
   "Suma 1 al contador para que el próximo registro tenga un id distinto. Resuelve: mantener ids únicos."),
  ("Código main.py",
   "return nuevo",
   "Devuelve el registro creado (ya con id) como respuesta. Es lo que 'sale' del endpoint."),
  ("Código main.py",
   '@app.get("/registros")',
   "Decorador para un GET a /registros: leer/listar. La función de abajo devuelve la lista entera."),
  ("Código main.py",
   '@app.get("/registros/{id}")',
   "Endpoint GET con un 'path parameter' {id}: una parte variable de la ruta para pedir UN registro concreto "
   "(ej. /registros/2)."),
  ("Código main.py",
   "def obtener(id: int):",
   "La función recibe el id de la ruta; 'id: int' hace que FastAPI valide que sea entero "
   "(si mandan /registros/abc → 422 automático)."),
  ("Código main.py",
   'for r in registros:\n    if r["id"] == id:\n        return r',
   "Recorre la lista buscando el registro cuyo id coincide; si lo encuentra, lo devuelve. "
   "Resuelve: localizar un registro por su id."),
  ("Código main.py",
   'raise HTTPException(status_code=404, detail="registro no encontrado")',
   "Si no se encontró el registro, corta y devuelve un error 404 (no existe). Se usa 'raise' (no 'return') "
   "para frenar la ejecución y mandar el código de error correcto."),
]

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.sec { display: inline-block; font-size: 11px; letter-spacing: .8px; text-transform: uppercase;
  color: #fff; background: #0f766e; padding: 3px 10px; border-radius: 6px; margin-bottom: 12px; }
.cmd { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 17px;
  background: #0c1322; color: #e7ecf5; padding: 12px 14px; border-radius: 8px; white-space: pre-wrap; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.exp { color: #1a1a1a; }
"""

model = genanki.Model(
    MODEL_ID, "Comandos Dev QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def build():
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for i, (sec, front, back) in enumerate(CARDS):
        code = html.escape(front, quote=False)
        front_html = f'<div class="sec">{html.escape(sec)}</div><div class="cmd">{code}</div>'
        back_html = f'<div class="exp">{back}</div>'
        guid = genanki.guid_for(f"basdev:cmd:{i}")
        deck.add_note(genanki.Note(model=model, fields=[front_html, back_html],
                                   tags=["basicos", "dev", "comandos", "git", "fastapi"], guid=guid))
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "Basicos_Comandos_GitFastAPI.apkg")
    genanki.Package(deck).write_to_file(out)
    print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
