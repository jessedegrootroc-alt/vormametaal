# -*- coding: utf-8 -*-
"""Inhoud van materialen.html. Het skelet staat in bouw_rest.bouw_materialen()
en verandert niet: het MADEGRO-overzichtssjabloon van cursusaanbod.html, met
patroonhero, introband, een paneelrij, een vlakkenrij, de FAQ en het slotblok.

Enige bron voor de feiten: inhoud/BRIEF.md. Welke MADEGRO-component welke
Vorma-inhoud krijgt staat in inhoud/MAPPING.md; deze pagina is nieuw en leent
het overzichtssjabloon, dus de tekstlengtes zijn afgestemd op de plekken die
dat sjabloon al vulde (intro ca. 230-270 tekens per alinea, paneeltekst ca.
120, vlaktekst ca. 120, FAQ-antwoorden 130-190).

De pagina antwoordt op twee vragen: in welk materiaal kan mijn onderdeel, en
wat als mijn materiaal er niet bij staat. De koppen zijn daarop geschreven,
zodat iemand die alleen de koppen scant beide antwoorden ziet.

De brief geeft drie materialen met een typering en voorbeeldkwaliteiten. Die
drie teksten en die kwaliteiten staan in de panelen woord voor woord zoals ze
in de bron staan: er is niets bijgeschreven en niets weggelaten. Het zijn
voorbeeldkwaliteiten en geen voorraadlijst, en dat staat er ook bij. In de
vlakken en de FAQ staat dezelfde inhoud in gewone taal, vanuit de vraag
"wanneer kies ik dit?"; er is daar geen eigenschap bijgekomen.

Wat hier bewust NIET staat, omdat het nergens in de bron staat: plaatdiktes,
maximale afmetingen, toleranties, machines of machinemerken, certificeringen,
levertijden voor de productie, capaciteit, voorraad, klantnamen en cases. Er
staat dus ook nergens tot welke dikte of in welk formaat een materiaal
geleverd kan worden.

Eigen huis versus uitbesteed: lasersnijden, buislasersnijden, kanten, lassen,
nabewerking en CNC-verspanen gebeuren in eigen huis; assemblage loopt via
zusterbedrijf Tentije Industri&euml;le Automatisering B.V.;
oppervlaktebehandeling wordt uitbesteed maar volledig door Vorma geregeld.
Deze pagina gaat over materiaal en niet over bewerkingen, dus die verdeling
komt hier niet in beeld en wordt ook niet aangeraakt.

Aanspreekvorm "u", overal. Zie inhoud/COPY.md voor de vier toetsen.
"""

