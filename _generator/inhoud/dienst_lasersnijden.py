# -*- coding: utf-8 -*-
"""Inhoud van de dienstpagina Lasersnijden. Het skelet staat in bouw_service.py.

Enige bron voor de feiten: inhoud/BRIEF.md. De formulering is van ons: de
brontekst ("Nauwkeurig snijden van plaatmateriaal met de laser.") is input,
geen tekst om over te nemen. Lasersnijden gebeurt in eigen huis. Geen
machines, plaatdiktes, toleranties, capaciteit of levertijden voor de
productie: die staan nergens in de bron.

Aanspreekvorm "u", overal. Zie inhoud/COPY.md voor de vier toetsen.
"""

DIENST = {
    "bestand": "dienst-lasersnijden.html",
    "slug": "lasersnijden",
    "service_naam": "Lasersnijden",
    "service_naam_kort": "Lasersnijden",
    "namespace": "dienst-lasersnijden",
    "onderwerp": "lasersnijden",
    "titel": "Lasersnijden | Vorma Metaal",

    # Meta description: ca. 145 tekens. Zegt wat de bezoeker aanlevert, waarin
    # wij snijden, waar het gebeurt en welk bereik. Geen diktes of levertijden,
    # want die staan niet in de bron.
    "omschrijving": "Vorma Metaal snijdt plaatwerk op maat uit uw eigen CAD-bestand, in staal, RVS of aluminium. In eigen huis in Goor, van &eacute;&eacute;n stuk tot serie.",

    # Korte typering voor schema.org, zelfde soort lengte als de
    # MADEGRO-waarden ("Veiligheidsinspectie en audit").
    "service_type": "Lasersnijden van plaatmateriaal",

    "hero_foto": "lasersnijden",
    "eyebrow": "Dienst 01",

    # Twee alinea's, even lang als de MADEGRO-intro (ca. 230 en 270 tekens).
    # Eerste alinea is voor iemand die Vorma niet kent en misschien niet weet
    # wat lasersnijden is: eerst wat het bedrijf maakt, dan de bewerking in
    # gewone taal, dan wat de klant aanlevert (STEP, DXF, DWG uit de brief).
    # Tweede alinea: eigen huis plus de bewerkingen die er in dezelfde
    # werkplaats op volgen, met "kanten" uitgelegd. Assemblage staat hier
    # bewust niet bij, die loopt via Tentije. Vaktermen als kantlijn en tapgat
    # staan er niet in: die zeggen een inkoper wel iets en een ontwerper of
    # eerste bezoeker niets.
    "intro": "<p>Vorma Metaal maakt onderdelen van metaal op maat. Bij lasersnijden snijdt een laserstraal de vorm uit een vlakke plaat, precies zoals hij in uw tekening staat. U stuurt een STEP-, DXF- of DWG-bestand; wij snijden in staal, RVS of aluminium.</p>\n          <p>Het snijden doen wij in eigen huis, in dezelfde werkplaats waar uw plaat daarna gekant (in de gewenste vorm gezet), gelast of nabewerkt wordt. Zo loopt uw onderdeel op &eacute;&eacute;n aanvraag door alle bewerkingen die het nodig heeft, van &eacute;&eacute;n stuk tot een hele serie.</p>",

    # Eén zin boven de drie situatiekaarten, zelfde lengte als de
    # MADEGRO-inleiding op deze plek (ca. 160 tekens). Vat de drie kaarten
    # samen in plaats van ze aan te kondigen, zodat de zin zelf al iets zegt.
    # Geen "meestal" of ander aandeel: hoe de aanvragen zich verdelen staat
    # nergens in de bron en zou dus een verzonnen cijfer zijn.
    "wanneer_intro": "Drie situaties waarin lasersnijden bij ons past: een ontwerp dat klaar is om gemaakt te worden, een prototype dat later een serie wordt, of snijwerk dat nu los van het vervolg wordt ingekocht.",

    # Drie situaties uit het inkoopperspectief, elk ca. 190 tekens zoals de
    # MADEGRO-kaarten. De titels zijn hele mededelingen, geen labels: wie
    # alleen de kaartkoppen leest, weet welke drie gevallen dit zijn. Concreet
    # maar zonder specificaties: geen diktes, afmetingen of toleranties, want
    # die staan niet in de bron. De derde kaart gaat over losse leveranciers en
    # niet over materiaalkeuze, omdat de materiaalsectie verderop dat al doet.
    "herkenning": [
        ("Uw ontwerp is klaar, het onderdeel niet",
         "Het onderdeel bestaat nog alleen in CAD. Wij lezen uw STEP-, DXF- of DWG-bestand in, controleren of het maakbaar is en snijden de platen die eruit volgen."),
        ("Eerst &eacute;&eacute;n stuk, later een serie",
         "Eerst een prototype om te testen, dezelfde plaat later in serie. Bij een herhaalaanvraag offreren wij volgens dezelfde vaste calculatie, zodat u de prijs kunt vergelijken met de vorige keer."),
        ("Snijden hier, kanten bij een ander",
         "U koopt het snijden bij de een en het kanten of lassen bij de ander, en levert uw tekening twee keer aan. Bij ons gaan die bewerkingen door dezelfde werkplaats, op &eacute;&eacute;n aanvraag."),
    ],

    # Kop boven de vier treden. Noemt het aantal stappen, zodat de kop alleen
    # al vertelt wat er onder staat.
    "aanpak_kop": "Van CAD-bestand naar gesneden plaat in vier stappen",

    # Vier zinnen (ca. 275 tekens, als de MADEGRO-tekst) over het traject
    # rondom deze bewerking: aanvraag, maakbaarheidscontrole en offerte uit de
    # vijf stappen. De offertetermijn staat letterlijk in de brief; een
    # productielevertijd staat er niet en wordt dus niet genoemd.
    "aanpak_intro": "Uw aanvraag komt binnen via het portaal. Wij kijken eerst of de onderdelen maakbaar zijn en bellen u bij een complexe opdracht voordat de offerte uitgaat. Standaardwerk offreert het portaal automatisch, binnen enkele minuten. Pas na uw akkoord gaat het snijwerk de werkplaats in.",

    # Vier treden binnen deze bewerking, elk ca. 210 tekens zoals de
    # MADEGRO-treden. De titels zeggen wie wat doet, zodat de trap ook los te
    # lezen is; trede 01 spreekt van kiezen en niet van aanleveren, want het
    # materiaal komt van Vorma en de klant kiest het alleen in het portaal.
    # Detailregel blijft leeg (None): "herkenbaar gedrag" hoorde bij de
    # Veiligheidsladder en heeft hier geen tegenhanger.
    "stappen": [
        ("U uploadt uw tekening en kiest het materiaal",
         "U uploadt uw plaatonderdelen als STEP, DXF of DWG, eventueel met een PDF-tekening erbij, en kiest in het portaal het materiaal: staal, RVS of aluminium. Staat de kwaliteit die u nodig heeft er niet bij, vermeld dat dan bij de aanvraag.",
         None),
        ("Wij controleren de maakbaarheid",
         "Voordat er iets gesneden wordt, kijken wij of uw aanvraag maakbaar is. Bij een complexe opdracht stemmen wij eerst met u af, zodat een onduidelijkheid in de tekening geen onbruikbaar onderdeel oplevert.",
         None),
        ("Wij snijden in eigen huis",
         "Het snijwerk gebeurt in onze eigen werkplaats in Goor. Daarmee blijft uw plaat in beeld bij de mensen die hem daarna kanten, lassen of nabewerken, en gaat uw tekening niet naar een tweede leverancier.",
         None),
        ("Leveren, of door naar kanten en lassen",
         "Is snijden alles wat u nodig heeft, dan worden de platen geleverd of staan ze klaar om af te halen in Goor. Hoort er kanten, lassen of nabewerking bij, dan gaat uw werk intern door naar die bewerking; opnieuw aanvragen hoeft niet.",
         None),
    ],

    # Kop van de voordelensectie. Zegt wat de bezoeker eraan overhoudt in
    # plaats van dat er iets opgeleverd wordt; kanten en lassen zijn eigen
    # huis, dus de claim is waar.
    "voordelen_kop": "Uw plaat komt gesneden, gekant en gelast uit dezelfde werkplaats",

    # Vier korte panelen (ca. 100-120 tekens per tekst, als MADEGRO). Iconen
    # uit de vaste set in bouw_service.py. Alles staat in de brief: de
    # maakbaarheidscontrole, de drie bestandsformaten, het vrijblijvende
    # aanvragen en de vervolgbewerkingen in eigen huis. Geen materiaalpaneel,
    # want de materiaalsectie op deze pagina doet dat al. In paneel 03 staat
    # "draaien en frezen" en niet "verspanen": dezelfde bewerking uit de
    # brief, maar leesbaar voor iemand die geen metaalbewerker is.
    "voordelen": [
        ("vinkje", "Uw tekening eerst gecontroleerd",
         "Wij kijken of uw onderdeel maakbaar is voordat er gesneden wordt, en bellen u als de tekening vragen oproept."),
        ("document", "STEP, DXF en DWG worden ingelezen",
         "Uw eigen CAD-bestand gaat er direct in, eventueel met een PDF-tekening erbij. Overtekenen hoeft niet."),
        ("trap", "Kanten en lassen in hetzelfde pand",
         "Kanten, lassen, afbramen, draaien en frezen gebeuren in dezelfde werkplaats, dus uw plaat verhuist niet."),
        ("schild", "Aanvragen is vrijblijvend",
         "Een aanvraag verplicht u tot niets. Het snijden begint pas nadat u de offerte heeft goedgekeurd."),
    ],

    # LEEG. MADEGRO had hier drie samenwerkingspartners. Vorma Metaal heeft
    # alleen zusterbedrijf Tentije Industri&euml;le Automatisering B.V. en dat
    # staat in de lopende tekst. Partners verzinnen mag niet.
    "partners": [],

    # Kop van het slotblok. Dit is de aanvraagfase en de knop eronder is
    # "Vraag een offerte aan", dus de kop vraagt om de opdracht in plaats van
    # om herkenning. Zelfde lengte als "Wil je weten hoe je ervoor staat?".
    "contact_kop": "Laat uw plaatwerk bij ons snijden",

    # De vier vragen die iemand nog heeft vlak voordat hij aanvraagt:
    # bestanden, materiaal, aantallen en wat er na het versturen gebeurt. Die
    # laatste vervangt de oude afbraamvraag en beantwoordt in één keer wie de
    # tekening beoordeelt, wanneer de prijs komt en wanneer het werk start; de
    # nabewerking is verhuisd naar het antwoord over aantallen. Elk antwoord
    # twee alinea's van ca. 150-200 tekens. Alle feiten komen uit de brief.
    "faq": [
        ("Welke bestanden moet ik aanleveren?", [
            "STEP, DXF en DWG worden direct ingelezen; een PDF-tekening kunt u erbij uploaden. Overtekenen hoeft niet, dus u levert aan wat uw engineering al heeft liggen.",
            "Heeft u een ander formaat, of twijfelt u of uw bestand compleet is? Bel 0547 227 000 of mail info@vormametaal.nl, dan kijken wij eerst samen wat er nodig is.",
        ]),
        ("In welk materiaal kan mijn onderdeel gesneden worden?", [
            "Staal, RVS en aluminium. U kiest de kwaliteit bij uw aanvraag: in staal bijvoorbeeld DC01, S235JR of DX51D+Z, in RVS 304 en 316 met afwerking 2B of 1D, met of zonder beschermfolie.",
            "Dat zijn voorbeelden, geen voorraadlijst. Bijzondere metalen zijn op aanvraag leverbaar; staat uw materiaal niet in de lijst, vermeld het dan bij uw aanvraag of neem contact op.",
        ]),
        ("Kan ik &eacute;&eacute;n plaat laten snijden, of moet het een serie zijn?", [
            "Een enkel stuk mag. Wij snijden losse onderdelen en series naast elkaar; &eacute;&eacute;n plaat is net zo goed een aanvraag als een terugkerende serie.",
            "Vraagt u dezelfde onderdelen later opnieuw aan, dan geldt dezelfde vaste calculatie. Hoort er nabewerking bij, zoals afbramen, boren of tappen (schroefdraad maken), geef dat dan aan; het gaat mee in de offerte.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Wij controleren eerst of uw onderdelen maakbaar zijn. Standaardwerk offreert het portaal automatisch, binnen enkele minuten; complex werk en bijzondere materialen beoordelen wij persoonlijk.",
            "U krijgt een vrijblijvende offerte en beslist daarna. Pas na uw akkoord gaat het snijwerk de werkplaats in; daarna wordt het geleverd of staat het klaar om af te halen in Goor.",
        ]),
    ],
}
