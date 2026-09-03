# -*- coding: utf-8 -*-
"""
Gedeelde paginaschil voor de Vorma Metaal-site, op de MADEGRO-template.

Dit script schrijft platte HTML-bestanden weg. De site zelf heeft geen build-stap:
wat hier uitkomt is gewone HTML die je met een statische server serveert. Dit
bestand hoort dan ook niet bij de site, het is gereedschap om de dertien pagina's
identiek te houden terwijl ze gebouwd worden.
"""

BASIS = "https://www.vormametaal.nl"

# Het hoofdmenu. Zelfde component en zelfde uitklapgedrag als in de
# MADEGRO-template; alleen de inhoud en de links zijn anders. De uitklapper met
# cursussen is eruit: Vorma Metaal geeft geen cursussen.
#
# De sublinks komen uit SERVICES verderop, zodat een wijziging daar meteen in
# het menu, de voet en het overzicht landt. Daarom wordt NAV pas onderaan
# opgebouwd, in bouw_nav().
NAV = []

# De acht bewerkingen van Vorma Metaal. Dit is dezelfde lijst en dezelfde vorm
# als de drie MADEGRO-diensten die hier stonden: (bestand, naam, ondertitel,
# beeldsleutel). De variabele houdt zijn naam, zodat de voet, het menu, de
# homepage en het dienstsjabloon ongewijzigd kunnen blijven werken.
#
# TODO-CONTENT: het beeld is opvulbeeld uit de stockmap van MADEGRO. Er zijn zes
# foto's voor acht diensten, dus er zit herhaling in. Zodra er foto's van de
# eigen werkplaats zijn, vervangen die deze.
SERVICES = [
    ("dienst-lasersnijden.html", "Lasersnijden",
     "Nauwkeurig snijden van plaatmateriaal", "lasersnijden"),
    ("dienst-buislasersnijden.html", "Buislasersnijden",
     "Snijden en bewerken van buis en profiel", "buislasersnijden"),
    ("dienst-kanten.html", "Kanten",
     "Plaatmateriaal zetten tot de gewenste vorm", "kanten"),
    ("dienst-lassen.html", "Lassen",
     "Lassen met TIG, MIG of laser", "lassen"),
    ("dienst-nabewerking.html", "Nabewerking",
     "Afbramen, tappen, boren en verzinken", "productiehal"),
    ("dienst-assemblage.html", "Assemblage",
     "Samenbouwen via ons zusterbedrijf", "werkplaats"),
    ("dienst-oppervlaktebehandeling.html", "Oppervlaktebehandeling",
     "Poedercoaten, volledig geregeld", "werkbank"),
    ("dienst-cnc-verspanen.html", "CNC-verspanen",
     "Draaien en frezen in eigen huis", "verspanen"),
]


def dienst(slug):
    """De regel uit SERVICES bij een slug, bijvoorbeeld 'lasersnijden'."""
    doel = f"dienst-{slug}.html"
    return next(s for s in SERVICES if s[0] == doel)


# De vijf stappen van aanvraag tot levering. Ze staan op de homepage (in de
# sectie waar MADEGRO "hoe we werken" had) en op werkwijze.html.
STAPPEN = [
    ("Aanvraag",
     "Upload uw CAD-bestanden, eventueel met een PDF. Wij nemen hem in behandeling."),
    ("Controle",
     "Wij controleren of uw aanvraag maakbaar is. Bij een complexe opdracht "
     "stemmen wij met u af."),
    ("Offerte",
     "U ontvangt een duidelijke, vrijblijvende offerte. Het werk start pas na "
     "uw akkoord."),
    ("Productie",
     "Wij maken uw producten in onze werkplaats: van lasersnijden en kanten tot "
     "verspanen, lassen en de afgesproken nabewerking."),
    ("Levering of afhalen",
     "Uw producten worden geleverd, of staan klaar om af te halen."),
]

# De drie materialen met hun voorbeeldkwaliteiten. Voorbeelden, geen
# voorraadlijst; bijzondere metalen zijn op aanvraag leverbaar.
def materiaal_slug(naam):
    """Het anker waar de materiaalrijen op de homepage naartoe wijzen.
       "Staal" -> #staal, "RVS" -> #rvs, "Aluminium" -> #aluminium."""
    return naam.lower()


MATERIALEN = [
    ("Staal",
     "Sterk, veelzijdig en geschikt voor uiteenlopende constructieve en "
     "industri&euml;le toepassingen.",
     ["DC01", "DD11", "S235JR", "S355MC", "DX51D+Z (sendzimir verzinkt)"]),
    ("RVS",
     "Corrosiebestendig en duurzaam materiaal voor toepassingen waar "
     "hygi&euml;ne, uitstraling en een lange levensduur belangrijk zijn.",
     ["RVS 304", "RVS 316", "Afwerking 2B of 1D, met of zonder beschermfolie"]),
    ("Aluminium",
     "Lichtgewicht, sterk en goed te bewerken, met een uitstekende verhouding "
     "tussen gewicht en sterkte.",
     ["EN AW-1050A", "EN AW-5005 (AlMg1)", "EN AW-5754 H111", "EN AW-5083"]),
]

# De tien sectoren. Ze vullen voor-wie.html en de band onderaan de homepage,
# waar MADEGRO de logoband van opdrachtgevers had.
SECTOREN = [
    "Machinebouw", "Constructie", "Installatietechniek", "Interieurbouw",
    "Industrie", "Productontwikkeling", "Engineering",
    "Technische dienstverlening", "Onderhoud en reparatie",
    "Bouwgerelateerde bedrijven",
]

# De bestandsformaten die het portaal inleest.
FORMATEN = ["STEP", "DXF", "DWG", "PDF"]


def bouw_nav():
    """NAV invullen zodra SERVICES bekend is.

       Zelfde structuur als MADEGRO: een paar gewone links plus één uitklapper
       met een kaart ernaast. De cursusuitklapper is eruit."""
    NAV.extend([
        {"soort": "link", "href": "index.html", "label": "Home"},
        {
            "soort": "uitklap", "id": "diensten", "label": "Diensten",
            "links": ([("diensten.html", "Alle diensten",
                        "De acht bewerkingen op een rij")]
                      + [(b, t, o) for b, t, o, _ in SERVICES]),
            "kaart": {
                "kop": "Niet zeker welke bewerkingen u nodig heeft?",
                "tekst": "Stuur uw CAD-bestand in. Wij controleren de "
                         "maakbaarheid en zetten de bewerkingen in de offerte.",
                "knop": "Offerte aanvragen",
                "href": "contact.html",
                "foto": "werkplaats",
            },
        },
        {"soort": "link", "href": "werkwijze.html", "label": "Werkwijze"},
        {"soort": "link", "href": "materialen.html", "label": "Materialen"},
        {"soort": "link", "href": "voor-wie.html", "label": "Voor wie"},
        {"soort": "link", "href": "over-vorma-metaal.html", "label": "Over Vorma Metaal"},
    ])


