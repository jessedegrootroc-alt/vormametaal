# -*- coding: utf-8 -*-
# Inhoud voor de dienstpagina Kanten. Het skelet en de sectievolgorde staan in
# bouw_service.py en veranderen niet; hier staat alleen de tekst.
# Feit uit BRIEF.md: kanten is "plaatmateriaal nauwkeurig zetten en kanten tot
# de gewenste vorm", en het gebeurt in eigen huis. Die brontekst is input, geen
# formulering om over te nemen: de tekst hieronder is eigen taal met dezelfde
# feiten. Geen machines, diktes, radii, toleranties of levertijden genoemd; die
# staan niet in de bron.

DIENST = {
    "bestand": "dienst-kanten.html",
    "slug": "kanten",
    "service_naam": "Kanten",
    "service_naam_kort": "Kanten",
    "namespace": "dienst-kanten",
    "onderwerp": "kanten",
    "titel": "Kanten | Vorma Metaal",

    # Meta description, 150 tekens: eerst wat de bezoeker krijgt, dan wie het
    # doet, waar en in welk materiaal. Geen belofte over levertijd of capaciteit.
    "omschrijving": "Uw plaat in de juiste vorm gezet, uit uw eigen CAD-bestand. Vorma Metaal zet staal, RVS en aluminium in eigen huis in Goor, van enkelstuks tot series.",

    # Korte typering voor schema.org serviceType, geen marketingzin.
    "service_type": "Kanten en zetten van plaatmateriaal",

    "hero_foto": "productiehal",
    "eyebrow": "Dienst 03",

    # Twee alinea's van dezelfde lengte als de MADEGRO-intro (circa 250 en 220
    # tekens). Alinea 1 is voor iemand die Vorma Metaal niet kent: eerst wat wij
    # doen, dan in gewone taal wat kanten is. Alinea 2 zegt dat het in eigen
    # huis gebeurt en noemt de drie materialen uit de brief.
    "intro": '''          <p>Vorma Metaal maakt metalen onderdelen op maat, uit het CAD-bestand dat u aanlevert. Kanten is de bewerking die daar de vorm in brengt: een vlakke, gesneden plaat wordt langs rechte lijnen gezet tot een hoek, een profiel, een bak of een omkasting.</p>
          <p>Dat zetten doen wij in eigen huis, in dezelfde werkplaats waar uw plaat wordt gesneden en gelast. Wij zetten staal, RVS en aluminium; elk materiaal veert na een zetting anders terug, dus wij bepalen per materiaal hoe de plaat vlak gesneden moet worden.</p>''',

    # Inleiding op de drie kaarten. Zegt wat kanten in de rij bewerkingen doet
    # en wat de bezoeker nodig heeft om te beginnen: zijn tekening.
    "wanneer_intro": "Kanten volgt op het snijden en gaat daarna vaak door naar lassen of nabewerking. Hieronder staan drie situaties waarin zetwerk aan de orde is; herkent u er een, dan is uw tekening genoeg om te beginnen.",

    # Drie situaties waarin een inkoper of engineer zetwerk nodig heeft. De
    # titels zeggen los van de tekst al om welke situatie het gaat. Concreet,
    # zonder plaatdiktes, afmetingen of toleranties.
    "herkenning": [
        ("Een kast of bak uit &eacute;&eacute;n plaat",
         "Een kast, kap of bak die u nu uit losse platen laat lassen, komt vaak uit &eacute;&eacute;n gesneden plaat. Elke hoek die gezet wordt in plaats van gelast, scheelt een naad, uitlijnwerk en nabewerking."),
        ("U heeft alleen een 3D-model",
         "Uw model bestaat, maar de platte vorm waaruit het deel gezet wordt niet. Die leiden wij uit uw STEP-, DXF- of DWG-bestand af, en u hoort van ons als de zettingen in uw model niet uitkomen."),
        ("Het deel moet om een bestaand frame passen",
         "Een gezette plaat die om een frame valt of tegen een ander deel aansluit, moet na het zetten nog precies op maat zijn. Vraagt u de delen later opnieuw aan, dan gaan ze langs dezelfde platte vorm en dezelfde calculatie."),
    ],

    "aanpak_kop": "Van uw 3D-model tot een gezet onderdeel",

    # Drie zinnen over het traject van aanvraag tot levering, in de woorden van
    # de vijf stappen uit de brief: portaal, maakbaarheidscontrole,
    # vrijblijvende offerte, akkoord, levering of afhalen.
    "aanpak_intro": "U dient uw aanvraag in via het portaal, met een STEP-, DXF- of DWG-bestand en eventueel een PDF-tekening. Wij controleren eerst of het zetwerk maakbaar is en stemmen bij een complexe opdracht met u af. De offerte is vrijblijvend; het werk start pas na uw akkoord.",

    # Vier stappen binnen deze bewerking zelf, niet het algemene traject. De
    # titels zijn los te lezen: iemand die alleen de treden scant, ziet de weg
    # van bestand naar levering. Detail blijft None: de trede__gedrag-regel
    # hoort bij de Veiligheidsladder van MADEGRO en heeft hier geen
    # inhoudelijke tegenhanger.
    "stappen": [
        ("Van 3D-model naar vlakke plaat",
         "Uit uw bestand leiden wij de platte vorm met de zetlijnen af. Wij kijken of de zettingen elkaar niet in de weg zitten en of er geen gat of uitsparing zo dicht op een zetlijn ligt dat het vervormt.",
         None),
        ("Eerst de zetvolgorde bepalen",
         "De volgorde van de zettingen bepaalt of elke volgende zetting nog te maken is: een rand die al gezet is, kan de volgende in de weg zitten. Die volgorde staat vast voordat de eerste plaat wordt gezet.",
         None),
        ("Zetten in eigen huis",
         "De zettingen worden in die volgorde gemaakt, in onze eigen werkplaats in Goor. Wij besteden dit niet uit: dezelfde werkplaats die uw plaat snijdt, zet hem ook.",
         None),
        ("Door naar lassen of naar levering",
         "Hoort er lassen of nabewerking bij, dan gaat het deel in dezelfde werkplaats door. Poedercoaten en andere oppervlaktebehandeling besteden wij uit en regelen wij volledig. Daarna leveren wij, of u haalt op.",
         None),
    ],

    # De vaste subtitle boven deze kop is "Wat het oplevert"; de kop zelf zegt
    # dus wat dat concreet is en dekt de vier panelen eronder.
    "voordelen_kop": "Uw plaat komt gesneden en gezet uit &eacute;&eacute;n werkplaats",

    # Vier voordelen, elk circa 100-130 tekens zoals bij MADEGRO. Iconen uit de
    # vaste set: vinkje, klok, schild, grafiek.
    "voordelen": [
        ("vinkje", "Uw zetlijnen eerst nagekeken",
         "Wij lopen de vlakke plaat en de zetvolgorde na bij de maakbaarheidscontrole, dus voordat er materiaal in gaat."),
        ("klok", "Snijden en zetten achter elkaar",
         "Na het snijden gaat uw plaat direct door naar het zetwerk, zonder tussentransport en zonder tweede leverancier."),
        ("schild", "Minder naden om te lassen",
         "Wat gezet is, hoeft niet gelast en niet afgebraamd te worden. Dat scheelt werk en er zit geen naad in het zichtvlak."),
        ("grafiek", "Van &eacute;&eacute;n stuk tot een serie",
         "Bij een herhaalaanvraag houden wij dezelfde vlakke plaat en dezelfde vaste calculatie aan, van enkelstuks tot serie."),
    ],

    # Leeg: MADEGRO had hier drie samenwerkingspartners. Vorma Metaal heeft
    # alleen zusterbedrijf Tentije, dat in de FAQ staat. Geen partners verzinnen.
    "partners": [],

    # Laatste sectie, dus de aanvraagfase: de knop eronder is "Vraag een
    # offerte aan". De kop vraagt om de opdracht in plaats van te verkennen.
    "contact_kop": "Laat uw plaatwerk bij ons zetten",

    # De vier vragen die vlak voor een aanvraag nog open staan: welk bestand,
    # wie de tekening beoordeelt en wanneer de prijs komt, welk materiaal en
    # welke aantallen, en wat er na het versturen gebeurt. Alle antwoorden komen
    # uit de brief: portaalformaten, maakbaarheidscontrole voor de offerte, de
    # offertetermijn, de drie materialen, de acht bewerkingen en Tentije.
    "faq": [
        ("Welk bestand moet ik aanleveren?", [
            "Het portaal leest STEP, DXF en DWG in, eventueel met een PDF-tekening erbij. Overtekenen hoeft niet: uw eigen CAD-bestand is genoeg voor een aanvraag.",
            "Een 3D-model mag; de platte vorm met de zetlijnen leiden wij daar zelf uit af. Heeft u die al zelf getekend, dan houden wij die aan en controleren wij of de maten na het zetten uitkomen.",
        ]),
        ("Wie beoordeelt mijn tekening, en wanneer weet ik de prijs?", [
            "Wij kijken zelf naar uw tekening, in dezelfde werkplaats waar het zetwerk gebeurt. Standaardwerk wordt automatisch geoffreerd en staat binnen enkele minuten online; complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd.",
            "Is de opdracht complex, of is een zetting zo niet te maken, dan nemen wij eerst contact met u op &mdash; voordat de offerte uitgaat. Dan bespreken wij wat er in de tekening aangepast moet worden.",
        ]),
        ("In welk materiaal en welke aantallen kan het?", [
            "Wij verwerken staal, RVS en aluminium. Elk van de drie veert anders terug, dus wij rekenen de vlakke plaat per materiaal door. Voor RVS is plaat met beschermfolie een van de mogelijkheden; die folie beschermt de zichtzijde tijdens het bewerken en het transport.",
            "In aantallen bent u vrij: van &eacute;&eacute;n stuk tot seriematige productie, bij een herhaalaanvraag met dezelfde vlakke plaat en dezelfde vaste calculatie. Bijzondere metalen zijn op aanvraag leverbaar; vermeld dat bij uw aanvraag of neem contact op.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Wij nemen uw aanvraag in behandeling en controleren of hij maakbaar is; bij een complexe opdracht stemmen wij eerst met u af. Daarna volgt een vrijblijvende offerte en start het werk pas na uw akkoord.",
            "Daarna gaat uw plaat de werkplaats in: snijden, zetten en zo nodig lassen, nabewerken of verspanen. Poedercoaten besteden wij uit en regelen wij volledig; samenbouwen tot een compleet geheel loopt via zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Wij leveren, of u haalt op.",
        ]),
    ],
}
