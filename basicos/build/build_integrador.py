"""Builder de los decks INTEGRADOR (de las SENALES al concepto) - formato Integrador de gine.

Front: un cluster tematico + 3 senales/caracteristicas concretas.
Back:  el concepto + un tip verbalizable (el porque profundo / la analogia).
Lee data_integrador.INTEGRADOR y emite un .apkg por area presente.
"""
import os
import sys
import genanki

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _common import MODEL_QA_ID, PADRE, AREAS, deck_id
from data_integrador import INTEGRADOR

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.loc { display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #1e3a8a; color: #fff; border-radius: 6px; font-size: 14px;
  letter-spacing: 0.5px; font-weight: 600; }
ul.disc { margin: 8px 0 18px 0; padding-left: 22px; }
ul.disc li { margin: 6px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 10px; }
.dx { font-size: 22px; font-weight: 700; color: #047857; margin-top: 4px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 12px; display: block; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Basicos Dev QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def make_note(loc, d1, d2, d3, dx, tip, base_tags, guid):
    front = (
        f'<div class="loc">{loc}</div>'
        f'<ul class="disc"><li>{d1}</li><li>{d2}</li><li>{d3}</li></ul>'
        '<div class="prompt">&iquest;Qu&eacute; concepto es?</div>'
    )
    back = f'<div class="dx">{dx}</div><span class="ecoe">Dilo as&iacute;: &laquo;{tip}&raquo;</span>'
    # GUID estable por posicion (no por contenido): reimportar tras corregir
    # texto ACTUALIZA la carta en su sitio, nunca duplica.
    return genanki.Note(model=model_qa, fields=[front, back], tags=base_tags, guid=guid)


def build():
    total = 0
    for data_name, short, slug, tag, idx in AREAS:
        sysdata = INTEGRADOR.get(data_name)
        if not sysdata:
            continue
        deck = genanki.Deck(deck_id(idx, 2), f"{PADRE}::{short}::Integrador")
        base_tags = ["basicos", "dev", "integrador", tag]
        for si, (loc, rows) in enumerate(sysdata["estaciones"]):
            for ri, (d1, d2, d3, dx, tip) in enumerate(rows):
                guid = genanki.guid_for(f"basdev:int:{idx}:{si}:{ri}")
                deck.add_note(make_note(loc, d1, d2, d3, dx, tip, base_tags, guid))
        out = os.path.join(OUTPUT_DIR, f"Basicos_{slug}_Integrador.apkg")
        genanki.Package(deck).write_to_file(out)
        print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")
        total += 1
    print(f"--- {total} decks Integrador generados ---")


if __name__ == "__main__":
    build()
