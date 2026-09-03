# -*- coding: utf-8 -*-
"""Inhoud van over-vorma-metaal.html. Het skelet staat in bouw_rest.py en is
het ongewijzigde over-ons-sjabloon van MADEGRO.

Enige bron voor de feiten: inhoud/BRIEF.md. Wat daar niet staat, staat hier
niet: geen oprichter van Vorma Metaal zelf (Richard ten Tije richtte Tentije
op, niet Vorma), geen personeelsaantal, geen machinepark, geen certificering,
geen klanten, cases of levertijden voor de productie.

De MADEGRO-pagina waar dit sjabloon van komt, gemeten per slot:
  s02 statement      1 alinea van ca. 285 tekens
  s03 waarden        4 vlakken, titels 7-13 tekens, teksten 95-105 tekens
  s05 medewerker     kop van 15 tekens plus 2 alinea's van ca. 300 en 180
  s07 FAQ            3 vragen, elk 1 antwoordalinea van 80-215 tekens
  s09 slot           kop van 17 tekens ("Even kennismaken?")
Het intro-slot is in het Vorma-sjabloon een volle introband met eigen kop en
draagt daarom drie alinea's in plaats van een enkele; de rest houdt de maat
van MADEGRO aan.

De vraag waarmee iemand deze pagina opent, is: met wie heb ik te maken en
kunnen zij dit aan. Daarom antwoordt elke kop op een stuk van die vraag en
zegt geen enkele kop alleen maar waar de sectie over gaat. Wie de koppen
scant, leest: maatwerk in metaal met 22 jaar technische ervaring &mdash; van
besturingskasten in 2004 naar maatwerk in metaal &mdash; ervaring, direct
overleg en werk vanaf &eacute;&eacute;n stuk &mdash; Tentije bouwt machines, wij maken het
metaalwerk &mdash; waar u ons vindt &mdash; heeft u een tekening klaarliggen?

Aanspreekvorm "u", overal. Zie inhoud/COPY.md voor de vier toetsen.
"""

