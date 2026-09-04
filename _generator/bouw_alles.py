# -*- coding: utf-8 -*-
"""Bouwt alle pagina's. Gebruik dit en niet de losse scripts.

   De teksten komen uit _generator/inhoud/; dit script kent alleen de volgorde.
   Ontbreekt er een inhoudsbestand, dan slaat het bijbehorende script die ene
   pagina over en gaat de rest gewoon door."""
import runpy, sys, pathlib
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

for naam in ["bouw_home", "bouw_service", "bouw_rest", "bouw_cases", "bouw_contact",
             "bouw_zoekmachine"]:
    print(f"--- {naam}")
    runpy.run_path(str(HIER / f"{naam}.py"), run_name="__main__")
