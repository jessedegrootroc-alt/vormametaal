# -*- coding: utf-8 -*-
"""Inhoud van diensten.html, het overzicht van de acht bewerkingen.

Het skelet is overzicht() in bouw_rest.py: het MADEGRO-overzichtssjabloon dat
hier voor cursusaanbod.html stond. Patroonhero, introband, een rij panelen in
panel-row--4, een FAQ en het slotblok. De acht kaarten worden niet hier maar
uit schil.SERVICES opgebouwd; dit bestand levert alleen de omliggende tekst.
De tekstlengtes volgen de MADEGRO-tekst op die plek, want de layout verandert
niet.

Enige bron voor de feiten: inhoud/BRIEF.md. Welke MADEGRO-component welke
Vorma-inhoud krijgt staat in inhoud/MAPPING.md.

Wat hier bewust NIET staat, omdat het nergens in de bron staat: machines of
machinemerken, plaatdiktes, afmetingen, toleranties, certificeringen (ISO,
VCA), klantnamen, logo's, citaten, cases, projecten, aantallen klanten of
medewerkers, productielevertijden, garanties en capaciteit.

Eigen huis versus uitbesteed is op deze pagina de belangrijkste val, want dit
is de plek waar de acht bewerkingen bij elkaar staan: lasersnijden,
buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen gebeuren in
eigen huis; assemblage loopt via zusterbedrijf Tentije Industri&euml;le
Automatisering B.V.; oppervlaktebehandeling wordt uitbesteed maar volledig
door Vorma geregeld. "In eigen huis" wordt hier daarom alleen gebruikt waar
het over die zes gaat, en "onder &eacute;&eacute;n dak" &mdash; de samenvatting
van de bron zelf &mdash; waar het over alle acht gaat.

Aanspreekvorm "u", overal. Zie inhoud/COPY.md voor de vier toetsen.
"""

