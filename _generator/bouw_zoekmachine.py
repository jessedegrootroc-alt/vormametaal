# -*- coding: utf-8 -*-
"""Schrijft sitemap.xml en robots.txt.

   Deze twee stonden er nog als die van het bronproject in: robots.txt wees
   naar de sitemap op madegro.nl, en sitemap.xml somde casepagina's op die hier
   niet bestaan, op een domein dat niet van Vorma Metaal is. Beide bestanden
   gaan live, dus dat is geen kleinigheid.

   Ze worden nu gegenereerd en niet met de hand bijgehouden: de lijst pagina's
   komt uit de map zelf en het domein uit BASIS in schil.py, dus ze kunnen niet
   meer uit de pas lopen met de site.

   Geen lastmod. Die zou bij elke build veranderen omdat hij van de
   bestandsdatum komt, en dan zegt hij niets meer. Het veld is optioneel."""
import pathlib
import sys

HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
UIT = HIER.parent

from schil import BASIS, SERVICES  # noqa: E402

# Hoe belangrijk een pagina is, en hoe vaak hij verandert. De dienstpagina's
# staan hoger dan de overige omdat daar de aanvraag vandaan komt.
PRIORITEIT = {
    "index.html": ("weekly", "1.0"),
    "diensten.html": ("monthly", "0.9"),
    "contact.html": ("monthly", "0.9"),
    "werkwijze.html": ("monthly", "0.7"),
    "materialen.html": ("monthly", "0.7"),
    "voor-wie.html": ("monthly", "0.7"),
    "over-vorma-metaal.html": ("yearly", "0.6"),
    "privacybeleid.html": ("yearly", "0.3"),
    "cookies.html": ("yearly", "0.3"),
}
for bestand, *_rest in SERVICES:
    PRIORITEIT[bestand] = ("monthly", "0.8")


def paginas():
    """Elke .html in de hoofdmap, in de volgorde van PRIORITEIT. Een pagina die
       daar niet in staat komt achteraan met een standaardwaarde, zodat een
       nieuwe pagina nooit stil uit de sitemap valt."""
    aanwezig = sorted(p.name for p in UIT.glob("*.html"))
    volgorde = [b for b in PRIORITEIT if b in aanwezig]
    rest = [b for b in aanwezig if b not in PRIORITEIT]
    for b in rest:
        print(f"   LET OP: {b} staat niet in PRIORITEIT, krijgt monthly/0.5")
    return volgorde + rest


def bouw_sitemap():
    regels = []
    for bestand in paginas():
        wissel, prio = PRIORITEIT.get(bestand, ("monthly", "0.5"))
        regels.append("  <url>\n"
                      f"    <loc>{BASIS}/{bestand}</loc>\n"
                      f"    <changefreq>{wissel}</changefreq>\n"
                      f"    <priority>{prio}</priority>\n"
                      "  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(regels) + "\n</urlset>\n")
    (UIT / "sitemap.xml").write_text(xml, encoding="utf-8")
    return len(regels)


def bouw_robots():
    tekst = ("User-agent: *\n"
             "Allow: /\n"
             "\n"
             f"Sitemap: {BASIS}/sitemap.xml\n")
    (UIT / "robots.txt").write_text(tekst, encoding="utf-8")


if __name__ == "__main__":
    n = bouw_sitemap()
    bouw_robots()
    print(f"sitemap.xml geschreven ({n} pagina's) en robots.txt geschreven")