# ---------------------------------------------------------------- gegevens
TELEFOON_WEERGAVE = "0547 227 000"
TELEFOON_LINK = "+31547227000"
EMAIL = "info@vormametaal.nl"
ADRES = "Dammaten 14, 7472 DJ Goor"
ADRES_STRAAT = "Dammaten 14"
ADRES_POSTCODE = "7472 DJ"
ADRES_PLAATS = "Goor"
LINKEDIN = "https://www.linkedin.com/company/vormametaal/"
ZUSTERBEDRIJF = "Tentije Industri&euml;le Automatisering B.V."
ERVARING_JAREN = "22"

# TODO-CONTENT: het KvK-nummer staat niet op vormametaal.nl. Zolang dit leeg is
# laat de voet de regel weg; een verzonnen nummer is erger dan geen nummer.
KVK = ""

# De offertetermijn, letterlijk van vormametaal.nl. Standaardwerk gaat
# automatisch, complex werk langs een mens; in beide gevallen geen dagen wachten.
OFFERTE_STANDAARD = "binnen enkele minuten"
OFFERTE_COMPLEX = "binnen korte tijd"
# TODO-CONTENT: de reactietijd op een gewone vraag via het formulier staat niet
# op de bronsite en is dus een aanname.
# Hier stond REACTIETIJD = "&eacute;&eacute;n werkdag". Dat is eruit: op
# vormametaal.nl staat nergens een reactietermijn op mail of telefoon, dus
# was het een verzonnen belofte. Wat er wel staat, staat in
# OFFERTE_STANDAARD en OFFERTE_COMPLEX, en dat gaat over de offerte en
# niet over een antwoord op een bericht.

OPENINGSTIJDEN = [
    ("maandag t/m vrijdag", "07:30&ndash;16:30"),
    ("zaterdag en zondag", "gesloten"),
]


# (naam, groot, groothoogte, klein, kleinhoogte, alt, map, midden)
#
# Middenmaat staat op None voor alle foto's, en dat is een bewuste keuze. Er
# hebben tussenmaten van 800px in gezeten, want op een telefoon van 412 CSS-
# pixels met dpr 1,75 is 721px nodig en dan slaat de browser 640 over en neemt
# 1200. Op papier drie keer zoveel pixels als er te zien is.
#
# In beeld pakte dat verkeerd uit. Een kandidaat die net boven de gevraagde
# breedte ligt wordt door de browser met een goedkoper filter verkleind dan een
# kandidaat die er ruim boven ligt: 800 naar 720 werd zichtbaar zachter dan 1200
# naar 720. Vergeleken op schermafdrukken van voor en na, en nagerekend: de
# scherpte van het gebied zakte met ruim zestig procent. Dat is precies wat we
# niet wilden inleveren, dus de tussenmaten zijn eruit.
#
# Bij de patronen staat wel een tussenmaat, want daar zit geen fijn detail in
# dat zachter kan worden; het zijn vloeiende verlopen.
FOTOS = {
    # ---- Beeldjes uit de herofilm: de werkplaats en de bewerkingen ----
    # Allemaal uit dezelfde reeks, dus dezelfde hal, lichtval en kleuren.
    # De bron is 1280x720; er staat geen opgeschaalde maat in de srcset, want
    # dan doet een beeld scherper dan het is.
    #
    # De alt-teksten noemen geen materiaal. Uit een filmbeeld is niet te zien
    # of een plaat staal of RVS is, en dat dan toch opschrijven is een bewering
    # die niet uit de bron volgt. Hier stond eerst "stalen plaat" en "stalen
    # koker".
    'werkplaats':       ('werkplaats', 2260, 1440, 1130, 720,
                         'Lasersnijmachine in een productiehal', 'foto', None),
    'lasersnijden':     ('lasersnijden', 1280, 720, 640, 360,
                         'Snijkop boven een plaat, met de uitgesneden onderdelen eromheen', 'foto', None),
    'buislasersnijden': ('buislasersnijden', 1280, 720, 640, 360,
                         'Buislaser snijdt een koker op maat, met een regen van vonken', 'foto', None),
    # 1130 breed en niet 1280: op de jas van de operator staat het beeldmerk
    # van een ander bedrijf, tussen x=1136 en de rechterrand. Zie
    # assets/video/HERKOMST.md.
    'kanten':           ('kanten', 1130, 720, 640, 408,
                         'Operator zet een plaat in de kantbank', 'foto', None),
    'lassen':           ('lassen', 1280, 720, 640, 360,
                         'Lasboog op de verbinding tussen een koker en een plaat', 'foto', None),
    'verspanen':        ('verspanen', 1280, 720, 640, 360,
                         'Freeskop met koelvloeistof bewerkt een metalen onderdeel', 'foto', None),
    'productiehal':     ('productiehal', 1280, 720, 640, 360,
                         'Werkplaats met medewerkers aan gesneden plaatdelen', 'foto', None),
    'werkbank':         ('werkbank', 1280, 720, 640, 360,
                         'Werkbanken met een samengestelde constructie op de voorgrond', 'foto', None),

    # ---- De drie materialen ----
    # Aangeleverd door Jesse op 3 september 2026, twee per materiaal. Hiervan
    # staat de scherpste van elk paar op de site; zie assets/foto/HERKOMST.md
    # voor welke dat zijn en wat er met de andere drie kan.
    #
    # Ze staan in de materiaalrijen op de homepage, in een vak van 50vw met de
    # tekst ernaast. Geen enkele maat is opgeschaald: aluminium is 1200 breed
    # omdat de bron dat is.
    'staal':            ('staal', 1280, 800, 640, 400,
                         'Stapel stalen buizen', 'foto', None),
    'rvs':              ('rvs', 1280, 781, 640, 390,
                         'Gestapelde platen met een geschuurd oppervlak', 'foto', None),
    'aluminium':        ('aluminium', 1200, 630, 640, 336,
                         'Lichte metalen panelen in een ruitpatroon', 'foto', None),

    # ---- De zes redenen op de homepage ----
    # Aangeleverd door Jesse op 3 september 2026 als 01.png t/m 06.png; die
    # nummering hoort bij de zes kaarten. Welke kaart welke foto krijgt, staat
    # in _WAAROM_BEELD in bouw_home.py.
    #
    # Vijf van de zes zijn kantoorbeelden met mensen erop, en dat is een breuk
    # met de rest van de site: daar staat alleen werkplaats en machine. Op
    # verzoek. 'plaatdelen' is het enige productbeeld.
    #
    # Het beeldvak van de kaart staat op aspect-ratio 16/10 met cover, dus de
    # verschillende bronverhoudingen (2,00 tot 1,33) worden bijgesneden en
    # geven geen layoutprobleem. Geen maat is opgeschaald: laptop en telefoon
    # houden hun eigen breedte omdat de bron kleiner is dan 1280.
    'handdruk':         ('handdruk', 1280, 640, 640, 320,
                         'Twee mensen geven elkaar een hand', 'foto', None),
    'uitleg':           ('uitleg', 1280, 715, 640, 358,
                         'Man die iets uitlegt aan iemand tegenover hem', 'foto', None),
    'laptop':           ('laptop', 970, 646, 640, 426,
                         'Iemand werkt aan een laptop', 'foto', None),
    'calculator':       ('calculator', 1280, 640, 640, 320,
                         'Handen bij een rekenmachine naast een laptop', 'foto', None),
    'telefoon':         ('telefoon', 885, 531, 640, 384,
                         'Man kijkt glimlachend op zijn telefoon', 'foto', None),
    'plaatdelen':       ('plaatdelen', 1280, 960, 640, 480,
                         'Rij gekante plaatdelen op een werkbank', 'foto', None),
}


