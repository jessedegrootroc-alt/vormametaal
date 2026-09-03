# -*- coding: utf-8 -*-
"""Inhoud van de dienstpagina Nabewerking. Het skelet staat in bouw_service.py.

Feiten uit BRIEF.md: nabewerking is afbramen, tappen, boren en verzinken, en
Vorma doet die bewerking in eigen huis. Verder staat er in de bron niets over
machines, diktes, toleranties of doorlooptijden, dus staat dat hier ook niet.
De brontekst is input en geen waarheid: de formulering hieronder is nieuw,
alleen de feiten zijn overgenomen.

De pagina houdt &eacute;&eacute;n lijn vast: het onderdeel montageklaar maken &mdash; braamvrije
kanten, schroefdraad in het onderdeel zelf, gaten en verzinkingen waar ze horen &mdash;
zonder dat er een tweede leverancier bij komt. De koppen zijn zo geschreven dat
iemand die alleen scant de pagina begrijpt, en de FAQ neemt de vragen weg die
iemand nog heeft voordat hij een aanvraag verstuurt.
"""

DIENST = {
    "bestand": "dienst-nabewerking.html",
    "slug": "nabewerking",
    "service_naam": "Nabewerking",
    "service_naam_kort": "Nabewerking",
    "namespace": "dienst-nabewerking",
    "onderwerp": "nabewerking",
    "titel": "Nabewerking | Vorma Metaal",

    # Meta description, 120-155 tekens: eerst letterlijk de vier bewerkingen uit
    # de bron (dat is waar iemand op zoekt), dan het feit dat het eigen huis is.
    "omschrijving": "Afbramen, tappen, boren en verzinken in eigen huis. Vorma Metaal levert uw onderdelen montageklaar, in dezelfde offerte als het snijwerk.",

    # Korte typering voor schema.org serviceType; geen marketingterm, gewoon de
    # bewerking zoals een inkoper hem zou inkopen.
    "service_type": "Nabewerking van metaalonderdelen",

    "hero_foto": "productiehal",
    "eyebrow": "Dienst 05",

    # Twee alinea's, samen ongeveer 80 woorden zoals de MADEGRO-intro. Alinea 1
    # gaat ervan uit dat de bezoeker Vorma niet kent: eerst in gewone taal wat
    # wij maken, dan wat nabewerking is, uitgelegd aan de vier bewerkingen uit
    # de bron. Alinea 2 is de eerste vertrouwensstap: eigen huis, dezelfde
    # werkplaats, dezelfde offerte. Geen claim over machines, maten of termijnen.
    "intro": '''          <p>Vorma Metaal maakt metaalonderdelen op tekening: wij snijden, zetten, lassen en verspanen plaat, buis en profiel voor zakelijke opdrachtgevers. Nabewerking is alles wat daarna nog aan het onderdeel gebeurt &mdash; de scherpe snijrand (braam) wegnemen, schroefdraad in de gaten tappen, boren, en verzinken zodat een schroefkop niet uitsteekt.</p>
          <p>Wij doen dat in eigen huis, in dezelfde werkplaats waar uw onderdeel is gesneden, gezet of gelast. De nabewerking loopt mee in dezelfde aanvraag en dezelfde offerte als het snijwerk, van &eacute;&eacute;n stuk tot een serie.</p>''',

    # Eén à twee zinnen, ongeveer 24 woorden zoals MADEGRO, als inleiding op de
    # drie kaarten. Zegt concreet wat er zonder nabewerking uit de werkplaats
    # komt, zodat de bezoeker zijn eigen situatie herkent. Geen uitspraak over
    # hoe vaak iets voorkomt: de bron zegt niets over aantallen aanvragen.
    "wanneer_intro": "Zonder nabewerking komt uw onderdeel met scherpe snijkanten en met gaten zonder schroefdraad uit de werkplaats. In deze drie gevallen heeft u nabewerking nodig.",

    # Exact drie situaties, elk 19-25 woorden zoals de MADEGRO-kaarten. Elke
    # kaarttitel is een situatie die de bezoeker in zijn eigen tekening
    # terugziet en hangt aan één bewerking uit de bron (tappen, afbramen,
    # verzinken), zodat de kaarten elkaar niet herhalen. Boren komt bij de
    # stappen aan de orde. Geen plaatdiktes, draadmaten of toleranties.
    "herkenning": [
        ("U wilt de schroef in het onderdeel zelf draaien",
         "Schroefdraad in het onderdeel scheelt u losse moeren en een handeling bij de montage. Wij tappen de gaten die u op de tekening aanwijst."),
        ("De snijkanten zijn nog scherp",
         "De braam die bij het snijden achterblijft, snijdt in de handen en houdt vlakken bij de montage van elkaar af. Wij halen hem eraf."),
        ("De schroefkop mag niet uitsteken",
         "Bij panelen en delen die vlak tegen elkaar moeten sluiten verzinken wij de gaten, zodat de kop van de schroef gelijk met het vlak ligt."),
    ],

    "aanpak_kop": "Van tekening naar getapt en braamvrij onderdeel",

    # Twee à drie zinnen, ongeveer 45 woorden zoals MADEGRO. Beschrijft de plek
    # van deze bewerking in de vijf stappen uit BRIEF.md (aanvraag, controle,
    # offerte, productie, levering of afhalen) zonder een doorlooptijd of
    # planning te noemen: die staan nergens in de bron.
    "aanpak_intro": "De nabewerking begint bij uw aanvraag: uit uw bestanden lezen wij welke gaten schroefdraad krijgen, geboord of verzonken worden. In de werkplaats komt ze na het snijden, kanten en lassen, en gaat ze vooraf aan de oppervlaktebehandeling als uw onderdeel nog gecoat wordt.",

    # Vier stappen binnen deze bewerking, elk ongeveer 28 woorden zoals de
    # drie-stapsversies bij MADEGRO. Elke titel noemt de handeling zelf, zodat
    # de trap zonder de tekst eronder te lezen valt. De volgorde volgt de
    # bewerkingen uit de bron: eerst de maakbaarheidscontrole, dan afbramen, dan
    # schroefdraad en gaten, dan de overdracht naar wat erna komt. detail is None,
    # want &ldquo;herkenbaar gedrag&rdquo; hoort bij het MADEGRO-onderwerp en niet hier.
    "stappen": [
        ("Wij controleren de gaten op uw tekening",
         "Bij de maakbaarheidscontrole kijken wij of de gaten en verzinkingen op uw tekening kloppen met het materiaal dat u kiest. Is iets onduidelijk, dan stemmen wij het met u af.",
         None),
        ("De snijkanten afbramen",
         "De braam die bij het snijden en boren ontstaat, halen wij van de kanten en de gatranden. Er blijft niets scherps achter dat bij de montage in de weg zit.",
         None),
        ("Schroefdraad tappen, gaten boren en verzinken",
         "Schroefdraad, gaten en verzinkingen brengen wij aan zoals ze op uw tekening staan. Daarmee is het onderdeel klaar voor de bouten en schroeven waarmee u het monteert.",
         None),
        ("Door naar lassen, coating of levering",
         "Wij stemmen de nabewerking af op wat erna komt: lassen in eigen huis, de oppervlaktebehandeling die wij buiten de deur voor u regelen, of de levering of het afhalen in Goor.",
         None),
    ],

    "voordelen_kop": "Uw onderdeel komt montageklaar uit dezelfde werkplaats",

    # Exact vier voordelen, tekst 13-21 woorden zoals MADEGRO. De titels zijn
    # geen labels maar uitspraken, zodat ook een scannende bezoeker ze snapt.
    # Alle vier zijn terug te voeren op de bron: eigen huis, één offerte volgens
    # een vaste calculatie, en het poedercoaten dat Vorma voor u regelt. Geen
    # doorlooptijd, geen capaciteitsbelofte.
    "voordelen": [
        ("vinkje", "U kunt het onderdeel direct vastschroeven",
         "Schroefdraad, gaten en verzinkingen zitten er al in. Uw monteur pakt het onderdeel uit en kan het meteen vastzetten."),
        ("document", "Nabewerking staat in dezelfde offerte",
         "Afbramen, tappen, boren en verzinken worden geoffreerd bij het snijden, kanten en lassen, volgens dezelfde vaste calculatie."),
        ("klok", "Het onderdeel gaat de werkplaats niet uit",
         "Snijden, kanten, lassen en nabewerken gebeuren op &eacute;&eacute;n adres in Goor. U hoeft er geen tweede bedrijf bij te zoeken."),
        ("schild", "Braamvrij de poedercoating in",
         "Scherpe randen en braam in de gaten zijn weg voordat het onderdeel naar de coating gaat die wij voor u regelen."),
    ],

    # LEEG. MADEGRO had hier drie samenwerkingspartners. Vorma Metaal heeft
    # alleen zusterbedrijf Tentije Industri&euml;le Automatisering B.V., en dat
    # bedrijf komt in de lopende tekst al aan de orde. Niets verzinnen.
    "partners": [],

    # Kop van het slotblok: dit is de laatste sectie en dus de aanvraagfase. De
    # knop eronder is &ldquo;Vraag een offerte aan&rdquo;, dus de kop vraagt hier om de
    # opdracht in plaats van nog een keer uit te leggen wat nabewerking is.
    # Zes woorden, zoals MADEGRO.
    "contact_kop": "Laat uw onderdelen bij ons montageklaar maken",

    # Exact vier vragen, en bewust de vier die iemand nog heeft voordat hij op
    # verzenden drukt: welke bestanden, wat er na het versturen gebeurt en wie
    # de tekening beoordeelt, welk materiaal en welke aantallen, en of de prijs
    # de nabewerking dekt. Elke alinea 20-33 woorden zoals MADEGRO. De
    # antwoorden gebruiken alleen wat in BRIEF.md staat: STEP, DXF en DWG met
    # eventueel een PDF, maakbaarheidscontrole, automatische offerte voor
    # standaardwerk en persoonlijke beoordeling bij complex werk, staal, RVS en
    # aluminium, vaste calculatie, vrijblijvend, akkoord voor de start,
    # enkelstuks tot series, en het telefoonnummer. Geen levertijd, geen prijs.
    "faq": [
        ("Welke bestanden moet ik aanleveren?", [
            "Het portaal leest STEP, DXF en DWG in. Voeg een PDF-tekening bij waarop staat welke gaten schroefdraad krijgen, geboord worden of verzonken moeten worden.",
            "Staat het niet in uw bestanden? Vermeld het dan bij uw aanvraag, of bel 0547 227 000 en wij nemen de tekening met u door.",
        ]),
        ("Wat gebeurt er nadat ik mijn aanvraag heb verstuurd?", [
            "Wij controleren eerst zelf of uw aanvraag maakbaar is, de gevraagde nabewerking inbegrepen. Bij een complexe opdracht bellen wij u voordat de offerte uitgaat.",
            "Standaardwerk offreert het portaal automatisch: uw offerte staat binnen enkele minuten online. Complexe opdrachten en bijzondere materialen beoordelen wij persoonlijk, binnen korte tijd.",
        ]),
        ("In welk materiaal en in welke aantallen kan het?", [
            "Wij bewerken staal, RVS en aluminium; bijzondere metalen zijn op aanvraag leverbaar. Bij uw aanvraag selecteert u het materiaal in het portaal.",
            "Aantallen liggen niet vast: van &eacute;&eacute;n stuk tot seriematige productie. De nabewerking hoort er in beide gevallen bij.",
        ]),
        ("Zit de nabewerking in de prijs van mijn onderdeel?", [
            "Ja. Afbramen, tappen, boren en verzinken staan in dezelfde offerte als het overige werk, volgens een vaste calculatie, zodat u weet waar u aan toe bent.",
            "Uw aanvraag is vrijblijvend en het werk start pas na uw akkoord. Vraagt u hetzelfde onderdeel later opnieuw aan, dan geldt dezelfde calculatie.",
        ]),
    ],
}
