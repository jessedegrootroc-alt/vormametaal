# Herkomst van de foto's

## De beelden die de site nu gebruikt

Allemaal stilstaande beeldjes uit `assets/video/hero-werkplaats.mp4`, de
herofilm. Daarmee komen alle foto's uit dezelfde reeks: dezelfde hal, dezelfde
lichtval, dezelfde kleuren. En ze laten de bewerking zien die erbij staat.

| bestand | uit de film op | wat er te zien is |
|---|---|---|
| `werkplaats-1130/2260.webp` | 0,0 s | de lasersnijmachine in de hal, wijd opgenomen |
| `lasersnijden-640/1280.webp` | 1,4 s | de snijkop boven de plaat, met de uitgesneden delen eromheen |
| `buislasersnijden-640/1280.webp` | 2,9 s | een koker in de spankop, met een regen van vonken |
| `kanten-640/1130.webp` | 4,2 s | een operator die een plaat in de kantbank zet |
| `lassen-640/1280.webp` | 5,9 s | de lasboog op de verbinding tussen een koker en een plaat |
| `verspanen-640/1280.webp` | 7,6 s | de freeskop met koelvloeistof en wegspringende spanen |
| `productiehal-640/1280.webp` | 9,2 s | de werkplaats met medewerkers aan gesneden plaatdelen |

Omgezet met `cwebp -q 90 -m 6`, na verkleinen met Lanczos.

`werkplaats` is 1130 breed en niet 1280, en `kanten` ook: in de kantbankscene
staat op de jas van de operator het beeldmerk van een ander bedrijf, tussen
x=1136 en de rechterrand. De film is daarom op 1130 gesneden; zie
`assets/video/HERKOMST.md` voor de afweging.

## Waarom er geen grotere maat in de srcset staat

De bron is 1280x720. Er staat bewust niets van 1920 of 2400 bij: dan zou de
browser een opgeschaald beeld ophalen dat scherper doet dan het is. De
dienst-hero is de helft van het scherm breed, dus op een gewoon scherm tot
2560px is 1280 genoeg; op een scherm met dubbele pixeldichtheid is hij niet
helemaal scherp. Dat is de grens van deze bron en niet met verkleinen of
comprimeren op te lossen.

De brede baan op de homepage toont `productiehal` tot 70vw. Bij het beeld dat
hier eerder stond was dat 1024 breed op een vak van ruim 1000px; nu is het
1280.

## Wat er eerder stond

De foto's van de template: een bouwplaats met torenkraan, een containerschip
aan een containerterminal, een industriële transportbrug, een vrachtwagen op
een dijkweg en een vergadering. Ze stonden onder CC0 of in het publiek domein
en mochten commercieel gebruikt worden.

Ze zeiden niets over metaalbewerking, en op sommige plekken werd dat pijnlijk:
oppervlaktebehandeling had een containerschip en CNC-verspanen een torenkraan.
De bestanden staan nog in deze map maar zijn uit de repo gehouden; geen pagina
gebruikt ze.

Ook uit de repo: `martin*`, foto's van een herkenbaar persoon uit het
bronproject die niets met Vorma Metaal te maken heeft.

## Twee dingen om na te gaan voor het live gaat

1. **De licentie van de film is niet bekend**, en daarmee die van deze foto's
   ook niet. Zie `assets/video/HERKOMST.md`. De oude foto's hadden een heldere
   CC0-status; dat is met deze ruil ingeleverd voor beelden die wel over het
   onderwerp gaan.
2. **Het is niet de werkplaats van Vorma Metaal.** De machines, de hal en de
   mensen zijn niet die aan Dammaten 14 in Goor. Eigen beeld is beter, en dan
   kan de resolutie ook hoger dan 720p.
