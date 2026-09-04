# -*- coding: utf-8 -*-
# Inhoud van de dienstpagina Lassen. Het skelet en de sectievolgorde staan vast
# in bouw_service.py; hier staat alleen de tekst die daarin geschoven wordt.
#
# De brontekst ("Lassen met TIG, MIG of laser tot een sterk en strak geheel.")
# is input, geen model: de feiten blijven, de formulering is hier eigen. Lassen
# is eigen huis, net als lasersnijden, buislasersnijden, kanten, nabewerking en
# CNC-verspanen. Assemblage loopt via zusterbedrijf Tentije, oppervlakte-
# behandeling wordt uitbesteed maar volledig door Vorma geregeld. Geen
# machines, plaatdiktes, toleranties, levertijden of certificeringen: die staan
# niet in de bron en bestaan dus niet.
#
# De bezoeker kent Vorma Metaal niet en weet misschien niet wat lassen is: de
# eerste alinea van "intro" legt beide in gewone taal uit. De koppen zijn
# geschreven om los te lezen; de vier FAQ-vragen dekken de onzekerheden die
# vlak voor een aanvraag overblijven (bestanden, materiaal, aantallen, wie de
# tekening beoordeelt, wanneer de prijs komt, wat er na het versturen gebeurt).

DIENST = {
    "bestand": "dienst-lassen.html",
    "slug": "lassen",
    "service_naam": "Lassen",
    "service_naam_kort": "Lassen",
    "namespace": "dienst-lassen",
    "onderwerp": "lassen",
    "titel": "Lassen | Vorma Metaal",

    # Meta description, 139 tekens. Zegt in de eerste regel wat lassen oplevert,
    # noemt daarna de methodes, de drie materialen en het bereik enkelstuks tot
    # series: allemaal uit de brief.
    "omschrijving": "Vorma Metaal last uw platen, buizen en profielen tot &eacute;&eacute;n onderdeel: TIG, MIG of laser in staal, RVS en aluminium, van enkelstuks tot series.",

    # Korte typering voor schema.org serviceType, geen marketingzin.
    "service_type": "Lassen en lasconstructies in metaal",

    "hero_foto": "lassen",
    "eyebrow": "Dienst 04",

    # Twee alinea's van ongeveer 230 tekens, gelijk aan de MADEGRO-intro (twee
    # korte alinea's naast de contactknop). Alinea 1 is voor wie Vorma Metaal
    # niet kent: wat wij doen en wat lassen is, in gewone woorden. Alinea 2 het
    # enige echte onderscheid dat de brief geeft: dezelfde werkplaats voor
    # snijden, kanten en lassen.
    "intro": '''          <p>Vorma Metaal maakt onderdelen in metaal, op maat, uit uw eigen CAD-bestand. Lassen is de bewerking die losse platen, buizen en profielen blijvend aan elkaar verbindt: wij lassen met TIG, MIG of laser in staal, RVS en aluminium, van enkelstuks tot series.</p>
          <p>Dat gebeurt in onze eigen werkplaats in Goor, op dezelfde vloer waar uw delen worden gesneden en gekant (plaatmateriaal in de gewenste vorm zetten). Snijden, kanten en lassen volgen daar op elkaar, zonder dat uw werk er tussendoor uit moet voor transport.</p>''',

    # Twee korte zinnen die de drie kaarten inleiden, zelfde lengte als MADEGRO.
    # Zegt wanneer lassen aan de orde is en benoemt de drie eisen die de kaarten
    # uitwerken. Geen uitspraak over hoe vaak iets voorkomt: de orderverdeling
    # staat nergens.
    "wanneer_intro": "Lassen is nodig zodra uw product uit meer dan &eacute;&eacute;n stuk metaal bestaat. Hieronder staan drie situaties waarin er iets anders van de las wordt gevraagd: sterkte, een net aanzicht of een serie waarin elk stuk gelijk is.",

    # Drie situaties die ver uiteen liggen: constructie, zichtwerk en herhaal-
    # werk. De titels benoemen de situatie zelf, zodat ze los te scannen zijn.
    # Concreet, zonder plaatdiktes of toleranties. De laatste kaart leunt op de
    # vaste calculatie bij een herhaalaanvraag, die wel vaststaat.
    "herkenning": [
        ("Losse delen die &eacute;&eacute;n onderdeel moeten worden",
         "U heeft gesneden plaat, buis of profiel die samen een frame, bak of behuizing vormen. Wij richten de delen uit en lassen ze vast, zodat u geen bouwpakket maar &eacute;&eacute;n onderdeel geleverd krijgt."),
        ("De lasnaad blijft in het zicht",
         "Bij RVS in de interieurbouw of een behuizing die zichtbaar blijft, wordt de naad gezien. Naast de sterkte telt dan het aanzicht. Vermeld dat bij uw aanvraag, dan kiezen wij de lasmethode daarop."),
        ("Een serie waarin elk stuk gelijk is",
         "In een serie moet het laatste stuk net zo passen als het eerste. Wij maken enkelstuks en series; vraagt u dezelfde opdracht later opnieuw aan, dan rekenen wij volgens dezelfde vaste calculatie."),
    ],

    # Kop van de aanpak-band: dekt de vier treden ernaast, van tekening tot
    # nabewerkt onderdeel, en is los van de alinea te begrijpen.
    "aanpak_kop": "Van tekening tot gelast en nabewerkt onderdeel",

    # De vijf stappen uit de brief in vier zinnen: aanvraag met bestandsformaten,
    # maakbaarheidscontrole met afstemming, vrijblijvende offerte die pas na
    # akkoord tot werk leidt, productie en levering of afhalen. Geen termijn voor
    # de productie genoemd, die staat er niet.
    "aanpak_intro": "U uploadt uw CAD-bestanden in het portaal: STEP, DXF of DWG, eventueel met een PDF-tekening. Wij controleren of uw onderdeel maakbaar is en bellen u bij een complexe opdracht voordat de offerte uitgaat. Die offerte is vrijblijvend; het werk start pas na uw akkoord. Daarna lassen wij uw delen, bewerken ze na en leveren ze bij u af, of uw werk staat klaar om af te halen.",

    # Vier treden binnen de bewerking zelf, elk ongeveer 200 tekens zoals de
    # MADEGRO-treden. Trede 4 zet de grens goed: nabewerking eigen huis,
    # oppervlaktebehandeling uitbesteed maar geregeld, samenbouw via Tentije.
    "stappen": [
        ("Uw tekening en de naden nalopen",
         "Bij de maakbaarheidscontrole kijken wij hoe de delen samenkomen: waar de naden liggen, of ze bereikbaar zijn en welke methode daarbij past. Bij een complexe opdracht stemmen wij dat eerst met u af.",
         None),
        ("Delen uitrichten voordat er gelast wordt",
         "De gesneden en gekante delen komen uit dezelfde werkplaats. Ze worden eerst uitgericht (op de juiste plaats en hoek gezet) en vastgezet: de pasvorm bepaalt hoe sterk en hoe strak het geheel wordt.",
         None),
        ("Lassen met TIG, MIG of laser",
         "Dat zijn drie lasmethodes. Welke het wordt, volgt uit het materiaal en uit wat de constructie moet dragen: staal, RVS en aluminium vragen elk een eigen aanpak. Ligt de naad in het zicht, dan weegt het aanzicht mee.",
         None),
        ("Nabewerken zelf, coating door ons geregeld",
         "Afbramen (scherpe randen wegnemen), tappen, boren en verzinken doen wij zelf. Moet het geheel gecoat worden, dan regelen wij dat voor u. Samenbouw tot een complete samenstelling loopt via zusterbedrijf Tentije.",
         None),
    ],

    # Kop van de voordelen-band: zegt het voordeel zelf in plaats van het aan te
    # kondigen. De drie genoemde bewerkingen zijn alle drie eigen huis.
    "voordelen_kop": "Uw onderdeel komt gesneden, gekant en gelast uit &eacute;&eacute;n werkplaats",

    # Vier korte panelen van ongeveer 110 tekens, zoals MADEGRO. Elke titel
    # noemt het voordeel, niet de categorie. Elk punt is terug te vinden in de
    # brief: eigen huis, sterk en strak uit de brontekst, enkelstuks tot series,
    # en de doorloop naar nabewerking en coating.
    "voordelen": [
        ("vinkje", "Geen transport tussenin",
         "Snijden, kanten en lassen gebeuren in dezelfde werkplaats in Goor, zonder tussentijds transport naar een ander bedrijf."),
        ("schild", "Sterk en strak tegelijk",
         "Een las moet dragen; ligt hij in het zicht, dan moet hij er ook netjes uitzien. Daarop kiezen wij de methode."),
        ("lijst", "Van &eacute;&eacute;n stuk tot een serie",
         "Enkelstuks en seriematige productie, met dezelfde vaste calculatie als u dezelfde opdracht opnieuw aanvraagt."),
        ("document", "De coating regelen wij voor u",
         "Nabewerking doen wij zelf; poedercoaten besteden wij uit en regelen wij volledig. U zoekt er geen tweede leverancier bij."),
    ],

    # LEEG. Vorma Metaal heeft geen samenwerkingspartners om te tonen; het
    # zusterbedrijf Tentije staat al in de stappen en de FAQ.
    "partners": [],

    # Laatste sectie, dus de aanvraagfase: de kop vraagt om de opdracht en niet
    # om een gesprek. De knop eronder is "Vraag een offerte aan".
    "contact_kop": "Laat uw lasconstructie bij ons maken",

    # De FAQ staat vlak voor de offerteknop en neemt daarom de onzekerheden weg
    # die dan nog over zijn: welke bestanden, welk materiaal en welke aantallen,
    # wie de tekening beoordeelt en wanneer de prijs komt, en wat er na het
    # versturen gebeurt. Geen termijnen buiten de twee die de brief geeft
    # (automatisch geoffreerd binnen enkele minuten, complex binnen korte tijd),
    # geen diktes, geen garanties; wel de grenzen van eigen huis.
    "faq": [
        ("Welke bestanden moet ik aanleveren voor een lasconstructie?", [
            "Ons portaal leest STEP, DXF en DWG in, eventueel met een PDF-tekening erbij. U uploadt uw CAD-bestanden en kiest het materiaal; de bestanden worden direct ingelezen.",
            "Zet in de tekening of bij uw aanvraag wat het product moet doen, waar het komt te zitten en of de naad in het zicht blijft. Dat bepaalt de lasmethode en de afwerking.",
        ]),
        ("In welk materiaal en in welke aantallen kunt u lassen?", [
            "Wij lassen staal, RVS en aluminium; bijzondere metalen zijn op aanvraag leverbaar. In het portaal selecteert u het gewenste materiaal. Staat het er niet bij, vermeld het dan bij uw aanvraag of neem contact op.",
            "Van &eacute;&eacute;n stuk tot seriematige productie: een enkel frame kan, net als een serie van hetzelfde onderdeel. Het aantal geeft u bij uw aanvraag op.",
        ]),
        ("Wie beoordeelt mijn tekening, en wanneer krijg ik de prijs?", [
            "Wij controleren zelf of uw aanvraag maakbaar is, voordat er een prijs uitgaat. Bij een complexe opdracht of een bijzonder materiaal beoordelen wij uw tekening persoonlijk en stemmen wij die eerst met u af.",
            "Standaardwerk offreren wij volledig automatisch: die offerte staat binnen enkele minuten online. Complexe aanvragen beoordelen wij persoonlijk, binnen korte tijd. U wacht geen dagen op uw prijs.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "U ontvangt een duidelijke, vrijblijvende offerte; het werk start pas na uw akkoord. Daarna maken wij uw delen in onze werkplaats (snijden, kanten, lassen), met de afgesproken nabewerking erbij.",
            "Poedercoaten en andere oppervlaktebehandelingen besteden wij uit en regelen wij volledig voor u; samenbouw tot een complete samenstelling loopt via zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Daarna leveren wij uw werk, of het staat klaar om af te halen.",
        ]),
    ],
}
