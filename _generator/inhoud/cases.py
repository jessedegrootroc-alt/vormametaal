# -*- coding: utf-8 -*-
"""Inhoud van cases.html en de drie casepagina's. Het skelet staat in
bouw_cases.py; het register met klant, beelden, bewerkingen en bestandsnamen
staat in schil.py onder CASES.

==========================================================================
PLAATSHOUDERS -- MAG NIET LIVE ALS FEIT
--------------------------------------------------------------------------
Op vormametaal.nl staan geen cases en er is geen opdrachtgever die deze
projecten bevestigt. Op verzoek (4 september 2026) zijn het toch complete
casestudies met een klantnaam, zodat kaarten en pagina's af zijn en later
een-op-een te vervangen. De klantnamen komen uit de logoband (OPDRACHTGEVERS
in schil.py): dezelfde plaatshouderset als bij de testimonials.

Wat er bewust NIET in staat: aantallen, jaartallen, plaatsnamen, doorlooptijden,
prijzen, citaten en resultaten die niet te bewijzen zijn (tijdsbesparing,
percentages). Het "type productie" is weggelaten: dat is niet bekend.

Elke kaart en pagina draagt data-plaatshouder="case" en de audit meldt ze.
Vervangen: per case de sleutels hieronder, en in CASES "plaatshouder" op False.
==========================================================================

Structuur per casepagina, voor alle drie gelijk:
  1 hero: klant, titel, foto, samenvatting
  2 project in het kort: opdrachtgever, sector, materiaal, bewerkingen
  3 de vraag
  4 onze aanpak: intro plus de stappen
  5 het resultaat
  6 fotogalerij
  7 andere projecten
  8 CTA
"""

CASES_PAGINA = {
    "bestand": "cases.html",
    "namespace": "cases",
    "titel": "Projecten | Vorma Metaal",
    "omschrijving": "Een selectie van onderdelen en samenstellingen die Vorma Metaal voor technische en industri&euml;le opdrachtgevers heeft geproduceerd: wat er gemaakt is, voor wie en met welke bewerkingen.",
    "hero_label": "Wat wij maken",
    "hero_titel": "Projecten",
    "intro_kop": "Een selectie van ons werk",
    "intro_tekst": (
        "          <p>Bekijk een selectie van onderdelen en samenstellingen die Vorma Metaal voor technische en industri&euml;le opdrachtgevers heeft geproduceerd.</p>\n"
        "          <p>Per project staat wie de opdrachtgever was, wat er gemaakt is, van welk materiaal en welke bewerkingen erbij hoorden. Elk project heeft een eigen pagina met de vraag, onze aanpak en het resultaat.</p>"
    ),
    "raster_kop": "Alle projecten",
    "contact_kop": "Heeft u een vergelijkbaar onderdeel nodig?",
    "contact_tekst": "Stuur uw CAD-bestand voor een vrijblijvende offerte of neem contact op om uw project eerst te bespreken.",
}

# Vaste koppen op de casepagina's, zodat alle drie dezelfde opbouw hebben.
KOPPEN = {
    "kort": "Project in het kort",
    "vraag": "De vraag",
    "aanpak": "Onze aanpak",
    "resultaat": "Het resultaat",
    "galerij": "Beelden van het project",
    "andere": "Andere projecten",
}

