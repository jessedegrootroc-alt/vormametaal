# -*- coding: utf-8 -*-
"""Inhoud van voor-wie.html. Het skelet staat in bouw_rest.bouw_voor_wie() en
verandert niet: het MADEGRO-overzichtssjabloon (patroonhero, introband, een
paneelrij in panel-row--4, FAQ, slotblok).

Enige bron voor de feiten: inhoud/BRIEF.md. Welke MADEGRO-component welke
Vorma-inhoud krijgt staat in inhoud/MAPPING.md; de schrijfnorm in inhoud/COPY.md.

De tien sectoren staan letterlijk in de brief en ook in schil.SECTOREN; hier
staan ze in dezelfde volgorde, met dezelfde namen. Er is geen sector bij
verzonnen en er is er geen weggelaten.

Wat de brief NIET over deze sectoren zegt, en wat hier dus niet staat: welke
producten Vorma per sector maakt, voor welke bedrijven, in welke aantallen of
met welke afmetingen. De paneelteksten beschrijven daarom niet een verzonnen
product, maar wat er in de bron w&eacute;l staat: de acht bewerkingen, de drie
materialen, de bestandsformaten, de maakbaarheidscontrole en het bereik van
enkelstuks tot seriematige productie.

TODO-CONTENT: wil Vorma per sector een concreet voorbeeld noemen van wat er
gemaakt wordt, dan hoort dat in de tweede zin van de betreffende paneeltekst.
Dat kan alleen met opgave van Vorma zelf; verzinnen mag niet.

Eigen huis versus uitbesteed, ook op deze pagina de belangrijkste val:
lasersnijden, buislasersnijden, kanten, lassen, nabewerking en CNC-verspanen
gebeuren in eigen huis; assemblage loopt via zusterbedrijf Tentije
Industri&euml;le Automatisering B.V.; oppervlaktebehandeling wordt uitbesteed
maar volledig door Vorma geregeld. Waar het over alle acht gaat, staat er
&ldquo;bewerkingen&rdquo; of &ldquo;onder &eacute;&eacute;n dak&rdquo;, nooit
&ldquo;in eigen huis&rdquo;.

Aanspreekvorm "u", overal.
"""

