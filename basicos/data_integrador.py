# -*- coding: utf-8 -*-
"""Carga INTEGRADOR desde los modulos en _parts/.

Cada _parts/<slug>.py define: NAME (str), EJES (list), ESTACIONES (list).
Aqui solo usamos NAME + ESTACIONES.
"""
import os
import importlib.util

PARTS_DIR = os.path.join(os.path.dirname(__file__), "_parts")

INTEGRADOR = {}
for fn in sorted(os.listdir(PARTS_DIR)):
    if not fn.endswith(".py") or fn.startswith("_"):
        continue
    spec = importlib.util.spec_from_file_location(fn[:-3], os.path.join(PARTS_DIR, fn))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    INTEGRADOR[mod.NAME] = {"estaciones": mod.ESTACIONES}