# Per case: de tekst op de kaart, de samenvatting in de hero en de blokken.
# "stappen" is een lijst van (stap, uitleg); de stap is de bewerking of de
# controle vooraf, de uitleg zegt wat er in dit project precies gebeurde.
CASE_TEKSTEN = {
    "liftdeuren": {
        "kaart": "Deurpanelen en omlijstingen in geborsteld RVS voor de liften van een kantoorgebouw: uit plaat gesneden en gezet, geleverd met folie op de zichtzijde.",
        "samenvatting": "Voor een kantoorgebouw van Ballast Nedam maakten wij de RVS bekleding van de liftdeuren en de omlijstingen eromheen: deurpanelen, kozijnzijkanten en bovenranden, uit plaat gesneden, gezet en gelast.",
        "vraag": (
            "<p>Bij de afbouw van het gebouw moesten de liften een omlijsting en deurbekleding in geborsteld RVS krijgen, met dezelfde uitstraling op elke verdieping. De liftinstallatie was al besteld; de bekleding moest daar precies op passen.</p>"
            "<p>Ballast Nedam zocht een leverancier die de plaatdelen uit de tekening kon snijden, zetten en lassen, en ze zonder krassen op de bouwplaats kon afleveren. De zichtzijde is geborsteld, dus elke kras blijft zichtbaar.</p>"
        ),
        "aanpak_intro": "De tekeningen kwamen als STEP- en DXF-bestanden binnen. Wij controleerden of de zettingen te maken waren en of de borstelrichting op alle delen gelijk kon lopen, en zetten daarna de bewerkingen op een rij.",
        "stappen": [
            ("CAD-bestanden controleren", "De maakbaarheid van de zettingen en de borstelrichting nagekeken voordat de offerte uitging."),
            ("Lasersnijden", "Contouren, uitsparingen en bevestigingsgaten uit de RVS-plaat gesneden, met de beschermfolie erop."),
            ("Kanten", "De randen van de panelen en kozijndelen gezet, zodat de delen stijf worden en een schone kant krijgen."),
            ("Lassen", "De hoeken van de omlijsting gelast en de naden afgewerkt tot ze in de borstelstructuur wegvallen."),
            ("Nabewerking", "Snijkanten afgebraamd; de folie blijft tot aan de montage op de zichtzijde."),
        ],
        "resultaat": (
            "<p>Ballast Nedam ontving per lift een complete set: de deurpanelen, de kozijnzijkanten en de bovenrand, in RVS 304 met dezelfde borstelrichting en met de folie er nog op.</p>"
            "<p>Snijden, zetten, lassen en nabewerken liepen in &eacute;&eacute;n aanvraag en in &eacute;&eacute;n werkplaats. Voor de bouwplaats was er &eacute;&eacute;n leverancier en &eacute;&eacute;n levering.</p>"
        ),
    },
    "roltrappen": {
        "kaart": "Zijpanelen, sokkels en leuningsteunen voor roltrappen in een stationshal: vlak plaatwerk in RVS en gesneden buis voor het dragende deel.",
        "samenvatting": "Voor Alstom maakten wij het zichtbare plaatwerk van roltrappen in een stationshal: de zijpanelen langs de treden, de sokkels onder de balustrade en de stalen steunen onder de leuning.",
        "vraag": (
            "<p>De roltrappen krijgen aan de buitenkant panelen die op ooghoogte in beeld komen en tegen het glas van de balustrade aansluiten. Dat plaatwerk moet vlak zijn en over de hele lengte dezelfde naad houden.</p>"
            "<p>Onder de leuning zitten steunen van buis die niet in beeld komen, maar wel maatvast moeten zijn: de leuning wordt erop uitgelijnd. Alstom wilde beide soorten delen bij &eacute;&eacute;n leverancier onderbrengen.</p>"
        ),
        "aanpak_intro": "Lange, smalle panelen vragen een zetvolgorde die vooraf vaststaat; anders past het deel na de laatste zetting niet meer in de kantbank. Die volgorde hebben wij bij de controle van de bestanden bepaald.",
        "stappen": [
            ("CAD-bestanden controleren", "De zetvolgorde van de lange panelen vastgelegd en de buisdelen op de maten van de leuning nagekeken."),
            ("Lasersnijden", "Zijpanelen en sokkels uit RVS-plaat gesneden, met de bevestigingsgaten erin."),
            ("Kanten", "De aansluitranden tegen het glas gezet, in de vooraf bepaalde volgorde."),
            ("Buislasersnijden", "De leuningsteunen van stalen buis op lengte gesneden, met de gaten in dezelfde gang."),
            ("Nabewerking", "Alle snijkanten afgebraamd; de stalen delen klaargemaakt om te coaten."),
        ],
        "resultaat": (
            "<p>Alstom ontving per roltrap de zijpanelen en sokkels in RVS 304 en de leuningsteunen in staal, gereed om te coaten, in &eacute;&eacute;n levering.</p>"
            "<p>Plaat en buis kwamen uit dezelfde werkplaats en dezelfde aanvraag, zodat het zichtwerk en het dragende werk op elkaar waren afgestemd voordat de montage begon.</p>"
        ),
    },
    "draaideuren": {
        "kaart": "Het ronde frame en de dorpel van draaideuren voor een kantoorgebouw: kokerprofiel op maat gesneden, gelast tot &eacute;&eacute;n geheel en gepoedercoat in de gevelkleur.",
        "samenvatting": "Voor een kantoorgebouw van Ooms Bouw &amp; Ontwikkeling maakten wij de stalen frames van de draaideuren in de entree: de ronde bovenrand, de stijlen die het glas dragen en de dorpel, gelast en gepoedercoat.",
        "vraag": (
            "<p>De entree kreeg draaideuren met een stalen frame dat het glas draagt en de ronding bepaalt. Het frame staat buiten, in het zicht, en moet in de kleur van de gevel worden afgewerkt.</p>"
            "<p>De ronding is het lastige deel: de bovenrand bestaat uit gesneden segmenten die tot een cirkel worden gelast, en die cirkel moet rond zijn, anders loopt de deur aan. Ooms zocht een leverancier die het snijden, lassen en coaten in &eacute;&eacute;n opdracht kon regelen.</p>"
        ),
        "aanpak_intro": "Het frame is opgebouwd uit kokerprofiel. De verstekken en de gaten voor de glasbevestiging komen uit het model, zodat er na het snijden niets meer afgetekend of nageboord hoeft te worden.",
        "stappen": [
            ("CAD-bestanden controleren", "De segmentverdeling van de ronde bovenrand en de lasvolgorde nagekeken."),
            ("Buislasersnijden", "Kokerprofiel op lengte gesneden, met de verstekken en de gaten voor het glas in dezelfde gang."),
            ("Lassen", "De segmenten in een mal tot een cirkel gelast, de stijlen en de dorpel aangelast en de naden afgewerkt."),
            ("Oppervlaktebehandeling", "Poedercoaten in de gevelkleur, uitbesteed aan een coater en door ons geregeld."),
        ],
        "resultaat": (
            "<p>Ooms ontving per deur een compleet frame: rond, gelast tot &eacute;&eacute;n geheel en gepoedercoat in de gevelkleur, klaar om het glas in te zetten.</p>"
            "<p>Snijden en lassen gebeurden in onze werkplaats; het coaten regelden wij bij de coater. Voor de bouw was er &eacute;&eacute;n aanspreekpunt voor het hele frame.</p>"
        ),
    },
}
