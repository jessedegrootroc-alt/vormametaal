# -*- coding: utf-8 -*-
"""diensten, werkwijze, materialen, voor-wie en over-vorma-metaal.

   Alle vijf op het BESTAANDE MADEGRO-overzichtssjabloon dat hier voor
   cursusaanbod.html stond: patroonhero, een introband, een rij panelen in
   panel-row--4, een FAQ en het slotblok. Dezelfde secties, dezelfde ids,
   dezelfde spacing; alleen de inhoud verschilt.

   over-vorma-metaal.html houdt het eigen over-ons-sjabloon.

   De teksten staan in inhoud/; dit bestand bepaalt alleen de opbouw."""
import sys, pathlib, importlib.util
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from bouw_service import stappen as trapstappen

UIT = pathlib.Path(__file__).resolve().parent.parent
INHOUD = pathlib.Path(__file__).resolve().parent / "inhoud"


def laad(bestand, naam):
    pad = INHOUD / bestand
    if not pad.exists():
        print(f"   LET OP: inhoud/{bestand} ontbreekt, pagina overgeslagen")
        return None
    spec = importlib.util.spec_from_file_location(pad.stem, pad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, naam)


def overzicht(cfg, ident, kaarten_html, eyebrow, kaarten_kop, css="overzicht.css", css_naam="overzicht"):
    """Het overzichtssjabloon, ongewijzigd overgenomen van cursusaanbod.html."""
    inhoud = f'''{patroonhero("01", ident, cfg["hero_label"], cfg["hero_titel"])}

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

  <section class="content-block" id="s03-{ident}">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{eyebrow}</span>
            <h2 class="section-heading">{kaarten_kop}</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{kaarten_html}
      </div>
    </div>
  </section>

{faq_blok("04", cfg["faq"])}

{slotblok("05", cfg["contact_kop"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css=css, css_naam=css_naam,
        inhoud=inhoud, extra_ld=faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


# ======================================================== diensten.html
def bouw_diensten():
    """De acht bewerkingen als kaarten. Dit is de plek van cursusaanbod.html en
       gebruikt dezelfde cursuskaart(): paneel, foto erboven, meta, titel,
       tekst en pijlknop. Acht kaarten in panel-row--4 vullen twee rijen."""
    cfg = laad("diensten_overzicht.py", "DIENSTEN_OVERZICHT")
    if not cfg:
        return
    kaarten = "\n".join(dienstpaneel(i, d) for i, d in enumerate(SERVICES))
    overzicht(cfg, "diensten", kaarten, cfg["kaarten_eyebrow"], cfg["kaarten_kop"])


def dienstpaneel(i, dienst):
    """Zelfde markup als cursuskaart() in de MADEGRO-template: paneel met de
       foto erboven, een metaregel, de titel, een regel tekst en de pijlknop.
       De metaregel droeg de doelgroep van een cursus en draagt nu het
       dienstnummer."""
    bestand, naam, onder, beeld = dienst
    return f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_4, alt="")}
            </figure>
            <span class="panel__meta">Dienst {i + 1:02d}</span>
            <h3 class="panel__title">{naam}</h3>
            <p class="panel__body">{onder}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''


# ======================================================== werkwijze.html
def bouw_werkwijze():
    """Zelfde overzichtssjabloon, maar met de trap uit het dienstsjabloon in
       plaats van een kaartenrij: de vijf stappen lenen zich daar beter voor en
       de trap is een bestaand MADEGRO-component."""
    cfg = laad("werkwijze.py", "WERKWIJZE")
    if not cfg:
        return
    formaten = "".join(f'<li class="check-lijst__item">{f}</li>' for f in FORMATEN)
    inhoud = f'''{patroonhero("01", "werkwijze", cfg["hero_label"], cfg["hero_titel"])}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{cfg["stappen_kop"]}</h2>
          <div class="article-body content-fit--half">
{cfg["intro"]}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--grey" id="s03-stappen">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Vijf stappen</span>
          <h2 class="section-heading">Zo loopt uw opdracht</h2>
          <p class="article-body" style="margin-top:var(--space-500)">{cfg["stappen_intro"]}</p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{trapstappen(cfg["stappen"])}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--white" id="s04-offerte">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">{cfg["formaten_kop"]}</span>
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{cfg["offerte_kop"]}</h2>
          <div class="article-body content-fit--half">
            <p>{cfg["formaten_intro"]}</p>
            <p>{cfg["offerte_tekst"]}</p>
          </div>
          <ul class="check-lijst" role="list">{formaten}</ul>
        </div>
      </div>
    </div>
  </section>

{faq_blok("05", cfg["faq"])}