OVER_ONS = {
    "bestand": "over-vorma-metaal.html",
    "namespace": "over-vorma-metaal",
    "titel": "Over Vorma Metaal | Vorma Metaal",

    # Meta description, ca. 140 tekens als de MADEGRO-regel (137). Noemt wat
    # het bedrijf maakt, waar het staat, waarop de ervaring berust en waar het
    # vandaan komt: dat zijn de vragen die deze pagina beantwoordt. Geen
    # cijfers over mensen of machines, want die staan niet in de bron.
    "omschrijving": "Vorma Metaal maakt in Goor maatwerk in metaal, met 22 jaar ervaring uit de machinebouw en automatisering. Ontstaan uit zusterbedrijf Tentije.",

    # Hero. In de MADEGRO-hero waren label en titel identiek ("Over MADEGRO"
    # twee keer) en dan zegt de <h1> niets. Het label houdt de paginanaam, de
    # <h1> antwoordt op de vraag waarmee iemand deze pagina opent: wie zijn
    # dit en kunnen zij dit aan. Even lang als de <h1> op diensten.html (49),
    # dus de hero blijft binnen dezelfde twee regels.
    "hero_label": "Over Vorma Metaal",
    "hero_titel": "Maatwerk in metaal, met 22 jaar technische ervaring",

    # Kop van de introband. Zet de hele herkomst in &eacute;&eacute;n regel: het bedrijf
    # begon in de besturingstechniek en maakt nu metaal op maat. Wie alleen de
    # koppen scant, weet daarmee waar deze sectie over gaat. Niet "Onze
    # geschiedenis": dat is een label en geen mededeling.
    "intro_kop": "Van besturingskasten in 2004 naar maatwerk in metaal",

    # Drie alinea's van ca. 225, 230 en 240 tekens, elk met &eacute;&eacute;n taak, zodat
    # geen enkele alinea herhaalt wat de panelen of de FAQ eronder al zeggen.
    # Alinea 1: waar het bedrijf vandaan komt en waarop de 22 jaar berust.
    # "PLC-programmering" is uitgeschreven als machinebesturingen
    # programmeren; dat is hetzelfde feit, leesbaar voor wie geen
    # besturingstechnicus is. Alinea 2: welke bewerkingen in eigen werkplaats
    # gebeuren en wat wij erbij regelen &mdash; samenbouwen loopt via Tentije en
    # oppervlaktebehandeling is uitbesteed, dus "regelen wij erbij" en nooit
    # "doen wij". Alinea 3: voor wie, uit welk bestand en in welke aantallen;
    # de opdrachtgevers zijn zes van de tien sectoren uit de brief.
    # Richard ten Tije is oprichter van Tentije; een oprichter van Vorma
    # Metaal staat niet in de bron en wordt hier dus niet genoemd.
    # De indentatie van twaalf spaties hoort bij het sjabloon: de string
    # wordt als losse regel in <div class="article-body"> geplakt.
    "intro_tekst": (
        "            <p>Tentije Industri&euml;le Automatisering B.V. begon in 2004 in Goor als eenmanszaak van Richard ten Tije: machinebesturingen programmeren en besturingskasten bouwen. Daar is in 22 jaar de ervaring opgebouwd waarmee wij nu werken.</p>\n"
        "            <p>Voor het maatwerk in metaal is daaruit Vorma Metaal ontstaan. Snijden van plaat en buis, kanten, lassen, verspanen en nabewerken doen wij in onze eigen werkplaats in Goor; samenbouwen en oppervlaktebehandeling regelen wij erbij.</p>\n"
        # "Wij werken voor" en niet "onze opdrachtgevers zijn": de brief geeft
        # tien sectoren onder "Voor wie" plus werkgebied heel Nederland. Dat
        # onderbouwt voor wie Vorma werkt, niet dat er in elke sector een
        # bestaande opdrachtgever zit. Klantaantallen staan nergens.
        "            <p>Wij werken in heel Nederland, voor machinebouwers, constructiebedrijven, installateurs, interieurbouwers, engineeringbureaus en onderhoudsdiensten. Uw onderdelen maken wij uit uw eigen CAD-bestand: STEP, DXF of DWG.</p>"
    ),

    # Kop boven de vier panelen. Het label erboven staat vast in het sjabloon
    # ("Waar wij voor staan"), dus deze kop mag dat niet herhalen en noemt in
    # plaats daarvan wat er in de panelen staat: ervaring, u kunt bellen, en
    # er is geen ondergrens aan de opdracht. Iets langer dan de MADEGRO-kop
    # (19 tekens), maar in dezelfde kolom en dus binnen twee regels.
    "waarden_kop": "Ervaring, direct overleg en werk vanaf &eacute;&eacute;n stuk",

    # Vier van de zes waarom-punten uit de brief: die vier gaan over het
    # bedrijf, "Aanvragen eenvoudiger" en "Duidelijk offreren" gaan over het
    # portaal en de offerte en horen op werkwijze.html. Titels 16-21 tekens,
    # teksten 103-120 tekens, tegen 7-13 en 95-105 bij de MADEGRO-vlakken.
    # Elke tekst voegt aan het brief-punt &eacute;&eacute;n feit toe dat elders in de brief
    # staat (afstemmen bij complex werk, akkoord vooraf, losse stuks), zodat
    # het paneel iets zegt in plaats van een kwaliteit te benoemen.
    "waarden": [
        ("22 jaar ervaring",
         "Opgebouwd in technische sectoren, met name machinebouw en automatisering: het werk waar Vorma Metaal uit voortkomt."),
        ("Persoonlijk contact",
         "Bel of mail ons als u wilt overleggen. Bij een complexe opdracht stemmen wij met u af voordat de offerte uitgaat."),
        ("Overzichtelijk proces",
         "Van offerte tot levering hoort u van ons wanneer het ertoe doet. Het werk start pas nadat u de offerte goedkeurt."),
        ("Maatwerk en series",
         "Uniek maatwerk en series, van enkelstuks tot seriematige productie. Ook voor &eacute;&eacute;n stuk vraagt u een offerte aan."),
    ],

    # Waar in MADEGRO de naam van de eigenaar stond, gaat het hier over het
    # zusterbedrijf; van Vorma Metaal is geen medewerkersfoto beschikbaar. Een
    # bedrijfsnaam als kop zou hier niets zeggen, dus de kop maakt meteen het
    # verschil duidelijk. Het label erboven staat vast op "Zusterbedrijf" en
    # de volledige naam staat in de eerste alinea. Even lang als de naam die
    # hier stond (43 tekens), dus de kop blijft op dezelfde regels staan.
    "zuster_kop": "Tentije bouwt machines, wij maken het metaalwerk",

    # Twee alinea's van ca. 295 en 180 tekens, als de MADEGRO-biografie
    # (300 en 180). Alinea 1 zet de twee bedrijven naast elkaar, noemt de
    # volledige naam en de gedeelde werkplaats, en zegt wat de bezoeker daar
    # aan heeft: zijn onderdeel wordt gemaakt waar ook machines worden
    # gebouwd. De oprichting staat al in de introband en wordt hier niet
    # herhaald. Alinea 2 is de praktische consequentie: assemblage loopt via
    # Tentije, dus een compleet samengesteld product kan. Niet omdraaien: de
    # zes andere bewerkingen zijn eigen huis en oppervlaktebehandeling wordt
    # uitbesteed maar door ons geregeld.
    "zuster_tekst": (
        "            <p>Tentije Industri&euml;le Automatisering B.V. richt zich op machinebouw, onderhoud en besturingstechniek; Vorma Metaal doet het maatwerk in metaal. De twee bedrijven delen dezelfde werkplaats en hetzelfde team. Uw onderdelen worden dus gemaakt op de plek waar ook machines worden gebouwd en onderhouden.</p>\n"
        "            <p>Complete samenstellingen zijn mogelijk via Tentije. Wilt u geen losse onderdelen maar een samengebouwd product? Vermeld dat bij uw aanvraag, dan nemen wij de assemblage mee.</p>"
    ),

    # Drie vragen die deze pagina oproept, op de plek van de MADEGRO-vragen
    # over wie het werk doet, in welke regio dat gebeurt en wat de tarieven
    # zijn. Dezelfde drie soorten vragen: kunnen zij dit maken, met wie heb ik
    # te maken, en werken zij bij mij in de buurt. Over tarieven staat niets
    # in de bron, dus die vraag is de maakbaarheidsvraag geworden.
    # De vraag naar zelf doen of uitbesteden staat al op diensten.html en de
    # regiovraag op voor-wie.html; hier is de tweede vraag daarom de zorg die
    # alleen deze pagina oproept: krijg ik twee bedrijven aan de lijn?
    # Vraagvorm als op de andere pagina's: de bezoeker vraagt in de ik-vorm en
    # spreekt Vorma met "u" aan. Elk antwoord &eacute;&eacute;n alinea, zoals in het
    # sjabloon; 165-240 tekens tegen 80-215 bij MADEGRO.
    "faq": [
        ("Hoe weet ik of u mijn onderdeel kunt maken?", [
            "Dat controleren wij voor u: stuur uw CAD-bestand in en wij kijken of het onderdeel zo te maken is. Wij verwerken staal, RVS en aluminium, en doen lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen in eigen huis.",
        ]),
        ("Heb ik met twee bedrijven te maken?", [
            "Nee, u vraagt alles bij Vorma Metaal aan. Tentije Industri&euml;le Automatisering B.V. is ons zusterbedrijf en werkt in dezelfde werkplaats met hetzelfde team; loopt een deel van uw opdracht via Tentije, dan regelen wij dat.",
        ]),
        ("Werkt u in heel Nederland?", [
            "Ja. Onze werkplaats staat aan Dammaten 14 in Goor, in Twente, en ons werkgebied is heel Nederland. Uw producten worden geleverd, of staan in Goor klaar om af te halen.",
        ]),
    ],

    # Kop van het slotblok. De knop eronder staat vast op "Vraag een offerte
    # aan" en de regel ernaast vraagt om uw CAD-bestand, dus de kop vraagt om
    # de tekening en niet om een kennismaking. Zelfde vorm en lengte als
    # MADEGRO's "Even kennismaken?": een korte vraag.
    "contact_kop": "Heeft u een tekening klaarliggen?",
}
