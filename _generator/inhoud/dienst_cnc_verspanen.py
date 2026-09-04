# -*- coding: utf-8 -*-
"""Inhoud van de dienstpagina CNC-verspanen. Het skelet staat in bouw_service.py.

Feit uit BRIEF.md: draaien en frezen doet Vorma IN EIGEN HUIS. De brontekst van
vormametaal.nl is input, geen waarheid: de feiten blijven, de formulering is
hier opnieuw geschreven volgens COPY.md. Geen machines, maten, toleranties,
levertijden, certificeringen, klanten of cases. Aanspreekvorm &ldquo;u&rdquo;.

De pagina loopt van begrijpen naar aanvragen: de intro legt uit wat Vorma doet
en wat verspanen is, de middensecties nemen twijfel weg over bestand, materiaal
en aantallen, de FAQ ruimt op wat vlak voor een aanvraag nog onzeker is, en de
slotkop vraagt om de opdracht.
"""

DIENST = {
    "bestand": "dienst-cnc-verspanen.html",
    "slug": "cnc-verspanen",
    "service_naam": "CNC-verspanen",
    "service_naam_kort": "CNC-verspanen",
    "namespace": "dienst-cnc-verspanen",
    "onderwerp": "cnc-verspanen",
    "titel": "CNC-verspanen | Vorma Metaal",

    # Meta description, 120-155 tekens. Noemt de bewerking, de plaats, de drie
    # materialen uit BRIEF.md en het bereik enkelstuks-serie: dat zijn de vier
    # dingen waarop een inkoper zoekt. Geen belofte over termijn of capaciteit.
    "omschrijving": "Draaien en frezen in eigen huis bij Vorma Metaal in Goor: nauwkeurig verspaande onderdelen in staal, RVS en aluminium, enkelstuks of serie.",

    # Korte typering voor schema.org serviceType, zonder marketingwoorden.
    "service_type": "CNC-draaien en -frezen van metaalonderdelen",

    "hero_foto": "verspanen",
    "eyebrow": "Dienst 08",

    # Twee alinea's, net als de MADEGRO-intro elk twee zinnen. Alinea 1 is voor
    # iemand die Vorma niet kent en misschien niet weet wat verspanen is: eerst
    # wat het bedrijf doet, dan de bewerking in gewone taal. Alinea 2 zegt wat
    # de bezoeker eraan heeft: &eacute;&eacute;n aanvraag in plaats van twee
    # leveranciers. Geen onderdeelsoorten: BRIEF.md noemt geen enkel product.
    "intro": '''          <p>Vorma Metaal maakt onderdelen van metaal in opdracht, in onze eigen werkplaats in Goor. CNC-verspanen is de bewerking waarbij een computergestuurde machine materiaal wegneemt uit een massief stuk staal, RVS of aluminium: draaien en frezen, tot het deel de vorm en de maten van uw tekening heeft.</p>
          <p>Dat verspaanwerk doen wij zelf, in dezelfde werkplaats waar wij plaat snijden, kanten (in de gewenste vorm zetten), lassen en nabewerken. Hoort er bij uw gedraaide of gefreesde deel ook plaatwerk, dan is dat &eacute;&eacute;n aanvraag en &eacute;&eacute;n offerte in plaats van twee leveranciers.</p>''',

    # Deze regel noemt de drie situaties zelf, in plaats van aan te kondigen dat
    # er drie volgen; dan zegt de tekst iets ook voor wie de kaarten niet leest.
    # Deze sectie hoort bij de begrijpen-fase, dus geen aanvraagoproep in de
    # tekst: de bezoeker wil hier eerst weten of zijn onderdeel hier kan.
    # Geen urgentie en geen aantallen.
    "wanneer_intro": "Draai- en freeswerk komt in beeld als een onderdeel niet uit plaat te maken is, als het bij plaatwerk in dezelfde samenstelling hoort, of als er na &eacute;&eacute;n stuk een serie volgt. In alle drie de gevallen draaien en frezen wij het hier, in staal, RVS of aluminium.",

    # Drie situaties waarin een klant juist deze bewerking nodig heeft. De
    # titels zeggen los van de tekst eronder al wat de situatie is, in gewone
    # woorden: uit een massief stuk, binnen een samenstelling, en de stap van
    # enkelstuk naar serie. Geen maten, toleranties of onderdeelsoorten, want
    # die staan niet in BRIEF.md.
    "herkenning": [
        ("Uw onderdeel moet uit een massief stuk komen",
         "Wat niet uit plaat te snijden en te kanten is, ontstaat door metaal weg te nemen uit een massief stuk. Dat draaien en frezen doen wij in onze eigen werkplaats."),
        ("Uw samenstelling bevat gedraaide of gefreesde delen",
         "In &eacute;&eacute;n samenstelling zitten vaak gesneden platen, gezette delen en daarnaast een paar gedraaide of gefreesde onderdelen. Die komen hier uit dezelfde werkplaats."),
        ("Eerst &eacute;&eacute;n stuk, daarna een serie",
         "Tijdens het ontwerpen wilt u eerst &eacute;&eacute;n onderdeel om te proberen; werkt het, dan volgt dezelfde tekening in serie. Wij maken beide."),
    ],

    "aanpak_kop": "Van uw STEP-bestand tot een verspaand onderdeel",

    # Drie zinnen, zelfde lengte als de MADEGRO-aanpaktekst. Volgt de vijf
    # stappen uit BRIEF.md (aanvraag, controle, offerte, productie, levering),
    # maar toegespitst op verspanen: bij draai- en freeswerk is het 3D-bestand
    # met tekening het startpunt.
    "aanpak_intro": "U uploadt uw bestand in het portaal: STEP, DXF of DWG, eventueel met een PDF-tekening erbij. Wij controleren eerst of het onderdeel te maken is en bellen u bij een complexe opdracht voordat de offerte uitgaat. Die offerte is vrijblijvend; na uw akkoord gaat het werk de werkplaats in.",

    # Vier stappen binnen deze bewerking, in de volgorde die de klant meemaakt.
    # De titels zeggen wie wat doet, zodat de trap ook los te scannen is. De
    # offertetermijn staat er zoals BRIEF.md hem geeft; over de productietijd
    # staat niets, want dat is nergens vermeld. Detail blijft None: de
    # trede-regel &ldquo;Herkenbaar gedrag&rdquo; hoort bij MADEGRO.
    "stappen": [
        ("U uploadt uw bestand en kiest het materiaal",
         "In het portaal laadt u uw STEP-, DXF- of DWG-bestand in en kiest u staal, RVS of aluminium. Een PDF-tekening erbij helpt, want daarop staat welke maten precies moeten passen.",
         None),
        ("Wij controleren of uw onderdeel te maken is",
         "Wij kijken of het onderdeel te draaien of te frezen is zoals het getekend staat. Loopt er iets niet, dan bellen of mailen wij u daarover voordat u een offerte krijgt.",
         None),
        ("U ontvangt de offerte en beslist",
         "Standaardwerk wordt automatisch geoffreerd en staat binnen enkele minuten online. Een complexe opdracht of een bijzonder materiaal beoordelen wij persoonlijk. Het werk start pas na uw akkoord.",
         None),
        ("Wij draaien of frezen, bewerken na en leveren",
         "Het onderdeel wordt in onze werkplaats gedraaid of gefreesd en waar afgesproken nabewerkt: afbramen, tappen, boren of verzinken. Daarna leveren wij het, of het staat klaar om af te halen.",
         None),
    ],

    # De subtitel boven deze kop is &ldquo;Wat het oplevert&rdquo;; de kop zelf
    # zegt daarom wat de bezoeker overhoudt, niet nog een keer het thema.
    "voordelen_kop": "Uw verspaande deel komt uit dezelfde werkplaats als uw plaatwerk",

    # Vier panelen, tekst zo kort als bij MADEGRO (&eacute;&eacute;n of twee
    # korte zinnen). Alle vier onderbouwd door BRIEF.md: eigen huis, de zes
    # bewerkingen die Vorma zelf doet (assemblage loopt via Tentije,
    # oppervlaktebehandeling is uitbesteed), enkelstuks tot series, en de
    # herkomst: 22 jaar, Tentije, 2004 in Goor, dezelfde werkplaats en hetzelfde
    # team. Geen garanties, termijnen of capaciteit.
    "voordelen": [
        ("schild", "Draaien en frezen in eigen huis",
         "Uw onderdeel wordt hier verspaand en niet doorgestuurd. Een vraag erover loopt dus niet via een tussenpartij."),
        ("lijst", "Zes bewerkingen in eigen huis",
         "Lasersnijden, buislasersnijden, kanten, lassen, nabewerking en verspanen: &eacute;&eacute;n aanvraag, &eacute;&eacute;n offerte."),
        ("grafiek", "Van &eacute;&eacute;n stuk tot serie",
         "Eerst &eacute;&eacute;n onderdeel om te proberen, later dezelfde tekening in seriematige productie."),
        ("mensen", "22 jaar in machinebouw en automatisering",
         "Vorma Metaal komt voort uit Tentije Industri&euml;le Automatisering, in 2004 opgericht in Goor. Wij delen werkplaats en team."),
    ],

    # LEEG en dat blijft zo. MADEGRO had hier drie samenwerkingspartners; Vorma
    # Metaal heeft alleen zusterbedrijf Tentije Industri&euml;le Automatisering
    # B.V., en dat staat al in de FAQ. Partners verzinnen mag niet.
    "partners": [],

    # Laatste sectie, dus de aanvraagfase; de knop eronder is de offerte. Deze
    # kop vraagt om de opdracht in plaats van naar een situatie.
    "contact_kop": "Laat uw draai- en freeswerk bij ons maken",

    # De vier vragen die vlak voor een aanvraag nog onzekerheid geven: welk
    # bestand, welk materiaal en welke aantallen, wie de tekening beoordeelt en
    # wanneer de prijs komt, en wat er na het versturen gebeurt. Elk antwoord
    # blijft binnen BRIEF.md; de laatste zet de rolverdeling goed neer
    # (verspanen en nabewerking eigen huis, assemblage via Tentije,
    # oppervlaktebehandeling uitbesteed maar door ons geregeld).
    "faq": [
        ("Welk bestand heeft u van mij nodig?", [
            "Ons portaal leest STEP, DXF en DWG in. In een STEP-bestand ligt uw onderdeel in drie dimensies vast, dus met de vorm van alle kanten.",
            "Voeg een PDF-tekening bij als er maten zijn die precies moeten passen. Twijfelt u of uw aanvraag compleet is, bel of mail ons dan voordat u hem verstuurt.",
        ]),
        ("In welk materiaal en in welke aantallen kunt u verspanen?", [
            "Wij verwerken staal, RVS en aluminium; bijzondere metalen zijn op aanvraag leverbaar. Het materiaal kiest u bij uw aanvraag in het portaal; staat het er niet bij, vermeld het dan of neem contact op.",
            "Wij maken uniek maatwerk en series, van enkelstuks tot seriematige productie; ook voor &eacute;&eacute;n gedraaid deel kunt u een aanvraag indienen. Komt dezelfde tekening later opnieuw langs, dan offreren wij volgens dezelfde vaste calculatie.",
        ]),
        ("Wie beoordeelt mijn tekening, en wanneer krijg ik de prijs?", [
            "Wij controleren uw aanvraag eerst op maakbaarheid. Is de opdracht complex of het materiaal bijzonder, dan beoordelen wij hem persoonlijk en stemmen wij met u af voordat de offerte uitgaat.",
            "Standaardwerk wordt automatisch geoffreerd; die offerte staat binnen enkele minuten online. Complexe aanvragen volgen binnen korte tijd, u wacht geen dagen. De offerte is vrijblijvend.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Na uw akkoord op de offerte gaat het onderdeel de werkplaats in: draaien of frezen, plus de nabewerking die is afgesproken: afbramen, tappen, boren of verzinken. Daarna leveren wij het, of het staat klaar om af te halen.",
            "Moet er meer gebeuren, dan regelen wij dat. Samenbouwen tot een complete samenstelling loopt via ons zusterbedrijf Tentije Industri&euml;le Automatisering B.V.; poedercoaten en andere oppervlaktebehandelingen besteden wij uit en co&ouml;rdineren wij voor u.",
        ]),
    ],
}
