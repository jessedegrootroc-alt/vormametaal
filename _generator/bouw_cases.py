# -*- coding: utf-8 -*-
"""Bouwt cases.html en de drie casepagina's.

   Het overzicht staat op het overzichtssjabloon (patroonhero, inleiding,
   raster, slotblok). Het raster gebruikt de casekaart uit cases.css, het
   casecomponent van de template. Geen filters: bij drie projecten zijn die
   zinloos, en dan hoeft cases.js niet mee.

   De casepagina heeft voor alle drie dezelfde acht delen, in deze volgorde:
   hero met klant, titel, foto en samenvatting; project in het kort (de
   vlakkenrij van de contactpagina); de vraag en onze aanpak naast elkaar;
   het resultaat; de fotogalerij; de andere projecten (hetzelfde kaartraster
   als het overzicht); en het slotblok met de CTA.

   LET OP: klantnamen en projecten zijn PLAATSHOUDERS, zie het kader bij CASES
   in schil.py en de kop van inhoud/cases.py. Elke kaart en pagina draagt
   data-plaatshouder="case"; de audit meldt ze.
"""
import importlib.util
import pathlib
import sys

HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
UIT = HIER.parent
INHOUD = HIER / "inhoud"

from schil import (CASES, pagina, patroonhero, paginahero, vlakkenrij,  # noqa: E402
                   foto, knop, icoonknop, slotblok, klantnaam, plaatshouder_attr,
                   bewerkingen_tekst)


def laad(bestand, naam):
    pad = INHOUD / bestand
    if not pad.exists():
        print(f"   LET OP: inhoud/{bestand} ontbreekt, cases niet geschreven")
        return None
    spec = importlib.util.spec_from_file_location(pad.stem, pad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, naam)


def kaart(i, c, tekst):
    """Eén kaart in het raster, in de markup die cases.css verwacht. Boven de
       titel de klant, onder de tekst de bewerkingen, in de voet de CTA.
       is-even zet cases.js normaal na het filteren; zonder filters staat hij
       hier gewoon in de HTML, om en om."""
    even = " is-even" if i % 2 else ""
    return f'''        <article class="case-kaart{even}"{plaatshouder_attr(c)}>
          <a class="case-kaart__link" href="{c["bestand"]}">
            <figure class="case-kaart__beeld">
              {foto(c["kaart"], maten="(max-width: 767px) 100vw, (max-width: 1199px) 50vw, 33vw", alt="")}
            </figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">
                <span class="case-kaart__label">{klantnaam(c)}</span>
              </div>
              <h3 class="case-kaart__titel">{c["titel"]}</h3>
              <p class="case-kaart__tekst">{tekst}</p>
              <p class="case-kaart__label" style="margin:0; color:var(--color-groen-diep)">{" &middot; ".join(c["bewerkingen"])}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Bekijk project</span>
                {icoonknop("button--icon--54", "button--secundair")}
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


def bouw_case(c, t, cfg, koppen):
    klant = klantnaam(c)
    # De twee andere projecten, in de kaart van het overzicht. Het slot
    # eronder heeft al "Bekijk alle projecten" in de resultaatsectie.
    andere = "\n".join(kaart(i, d, CASE_TEKSTEN[d["slug"]]["kaart"])
                       for i, d in enumerate(d for d in CASES if d["slug"] != c["slug"]))
    stappen = "".join(f"<li><strong>{stap}.</strong> {uitleg}</li>" for stap, uitleg in t["stappen"])
    galerij = "\n".join(f'      <figure>{foto(b, maten="(max-width: 767px) 100vw, 50vw")}</figure>'
                        for b in c["galerij"])
    # De vlakkenrij komt direct na de hero, die geen ruimte onder zich heeft;
    # op de contactpagina staat er een band voor. Vandaar de bovenruimte hier.
    kort = vlakkenrij("02", "kort", koppen["kort"], [
        ("Opdrachtgever", klant),
        ("Sector", c["sector"]),
        ("Materiaal", c["materiaal"]),
        ("Bewerkingen", bewerkingen_tekst(c["bewerkingen"])),
    ]).replace('class="vlakkenband"', 'class="vlakkenband" style="padding-top:var(--space-section-y)"', 1)

    inhoud = f'''{paginahero("01", c["slug"], klant, c["titel"], c["hero"], intro=t["samenvatting"], extra=plaatshouder_attr(c))}

{kort}

  <section class="band background--grey" id="s03-vraag-aanpak">
    <div class="container">
      <div class="row">
        <div class="col-lg-6 col-12">
          <div class="case-blok__inner">
            <h2 class="case-blok__kop">{koppen["vraag"]}</h2>
            <div class="case-blok__body">{t["vraag"]}</div>
          </div>
        </div>
        <div class="col-lg-6 col-12">
          <div class="case-blok__inner">
            <h2 class="case-blok__kop">{koppen["aanpak"]}</h2>
            <div class="case-blok__body"><p>{t["aanpak_intro"]}</p></div>
            <ul class="case-lijst">{stappen}</ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--white" id="s04-resultaat">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="case-blok__kop">{koppen["resultaat"]}</h2>
          <div class="case-blok__body">{t["resultaat"]}</div>
          <p style="margin-top:var(--space-600)">{knop("Bekijk alle projecten", "cases.html", "secundair")}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s05-galerij" aria-labelledby="galerij-kop">
    <div class="container">
      <h2 class="section-heading" id="galerij-kop" style="margin:0 var(--inset-x) var(--space-600)">{koppen["galerij"]}</h2>
      <div class="case-galerij">
{galerij}
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s06-andere" aria-labelledby="andere-kop">
    <div class="container">
      <h2 class="section-heading" id="andere-kop" style="margin:0 var(--inset-x) var(--space-600)">{koppen["andere"]}</h2>
      <div class="cases-overzicht__raster">
{andere}
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
    KOPPEN = laad("cases.py", "KOPPEN")
    if CFG and CASE_TEKSTEN and KOPPEN:
        bouw_overzicht(CFG, CASE_TEKSTEN)
        for c in CASES:
            bouw_case(c, CASE_TEKSTEN[c["slug"]], CFG, KOPPEN)
