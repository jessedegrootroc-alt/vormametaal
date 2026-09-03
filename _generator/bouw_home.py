# -*- coding: utf-8 -*-
"""index.html.

   Dezelfde twaalf secties als de MADEGRO-homepage, in dezelfde volgorde, met
   dezelfde ids, klassen en spacing. Alleen de inhoud is van Vorma Metaal.

   Vier secties dragen andere inhoud omdat Vorma niet heeft wat MADEGRO er had.
   Ze zijn hergebruikt in plaats van verwijderd; welke en waarom staat in
   inhoud/MAPPING.md:

     s05  cases-rijen        -> de drie materialen
     s06  drie cijfers       -> 22 jaar, 8 bewerkingen, 3 materialen
     s07  cursuskaarten      -> de zes redenen om voor Vorma te kiezen
     s08  klantcitaten       -> drie procesafspraken, op naam van Vorma zelf
     s10  portret + biografie-> de herkomst uit Tentije
     s11  logoband           -> de tien sectoren als tekstband

   De teksten staan in inhoud/home.py."""
import sys, pathlib, importlib.util
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

UIT = pathlib.Path(__file__).resolve().parent.parent
INHOUD = pathlib.Path(__file__).resolve().parent / "inhoud"

pad = INHOUD / "home.py"
if not pad.exists():
    print("   LET OP: inhoud/home.py ontbreekt, index.html niet geschreven")
    sys.exit(0)
spec = importlib.util.spec_from_file_location("home", pad)
_m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_m)
cfg = _m.HOME

# De leadalinea van de dienstensectie. Levert inhoud/home.py hem niet, dan
# bouwen we hem uit SERVICES: dat is de opsomming zelf en die is per definitie
# feitelijk en concreet.
if not cfg.get("diensten_tekst"):
    namen = [t for _b, t, _o, _f in SERVICES]
    cfg["diensten_tekst"] = (", ".join(namen[:-1]) + " en " + namen[-1]
                             + ". Alle acht in eigen beheer aangestuurd, zodat "
                               "uw onderdeel niet tussen leveranciers heen en "
                               "weer gaat.")

# ---- s04: de acht diensten in de bestaande dienstkaart -------------------
diensten = "\n".join(dienstkaart(i, d, intro)
                     for i, (d, intro) in enumerate(zip(SERVICES, cfg["diensten_intros"])))

