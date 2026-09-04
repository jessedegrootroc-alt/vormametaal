# -*- coding: utf-8 -*-
"""Inhoud van de homepage. Het skelet staat in bouw_home.py en verandert niet:
de twaalf secties van de template in dezelfde volgorde, plus de
projectensectie direct onder de materialen.

Enige bron voor de feiten: inhoud/BRIEF.md. Welke MADEGRO-component welke
Vorma-inhoud krijgt staat in inhoud/MAPPING.md.

Wat hier bewust NIET staat, omdat het nergens in de bron staat: machines of
machinemerken, plaatdiktes, afmetingen, toleranties, certificeringen (ISO,
VCA), klantnamen, logo's, citaten, cases, projecten, aantallen klanten of
medewerkers, productielevertijden, garanties en capaciteit.

Eigen huis versus uitbesteed, en dat is de belangrijkste val op deze pagina:
lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen
gebeuren in eigen huis; assemblage loopt via zusterbedrijf Tentije
Industri&euml;le Automatisering B.V.; oppervlaktebehandeling wordt uitbesteed
maar volledig door Vorma geregeld. De bron zelf vat alle acht samen als
&ldquo;onder &eacute;&eacute;n dak&rdquo;; die formulering wordt hier gebruikt
waar het over de acht gaat, en &ldquo;in eigen huis&rdquo; alleen waar het over
de zes gaat.

Waar de <p>-tags horen, en waar niet: bouw_home.py zet wat_tekst, diensten_tekst
en waarom_intro zelf in een <p>, dus die drie velden zijn platte tekst zonder
tags. hero_intro en over_tekst komen in een div met de klasse article-body en
dragen hun eigen <p>-alinea's.

Drie sleutels blijven staan omdat het bouwscript op de sleutelverzameling
rekent, maar bouw_home.py rendert ze op de homepage niet: wat_eyebrow, wat_kop
(dit component heeft geen kopslot) en werkwijze_eyebrow.
De vijf stappen in "stappen" staan hier om dezelfde reden; op de homepage draagt
s03 alleen tekst met beeld en verwijst de knop naar werkwijze.html, waar de
stappen wel als treden staan.
"""

