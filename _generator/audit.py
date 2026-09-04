#!/usr/bin/env python3
"""Nakijken van de geleverde HTML. Draaien: python3 _generator/audit.py

Zestien controles, alle op nul als het goed is. Ze staan er niet voor de
netheid: elke controle hoort bij een fout die in dit project echt is gemaakt.
De regels waar ze op letten staan in inhoud/BRIEF.md en inhoud/COPY.md.
"""
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(WORTEL)
PAGINAS = sorted(glob.glob("*.html"))

CONTROLES = [
    "dode links", "MADEGRO/cursus", "informeel (je/jij/jouw)", "holle claims",
    "dubbele id", "h1 afwijkend", "kopsprong", "img zonder alt",
    "JSON-LD kapot", "TODO in html", "verboden kop",
    "plaatshouder-logoband (MAG NIET LIVE)", "verzonnen termijn",
    "onvervangen plaatshouder", "oud patroon-woord",
    "ontbrekend bestand", "sitemap/robots",
    "voorbeeldcase (nog te bevestigen)",
]
fouten = {k: [] for k in CONTROLES}

# Claims die niet waar te maken zijn met wat er over Vorma Metaal bekend is.
HOL = [
    r"\bkwaliteit staat bij ons voorop\b", r"\bjarenlange ervaring\b",
    r"\bhoogwaardige kwaliteit\b", r"\bde beste\b", r"\bmarktleider\b",
    r"\buniek in\b", r"\bpassie voor\b", r"\bsamen sterk\b",
    r"\bvakmanschap in metaal\b", r"\bonze mogelijkheden\b", r"\bdaarom vorma\b",
    r"\bscherpe prijzen\b", r"\bnr\.? ?1\b", r"\bnog maar \d+ plek",
    r"\bbeperkt aantal\b", r"\bmeer dan \d+ (?:klanten|tevreden)\b",
    r"\bISO ?9001\b", r"\bVCA\b", r"\bgecertificeerd\b",
    r"\b\d+ ?% (?:tevreden|op tijd)\b", r"\btoonaangevend\b",
    r"\btotaaloplossing\b", r"\bnaar het volgende niveau\b",
    r"\bgrenzeloze mogelijkheden\b", r"\bpartner voor succes\b",
    r"\binnovatieve oplossingen\b",
]

INFORMEEL = [r"\bje\b", r"\bjij\b", r"\bjou\b", r"\bjouw\b", r"\bjullie\b",
             r"\bJe\b", r"\bJij\b", r"\bJouw\b"]

# Formuleringen die nergens als kop mogen staan, ook niet als variant. In
# lopende tekst is "onder een dak" wel toegestaan: daar is het de formulering
# van de bron over een aantoonbaar feit.
VERBODEN_KOP = [
    r"onder (?:&eacute;&eacute;n|één|een|1) dak",
    r"onze mogelijkheden", r"samen sterk", r"vakmanschap in metaal",
    r"daarom vorma", r"kwaliteit voorop", r"met passie", r"uw partner in",
    r"totaaloplossing", r"maatwerk op maat",
]

# Beeldmerken uit de template. Geen van deze bedrijven is opdrachtgever van
# Vorma Metaal; ze tonen is een onware claim.
TEMPLATE_KLANTEN = [
    "Alstom", "Ballast Nedam", "Bilfinger", "Cosun", "Ebert Hera",
    "Electrabel", "GDF Suez", "Freesmij", "GE Vernova", "Huhtamaki",
    "Ivens", "Ooms", "Stork", "TES Industrial",
]

# Termijnen die vormametaal.nl niet noemt. Wat er wel staat: standaardwerk
# wordt automatisch geoffreerd binnen enkele minuten, complex werk binnen korte
# tijd, en de werkplaats is ma-vr 07:30-16:30 open.
TERMIJN = [
    r"(?:antwoord|reageren|reactie|terugbel\w*)[^.<]{0,40}binnen",
    r"binnen \d+ (?:uur|werkdag|werkdagen|dag|dagen|week|weken)",
    r"binnen (?:&eacute;&eacute;n|één|een) (?:uur|werkdag|dag|week)",
    r"levertijd van", r"lever(?:en|ing) binnen",
]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.niveaus, self.imgs, self.links, self.jsonld = [], [], [], [], []
        self.tekst, self.koptekst = [], []
        self._in_ld, self._ld, self._skip, self._kop = False, "", 0, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.niveaus.append(int(tag[1]))
            self._kop = len(self.koptekst)
            self.koptekst.append("")
        if tag == "img":
            self.imgs.append(a.get("alt"))
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld, self._ld = True, ""
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._kop = None
        if tag == "script" and self._in_ld:
            self.jsonld.append(self._ld)
            self._in_ld = False
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if self._in_ld:
            self._ld += d
        elif not self._skip:
            self.tekst.append(d)
            if self._kop is not None:
                self.koptekst[self._kop] += d


