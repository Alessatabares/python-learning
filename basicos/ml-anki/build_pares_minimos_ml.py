# -*- coding: utf-8 -*-
"""Corrida 4 - PARES MINIMOS del proyecto de Machine Learning (vision medica / OCT).

Estructura del metodo: caso ancla + UNA sola pieza que cambia -> que se rompe.
Si cambian dos variables la tarjeta esta mal y se parte en dos.

Front: el ancla (lo correcto) + la pieza que cambia.
Back:  que se rompe + como se arregla.

Genera Basicos_MachineLearning_ParesMinimos.apkg en ../output/.
Correr:  ../../.venv/bin/python build_pares_minimos_ml.py
"""
import os
import genanki

MODEL_ID = 1607392352          # propio de este deck, sin colision
DECK_ID = 1500014004           # esquema 1500_AA_C con AA=14 (Machine Learning)
DECK_NAME = "Basicos Dev::Machine Learning::Pares Minimos"

# (seccion, ancla, pieza_que_cambia, que_se_rompe, como_se_arregla)
CARDS = [
  # ---------- ENTORNO ----------
  ("Entorno",
   "Activas el venv y despues corres pip install torch.",
   "Corres el mismo pip install SIN activar el venv.",
   "Torch se instala en el Python del sistema. El proyecto no lo ve: al correr tu script sale "
   "ModuleNotFoundError aunque acabas de instalarlo. Y ensucias el sistema para todos tus otros proyectos.",
   "Antes de cualquier pip: <b>source .venv/bin/activate</b> y confirmar con <b>which python</b> "
   "que la ruta termina en .venv/bin/python."),
  ("Entorno",
   "Guardas requirements.txt con las versiones congeladas.",
   "No lo guardas: instalaste 'a mano' y ya funciona.",
   "En tres meses reinstalas, pip te da versiones nuevas, y el codigo que funcionaba deja de correr "
   "por un cambio de API. No sabes que version tenias.",
   "<b>pip freeze &gt; requirements.txt</b> al terminar de instalar, y commitearlo. "
   "Es el unico archivo que hace tu proyecto reproducible."),

  # ---------- REPOSITORIO ----------
  ("Repositorio",
   "Creas el .gitignore con datos/ ANTES del primer commit.",
   "Lo creas DESPUES de haber commiteado la carpeta de datos.",
   "El .gitignore no afecta a lo que git ya rastrea. Los 5 GB siguen en el historial y siguen subiendo. "
   "Ignorar tarde no deshace nada.",
   "<b>git rm --cached -r datos/</b> (los saca del rastreo, los deja en tu disco) y commitear. "
   "El historial viejo los conserva igual: si eran enormes, hay que reescribir historial."),
  ("Repositorio",
   "kaggle.json vive en ~/.kaggle/ con chmod 600.",
   "Lo dejas dentro de la carpeta del proyecto.",
   "Se sube a GitHub en el primer push. Con un repo publico, cualquiera descarga tu token y actua "
   "con tu cuenta de Kaggle.",
   "El token va SIEMPRE fuera del repo, en el HOME. Y si ya se subio: <b>revocar el token en Kaggle "
   "y generar uno nuevo</b>. Borrar el archivo no basta, el historial lo conserva."),
  ("Repositorio",
   "El repo lleva el codigo + un README con el comando de descarga.",
   "El repo lleva tambien los 5 GB de imagenes.",
   "GitHub rechaza cualquier archivo de mas de 100 MB, y si el dataset pasa en trozos, clonar el repo "
   "se vuelve inviable para cualquiera (incluida tu, en otra maquina).",
   "Los datos NUNCA van al repo: va la <b>instruccion para regenerarlos</b>. Esa es justamente la razon "
   "de bajarlos por CLI y no a mano."),

  # ---------- DATOS ----------
  ("Datos",
   "unzip -q archivo.zip -d datos/crudo",
   "El mismo comando sin la opcion -d.",
   "Las 84.000 imagenes se descomprimen en el directorio donde estas parada, mezcladas con tu codigo. "
   "Limpiarlo a mano es una pesadilla.",
   "-d dice EN QUE carpeta extraer. Reflejo: revisar con <b>pwd</b> donde estas antes de descomprimir "
   "cualquier cosa grande."),
  ("Datos",
   "Corres kaggle datasets download con el token ya colocado.",
   "Lo corres sin haber puesto kaggle.json en ~/.kaggle/.",
   "Error 401 / 403. La CLI no sabe quien eres, y varios datasets exigen ademas haber aceptado sus "
   "condiciones en la web una primera vez.",
   "Bajar el token desde Kaggle (Settings -&gt; API -&gt; Create New Token), moverlo a ~/.kaggle/ "
   "y darle <b>chmod 600</b>."),
  ("Datos",
   "Las imagenes se redimensionan todas a 224x224 antes del DataLoader.",
   "Se las pasas en su tamano original, que varia de imagen a imagen.",
   "El DataLoader no puede apilar un lote con tensores de distinto tamano: RuntimeError de dimensiones "
   "en la primera iteracion.",
   "<b>transforms.Resize((224,224))</b> dentro del Compose. El 224 no es arbitrario: es el tamano con "
   "el que se entreno la red que estas tomando prestada."),
  ("Datos",
   "Normalizas con la media y desviacion de ImageNet.",
   "Te saltas la normalizacion: solo conviertes a tensor.",
   "La red preentrenada recibe numeros en un rango que no reconoce. No da error: simplemente converge "
   "mucho peor y no entiendes por que.",
   "<b>transforms.Normalize(mean, std)</b> con los valores de ImageNet. Usar una red prestada obliga "
   "a preparar la entrada exactamente como ella espera."),
  ("Datos",
   "Los splits se hacen de modo que un paciente esta en train O en test, nunca en ambos.",
   "Repartes por imagen, sin mirar de que paciente viene cada una.",
   "Fuga de datos. El mismo ojo aparece a los dos lados: el modelo reconoce al paciente, no la patologia. "
   "Sacas 99% y el modelo fracasa con datos nuevos.",
   "Partir por <b>paciente</b>, no por imagen. Es el error que mas invalida papers de imagen medica."),
  ("Datos",
   "shuffle=True en el DataLoader de entrenamiento.",
   "Lo dejas en False.",
   "Las imagenes llegan agrupadas por clase: primero todas las CNV, luego todas las DME. El modelo "
   "aprende el orden del lote en vez de la imagen, y el entrenamiento se desestabiliza.",
   "shuffle=True <b>solo en train</b>. En validacion y test va False, porque ahi no se aprende y quieres "
   "el mismo orden siempre."),

  # ---------- ENTRENAMIENTO ----------
  ("Entrenamiento",
   "Congelas las capas de abajo y entrenas solo la ultima.",
   "Descongelas la red entera teniendo pocas imagenes.",
   "La red destruye lo que sabia de ImageNet (olvido catastrofico) y sobreajusta tus pocas imagenes. "
   "Rinde peor que si no hubieras tocado nada.",
   "Con pocos datos: congelar todo y entrenar solo la capa nueva. El fine-tuning completo se desbloquea "
   "cuando tienes muchos datos, y con un learning rate mucho mas bajo."),
  ("Entrenamiento",
   "learning rate = 1e-3.",
   "learning rate = 1e-1.",
   "Los pasos de correccion son enormes: la perdida salta, se va a NaN y nunca converge. "
   "Parece que el codigo esta roto, pero el codigo esta bien.",
   "Ante una perdida que explota, lo PRIMERO que se baja es el lr (un orden de magnitud cada vez). "
   "Es el hiperparametro que mas rompe."),
  ("Entrenamiento",
   "batch_size=32 entrenando en CPU.",
   "batch_size=256.",
   "Se queda sin memoria RAM y el proceso muere, o entra en swap y cada epoch tarda una eternidad.",
   "El batch lo limita tu hardware, no tu ambicion. En CPU: 16-32. Si falla por memoria, bajarlo es "
   "lo primero que se prueba."),
  ("Entrenamiento",
   "zero_grad() -&gt; backward() -&gt; step(), en ese orden, en cada lote.",
   "Olvidas zero_grad().",
   "Los gradientes de cada lote se SUMAN a los del anterior. El modelo aprende basura. "
   "Lo peor: no lanza ningun error, solo entrena mal.",
   "Memorizar el trio como una unidad: <b>borrar, calcular, aplicar</b>. Si el entrenamiento no mejora "
   "y no hay error, revisar esto primero."),
  ("Entrenamiento",
   "La perdida de train baja y la de validacion tambien baja.",
   "La de train sigue bajando pero la de validacion empieza a SUBIR.",
   "Overfitting: el modelo dejo de aprender el problema y empezo a memorizar tus imagenes concretas. "
   "Seguir entrenando solo lo empeora.",
   "Parar en el punto donde la validacion toco su minimo (early stopping) y quedarse con esos pesos. "
   "Por eso se mira la curva de validacion, no solo la de train."),

  # ---------- EVALUACION ----------
  ("Evaluacion",
   "Eliges los hiperparametros mirando el set de VALIDACION.",
   "Los eliges mirando el set de TEST.",
   "El test deja de ser un juez independiente: lo has usado para decidir. Tu numero final esta inflado "
   "y no predice nada sobre datos nuevos.",
   "Train para aprender, validacion para decidir, <b>test se abre una sola vez</b>, al final, y ya no "
   "se cambia nada despues."),
  ("Evaluacion",
   "Reportas 95% de accuracy con cuatro clases balanceadas.",
   "Reportas 95% de accuracy donde una clase es el 95% de los datos.",
   "Un modelo que responde siempre la clase mayoritaria saca ese mismo 95% sin haber aprendido nada. "
   "El numero es real y la conclusion es falsa.",
   "En datos desbalanceados el accuracy no significa nada. Reportar <b>sensibilidad y especificidad por "
   "clase</b> y mirar la matriz de confusion."),
  ("Evaluacion",
   "Entrenas con ~500 imagenes por clase, balanceadas.",
   "Entrenas con el dataset crudo: 37.000 CNV frente a 8.600 drusas.",
   "El modelo aprende que apostar por CNV casi siempre paga. Las drusas, que es lo que quieres detectar "
   "temprano, son justo lo que peor detecta.",
   "Balancear el subset, o pesar las clases en la perdida (<b>class_weight</b>). "
   "Mirar el conteo por carpeta ANTES de entrenar, no despues."),
  ("Evaluacion",
   "Pones model.eval() y torch.no_grad() antes de evaluar.",
   "Olvidas model.eval().",
   "Dropout y BatchNorm siguen en modo entrenamiento: apagan neuronas al azar y actualizan estadisticas. "
   "El mismo test da un resultado distinto cada vez que lo corres.",
   "<b>model.eval()</b> al evaluar y <b>model.train()</b> al volver a entrenar. Si tus metricas bailan "
   "sin que cambies nada, es esto."),
  ("Evaluacion",
   "El Grad-CAM senala la zona de liquido intrarretiniano de la macula.",
   "El Grad-CAM senala el borde negro de la imagen o la marca del aparato.",
   "Shortcut learning: el modelo acerto, pero por la maquina que tomo la imagen, no por la retina. "
   "Cambias de hospital y el rendimiento se cae entero.",
   "Recortar la zona util de la imagen y volver a entrenar. Es la razon de existir del Grad-CAM: "
   "una metrica alta no dice si miro lo correcto."),
]

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.6; }
.sec { display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #4c1d95; color: #fff; border-radius: 6px; font-size: 13px;
  letter-spacing: 0.6px; font-weight: 700; text-transform: uppercase; }