# Hoe breed een kaart werkelijk is, voor het sizes-attribuut. Zonder dit haalt
# de browser het grootste bestand op voor een kaart van een kwart pagina breed.
BEELD_MATEN_4 = "(max-width: 767px) 100vw, (max-width: 991px) 50vw, 25vw"
BEELD_MATEN_3 = "(max-width: 991px) 100vw, 33vw"


def foto(sleutel, klasse='', laden='lazy', maten='100vw', alt=None):
    """Eén beeld met srcset. De alt-tekst beschrijft wat er te
       zien is; bij puur decoratief beeld geef je alt='' mee.

       Twee of drie maten in de srcset, afhankelijk van of er een middenmaat is.
       De browser kiest zelf, op grond van sizes en de pixeldichtheid van het
       scherm."""
    naam, gb, gh, kb, kh, standaard_alt, map_, mb = FOTOS[sleutel]
    tekst = standaard_alt if alt is None else alt
    prioriteit = ' fetchpriority="high" decoding="async"' if laden == 'eager' else ' decoding="async"'
    maten_lijst = sorted({kb, gb} | ({mb} if mb else set()))
    srcset = ', '.join(f'assets/{map_}/{naam}-{b}.webp {b}w' for b in maten_lijst)
    return (f'<img src="assets/{map_}/{naam}-{gb}.webp" '
            f'srcset="{srcset}" '
            f'sizes="{maten}" width="{gb}" height="{gh}" alt="{tekst}" '
            f'loading="{laden}"{prioriteit}'
            + (f' class="{klasse}"' if klasse else '') + '>')

PIJL = ('<svg class="arrow--animation is-{n}" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>')


SPOOR = ('<span class="button__spoor" aria-hidden="true">'
         + PIJL.format(n=1).replace('width="16" height="16"', 'width="14" height="14"')
         + PIJL.format(n=2).replace('width="16" height="16"', 'width="14" height="14"')
         + '</span>')


def _inhoud(label):
    return f'<span class="button__inhoud">{label}{SPOOR}</span>'


def knop(label, href, soort='primary', extra=''):
    """De grote CTA-knop met dezelfde pijlwissel als de ronde icoonknop."""
    attr = f' {extra}' if extra else ''
    return f'<a href="{href}" class="button button--{soort}"{attr}>{_inhoud(label)}</a>'


def icoonknop(maat="", soort=""):
    """De ronde icoonknop uit §6.6.2. Decoratief: de hele kaart is de link.

       soort="button--secundair" geeft de diepgroene variant; die is voor de
       cases, die naast diensten en cursussen de tweede keus zijn."""
    klasse = f"button--icon {maat} {soort}".strip()
    return (f'<span class="{klasse}" aria-hidden="true" inert>'
            f'<span class="button--circle"><span class="circle-container">'
            f'{PIJL.format(n=1)}{PIJL.format(n=2)}'
            f'</span></span></span>')


CHEVRON = ('<svg class="submenu--chevron" width="12" height="12" viewBox="0 0 24 24" aria-hidden="true">'
           '<path d="M12 15.4 5.6 9 7 7.6l5 5 5-5L18.4 9 12 15.4Z"/></svg>')


