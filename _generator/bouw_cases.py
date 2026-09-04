# -*- coding: utf-8 -*-
"""Bouwt cases.html en de drie casepagina's.

   Het overzicht staat op het overzichtssjabloon (patroonhero, inleiding,
   raster, slotblok). Het raster en de casepagina gebruiken de componenten uit
   cases.css: dat is het casecomponent van de template, dat hier ongewijzigd
   wordt hergebruikt. Geen filters: bij drie projecten zijn die zinloos, en dan
   hoeft cases.js niet mee.

   LET OP: het zijn VOORBEELDPROJECTEN, zie het kader bij CASES in schil.py en
   de kop van inhoud/cases.py. Elke pagina draagt het label; de audit meldt ze.
"""
import importlib.util
import pathlib
import sys

HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
UIT = HIER.parent
INHOUD = HIER / "inhoud"

from schil import (CASES, VOORBEELD_LABEL, pagina, patroonhero, paginahero,  # noqa: E402
                   foto, knop, slotblok)


def laad(bestand, naam):
    pad = INHOUD / bestand
    if not pad.exists():
        print(f"   LET OP: inhoud/{bestand} ontbreekt, cases niet geschreven")
        return None
    spec = importlib.util.spec_from_file_location(pad.stem, pad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, naam)


def label(c):
    return VOORBEELD_LABEL if c.get("voorbeeld") else c["sector"]


def kaart(i, c, tekst):
    """Eén kaart in het raster, precies de markup die cases.css verwacht.
       is-even zet cases.js normaal na het filteren; zonder filters staat hij
       hier gewoon in de HTML, om en om."""
    even = " is-even" if i % 2 else ""
    return f'''        <article class="case-kaart{even}">
          <a class="case-kaart__link" href="{c["bestand"]}">
            <figure class="case-kaart__beeld">
              {foto(c["kaart"], maten="(max-width: 767px) 100vw, (max-width: 1199px) 50vw, 33vw", alt="")}
            </figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">
                <span class="case-kaart__label">{c["kort"]}</span>
                <span class="case-kaart__label">{label(c)}</span>
              </div>
              <h3 class="case-kaart__titel">{c["titel"]}</h3>
              <p class="case-kaart__tekst">{tekst}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Bekijk het project</span>
              </div>
            </div>
          </a>
        </article>'''


def bouw_overzicht(cfg, teksten):
    kaarten = "\n".join(kaart(i, c, teksten[c["slug"]]["kaart"]) for i, c in enumerate(CASES))
    inhoud = f'''{patroonhero("01", "cases", cfg["hero_label"], cfg["hero_titel"])}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{cfg["intro_kop"]}</h2>
          <div class="article-body content-fit--half">
{cfg["intro_tekst"]}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s03-projecten" aria-labelledby="projecten-kop">
    <div class="container">
      <h2 class="section-heading" id="projecten-kop" style="margin:0 var(--inset-x) var(--space-600)">{cfg["raster_kop"]}</h2>
      <div class="cases-overzicht__raster" id="caseRaster">
{kaarten}
      </div>
    </div>
  </section>

{slotblok("04", cfg["contact_kop"], cfg["contact_tekst"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css="cases.css", css_naam="cases",
        inhoud=inhoud,
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


def bouw_case(c, t, cfg):
    andere = [d for d in CASES if d["slug"] != c["slug"]]
    andere_html = "\n".join(kaart(i, d, CASE_TEKSTEN[d["slug"]]["kaart"]) for i, d in enumerate(andere))
    bewerkingen = "".join(f"<li>{b}</li>" for b in c["bewerkingen"])
    inhoud = f'''{paginahero("01", c["slug"], label(c), c["titel"], c["hero"])}

  <section class="band background--white" id="s02-inleiding">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <p class="case-lead">{t["lead"]}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--grey" id="s03-opdracht">
    <div class="container">
      <div class="row">
        <div class="col-lg-6 col-12">
          <div class="case-blok__inner">
            <h2 class="case-blok__kop">{t["opdracht_kop"]}</h2>
            <div class="case-blok__body">{t["opdracht"]}</div>
          </div>
        </div>
        <div class="col-lg-6 col-12">
          <div class="case-blok__inner">
            <h2 class="case-blok__kop">{t["aanpak_kop"]}</h2>
            <div class="case-blok__body">{t["aanpak"]}</div>
            <h3 class="case-blok__kop" style="margin-top:var(--space-700); font-size:1.25rem">Bewerkingen in dit project</h3>
            <ul class="case-lijst">{bewerkingen}</ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <figure class="case-bleed" id="s04-beeld">
    {foto(c["tweede"], maten="100vw")}
  </figure>

  <section class="band background--white" id="s05-materiaal">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="case-blok__kop">{t["materiaal_kop"]}</h2>
          <p class="case-blok__body">{t["materiaal"]}</p>
          <p style="margin-top:var(--space-600)">{knop("Alle projecten", "cases.html", "secundair")}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s06-andere" aria-labelledby="andere-kop">
    <div class="container">
      <h2 class="section-heading" id="andere-kop" style="margin:0 var(--inset-x) var(--space-600)">Andere projecten</h2>
      <div class="cases-overzicht__raster">
{andere_html}
      </div>
    </div>
  </section>

{slotblok("07", cfg["contact_kop"], cfg["contact_tekst"])}
'''
    (UIT / c["bestand"]).write_text(pagina(
        bestand=c["bestand"], titel=f'{c["titel"]} | Vorma Metaal',
        omschrijving=t["kaart"], namespace=f'case-{c["slug"]}',
        pagina_css="cases.css", css_naam="cases", inhoud=inhoud,
    ), encoding="utf-8")
    print(f'{c["bestand"]} geschreven')


if __name__ == "__main__":
    CFG = laad("cases.py", "CASES_PAGINA")
    CASE_TEKSTEN = laad("cases.py", "CASE_TEKSTEN")
    if CFG and CASE_TEKSTEN:
        bouw_overzicht(CFG, CASE_TEKSTEN)
        for c in CASES:
            bouw_case(c, CASE_TEKSTEN[c["slug"]], CFG)
