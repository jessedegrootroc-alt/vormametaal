# Van MADEGRO-component naar Vorma-inhoud

Uitgangspunt: de MADEGRO-template blijft leidend. Geen nieuwe layouts, geen
nieuwe componenten, dezelfde sectievolgorde. Alleen de inhoud verandert.

## Homepage: dezelfde twaalf secties, in dezelfde volgorde

| # | id (blijft) | MADEGRO-component | krijgt Vorma-inhoud |
|---|---|---|---|
| 01 | `s01-introductie` | hero: beeld + kop + twee knoppen | &ldquo;Wij geven vorm aan uw metaal&rdquo; + Offerte aanvragen / Wat wij doen |
| 02 | `s02-wat-we-doen` | `content-text-side-cta` | wat Vorma doet: metaalbewerking van aanvraag tot eindproduct |
| 03 | `s03-hoe-we-werken` | `content-text-side-visual` | **de vijf stappen** van aanvraag tot levering |
| 04 | `s04-diensten` | 3&times; `dienstkaart` in `col-lg-4` | **de acht bewerkingen** &mdash; zelfde kaart, acht in plaats van drie |
| 05 | `s05-projecten` | `cases-grid`, rijen met beeld + tekst | **materialen**: staal, RVS en aluminium als drie rijen |
| 06 | `s06-usps` | drie cijfers met tellers | **echte cijfers**: 22 jaar, 8 bewerkingen, 3 materialen |
| 07 | `s07-cursusaanbod` | `panel-row--4` | **waarom Vorma Metaal** &mdash; de zes punten in hetzelfde paneel |
| 08 | `s08-testimonials` | `quoteslider`, drie dia's | **wat u van ons kunt verwachten** &mdash; drie procesafspraken, op naam van Vorma zelf |
| 09 | `s09-faq` | accordeon | **de zeven echte FAQ-vragen** van vormametaal.nl |
| 10 | `s10-martin` | medewerkersband met portretslot | **over Vorma Metaal**: ontstaan uit Tentije, 2004 in Goor |
| 11 | `s11-partners` | `logo-slider`, doorlopende band | **sectorenband**: de tien echte sectoren als tekstitems in dezelfde band |
| 12 | `s12-contact` | `cta-slot` | offerte aanvragen |

### Waarom niet één-op-één, waar dat niet kon

- **`s04-diensten` had drie kaarten, Vorma heeft acht bewerkingen.** Dezelfde
  kaart en hetzelfde grid; het grid is `col-lg-4`, dus acht kaarten vullen
  3&nbsp;+&nbsp;3&nbsp;+&nbsp;2. Geen nieuw component.
- **`s05-projecten` was een cases-rij.** Vorma Metaal heeft geen cases of
  projecten op zijn site en die verzinnen mag niet. De layout (rij met beeld
  links en tekst rechts) past precies op de drie materialen, met de
  voorbeeldkwaliteiten als opsomming. De sectie blijft dus staan met andere
  inhoud in plaats van dat hij verdwijnt.
- **`s06-usps` had 24 jaar / 18 klanten / 6 sectoren.** Van die drie is voor
  Vorma alleen een jarental bekend (22). De andere twee worden 8 bewerkingen en
  3 materialen: allebei te controleren op de eigen site. Geen klantaantallen,
  want die zijn nergens vermeld.
- **`s07-cursusaanbod` was het cursusgrid.** Cursussen verdwijnen helemaal. De
  vier panelen worden de zes punten onder &ldquo;Waarom Vorma Metaal&rdquo;;
  `panel-row--4` verwerkt zes items zonder aanpassing.
- **`s08-testimonials` had drie klantcitaten met naam, functie en logo.** Vorma
  Metaal heeft geen testimonials en verzinnen mag niet. De slider blijft, maar
  de dia's worden drie procesafspraken die wél op de site staan (vrijblijvende
  offerte, maakbaarheidscontrole, levering of afhalen), op naam van Vorma
  Metaal zelf. Dat is een aantoonbaar vertrouwenselement in plaats van een
  fictief citaat.
- **`s10-martin` was een portret met biografie.** Van Vorma is geen
  medewerkersfoto beschikbaar. Het beeldslot houdt zijn plek en verhouding en
  krijgt een werkplaatsfoto; de tekst wordt het herkomstverhaal (Tentije, 2004,
  Goor, dezelfde werkplaats en hetzelfde team).
- **`s11-partners` was een logoband van opdrachtgevers.** In
  `assets/partners/` staan beeldmerken van bestaande bedrijven (Alstom, Stork,
  Ballast Nedam en meer) die bij de vorige eigenaar van dit sjabloon horen en
  **geen** opdrachtgever van Vorma zijn. Op vormametaal.nl staan geen
  klantlogo&rsquo;s. De band blijft met dezelfde animatie, maar draagt de tien
  sectoren als tekst.

## Pagina's

| MADEGRO | wordt | template die hergebruikt wordt |
|---|---|---|
| `index.html` | `index.html` | homepage |
| `veilig-gedrag` `ehs-rie` `safety-checks` | `dienst-lasersnijden` t/m `dienst-cnc-verspanen` (8) | het dienstsjabloon, ongewijzigd |
| `cursusaanbod.html` | `diensten.html` | het overzichtssjabloon |
| `cursus-*.html` (4) | **weg** | &mdash; |
| `cases.html` + `case-*.html` (6) | **weg**; de layout leeft door op de homepage voor de materialen | &mdash; |
| &mdash; | `werkwijze.html` | het cursussjabloon (dat heeft de `.trap` met treden) |
| &mdash; | `materialen.html` | het overzichtssjabloon |
| &mdash; | `voor-wie.html` | het overzichtssjabloon |
| `over-ons.html` | `over-vorma-metaal.html` | ongewijzigd |
| `contact.html` | `contact.html` | ongewijzigd |
| `privacybeleid.html` `cookies.html` | idem | tekstpagina |

## Navigatie

Zelfde component, zelfde dropdowngedrag. Alleen inhoud en links:

Home &middot; Diensten (uitklap met de acht) &middot; Werkwijze &middot;
Materialen &middot; Voor wie &middot; Over Vorma Metaal &middot; Contact

## Wat niet verandert

Palet (MADEGRO-groen en -geel), typografie, grids, containerbreedtes,
sectiespacing, knopstijlen, kaarten, randen, radii, animaties, hover states,
navigatiegedrag, footer-layout, responsive gedrag.