.lab { font-size: 12px; letter-spacing: 1px; font-weight: 700; text-transform: uppercase;
  color: #6b7280; margin-bottom: 4px; }
.ancla { background: #ecfdf5; border-left: 4px solid #047857; padding: 10px 14px;
  border-radius: 0 6px 6px 0; margin-bottom: 14px; }
.cambio { background: #fef2f2; border-left: 4px solid #b91c1c; padding: 10px 14px;
  border-radius: 0 6px 6px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 14px; }
.rompe { font-weight: 600; color: #991b1b; margin-bottom: 12px; }
.fix { background: #eff6ff; border-left: 4px solid #1d4ed8; padding: 10px 14px;
  border-radius: 0 6px 6px 0; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model = genanki.Model(
    MODEL_ID, "Basicos ML Pares Minimos",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def build():
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for i, (sec, ancla, cambio, rompe, fix) in enumerate(CARDS):
        front = (
            f'<div class="sec">{sec}</div>'
            f'<div class="ancla"><div class="lab">Ancla</div>{ancla}</div>'
            f'<div class="cambio"><div class="lab">Cambia una pieza</div>{cambio}</div>'
            '<div class="prompt">&iquest;Qu&eacute; se rompe, y c&oacute;mo se arregla?</div>'
        )
        back = (
            f'<div class="rompe">{rompe}</div>'
            f'<div class="fix"><div class="lab">Arreglo</div>{fix}</div>'
        )
        # GUID estable por posicion: reimportar tras corregir ACTUALIZA, no duplica.
        guid = genanki.guid_for(f"basdev:mlpar:{i}")
        deck.add_note(genanki.Note(model=model, fields=[front, back],
                                   tags=["basicos", "dev", "machine_learning", "pares_minimos"],
                                   guid=guid))
    out = os.path.join(os.path.dirname(__file__), "..", "output",
                       "Basicos_MachineLearning_ParesMinimos.apkg")
    genanki.Package(deck).write_to_file(out)
    print(f"OK: Basicos_MachineLearning_ParesMinimos.apkg  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
