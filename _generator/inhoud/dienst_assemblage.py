# -*- coding: utf-8 -*-
# Inhoud van de dienstpagina Assemblage. Vult het bestaande MADEGRO-dienstsjabloon
# (bouw_service.py); sectievolgorde en layout blijven ongewijzigd.
#
# Feit uit BRIEF.md: samenbouwen tot complete samenstellingen loopt via
# zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Assemblage gebeurt
# dus NIET in eigen huis van Vorma. Elke tekst hieronder zegt dat eerlijk en
# zet er het feit naast dat het op dezelfde vloer blijft: Vorma Metaal is uit
# Tentije voortgekomen en beide bedrijven delen dezelfde werkplaats en hetzelfde
# team.
#
# De brontekst van vormametaal.nl is input, geen waarheid: de feiten staan vast,
# de formulering is hier opnieuw geschreven op de vier toetsen uit COPY.md
# (begrijpelijk, concreet, conversiegericht, relevant). Geen machines,
# plaatdiktes, afmetingen, toleranties, certificeringen, klantnamen, aantallen
# of levertijden: die staan niet in de brief.

DIENST = {
    "bestand": "dienst-assemblage.html",
    "slug": "assemblage",
    "service_naam": "Assemblage",
    "service_naam_kort": "Assemblage",
    "namespace": "dienst-assemblage",
    "onderwerp": "assemblage",
    "titel": "Assemblage | Vorma Metaal",

    # Meta description, 120&ndash;155 tekens. Zegt in de zoekresultaten meteen
    # wat de bezoeker krijgt en wie wat doet, zodat niemand op een verkeerde
    # verwachting klikt.
    "omschrijving": "Uw metalen onderdelen samengebouwd tot &eacute;&eacute;n product: wij maken de delen in Goor, zusterbedrijf Tentije bouwt ze samen. &Eacute;&eacute;n aanvraag.",

    # Korte typering voor de schema.org Service; geen marketingzin.
    "service_type": "Assemblage van metalen samenstellingen",

    "hero_foto": "overleg",
    "eyebrow": "Dienst 06",

    # Twee alinea's, zelfde lengte als de MADEGRO-intro (twee blokjes van
    # ongeveer gelijke omvang). Alinea 1 is voor iemand die Vorma Metaal niet
    # kent en misschien niet weet wat assemblage is: eerst wat wij doen, dan wat
    # assemblage is, dan bij wie het samenbouwen gebeurt. Alinea 2 legt uit
    # waarom dat geen doorverwijzing naar een vreemde partij is.
    "intro": '''          <p>Vorma Metaal maakt metalen onderdelen op maat, uit het tekenbestand dat u aanlevert. Assemblage is de stap daarna: de losse delen &mdash; plaatwerk, buiswerk en verspaand werk (gedraaide en gefreesde onderdelen) &mdash; worden samengebouwd tot &eacute;&eacute;n product, zoals een frame of een omkasting. Dat samenbouwen loopt via zusterbedrijf Tentije Industri&euml;le Automatisering B.V.</p>
          <p>Dat is geen doorverwijzing naar een vreemde partij. Tentije begon in 2004 in Goor en Vorma Metaal is daaruit voortgekomen; de twee bedrijven werken in dezelfde werkplaats, met hetzelfde team. Uw delen worden dus gemaakt en samengebouwd op dezelfde vloer, met &eacute;&eacute;n aanvraag en &eacute;&eacute;n aanspreekpunt.</p>''',

    # Leidt de drie kaarten in en zet de keuze neer die de bezoeker hier maakt:
    # onderdelen los laten leveren, of samengebouwd als &eacute;&eacute;n product.
    "wanneer_intro": "U kunt uw onderdelen los laten leveren, of samengebouwd als &eacute;&eacute;n product. Deze drie situaties laten zien wanneer samenbouwen u werk uit handen neemt.",

    # Exact 3 situaties, elk met een titel die op zichzelf te lezen is.
    # Concreet, zonder plaatdiktes, afmetingen of toleranties &mdash; die staan
    # niet in de bron.
    "herkenning": [
        ("Plaat, buis en verspaand werk in &eacute;&eacute;n frame",
         "Uw delen vormen samen een frame, kast of omkasting. Koopt u ze los in, dan blijft het passen, uitlijnen en monteren bij u liggen."),
        ("Het samenbouwen ligt nu bij uw eigen monteurs",
         "Uw mensen zijn bezig met schroeven en uitlijnen in plaats van met het werk waarvoor u ze in dienst heeft. Een samenstelling die compleet aankomt, geeft die uren terug."),
        ("Uw product is een machineframe of besturingskast",
         "Het samenbouwen gebeurt bij Tentije, dat zich richt op machinebouw, onderhoud en besturingstechniek. Uw delen worden dus samengebouwd in de werkplaats waar dat werk gebeurt."),
    ],

    # Kop boven het stappenblok; zelfde lengte-orde als de MADEGRO-koppen
    # ("Van inventarisatie naar plan van aanpak"). Zegt de rolverdeling in
    # &eacute;&eacute;n regel, zodat wie alleen de koppen scant het al weet.
    "aanpak_kop": "Wij maken de delen, Tentije bouwt ze samen",

    # Drie zinnen over het traject van aanvraag tot levering, in de woorden van
    # de vijf stappen uit de brief. De persoonlijke beoordeling van een complexe
    # aanvraag staat in de bron; er wordt geen termijn genoemd.
    "aanpak_intro": "U vraagt uw samenstelling aan via ons online portaal. Wij controleren of het geheel maakbaar is en welk deel waar wordt gemaakt; bij een complexe opdracht stemmen wij dat eerst met u af. U ontvangt een vrijblijvende offerte en het werk start pas na uw akkoord.",

    # Vier stappen binnen deze bewerking. Stap 3 benoemt onomwonden dat het
    # samenbouwen bij Tentije gebeurt; stap 4 dat het contact bij Vorma blijft.
    "stappen": [
        ("Aanvraag en maakbaarheid",
         "U levert uw bestanden aan via ons portaal: STEP, DXF of DWG, eventueel met een PDF-tekening. Wij kijken naar het geheel, niet alleen naar de losse delen: welke onderdelen wij maken en wat het samenbouwen vraagt.",
         None),
        ("Onderdelen in onze eigen werkplaats",
         "Plaatwerk, buiswerk en verspaand werk maken wij zelf: lasersnijden, buislasersnijden, kanten (plaat in vorm zetten), lassen en nabewerking. Moet er gepoedercoat worden, dan besteden wij dat uit en regelen wij het volledig.",
         None),
        ("Samenbouwen bij Tentije",
         "Het samenbouwen tot een compleet product gebeurt door zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Dat is dezelfde werkplaats en hetzelfde team, dus uw onderdelen blijven op dezelfde vloer.",
         None),
        ("Levering of afhalen in Goor",
         "U ontvangt de samenstelling als &eacute;&eacute;n geheel, of hij staat klaar om af te halen in Goor. Aanvraag, offerte, terugkoppeling en levering lopen via Vorma Metaal, ook voor het deel dat Tentije samenbouwt.",
         None),
    ],

    "voordelen_kop": "U ontvangt &eacute;&eacute;n samengebouwd product, geen losse delen",

    # Exact 4 voordelen, iconen uit de vaste set. Elke titel is een uitkomst,
    # geen sfeerwoord. Geen levertijd, capaciteit of garantie &mdash; alleen wat
    # aantoonbaar uit de bron volgt.
    "voordelen": [
        ("mensen", "Hetzelfde team, dezelfde vloer",
         "Vorma Metaal en Tentije delen werkplaats en team. Wat wij maken, wordt samengebouwd op de vloer waar het gemaakt is."),
        ("vinkje", "&Eacute;&eacute;n aanvraag, &eacute;&eacute;n offerte",
         "U vraagt een product aan, geen losse bewerkingen. Geen losse orders bij verschillende leveranciers die u zelf op elkaar moet afstemmen."),
        ("lijst", "Zes bewerkingen in eigen huis",
         "Lasersnijden, buislasersnijden, kanten, lassen, nabewerking en verspanen doen wij zelf. Het poedercoaten regelen wij voor u."),
        ("schild", "Correcties blijven in dezelfde werkplaats",
         "Past een deel niet, dan wordt het daar opgepakt waar het gemaakt is. U meldt het bij ons; wij stemmen het met Tentije af."),
    ],

    # LEEG. MADEGRO had hier drie samenwerkingspartners. Vorma Metaal heeft
    # alleen zusterbedrijf Tentije, en dat staat al in de intro, de stappen en
    # de FAQ. Partners verzinnen mag niet.
    "partners": [],

    # Laatste sectie, dus de aanvraagfase: deze kop vraagt om de opdracht. De
    # knop eronder is "Vraag een offerte aan".
    "contact_kop": "Vraag uw complete samenstelling aan",

    # De vier vragen die iemand nog heeft v&oacute;&oacute;r hij de aanvraag
    # verstuurt: welke bestanden, welk materiaal en welke aantallen, wie de
    # tekening beoordeelt en wanneer de prijs komt, en wat er na het versturen
    # gebeurt. Geen algemeenheden; alle antwoorden komen uit de brief.
    "faq": [
        ("Welke bestanden moet ik aanleveren voor een samenstelling?", [
            "Het portaal leest STEP, DXF en DWG in, eventueel met een PDF-tekening erbij. Heeft u het complete geheel getekend, stuur dat bestand dan mee: dan is te zien hoe de losse delen in elkaar passen.",
            "Is het samenbouwen nergens vastgelegd, dan nemen wij het met u door. Bel of mail ons als u vooraf wilt overleggen; bij een complexe aanvraag nemen wij zelf contact met u op voordat de offerte uitgaat.",
        ]),
        ("In welk materiaal en in welke aantallen kan het?", [
            "Wij verwerken staal, RVS en aluminium; bijzondere metalen zijn op aanvraag leverbaar. U selecteert het materiaal in het portaal. Staat het uwe er niet bij, vermeld dat dan bij uw aanvraag of neem contact op.",
            "Aantallen lopen van enkelstuks tot seriematige productie. &Eacute;&eacute;n samenstelling laten maken kan dus, en bij een herhaalaanvraag rekenen wij volgens dezelfde vaste calculatie.",
        ]),
        ("Wie beoordeelt mijn tekening en wanneer weet ik de prijs?", [
            "Standaardwerk offreert het portaal automatisch: die offerte staat binnen enkele minuten online. Een samenstelling met montage is geen standaardwerk, dus die beoordelen wij persoonlijk, binnen korte tijd. U wacht geen dagen op uw offerte.",
            "Uw aanvraag wordt beoordeeld door hetzelfde team dat het werk maakt, met 22 jaar ervaring in de machinebouw en automatisering. Is het geheel niet maakbaar zoals getekend, dan hoort u dat van ons. De offerte is vrijblijvend en volgt een vaste calculatie.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Wij nemen uw aanvraag in behandeling en controleren de maakbaarheid. U ontvangt een vrijblijvende offerte; het werk start pas na uw akkoord. Daarna maken wij de onderdelen en bouwt Tentije ze in dezelfde werkplaats samen.",
            "Van offerte tot levering hoort u van ons wanneer het ertoe doet, en u houdt &eacute;&eacute;n aanspreekpunt bij Vorma Metaal &mdash; ook voor het deel dat Tentije samenbouwt. Uw samenstelling wordt geleverd, of staat klaar om af te halen aan de Dammaten 14 in Goor.",
        ]),
    ],
}