{slotblok("06", cfg["contact_kop"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css="overzicht.css", css_naam="overzicht",
        inhoud=inhoud, extra_ld=faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


# ======================================================== materialen.html
def bouw_materialen():
    cfg = laad("materialen.py", "MATERIALEN_PAGINA")
    if not cfg:
        return

    # Elk materiaal een eigen blok over de volle breedte, met de foto ernaast
    # en een id om naartoe te linken. Dit was een rij van drie smalle panelen
    # zonder beeld; de drie materiaalrijen op de homepage wezen alle drie naar
    # de kale pagina, dus je kwam nergens uit.
    #
    # Zelfde component als die rijen op de homepage (cases-grid__row), maar als
    # div en niet als link: dit IS de bestemming. De klasse doet het op een div,
    # de twee regels die eruit vallen zijn de linkresets.
    blokken = []
    for i, m in enumerate(cfg["materialen"]):
        slug = materiaal_slug(m["naam"])
        lijst = "".join(f'<li class="check-lijst__item">{k}</li>' for k in m["kwaliteiten"])
        grijs = "grey" if i % 2 == 0 else "white"
        blokken.append(f'''      <div class="cases-grid__row cases-grid__row--{grijs}" id="{slug}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">Materiaal {m["nr"]}</span>
            <span class="cases-grid__meta-item">{m["eigenschap"]}</span>
          </div>
          <h3 class="cases-grid__title">{m["naam"]}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{m["tekst"]}</p>
          </div>
          <ul class="check-lijst" role="list">{lijst}</ul>
        </div>
        <figure class="cases-grid__image">
          {foto(slug, maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </div>''')

    inhoud = f'''{patroonhero("01", "materialen", cfg["hero_label"], cfg["hero_titel"])}

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

  <section class="cases-grid" id="s03-materialen">
    <div class="container">
      <div class="cases-grid__header">
        <span class="subtitle">Drie materialen</span>
        <h2 class="cases-grid__heading">Staal, RVS en aluminium</h2>
      </div>
      <!-- De kwaliteiten zijn voorbeelden, geen voorraadlijst. Zie schil.MATERIALEN. -->
{chr(10).join(blokken)}
    </div>
  </section>

{vlakkenrij("04", "wanneer", "Wanneer welk materiaal", cfg["vlakken"])}

{faq_blok("05", cfg["faq"])}

{slotblok("06", cfg["contact_kop"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css="overzicht.css", css_naam="overzicht",
        inhoud=inhoud, extra_ld=faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


# ======================================================== voor-wie.html
def bouw_voor_wie():
    cfg = laad("voor_wie.py", "VOOR_WIE")
    if not cfg:
        return
    kaarten = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 else 'wit'}">
            <span class="panel__meta">{i + 1:02d}</span>
            <h3 class="panel__title">{naam}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (naam, tekst) in enumerate(cfg["sectoren"]))
    inhoud = f'''{patroonhero("01", "voor-wie", cfg["hero_label"], cfg["hero_titel"])}

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

  <section class="content-block" id="s03-voor-wie">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Tien sectoren</span>
            <h2 class="section-heading">{cfg["series_kop"]}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{cfg["series_tekst"]}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{kaarten}
      </div>
    </div>
  </section>

{faq_blok("04", cfg["faq"])}

{slotblok("05", cfg["contact_kop"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css="overzicht.css", css_naam="overzicht",
        inhoud=inhoud, extra_ld=faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


# ================================================ over-vorma-metaal.html
def bouw_over_ons():
    """Houdt het eigen over-ons-sjabloon. De medewerkersband met portret die
       hier stond is een tekstblok geworden: van Vorma Metaal is geen
       medewerkersfoto beschikbaar en die verzinnen kan niet."""
    cfg = laad("over_ons.py", "OVER_ONS")
    if not cfg:
        return
    waarden = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 else 'wit'}">
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(cfg["waarden"]))
    inhoud = f'''{patroonhero("01", "over-vorma-metaal", cfg["hero_label"], cfg["hero_titel"])}

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

  <section class="content-block" id="s03-waarden">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Waar wij voor staan</span>
            <h2 class="section-heading">{cfg["waarden_kop"]}</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{waarden}
      </div>
    </div>
  </section>

  <section class="band background--grey" id="s04-zusterbedrijf">
    <div class="container">
      <div class="row">
        <div class="col-lg-7 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Zusterbedrijf</span>
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{cfg["zuster_kop"]}</h2>
          <div class="article-body">
{cfg["zuster_tekst"]}
          </div>
        </div>
        <div class="col-lg-5 col-12">
          <figure class="box--image" style="margin-top:var(--space-600)">
            {foto("productiehal", maten="(max-width: 991px) 100vw, 40vw")}
          </figure>
        </div>
      </div>
    </div>
  </section>

{vlakkenrij("05", "gegevens", "Waar u ons vindt", [
    ("Adres", f"{ADRES_STRAAT}<br>{ADRES_POSTCODE} {ADRES_PLAATS}"),
    ("Telefoon", f'<a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a>'),
    ("E-mail", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
    ("Openingstijden", "<br>".join(f"{d}: {t}" for d, t in OPENINGSTIJDEN)),
])}

{faq_blok("06", cfg["faq"])}

{slotblok("07", cfg["contact_kop"])}
'''
    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"], titel=cfg["titel"], omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"], pagina_css="over-ons.css", css_naam="over-ons",
        inhoud=inhoud, extra_ld=faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(f'{cfg["bestand"]} geschreven')


if __name__ == "__main__":
    bouw_diensten()
    bouw_werkwijze()
    bouw_materialen()
    bouw_voor_wie()
    bouw_over_ons()
