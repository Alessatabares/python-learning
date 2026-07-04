# -*- coding: utf-8 -*-
"""Deck de comandos/código de la Capa 2: "Base de datos con SQLite + SQLAlchemy".

Front: el comando o fragmento de código.
Back:  qué hace / qué resuelve / por qué.

Solo cubre lo NUEVO de la capa 2 (no repite git/venv básicos del deck de capa 1).
Genera Basicos_Comandos_Capa2_DB.apkg en ./output/.
Correr:  ../../.venv/bin/python build_comandos_capa2.py
"""
import os
import html
import genanki

MODEL_ID = 1607392326        # distinto del deck de capa 1 (…325)
DECK_ID = 1599000002         # distinto del deck de capa 1 (…001)
DECK_NAME = "Basicos Dev::Comandos (Capa 2 · Base de datos)"

# (seccion, front_codigo, back_explicacion)
CARDS = [
  # ---------- ENTORNO (SQLAlchemy) ----------
  ("Entorno (SQLAlchemy)",
   "pip install sqlalchemy",
   "Instala SQLAlchemy (el ORM: el traductor entre objetos Python y la base de datos) DENTRO del venv activo. "
   "Ojo clave: pip instala en el venv que tenés ACTIVADO, no en la carpeta donde estás parada. "
   "Resuelve: traer la herramienta que persiste datos en una base."),
  ("Entorno (SQLAlchemy)",
   "echo $VIRTUAL_ENV",
   "Muestra la ruta del venv que tenés activo ahora mismo. Resuelve: confirmar que vas a instalar en la caja "
   "correcta (debe terminar en tu_proyecto/.venv). El prompt muestra (.venv) pero NO de cuál proyecto; esto sí."),

  # ---------- database.py · CONEXIÓN ----------
  ("database.py · conexión",
   "from sqlalchemy import create_engine",
   "Trae create_engine, la función que fabrica el 'engine' (el cable a la base). Vive en el Core de SQLAlchemy "
   "(el nivel de arriba, sqlalchemy). Resuelve: poder abrir la conexión."),
  ("database.py · conexión",
   "from sqlalchemy.orm import sessionmaker, declarative_base",
   "Del submódulo .orm (la 'agencia de traducción'): sessionmaker (fábrica de conversaciones con la base) y "
   "declarative_base (el cuaderno donde se registran las tablas). El punto en sqlalchemy.orm significa "
   "'lo que está dentro de'. Van aparte de create_engine porque son de otra capa (ORM, no Core)."),
  ("database.py · conexión",
   "engine = create_engine('sqlite:///registro_estudios.db', echo=True)",
   "Crea el engine (el enchufe a la base). 'sqlite:///archivo.db' es la connection string: tipo de base + ruta. "
   "SQLite no tiene servidor: la base ES un archivo en tu disco (se crea solo si no existe). "
   "echo=True imprime en la terminal el SQL que SQLAlchemy genera (espejo para aprender)."),
  ("database.py · conexión",
   "SessionLocal = sessionmaker(bind=engine)",
   "Crea una FÁBRICA de sessions, amarrada (bind) al engine. No es una session: es el molde que fabrica una "
   "conversación nueva cada vez. Resuelve: que cada petición tenga su propia session sin cruzarse."),
  ("database.py · conexión",
   "Base = declarative_base()",
   "Crea el 'cuaderno' (base declarativa) donde se anotan las tablas. Cada modelo hereda de Base para quedar "
   "registrado. Resuelve: tener un índice de todas las tablas para poder crearlas luego de un golpe."),

  # ---------- models.py · LA TABLA ----------
  ("models.py · la tabla",
   "from sqlalchemy import Column, Integer, String",
   "Trae las herramientas para declarar columnas: Column (=esto es una columna), Integer (número entero), "
   "String (texto → VARCHAR en SQL). El tipo debe calzar con la naturaleza del dato."),
  ("models.py · la tabla",
   "from database import Base",
   "Importa Base de TU propio archivo database.py (nombre del módulo, SIN el .py). Distinto de importar de "
   "una librería: lo que vos creaste sale de tu archivo; las herramientas salen de sqlalchemy."),
  ("models.py · la tabla",
   "class Registro(Base):",
   "Define el modelo: la clase que describe la tabla. Hereda de Base (no de BaseModel) para quedar registrada "
   "en el cuaderno. Es el 'gemelo' de RegistroIn de Pydantic, pero describe la TABLA, no lo que entra por HTTP."),
  ("models.py · la tabla",
   '__tablename__ = "registros"',
   "Nombre 'mágico' fijo que SQLAlchemy busca: dice cómo se llamará la tabla dentro de la base. La clase es "
   "Registro (singular), la tabla registros (plural) — se conectan explícitamente con esta línea."),
  ("models.py · la tabla",
   "id = Column(Integer, primary_key=True)",
   "La clave primaria (PK): identificador único de cada fila, nunca vacío, nunca repetido. primary_key=True hace "
   "que la BASE genere el id sola y autoincremental. Jubila el 'contador' global de la capa 1."),
  ("models.py · la tabla",
   "paciente = Column(String)",
   "Una columna de texto. Se repite el patrón (protocolo, fecha, hora, doctor). Fecha y hora van como String "
   "(texto tipo '2026-07-04'), no Integer, porque no son números puros. String se traduce a VARCHAR en SQL."),

  # ---------- crear_db.py · FABRICAR LA TABLA ----------
  ("crear_db.py · fabricar",
   "from database import engine, Base",
   "Trae DOS cosas de database (mismo origen → una línea con coma): el engine (a qué .db) y Base (el cuaderno "
   "con las tablas registradas). Resuelve: juntar lo necesario para construir la tabla."),
  ("crear_db.py · fabricar",
   "import models",
   "Importa el archivo models ENTERO (sin 'from', sin nombrar nada). ¿Por qué? Al leer models, Python encuentra "
   "'class Registro' y la REGISTRA en Base. Sin esto, create_all no vería la tabla y el .db nacería vacío."),
  ("crear_db.py · fabricar",
   "Base.metadata.create_all(bind=engine)",
   "La ORDEN que construye en disco todas las tablas registradas en Base (lee el plano → levanta la casa). "
   "No lleva '=' porque no fabrica ni guarda nada: es una acción (objeto.accion()). Es seguro correrla varias "
   "veces: primero pregunta si la tabla existe y no la pisa."),
  ("crear_db.py · fabricar",
   "python crear_db.py",
   "Ejecuta el script una vez. Al correrlo nace el archivo registro_estudios.db en la carpeta. "
   "Regla: nunca subas a git código que no corriste; correrlo verifica que funciona."),

  # ---------- main.py · ENDPOINTS CON BASE ----------
  ("main.py · con base",
   "from database import SessionLocal",
   "Trae la fábrica de sessions a main.py, para que los endpoints puedan abrir conversaciones con la base."),
  ("main.py · con base",
   "from models import Registro",
   "Trae el modelo a main.py, para crear objetos Registro (al guardar) y consultarlos (al leer)."),
  ("main.py · con base",
   "db = SessionLocal()",
   "Abre una session (conversación) NUEVA. Va DENTRO del endpoint: se ejecuta en cada petición, así cada cliente "
   "tiene la suya y no se cruzan. La fábrica vive en database; la conversación nace acá."),
  ("main.py · con base",
   "nuevo = Registro(paciente=reg.paciente, protocolo=reg.protocolo, ...)",
   "Crea un OBJETO del modelo (ya no un dict) con los datos que llegaron. NO se le pasa 'id': lo genera la base. "
   "Izquierda del = es la columna; derecha es el dato que vino en la request."),
  ("main.py · con base",
   "db.add(nuevo)",
   "Apunta el objeto en la 'bandeja de salida' de la session. Todavía NO lo escribe en disco: solo lo deja "
   "pendiente. (Como git add: preparás, no guardás aún.)"),
  ("main.py · con base",
   "db.commit()",
   "Escribe de verdad en el disco lo que estaba pendiente. Es el 'guardar definitivo'. "
   "Flujo de escritura: add (apuntar) → commit (guardar)."),
  ("main.py · con base",
   "db.refresh(nuevo)",
   "Recarga el objeto desde la base para traer lo que ella le puso: el id recién generado. Sin esto, 'nuevo' "
   "no sabría su id (se creó sin él). Imagen: preguntar '¿qué número de ficha me tocó?'."),
  ("main.py · con base",
   "db.close()",
   "Cierra la conversación con la base (colgás el teléfono). Se hace al terminar de usar la session en el endpoint."),
  ("main.py · con base",
   "db.query(Registro).all()",
   "LEER: consulta la tabla Registro y trae TODAS las filas (una lista). Es el verbo de lectura, la otra mitad "
   "de la session (add/commit escriben; query lee). Reemplaza el 'return registros' de la lista RAM."),
  ("main.py · con base",
   "db.query(Registro).filter(Registro.id == id).first()",
   "Busca UNA fila por id: filter = el 'dónde' (solo filas cuya columna id == al id pedido; == es comparación, "
   "no asignación); first() = trae el primero, o None si no hay. Reemplaza el bucle 'for' de búsqueda manual."),
  ("main.py · con base",
   "if registro is None:\n    raise HTTPException(status_code=404, detail='registro no encontrado')",
   "Si el query no encontró nada, first() devuelve None → se corta con un 404 (no existe). "
   "Se usa 'raise' (no return) para frenar y mandar el status de error correcto."),

  # ---------- GIT (remoto adelantado) ----------
  ("Git (remoto adelantado)",
   "[rejected]  main -> main  (fetch first)",
   "Error al hacer push: GitHub tiene commits que vos no tenés en local, así que no te deja pisar. "
   "Ojo: 'git status' puede decir 'up to date' porque muestra una foto vieja; git no habla con GitHub hasta "
   "el push. Solución: bajar antes de subir."),
  ("Git (remoto adelantado)",
   "git pull --no-rebase",
   "Baja los commits del remoto y los FUSIONA (merge) con los tuyos. Se usa cuando el push sale [rejected]. "
   "Si abre el editor nano pidiendo mensaje de merge: Ctrl+O, Enter, Ctrl+X. Luego 'git push' ya sube todo. "
   "Ciclo completo real: commit → pull → (resolver merge) → push."),

  # ---------- .gitignore ----------
  (".gitignore",
   "*.db",
   "Patrón con comodín (*) que ignora CUALQUIER archivo terminado en .db. Los archivos de base de datos NO se "
   "suben a git: son datos locales que se regeneran. Distinto de un nombre literal como 'db.sqlite3', que solo "
   "ignora ESE nombre exacto."),
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
    MODEL_ID, "Comandos Dev QA (Capa 2)",
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
        guid = genanki.guid_for(f"basdev:cmd2:{i}")
        deck.add_note(genanki.Note(model=model, fields=[front_html, back_html],
                                   tags=["basicos", "dev", "comandos", "capa2", "sqlalchemy", "database"], guid=guid))
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "Basicos_Comandos_Capa2_DB.apkg")
    genanki.Package(deck).write_to_file(out)
    print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
