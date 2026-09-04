# Vorma Metaal: website

Statische site voor Vorma Metaal, Dammaten 14 in Goor: HTML, CSS en vanilla
JavaScript, geen build-stap en geen npm-afhankelijkheden. Van een CDN komen
alleen GSAP (met de plug-ins ScrollTrigger en ScrollSmoother) en Barba.js:
samen doen die de pagina-overgangen en het vloeiende scrollen.

De HTML wordt niet met de hand bijgehouden. Alle 20 pagina's worden gegenereerd
door de scripts in `_generator/`; de teksten staan in `_generator/inhoud/`. Wie
een tekst wijzigt, wijzigt daar het Python-bestand en bouwt opnieuw. Een
wijziging rechtstreeks in een `.html` gaat bij de volgende build verloren.

## Lokaal draaien

    node _generator/server.js 5501

Dan staat de site op `http://localhost:5501`. De server doet brotli en gzip,
ETags en Range-verzoeken, en zet `Cache-Control: no-cache` op afbeeldingen,
zodat een vervangen bestand met dezelfde naam niet uit de cache blijft komen.
Zonder poortargument draait hij op 5500.

Alle links zijn relatief, dus de map kan ook zonder server of vanuit een submap.

## Opnieuw bouwen

    python3 _generator/bouw_alles.py

Dat draait de bouwers achter elkaar en schrijft alle 20 pagina's, plus sitemap.xml en robots.txt.

## Publiceren

Statisch, werkt zonder configuratie op GitHub Pages, Netlify, Vercel of
Cloudflare Pages: wijs de host naar deze map. Zet daarna in `sitemap.xml`,
`robots.txt` en de `canonical`- en Open Graph-tags het juiste domein; `BASIS` in
`_generator/schil.py` is het adres dat de generator gebruikt.

## Structuur

```
_generator/schil.py         de gedeelde paginaschil: head, header, nav, voet
_generator/bouw_home.py     de homepage, twaalf secties
_generator/bouw_service.py  het dienstsjabloon, draait alle acht dienstpagina's
_generator/bouw_rest.py     diensten, werkwijze, voor wie, over ons
_generator/bouw_cases.py    de projectenpagina en de drie voorbeeldprojecten
_generator/bouw_contact.py  contact, privacybeleid, cookies
_generator/bouw_zoekmachine.py  sitemap.xml en robots.txt
_generator/bouw_alles.py    draait alles
_generator/server.js        de ontwikkelserver
_generator/inhoud/          de teksten, een module per pagina

_generator/inhoud/BRIEF.md    de enige bron voor feiten over Vorma Metaal
_generator/inhoud/COPY.md     de schrijfnorm: de vier toetsen en de koppenregels
_generator/inhoud/MAPPING.md  welk component van de template welke inhoud draagt

index.html                  Home
dienst-lasersnijden.html    ┐
dienst-buislasersnijden.html│
dienst-kanten.html          │
dienst-lassen.html          ├ acht dienstpagina's, één sectieskelet
dienst-nabewerking.html     │
dienst-assemblage.html      │
dienst-oppervlaktebehandeling.html
dienst-cnc-verspanen.html   ┘
diensten.html  werkwijze.html  voor-wie.html  over-vorma-metaal.html
cases.html                  ┐
case-liftdeuren.html        ├ projecten: een overzicht en drie voorbeeldprojecten,
case-roltrappen.html        │ gelabeld als "nog te bevestigen" (zie CASES in schil.py)
case-draaideuren.html       ┘
contact.html
privacybeleid.html  cookies.html

STYLEGUIDE.md           het ontwerpsysteem en waar deze site afwijkt
SECTIONS.md             het sectieskelet dat de pagina's delen
CONTENT-TODO.md         alles wat nog aangeleverd moet worden

styleguide.css          tokens en componenten, geldt overal
index.css  service.css  overzicht.css  contact.css  over-ons.css  tekstpagina.css
cookiebalk.css  transitions.css
cases.css               de projectenpagina en de casepagina's

site.js                 header, mobiel paneel, accordeons, op elke pagina
contactformulier.js     het contactformulier, één keer
index.js                alleen de tellers op de homepage
smooth-scroll.js        vloeiend scrollen met GSAP ScrollSmoother
page-transitions.js     Barba.js + GSAP
cookiebalk.js  analytics.js
cases.js                ongebruikt, geen pagina laadt hem nog

assets/                 logo, patronen, foto's, fonts, favicons, deelafbeelding
sitemap.xml  robots.txt
```

## Werken aan deze site

- **Teksten wijzig je in `_generator/inhoud/`, niet in de HTML.** Daarna
  `python3 _generator/bouw_alles.py`.
- **Verzin geen feiten.** `_generator/inhoud/BRIEF.md` is de enige bron. Staat
  een dienst, materiaal, cijfer, certificering, klantnaam, levertijd of
  technische mogelijkheid daar niet in, dan hoort hij niet op de site. Is een
  component niet met echte inhoud te vullen, verander dan het component; vul
  hem niet met een verzinsel.
- **Aanspreekvorm is &ldquo;u&rdquo;.** Nooit &ldquo;je&rdquo;.
- Voor koppen en CTA's: `_generator/inhoud/COPY.md`.
- De layout is gegeven. Deze site is opgebouwd op een bestaande template; de
  inhoud past zich aan het ontwerp aan, niet omgekeerd. Grids, containerbreedtes,
  spacing, typografie, knoppen, kaarten, animaties en de sectievolgorde blijven
  zoals ze zijn.
- Nieuwe kleuren, maten of afstanden komen uit de tokens in `styleguide.css`.
- In `assets/partners/` staan beeldmerken van bestaande bedrijven. Die horen bij
  de template en zijn **geen** opdrachtgever van Vorma Metaal; ze op deze site
  zetten is een onware claim.
- Het contactformulier verstuurt nog niets: zet het endpoint in
  `contactformulier.js`.
- Statistieken laden pas na toestemming en alleen als er een meet-ID staat in
  `analytics.js`. Dat veld is nu bewust leeg.