MATERIALEN_PAGINA = {
    "bestand": "materialen.html",
    "namespace": "materialen",
    "titel": "Materialen | Vorma Metaal",

    # Meta description: 150 tekens, als de andere pagina's (145-150). Noemt
    # eerst de drie materialen (daarop wordt gezocht) en de
    # voorbeeldkwaliteiten, en daarna de tweede vraag van deze pagina: wat als
    # uw metaal er niet bij staat. Geen diktes, formaten of voorraad, want die
    # staan niet in de bron.
    "omschrijving": "Vorma Metaal verwerkt staal, RVS en aluminium, met per materiaal de voorbeeldkwaliteiten. Staat uw metaal er niet bij? Bijzondere metalen op aanvraag.",

    # De <h1> was tweemaal "Materialen": hetzelfde woord als het label erboven,
    # dus de kop voegde niets toe. Hij zegt nu waar de pagina antwoord op geeft
    # en blijft binnen de lengte van de andere paginahero's (40 tekens, tegen 49
    # op diensten.html). "Staal, RVS en aluminium" staat bewust niet hier: dat
    # is de vaste kop van de paneelrij verderop.
    "hero_label": "Materialen",
    "hero_titel": "In welk materiaal wij uw onderdeel maken",

    # Kop van de introband, 41 tekens, als de section-heading die hier bij
    # MADEGRO stond. De twee alinea's eronder gaan over kiezen: welke
    # materialen er zijn en hoe u uw keuze doorgeeft. De kop dekt dat en
    # herhaalt de <h1> niet.
    "intro_kop": "Zo kiest u het materiaal voor uw aanvraag",

    # Twee alinea's van ca. 250 tekens, tegen 230 en 270 op deze plek in het
    # sjabloon. De eerste alinea begint met wat Vorma maakt en niet met "wij
    # verwerken": wie hier via een zoekopdracht op materiaal binnenkomt, kent
    # het bedrijf niet. Daarna de drie materialen en de waarschuwing dat de
    # kwaliteiten voorbeelden zijn en geen voorraadlijst. Tweede alinea: het
    # portaal, de bijzondere metalen op aanvraag, wat u doet als uw metaal er
    # niet bij staat, en de maakbaarheidscontrole uit stap 2 van de brief. Er
    # is geen uitspraak over voorraad, dikte of formaat bij verzonnen.
    # "Onderdelen op maat" stond hier eerst; dat is de holle claim uit COPY.md
    # en is nu "onderdelen uit uw eigen CAD-bestand", wat hetzelfde zegt en
    # meteen laat zien hoe u een onderdeel aanlevert.
    "intro_tekst": "<p>U kiest het materiaal in het portaal, tijdens het uploaden van uw tekening. Uw keuze gaat mee in de calculatie, dus hij bepaalt mede wat de offerte wordt.</p>\n            <p>Hieronder staat per materiaal waarvoor het geschikt is, met voorbeeldkwaliteiten. Dat is geen voorraadlijst: welke kwaliteit uw onderdeel nodig heeft, geeft u zelf op bij uw aanvraag.</p>",

    # De drie materialen in de volgorde van de brief, in panel-row--3. De
    # typering en de kwaliteiten zijn woord voor woord de brontekst: dit is
    # materiaalinformatie waar een inkoper op afrekent, dus hier wordt niet
    # geherformuleerd. De teksten zijn 91 tot 124 tekens en passen daarmee in
    # de paneeltekst, die bij MADEGRO 110 tot 130 tekens droeg. Het nummer
    # vult panel__meta, waar bij de dienstkaarten "Dienst 01" staat.
    "materialen": [
        {"nr": "01",
         "naam": "Staal",
         "eigenschap": "Sterk en veelzijdig",
         "tekst": "Sterk, veelzijdig en geschikt voor uiteenlopende constructieve en industri&euml;le toepassingen.",
         "kwaliteiten": ["DC01", "DD11", "S235JR", "S355MC", "DX51D+Z (sendzimir verzinkt)"]},
        {"nr": "02",
         "naam": "RVS",
         "eigenschap": "Corrosiebestendig",
         "tekst": "Corrosiebestendig en duurzaam materiaal voor toepassingen waar hygi&euml;ne, uitstraling en een lange levensduur belangrijk zijn.",
         "kwaliteiten": ["RVS 304", "RVS 316", "Afwerking 2B of 1D, met of zonder beschermfolie"]},
        {"nr": "03",
         "naam": "Aluminium",
         "eigenschap": "Lichtgewicht en sterk",
         "tekst": "Lichtgewicht, sterk en goed te bewerken, met een uitstekende verhouding tussen gewicht en sterkte.",
         "kwaliteiten": ["EN AW-1050A", "EN AW-5005 (AlMg1)", "EN AW-5754 H111", "EN AW-5083"]},
    ],

    # De vlakkenrij onder de kop "Wanneer welk materiaal" (die kop staat vast in
    # bouw_rest.py). Vier vlakken: drie keuzemomenten en het vierde voor wat er
    # buiten de lijst valt. De koppen zijn 11 tot 17 tekens, want vlak__kop
    # staat op 24px in een kolom van een kwart scherm en breekt daarboven; de
    # teksten zijn 121 tot 128 tekens, zoals de waardenvlakken bij MADEGRO.
    # De eigenschappen per materiaal zijn dezelfde als in de panelen hierboven,
    # maar hier vanuit de vraag "wanneer kies ik dit?" geformuleerd, in gewone
    # taal: "niet mag roesten" in plaats van "corrosiebestendig", "verzinkt"
    # bij DX51D+Z in plaats van "sendzimir verzinkt", en "glad (2B) of mat
    # (1D)" bij de RVS-afwerking, want die codes zeggen een ontwerper niets.
    # De exacte bronterm staat in het paneel erboven. Er staat geen sector,
    # toepassing of eigenschap bij die niet in de bron voorkomt.
    #
    # De kwaliteiten worden hier opgesomd ("kwaliteiten als", "legeringen
    # als") en niet als reeks ("van DC01 tot S355MC"): het zijn losse
    # voorbeelden uit de bron en geen doorlopend assortiment.
    #
    # Het vierde vlak heet niet meer "Bijzondere metalen" maar stelt de vraag
    # die de bezoeker hier heeft: staat mijn metaal er niet bij? Het geeft de
    # route en wat er dan gebeurt (persoonlijke beoordeling), zodat het geen
    # derde herhaling van de introalinea is.
    "vlakken": [
        ("Wanneer staal",
         "Als sterkte de eis is, voor constructie- en industriewerk."),
        ("Wanneer RVS",
         "Als het onderdeel niet mag roesten, of als uitstraling en levensduur meewegen."),
        ("Wanneer aluminium",
         "Als gewicht meetelt en het onderdeel toch sterk moet zijn."),
        ("Niet in de lijst?",
         "Bijzondere metalen zijn op aanvraag leverbaar; zo&rsquo;n opdracht beoordelen wij persoonlijk."),
    ],

    # Drie vragen in de volgorde waarin de bezoeker ze stelt: wat kan er, kan
    # ook iets anders, en hoe geef ik het op. De tweede vraag was "Zijn dit alle
    # kwaliteiten die u kunt verwerken?"; dat is nu de vraag zoals iemand hem
    # werkelijk stelt, en het "voorbeelden, geen voorraadlijst" is naar de
    # eerste vraag verhuisd, waar het over de lijst zelf gaat. De zeven vaste
    # vragen uit de brief horen bij de homepage; dit zijn de vragen die op deze
    # pagina overblijven. Elk antwoord twee alinea's van 132 tot 162 tekens, als
    # de MADEGRO-antwoorden (169 en 194) maar iets korter omdat het er twee per
    # vraag zijn. Alle feiten komen uit de brief: de drie materialen, de
    # voorbeeldkwaliteiten, bijzondere metalen op aanvraag, het portaal met
    # STEP, DXF en DWG, de maakbaarheidscontrole, de vaste calculatie en de
    # offertetermijn voor standaardwerk. Geen voorraad, geen prijs, geen
    # minimumafname, geen levertijd. De derde vraag gaat over opgeven, dus het
    # antwoord blijft daarbij: de tweede alinea zegt wat er met die keuze
    # gebeurt en dwaalt niet af naar de offerte in het algemeen.
    "faq": [
        ("In welke materialen kunt u mijn onderdeel maken?", [
            "Staal, RVS en aluminium. Alle acht bewerkingen gelden voor alle drie: wat wij uit staal snijden, kanten en lassen, doen wij ook uit RVS en aluminium.",
            "Welke kwaliteit binnen dat materiaal, bepaalt u. De voorbeelden hierboven geven de richting; uw eigen opgave is wat wij aanhouden.",
        ]),
        ("Kunt u ook een metaal verwerken dat er niet bij staat?", [
            "Vermeld het gewenste metaal bij uw aanvraag of bel 0547 227 000, dan bekijken wij het aan de hand van uw tekening.",
            "Zo&rsquo;n aanvraag gaat niet automatisch door de calculatie. Wij beoordelen hem persoonlijk, samen met de vraag of uw onderdeel maakbaar is zoals het getekend staat.",
        ]),
        ("Hoe geef ik het materiaal op bij mijn aanvraag?", [
            "Bij het uploaden van uw STEP-, DXF- of DWG-bestand, eventueel met een PDF-tekening erbij.",
            "Staat de kwaliteit die u nodig heeft niet in de keuzelijst, zet hem dan bij de aanvraag in het bericht. Dan houden wij die aan in plaats van de standaard.",
        ]),
    ],

    # Kop van het slotblok. De knop eronder staat vast op "Vraag een offerte
    # aan", dus dit is de aanvraagfase en de kop vraagt om de opdracht in
    # plaats van een vraag te stellen waarop "nee" een antwoord is. 49 tekens,
    # als de contactkoppen op de dienstpagina's (33 tot 45). Wie nog twijfelt
    # over het materiaal wordt opgevangen door de vaste regel eronder, die
    # zegt dat u ook eerst uw vraag kunt stellen.
    "contact_kop": "Laat uw onderdeel in staal, RVS of aluminium maken",
}
