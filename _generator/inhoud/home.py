# -*- coding: utf-8 -*-
"""Inhoud van de homepage. Het skelet staat in bouw_home.py.

Volgorde van de secties (4 september 2026, op verzoek herschikt):

  01 hero              wat doet Vorma, kan ik hier mijn onderdeel laten maken
  02 logoband          voor welke bedrijven (PLAATSHOUDER, zie schil.py)
  03 proces            hoe werkt aanvragen
  04 bewerkingen       wat kan er gemaakt en bewerkt worden
  05 waarom Vorma      waarom is de samenwerking praktisch
  06 materialen        welke materialen
  07 projecten         wat is er gemaakt (PLAATSHOUDER, zie inhoud/cases.py)
  08 cijfers           hoeveel ervaring en breedte
  09 offerte           hoe snel weet ik wat het kost (het statementblok)
  10 team              wie zit erachter
  11 testimonials      hoe ervaren opdrachtgevers het (PLAATSHOUDER)
  12 faq               welke vragen zijn er nog
  13 contact           wat is de volgende stap

Elke sectie beantwoordt een eigen vraag; een feit staat in de lopende tekst
op een plek. De FAQ mag herhalen, dat is waar hij voor is.

Enige bron voor de feiten: inhoud/BRIEF.md. Wat hier bewust NIET staat, omdat
het nergens in de bron staat: machines, plaatdiktes, toleranties,
certificeringen, levertijden, garanties, capaciteit, aantallen klanten of
medewerkers, prototypes.

Eigen huis versus geregeld: lasersnijden, buislasersnijden, kanten, lassen,
nabewerking en CNC-verspanen gebeuren in eigen huis; assemblage loopt via
zusterbedrijf Tentije Industri&euml;le Automatisering B.V.;
oppervlaktebehandeling wordt uitbesteed maar door Vorma geregeld. Nooit
omdraaien.

Waar de <p>-tags horen: bouw_home.py zet offerte_tekst, diensten_tekst,
waarom_intro, projecten_intro en materialen_intro zelf in een <p>, dus die zijn
platte tekst. hero_intro, werkwijze_intro en over_tekst komen in een div met de
klasse article-body en dragen hun eigen <p>-alinea's.

Geen gedachtestreepje (em dash) in de copy; de audit controleert erop.
"""

