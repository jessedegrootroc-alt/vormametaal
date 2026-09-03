# -*- coding: utf-8 -*-
# Inhoud voor de dienstpagina Buislasersnijden. Vult het bestaande
# MADEGRO-dienstsjabloon (bouw_service.py); sectievolgorde en layout blijven
# ongewijzigd. Enige bron voor feiten: inhoud/BRIEF.md.
# De brontekst van deze bewerking ("Snijden en bewerken van buis- en
# profielmateriaal.", in eigen huis) is input, geen waarheid: het feit blijft,
# de formulering is hier vrij. Schrijfnorm: inhoud/COPY.md.

DIENST = {
    "bestand": "dienst-buislasersnijden.html",
    "slug": "buislasersnijden",
    "service_naam": "Buislasersnijden",
    "service_naam_kort": "Buislasersnijden",
    "namespace": "dienst-buislasersnijden",
    "onderwerp": "buislasersnijden",
    "titel": "Buislasersnijden | Vorma Metaal",

    # Meta description, circa 140 tekens. Noemt de bewerking, de materialen uit
    # de brief en de eerste stap (aanvraag via het portaal). Geen maten,
    # diktes of levertijden: die staan niet in de bron.
    "omschrijving": "Buislasersnijden bij Vorma Metaal: snijden en bewerken van buis- en profielmateriaal in staal, RVS en aluminium. Vraag uw offerte online aan.",

    # Korte typering voor schema.org, in dezelfde lengte als de MADEGRO-waarde.
    "service_type": "Buislasersnijden en profielbewerking",

    "hero_foto": "transport",
    "eyebrow": "Dienst 02",

    # Twee alinea's, even lang als de MADEGRO-intro (circa 250 tekens per
    # alinea). Alinea 1 zegt eerst wat Vorma Metaal doet en legt dan de term
    # uit in gewone taal: de bezoeker kent het bedrijf niet en misschien de
    # bewerking niet. Alinea 2 zegt wat de inkoper eraan heeft en benoemt dat
    # het snijden in eigen huis gebeurt, naast de andere bewerkingen.
    "intro": "<p>Vorma Metaal maakt metalen onderdelen op uw tekening. Buislasersnijden is daarvan de bewerking voor buis en profiel: de laser kort het profiel af op lengte en snijdt in dezelfde bewerking de gaten, uitsparingen en aansluitingen mee die uw onderdeel nodig heeft.</p>\n          <p>Dat scheelt losse handelingen: minder aftekenen, zagen en naboren voordat er gelast kan worden. Wij snijden in eigen huis, in dezelfde werkplaats waar ook gekant, gelast en verspaand wordt &mdash; van &eacute;&eacute;n stuk tot een serie.</p>",

    # Twee zinnen die de drie situatiekaarten inleiden, zelfde lengte als de
    # MADEGRO-tekst. Zegt waar het bij buiswerk op aankomt en wat de kaarten
    # eronder de bezoeker opleveren; geen claim over hoe vaak iets voorkomt,
    # want dat staat niet in de brief.
    "wanneer_intro": "Buis en profiel moeten straks ergens op passen: op elkaar, of op plaatdelen. In deze drie situaties scheelt het u werk als de aansluitingen al in de buis gesneden zitten.",

    # Exact drie situaties, concreet en zonder specificaties. De titel noemt de
    # opdracht die de bezoeker zelf in handen heeft; de tekst zegt wat hij
    # eraan overhoudt. Niets over de machine.
    "herkenning": [
        ("U bouwt frames van buis of profiel",
         "Een frame wordt zo strak als zijn aansluitingen. Snijden wij die mee in de buis, dan vallen de delen op hun plek en hoeft er bij het lassen minder uitgelijnd en bijgewerkt te worden."),
        ("U bestelt hetzelfde onderdeel opnieuw",
         "Bij een herhaalorder moet het laatste stuk gelijk zijn aan het eerste. Wij snijden elke buis uit hetzelfde bestand en rekenen uw herhaalaanvraag volgens dezelfde vaste calculatie."),
        ("Uw product bestaat uit buis &eacute;n plaat",
         "Buisdelen en plaatdelen komen hier uit dezelfde werkplaats. U hoeft dus geen twee leveranciers op elkaar af te stemmen voor delen die straks aan elkaar gelast worden."),
    ],

    # Kop boven de trap. Beschrijft de route die het werk aflegt, niet een
    # ladder of model: die had MADEGRO en Vorma heeft dat niet. "CAD-bestand"
    # in plaats van "STEP-bestand", want de kop moet ook los te begrijpen zijn;
    # welke formaten het portaal inleest staat in trede 01.
    "aanpak_kop": "Van uw CAD-bestand tot gesneden en afgebraamd buiswerk",

    # Drie zinnen over de plek van deze bewerking in het traject van aanvraag
    # tot levering. Alles komt uit de vijf stappen en de offertetermijn in de
    # brief; geen productielevertijd, want die staat nergens.
    "aanpak_intro": "U levert uw bestand aan via het portaal; wij controleren eerst of het onderdeel zo te maken is. Bij standaardwerk staat uw offerte direct online, bij een complexer onderdeel bellen wij u voordat de offerte uitgaat. Na uw akkoord gaat het buiswerk in productie en volgt levering of afhalen.",

    # Vier treden BINNEN deze bewerking, elk circa 220 tekens zoals de
    # MADEGRO-treden. De titels zijn korte mededelingen in plaats van labels,
    # zodat wie alleen de trap scant de volgorde begrijpt. Het detailveld
    # blijft leeg: MADEGRO gebruikte dat voor "herkenbaar gedrag" bij de
    # Veiligheidsladder en dat heeft hier geen tegenhanger.
    "stappen": [
        ("Wij toetsen uw bestand",
         "Uw STEP-, DXF- of DWG-bestand komt binnen via het portaal, eventueel met een PDF-tekening erbij. Wij kijken of het profiel zo te snijden is en of de gaten en uitsparingen op de aangegeven plek passen.",
         None),
        ("U kiest het materiaal",
         "In het portaal kiest u staal, RVS of aluminium; bijzondere metalen zijn op aanvraag leverbaar. Staat het materiaal dat u nodig hebt niet in de lijst, vermeld dat dan bij uw aanvraag of bel ons er eerst over.",
         None),
        ("De laser snijdt uw profiel",
         "De lengte, de gaten en de uitsparingen komen uit hetzelfde model dat u aanlevert. Doordat ze in &eacute;&eacute;n bewerking gesneden worden, ligt elk gat op de plek waar uw tekening het zet &mdash; bij het eerste stuk en bij het laatste.",
         None),
        ("Wij bramen af en regelen het vervolg",
         "Wij bramen af, dus de scherpe snijranden gaan eraf, en tappen of boren wat er nog bij hoort. Gaat uw buiswerk daarna naar het lassen, dan blijft het in dezelfde werkplaats; poedercoaten besteden wij uit en regelen wij voor u.",
         None),
    ],

    # Kop boven de vier voordeelpanelen. Vat de vier panelen samen: minder
    # voorbewerking (1), delen die passen (2), en een prijs die u kunt
    # narekenen omdat hetzelfde bestand en dezelfde calculatie terugkomen
    # (3 en 4). De sectielabel boven de kop ("Wat het oplevert") staat vast in
    # het sjabloon, dus de kop moet zelf de inhoud dekken.
    "voordelen_kop": "Minder voorbewerking, delen die passen, een prijs die u kunt narekenen",

    # Exact vier panelen, kort gehouden zoals in MADEGRO (circa 110 tekens).
    # Alle vier gaan over iets wat de inkoper merkt: minder stappen, minder
    # pasmaken, herhaalbaarheid en een prijs volgens een vaste calculatie.
    "voordelen": [
        ("vinkje", "Minder losse bewerkingen",
         "Afkorten, gaten en uitsparingen komen uit &eacute;&eacute;n bewerking; vooraf zagen en naboren hoeft niet."),
        ("trap", "Minder pasmaken bij het lassen",
         "Delen met meegesneden aansluitingen hoeft u niet eerst passend te maken voordat er gelast kan worden."),
        ("lijst", "Herhaalorders uit hetzelfde bestand",
         "Een vervolgorder snijden wij uit het bestand van uw eerste aanvraag, dus het laatste stuk is gelijk aan het eerste."),
        ("document", "Prijs volgens vaste calculatie",
         "Standaardwerk offreert het portaal automatisch, dus u weet snel wat uw buiswerk kost &mdash; ook bij een herhaalaanvraag."),
    ],

    # Leeg. MADEGRO had hier drie samenwerkingspartners. Vorma Metaal heeft
    # alleen zusterbedrijf Tentije, en dat hoort bij assemblage, niet bij deze
    # bewerking; partners verzinnen mag niet. Het sjabloon vult deze plek met
    # de drie materialen.
    "partners": [],

    # Laatste sectie, dus de aanvraagfase: de kop vraagt om de opdracht en de
    # knop eronder is "Vraag een offerte aan". Even kort als de
    # MADEGRO-slotkoppen.
    "contact_kop": "Laat uw buiswerk bij ons snijden",

    # Exact vier vragen, en dit is de laatste sectie voor de offerteknop: ze
    # ruimen de twijfels op die een aanvraag tegenhouden - welke bestanden en
    # welk materiaal, wie de tekening beoordeelt en wanneer de prijs komt, wat
    # er na het versturen gebeurt en welke aantallen kunnen. De vragen staan in
    # de ik-vorm van de bezoeker. De antwoorden komen uit de brief; nergens een
    # termijn of tolerantie die daar niet staat.
    "faq": [
        ("Welk bestand en welk materiaal lever ik aan?", [
            "Het portaal leest STEP, DXF en DWG in, eventueel met een PDF-tekening erbij. Voor buis en profiel zegt een STEP-model het meest: daarin liggen de vorm van het profiel en de plaats van elke bewerking vast.",
            "Het materiaal kiest u in het portaal: staal, RVS of aluminium, met de kwaliteit erbij &mdash; bijvoorbeeld S235JR of RVS 304. De genoemde kwaliteiten zijn voorbeelden en geen voorraadlijst; bijzondere metalen zijn op aanvraag leverbaar.",
        ]),
        ("Wanneer krijg ik mijn prijs?", [
            "Wij controleren uw aanvraag zelf op maakbaarheid, voordat er een prijs uitgaat. Standaardwerk wordt automatisch geoffreerd: die offerte staat binnen enkele minuten online.",
            "Complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd; u wacht geen dagen op uw offerte. Wilt u uw buiswerk eerst bespreken, bel of mail ons dan.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag verstuur?", [
            "Uw aanvraag is vrijblijvend. Wij kijken of het onderdeel zo te maken is en nemen contact met u op als iets ontbreekt of onduidelijk is; het snijden begint pas na uw akkoord op de offerte.",
            "Daarna maken wij uw buiswerk in onze werkplaats, met de afgesproken nabewerking, en hoort u van ons wanneer het ertoe doet. Uw producten worden geleverd of staan klaar om in Goor af te halen.",
        ]),
        ("Kan ik ook &eacute;&eacute;n buis laten snijden?", [
            "Ja. Wij maken uniek maatwerk en series, van enkelstuks tot seriematige productie; ook voor &eacute;&eacute;n buis dient u gewoon een aanvraag in via het portaal.",
            "Wordt het een herhaalorder, dan snijden wij uit hetzelfde bestand en geldt dezelfde vaste calculatie, zodat u de prijs naast die van uw eerste aanvraag kunt leggen.",
        ]),
    ],
}