HOME = {
    "titel": "Vorma Metaal | Wij geven vorm aan uw metaal",

    # Meta description: 139 tekens. Opent met plaats en wat er gemaakt wordt,
    # dan de bewerkingen die een inkoper intypt, dan de eerste stap. Geen
    # diktes, levertijden of aantallen, want die staan niet in de bron.
    "omschrijving": "Vorma Metaal in Goor maakt onderdelen van metaal op maat: lasersnijden, kanten, lassen en CNC-verspanen. Vraag aan met uw eigen CAD-bestand.",

    # ---------------------------------------------------------------- s01 hero
    # Kort label boven de kop, waar MADEGRO "Veiligheidskunde en kwaliteit"
    # had. Zegt in drie woorden wat het bedrijf verkoopt.
    "hero_eyebrow": "Maatwerk in metaal",

    "hero_h1": "Wij geven vorm aan uw metaal",

    # Twee alinea's, zelfde lengte als de MADEGRO-hero-intro (191 en 186
    # tekens). De eerste alinea zegt eerst w&aacute;t u hier kunt laten maken
    # (plaatwerk, buiswerk, verspaand werk, samenstellingen) en pas daarna met
    # welke bewerkingen; dat is de volgorde waarin een bezoeker kijkt. "Onder
    # &eacute;&eacute;n dak" is de samenvatting van de bron zelf voor alle
    # acht, dus er wordt niet beweerd dat alle acht in eigen huis gebeuren; s02
    # en s04 splitsen dat meteen uit. De tweede alinea zegt voor wie en hoe een
    # aanvraag begint, met de inleesformaten in plaats van het vage
    # "CAD-bestand", zodat de bezoeker weet of hij het juiste bestand heeft.
    "hero_intro": "<p>Vorma Metaal maakt onderdelen van metaal op maat: plaatwerk, buis- en profielwerk, verspaande delen en complete samenstellingen. Acht bewerkingen, van lasersnijden tot lassen en verspanen, onder &eacute;&eacute;n dak.</p>\n          <p>Wij werken voor zakelijke opdrachtgevers die metaalwerk op tekening nodig hebben. Uw aanvraag begint bij het bestand dat u al heeft liggen.</p>",

    # Knop 1 is de aanvraagfase, knop 2 de begrijpfase. "Wat wij doen" zei niet
    # waar de knop heen ging; deze wel. De knop van s07 heet "Bekijk alle
    # bewerkingen" en gaat naar dezelfde pagina, dus dit label is korter
    # gehouden om die twee niet identiek te maken.
    "hero_knop1": "Offerte aanvragen",
    "hero_knop2": "Bekijk de bewerkingen",

    # ------------------------------------------------------- s02 wat we doen
    # Deze twee sleutels blijven staan voor de sleutelverzameling, maar
    # bouw_home.py rendert ze niet: dit MADEGRO-component heeft alleen een
    # tekstslot en geen kop. De tekst eronder moet het dus alleen doen.
    "wat_eyebrow": "Wat wij doen",
    "wat_kop": "Metaalwerk van aanvraag tot eindproduct",

    # E&eacute;n alinea van ca. 195 tekens, tegen 257 bij MADEGRO. Platte tekst
    # zonder <p>: bouw_home.py zet dit veld zelf in een <p>. Het blok staat in
    # de grote lichte snede (2,25rem), dus dit is de eerste tekst die iemand
    # leest die nog niets van Vorma weet. Daarom in deze orde: wat het bedrijf
    # is, waar het staat, wat u aanlevert, wat u terugkrijgt en in welke
    # aantallen. Geen enkele claim, alleen de plaatsbepaling.
    "wat_tekst": "Wat u aanlevert is een CAD-bestand. Wat u terugkrijgt is het onderdeel: gesneden, gekant, gelast, verspaand en nabewerkt. Voor de stappen daartussen hoeft u geen tweede leverancier te zoeken.",

    # ----------------------------------------------------- s03 hoe we werken
    # Blijft staan voor de sleutelverzameling; bouw_home.py rendert in deze
    # sectie geen bovenkopje.
    "werkwijze_eyebrow": "Hoe wij werken",

    # Zelfde lengte als de MADEGRO-kop op deze plek (44 tekens). Begint bij het
    # bestand dat de bezoeker al heeft liggen en eindigt bij levering, zodat de
    # kop los te lezen is; "in vijf stappen" kondigt aan wat de knop eronder
    # opent.
    "werkwijze_kop": "Van uw tekening tot levering in vijf stappen",

    # Twee alinea's van samen ca. 350 tekens, tegen 417 bij MADEGRO. De vijf
    # stappen staan hier niet als lijst: dit component is tekst met beeld en de
    # knop eronder ("Zo werkt een aanvraag") gaat naar werkwijze.html, waar ze
    # als treden staan. De eerste alinea noemt daarom dat elke aanvraag langs
    # dezelfde vijf stappen loopt en vat ze samen; de tweede haalt de twee
    # onzekerheden weg die hier spelen: welk bestand, en wat er gebeurt als de
    # opdracht niet standaard is. Dat laatste staat als "afstemmen" in de bron;
    # hier staat wanneer dat gebeurt, niet hoe.
    # LET OP: de vijf stappen zelf staan NIET op de homepage, alleen op
    # werkwijze.html. De kop belooft ze wel, dus deze intro moet ze noemen;
    # anders staat er een kop over vijf stappen met niets eronder. Dit is ook
    # de enige plek op de homepage waar "vrijblijvend" en "pas na uw akkoord"
    # staan, de twee dingen die een bezoeker over de drempel helpen.
    "werkwijze_intro": "<p>Aanvraag, controle, offerte, productie, levering. U levert uw tekening aan, wij controleren of die maakbaar is, en het werk start pas na uw akkoord op een vrijblijvende offerte.</p>\n              <p>Het portaal leest STEP-, DXF- en DWG-bestanden in, eventueel met een PDF-tekening erbij; overtekenen is niet nodig. Bij een complexe opdracht of een bijzonder materiaal beoordelen wij uw aanvraag persoonlijk.</p>",

    # De vijf stappen, letterlijk uit BRIEF.md. Ze staan hier voor de
    # sleutelverzameling; op de homepage rendert bouw_home.py ze niet, want s03
    # is een tekstblok met beeld. Uitgeschreven staan ze op werkwijze.html.
    # Niets toegevoegd: er staat bewust geen doorlooptijd bij "Productie" en
    # geen levertermijn bij "Levering of afhalen", want die staan nergens in
    # de bron.
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

    # ---------------------------------------------------------- s04 diensten
    # MADEGRO had hier drie kaarten en de subtitel "Wat we doen"; die is naar
    # s02 verhuisd, dus hier staat een label dat de acht kaarten aankondigt.
    "diensten_eyebrow": "Onze bewerkingen",

    # Zelfde lengte als "Drie manieren om het veiligheidsniveau te verhogen"
    # (50 tekens). Noemt het aantal, want acht bewerkingen bij &eacute;&eacute;n
    # leverancier is het argument van deze sectie, en noemt de eerste en de
    # laatste bewerking, zodat de kop ook zonder de kaarten eronder te lezen is.
    # De hero zegt al "Acht bewerkingen, van lasersnijden tot lassen en
    # verspanen". Deze kop zei dat bijna woordelijk na. Nu zegt hij wat de
    # bezoeker hier als enige leest: welke zes Vorma zelf doet en welke twee
    # het regelt.
    "diensten_kop": "Zes bewerkingen in eigen huis, twee die wij voor u regelen",

    # De leadalinea. Levert dit bestand hem niet, dan bouwt bouw_home.py hem
    # uit SERVICES; hij staat hier omdat de bezoekersvraag "welke bewerkingen
    # doen ze zelf en wat besteden ze uit" precies boven deze acht kaarten
    # hoort, en niet pas in de FAQ. Platte tekst zonder <p>: bouw_home.py zet
    # dit veld zelf in een <p>. Ca. 230 tekens, als de opsomming die hij
    # vervangt. Zes / assemblage / oppervlaktebehandeling in die orde; nooit
    # omdraaien.
    "diensten_tekst": "Assemblage loopt via ons zusterbedrijf Tentije, oppervlaktebehandeling via een coater. Beide staan op dezelfde aanvraag, dus u hoeft er zelf niets voor te regelen.",

    # Eén regel per bewerking, elk ca. 100 tekens zoals de MADEGRO-introregels
    # (106 tot 108). De kaart drukt hierboven al de korte typering uit SERVICES
    # af ("Nauwkeurig snijden van plaatmateriaal" en zo), dus deze regel zegt
    # niet wat de machine doet maar wat de bewerking u oplevert: uw bestand
    # zonder natekenen, materiaal dat niet meer op lengte hoeft, een onderdeel
    # dat af is, &eacute;&eacute;n aanspreekpunt.
    # Volgorde vast: lasersnijden, buislasersnijden, kanten, lassen,
    # nabewerking, assemblage, oppervlaktebehandeling, CNC-verspanen.
    # Let op kaart 6 en 7: assemblage via Tentije, coaten uitbesteed maar
    # volledig geregeld. Nooit omdraaien.
    "diensten_intros": [
        # TODO-CONTENT: hier stond eerder "zodat de delen bij het lassen zonder
        # passwerk sluiten". Dat is een uitspraak over pasnauwkeurigheid en die
        # staat nergens in de bron; de bron noemt geen toleranties.
        "Uw plaatdelen komen rechtstreeks uit uw eigen bestand, in staal, RVS of aluminium. Natekenen hoeft niet.",
        "Buis en profiel krijgt u op maat gesneden en bewerkt, zodat er bij u niets meer op lengte hoeft.",
        "De gesneden plaat wordt in dezelfde werkplaats gezet, in de vorm die op uw tekening staat.",
        "Losse delen worden &eacute;&eacute;n geheel; wij kiezen TIG, MIG of laser bij het werk dat er ligt.",
        "Het werk dat een onderdeel afmaakt, in dezelfde aanvraag geregeld in plaats van bij een ander bedrijf.",
        "Een complete samenstelling bouwt ons zusterbedrijf Tentije samen: dezelfde werkplaats, hetzelfde team.",
        "Coaten besteden wij uit en regelen wij volledig. U krijgt uw onderdeel afgewerkt terug, van &eacute;&eacute;n adres.",
        "Verspaande delen komen uit dezelfde aanvraag als uw plaatwerk, dus bij dezelfde leverancier vandaan.",
    ],

    # -------------------------------------------------------- s05 materialen
    # Was "Recente trajecten" (17 tekens). Vorma Metaal heeft geen cases op
    # zijn site, dus deze rijen dragen de drie materialen. De kop staat in een
    # flexregel naast de knop "Bekijk de materialen" en wordt tot 3,5rem groot,
    # dus hij moet kort blijven: 23 tekens tegen 17 bij MADEGRO. Hij noemt de
    # drie materialen zelf, want dat is het antwoord op de vraag van de
    # bezoeker hier ("in welk materiaal kan het?"); "Onze materialen" zou
    # dezelfde ruimte kosten en niets zeggen.
    "materialen_kop": "Staal, RVS en aluminium",

    # Blijft staan voor de sleutelverzameling; bouw_home.py rendert in deze
    # sectie geen inleiding, alleen de kop, de knop en de drie rijen. Twee
    # zinnen, letterlijk uit de brief. Bijzondere metalen staan er bewust bij:
    # dat is de enige uitspraak die de bron over andere metalen doet.
    "materialen_intro": "Bij uw aanvraag kiest u het materiaal zelf. Staat de kwaliteit die u nodig heeft er niet bij, vermeld dat dan of neem eerst contact met ons op.",

    # De drie materialen, in de volgorde van de brief. Tekst en kwaliteiten
    # komen woord voor woord uit BRIEF.md; er is geen kwaliteit bij verzonnen
    # en er is er geen weggelaten. Het zijn voorbeeldkwaliteiten en geen
    # voorraadlijst, wat de sectie-inleiding hierboven al zegt.
    # De teksten zijn 89 tot 122 tekens, tegen 122 tot 133 bij de
    # MADEGRO-casebeschrijvingen op deze plek.
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
    # Het label boven de lijst per materiaal. "Beschikbare kwaliteiten" zegt
    # de bron letterlijk; de inleiding erboven zegt al dat het voorbeelden
    # zijn en dat een andere kwaliteit op aanvraag kan.
    "materialen_lijstlabel": "Kwaliteiten",

    # -------------------------------------------------------------- s06 projecten
    # Nieuw, direct onder de materialen. Drie kaarten uit CASES (schil.py) met
    # de kaarttekst uit inhoud/cases.py; hier alleen de kop van de sectie.
    # PLAATSHOUDERS: de klantnamen zijn niet bevestigd, zie het kader bij CASES.
    "projecten_eyebrow": "Projecten",
    "projecten_kop": "Wat wij voor opdrachtgevers hebben gemaakt",
    "projecten_intro": "Drie voorbeelden van plaatwerk en profielwerk uit onze werkplaats, met de bewerkingen die erbij hoorden. Van gesneden plaat tot gelast en gecoat frame.",

    # -------------------------------------------------------------- s07 usps
    # Was "Waar we vandaan komen" (21 tekens). Die kop zei niets over de drie
    # cijfers eronder en botste met s10, dat pas echt over de herkomst gaat.
    # Deze kop is 51 tekens (de kop van s04 is er 47) en noemt alle drie de
    # cijfers die eronder staan, in dezelfde volgorde.
    #
    # Hier stond "22 jaar ervaring, acht bewerkingen onder &eacute;&eacute;n
    # dak". Dat is eruit: "onder &eacute;&eacute;n dak" staat op de lijst met
    # verboden koppen. In lopende tekst mag het blijven staan, want daar is het
    # de formulering van de bron zelf over een aantoonbaar feit; als kop is het
    # precies de holle samenvatting die COPY.md uitsluit.
    "usps_kop": "22 jaar ervaring, acht bewerkingen, drie materialen",

    # Drie cijfers met tellers. MADEGRO had 24 jaar / 18 opdrachtgevers /
    # 6 branches. Van Vorma Metaal is alleen het jarental bekend; de andere
    # twee zijn vervangen door getallen die op de eigen site na te tellen
    # zijn. Geen klant- of medewerkeraantallen: die staan nergens.
    # De teksten zijn 70 tot 94 tekens, als de MADEGRO-teksten (83 tot 94).
    # Cijfer 1 zegt hier waar de ervaring vandaan komt en wat ermee gebeurt;
    # de letterlijke formulering uit de brief staat in s07, zodat de twee
    # secties niet dezelfde zin twee keer afdrukken.
    "usps": [
        ("22", "jaar ervaring",
         "Zoveel jaar techniek zit er achter dit bedrijf, en dat merkt u zodra een tekening vragen oproept."),
        ("8", "bewerkingen",
         "Uw onderdeel gaat van de ene bewerking naar de volgende zonder tussentransport."),
        ("3", "materialen",
         "Bijzondere metalen zijn op aanvraag leverbaar."),
    ],

    # ----------------------------------------------------- s08 waarom Vorma
    # Waar MADEGRO het cursusgrid had. Cursussen zijn er niet; de zes punten
    # uit de brief vullen hetzelfde paneelraster.
    # De kop was "Waarom Vorma Metaal": een label, geen kop, en van dezelfde
    # soort als de vage koppen die COPY.md verbiedt. De bedrijfsnaam staat nu
    # in het bovenkopje en de kop zegt wat er onder hem staat: zes redenen, en
    # waar ze over gaan.
    "waarom_eyebrow": "Waarom Vorma Metaal",
    "waarom_kop": "Zes redenen om uw metaalwerk bij ons aan te vragen",

    # Eén alinea van ca. 150 tekens, als de MADEGRO-inleiding hier (143).
    # Platte tekst zonder <p>: bouw_home.py zet dit veld zelf in een <p>.
    # De oude tekst eindigde met "wat dat betekent voor uw aanvraag, uw offerte
    # en uw levering": een drieslag die niets toevoegde. Hier staan in plaats
    # daarvan de twee dingen die de zes panelen samen zeggen: het werk gebeurt
    # in Goor, en het aanvragen loopt langs een vaste route.
    "waarom_intro": "Uw aanvraag komt terecht bij de mensen die het werk ook uitvoeren. Dat scheelt een schakel, bij het offreren en bij het maken.",

    # De zes punten uit BRIEF.md. Titels van 16 tot 22 tekens en teksten van 63
    # tot 122 tekens passen op de panelen, waar de bestaande panelen titels van
    # ca. 30 en teksten van ca. 110 tekens dragen.
    # De titels zijn zo geschreven dat ze los te scannen zijn: "Aanvragen
    # eenvoudiger" en "Duidelijk offreren" zeiden niet wat er eenvoudiger of
    # duidelijk is. Bij "Persoonlijk contact" stond "wij denken met u mee",
    # precies de holle formulering die COPY.md verbiedt; daar staat nu wanneer
    # wij zelf contact opnemen.
    "waarom": [
        ("22 jaar in de techniek",
         "Lang genoeg om te weten waar een tekening in de praktijk op stuk loopt."),
        ("Persoonlijk contact",
         "Bel of mail ons over uw opdracht; u krijgt iemand die het werk zelf kent."),
        ("Online aanvragen",
         "Via ons portaal, dus zonder mailwisseling over versies en bijlagen."),
        ("Vaste calculatie",
         "Dezelfde aanvraag levert later dezelfde prijsopbouw op, zodat een herhaalorder navolgbaar blijft."),
        ("U weet waar het staat",
         "Tussen uw akkoord en de levering blijft u niet in het ongewisse."),
        ("Van &eacute;&eacute;n stuk tot serie",
         "Een enkel onderdeel vraagt u op dezelfde manier aan als een serie."),
    ],

    # ------------------------------------------------------ s09 testimonials
    # ==================================================================
    # PLAATSHOUDERS -- FICTIEVE CITATEN, MAG NIET LIVE ALS FEIT
    # ------------------------------------------------------------------
    # Er zijn nog geen echte klantreviews van Vorma Metaal. Op verzoek (4
    # september 2026) draagt de slider toch drie citaten, zodat de sectie af
    # is en later een-op-een te vervangen: quote, naam, functie, bedrijf en
    # logo. Het bedrijf en het logo komen uit de logoband (OPDRACHTGEVERS in
    # schil.py), zodat er geen nieuwe assets nodig zijn.
    #
    #  - De persoonsnaam staat als "Naam klant": er is geen echte persoon en
    #    een verzonnen naam bij een bestaand bedrijf is erger dan een zichtbare
    #    plaatshouder.
    #  - De citaten gaan over wat op de site staat: meerdere bewerkingen bij
    #    een leverancier, meedenken op de tekening, de offertetermijn en het
    #    nakomen van de levering. Geen cijfers, geen percentages, geen
    #    resultaten die niet te bewijzen zijn.
    #  - Elke dia draagt data-plaatshouder="testimonial"; de audit telt ze.
    #
    # Vervangen: (tekst, naam, functie, fotosleutel, logoslug) per citaat; de
    # logoslug is een sleutel uit OPDRACHTGEVERS of None voor een invulveld.
    # ==================================================================
    "testimonials_eyebrow": "Wat opdrachtgevers zeggen",
    "testimonials_kop": "Zo ervaren opdrachtgevers het werken met Vorma Metaal",

    "testimonials": [
        ("Wij laten onze plaatdelen snijden, kanten en lassen bij Vorma Metaal en krijgen ze afgewerkt terug. Dat scheelt ons het afstemmen tussen drie leveranciers.",
         "Naam klant", "Technical Buyer", "lasersnijden", "tes"),
        ("Toen een zetting op onze tekening niet te maken was, belden ze voordat de offerte uitging. Dat meedenken op de tekening maakt voor ons het verschil.",
         "Naam klant", "Werkvoorbereider", "kanten", "stork"),
        ("De offerte voor standaardwerk staat er binnen een paar minuten, en de levering komt op het moment dat is afgesproken. Daar plannen wij ons onderhoud op.",
         "Naam klant", "Hoofd Technische Dienst", "werkbank", "huhtamaki"),
    ],

    # --------------------------------------------------------------- s10 faq
    # Was "Wat mensen meestal eerst vragen" (31 tekens). Deze kop (36 tekens)
    # zegt wanneer deze vragen spelen, en spreekt de bezoeker aan in plaats van
    # over "klanten" te praten.
    "faq_kop": "Wat u wilt weten voordat u aanvraagt",

    # De zeven vragen staan vast en staan hier in de volgorde van BRIEF.md.
    # De antwoorden volgen uit de brief: portaal, inleesformaten,
    # maakbaarheidscontrole, vrijblijvend offreren, de offertetermijn, het
    # zusterbedrijf en het seriebereik. Nergens een productielevertijd, een
    # prijs, een minimumafname of een garantie, want die staan niet in de
    # bron. Antwoorden van &eacute;&eacute;n of twee alinea's van 120 tot 190
    # tekens, als de MADEGRO-antwoorden (169 en 194).
    "faq": [
        ("Hoe vraag ik een offerte aan?", [
            "Via ons portaal. U uploadt uw CAD-bestanden (STEP, DXF of DWG), eventueel met een PDF-tekening erbij, en u kiest het materiaal: staal, RVS of aluminium.",
            "Wij nemen uw aanvraag daarna in behandeling en controleren of die maakbaar is. Wilt u liever eerst overleggen? Bel of mail ons uw tekening; ook dan gaat uw aanvraag in behandeling.",
        ]),
        # TODO-CONTENT: op vormametaal.nl staat niet of het portaal een account
        # vereist. Dit antwoord zegt daarom wat vaststaat (de aanvraag loopt via
        # het portaal, de offerte komt online te staan) en biedt de route buiten
        # het portaal om. Zodra bekend is of registratie nodig is, hier vullen.
        ("Heb ik een account nodig om een offerte aan te vragen?", [
            "Uw aanvraag loopt via ons portaal: daar levert u uw bestanden aan en daar komt uw offerte online te staan.",
            "Werkt u liever niet via het portaal? Bel of mail ons uw tekening; wij nemen uw aanvraag dan gewoon in behandeling.",
        ]),
        ("Is mijn aanvraag vrijblijvend?", [
            "Ja. U ontvangt een duidelijke, vrijblijvende offerte en het werk start pas na uw akkoord. Tot dat moment verplicht een aanvraag u tot niets.",
        ]),
        ("Hoe snel ontvang ik mijn offerte?", [
            "Standaardwerk offreert het portaal volledig automatisch: uw offerte staat direct online, binnen enkele minuten.",
            "Complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd. Dagen wachten op een offerte hoeft in geen van beide gevallen.",
        ]),
        ("Kan ik een complete samenstelling aanvragen?", [
            "Ja. Samenbouwen tot complete samenstellingen loopt via ons zusterbedrijf Tentije Industri&euml;le Automatisering B.V., waarmee wij dezelfde werkplaats en hetzelfde team delen.",
            "Hoort er poedercoaten of een andere oppervlaktebehandeling bij, dan besteden wij dat uit en regelen wij het volledig. U houdt &eacute;&eacute;n aanspreekpunt voor het geheel.",
        ]),
        ("Welke bewerkingen kunnen wij voor u verzorgen?", [
            "Lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen doen wij in eigen huis, in onze werkplaats in Goor.",
            "Assemblage loopt via ons zusterbedrijf Tentije Industri&euml;le Automatisering B.V.; oppervlaktebehandeling besteden wij uit en regelen wij voor u. Samen zijn dat acht bewerkingen onder &eacute;&eacute;n dak.",
        ]),
        ("Kan ik losse stuks of kleine series laten maken?", [
            "Ja. Wij maken uniek maatwerk en series, van enkelstuks tot seriematige productie; ook voor &eacute;&eacute;n onderdeel dient u gewoon een aanvraag in.",
            # TODO-CONTENT: hier stond dat u bij een herhaalaanvraag "niet
            # opnieuw over de prijs hoeft te praten". Dat is een prijsbelofte
            # en die staat niet in de bron; die zegt alleen dat er volgens een
            # vaste calculatie geoffreerd wordt, ook bij een herhaalaanvraag.
            "Komt dezelfde aanvraag later terug, dan offreren wij die volgens dezelfde vaste calculatie, zodat de offerte navolgbaar blijft.",
        ]),
    ],

    # ------------------------------------------------------------ s11 team
    # Was de medewerkersband met een portret. Van Vorma Metaal is geen
    # medewerkersfoto beschikbaar, dus het beeldslot houdt zijn plek en krijgt
    # de werkplaatsfoto met mensen erop.
    #
    # Deze sectie ging over de herkomst (oprichting, Richard ten Tije, 2004).
    # Op verzoek (4 september 2026) gaat hij over het team: wie uw aanvraag
    # beoordeelt en waarom dat mensen zijn die het werk kennen. De feiten komen
    # alle uit de brief: Goor, dezelfde werkplaats en hetzelfde team als
    # Tentije, sinds 2004 besturingstechniek en machinebouw, persoonlijke
    # beoordeling van complexe aanvragen. Geen namen, functies of aantallen:
    # die staan nergens. De oprichtingsgeschiedenis staat nog op
    # over-vorma-metaal.html, waar de knop heen gaat.
    #
    # Het bovenkopje is de ondertitel van de sectie en de naamregel de kop; de
    # naamregel wordt 2rem, dus 29 tekens past.
    "over_eyebrow": "Technische kennis vanuit de machinebouw",
    "over_kop": "De mensen achter Vorma Metaal",

    "over_tekst": "<p>Vorma Metaal werkt vanuit Goor, in dezelfde werkplaats en met hetzelfde team als zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Dat bedrijf bouwt sinds 2004 besturingskasten en machines, en daar komt onze technische achtergrond vandaan.</p>\n            <p>Uw aanvraag wordt beoordeeld door mensen die weten hoe een onderdeel gemaakt wordt en waar het straks in terechtkomt. Is een opdracht complex, dan nemen wij eerst contact met u op, voordat de offerte uitgaat.</p>\n            <p>Persoonlijk contact hoort daarbij. Heeft u een vraag over uw project, bel of mail ons dan; wij bespreken die met u voordat u aanvraagt.</p>",

    # Wijst naar over-vorma-metaal.html, waar de herkomst staat.
    "over_knop": "Over Vorma Metaal",

    # ---------------------------------------------------------- s12 sectoren
    # Was de logoband van opdrachtgevers, met aria-label "Opdrachtgevers". In
    # assets/partners/ staan beeldmerken van bestaande bedrijven (Alstom,
    # Stork, Ballast Nedam en meer) die bij MADEGRO horen en geen
    # opdrachtgever van Vorma Metaal zijn; op vormametaal.nl staan geen
    # klantlogo's. De band draagt daarom de tien sectoren als tekst, en het
    # aria-label zegt wat er langsschuift zonder een klantclaim te doen.
    "sectoren_label": "Sectoren waarvoor wij werken",

    # ------------------------------------------------------------ s13 contact
    # Kop en tekst uit de contactsectie van de brief. De kop is 26 tekens tegen
    # 32 bij MADEGRO en past daarmee in de 20ch van cta-slot__kop; de tekst is
    # 81 tekens en past in de 46ch van cta-slot__tekst. De knop van dit blok
    # staat vast op "Vraag een offerte aan", dus dat is de aanvraagroute; de
    # tekst dekt de andere route, voor wie eerst wil overleggen, en noemt
    # daarvan de drie manieren.
    "contact_kop": "Een vraag over uw project?",
    "contact_tekst": "Wilt u uw aanvraag eerst bespreken? Bel ons, mail ons of laat uw nummer achter.",
}
