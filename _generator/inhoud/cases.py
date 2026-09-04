# -*- coding: utf-8 -*-
"""Inhoud van cases.html en de drie casepagina's. Het skelet staat in
bouw_cases.py; het register met beelden, bewerkingen en bestandsnamen staat in
schil.py onder CASES.

LET OP: dit zijn VOORBEELDPROJECTEN. Op vormametaal.nl staan geen cases en er
is geen opdrachtgever die deze projecten bevestigt. Daarom:

 - de opdrachtgever is anoniem: "een liftenbouwer", "een leverancier van
   roltrappen", "een deurenfabrikant";
 - geen aantallen, jaartallen, plaatsnamen of citaten;
 - de tekst beschrijft het soort werk dat bij het beeld past en dat Vorma met
   zijn acht bewerkingen kan maken, niet een geleverd resultaat;
 - elke pagina draagt het label "Voorbeeldproject -- nog te bevestigen".

Pas als Vorma Metaal per project bevestigt wat er echt gemaakt is, mag de
tekst concreter worden en gaat het label eraf (CASES[...]["voorbeeld"] = False).
"""

CASES_PAGINA = {
    "bestand": "cases.html",
    "namespace": "cases",
    "titel": "Projecten | Vorma Metaal",
    "omschrijving": "Drie voorbeelden van plaatwerk en profielwerk voor liften, roltrappen en draaideuren: wat er gemaakt wordt, van welk materiaal en met welke bewerkingen.",
    "hero_label": "Projecten",
    "hero_titel": "Wat er uit onze werkplaats komt",
    "intro_kop": "Drie voorbeelden van werk voor de installatiebranche",
    "intro_tekst": (
        "          <p>Liften, roltrappen en draaideuren zijn producten waar veel plaatwerk en profielwerk in zit dat in het zicht komt: deurbekleding, zijpanelen, omlijstingen, frames. Precies het werk waarvoor onze acht bewerkingen bedoeld zijn.</p>\n"
        "          <p>Hieronder staat per voorbeeld wat er gemaakt wordt, van welk materiaal en welke bewerkingen erbij horen. De opdrachtgevers noemen wij niet bij naam.</p>"
    ),
    "raster_kop": "Drie voorbeelden",
    "contact_kop": "Heeft u vergelijkbaar werk?",
    "contact_tekst": "Stuur uw CAD-bestand mee, of stel eerst uw vraag. Een aanvraag is vrijblijvend: het werk start pas na uw akkoord.",
}