def knip(bron, m, marge=55):
    return "…" + " ".join(bron[max(0, m.start() - marge):m.end() + marge].split()) + "…"


bestaand = set(os.listdir("."))
for p in PAGINAS:
    ruw = open(p, encoding="utf-8").read()
    par = Parser()
    par.feed(ruw)
    tekst = " ".join(par.tekst)

    for h in par.links:
        if h.startswith(("http", "mailto:", "tel:", "#", "javascript:")) or not h:
            continue
        doel = h.split("#")[0].split("?")[0]
        if doel and doel not in bestaand and not os.path.exists(doel):
            fouten["dode links"].append(f"{p} -> {h}")

    # Elk lokaal bestand waar de pagina naar wijst moet bestaan. De
    # linkcontrole hierboven kijkt alleen naar <a href>; hier gaan ook
    # afbeeldingen, srcset, video, stylesheets, scripts en de og:image mee.
    # Dat laatste was fout: og:image wees naar een deelafbeelding die niet
    # bestond, dus elke sharepreview was stuk.
    verwijzingen = set()
    for pat in (r'(?:src|href)="([^"]+)"',
                r'content="(?:https?://[^"]*?)?(assets/[^"]+)"',
                r'srcset="([^"]+)"',
                r'url\("([^"]+)"\)'):
        for m in re.finditer(pat, ruw):
            for stuk in m.group(1).split(","):
                adres = stuk.strip().split(" ")[0]
                verwijzingen.add(adres)
    for adres in sorted(verwijzingen):
        if adres.startswith(("http", "mailto:", "tel:", "#", "data:", "javascript:")) or not adres:
            continue
        doel = adres.split("#")[0].split("?")[0]
        if doel and not os.path.exists(doel):
            fouten["ontbrekend bestand"].append(f"{p} -> {doel}")

    for m in re.finditer(r"(?i)madegro|cursus|opleiding|training", ruw):
        fouten["MADEGRO/cursus"].append(f"{p}: {knip(ruw, m)}")

    for pat in INFORMEEL:
        for m in re.finditer(pat, tekst):
            fouten["informeel (je/jij/jouw)"].append(f"{p}: {knip(tekst, m)}")

    for pat in HOL:
        for m in re.finditer(pat, tekst, re.I):
            fouten["holle claims"].append(f"{p}: {knip(tekst, m)}")

    for i in sorted({i for i in par.ids if par.ids.count(i) > 1}):
        fouten["dubbele id"].append(f"{p}: #{i}")

    if par.niveaus.count(1) != 1:
        fouten["h1 afwijkend"].append(f"{p}: {par.niveaus.count(1)} h1")
    vorige = 0
    for niv in par.niveaus:
        if vorige and niv > vorige + 1:
            fouten["kopsprong"].append(f"{p}: h{vorige} -> h{niv}")
        vorige = niv

    for alt in par.imgs:
        if alt is None:
            fouten["img zonder alt"].append(p)

    for ld in par.jsonld:
        try:
            json.loads(ld)
        except Exception as e:
            fouten["JSON-LD kapot"].append(f"{p}: {e}")

    for m in re.finditer(r"TODO|FIXME|LOREM|Lorem ipsum|placeholder", ruw, re.I):
        fouten["TODO in html"].append(f"{p}: {knip(ruw, m)}")

    for kt in par.koptekst:
        k = " ".join(kt.split())
        for pat in VERBODEN_KOP:
            if re.search(pat, k, re.I):
                fouten["verboden kop"].append(f"{p}: {k}")

    # Eén melding per pagina, niet een per logo: anders verdrinkt de rest van
    # het rapport in tweehonderd regels. De band staat er op verzoek als
    # plaatshouder; deze melding hoort pas weg als er echte logo's met
    # toestemming staan, of als de band terug is op sectorenband().
    logos = len(re.findall(r"assets/partners/[a-z-]+\.webp", ruw))
    namen = [n for n in TEMPLATE_KLANTEN if n.lower() in ruw.lower()]
    if logos or namen:
        fouten["plaatshouder-logoband (MAG NIET LIVE)"].append(
            f"{p}: {logos} verwijzingen naar assets/partners/, "
            f"{len(namen)} bedrijfsnamen ({', '.join(namen[:3])}…)")

    for pat in TERMIJN:
        for m in re.finditer(pat, tekst, re.I):
            fragment = knip(tekst, m)
            # "binnen een maand" op het privacybeleid is de wettelijke
            # AVG-termijn voor een inzage- of verwijderverzoek, geen belofte
            # die Vorma Metaal zelf verzint.
            if "maand" in fragment and p == "privacybeleid.html":
                continue
            fouten["verzonnen termijn"].append(f"{p}: {fragment}")

    # De voorbeeldprojecten: anonieme opdrachtgever, geen cijfers, maar wel
    # een bewering dat Vorma dit soort werk maakte. Zolang Vorma dat niet per
    # project bevestigt staat er een label op, en meldt de audit de pagina.
    n_vb = ruw.count('data-plaatshouder="voorbeeldcase"')
    if n_vb:
        fouten["voorbeeldcase (nog te bevestigen)"].append(f"{p}: {n_vb} label(s)")

    for m in re.finditer(r"\{[A-Z_]{3,}\}", ruw):
        fouten["onvervangen plaatshouder"].append(f"{p}: {m.group(0)}")

    for m in re.finditer(r"(?i)gele stral|groene patroon", ruw):
        fouten["oud patroon-woord"].append(f"{p}: {knip(ruw, m)}")