# ---- s05: was cases-rijen, draagt nu de materialen -----------------------
# Zelfde rij: beeld rechts, meta, kop, tekst en de pijlknop. De metaregels
# droegen branche en plaats van een case en dragen nu het rijnummer en het
# woord "materiaal".
# Elk materiaal zijn eigen foto, aangeleverd door Jesse. Hier stonden beeldjes
# uit de herofilm (de laser, de kantbank, de freeskop); die staan al bij de
# bewerkingen, en dan zag je op de homepage twee keer hetzelfde.
_MAT_BEELD = ["staal", "rvs", "aluminium"]
materiaalrijen = "\n".join(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="materialen.html" aria-label="{m["naam"]}: voorbeeldkwaliteiten">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">Materiaal {i + 1:02d}</span>
            <span class="cases-grid__meta-item">{" &middot; ".join(m["kwaliteiten"][:2])}</span>
          </div>
          <h3 class="cases-grid__title">{m["naam"]}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{m["tekst"]}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(_MAT_BEELD[i % 3], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''' for i, m in enumerate(cfg["materialen"]))

# ---- s06: de drie cijfers, met de tellers uit index.js -------------------
usps = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <p class="usp__getal" data-telop="{getal}">{getal}</p>
            <p class="usp__label">{label}</p>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (getal, label, tekst) in enumerate(cfg["usps"]))

# ---- s07: was cursuskaarten, draagt nu de zes redenen -------------------
# Zelfde paneel als cursuskaart(), met de foto erboven en een metaregel. Zes
# items in panel-row--4 vullen anderhalve rij; het grid vangt dat op.
# Zes verschillende beelden, elk een bewerking of de werkplaats. Hier stonden
# een containerschip en een torenkraan bij.
_WAAROM_BEELD = ["werkplaats", "kanten", "lasersnijden",
                 "buislasersnijden", "productiehal", "verspanen"]
waarom = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld">
            <figure class="panel__beeld">
              {foto(_WAAROM_BEELD[i % 6], maten=BEELD_MATEN_4, alt="")}
            </figure>
            <span class="panel__meta">{i + 1:02d}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(cfg["waarom"]))

# ---- s08: was klantcitaten, draagt nu uitspraken van Vorma zelf ---------
# Vijfde veld is False en niet None: dat laat het logoslot helemaal weg, in
# plaats van er een invulveld "Logo opdrachtgever" te zetten. Dit zijn geen
# klantcitaten, dus er hoort geen klantlogo bij te komen.
verwachten = [(tekst, wie, wat, beeld, False) for tekst, wie, wat, beeld in cfg["verwachten"]]

# ---- s11: de logoband -----------------------------------------------------
# Draagt op verzoek weer de beeldmerken uit de template. PLAATSHOUDER, mag niet
# live; zie het kader boven OPDRACHTGEVERS in schil.py.
#
# De aantoonbaar ware variant staat klaar: sectorenband("11",
# cfg["sectoren_label"]) zet de tien sectoren in dezelfde band, met dezelfde
# animatie en hetzelfde dubbele spoor. Beide functies staan in schil.py.


# De herofilm. De film uit de template was een vrachtwagen op een dijkweg en
# zei niets over metaalbewerking; deze laat vijf van de acht bewerkingen zien,
# in deze volgorde: lasersnijden, buislasersnijden, kanten, lassen en
# CNC-verspanen, met een haloverzicht als slot.
#
# site.js hangt de bron pas in als hij die mag ophalen, en tot dat moment staat
# het stilstaande beeld er: het eerste beeldje van dezelfde film.
#
# NOG TE DOEN: het is nog steeds stockbeeld en niet de werkplaats aan Dammaten
# 14. Zie assets/video/HERKOMST.md voor wat er over de herkomst bekend is.
inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="hero" id="s01-introductie" data-header-theme="light">
    <div class="hero--beeld" aria-hidden="true">
      {foto("werkplaats", laden="eager", maten="100vw")}
      <!-- site.js hangt de bron hierin; zie de toelichting daar voor de vier
           gevallen waarin dat niet gebeurt. Dan blijft de foto staan. -->
      <video class="hero--video" width="1130" height="720" muted loop playsinline preload="none"
             data-herovideo="assets/video/hero-werkplaats.mp4"></video>
      <span class="hero--sluier"></span>
    </div>
    <div class="container hero--container">
      <div class="hero--content">
        <span class="subtitle" style="color:var(--color-white)">{cfg["hero_eyebrow"]}</span>
        <h1 class="hero--title">{cfg["hero_h1"]}</h1>
        <div class="hero--intro article-body">
{cfg["hero_intro"]}
        </div>
        <div class="hero--actions">
          {knop(cfg["hero_knop1"], "contact.html")}
          {knop(cfg["hero_knop2"], "diensten.html", "secondary")}
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 02 WAT VORMA METAAL DOET ================= -->
  <section class="content-text-side-cta" id="s02-wat-we-doen">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
              <p>{cfg["wat_tekst"]}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-text-side-visual background--white" id="s03-hoe-we-werken">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>{cfg["werkwijze_kop"]}</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
{cfg["werkwijze_intro"]}
            </div>
            {knop("Zo werkt een aanvraag", "werkwijze.html")}
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual added-distance">
      {foto("productiehal", maten="(max-width: 991px) calc(100vw - 32px), (max-width: 1199px) calc(100vw - 96px), (max-width: 1352px) 940px, 70vw")}
    </div>
  </section>

  <!-- ================= 04 DE ACHT DIENSTEN ================= -->
  <section class="content-block" id="s04-diensten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{cfg["diensten_eyebrow"]}</span>
            <h2 class="section-heading">{cfg["diensten_kop"]}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              {cfg["diensten_tekst"]}
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{diensten}
      </div>
    </div>
  </section>

  <!-- ================= 05 MATERIALEN ================= -->
  <section class="cases-grid" id="s05-materialen">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">{cfg["materialen_kop"]}</h2>
        {knop("Bekijk de materialen", "materialen.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{materiaalrijen}
      </div>
    </div>
  </section>

  <!-- ================= 06 IN CIJFERS ================= -->
  <section class="content-block" id="s06-usps">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">In cijfers</span>
            <h2 class="section-heading">{cfg["usps_kop"]}</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{usps}
      </div>
    </div>
  </section>

  <!-- ================= 07 WAAROM VORMA METAAL ================= -->
  <section class="content-block" id="s07-waarom">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{cfg["waarom_eyebrow"]}</span>
            <h2 class="section-heading">{cfg["waarom_kop"]}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              {cfg["waarom_intro"]}
            </p>
          </div>
          <div class="col-md-4 col-12 text-md-end">
            {knop("Bekijk alle bewerkingen", "diensten.html")}
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{waarom}
      </div>
    </div>
  </section>

{quoteslider("08", "verwachten", cfg["verwachten_eyebrow"], cfg["verwachten_kop"], verwachten)}

{faq_blok("09", cfg["faq"], cfg["faq_kop"])}

  <!-- ================= 10 WAAR VORMA VANDAAN KOMT ================= -->
  <!-- Was het portret met de biografie van Martin de Groot. Van Vorma Metaal
       is geen medewerkersfoto beschikbaar en die verzinnen kan niet; het
       beeldslot houdt zijn plek en verhouding en krijgt een werkplaatsfoto. -->
  <section class="streamer streamer--employee streamer--employee--portret background--groen" id="s10-herkomst">
    <div class="container">
      <div class="streamer--employee-row">
        <figure class="streamer--employee-portrait">
          {foto("productiehal", maten="(max-width: 991px) 100vw, 40vw")}
        </figure>
        <div class="streamer--employee-panel band">
          <span class="subtitle" style="color:var(--color-white)">{cfg["over_eyebrow"]}</span>
          <h2 class="streamer--employee-name">{cfg["over_kop"]}</h2>
          <div class="article-body content-fit--half">
{cfg["over_tekst"]}
          </div>
          <div>
            {knop(cfg["over_knop"], "over-vorma-metaal.html")}
          </div>
        </div>
      </div>
    </div>
  </section>

{logoslider("11")}

{ctablok("12", cfg["contact_kop"], cfg["contact_tekst"])}
'''

(UIT / "index.html").write_text(pagina(
    bestand="index.html",
    titel=cfg["titel"],
    omschrijving=cfg["omschrijving"],
    namespace="home",
    pagina_css="index.css",
    css_naam="index",
    inhoud=inhoud,
    scripts=["index.js"],
    extra_ld=faq_ld(cfg["faq"]),
), encoding="utf-8")
print("index.html geschreven")