DIENSTEN_OVERZICHT = {
    "bestand": "diensten.html",
    "namespace": "diensten",
    "titel": "Diensten | Vorma Metaal",

    # Meta description: 153 tekens, dus binnen de 155. Noemt de bewerkingen
    # zoals een inkoper ze intypt, plus de plaats, en zet de grens eigen huis
    # versus geregeld er meteen in &mdash; dat is de vraag waarmee iemand op
    # deze pagina klikt. Twee zinnen, want de punt na "eigen huis" zet die
    # grens harder dan een komma: de zes staan aan de ene kant, assemblage en
    # poedercoaten aan de andere. "Poedercoaten" voluit, want dat is de term
    # uit de bron en het woord dat een inkoper intypt.
    # Geen diktes, levertijden of aantallen, want die staan niet in de bron.
    "omschrijving": "Vorma Metaal in Goor: lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen in eigen huis. Assemblage en poedercoaten regelen wij.",

    "hero_label": "Diensten",

    # H1 in de patroonhero. Die kop wordt op breed scherm tot 5rem groot en
    # staat in een halve kolom, dus kort houden en geen lange samenstellingen:
    # dit is 38 tekens, in de orde van de andere hero's op dit sjabloon
    # ("Metaalwerk voor tien sectoren, in heel Nederland" is 47, "Zo gaat uw
    # aanvraag van tekening naar eindproduct" 48). Hij zegt wat u hier kunt
    # laten maken; het aantal staat in het bovenkopje boven de kaarten en de
    # verdeling eigen huis/geregeld in de kop van de introband, zodat de drie
    # koppen elk iets toevoegen. De formulering is de korte vorm van het goede
    # voorbeeld in COPY.md ("Van plaatmateriaal tot compleet samengesteld
    # product"). "Plaat en buis", niet alleen plaat: de bron noemt naast
    # plaatmateriaal ook buis- en profielmateriaal, en wie een buisframe laat
    # maken moet zich in de eerste kop herkennen. Samenbouw in eigen huis
    # belooft hij niet: de introband eronder zegt meteen dat assemblage via
    # Tentije loopt.
    "hero_titel": "Van plaat en buis tot compleet product",

    # Kop van de introband, 54 tekens, in de orde van de koppen op deze plek
    # op de andere pagina's. Dit is de belangrijkste kop van de pagina: hij
    # geeft de grens eigen huis versus uitbesteed al weg aan wie alleen de
    # koppen scant, in plaats van de sectie aan te kondigen. Zes plus twee is
    # acht; dat aantal noemt de alinea eronder.
    "intro_kop": "Zes bewerkingen doen wij zelf, twee regelen wij voor u",

    # Twee alinea's, even lang als de MADEGRO-intro op deze plek (ca. 230 en
    # 270 tekens) en in een halfbrede leeskolom. Eerste alinea: wat Vorma
    # maakt, de zes bewerkingen die in eigen huis gebeuren, de materialen en
    # het seriebereik. Bij "kanten" staat in vier woorden wat het is, want een
    # ontwerper of inkoper buiten de plaatwerkwereld kent die term niet
    # (COPY.md, toets 1). Tweede alinea: de twee die niet in eigen huis
    # gebeuren, met per bewerking waar hij dan wel loopt, zodat de kaartenrij
    # eronder niet verkeerd gelezen kan worden. De slotregel geeft het antwoord
    # waarvoor iemand deze pagina opent &mdash; alle acht op &eacute;&eacute;n
    # aanvraag &mdash; met "onder &eacute;&eacute;n dak", de samenvatting van de
    # bron zelf, in lopende tekst en niet als kop.
    "intro_tekst": "          <p>Vorma Metaal maakt onderdelen van metaal op maat, in staal, RVS of aluminium. Lasersnijden, buislasersnijden, kanten (plaat in vorm zetten), lassen, nabewerking en CNC-verspanen doen wij in onze eigen werkplaats in Goor, van &eacute;&eacute;n stuk tot een serie.</p>\n          <p>Assemblage loopt via ons zusterbedrijf Tentije Industri&euml;le Automatisering B.V., in dezelfde werkplaats en met hetzelfde team. Poedercoaten en andere oppervlaktebehandelingen besteden wij uit en regelen wij volledig voor u. Samen zijn dat acht bewerkingen onder &eacute;&eacute;n dak, op &eacute;&eacute;n aanvraag.</p>",

    # Bovenkopje boven de kaartenrij. Zelfde soort teller als op de andere
    # pagina's van dit sjabloon ("Drie materialen", "Tien sectoren").
    "kaarten_eyebrow": "Acht bewerkingen",

    # Kop boven de acht kaarten, 34 tekens. Zelfde patroon als op
    # materialen.html, waar het bovenkopje "Drie materialen" zegt en de kop
    # eronder "Staal, RVS en aluminium": het bovenkopje telt, de kop noemt de
    # inhoud. Wie alleen de koppen scant, leest hier dus welke bewerkingen er
    # staan in plaats van dat er iets te bekijken valt; de eerste en de laatste
    # kaart van de rij vormen de reeks. De pijlknop op elke kaart wijst er zelf
    # al op dat de kaarten doorlinken.
    "kaarten_kop": "Van lasersnijden tot CNC-verspanen",

    # Drie vragen over de acht bewerkingen samen; de bewerking-specifieke
    # vragen staan op de acht dienstpagina's zelf. Dit zijn de drie vragen die
    # een bezoeker op een overzichtspagina overhoudt: wat doet u zelf, kan het
    # bij &eacute;&eacute;n partij, en werkt u ook met kleine aantallen.
    # Antwoorden van twee alinea's van ca. 150-190 tekens, zoals de
    # MADEGRO-antwoorden in dit accordeon. Alle feiten komen uit de brief.
    #
    # De vragen zeggen "wij" waar het over Vorma gaat, zoals de FAQ op de
    # homepage: op deze site is "u" altijd de bezoeker, dus "doet u zelf" zou
    # de aanspreekvorm omdraaien.
    "faq": [
        ("Welke bewerkingen doen wij zelf en wat besteden wij uit?", [
            "Zes van de acht doen wij zelf, in onze werkplaats in Goor: lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen (draaien en frezen).",
            "Assemblage loopt via ons zusterbedrijf Tentije Industri&euml;le Automatisering B.V. Poedercoaten en andere oppervlaktebehandelingen besteden wij uit en regelen wij volledig voor u.",
        ]),
        ("Kan ik meerdere bewerkingen in &eacute;&eacute;n aanvraag combineren?", [
            "Ja. U vraagt de bewerkingen aan die uw onderdeel nodig heeft en krijgt er &eacute;&eacute;n offerte voor. Uw tekening hoeft niet langs meerdere leveranciers en u houdt &eacute;&eacute;n aanspreekpunt.",
            "Ook een compleet samengebouwd product kan: het samenbouwen gebeurt via ons zusterbedrijf, met hetzelfde team in hetzelfde pand. Hoort er poedercoaten bij, dan gaat dat mee in dezelfde offerte.",
        ]),
        ("Kan ik losse stuks laten maken, of moet het een serie zijn?", [
            "Losse stuks kunnen. Wij maken zowel enkelstuks als series; &eacute;&eacute;n onderdeel is net zo goed een opdracht en volgt dezelfde weg als een serie.",
            "Komt dezelfde aanvraag later terug, dan offreren wij die volgens dezelfde vaste calculatie, zodat u weet waar u aan toe bent.",
        ]),
    ],

    # Kop van het slotblok. Dit is de aanvraagfase en de knop eronder is
    # "Vraag een offerte aan", dus de kop vraagt om de opdracht. Zelfde lengte
    # als de contactkoppen op de acht dienstpagina's (ca. 35 tekens) en hij
    # sluit aan op wat deze pagina toevoegt: alle bewerkingen in &eacute;&eacute;n
    # aanvraag in plaats van &eacute;&eacute;n bewerking.
    "contact_kop": "Vraag uw metaalwerk in &eacute;&eacute;n keer aan",
}
