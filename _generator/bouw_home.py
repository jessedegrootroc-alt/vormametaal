# -*- coding: utf-8 -*-
"""index.html.

   De dertien secties van de homepage, in de volgorde die op 4 september 2026
   is gevraagd. Het zijn dezelfde componenten als voorheen (twaalf uit de
   template plus de projectensectie), alleen verplaatst; layout, klassen en
   spacing zijn ongewijzigd. De ids lopen in de nieuwe volgorde door.

     s01 hero            s08 cijfers (drie tellers)
     s02 logoband        s09 offerte (het statementblok, was "wat we doen")
     s03 proces          s10 team (portret + tekst)
     s04 bewerkingen     s11 testimonials (quoteslider, PLAATSHOUDERS)
     s05 waarom Vorma    s12 faq
     s06 materialen      s13 contact
     s07 projecten (PLAATSHOUDERS)

   Twee ids staan elders: #s05-waarom in styleguide.css (tabletregel) en
   #s06-materialen in bouw_service.py (de link uit de materiaalpanelen).
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

# ---- s06: de materialen, compact ------------------------------------------
# Hier stonden drie rijen over de volle breedte die alle drie naar
# materialen.html wezen. Die pagina is er niet meer, en drie rijen voor drie
# regels feiten was te veel. Nu drie panelen naast elkaar, met dezelfde opbouw
# als de zes redenen: beeld, nummer, naam, tekst, en de voorbeeldkwaliteiten
# als lijst. Alles wat er over de materialen te zeggen is, staat hier.
_MAT_BEELD = ["staal", "rvs", "aluminium"]
materiaalkaarten = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld" id="{materiaal_slug(m["naam"])}">
            <figure class="panel__beeld">
              {foto(_MAT_BEELD[i % 3], maten="(max-width: 767px) 100vw, (max-width: 991px) 50vw, 33vw", alt="")}
            </figure>
            <span class="panel__meta">Materiaal {i + 1:02d}</span>
            <h3 class="panel__title">{m["naam"]}</h3>
            <p class="panel__body">{m["tekst"]}</p>
            <span class="panel__meta" style="margin-top:var(--space-400)">{cfg["materialen_lijstlabel"]}</span>
            <ul class="check-lijst" style="margin-top:calc(var(--space-300) * -1)">
{"".join(f'              <li class="check-lijst__item">{k}</li>' + chr(10) for k in m["kwaliteiten"])}            </ul>
          </div>
        </div>''' for i, m in enumerate(cfg["materialen"]))

# ---- s07: drie uitgelichte projecten -------------------------------------
# Nieuw, direct onder de materialen. Zelfde paneel als de zes redenen en de
# cursuskaarten van de template (panel--beeld panel--link): foto, klant als
# metaregel, titel, de bewerkingen als tweede metaregel, korte tekst en de
# icoonknop. De hele kaart is de link.
#
# PLAATSHOUDERS: de klantnamen komen uit de logoband en zijn niet bevestigd;
# zie het kader bij CASES in schil.py. Elke kaart draagt data-plaatshouder.
pad_cases = INHOUD / "cases.py"
spec_c = importlib.util.spec_from_file_location("cases_inhoud", pad_cases)
_c = importlib.util.module_from_spec(spec_c)
spec_c.loader.exec_module(_c)
CASE_TEKSTEN = _c.CASE_TEKSTEN

projecten = "\n".join(f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{c["bestand"]}"{plaatshouder_attr(c)}>
            <figure class="panel__beeld">
              {foto(c["kaart"], maten="(max-width: 767px) 100vw, (max-width: 991px) 50vw, 33vw", alt="")}
            </figure>
            <span class="panel__meta">{klantnaam(c)}</span>
            <h3 class="panel__title">{c["titel"]}</h3>
            <span class="panel__meta" style="color:var(--color-groen-diep)">{" &middot; ".join(c["bewerkingen"])}</span>
            <p class="panel__body">{CASE_TEKSTEN[c["slug"]]["kaart"]}</p>
            <span class="panel__actie" style="display:flex; align-items:center; justify-content:space-between; gap:var(--space-400); width:100%">
              <span class="panel__meta">Bekijk project</span>
              {icoonknop()}
            </span>
          </a>
        </div>''' for i, c in enumerate(CASES))

# ---- s08: de drie cijfers, met de tellers uit index.js -------------------
usps = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <p class="usp__getal" data-telop="{getal}">{getal}</p>
            <p class="usp__label">{label}</p>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (getal, label, tekst) in enumerate(cfg["usps"]))

# ---- s05: was cursuskaarten, draagt nu de zes redenen -------------------
# Zelfde paneel als cursuskaart(), met de foto erboven en een metaregel.
#
# Drie per rij en niet vier: zes items vullen dan twee volle rijen. In
# panel-row--4 stond er een rij van vier met daaronder een rij van twee, en de
# twee lege plekken rechts lieten de sectie onafgemaakt lijken.
# Zes verschillende beelden, elk een bewerking of de werkplaats. Hier stonden
# een containerschip en een torenkraan bij.
# Het vak is nu een derde van de pagina breed en niet een kwart, dus vraagt
# de browser een groter bestand op. Met de oude maat van 25vw kwam er een
# te klein beeld in een vak dat de helft breder is.
BEELD_MATEN_WAAROM = "(max-width: 767px) 100vw, (max-width: 991px) 50vw, 33vw"
# Zes aangeleverde beelden, in de nummering waarin ze zijn aangeleverd: 01.png
# hoort bij kaart 01. Hier stonden beeldjes uit de herofilm; die staan al bij
# de bewerkingen en de materialen.
#
# Elk beeld sluit aan op zijn reden: de rekenmachine bij de vaste calculatie,
# de telefoon bij het op de hoogte blijven, de laptop bij het online
# aanvragen, en de rij gekante delen bij een stuk of een serie.
_WAAROM_BEELD = ["handdruk", "uitleg", "laptop",
                 "calculator", "telefoon", "plaatdelen"]
waarom = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld">
            <figure class="panel__beeld">
              {foto(_WAAROM_BEELD[i % 6], maten=BEELD_MATEN_WAAROM, alt="")}
            </figure>
            <span class="panel__meta">{i + 1:02d}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(cfg["waarom"]))

# ---- s11: klantcitaten, zoals het component in de template stond --------
# PLAATSHOUDERS: er zijn nog geen echte testimonials. De citaten zijn op
# verzoek fictief, met de bedrijven en logo's uit de logoband, en dragen
# data-plaatshouder="testimonial"; de audit telt ze. Zie inhoud/home.py.
testimonials = [(tekst, naam, functie, beeld, logo)
                for tekst, naam, functie, beeld, logo in cfg["testimonials"]]

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
inhoud = f'''  <!-- ================= 01 HERO ================= -->
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

  <!-- ================= 02 LOGOBAND ================= -->
  <!-- Hoog op de pagina, direct na de hero. PLAATSHOUDER, mag niet live; zie
       het kader boven OPDRACHTGEVERS in schil.py. De band heeft geen
       tekstslot. De aantoonbaar ware variant: sectorenband("02",
       cfg["sectoren_label"]). -->
{logoslider("02")}

  <!-- ================= 03 PROCES ================= -->
  <section class="content-text-side-visual background--white" id="s03-hoe-we-werken">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>{cfg["werkwijze_kop"]}</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
{cfg["werkwijze_intro"]}
            </div>
            {knop(cfg["werkwijze_knop"], "werkwijze.html")}
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual added-distance">
      {foto("productiehal", maten="(max-width: 991px) calc(100vw - 32px), (max-width: 1199px) calc(100vw - 96px), (max-width: 1352px) 940px, 70vw")}
    </div>
  </section>

  <!-- ================= 04 BEWERKINGEN ================= -->
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

  <!-- ================= 05 WAAROM VORMA METAAL ================= -->
  <!-- Het id staat in styleguide.css (tabletregel voor twee per rij). -->
  <section class="content-block" id="s05-waarom">
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
            {knop(cfg["waarom_knop"], "contact.html")}
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{waarom}
      </div>
    </div>
  </section>

  <!-- ================= 06 MATERIALEN ================= -->
  <!-- Het id is het doel van de link in de materiaalpanelen op de
       dienstpagina's (bouw_service.py). -->
  <section class="content-block" id="s06-materialen">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Materialen</span>
            <h2 class="section-heading">{cfg["materialen_kop"]}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{cfg["materialen_intro"]}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{materiaalkaarten}
      </div>
    </div>
  </section>

  <!-- ================= 07 PROJECTEN ================= -->
  <!-- Direct onder de materialen: "in welk materiaal" wordt gevolgd door
       "en wat wordt daar dan van gemaakt". PLAATSHOUDERS, zie CASES. -->
  <section class="content-block" id="s07-projecten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{cfg["projecten_eyebrow"]}</span>
            <h2 class="section-heading">{cfg["projecten_kop"]}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              {cfg["projecten_intro"]}
            </p>
          </div>
          <div class="col-md-4 col-12 text-md-end">
            {knop(cfg["projecten_knop"], "cases.html")}
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{projecten}
      </div>
    </div>
  </section>

  <!-- ================= 08 IN CIJFERS ================= -->
  <section class="content-block" id="s08-usps">
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

  <!-- ================= 09 OFFERTE ================= -->
  <!-- Het statementblok van de template: een tekstslot in de grote lichte
       snede, geen kop. Stond direct onder de hero; draagt nu het antwoord op
       "hoe snel weet ik wat het kost". -->
  <section class="content-text-side-cta" id="s09-offerte">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
              <p>{cfg["offerte_tekst"]}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 10 HET TEAM ================= -->
  <!-- Portret-en-tekstband van de template. Van Vorma Metaal is geen
       medewerkersfoto beschikbaar en die verzinnen kan niet; het beeldslot
       houdt zijn plek en krijgt de werkplaatsfoto met medewerkers erop. -->
  <section class="streamer streamer--employee streamer--employee--portret background--groen" id="s10-team">
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

  <!-- ================= 11 TESTIMONIALS ================= -->
  <!-- PLAATSHOUDERS, zie inhoud/home.py. -->
{quoteslider("11", "testimonials", cfg["testimonials_eyebrow"], cfg["testimonials_kop"], testimonials,
             citaat=True, plaatshouder=True)}

  <!-- ================= 12 FAQ ================= -->
{faq_blok("12", cfg["faq"], cfg["faq_kop"])}

  <!-- ================= 13 CONTACT ================= -->
{ctablok("13", cfg["contact_kop"], cfg["contact_tekst"])}
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
