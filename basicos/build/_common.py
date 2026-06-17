"""Metadatos compartidos para los decks Basicos (Frontend / Backend / Data).

Replica la metodologia de examen-ecoe-anki/ejes_diagnosticos/topografico_clinico:
cada AREA genera DOS decks con la misma logica que los ejes ECOE:
  - Eje Clinico  (del PROBLEMA al concepto)        -> formato Eje Clinico de gine
  - Integrador   (de las SENALES al concepto + tip) -> formato Integrador de gine

Cada _parts/<slug>.py define: NAME (str), EJES (list), ESTACIONES (list).

Esquema de deck_id: 1500_AA_C
  AA = indice del area (01-03)
  C  = 1 (Eje Clinico) | 2 (Integrador)
Rango valido [1<<30, 1<<31); sin colision con el repo ECOE (12xx/13xx).
"""

MODEL_QA_ID = 1607392321  # qa_basicos (propio de este repo, no colisiona con ECOE)
PADRE = "Basicos Dev"

# (nombre_en_data, nombre_corto_para_deck, slug_archivo, tag, idx)
AREAS = [
    ("Frontend",          "Frontend",  "Frontend",  "frontend",  1),
    ("Backend",           "Backend",   "Backend",   "backend",   2),
    ("Analisis de Datos", "Data",      "Data",      "data",      3),
    ("Flask",             "Flask",     "Flask",     "flask",     4),
]


def deck_id(idx, fmt):
    """fmt: 1 = Eje Clinico, 2 = Integrador."""
    return 1500000000 + idx * 1000 + fmt