HOME = {
    "titel": "Vorma Metaal | Van CAD-bestand naar afgewerkt metalen onderdeel",

    # Meta description, 150 tekens: plaats, wat er gemaakt wordt, de
    # bewerkingen die een inkoper intypt, en de eerste stap.
    "omschrijving": "Vorma Metaal in Goor maakt plaatwerk, buiswerk, verspaande delen en samenstellingen op tekening. Lasersnijden, kanten, lassen en CNC-verspanen vanuit één aanvraag.",

    # ---------------------------------------------------------------- 01 hero
    # Vraag: wat doet Vorma en kan ik hier mijn onderdeel laten maken. De kop
    # zegt wat er in en wat eruit gaat; de intro noemt de vier soorten werk en
    # het combineren van bewerkingen. De hero vat niet de hele site samen:
    # materialen, termijnen en herkomst komen verderop.
    "hero_eyebrow": "Maatwerk in metaal",
    "hero_h1": "Van CAD-bestand naar afgewerkt metalen onderdeel",
    "hero_intro": "<p>Laat plaatwerk, buis- en profielwerk, verspaande delen en complete samenstellingen produceren vanuit &eacute;&eacute;n aanvraag. Snijden, kanten, lassen, verspanen en afwerken worden gecombineerd binnen dezelfde opdracht.</p>\n          <p>Voor inkopers, engineers en werkvoorbereiders die metaalwerk op tekening nodig hebben. Uw aanvraag begint bij het CAD-bestand dat u al heeft.</p>",
    "hero_knop1": "Vraag een offerte aan",
    "hero_knop2": "Bekijk de bewerkingen",

    # ------------------------------------------------------------ 09 offerte
    # Het statementblok (een tekstslot, geen kop). Stond direct onder de hero
    # als "wat wij doen"; het staat nu na de cijfers en beantwoordt de vraag
    # hoe snel iemand weet wat zijn onderdeel kost. De twee eerste sleutels
    # blijven staan voor de sleutelverzameling; dit component heeft geen
    # kopslot en bouw_home.py rendert ze niet.
    "offerte_eyebrow": "Offerte",
    "offerte_kop": "Snel inzicht in de kosten van uw onderdeel",
    "offerte_tekst": "Snel inzicht in de kosten van uw onderdeel: standaardwerk calculeert het portaal automatisch, zodat uw offerte binnen enkele minuten online staat. Complexe aanvragen en bijzondere materialen bekijken wij persoonlijk, voordat er iets geproduceerd wordt.",

    # ----------------------------------------------------------- 03 proces
    # Vraag: hoe werkt het als ik iets wil laten maken. Dit component is tekst
    # met beeld; de vijf stappen staan als treden op werkwijze.html, waar de
    # knop heen gaat. De eerste alinea loopt daarom de vijf stappen in een
    # zin af, met de bestandsformaten en het akkoord erin. De tweede haalt de
    # twee onzekerheden weg: moet ik natekenen, en wat als iets niet kan.
    # De offertetermijn staat hier bewust NIET; die is van sectie 09.
    "werkwijze_eyebrow": "Werkwijze",
    "werkwijze_kop": "Zo verloopt uw aanvraag, in vijf stappen",
    "werkwijze_intro": "<p>U levert uw bestand aan (STEP, DXF of DWG, eventueel met een PDF-tekening). Wij controleren de maakbaarheid, u ontvangt een vrijblijvende offerte en de productie start pas na uw akkoord. Daarna wordt geleverd, of uw werk staat klaar om af te halen.</p>\n              <p>Natekenen is niet nodig: het portaal leest uw bestand direct in. Is een detail niet te maken zoals getekend, dan hoort u dat bij de controle, voordat er een offerte uitgaat.</p>",
    "werkwijze_knop": "Bekijk de werkwijze",

    # De vijf stappen, letterlijk uit BRIEF.md. Op de homepage rendert
    # bouw_home.py ze niet; ze staan op werkwijze.html.
    "stappen": [
        ("Aanvraag",
         "Upload uw CAD-bestanden, eventueel met een PDF. Wij nemen hem in behandeling."),
        ("Controle",
         "Wij controleren of uw aanvraag maakbaar is. Bij een complexe opdracht stemmen wij met u af."),
        ("Offerte",
         "U ontvangt een duidelijke, vrijblijvende offerte. Het werk start pas na uw akkoord."),
        ("Productie",
         "Wij maken uw producten in onze werkplaats: van lasersnijden en kanten tot verspanen, lassen en de afgesproken nabewerking."),
        ("Levering of afhalen",
         "Uw producten worden geleverd, of staan klaar om af te halen."),
    ],

    # ------------------------------------------------------- 04 bewerkingen
    # Vraag: kunnen jullie het werk uitvoeren dat mijn onderdeel nodig heeft.
    # De kop noemt het aantal en het combineren; de leadtekst zegt welke zes
    # in eigen huis gebeuren en welke twee geregeld worden. Dat onderscheid
    # staat alleen hier en in de FAQ.
    "diensten_eyebrow": "Bewerkingen",
    "diensten_kop": "Acht bewerkingen, te combineren in &eacute;&eacute;n opdracht",
    "diensten_tekst": "Zes bewerkingen gebeuren in onze eigen werkplaats in Goor. Assemblage loopt via zusterbedrijf Tentije en poedercoaten via een coater; beide staan op dezelfde aanvraag, zodat u er geen tweede leverancier voor hoeft aan te sturen.",

    # Een regel per kaart, geschreven vanuit wat het de opdrachtgever oplevert.
    # De kaart drukt erboven al de korte typering uit SERVICES af.
    # Volgorde vast: lasersnijden, buislasersnijden, kanten, lassen,
    # nabewerking, assemblage, oppervlaktebehandeling, CNC-verspanen.
    "diensten_intros": [
        "Plaatdelen rechtstreeks uit uw CAD-bestand gesneden, in staal, RVS of aluminium. Natekenen is niet nodig.",
        "Buis en profiel op maat gesneden, met de uitsparingen en gaten in dezelfde gang erin.",
        "Gesneden plaatdelen gezet volgens de vorm en maatvoering van uw tekening, in dezelfde werkplaats.",
        "Losse delen samengevoegd tot &eacute;&eacute;n samenstelling, met TIG, MIG of laserlassen, passend bij het werk.",
        "Afbramen, boren, tappen en verzinken binnen dezelfde opdracht, zodat uw onderdeel montageklaar is.",
        "Complete samenstellingen laten bouwen via zusterbedrijf Tentije, in dezelfde werkplaats en met hetzelfde team.",
        "Poedercoaten geregeld binnen dezelfde opdracht. U stuurt zelf geen coater aan en krijgt uw onderdeel afgewerkt terug.",
        "Draaien en frezen voor delen die verspanende bewerkingen nodig hebben, uit dezelfde aanvraag als uw plaatwerk.",
    ],

    # ------------------------------------------------------ 05 waarom Vorma
    # Vraag: waarom is de samenwerking praktisch. Zes kaarten, elk vanuit wat
    # het de opdrachtgever scheelt. De knop onder de kop gaat naar de
    # aanvraag: wie hier overtuigd is, hoeft niet terug naar de bewerkingen
    # die direct hierboven staan.
    "waarom_eyebrow": "Waarom Vorma Metaal",
    "waarom_kop": "Zes redenen om uw metaalwerk hier aan te vragen",
    "waarom_intro": "Minder leveranciers aansturen, geen mailwisseling over versies en een offerte die navolgbaar blijft. Dat is wat de werkwijze u in de praktijk oplevert.",
    "waarom_knop": "Start uw aanvraag",

    # Titels van 16 tot 27 tekens, teksten van 90 tot 125 tekens; dat past op
    # de panelen. Geen prototypes: die staan niet in de bron.
    "waarom": [
        ("22 jaar technische ervaring",
         "Opgebouwd in machinebouw en industri&euml;le automatisering. Uw tekening wordt beoordeeld op wat er in de praktijk te maken is."),
        ("Persoonlijk contact",
         "Uw vragen bespreekt u met mensen die zelf weten hoe een onderdeel geproduceerd wordt, niet met een tussenlaag."),
        ("Online aanvragen",
         "Bestanden, aanvraaggegevens en versies staan op &eacute;&eacute;n plek in het portaal, in plaats van verspreid over e-mails."),
        ("Vaste calculatie",
         "Dezelfde aanvraag levert later dezelfde prijsopbouw op. Een herhaalorder blijft daardoor navolgbaar."),
        ("U weet waar het staat",
         "Tussen akkoord, productie en levering hoort u van ons wanneer er iets te melden is. U hoeft er niet achteraan."),
        ("Van &eacute;&eacute;n stuk tot serie",
         "Een enkel stuk, een kleine serie of seriewerk: u vraagt het op dezelfde manier aan en het loopt door dezelfde werkwijze."),
    ],

    # -------------------------------------------------------- 06 materialen
    # Vraag: kunnen jullie mijn materiaal verwerken. Compact: kop, een
    # inleiding, drie panelen met korte tekst en de kwaliteiten als lijst.
    "materialen_kop": "Staal, RVS en aluminium",
    "materialen_intro": "Kies het materiaal en de kwaliteit bij uw aanvraag. Staat wat u nodig heeft er niet bij, vermeld het dan: bijzondere metalen zijn op aanvraag leverbaar.",
    "materialen": [
        {"naam": "Staal",
         "tekst": "Voor constructieve en industri&euml;le toepassingen.",
         "kwaliteiten": ["DC01", "DD11", "S235JR", "S355MC", "DX51D+Z"]},
        {"naam": "RVS",
         "tekst": "Voor toepassingen waar corrosiebestendigheid en duurzaamheid belangrijk zijn.",
         "kwaliteiten": ["RVS 304", "RVS 316", "2B of 1D", "Met of zonder beschermfolie"]},
        {"naam": "Aluminium",
         "tekst": "Licht, sterk en goed te bewerken.",
         "kwaliteiten": ["EN AW-1050A", "EN AW-5005", "EN AW-5754 H111", "EN AW-5083"]},
    ],
    "materialen_lijstlabel": "Kwaliteiten",

    # --------------------------------------------------------- 07 projecten
    # Vraag: hebben jullie vergelijkbaar werk gemaakt. Drie kaarten uit CASES
    # (schil.py) met de kaarttekst uit inhoud/cases.py; hier de sectiekop.
    # PLAATSHOUDERS: de klantnamen zijn niet bevestigd, zie het kader bij
    # CASES. De intro zegt wat de bezoeker hier ziet en waarom dat nuttig is:
    # het type werk, en hoe bewerkingen daarin gecombineerd zijn.
    "projecten_eyebrow": "Projecten",
    "projecten_kop": "Projecten uit de praktijk",
    "projecten_intro": "Onderdelen en samenstellingen die Vorma Metaal voor opdrachtgevers produceerde, met de bewerkingen die daarvoor gecombineerd zijn. Zo ziet u welk type werk u hier kunt laten maken.",
    "projecten_knop": "Bekijk alle projecten",

    # ------------------------------------------------------------ 08 cijfers
    # Vraag: hoeveel ervaring en breedte zit erachter. Drie getallen met een
    # korte regel. Sectie 05 zegt al wat de ervaring oplevert (maakbaarheid),
    # dus hier alleen waar ze vandaan komt.
    "usps_kop": "Wat er achter elke aanvraag staat",
    "usps": [
        ("22", "jaar ervaring",
         "Sinds 2004 in de techniek, eerst in machinebouw en industri&euml;le automatisering."),
        ("8", "bewerkingen",
         "Meerdere productiestappen gecombineerd binnen &eacute;&eacute;n aanvraag."),
        ("3", "materialen",
         "Staal, RVS en aluminium, met bijzondere metalen op aanvraag."),
    ],

    # --------------------------------------------------------------- 10 team
    # Vraag: wie zit erachter. Menselijker dan de rest, zonder namen,
    # functies of aantallen: die staan niet in de bron. Kort de achtergrond
    # bij Tentije als context, geen tijdlijn; de herkomst staat op
    # over-vorma-metaal.html, waar de knop heen gaat.
    "over_eyebrow": "Technische kennis vanuit de machinebouw",
    "over_kop": "De mensen achter Vorma Metaal",
    "over_tekst": "<p>Achter Vorma Metaal staat het team van zusterbedrijf Tentije Industri&euml;le Automatisering in Goor. Onze achtergrond ligt in machinebouw en industri&euml;le automatisering. Daardoor begrijpen we niet alleen hoe een onderdeel geproduceerd wordt, maar ook hoe het straks in een machine of samenstelling wordt toegepast.</p>\n            <p>Die kennis zit in elke aanvraag. Is een zetting krap, een las lastig bereikbaar of een materiaal ongebruikelijk, dan ziet u dat terug in de controle en hoort u het van ons voordat de offerte uitgaat.</p>\n            <p>Vorma Metaal en Tentije werken in dezelfde werkplaats. Uw metaalwerk en, als u dat wilt, de samenbouw gebeuren dus op &eacute;&eacute;n adres, door hetzelfde team.</p>",
    "over_knop": "Over Vorma Metaal",

    # ------------------------------------------------------ 11 testimonials
    # ==================================================================
    # PLAATSHOUDERS -- FICTIEVE CITATEN, MAG NIET LIVE ALS FEIT
    # ------------------------------------------------------------------
    # Er zijn nog geen echte klantreviews. De drie citaten zijn voorbeelden
    # van het type testimonial dat later nodig is: kort, over communicatie,
    # afspraken, kwaliteit, technische kennis en het combineren van
    # bewerkingen. Geen cijfers, termijnen of specifieke claims die klinken
    # als een echte uitspraak van dat bedrijf. Bedrijf en logo komen uit de
    # logoband (OPDRACHTGEVERS in schil.py); de persoonsnaam staat als
    # "Naam klant". Elke dia draagt data-plaatshouder="testimonial".
    #
    # Vervangen: (tekst, naam, functie, fotosleutel, logoslug) per citaat.
    # ==================================================================
    "testimonials_eyebrow": "Ervaringen van opdrachtgevers",
    "testimonials_kop": "Zo ervaren opdrachtgevers de samenwerking",
    "testimonials": [
        ("Snijden, kanten en lassen in &eacute;&eacute;n aanvraag, en de delen komen afgewerkt terug. Dat scheelt ons het afstemmen tussen leveranciers.",
         "Naam klant", "Technical Buyer", "lasersnijden", "tes"),
        ("Een zetting op onze tekening bleek niet te maken. Ze belden voordat de offerte uitging, met een aanpassing die wel werkte.",
         "Naam klant", "Werkvoorbereider", "kanten", "stork"),
        ("Duidelijke afspraken over prijs en levering, en die worden nagekomen. Daar kunnen wij ons onderhoud op plannen.",
         "Naam klant", "Hoofd Technische Dienst", "werkbank", "huhtamaki"),
    ],

    # --------------------------------------------------------------- 12 faq
    # Vraag: welke vragen of bezwaren heb ik nog. Zeven items, elk een korte
    # alinea; de FAQ mag herhalen wat elders staat. Geen prijs, minimumafname,
    # productielevertijd of garantie: die staan niet in de bron.
    "faq_kop": "Wat u wilt weten voordat u aanvraagt",
    "faq": [
        ("Hoe vraag ik een offerte aan?", [
            "Via het portaal: u uploadt uw CAD-bestand (STEP, DXF of DWG, eventueel met een PDF-tekening), kiest materiaal en aantal en verstuurt de aanvraag. Liever eerst overleggen? Bel of mail ons uw tekening; ook dan gaat de aanvraag in behandeling.",
        ]),
        # TODO-CONTENT: op vormametaal.nl staat niet of het portaal een account
        # vereist. Dit antwoord zegt wat vaststaat en biedt de route eromheen.
        ("Heb ik een account nodig?", [
            "Uw aanvraag en uw offerte lopen via het portaal. Werkt u liever niet via het portaal, mail dan uw tekening; wij nemen de aanvraag dan gewoon in behandeling.",
        ]),
        ("Is mijn aanvraag vrijblijvend?", [
            "Ja. U ontvangt een vrijblijvende offerte en de productie start pas na uw akkoord. Tot dat moment verplicht een aanvraag u tot niets.",
        ]),
        ("Hoe snel ontvang ik mijn offerte?", [
            "Standaardwerk calculeert het portaal automatisch: die offerte staat binnen enkele minuten online. Complexe aanvragen en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd.",
        ]),
        ("Kan ik een complete samenstelling aanvragen?", [
            "Ja. Samenbouwen loopt via zusterbedrijf Tentije Industri&euml;le Automatisering B.V., in dezelfde werkplaats. Poedercoaten regelen wij via een coater. U houdt &eacute;&eacute;n aanspreekpunt voor het geheel.",
        ]),
        ("Welke bewerkingen kunnen worden gecombineerd?", [
            "Alle acht: lasersnijden, buislasersnijden, kanten, lassen, nabewerking, CNC-verspanen, assemblage en oppervlaktebehandeling. U zet ze in dezelfde aanvraag en uw onderdeel gaat van de ene bewerking naar de volgende zonder tussentransport.",
        ]),
        ("Kan ik enkelstuks en kleine series laten maken?", [
            "Ja, van &eacute;&eacute;n onderdeel tot seriematige productie, via dezelfde aanvraag. Komt dezelfde aanvraag later terug, dan offreren wij die volgens dezelfde vaste calculatie.",
        ]),
    ],

    # ---------------------------------------------------------- 02 logoband
    # De band heeft geen tekstslot. Dit label is voor de aantoonbaar ware
    # variant sectorenband(); zie bouw_home.py.
    "sectoren_label": "Sectoren waarvoor wij werken",

    # ------------------------------------------------------------ 13 contact
    # Vraag: wat moet ik nu doen. Twee routes in een tekstslot en een knop:
    # de knop is de aanvraag, de tekst noemt het telefoonnummer voor wie
    # eerst wil bespreken. Kop past in de 20ch van cta-slot__kop over drie
    # regels; tekst in de 46ch van cta-slot__tekst.
    "contact_kop": "Heeft u een onderdeel dat gemaakt moet worden?",
    "contact_tekst": "Stuur uw CAD-bestand voor een vrijblijvende offerte, of bel 0547 227 000 om uw project eerst te bespreken.",
}
