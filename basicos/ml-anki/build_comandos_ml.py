# -*- coding: utf-8 -*-
"""Corrida 3 - COMANDOS del proyecto de Machine Learning (vision medica / OCT).

Front: el comando literal.
Back:  que hace, cuando se usa, y la trampa.

Genera Basicos_MachineLearning_Comandos.apkg en ../output/.
Correr:  ../../.venv/bin/python build_comandos_ml.py
"""
import os
import html
import genanki

MODEL_ID = 1607392351          # propio de este deck, sin colision
DECK_ID = 1500014003           # esquema 1500_AA_C con AA=14 (Machine Learning)
DECK_NAME = "Basicos Dev::Machine Learning::Comandos"

# (seccion, front_comando, back_explicacion)
CARDS = [
  # ---------- ENTORNO ----------
  ("Entorno",
   "mkdir -p ~/projects/oct-ml/{datos/crudo,src,notas}",
   "Crea el arbol del proyecto de una sola vez. -p crea los padres que falten y no se queja "
   "si ya existen. Las llaves expanden varias rutas en un comando. "
   "Resuelve: montar la estructura antes de escribir una linea de codigo."),
  ("Entorno",
   "python3 -m venv .venv",
   "Crea un entorno virtual en la carpeta .venv: una copia aislada de Python con su propio pip. "
   "Resuelve: que las librerias de este proyecto no se mezclen con las del sistema ni con las de otro proyecto. "
   "Ojo: crear no es activar. Despues de esto todavia estas fuera."),
  ("Entorno",
   "source .venv/bin/activate",
   "Activa el entorno: a partir de aqui 'python' y 'pip' son los de dentro del proyecto. "
   "Tu prompt cambia a (.venv). Hay que repetirlo en CADA terminal nueva. "
   "Trampa: instalar sin activar manda la libreria al sistema y el proyecto no la ve."),
  ("Entorno",
   "which python",
   "Muestra la RUTA del python que se esta usando ahora mismo. Si termina en .venv/bin/python estas dentro. "
   "Resuelve: confirmar el entorno cuando el prompt no lo deja claro."),
  ("Entorno",
   "deactivate",
   "Sale del entorno virtual sin cerrar la terminal: python y pip vuelven a ser los del sistema."),
  ("Entorno",
   "pip freeze &gt; requirements.txt",
   "Escribe en un archivo la lista exacta de librerias instaladas CON su version. "
   "Resuelve: que otra persona (o tu en tres meses) reproduzca la instalacion igualita. "
   "Correrlo solo con el venv activado: si no, congelas las librerias del sistema."),
  ("Entorno",
   "pip install -r requirements.txt",
   "Instala de golpe todo lo que dice ese archivo, en las versiones anotadas. "
   "Resuelve: levantar el proyecto en otra maquina en un comando."),

  # ---------- INSTALACION ----------
  ("Instalacion",
   "pip install --upgrade pip",
   "Actualiza el propio instalador antes de instalar nada pesado. "
   "Resuelve: errores raros de compatibilidad con paquetes grandes como torch. Primer comando tras activar."),
  ("Instalacion",
   "pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu",
   "Instala PyTorch y torchvision en su version para CPU. --index-url apunta al servidor propio de PyTorch, "
   "porque torch se publica en builds distintos segun el hardware. "
   "Resuelve: no bajar ~2 GB de CUDA que no vas a poder usar si no tienes GPU."),
  ("Instalacion",
   "pip install matplotlib scikit-learn pandas kaggle",
   "El resto del stack: ver imagenes y curvas (matplotlib), metricas de evaluacion (scikit-learn), "
   "tablas de resultados (pandas) y descarga de datasets (kaggle)."),
  ("Instalacion",
   "nvidia-smi",
   "Pregunta al sistema si hay una GPU NVIDIA y cuanta memoria tiene. "
   "Resuelve: decidir ANTES de instalar si vas por la version CPU o la CUDA. "
   "Si dice 'command not found', no hay GPU utilizable: vas por CPU."),
  ("Instalacion",
   'python -c "import torch; print(torch.__version__, torch.cuda.is_available())"',
   "Comprueba desde Python que torch quedo instalado y si ve una GPU. "
   "False significa que entrenaras en CPU (correcto y suficiente con un dataset pequeno). "
   "Resuelve: verificar la instalacion sin abrir un script."),
  ("Instalacion",
   "pip list | grep torch",
   "Filtra la lista de instalados para ver solo lo que contiene 'torch', con su version. "
   "Resuelve: confirmar rapido que algo esta y en que version."),

  # ---------- KAGGLE ----------
  ("Kaggle",
   "mkdir -p ~/.kaggle",
   "Crea la carpeta oculta donde la CLI de Kaggle busca tus credenciales. "
   "Va en tu HOME, FUERA del proyecto: asi el token nunca puede colarse al repo."),
  ("Kaggle",
   "cp /mnt/c/Users/*/Downloads/kaggle.json ~/.kaggle/",
   "Copia el token que bajaste desde Kaggle (Settings -&gt; API -&gt; Create New Token) al sitio donde la CLI lo busca. "
   "La ruta /mnt/c/... es como WSL ve el disco de Windows. "
   "Resuelve: autenticar la terminal sin escribir la clave a mano."),
  ("Kaggle",
   "chmod 600 ~/.kaggle/kaggle.json",
   "Deja el archivo legible SOLO por ti (6 = leer+escribir dueno, 0 y 0 para los demas). "
   "Kaggle avisa si el permiso es mas abierto. Resuelve: que otro usuario de la maquina no lea tu credencial."),
  ("Kaggle",
   'kaggle datasets list -s "retinal oct"',
   "Busca datasets publicos por texto, sin salir de la terminal. Devuelve el slug owner/nombre que necesitas para bajarlo. "
   "Resuelve: encontrar el identificador exacto del dataset."),
  ("Kaggle",
   "kaggle datasets download -d paultimothymooney/kermany2018 -p datos/crudo",
   "Baja el dataset identificado por su slug (-d) a la carpeta que le digas (-p). Llega como un .zip. "
   "Resuelve: una descarga REPETIBLE: este comando queda escrito en el README y cualquiera rehace tu dataset. "
   "Requiere kaggle.json ya colocado; sin el da 401/403."),
  ("Kaggle",
   "unzip -q datos/crudo/kermany2018.zip -d datos/crudo",
   "Descomprime. -q (quiet) evita imprimir 84.000 lineas. -d dice EN QUE carpeta dejarlo. "
   "Trampa: sin -d te vacia el zip entero en el directorio donde estas parada."),
  ("Kaggle",
   "unzip -t datos/crudo/kermany2018.zip",
   "Prueba la integridad del zip sin extraerlo (-t = test). "
   "Resuelve: distinguir 'la descarga se corto' de 'el codigo esta mal' antes de perder una hora."),

  # ---------- VERIFICAR ----------
  ("Verificar",
   "du -sh datos/crudo",
   "'disk usage': cuanto ocupa esa carpeta, -s sumado y -h en unidades legibles (GB). "
   "Resuelve: confirmar que bajo lo que debia bajar y controlar el disco."),
  ("Verificar",
   "find datos/crudo -maxdepth 4 -type d",
   "Lista solo DIRECTORIOS (-type d) hasta 4 niveles de profundidad. "
   "Resuelve: ver la estructura real del dataset (que suele venir anidada de forma rara) sin imprimir 84.000 rutas de archivo."),
  ("Verificar",
   'find datos/crudo -name "*.jpeg" | wc -l',
   "Encuentra todos los archivos .jpeg y cuenta las lineas: el total de imagenes. "
   "Resuelve: comprobar que el numero coincide con lo que anuncia el dataset."),
  ("Verificar",
   'for d in datos/crudo/OCT2017/train/*/; do echo "$d $(ls "$d" | wc -l)"; done',
   "Recorre cada carpeta de clase e imprime su nombre y cuantos archivos tiene. "
   "Resuelve: LA pregunta previa a entrenar: esta balanceado el dataset? Si una clase tiene 4 veces mas "
   "que otra, eso decide tu metrica y tu estrategia."),
  ("Verificar",
   "ls datos/crudo/OCT2017/train",
   "Muestra los nombres de las carpetas de clase. Importa porque ImageFolder usa esos nombres COMO etiquetas: "
   "si estan mal escritos, tus etiquetas estan mal."),

  # ---------- PROTEGER EL REPO ----------
  ("Proteger",
   "printf '.venv/\\ndatos/\\n__pycache__/\\n*.pth\\n' &gt; .gitignore",
   "Crea el .gitignore con las cuatro cosas que nunca deben subir: el entorno, los datos, la cache de Python "
   "y los pesos del modelo. Tiene que existir ANTES del primer commit. "
   "Resuelve: que un repo de codigo no se convierta en un repo de 5 GB."),
  ("Proteger",
   "git status",
   "Muestra que archivos cambiaron y cuales estan listos para subir. "
   "Resuelve: mirar SIEMPRE antes de hacer commit. Si ves datos/ o .venv/ aqui, tu .gitignore no esta funcionando."),
  ("Proteger",
   "git add -n .",
   "-n (dry run) muestra que se AGREGARIA, sin agregar nada. "
   "Resuelve: ensayo en seco antes de un add masivo; la red de seguridad contra subir algo enorme por accidente."),
  ("Proteger",
   "git check-ignore -v datos/",
   "Dice si esa ruta esta siendo ignorada y POR QUE regla del .gitignore (-v muestra la linea culpable). "
   "Resuelve: depurar un .gitignore que crees que funciona y no funciona."),
  ("Proteger",
   "git rm --cached -r datos/",
   "Saca la carpeta del rastreo de git pero la DEJA en tu disco (--cached). -r para recorrerla entera. "
   "Resuelve: el arreglo cuando ya commiteaste algo que debia estar ignorado. "
   "Ojo: el historial viejo lo sigue conteniendo."),
  ("Proteger",
   "git log --oneline -- datos/",
   "Muestra si esa ruta aparece en algun commit del historial. "
   "Resuelve: confirmar si algo pesado o secreto llego a entrar alguna vez."),

  # ---------- PYTORCH: DATOS ----------
  ("PyTorch datos",
   "from torchvision import datasets, transforms",
   "Importa las dos piezas de entrada: datasets (leer carpetas de imagenes) y transforms (prepararlas). "
   "Resuelve: la mitad 'datos' del proyecto en una linea."),
  ("PyTorch datos",
   'datasets.ImageFolder("datos/train", transform=tf)',
   "Lee una carpeta donde cada SUBCARPETA es una clase, y devuelve pares (imagen, etiqueta). "
   "Resuelve: no tener que escribir un csv de etiquetas: la estructura de carpetas ES la etiqueta. "
   "Trampa: el orden de las clases es alfabetico, no el que tu imaginas."),
  ("PyTorch datos",
   "transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(), transforms.Normalize(mean, std)])",
   "Encadena la preparacion: redimensionar al tamano que la red espera, convertir a tensor "
   "y normalizar con la media/desviacion de ImageNet. "
   "Resuelve: hablarle a la red preentrenada en el formato exacto con el que fue entrenada."),
  ("PyTorch datos",
   "DataLoader(ds, batch_size=32, shuffle=True)",
   "Entrega las imagenes en lotes de 32 y mezcla el orden en cada epoch. "
   "Resuelve: alimentar el entrenamiento sin cargar todo en memoria. "
   "shuffle=True solo en train; en validacion y test va en False."),

  # ---------- PYTORCH: MODELO ----------
  ("PyTorch modelo",
   'models.resnet18(weights="IMAGENET1K_V1")',
   "Carga una ResNet18 con los pesos ya aprendidos de ImageNet. "
   "Resuelve: el transfer learning. La red ya sabe ver bordes, texturas y formas; tu solo le ensenas a nombrar OCT."),
  ("PyTorch modelo",
   "model.fc = nn.Linear(512, 4)",
   "Reemplaza la ultima capa (que decidia entre 1000 clases de ImageNet) por una de 4 salidas: "
   "CNV, DME, drusas, normal. "
   "Resuelve: EL gesto central del transfer learning. 512 es lo que sale de la ResNet18."),
  ("PyTorch modelo",
   "for p in model.parameters(): p.requires_grad = False",
   "Congela todos los pesos: dejan de actualizarse. Se hace ANTES de reemplazar la ultima capa "
   "(la nueva nace descongelada). "
   "Resuelve: entrenar rapido y sobreajustar menos cuando tienes pocas imagenes."),
  ("PyTorch modelo",
   "criterion = nn.CrossEntropyLoss()",
   "La funcion de perdida estandar de clasificacion multiclase: mide que tan mal predijo. "
   "Resuelve: darle al entrenamiento un numero concreto que bajar."),
  ("PyTorch modelo",
   "optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)",
   "El optimizador aplica la correccion a los pesos; lr es el tamano del paso. "
   "Resuelve: quien y con que fuerza modifica la red. lr es el hiperparametro que mas rompe cuando se equivoca."),

  # ---------- PYTORCH: BUCLE Y EVALUACION ----------
  ("PyTorch bucle",
   "optimizer.zero_grad()",
   "Borra los gradientes de la iteracion anterior. "
   "Resuelve: que las correcciones no se acumulen una encima de otra. "
   "Trampa: si lo olvidas el modelo aprende basura y no da ningun error."),
  ("PyTorch bucle",
   "loss.backward()",
   "Calcula, hacia atras, cuanta culpa tiene cada peso en el error cometido (los gradientes). "
   "Resuelve: el 'aprender' propiamente dicho. Todavia no cambia nada."),
  ("PyTorch bucle",
   "optimizer.step()",
   "Ahora si: mueve cada peso segun su gradiente y el learning rate. "
   "El trio siempre en este orden: zero_grad -&gt; backward -&gt; step."),
  ("PyTorch bucle",
   "model.train()  /  model.eval()",
   "Cambia el MODO de la red. train() activa dropout y batchnorm en modo aprendizaje; eval() los desactiva. "
   "Resuelve: que la evaluacion sea determinista. Trampa: olvidar eval() hace que el mismo test de resultados distintos."),
  ("PyTorch bucle",
   "with torch.no_grad():",
   "Apaga el calculo de gradientes dentro del bloque. Se usa al validar y al testear. "
   "Resuelve: evaluar mas rapido y con menos memoria, ya que ahi no se aprende nada."),
  ("PyTorch bucle",
   'torch.save(model.state_dict(), "modelo.pth")',
   "Guarda solo los pesos aprendidos (no la arquitectura). "
   "Resuelve: no volver a entrenar cada vez. Ojo: los .pth van al .gitignore, pesan decenas de MB."),
  ("Evaluacion",
   "confusion_matrix(y_true, y_pred)",
   "Tabla de lo que ERA contra lo que PREDIJO. La diagonal son los aciertos. "
   "Resuelve: ver QUE confunde con QUE. En OCT te dira si mezcla DME con CNV, que es justo el par dificil."),
  ("Evaluacion",
   "classification_report(y_true, y_pred, target_names=clases)",
   "Da precision, recall (sensibilidad) y F1 POR CADA CLASE. "
   "Resuelve: la metrica que de verdad importa en clinica. El accuracy global esconde que fallas sistematicamente una clase."),
]

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.6; }
.sec { display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #7c2d12; color: #fff; border-radius: 6px; font-size: 13px;
  letter-spacing: 0.6px; font-weight: 700; text-transform: uppercase; }