# ---------------------------------------------------------------------------
# sitemap.xml en robots.txt. Die gaan ook live en stonden er nog als die van
# het bronproject in: robots.txt wees naar de sitemap op een ander domein en de
# sitemap somde pagina's op die hier niet bestaan.
# ---------------------------------------------------------------------------
import xml.etree.ElementTree as ET

BASIS = "https://www.vormametaal.nl"

if not os.path.exists("sitemap.xml"):
    fouten["sitemap/robots"].append("sitemap.xml ontbreekt")
else:
    ruw = open("sitemap.xml", encoding="utf-8").read()
    try:
        boom = ET.fromstring(ruw)
        adressen = [e.text for e in boom.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    except Exception as e:
        adressen = []
        fouten["sitemap/robots"].append(f"sitemap.xml is geen geldige XML: {e}")
    in_sitemap = set()
    for a in adressen:
        if not a.startswith(BASIS + "/"):
            fouten["sitemap/robots"].append(f"sitemap: verkeerd domein -> {a}")
            continue
        bestand = a[len(BASIS) + 1:]
        in_sitemap.add(bestand)
        if not os.path.exists(bestand):
            fouten["sitemap/robots"].append(f"sitemap: pagina bestaat niet -> {bestand}")
    for p in PAGINAS:
        if p not in in_sitemap:
            fouten["sitemap/robots"].append(f"sitemap: {p} staat er niet in")

if not os.path.exists("robots.txt"):
    fouten["sitemap/robots"].append("robots.txt ontbreekt")
else:
    r = open("robots.txt", encoding="utf-8").read()
    if f"Sitemap: {BASIS}/sitemap.xml" not in r:
        fouten["sitemap/robots"].append("robots.txt verwijst niet naar de eigen sitemap")
    for m in re.finditer(r"(?i)madegro", r):
        fouten["sitemap/robots"].append(f"robots.txt: {knip(r, m)}")

breed = max(len(k) for k in CONTROLES)
print(f"{len(PAGINAS)} pagina's\n")
for k in CONTROLES:
    v = fouten[k]
    print(f"  {k:<{breed}}  {len(v)}")
    for r in v[:6]:
        print(f"      {r}")
    if len(v) > 6:
        print(f"      … en nog {len(v) - 6}")
totaal = sum(len(v) for v in fouten.values())
print(f"\ntotaal {totaal}")

band = fouten["plaatshouder-logoband (MAG NIET LIVE)"]
if band:
    print()
    print("  " + "=" * 72)
    print("  LET OP: de logoband draagt beeldmerken van bestaande bedrijven")
    print("  (Alstom, Ballast Nedam, Bilfinger, Cosun, Ebert Hera, Electrabel,")
    print("  Freesmij, GE Vernova, Huhtamaki, Ivens, Ooms, Stork, TES).")
    print()
    print("  GEEN VAN DIE BEDRIJVEN IS OPDRACHTGEVER VAN VORMA METAAL.")
    print("  Ze komen uit de template en staan er als plaatshouder.")
    print(f"  Nu op {len(band)} van de {len(PAGINAS)} pagina's.")
    print()
    print("  Live gaan hiermee is een onware claim, richting de bezoeker en")
    print("  richting die dertien bedrijven. Weghalen is een regel: in")
    print("  slotblok() (schil.py) en bouw_home.py logoslider(...) vervangen")
    print("  door sectorenband(...).")
    print("  " + "=" * 72)

sys.exit(1 if totaal else 0)
