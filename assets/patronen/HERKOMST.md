# assets/patronen: het merkpatroon

Aangeleverd door Jesse, versie 3 op 2 september 2026: een navy rasterverloop in
plaats van het groene patroon met de gele stralen. De PNG's staan onveranderd in
`bron/`; de vorige versies liggen ernaast in `bron/v2-groen/` en `bron/v1/`.

| bron | maat | waarvoor |
|---|---|---|
| `CTA.SECTION.BACKGROUND.png` | 2880 x 760 (3,79:1) | achtergrond van het contactvlak |
| `HERO.SECTION.png` | 1440 x 940 (1,53:1) | hero vanaf 768px |
| `HERO.SECTION2.png` | 1440 x 1440 (1:1) | hero tot 767px, cover snijdt bij |

De aangeleverde bestanden heten `grid-gradient-153557-<maat>.png` en staan
daarnaast nog los in deze map. Ze zijn onder de bovenstaande namen in `bron/`
gezet omdat de omzetting op die namen werkt.

Omgezet naar WebP met `cwebp -q 88 -m 6`, na verkleinen met Lanczos. Het zijn
vlakke verlopen met een fijn raster, dus dat comprimeert extreem goed: samen
69 kB tegen 3,3 MB als PNG. Dat is bijna de helft van de 125 kB die het groene
patroon kostte.

## De uitsnede staat in de stylesheet, niet in het bestand

Beide herobestanden worden onveranderd geexporteerd; hoe groot het vak is
bepaalt de stylesheet. Reden: de vaste balk ligt over de bovenkant van de
pagina, en die is een vast aantal pixels hoog terwijl het vak meeschaalt met de
breedte. Een vaste uitsnede in het bestand kan dat niet opvangen.

Op een telefoon is het vak daarom 7:3 (de verhouding uit de referentie, gemeten
over vier schermafdrukken: 2,27, 2,29, 2,29 en 2,42) **plus** de hoogte van de
balk. Onder de balk staat dan precies 7:3 aan patroon. Het bronbestand is
vierkant zodat `cover` verticaal wat over heeft.

Vanaf 768px is de hero een balkhoogte hoger dan hij was, zodat er onder de balk
net zoveel patroon staat als bedoeld: 1,65:1 op 1440px.

## Contrast in het contactvlak

Daar staat witte tekst gecentreerd over het patroon, zonder waas ertussen. Het
navy verloop is over vrijwel het hele vlak donker: de mediaan geeft wit 12,5:1
en de lichtste pixel van het hele bestand (`#7597b7`, in de band bovenin) nog
3,06:1. Gemeten in de browser op de lichtste vijf procent van elk tekstvak, bij
375, 768, 997, 1440 en 1920px breed:

| onderdeel | haalt | nodig | |
|---|---|---|---|
| label (11px) | 3,39 - 3,81:1 | 4,5:1 | valt door de lichte band bovenin |
| kop (48px) | 5,91 - 8,01:1 | 3,0:1 | haalt de eis ruim |
| introtekst | 14,16 - 15,29:1 | 4,5:1 | haalt de eis ruim |

Bij het groene patroon zakten alle drie: label 1,76:1, kop 2,03:1 en introtekst
3,15:1. Daar liepen de gele stralen precies door het midden; de lichtste pixel
was `#f8f242` en gaf wit 1,17:1.

26% waas van het diepste navy (`#0e2640`) is genoeg om elke pixel van het
patroon op 4,5:1 te krijgen, dus bij welke uitsnede en welke tekstpositie dan
ook; met het diepste groen van het palet (`#014144`) is 32% nodig. Was 36% bij
het groene patroon. De regel staat als commentaar bij `.cta-slot__hoofd` in
`styleguide.css`. Zonder waas is de kleinste oplossing het label verplaatsen:
kop en introtekst staan al goed.

In de hero speelt dit niet: daar staat de h1 in het grijze vlak ernaast, niet
over het patroon.