def header(actief):
    """De balk met het logo, het hoofdmenu en de hamburger, plus de uitklappers
       en het mobiele paneel.

       De uitklappers staan buiten .header--container: ze lopen over de volle
       breedte onder de balk door, en dat kan niet binnen een flexrij. De balk
       is position:fixed en dus het ankerpunt voor hun position:absolute."""

    def is_actief(item):
        if item["soort"] == "link":
            return item["href"] == actief
        return any(b == actief for b, _, _ in item["links"])

    def bureau_item(item):
        aan = is_actief(item)
        klasse = "submenu--link is-actief" if aan else "submenu--link"
        if item["soort"] == "link":
            huidig = ' aria-current="page"' if aan else ""
            return f'      <a class="{klasse}" href="{item["href"]}"{huidig}>{item["label"]}</a>'
        return (f'      <button type="button" class="{klasse} submenu--trigger" '
                f'data-uitklap="{item["id"]}" aria-expanded="false" '
                f'aria-controls="uitklap-{item["id"]}">{item["label"]}{CHEVRON}</button>')

    def paneel(item):
        if item["soort"] != "uitklap":
            return ""
        k = item["kaart"]
        links = "\n".join(
            f'          <li><a class="uitklap__link" href="{b}">'
            f'<span class="uitklap__naam">{titel}</span>'
            f'<span class="uitklap__uitleg">{onder}</span></a></li>'
            for b, titel, onder in item["links"])
        return f'''  <div class="uitklap" id="uitklap-{item["id"]}" data-uitklap-paneel="{item["id"]}" inert>
    <div class="uitklap__inner">
      <div class="uitklap__kolom">
        <span class="subtitle">{item["label"]}</span>
        <ul class="uitklap__lijst" role="list">
{links}
        </ul>
      </div>
      <div class="uitklap__kaart">
        {foto(k["foto"], maten="(max-width: 1199px) 0px, 40vw", alt="")}
        <span class="uitklap__sluier" aria-hidden="true"></span>
        <div class="uitklap__kaart-tekst">
          <p class="uitklap__kaart-kop">{k["kop"]}</p>
          <p class="uitklap__kaart-body">{k["tekst"]}</p>
          {knop(k["knop"], k["href"])}
        </div>
      </div>
    </div>
  </div>'''

    def mobiel_item(item, i):
        vertraging = f'style="transition-delay:{i * 60}ms"'
        rol = (f'<span class="mobile-panel--text-slide"><span class="mobile-panel--text-slide-inner">'
               f'<span>{item["label"]}</span><span>{item["label"]}</span></span></span>')
        if item["soort"] == "link":
            return (f'      <li><a class="mobile-panel--nav-link" href="{item["href"]}" '
                    f'data-panel-sluit {vertraging}>{rol}</a></li>')
        sub = "\n".join(
            f'          <li><a class="mobile-panel--sublink" href="{b}" data-panel-sluit>{titel}</a></li>'
            for b, titel, _ in item["links"])
        return f'''      <li>
        <button type="button" class="mobile-panel--nav-link mobile-panel--nav-knop"
                data-mobiel-uitklap="{item["id"]}" aria-expanded="false"
                aria-controls="mobiel-{item["id"]}" {vertraging}>{rol}{CHEVRON}</button>
        <ul class="mobile-panel--sublijst" id="mobiel-{item["id"]}" role="list" hidden>
{sub}
        </ul>
      </li>'''

    links = "\n".join(bureau_item(n) for n in NAV)
    panelen = "\n".join(filter(None, (paneel(n) for n in NAV)))
    paneel_links = "\n".join(mobiel_item(n, i) for i, n in enumerate(NAV))

    # 85x40 en niet 227x40: de Vorma-lockup is 2,118:1 waar het woordmerk van
    # de template 5,675:1 was. De hoogte blijft 40px, dus de balk en zijn
    # spacing veranderen niet. Deze toelichting hoort niet in de uitvoer: de
    # naam van het bronproject staat niet in de geleverde HTML.
    return f'''<header class="header header--scrolled" id="siteHeader">
  <div class="header--container">
    <a href="index.html" class="header--logo" aria-label="Vorma Metaal, naar de homepage">
      <img class="header--logo-kleur" src="assets/logo/vorma-metaal.svg" alt="Vorma Metaal" width="85" height="40">
      <img class="header--logo-wit" src="assets/logo/vorma-metaal-wit.svg" alt="" aria-hidden="true" width="85" height="40">
    </a>

    <nav class="submenu" aria-label="Hoofdmenu">
{links}
      <a class="submenu--link highlight" href="contact.html">Contact</a>
    </nav>

    <button type="button" id="hamburger" class="hamburger" aria-expanded="false" aria-controls="mobilePanel">
      Menu
      <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5h20v2H2V5Zm0 6h20v2H2v-2Zm0 6h20v2H2v-2Z"/></svg>
    </button>
  </div>

{panelen}
</header>

<div class="mobile-panel--overlay" id="panelOverlay" hidden></div>
<div class="mobile-panel" id="mobilePanel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-panel--topbar">
    <a class="mobile-panel--chip" href="contact.html">Contact</a>
    <button type="button" class="mobile-panel--chip is-close" id="panelSluit">
      Sluiten
      <svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6L19 6.4Z"/></svg>
    </button>
  </div>
  <nav class="mobile-panel--nav" aria-label="Hoofdmenu">
    <span class="mobile-panel--label">Menu</span>
    <ul class="mobile-panel--list" role="list">
{paneel_links}
    </ul>
  </nav>
  <div class="mobile-panel--cta button__mobile-width">
    {knop("Vraag een offerte aan", "contact.html")}
  </div>
</div>'''


def footer():
    """Zelfde vier kolommen als MADEGRO. De cursuskolom is de sitekolom
       geworden; de layout, de klassen en de verhoudingen blijven gelijk.

       De KvK-regel valt weg zolang KVK leeg is: een lege regel "KvK" onder het
       adres leest als een fout en een verzonnen nummer is erger."""
    services = "\n".join(f'            <li><a href="{b}">{t}</a></li>' for b, t, _, _ in SERVICES)
    tijden = "<br>".join(f'{dag}: {tijd}' for dag, tijd in OPENINGSTIJDEN)
    kvk_regel = f'<br>KvK {KVK}' if KVK else ''
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer--widgets">
      <div class="row footer--gap">
        <div class="col-lg-3 col-md-4 col-12 widget">
          <img src="assets/logo/vorma-metaal.svg" alt="Vorma Metaal" width="85" height="40" style="margin-bottom:var(--space-500)">
          <p class="footer--intro">Maatwerk in metaal, van enkelstuks tot seriematige productie. Lasersnijden, buislasersnijden, kanten, lassen, nabewerking, assemblage, oppervlaktebehandeling en CNC-verspanen.</p>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h3>Diensten</h3>
          <ul role="list">
{services}
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h3>Site</h3>
          <ul role="list">
            <li><a href="werkwijze.html">Werkwijze</a></li>
            <li><a href="materialen.html">Materialen</a></li>
            <li><a href="voor-wie.html">Voor wie</a></li>
            <li><a href="over-vorma-metaal.html">Over Vorma Metaal</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h3>Contact</h3>
          <ul role="list">
            <li><a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <p class="footer--adres">{ADRES_STRAAT}<br>{ADRES_POSTCODE} {ADRES_PLAATS}{kvk_regel}</p>
          <p class="footer--adres">{tijden}</p>
        </div>
      </div>
    </div>
    <div class="footer--line"></div>
    <div class="footer--copyright">
      <span>&copy; 2026 Vorma Metaal</span>
      <a href="privacybeleid.html">Privacybeleid</a>
      <a href="cookies.html">Cookies</a>
    </div>
  </div>
</footer>'''


COOKIEBALK = '''<!-- ================= COOKIEMELDING ================= -->
<aside id="cookiebalk" class="cookiebalk" hidden aria-label="Cookiemelding">
  <h2>Cookie-instellingen</h2>
  <p>Deze site plaatst alleen wat nodig is om hem te laten werken. Zet u analytische cookies aan, dan helpt u ons te zien wat werkt en wat niet. Lees het <a href="cookies.html">cookiebeleid</a>.</p>

  <div id="cookieKeuzes" class="cookie-keuzes" hidden>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" checked disabled aria-label="Functionele cookies, altijd aan">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Functioneel</span>
        <p>Nodig om de site te laten werken. Staat altijd aan.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieAnalytisch" aria-label="Analytische cookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Analytisch</span>
        <p>Laat ons zien welke pagina&rsquo;s bezocht worden, zodat we de site kunnen verbeteren.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieMarketing" aria-label="Marketingcookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Marketing</span>
        <p>Voor advertenties en het meten daarvan. Nu niet in gebruik.</p>
      </div>
    </div>
  </div>

  <div class="cookie-knoppen">
    <button type="button" class="cookie-knop" data-cookie="weigeren">Weigeren</button>
    <button type="button" class="cookie-knop" data-cookie="aanpassen">Aanpassen</button>
    <button type="button" class="cookie-knop cookie-knop--donker" data-cookie="toestaan">Toestaan</button>
  </div>
