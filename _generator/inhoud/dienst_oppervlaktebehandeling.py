# -*- coding: utf-8 -*-
# Inhoud van de dienstpagina Oppervlaktebehandeling. Het skelet staat in
# bouw_service.py en verandert niet: zelfde secties, zelfde volgorde, zelfde
# tekstlengtes als de MADEGRO-versie die hier vervangen wordt.
#
# Bron: BRIEF.md. De brontekst van vormametaal.nl is input, geen waarheid: de
# feiten blijven, de formulering is hier opnieuw geschreven op de vier toetsen
# uit COPY.md (begrijpelijk, zegt iets, conversie, relevant).
#
# Het feit dat niet mag schuiven: deze bewerking gebeurt NIET in eigen huis.
# Poedercoaten en andere oppervlaktebehandelingen worden uitbesteed en volledig
# door Vorma geregeld. Snijden, buissnijden, kanten, lassen, nabewerking en
# verspanen zijn wel eigen huis; samenbouwen loopt via zusterbedrijf Tentije.
#
# Wat hier bewust niet staat, omdat het niet in de bron staat: namen van
# behandelaars, laagdiktes, kleurcodes, voorbehandelingsmethodes, doorlooptijden
# voor de behandeling, garanties op de laag en capaciteit.

DIENST = {
    "bestand": "dienst-oppervlaktebehandeling.html",
    "slug": "oppervlaktebehandeling",
    "service_naam": "Oppervlaktebehandeling",
    "service_naam_kort": "Oppervlaktebehandeling",
    "namespace": "dienst-oppervlaktebehandeling",
    "onderwerp": "oppervlaktebehandeling",
    "titel": "Oppervlaktebehandeling | Vorma Metaal",

    # Meta description, ~150 tekens zoals de MADEGRO-versie. Zegt direct dat de
    # behandeling wordt uitbesteed en wat de klant er dan aan heeft, zodat de
    # zoekresultaatregel geen verwachting wekt die niet klopt.
    "omschrijving": "Poedercoaten en andere oppervlaktebehandelingen besteden wij uit en regelen wij volledig: uw onderdeel komt gesneden, gelast en behandeld uit &eacute;&eacute;n opdracht.",

    # Korte typering voor schema.org, zelfde lengte als de MADEGRO-waarden;
    # bewust geen claim dat de bewerking in eigen huis gebeurt.
    "service_type": "Oppervlaktebehandeling en poedercoaten",

    "hero_foto": "productiehal",
    "eyebrow": "Dienst 07",

    # Twee alinea's, zelfde lengte als de MADEGRO-intro. Toets 1: de bezoeker
    # kent Vorma niet en misschien de term niet. Alinea 1 legt in gewone taal
    # uit wat Vorma maakt, wat oppervlaktebehandeling is en dat wij die laag
    # niet zelf aanbrengen; alinea 2 zegt wat de klant daaraan heeft en waar de
    # behandeling in de route zit.
    "intro": '''          <p>Vorma Metaal maakt onderdelen op maat van staal, RVS en aluminium: wij snijden, zetten, lassen en verspanen. Oppervlaktebehandeling is de laag die daarna op het metaal komt, bijvoorbeeld poedercoat: een gekleurde poederlaag die op het onderdeel wordt gebakken. Die laag brengen wij niet zelf aan; wij besteden hem uit en regelen hem volledig.</p>
          <p>U zoekt dus zelf geen coatingbedrijf, plaatst geen tweede order en rijdt niets heen en weer. Wij snijden, kanten, lassen en bewerken na; daarna gaat uw werk in behandeling en komt het behandeld terug voor levering of afhalen.</p>''',

    # Een of twee zinnen die de drie kaarten hieronder inleiden, zoals MADEGRO.
    # Zegt wanneer deze bewerking aan de orde is. Geen uitspraak over hoe vaak
    # een behandeling nodig is: de bron zegt daar niets over.
    "wanneer_intro": "Poedercoaten of een andere behandeling is niet bij elk onderdeel nodig. In deze drie situaties wel &mdash; en dan zet u die het beste in dezelfde aanvraag.",

    # Drie situaties waarin een inkoper deze bewerking nodig heeft. De titel
    # benoemt de situatie zelf, zodat wie alleen de kaarten scant het herkent.
    # Geen laagdiktes, kleurcodes of normen: die staan niet in de bron.
    "herkenning": [
        ("Uw onderdeel moet in kleur geleverd worden",
         "Panelen, kasten en frames die in het zicht blijven, wilt u niet in onbehandeld metaal ontvangen. U geeft de kleur op bij de aanvraag; wij leveren de delen in die kleur af."),
        ("U wilt de coating niet zelf uitbesteden",
         "Coating zelf inkopen betekent een tweede order, eigen transport en twee partijen die naar elkaar kunnen wijzen. Bij ons zit de behandeling in dezelfde opdracht als het snij- en laswerk."),
        ("Uw onderdeel komt buiten of in een vochtige ruimte",
         "Onbehandeld staal kan al roesten voordat het gemonteerd is. Hoort er een beschermende laag op, dan gaat die behandeling mee met de rest van uw aanvraag."),
    ],

    # Kop van de aanpaksectie. Zegt zelfstandig wie wat doet: de behandeling
    # gebeurt elders, de regie ligt bij Vorma.
    "aanpak_kop": "Wij besteden de behandeling uit en sturen die aan",

    # Twee tot drie zinnen over de plek van deze bewerking in het traject van
    # aanvraag tot levering. Woorden uit de bron: maakbaarheid gecontroleerd,
    # vrijblijvende offerte, werk start na akkoord, geleverd of klaar om af te
    # halen.
    "aanpak_intro": "U geeft bij uw aanvraag op welke behandeling en kleur u wilt; wij controleren de maakbaarheid en zetten alles in &eacute;&eacute;n vrijblijvende offerte. Na uw akkoord maken wij de onderdelen en laten wij de behandeling uitvoeren. Daarna volgt levering of afhalen.",

    # Vier stappen binnen deze bewerking, zelfde lengte als de MADEGRO-treden.
    # Detail is None: de MADEGRO-driestapsvarianten hadden hier ook geen
    # gedragsregel. Elke trede-titel zegt wie de stap zet; de volgorde
    # (bewerken, dan behandelen) is het inhoudelijke punt van deze pagina.
    "stappen": [
        ("U geeft behandeling en kleur op",
         "Bij de aanvraag vermeldt u welke behandeling en kleur uw product nodig heeft, en welke vlakken, gaten of schroefdraden vrij moeten blijven. Dat geven wij door in de opdracht voor de behandeling.",
         None),
        ("Wij maken uw onderdelen in Goor",
         "Snijden, kanten, lassen, verspanen en de afgesproken nabewerking gebeuren in onze eigen werkplaats. Eerst al het snij-, boor- en laswerk, dan de behandeling: wie er daarna nog een gat in boort, beschadigt de laag.",
         None),
        ("Wij laten de behandeling uitvoeren",
         "Wij brengen de onderdelen naar het bedrijf dat de behandeling uitvoert en geven uw eisen mee. U plaatst geen tweede order en regelt geen transport; het contact daarover loopt via ons.",
         None),
        ("U ontvangt het behandelde werk",
         "Uw onderdelen worden geleverd of staan in Goor klaar om af te halen. Moet er nog samengebouwd worden, dan loopt dat via zusterbedrijf Tentije Industri&euml;le Automatisering B.V., in dezelfde werkplaats.",
         None),
    ],

    # Kop van de voordelensectie. Boven deze kop staat in het sjabloon al de
    # subtitel "Wat het oplevert", dus de kop zelf noemt de uitkomst en niet
    # nog een keer dat er iets oplevert.
    "voordelen_kop": "Behandeld werk zonder tweede leverancier",

    # Vier korte voordelen, elk &eacute;&eacute;n of twee zinnen zoals in de
    # MADEGRO-panelen. Geen kwaliteitsbelofte over de laag zelf, want daarover
    # staat niets in de bron; wel over de route en de regie. Vier gaat over de
    # aantallen, omdat "werken ze ook met kleine aantallen?" een vraag is die
    # een eerste bezoeker heeft en die anders alleen in de FAQ antwoord krijgt.
    "voordelen": [
        ("mensen", "U belt &eacute;&eacute;n partij",
         "De behandeling gebeurt buiten de deur, maar het contact loopt via ons. U hoeft er zelf niet achteraan."),
        ("document", "Behandeling in dezelfde offerte",
         "Snij-, kant- en laswerk en de behandeling staan in &eacute;&eacute;n prijs. Een losse order ernaast is niet nodig."),
        ("lijst", "Eerst bewerken, dan behandelen",
         "Boren, tappen en lassen doen wij voordat de laag erop komt, zodat er geen gereedschap meer door de coating gaat."),
        ("grafiek", "Ook een enkel stuk gaat behandeld de deur uit",
         "Wij maken uniek maatwerk en series; de behandeling regelen wij bij elk aantal op dezelfde manier."),
    ],

    # Leeg. MADEGRO had hier drie samenwerkingspartners; Vorma Metaal heeft
    # alleen zusterbedrijf Tentije en dat staat al in de laatste trede.
    # Namen van behandelaars staan niet in de bron en worden dus niet verzonnen.
    "partners": [],

    # Laatste sectie van de pagina, dus de aanvraagfase; de knop eronder is
    # "Vraag een offerte aan". Deze kop vraagt om de opdracht.
    "contact_kop": "Vraag uw metaalwerk inclusief behandeling aan",

    # Vier vragen die iemand nog heeft voordat hij op verzenden
    # drukt: welke bestanden en welk materiaal, wie de tekening beoordeelt en
    # wanneer de prijs komt, welke aantallen kunnen, en wat er na het versturen
    # gebeurt. Geen algemeenheden en geen termijn die niet in de bron staat.
    "faq": [
        ("Welke bestanden en gegevens heeft u van mij nodig?", [
            "Uw onderdelen als STEP-, DXF- of DWG-bestand, eventueel met een PDF-tekening erbij. In het portaal kiest u het materiaal: staal, RVS of aluminium; bijzondere metalen zijn op aanvraag leverbaar.",
            "Vermeld daarbij welke behandeling u wilt, in welke kleur, en welke vlakken, gaten of schroefdraden vrij moeten blijven. Overtekenen hoeft niet: uw eigen CAD-bestand wordt direct ingelezen.",
        ]),
        ("Wie beoordeelt mijn tekening en wanneer weet ik de prijs?", [
            "Wij controleren eerst of uw aanvraag maakbaar is. Bij een complexe opdracht stemmen wij met u af voordat de offerte uitgaat, zodat een onduidelijkheid in de tekening geen onbruikbaar onderdeel wordt.",
            "Standaardwerk offreert het portaal automatisch: die offerte staat binnen enkele minuten online. Complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd; u wacht geen dagen.",
        ]),
        ("Kan ik &eacute;&eacute;n stuk laten behandelen of alleen series?", [
            "Ook &eacute;&eacute;n stuk. Wij maken uniek maatwerk en series, van enkelstuks tot seriematige productie; de behandeling hoort in beide gevallen bij dezelfde opdracht.",
            "Komt hetzelfde onderdeel later opnieuw langs, dan geldt dezelfde vaste calculatie. Bij een herhaalaanvraag hoeft u dus niet opnieuw over de prijs te praten.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Wij nemen hem in behandeling, controleren de maakbaarheid en sturen u een vrijblijvende offerte. Het werk start pas na uw akkoord; daarna maken wij de onderdelen in onze werkplaats in Goor.",
            "Het poedercoaten of een andere behandeling besteden wij uit en sturen wij aan; u zoekt daarvoor zelf geen leverancier. Daarna worden uw producten geleverd of staan ze klaar om af te halen.",
        ]),
    ],
}
