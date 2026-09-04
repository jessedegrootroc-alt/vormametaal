# -*- coding: utf-8 -*-
"""Inhoud van werkwijze.html. Het skelet staat in bouw_rest.py (bouw_werkwijze):
het cursussjabloon met de trap uit het dienstsjabloon.

Enige bron voor de feiten: inhoud/BRIEF.md. De vijf stappen staan daar; de
formulering is van ons. Geen levertijden of doorlooptijden voor de productie,
geen capaciteit, geen machines, geen certificeringen: die staan nergens in de
bron. Wel de offertetermijn, want die staat er letterlijk.

Eigen huis: lasersnijden, buislasersnijden, kanten, lassen, nabewerking en
CNC-verspanen. Assemblage loopt via zusterbedrijf Tentije Industri&euml;le
Automatisering B.V.; oppervlaktebehandeling wordt uitbesteed maar volledig door
Vorma geregeld.

Aanspreekvorm "u", overal. Zie inhoud/COPY.md voor de vier toetsen.
"""

WERKWIJZE = {
    "bestand": "werkwijze.html",
    "namespace": "werkwijze",
    "titel": "Werkwijze | Vorma Metaal",

    # Meta description, 150 tekens: de eerste drie stappen in de volgorde
    # waarin de bezoeker ze meemaakt, met de offertetermijn erin, want dat is
    # het sterkste feit dat de bron over het proces geeft. Geen termijn voor de
    # productie, want die staat er niet.
    "omschrijving": "Zo werkt een aanvraag bij Vorma Metaal: u levert uw CAD-bestand aan, wij controleren of het maakbaar is en standaardwerk krijgt binnen minuten een prijs.",

    "hero_label": "Werkwijze",

    # De <h1>. Zegt waar de pagina heen loopt in plaats van dat er een
    # werkwijze is: van het bestand van de bezoeker naar een gemaakt
    # onderdeel. 49 tekens, als de hero op diensten.html.
    "hero_titel": "Zo gaat uw aanvraag van tekening naar eindproduct",

    # Twee alinea's in het introblok, 183 en 273 tekens tegen ca. 240 en 270
    # bij de MADEGRO-intro op deze plek. Eerste alinea zegt wat Vorma maakt en
    # hoe klein de eerste stap is: het bestand dat de bezoeker al heeft, plus
    # de materiaalkeuze. De inleesformaten staan bewust niet hier maar in trede
    # 01 en in de offertesectie, waar de vinklijst met formaten onder staat.
    # Tweede alinea vat de vier stappen daarna samen en noemt welke bewerkingen
    # Vorma zelf doet; wat via Tentije loopt en wat wordt uitbesteed, staat in
    # de trap eronder. "Kanten" wordt hier in vier woorden uitgelegd, op de
    # eerste plek waar het woord valt: voor een inkoper is het bekend, voor een
    # ontwerper niet altijd.
    "intro": "<p>Vorma Metaal maakt onderdelen van metaal op maat voor zakelijke opdrachtgevers. U vraagt een prijs aan met het CAD-bestand dat u al heeft en de materiaalkeuze; overtekenen hoeft niet.</p>\n            <p>Daarna controleren wij of uw onderdelen te maken zijn en ontvangt u een vrijblijvende offerte. Pas na uw akkoord gaat het werk de werkplaats in. Snijden, kanten (plaat in vorm zetten), lassen, nabewerken en verspanen doen wij zelf; daarna leveren wij, of u haalt uw producten op in Goor.</p>",

    # Kop boven het introblok, 49 tekens. Hij moet beide alinea's eronder
    # dekken: wat de bezoeker zelf aanlevert en wat Vorma daarna doet. De trap
    # eronder heeft in het sjabloon al de vaste kop "Zo loopt uw opdracht", dus
    # deze kop zegt de rolverdeling en herhaalt de <h1> niet.
    "stappen_kop": "U levert het CAD-bestand, wij doen het metaalwerk",

    # E&eacute;n alinea in de smalle kolom naast de trap, 169 tekens tegen ca.
    # 198 bij de MADEGRO-tekst op die plek. Zegt eerst dat aantallen niets aan
    # het proces veranderen (het seriebereik uit de brief) en maakt daarna
    # "Overzichtelijk proces" concreet met de twee momenten waarop u
    # daadwerkelijk iets van ons hoort. Bewust geen doorlooptijd, want die
    # staat niet in de bron.
    "stappen_intro": "Dezelfde vijf stappen gelden voor &eacute;&eacute;n stuk en voor een hele serie. U hoort van ons wanneer het ertoe doet: als wij iets in uw tekening zien en als uw offerte klaarstaat.",

    # De vijf stappen uit BRIEF.md, elk 166-226 tekens zoals de MADEGRO-treden.
    # De titels zeggen wie wat doet, zodat de trap ook los te scannen is: twee
    # keer "u", drie keer "wij". Trede 03 legt uit wat "vrijblijvend" in de
    # praktijk betekent, want dat is het woord waar de twijfel zit.
    # Detail blijft overal None: het sjabloon zet boven die regel het vaste
    # label "Herkenbaar gedrag" uit de MADEGRO-Veiligheidsladder, en daar hoort
    # een klantverwachting niet onder. Wat van de klant verwacht wordt, staat
    # daarom in de tredetekst zelf.
    "stappen": [
        ("U uploadt uw bestand en kiest het materiaal",
         "In het portaal uploadt u uw CAD-bestanden (STEP, DXF of DWG), eventueel met een PDF-tekening erbij, en kiest u het materiaal: staal, RVS of aluminium. Daarna nemen wij uw aanvraag in behandeling.",
         None),
        ("Wij controleren of uw tekening maakbaar is",
         "Voordat u een prijs krijgt, kijken wij of uw onderdelen te maken zijn zoals ze getekend staan. Bij een complexe opdracht overleggen wij eerst met u, zodat een onduidelijkheid in de tekening geen onbruikbaar onderdeel oplevert.",
         None),
        ("U ontvangt een vrijblijvende offerte",
         "De offerte is duidelijk en volgt een vaste calculatie, ook als u dezelfde onderdelen later opnieuw aanvraagt. Vrijblijvend betekent hier dat u tot niets verplicht bent: het werk start pas nadat u akkoord heeft gegeven.",
         None),
        ("Wij maken uw producten in onze werkplaats",
         "Lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen (draaien en frezen) gebeuren in eigen huis. Poedercoaten en andere oppervlaktebehandelingen besteden wij uit en regelen wij volledig voor u.",
         None),
        ("Wij leveren, of u haalt uw producten op",
         "Uw producten worden geleverd, of staan klaar om af te halen aan Dammaten 14 in Goor. Ons werkgebied is heel Nederland; geef bij uw aanvraag door wat u het beste past.",
         None),
    ],

    # Subtitle boven de offertesectie. Kondigt beide alinea's eronder aan (de
    # formaten en de offertetermijn) plus de check-lijst, die uit
    # schil.FORMATEN komt: STEP, DXF, DWG, PDF. Even kort als de andere
    # subtitles in het sjabloon.
    "formaten_kop": "Bestanden en offerte",

    # Eerste alinea van die sectie, 198 tekens tegen ca. 230 bij MADEGRO: welke
    # formaten er rechtstreeks in kunnen, met de vinklijst eronder als
    # herhaling. De materiaalopmerking komt uit de brief; er staat een
    # telefoonroute bij, want dit is het punt waar iemand vastloopt.
    "formaten_intro": "STEP, DXF en DWG kunt u rechtstreeks aanleveren, eventueel met een PDF-tekening erbij. Staat het materiaal dat u nodig heeft niet in de lijst van het portaal? Vermeld dat bij uw aanvraag of bel ons.",

    # Kop van dezelfde sectie, 52 tekens tegen ca. 45 bij de MADEGRO-kop hier.
    # De offertetermijn is het sterkste feit dat de bron over het proces geeft,
    # dus die staat in de kop zelf en niet pas in de alinea. Bewust over
    # standaardwerk gesproken: alleen daarvan zegt de bron "binnen enkele
    # minuten", en de alinea eronder maakt het onderscheid af.
    "offerte_kop": "Standaardwerk krijgt binnen enkele minuten een prijs",

    # Tweede alinea, 249 tekens: de offertetermijn zoals BRIEF.md hem geeft.
    # Standaardwerk automatisch online binnen enkele minuten, complex werk en
    # bijzondere materialen persoonlijk beoordeeld, en in geen van beide
    # gevallen dagen wachten. Geen andere termijn erbij, want over de
    # productietijd staat niets in de bron.
    "offerte_tekst": "Standaardwerk offreert het portaal automatisch: uw offerte staat direct online, binnen enkele minuten. Complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd. U wacht in geen van beide gevallen dagen op een prijs.",

    # Vier vragen over het proces, in de volgorde van de stappen: aanvragen,
    # de controle van de tekening, bewerkingen combineren en de levering. De
    # offertetermijn en het vrijblijvende aanvragen staan al in de secties
    # hierboven en worden hier niet herhaald; de openingstijden staan hier en
    # niet in trede 05, zodat dat feit &eacute;&eacute;n plek heeft. Elk
    # antwoord twee alinea's van 95-201 tekens, als de MADEGRO-antwoorden. Dat
    # de assemblage bij Tentije door hetzelfde team in dezelfde werkplaats
    # gebeurt, staat erbij: anders leest het als een overdracht naar een
    # onbekende derde.
    "faq": [
        ("Hoe vraag ik een offerte aan?", [
            "Via ons portaal. U levert uw CAD-bestand aan, kiest het materiaal en verstuurt de aanvraag; wij nemen hem daarna in behandeling.",
            "Wilt u eerst overleggen? Bel 0547 227 000 of mail info@vormametaal.nl met uw tekening; ook dan kijken wij eerst of het maakbaar is voordat u een prijs krijgt.",
        ]),
        ("Wie beoordeelt mijn tekening?", [
            "Dat doen wij zelf, voordat u een prijs krijgt: wij kijken of uw onderdelen te maken zijn zoals ze getekend staan.",
            "Is de opdracht complex, dan overleggen wij eerst met u. Klopt er iets niet in de tekening, dan hoort u dat voordat de offerte uitgaat.",
        ]),
        ("Kan ik meerdere bewerkingen in &eacute;&eacute;n aanvraag combineren?", [
            "Ja. Lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen doen wij in eigen huis, in onze werkplaats in Goor.",
            "Samenbouwen tot een compleet product loopt via zusterbedrijf Tentije Industri&euml;le Automatisering B.V.: hetzelfde team, dezelfde werkplaats. Oppervlaktebehandeling besteden wij uit en regelen wij voor u.",
        ]),
        ("Worden mijn producten geleverd of kan ik ze afhalen?", [
            "Beide kan: wij leveren door heel Nederland, of uw producten staan klaar om in Goor af te halen.",
            "Afhalen kan op werkdagen van 07:30 tot 16:30; in het weekend is de werkplaats gesloten. Geef bij uw aanvraag door wat u het beste past.",
        ]),
    ],

    # Kop van het slotblok, 34 tekens, als de MADEGRO-kop op deze plek (33).
    # De knop eronder is "Vraag een offerte aan", dus dit is de aanvraagfase:
    # de kop vraagt om de tekening en niet om herkenning.
    "contact_kop": "Klaar om uw tekening in te sturen?",
}
