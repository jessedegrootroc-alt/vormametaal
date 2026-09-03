# Herkomst van de video

## hero-werkplaats.mp4 — de film die nu in de hero staat

Aangeleverd door Jesse op 3 september 2026, als
`Manufacturing_video_creation_prompt_202609031426.mp4` (1280x720, 24 fps,
10,0 s, 4,9 MB, met geluidsspoor).

Zes taferelen, waarvan vijf een bewerking van Vorma Metaal zijn:

| van | tot | wat |
|---|---|---|
| 0,0 s | 1,6 s | lasersnijden: snijtafel met uitgesneden delen in plaat |
| 1,6 s | 3,25 s | buislasersnijden: koker wordt op maat gesneden, vonken |
| 3,25 s | 5,13 s | kanten: kantbank met een operator ervoor |
| 5,13 s | 6,9 s | lassen: lasboog op een koker-plaatverbinding |
| 6,9 s | 8,38 s | CNC-verspanen: freeskop met koelvloeistof |
| 8,38 s | 10,0 s | haloverzicht met twee medewerkers aan werkbanken |

Bewerkt voor het web:

- **geluid eruit** (`-an`), want hij speelt als achtergrond en heeft geen bediening;
- opnieuw gecodeerd met H.264, crf 28, `-movflags +faststart`;
- **rechterrand van 150px eraf** (`crop=1130:720:0:0`), zie hieronder;
- **afgeknipt op 8,375 s**, zie hieronder.

Samen brengt dat 4,9 MB terug naar 1,04 MB.

Het stilstaande beeld `assets/foto/werkplaats-1130.webp` en `-2260.webp` is het
eerste beeldje van deze film, zodat de foto en de film op elkaar aansluiten. De
maten zijn 1x en 2x het videobeeld en niet de 2400 van de andere foto's: dan
staat er geen opgeschaald beeld in de srcset dat scherper doet dan het is.

## Waarom de rechterrand eraf is

In de kantbankscene staat een operator met de rug naar de camera, en op zijn jas
staat een leesbaar beeldmerk van een ander bedrijf: een oranje rond teken met
een woordmerk ernaast, tussen x=1136 en de rechterrand. Dat is een herkenbare
partij die daar niet om gevraagd heeft, en in de hero van Vorma Metaal wekt het
de indruk dat die persoon voor Vorma werkt.

Twee andere routes zijn geprobeerd en afgekeurd:

- **`boxblur` op dat vak**, alleen tussen 3,20 en 5,16 s. Werkt, maar laat een
  hardgerand vlekje op de jas achter dat als een storing leest.
- **`delogo` op dat vak.** Haalt het merk weg maar smeert verticaal uit over de
  schouder heen, tot in de achtergrond.

Wegsnijden is het enige dat niets achterlaat. De koker-, las- en freesscenes zijn
gecentreerd, dus die verliezen niets van belang; de operator staat nu tot aan de
rand in beeld, wat als een gewone kaderrand leest.

## Waarom hij op 8,375 s is afgeknipt

Het haloverzicht daarna heeft uitgeblazen witte ruiten: in het vak van het
bovenkopje staan pixels op zuiver wit, en wit op wit is 1,00:1. Om dat met de
sluier te ondervangen was 0,88 dekking onderin nodig, en dan is er van het beeld
niets meer over.

Alle vijf de bewerkingen zitten voor 8,375 s. Wat wegvalt is het minst
specifieke tafereel. De lasboog in scene vier is nog steeds het felste punt van
de film (1,15:1 onbedekt); daarop is de sluier in `index.css` afgestemd.

## Twee dingen om na te gaan voor het live gaat

1. **De licentie is niet bekend.** Het bestand kwam zonder bron mee. De
   bestandsnaam wijst op materiaal uit een generator; ga na wat de voorwaarden
   zijn en of het commercieel gebruikt mag worden.
2. **Het is niet de werkplaats van Vorma Metaal.** De machines, de hal en de
   mensen zijn niet die aan Dammaten 14 in Goor. De film claimt dat ook nergens
   in tekst, maar wie de hal kent ziet het verschil. Liever eigen beeld.

## hero-logistiek.mp4 — ongebruikt

De film uit de template: een vrachtwagen op een dijkweg, een lege loods, een
containerterminal en een containerschip. Zegt niets over metaalbewerking en
staat op geen enkele pagina meer. Het bijbehorende stilstaande beeld is
`assets/foto/logistiek-1200.webp` en `-2400.webp`.

Ook daar stond een aantekening bij die nog geldt als hij ooit terugkomt: op de
vrachtwagen staat een belettering ("A6"), en als dat een bestaand bedrijf is, is
dat een herkenbare partij in beeld die daar niet om gevraagd heeft.