</aside>'''


ORGANISATIE_LD = f'''{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Vorma Metaal",
  "foundingDate": "2004",
  "url": "{BASIS}/",
  "logo": "{BASIS}/assets/logo/vorma-metaal.svg",
  "email": "{EMAIL}",
  "telephone": "{TELEFOON_LINK}",
  "vatID": null,
  "identifier": {{ "@type": "PropertyValue", "name": "KvK", "value": "{KVK}" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Dammaten 14",
    "postalCode": "7472 DJ",
    "addressLocality": "Goor",
    "addressCountry": "NL"
  }}
}}'''


def pagina(bestand, titel, omschrijving, namespace, pagina_css, css_naam,
           inhoud, scripts=(), extra_ld=None, actief=None, body_klasse=""):
    """Zet één complete HTML-pagina in elkaar."""
    ld_blokken = f'<script type="application/ld+json">\n{ORGANISATIE_LD}\n</script>'
    if extra_ld:
        ld_blokken += f'\n<script type="application/ld+json">\n{extra_ld}\n</script>'

    script_regels = "\n".join(f'<script src="{s}"></script>' for s in scripts)
    body_attr = f' class="{body_klasse}"' if body_klasse else ""

    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titel}</title>
<meta name="description" content="{omschrijving}" />
<link rel="canonical" href="{BASIS}/{bestand}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="Vorma Metaal" />
<meta name="theme-color" content="#143557" />
<meta name="color-scheme" content="light" />

<!-- GSAP en Barba komen van jsDelivr. Het opzetten van die verbinding (dns,
     tcp, tls) kost op een telefoon een paar honderd ms en begint nu al terwijl
     de HTML nog binnenkomt, in plaats van pas onderaan de pagina. -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />

<!-- Het lettertype staat in de kop van de pagina en is dus onderdeel van de
     LCP. Zonder preload vindt de browser het pas nadat styleguide.css binnen is
     en ontleed is. crossorigin moet erbij, ook al staat het bestand op dezelfde
     server: een font wordt altijd in CORS-modus opgehaald, en zonder dat woord
     haalt de browser het twee keer op. -->
<link rel="preload" href="assets/fonts/inter-tight-latin.woff2" as="font" type="font/woff2" crossorigin />

<link rel="stylesheet" href="styleguide.css" />
<link rel="stylesheet" href="transitions.css" />
<!-- De cookiebalk verschijnt pas als cookiebalk.js hem opbouwt, dus zijn stijl
     hoeft de eerste weergave niet op te houden. media="print" laat de browser
     hem buiten het kritieke pad ophalen; onload zet hem daarna alsnog aan. De
     noscript-regel vangt op dat zonder JavaScript ook die onload niet afgaat. -->
<link rel="stylesheet" href="cookiebalk.css" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="cookiebalk.css" /></noscript>
<link rel="stylesheet" href="{pagina_css}" data-page-css="{css_naam}" />

<link rel="icon" href="assets/favicon/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png" />

<meta property="og:type" content="website" />
<meta property="og:site_name" content="Vorma Metaal" />
<meta property="og:locale" content="nl_NL" />
<meta property="og:url" content="{BASIS}/{bestand}" />
<meta property="og:title" content="{titel}" />
<meta property="og:description" content="{omschrijving}" />
<meta property="og:image" content="{BASIS}/assets/social/vorma-metaal-deelafbeelding.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{titel}" />
<meta name="twitter:description" content="{omschrijving}" />

{ld_blokken}
</head>

<body{body_attr}>
<a class="skip-link" href="#main-content">Naar de inhoud</a>

<!-- De header en het mobiele paneel staan bewust BUITEN #smooth-wrapper.
     ScrollSmoother verschuift de inhoud met een transform, en onder een
     transform hangt position:fixed aan dat element in plaats van aan het
     scherm. Ze blijven daardoor ook staan bij een pagina-overgang; welke
     menulink actief is wordt in page-transitions.js bijgewerkt. -->
{header(actief or bestand)}

<div id="smooth-wrapper">
<div id="smooth-content">

<div data-barba="wrapper">
<div class="app__wrapper" data-barba="container" data-barba-namespace="{namespace}">
<div class="content__wrapper">

<main id="main-content">

{inhoud}

</main>

{footer()}

<script src="site.js"></script>
<script src="contactformulier.js"></script>
{script_regels}
</div><!-- /.content__wrapper -->
</div><!-- /[data-barba=container] -->
</div><!-- /[data-barba=wrapper] -->

</div><!-- /#smooth-content -->
</div><!-- /#smooth-wrapper -->

{COOKIEBALK}

<!-- ================= PAGINA-OVERGANGEN =================
     Barba wisselt alleen de container hierboven om, GSAP animeert de wissel. -->
<!-- defer: de browser haalt ze op terwijl hij de pagina nog aan het ontleden is
     en voert ze daarna uit, in deze volgorde. Die volgorde is nodig, want
     ScrollTrigger heeft gsap nodig en page-transitions.js heeft Barba nodig. -->
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollSmoother.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@barba/core@2.10.3/dist/barba.umd.js"></script>
<script defer src="cookiebalk.js"></script>
<script defer src="analytics.js"></script>
<script defer src="smooth-scroll.js"></script>
<script defer src="page-transitions.js"></script>

</body>
</html>
'''


# ============================================================================
# PLAATSHOUDER -- MAG NIET LIVE
# ----------------------------------------------------------------------------
# De logoband draagt dertien beeldmerken van bestaande, herkenbare bedrijven:
# Alstom, Ballast Nedam, Bilfinger, Cosun, Ebert Hera, Electrabel, Freesmij,
# GE Vernova, Huhtamaki, Ivens, Ooms, Stork en TES.
#
# GEEN VAN DIE BEDRIJVEN IS OPDRACHTGEVER VAN VORMA METAAL. Ze komen uit de
# template. Op vormametaal.nl staan geen klantlogo's en er zijn er ook geen
# aangeleverd. Ze staan hier op verzoek, om tijdens het bouwen te zien hoe de
# band eruitziet.
#
# Live gaan met deze band is een onware claim, richting de bezoeker en richting
# de dertien genoemde bedrijven. `python3 _generator/audit.py` meldt hem daarom
# op elke pagina waar hij staat; die melding hoort pas weg te zijn als er echte
# logo's met toestemming staan, of als de band terug is op sectorenband().
#
# Terugzetten op de sectorenband is één regel: in slotblok() en in
# bouw_home.py logoslider(...) vervangen door sectorenband(...). Die functie
# staat hieronder en draagt de tien sectoren, wat aantoonbaar waar is.
# ============================================================================