code.cmd { display: block; background: #0f172a; color: #e2e8f0; padding: 14px 16px;
  border-radius: 8px; font-family: "SF Mono", Menlo, Consolas, monospace;
  font-size: 16px; line-height: 1.5; white-space: pre-wrap; word-break: break-word; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 12px; }
.exp { margin-top: 4px; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model = genanki.Model(
    MODEL_ID, "Basicos ML Comandos",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def build():
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for i, (sec, cmd, exp) in enumerate(CARDS):
        front = (
            f'<div class="sec">{sec}</div>'
            f'<code class="cmd">{cmd}</code>'
            '<div class="prompt">&iquest;Qu&eacute; hace, cu&aacute;ndo se usa y cu&aacute;l es la trampa?</div>'
        )
        back = f'<div class="exp">{exp}</div>'
        # GUID estable por posicion: reimportar tras corregir ACTUALIZA, no duplica.
        guid = genanki.guid_for(f"basdev:mlcmd:{i}")
        deck.add_note(genanki.Note(model=model, fields=[front, back],
                                   tags=["basicos", "dev", "machine_learning", "comandos"],
                                   guid=guid))
    out = os.path.join(os.path.dirname(__file__), "..", "output",
                       "Basicos_MachineLearning_Comandos.apkg")
    genanki.Package(deck).write_to_file(out)
    print(f"OK: Basicos_MachineLearning_Comandos.apkg  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