VOOR_WIE = {
    "bestand": "voor-wie.html",
    "namespace": "voor-wie",
    "titel": "Voor wie | Vorma Metaal",

    # Meta description: 149 tekens. Noemt eerst de drie sectoren die een
    # inkoper het vaakst intypt, dan het aantal, dan het seriebereik. Geen
    # klantnamen, aantallen of levertijden, want die staan niet in de bron.
    "omschrijving": "Vorma Metaal werkt voor zakelijke opdrachtgevers in machinebouw, constructie, installatietechniek en zeven andere sectoren. Van enkelstuks tot serie.",

    "hero_label": "Voor wie",

    # De h1. Het label boven de titel zegt al "Voor wie", dus de titel hoeft dat
    # niet te herhalen en draagt in plaats daarvan de twee feiten waar een
    # eerste bezoeker naar zoekt: hoeveel sectoren, en of wij in zijn regio
    # werken. 48 tekens, als de titel op deze hero elders (diensten: 49).
    "hero_titel": "Metaalwerk voor tien sectoren, in heel Nederland",

    # Kop van de introband. Los te lezen, en hij zegt in vier woorden wie de
    # klant is: niet "de industrie" of "onze relaties", maar bedrijven die dit
    # werk niet zelf doen. Het aantal sectoren staat al in de h1, dus dat wordt
    # hier niet herhaald. 40 tekens; deze plek droeg 40 tot 57.
    "intro_kop": "Bedrijven die hun metaalwerk uitbesteden",

    # Twee alinea's van ca. 250 tekens, zoals de intro's op de dienstpagina's
    # (230 en 270). Eerste alinea: wie de klant is, benoemd via het werk dat
    # hij uitbesteedt in plaats van via een branche-etiket, plus de 22 jaar en
    # de sectoren waarin die ervaring is opgebouwd. Het werk staat er in de
    # woorden die op de dienstpagina's ook gebruikt worden (plaatwerk,
    # buiswerk, verspaand werk) en niet als samentrekking van vaktermen.
    # Tweede alinea: wat de tien sectoren gemeen hebben, namelijk dezelfde
    # route van CAD-bestand naar offerte, en welke bewerkingen in eigen huis
    # gebeuren. "Kanten" krijgt hier zijn uitleg tussen haakjes, zoals op
    # diensten.html; verderop op deze pagina staat alleen nog "gekant".
    # "Betrouwbare partner" uit de brief is bewust niet overgenomen: dat zegt
    # volgens COPY.md niets; de route en de vijf eigen bewerkingen wel.
    "intro_tekst": "<p>Wij maken onderdelen van metaal op maat voor zakelijke opdrachtgevers: bedrijven die hun plaatwerk, buiswerk en verspaand werk uitbesteden. Onze 22 jaar ervaring is opgebouwd in diverse technische sectoren, met name in de machinebouw en automatisering.</p>\n            <p>Voor alle tien sectoren geldt dezelfde route: u uploadt uw CAD-bestand, wij controleren of het maakbaar is en u ontvangt een vrijblijvende offerte. Snijden, kanten (plaat in vorm zetten), lassen, nabewerken en verspanen gebeuren in onze eigen werkplaats in Goor.</p>",

    # De tien sectoren, in de volgorde van BRIEF.md en gelijk aan
    # schil.SECTOREN. De teksten zijn 98 tot 127 zichtbare tekens; de panelen
    # in panel-row--4 zijn op 1440px 360px breed met 32px inzet, dus daar
    # dragen de bestaande panelen teksten van ca. 110 tekens. Elke regel zegt
    # wat wij voor die sector maken, in de termen van de bron: welke bewerking,
    # welk materiaal of welke kwaliteit erbij hoort, of welke stap uit het
    # proces daar het meest speelt. Geen productnamen, afmetingen, diktes of
    # toleranties: die staan nergens in de bron. Elke regel komt maar
    # &eacute;&eacute;n keer voor; twee sectoren met dezelfde regel zouden
    # betekenen dat er niets over de tweede te zeggen was.
    "sectoren": [
        # Machinebouw staat vooraan omdat de brief de 22 jaar hier expliciet
        # aan ophangt ("met name in de machinebouw en automatisering").
        ("Machinebouw",
         "Hier is onze 22 jaar ervaring opgebouwd. Wij snijden plaat, buis en profiel en verspanen onderdelen uit uw CAD-bestand."),
        # Staal met de voorbeeldkwaliteiten uit de brief. "Bijvoorbeeld" hoort
        # erbij: het zijn voorbeeldkwaliteiten en geen voorraadlijst. De drie
        # lasmethoden staan letterlijk in de brief.
        ("Constructie",
         "Gesneden, gekante en gelaste delen in staal, bijvoorbeeld S235JR of S355MC. Lassen doen wij met TIG, MIG of laser."),
        # Nabewerking uit de brief: afbramen, tappen, boren en verzinken. Voor
        # wie iets in een bestaande opstelling monteert, zijn tappen en boren
        # het punt: dan past het onderdeel meteen. "Tappen" krijgt dezelfde
        # uitleg tussen haakjes als op dienst-lasersnijden.
        ("Installatietechniek",
         "Onderdelen die in een bestaande opstelling passen. Gesneden, gekant en gelast, met tappen (schroefdraad maken) en boren erbij."),
        # RVS uit de brief: hygi&euml;ne, uitstraling, lange levensduur, met
        # afwerking 2B of 1D en met of zonder beschermfolie. Poedercoaten wordt
        # uitbesteed, dus "regelen wij" en niet "doen wij".
        ("Interieurbouw",
         "Werk waarbij de uitstraling meetelt: RVS in afwerking 2B of 1D, met of zonder beschermfolie. Poedercoaten regelen wij erbij."),
        # Niet "onderdelen voor industri&euml;le toepassingen": dat is de
        # sectornaam nog een keer. Wat hier w&eacute;l iets zegt, is dat de
        # bewerkingen op &eacute;&eacute;n plek zitten. "Onder &eacute;&eacute;n
        # dak" en niet "in eigen huis", want assemblage loopt via Tentije en
        # oppervlaktebehandeling wordt uitbesteed.
        ("Industrie",
         "Losse onderdelen of series in staal, RVS of aluminium: snijden, kanten, lassen, nabewerken en verspanen onder &eacute;&eacute;n dak."),
        # De vaste calculatie bij een herhaalaanvraag staat bij de zes punten
        # in de brief: dezelfde calculatiewijze, geen prijsgarantie, dus
        # "volgens dezelfde vaste calculatie" en niet "tegen dezelfde prijs".
        ("Productontwikkeling",
         "Eerst &eacute;&eacute;n prototype uit uw CAD-bestand, later dezelfde onderdelen in serie volgens dezelfde vaste calculatie."),
        # Voor engineering is de maakbaarheidscontrole uit stap 2 het punt,
        # plus de formaten die het portaal inleest.
        ("Engineering",
         "U levert STEP, DXF of DWG aan. Wij controleren de maakbaarheid en stemmen bij een complexe opdracht eerst met u af."),
        # "Acht bewerkingen" en niet "in eigen huis": assemblage loopt via
        # Tentije en oppervlaktebehandeling wordt uitbesteed. Wie inkoopt voor
        # een eigen opdrachtgever, koopt in de eerste plaats &eacute;&eacute;n
        # aanspreekpunt.
        ("Technische dienstverlening",
         "Metaalwerk dat u voor uw eigen opdrachtgever inkoopt, met &eacute;&eacute;n aanspreekpunt voor acht bewerkingen."),
        # "Uit uw tekening" hoort erbij: de bron zegt nergens dat Vorma een
        # bestaand onderdeel opmeet of natekent. E&eacute;n stuk is hier de
        # vraag die telt.
        ("Onderhoud en reparatie",
         "Een vervangingsonderdeel uit uw tekening, ook als het om &eacute;&eacute;n stuk gaat. Gesneden, gekant, gelast of verspaand."),
        # DX51D+Z (sendzimir verzinkt) staat in de brief bij de
        # voorbeeldkwaliteiten staal; dat is de enige bronvaste bijzonderheid
        # die bij deze sector hoort. "Met zinklaag" is de uitleg van het woord
        # verzinkt, geen extra claim over dikte of klasse. Levering en afhalen
        # staan in de FAQ eronder, dus die hoeven hier niet nog een keer.
        ("Bouwgerelateerde bedrijven",
         "Plaat- en profielwerk in staal, ook met zinklaag (DX51D+Z, sendzimir verzinkt). Gesneden, gekant en gelast volgens uw tekening."),
    ],

    # Kop boven de paneelrij. Het bovenkopje "Tien sectoren" staat vast in
    # bouw_rest.py, dus de kop herhaalt het aantal niet. Hij moet w&eacute;l
    # dekken wat eronder staat, en dat zijn tien sectorpanelen met per sector
    # het werk dat wij er maken; een kop die alleen over het seriebereik gaat
    # dekt die panelen niet. Daarom eerst wat de panelen zijn, dan het bereik
    # uit de brief. 47 tekens, als de koppen op deze plek elders (40 tot 54).
    "series_kop": "Wat wij per sector maken, van &eacute;&eacute;n stuk tot serie",

    # E&eacute;n alinea van ca. 170 tekens, als de inleiding op deze plek in
    # het sjabloon (ca. 150 tot 190). Zegt eerst wat er in de panelen staat,
    # dan het antwoord op de vraag uit COPY.md die deze pagina nog niet gaf:
    # kan ik meerdere bewerkingen bij &eacute;&eacute;n partij laten doen. Het
    # seriebereik zit nu in de kop en de vaste calculatie staat in de FAQ
    # eronder, dus die worden hier niet nog een keer gezegd. Geen
    # minimumafname en geen prijs, want die staan niet in de bron.
    "series_tekst": "Elk paneel noemt de bewerkingen en materialen die daar het meest spelen. Vraagt uw onderdeel meerdere bewerkingen, dan lopen die via &eacute;&eacute;n aanvraag en &eacute;&eacute;n offerte.",

    # Drie vragen die iemand op d&eacute;ze pagina heeft: hoor ik erbij, mag
    # het om weinig stuks gaan, en komt u ook buiten Twente. De antwoorden
    # zijn &eacute;&eacute;n of twee alinea's van 100 tot 160 tekens, als de
    # FAQ-antwoorden elders op de site. Alle feiten komen uit BRIEF.md: de
    # maakbaarheidscontrole, het seriebereik, de vaste calculatie, het
    # werkgebied, het adres en de openingstijden. Nergens een levertijd, een
    # minimumafname of een garantie.
    "faq": [
        ("Werkt u ook voor een sector die er niet bij staat?", [
            "Ja. Wij kijken naar uw onderdeel en niet naar de branche waarin u zit: de tien sectoren hierboven zeggen waar onze ervaring zit, niet waar onze grens ligt.",
            "Upload uw STEP-, DXF- of DWG-bestand, of bel 0547 227 000. Wij controleren of uw aanvraag maakbaar is en stemmen bij een complexe opdracht eerst met u af.",
        ]),
        ("Kan ik losse stuks of kleine series laten maken?", [
            "Ja. Wij maken uniek maatwerk en series, van enkelstuks tot seriematige productie. E&eacute;n onderdeel is net zo goed een aanvraag als een herhaalorder.",
            "Vraagt u dezelfde onderdelen later opnieuw aan, dan rekenen wij met dezelfde vaste calculatie, zodat u weet waar u aan toe bent.",
        ]),
        ("Werkt u ook buiten Twente?", [
            "Ja, ons werkgebied is heel Nederland. Onze werkplaats staat aan de Dammaten 14 in Goor, in Twente.",
            "Uw producten worden geleverd, of staan klaar om af te halen in Goor. Wij zijn maandag tot en met vrijdag open van 07:30 tot 16:30.",
        ]),
    ],

    # Kop van het slotblok. De knop eronder is "Vraag een offerte aan", dus
    # dit is de aanvraagfase. De kop haalt de vraag van d&eacute;ze pagina
    # binnen op het moment van aanvragen: mag het ook om weinig stuks gaan?
    # 44 tekens, als de contactkoppen op de dienstpagina's (31 tot 45).
    "contact_kop": "Ook voor &eacute;&eacute;n onderdeel maken wij een offerte",
}