# Breedte is de echte breedte van het bestand op 80px hoog; die staat in de HTML
# zodat er geen sprong in de band zit terwijl ze laden.
OPDRACHTGEVERS = [
    ("alstom",        "Alstom",                       408),
    ("ballast-nedam", "Ballast Nedam",                452),
    ("bilfinger",     "Bilfinger",                    210),
    ("cosun",         "Cosun Beet Company",           345),
    ("ebert-hera",    "Ebert Hera",                   389),
    ("electrabel",    "Electrabel / GDF Suez",        203),
    ("freesmij",      "Freesmij",                     309),
    ("ge-vernova",    "GE Vernova",                   362),
    ("huhtamaki",     "Huhtamaki",                    478),
    ("ivens",         "Ivens",                        237),
    ("ooms",          "Ooms Bouw &amp; Ontwikkeling", 248),
    ("stork",         "Stork",                        197),
    ("tes",           "TES Industrial Systems",       160),
]


def _logoset(verborgen=False, plat=False):
    """De logo's in de band. Het tweede exemplaar van de reeks is aria-hidden,
       dus een schermlezer hoort de namen een keer.

       Het adres staat in data-src en niet in src, en site.js zet het om zodra
       de band in de buurt van het scherm komt. Dat scheelt bij het openen van
       elke pagina; de band staat altijd onderaan.

       loading="lazy" werkt hier niet, dat is gemeten: het venster knipt af met
       overflow:hidden, waardoor de browser alles rechts van de rand als "niet
       in beeld" ziet. Vandaar een waarnemer op de sectie zelf.

       plat=True geeft dezelfde reeks met een gewone src, voor de noscript."""
    extra = ' aria-hidden="true"' if verborgen else ''
    bron = 'src' if plat else 'data-src'
    regels = "\n".join(
        '          <li class="logo-slider__logo">'
        f'<img {bron}="assets/partners/{slug}.webp" alt="{naam}" '
        f'width="{breedte}" height="80" decoding="async"></li>'
        for slug, naam, breedte in OPDRACHTGEVERS)
    return f'        <ul class="logo-slider__set"{extra}>\n{regels}\n        </ul>'


def logoslider(nr):
    """De doorlopende logoband. De reeks staat er twee keer in: de animatie
       schuift precies de helft op, zodat het naadloos doorloopt. De band
       pauzeert bij hover en staat stil bij prefers-reduced-motion.

       Het label is "Logoband" en niet "Opdrachtgevers". Dat is de enige plek
       waar de band iets in woorden beweert, en die bewering is niet waar: het
       zijn de logo's van de template. Visueel verandert er niets door; een
       schermlezer krijgt geen claim te horen die niet klopt."""
    return (f'  <section class="logo-slider" id="s{nr}-partners" aria-label="Logoband" data-logoband>\n'
            '    <div class="logo-slider__venster">\n'
            '      <div class="logo-slider__spoor">\n'
            f'{_logoset()}\n{_logoset(verborgen=True)}\n'
            '      </div>\n'
            '    </div>\n'
            '    <noscript>\n'
            '      <div class="logo-slider__venster">\n'
            '        <div class="logo-slider__spoor">\n'
            f'{_logoset(plat=True)}\n{_logoset(verborgen=True, plat=True)}\n'
            '        </div>\n'
            '      </div>\n'
            '    </noscript>\n'
            '  </section>')