# Per case: de tekst op de kaart en de blokken op de eigen pagina.
CASE_TEKSTEN = {
    "liftdeuren": {
        "kaart": "Deurpanelen en omlijstingen in geborsteld RVS, gesneden en gezet uit plaat, met de zichtzijde beschermd tot aan de montage.",
        "lead": "Een liftdeur is het eerste wat een gebruiker van een lift ziet en aanraakt. De bekleding moet strak zijn, kraswerend en jaren meegaan.",
        "opdracht_kop": "Wat er gemaakt wordt",
        "opdracht": (
            "<p>Voor een liftenbouwer gaat het om de plaatdelen die de deur en de omlijsting bekleden: de deurpanelen zelf, de zijkanten van het kozijn en de bovenrand. Alles in RVS 304 met een geborstelde afwerking, zodat de richting van de borstel over alle delen gelijk loopt.</p>"
            "<p>De platen komen aan met beschermfolie op de zichtzijde. Die folie blijft erop tijdens het snijden, zetten en vervoeren, zodat er geen kras op de zichtzijde komt voordat de deur hangt.</p>"
        ),
        "aanpak_kop": "Hoe het door de werkplaats gaat",
        "aanpak": (
            "<p>De contouren en uitsparingen komen uit het CAD-bestand van de liftenbouwer en worden met de laser uit de plaat gesneden. Daarna gaan de delen naar de kantbank: de randen worden omgezet, zodat een deurpaneel stijf wordt en een schone kant krijgt.</p>"
            "<p>Waar delen aan elkaar moeten, wordt gelast en daarna de naad afgewerkt. Afbramen en het aanbrengen van bevestigingsgaten horen bij de nabewerking, in dezelfde aanvraag.</p>"
        ),
        "materiaal_kop": "Materiaal en afwerking",
        "materiaal": "RVS 304, afwerking geborsteld, geleverd met beschermfolie op de zichtzijde.",
    },
    "roltrappen": {
        "kaart": "Zijpanelen, sokkels en leuningsteunen voor roltrappen: vlak plaatwerk in RVS en gesneden buis en profiel voor het dragende deel.",
        "lead": "Bij een roltrap zit het plaatwerk aan de buitenkant: de zijpanelen langs de treden en de sokkels onder de balustrade. Dat werk moet vlak zijn en aansluiten op de glazen delen.",
        "opdracht_kop": "Wat er gemaakt wordt",
        "opdracht": (
            "<p>Voor een leverancier van roltrappen gaat het om twee soorten delen. De zijpanelen en sokkels zijn plaatwerk in RVS, lang en smal, met een gezette rand die tegen het glas van de balustrade aansluit. De steunen onder de leuning zijn buis- en profielwerk in staal.</p>"
            "<p>De panelen komen in beeld op ooghoogte, dus de zichtzijde telt. De dragende delen komen niet in beeld, maar moeten wel maatvast zijn omdat de leuning erop wordt uitgelijnd.</p>"
        ),
        "aanpak_kop": "Hoe het door de werkplaats gaat",
        "aanpak": (
            "<p>De plaatdelen worden met de laser gesneden en op de kantbank gezet. Omdat de panelen lang zijn, wordt de zetvolgorde vooraf bepaald zodat het deel na de laatste zetting nog op de machine past.</p>"
            "<p>De leuningsteunen komen van de buislaser: de buis wordt op lengte gesneden en de bevestigingsgaten worden in dezelfde gang gemaakt. Afbramen van alle snijkanten hoort bij de nabewerking.</p>"
        ),
        "materiaal_kop": "Materiaal en afwerking",
        "materiaal": "Zijpanelen en sokkels in RVS 304; leuningsteunen in staal, geschikt om te coaten.",
    },
    "draaideuren": {
        "kaart": "Het ronde frame en de dorpel van een draaideur: kokerprofiel op maat gesneden, gelast tot een geheel en gepoedercoat in de kleur van de gevel.",
        "lead": "Een draaideur bestaat uit glas en een frame. Het frame draagt het glas, bepaalt de ronding en moet buiten jaren tegen weer en gebruik kunnen.",
        "opdracht_kop": "Wat er gemaakt wordt",
        "opdracht": (
            "<p>Voor een deurenfabrikant gaat het om het stalen frame: de ronde bovenrand, de stijlen die het glas vasthouden en de dorpel onderin. Het frame wordt gemaakt uit kokerprofiel en afgewerkt met een poedercoating in de kleur die bij de gevel past.</p>"
            "<p>De ronding is het lastige deel. De bovenrand bestaat uit gesneden segmenten die tot een cirkel worden gelast, en die cirkel moet rond zijn, want anders loopt de deur aan.</p>"
        ),
        "aanpak_kop": "Hoe het door de werkplaats gaat",
        "aanpak": (
            "<p>De kokerprofielen komen van de buislaser: op lengte, met de verstekken en de gaten voor het glas in dezelfde gang gesneden. De segmenten van de bovenrand worden in een mal tegen elkaar gezet en gelast, daarna wordt de naad afgewerkt zodat hij onder de coating niet meer te zien is.</p>"
            "<p>Het poedercoaten besteden wij uit en regelen wij: het frame gaat na het lassen naar de coater en komt afgewerkt terug, en de opdrachtgever heeft daar geen tweede leverancier voor nodig.</p>"
        ),
        "materiaal_kop": "Materiaal en afwerking",
        "materiaal": "Stalen kokerprofiel, gelast, gepoedercoat in een gevelkleur.",
    },
}