def sectorenband(nr, label="Sectoren waarvoor wij werken"):
    """De doorlopende band uit de template, met de tien sectoren als tekst in
       plaats van beeldmerken. De reeks staat er twee keer in: de animatie
       schuift precies de helft op, zodat het naadloos doorloopt. Het tweede
       exemplaar is aria-hidden, dus een schermlezer hoort de namen een keer.
       De band pauzeert bij hover en staat stil bij prefers-reduced-motion.

       Geen data-logoband: dat attribuut zette site.js aan om data-src om te
       zetten in src, en er zijn geen afbeeldingen meer om te laden. Ook geen
       noscript-variant, want tekst staat er zonder JavaScript al."""
    def spoor(verborgen=False):
        extra = ' aria-hidden="true"' if verborgen else ''
        regels = "\n".join(
            f'          <li class="logo-slider__logo logo-slider__tekst">{s}</li>'
            for s in SECTOREN)
        return f'        <ul class="logo-slider__set"{extra}>\n{regels}\n        </ul>'
    return (f'  <section class="logo-slider" id="s{nr}-partners" aria-label="{label}">\n'
            '    <div class="logo-slider__venster">\n'
            '      <div class="logo-slider__spoor">\n'
            f'{spoor()}\n{spoor(verborgen=True)}\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


# ---------------------------------------------------------------------------
# HERSTELD uit het startpunt van de template. Bij het weghalen van de
# logoband is dit blok per ongeluk meegegaan; het is teruggezet uit
# scratchpad/madegro-startpunt-170049. Alles wat hierna in de
# Vorma-bewerking is aangepast, is opnieuw aangebracht en staat per functie
# aangetekend.
# ---------------------------------------------------------------------------

def ctablok(nr, kop, tekst=None):
    """Verwijst naar de contactpagina in plaats van zelf een formulier te tonen.
       Het formulier zelf staat op contact.html; dit is de aanloop erheen.

       Eén vlak over de volle breedte, alles gecentreerd. In de template stond
       hier een contactkaart naast; die is eruit gehaald omdat dezelfde gegevens
       een klik verderop staan.

       De standaardregel noemt geen termijn. Hij zegt wat de bezoeker kan doen en
       wat een aanvraag hem kost: niets, tot hij akkoord geeft."""
    regel = tekst or ('Stuur uw CAD-bestand mee, of stel eerst uw vraag. Een aanvraag '
                      'is vrijblijvend: het werk start pas na uw akkoord.')
    return (f'  <section class="cta-slot" id="s{nr}-contact">\n'
            '    <div class="container">\n'
            '      <div class="cta-slot__hoofd">\n'
            '        <span class="subtitle cta-slot__label">Contact</span>\n'
            f'        <h2 class="cta-slot__kop">{kop}</h2>\n'
            f'        <p class="cta-slot__tekst">{regel}</p>\n'
            '        <div class="cta-slot__actie">\n'
            f'          {knop("Vraag een offerte aan", "contact.html")}\n'
            '        </div>\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


def paginahero(nr, ident, label, titel, beeld, alt=None, positie=None):
    """De hero met links de kop op grijs en rechts een foto. De <h1> staat in de
       HTML voor het beeld; onder 768px zet de CSS het beeld met order bovenaan,
       zodat de leesvolgorde blijft kloppen."""
    stijl = f' style="object-position:{positie}"' if positie else ""
    beeldtag = foto(beeld, laden="eager", maten="(max-width: 767px) 100vw, 50vw", alt=alt)
    if stijl:
        beeldtag = beeldtag.replace("<img ", f"<img{stijl} ")
    return (f'  <section class="paginahero" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld">\n'
            f'      {beeldtag}\n'
            '    </div>\n'
            '  </section>')


def patroonhero(nr, ident, label, titel):
    """Dezelfde hero, maar met het merkpatroon in plaats van een foto.

       Twee bestanden, want de compositie verschilt: op breed scherm staat het
       patroon rechts in een liggend vak, op een telefoon als brede band boven de
       titel. <picture> kiest ze op dezelfde grens als de layout zelf omslaat
       (768px), zodat er nooit een verkeerde uitsnede te zien is.

       Hoe hoog die band is, staat in de stylesheet en niet in het bestand: 7:3
       plus de hoogte van de vaste balk, want die ligt eroverheen. Het
       bronbestand is daarom vierkant en niet al op 7:3 gesneden; cover heeft
       verticaal wat over nodig.

       Het patroon is versiering en zegt niets wat de kop niet al zegt, dus
       alt="" en aria-hidden: een schermlezer slaat het over."""
    return (f'  <section class="paginahero paginahero--patroon" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld" aria-hidden="true">\n'
            '      <picture>\n'
            '        <source media="(max-width: 767px)" srcset="assets/patronen/hero-patroon-mobiel-720.webp 720w, assets/patronen/hero-patroon-mobiel-800.webp 800w, assets/patronen/hero-patroon-mobiel-1440.webp 1440w" sizes="100vw" width="1440" height="1440">\n'
            '        <img src="assets/patronen/hero-patroon-1440.webp" srcset="assets/patronen/hero-patroon-720.webp 720w, assets/patronen/hero-patroon-1000.webp 1000w, assets/patronen/hero-patroon-1440.webp 1440w" sizes="50vw" width="1440" height="940" alt="" loading="eager" fetchpriority="high" decoding="async">\n'
            '      </picture>\n'
            '    </div>\n'
            '  </section>')


KLEURENRIJ = ("geel", "grijs", "wit", "groen")


def vlakkenrij(nr, ident, kop, vlakken, subtitel=None):
    """Kop met daaronder vier gekleurde vlakken over de volle breedte. vlakken is
       een lijst van (kop, tekst); de kleuren lopen vast in dezelfde volgorde,
       zodat de rij op elke pagina hetzelfde ritme heeft."""
    label = f'        <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n' if subtitel else ""
    items = "\n".join(
        f'      <li class="vlak vlak--{KLEURENRIJ[i % 4]}">\n'
        f'        <h3 class="vlak__kop">{titel}</h3>\n'
        f'        <p class="vlak__tekst">{tekst}</p>\n'
        '      </li>'
        for i, (titel, tekst) in enumerate(vlakken)
    )
    return (f'  <section class="vlakkenband" id="s{nr}-{ident}">\n'
            '    <div class="container">\n'
            '      <div class="vlakkenband__kop">\n'
            f'{label}'
            f'        <h2 class="section-heading">{kop}</h2>\n'
            '      </div>\n'
            '    </div>\n'
            '    <ul class="vlakkenrij">\n'
            f'{items}\n'
            '    </ul>\n'
            '  </section>')


def beeldkaart(kop, tekst, beeld, alt=None, kleur="grey", href=None):
    """Een kaart met de foto erboven en de tekst eronder, twee per rij. Dit is de
       verticale variant van .cta-blocks-advanced."""
    binnen = (f'      <figure class="cta-blocks-advanced__banner">\n'
              f'        {foto(beeld, maten="(max-width: 991px) 100vw, 50vw", alt=alt)}\n'
              '        <span class="cta-blocks-advanced__backdrop" aria-hidden="true"></span>\n'
              '      </figure>\n'
              f'      <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{kleur}">\n'
              f'        <h3 class="cta-blocks-advanced__title">{kop}</h3>\n'
              '        <div class="cta-blocks-advanced__wrapper">\n'
              f'          <div class="cta-blocks-advanced__content"><p>{tekst}</p></div>\n'
              '        </div>\n'
              '      </div>')
    if href:
        omhulsel = (f'    <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" '
                    f'href="{href}">\n{binnen}\n    </a>')
    else:
        omhulsel = f'    <div class="cta-blocks-advanced__card">\n{binnen}\n    </div>'
    return f'  <div class="col-lg-6 col-12 kolom--vullend">\n{omhulsel}\n  </div>'


def cursuskaart(i, cursus):
    """Eén cursus als paneel met de foto erboven. Staat hier en niet in de twee
       bouwbestanden, want de kaart komt op de homepage en op het cursus-
       overzicht voor; zo blijft het één definitie.

       De alt is leeg: de foto zegt niets wat de link niet al zegt, en een
       schermlezer zou anders eerst een beschrijving van een productiehal
       voorlezen voordat hij bij de cursusnaam is."""
    bestand, titel, doelgroep, duur, beeld = cursus
    return f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_4, alt="")}
            </figure>
            <span class="panel__meta">{doelgroep}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{duur}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''


def dienstkaart(i, dienst, intro):
    """Eén dienst als kaart met de foto erboven. Alleen de homepage gebruikt hem,
       maar hij staat hier bij cursuskaart() omdat het dezelfde soort kaart is."""
    bestand, titel, sub, beeld = dienst
    return f'''        <div class="col-lg-4 col-12 kolom--vullend">
          <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" href="{bestand}"
             aria-label="{titel}: {sub}">
            <figure class="cta-blocks-advanced__banner cta-blocks-advanced__banner--verhouding">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{'grey' if i % 2 == 0 else 'white'}">
              <span class="subtitle">Dienst 0{i + 1}</span>
              <div class="cta-blocks-advanced__wrapper">
                <div>
                  <h3 class="cta-blocks-advanced__title" style="margin-bottom:var(--space-500)">{titel}</h3>
                  <div class="cta-blocks-advanced__content"><p>{sub}</p><p>{intro}</p></div>
                </div>
                {icoonknop("button--icon--56")}
              </div>
            </div>
          </a>
        </div>'''


# Voorlopige woordmerken voor de verzonnen opdrachtgevers bij de citaten.
# TODO-CONTENT: dit zijn geen echte logo's. Ze zijn hier gemaakt als grijze
# letters in een websafe schreefloze, zodat de opmaak af is. Een logo van een
# van de dertien echte opdrachtgevers kan hier niet staan: dan hangt er een
# aanbeveling van Alstom of Stork onder een citaat dat niemand heeft gegeven.
# Zie CONTENT-TODO.md.
PLAATSHOUDER_LOGOS = {
    "van-deursen-metaal":    ("Van Deursen Metaal", 317),
    "rivierpoort-logistiek": ("Rivierpoort Logistiek", 317),
    "merwede-bouwgroep":     ("Merwede Bouwgroep", 275),
}


def quotelogo(slug):
    """Het logoslot onder de afzender in de band van quoteslider().

       slug=False laat het slot helemaal weg. Dat is wat deze site gebruikt: het
       component draagt geen klantcitaten meer maar afspraken van Vorma Metaal
       zelf, en daar hoort geen logo van een opdrachtgever bij.

       slug=None geeft het gele invulveld, voor als er ooit een echt citaat met
       een echt logo komt. De tak die een logo uit OPDRACHTGEVERS haalde is
       eruit: die lijst bestond uit beeldmerken van bedrijven die geen
       opdrachtgever van Vorma Metaal zijn. Zie de toelichting bij
       sectorenband()."""
    if slug is False:
        return ''
    if slug is None:
        return ('<p class="quote__logo quote__logo--leeg">'
                '<span class="invulveld">Logo opdrachtgever</span></p>')
    naam, breedte = PLAATSHOUDER_LOGOS[slug]
    return (f'<p class="quote__logo quote__logo--plaatshouder">'
            f'<img src="assets/partners/{slug}.svg" alt="{naam}" '
            f'width="{breedte}" height="80" loading="lazy" decoding="async"></p>')


def quoteslider(nr, ident, subtitel, kop, items):
    """Een uitspraak per keer, groot uitgelicht: beeld links, tekst rechts, met
       een streepje boven de afzender. Pijlen eronder om te bladeren.

       In de template droeg dit component klantcitaten. Vorma Metaal heeft geen
       testimonials met naam en toestemming, dus staan hier de afspraken die het
       bedrijf zelf maakt, met Vorma Metaal als afzender. Daarom geen
       <blockquote> en geen "citaat" in de toegankelijkheidslabels: het is geen
       aangehaalde uitspraak van een derde, en een schermlezer hoort dat verschil.

       items is een lijst van (tekst, naam, functie, fotosleutel, logoslug). De
       foto is een werkplek en geen portret. Voor logoslug: zie quotelogo()."""
    dias = "\n".join(f'''        <figure class="quote" role="group" aria-roledescription="afspraak"
               aria-label="Afspraak {i + 1} van {len(items)}">
          <div class="quote__beeld">
            {foto(sleutel, maten="(max-width: 767px) 100vw, 40vw")}
          </div>
          <div class="quote__body">
            <div class="quote__tekst"><p>{citaat}</p></div>
            <hr class="quote__streep">
            <figcaption class="quote__naam">{naam}, {functie}</figcaption>
            {quotelogo(logo)}
          </div>
        </figure>''' for i, (citaat, naam, functie, sleutel, logo) in enumerate(items))

    return f'''  <section class="quotes" id="s{nr}-{ident}">
    <div class="container">
      <div class="quotes__kop">
        <span class="subtitle">{subtitel}</span>
        <h2 class="section-heading">{kop}</h2>
      </div>
      <div class="quotes__venster" data-quoteslider aria-live="polite">
{dias}
      </div>
      <!-- De pijlen staan hidden en worden door site.js zichtbaar gemaakt.
           Zonder JavaScript staan alle citaten gewoon onder elkaar en zou je
           op knoppen klikken die niets doen. -->
      <div class="quotes__nav" hidden>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="vorige" aria-label="Vorige quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("links")}</span></span>
        </button>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="volgende" aria-label="Volgende quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("rechts")}</span></span>
        </button>
        <p class="quotes__teller" data-quote-teller>1 / {len(items)}</p>
      </div>
    </div>
  </section>'''


def _pijl_paar(richting):
    """De pijl uit de icoonknop, twee keer, zodat de bestaande hover-animatie
       (de ene schuift weg, de andere komt binnen) blijft werken."""
    draai = ' style="transform:scaleX(-1)"' if richting == "links" else ""
    pad = ('<path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/>')
    return "".join(
        f'<svg class="arrow--animation is-{n}" width="16" height="16" viewBox="0 0 24 24"'
        f' aria-hidden="true"{draai}>{pad}</svg>' for n in (1, 2))


def slotblok(nr, kop, tekst=None):
    """De band met daaronder de CTA, zoals in de template. Het zijn twee
       secties, dus ook twee nummers: de band krijgt nr, het contactblok nr+1.

       Die band draagt nu de logoband met de beeldmerken van de template. Dat
       is een PLAATSHOUDER; zie het kader boven OPDRACHTGEVERS. Voor de
       aantoonbaar ware variant: sectorenband()."""
    return logoslider(nr) + "\n\n" + ctablok(f"{int(nr) + 1:02d}", kop, tekst)


# LET OP: deze functie wordt nergens aangeroepen. Het formulier op contact.html
# wordt door bouw_contact.py zelf neergezet. De standaardteksten staan hier toch
# in "u" en zonder reactietermijn, zodat er niets fouts uitkomt als hij ooit
# weer gebruikt wordt.
def contactblok(onderwerp, kop="Vraag een offerte aan",
                intro="Stuur uw CAD-bestand mee, of stel eerst uw vraag. Een "
                      "aanvraag is vrijblijvend."):
    """Het gedeelde formulier. De HTML wordt door contactformulier.js gerenderd;
       hier staat alleen de haak plus een terugval voor bezoekers zonder JS."""
    return f'''  <section class="band background--grey" id="s{onderwerp["nr"]}-contact">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Contact</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">{kop}</h2>
          <p class="article-body">{intro}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <div data-contactformulier data-onderwerp="{onderwerp["waarde"]}"></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
              <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>'''


def faq_blok(nr, items, titel="Veelgestelde vragen"):
    """Drie FAQ-items als accordeon plus de bijbehorende FAQPage-structuurdata."""
    regels = []
    for i, (vraag, antwoorden) in enumerate(items):
        alineas = "".join(f"<p>{a}</p>" for a in antwoorden)
        regels.append(f'''          <div class="accordion__item">
            <button type="button" class="accordion__header" aria-expanded="false" aria-controls="faq-{nr}-{i}">
              <span class="accordion__number">{i + 1:02d}</span>
              <span class="accordion__title">{vraag}</span>
              <span class="accordion__suffix" aria-hidden="true"><span class="accordion__icon"></span></span>
            </button>
            <div class="accordion__details" id="faq-{nr}-{i}">
              <div class="accordion__details-inner article-body">{alineas}</div>
            </div>
          </div>''')
    return f'''  <section class="band background--white" id="s{nr}-faq">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-12">
          <span class="subtitle">FAQ</span>
          <h2 class="font-size--lg" style="margin-top:var(--space-500)">{titel}</h2>
        </div>
        <div class="col-md-8 col-12">
          <div class="accordion">
{chr(10).join(regels)}
          </div>
        </div>
      </div>
    </div>
  </section>'''


def faq_ld(items):
    import json
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": _plat(v),
             "acceptedAnswer": {"@type": "Answer", "text": " ".join(_plat(a) for a in ant)}}
            for v, ant in items
        ],
    }, ensure_ascii=False, indent=2)


def _plat(tekst):
    import re, html
    return html.unescape(re.sub(r"<[^>]+>", "", tekst))


# NAV verwijst naar SERVICES en foto(); die staan hierboven, dus de
# lijst wordt hier pas gevuld. header() leest hem daarna.
bouw_nav()
