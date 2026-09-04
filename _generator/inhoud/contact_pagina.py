# -*- coding: utf-8 -*-
# Inhoud van contact.html. Het sjabloon zelf verandert niet: dezelfde drie
# secties in dezelfde volgorde als bij MADEGRO (patroonhero, formulierband met
# een col-lg-4 tekstkolom naast het formulier, en de vlakkenrij met vier
# gekleurde vlakken). Hier staat alleen de tekst.
#
# Enige bron voor de feiten: inhoud/BRIEF.md. Welke MADEGRO-component welke
# Vorma-inhoud krijgt staat in inhoud/MAPPING.md; contact.html staat daar bij de
# pagina's die ongewijzigd hergebruikt worden.
#
# Deze pagina staat in de aanvraagfase, en dan in de tak "ik wil eerst
# overleggen": de bezoeker weet inmiddels wat Vorma Metaal doet en heeft nog drie
# vragen: kan ik hier gewoon iets vragen, wat moet ik aanleveren als ik een prijs
# wil, en wat kost het mij om ernaar te vragen. De tekstkolom naast het formulier
# beantwoordt die drie in die volgorde: eerst de uitnodiging om te overleggen,
# dan het CAD-bestand (STEP, DXF of DWG, eventueel met een PDF) plus het
# materiaal en het aantal, daarna de regel dat aanvragen vrijblijvend is en het
# werk pas na akkoord start.
#
# De brontekst van de contactsectie op vormametaal.nl ("Een vraag over uw
# project? Heeft u een vraag, of wilt u uw aanvraag eerst persoonlijk bespreken?
# Bel, mail of laat uw gegevens achter. Wilt u een offerte? Dien uw aanvraag in
# via ons portaal.") is input, geen norm. De feiten erin staan er nog allemaal;
# de formulering is anders en concreter. De twee routes blijven wel gescheiden:
# overleg loopt via dit formulier, een offerte via het portaal.
#
# Wat hier bewust NIET staat, omdat het nergens in de bron staat: een
# reactietermijn op een bericht via het formulier, levertijden, capaciteit,
# certificeringen, machines, plaatdiktes, toleranties, klantnamen en het
# KvK-nummer. Het vierde vlak van MADEGRO was "Madegro Advies B.V." met een
# KvK-nummer; dat nummer is voor Vorma Metaal onbekend, dus dat vlak draagt hier
# de openingstijden, die wel vaststaan.
#
# De gegevens staan als letterlijke tekst in dit bestand en niet als verwijzing,
# want dit bestand importeert niets. Telefoon, e-mail, adres en openingstijden
# moeten dus gelijk blijven aan de constanten in schil.py.
#
# Het formulier op deze pagina heeft velden voor naam, bedrijfsnaam, e-mail,
# telefoon, onderwerp en bericht (zie contactformulier.js) en géén
# bestandsupload. De tekst hiernaast noemt daarom wel welke bestanden een
# aanvraag nodig heeft, maar vraagt u niet ze hier aan te hechten; waar u ze
# uploadt staat in "portaal_regel", een paar regels lager in dezelfde kolom.

CONTACT_PAGINA = {
    "bestand": "contact.html",
    "namespace": "contact",
    "titel": "Contact | Vorma Metaal",

    # Meta description, 155 tekens (MADEGRO had er 127, de vorige versie 147).
    # Opent met de vraag waarmee iemand hier zoekt, noemt dan de twee routes die
    # deze pagina biedt (bellen of het formulier) met bedrijf, plaats en nummer
    # erbij, en neemt tot slot het risico weg. De bestandsformaten stonden hier
    # eerder, maar die horen bij het portaal en niet bij deze pagina: het
    # formulier hiernaast heeft geen uploadveld, dus "stuur uw tekening" in het
    # zoekresultaat belooft iets wat de pagina niet doet.
    # Geen reactietermijn en geen offertetermijn, want daarvoor geldt in de bron
    # een onderscheid tussen standaardwerk en complex werk dat niet in één regel
    # past zonder onwaar te worden.
    "omschrijving": "Een vraag over uw metaalwerk? Bel Vorma Metaal in Goor: 0547 227 000 of vul het formulier in. Aanvragen is vrijblijvend; een offerte loopt via ons portaal.",

    # Label boven de h1, zoals bij MADEGRO.
    "hero_label": "Contact",

    # De h1 is geen paginanaam meer maar de drie routes die op deze pagina zelf
    # staan: het telefoonnummer, het e-mailadres en het formulier. Het label
    # erboven zegt al waar u bent; "Contact" twee keer op elkaar zei niets over
    # de inhoud.
    #
    # De vorige kop ("Stel uw vraag of start uw aanvraag") beloofde iets wat deze
    # pagina niet kan: een aanvraag start u in het portaal, en dat staat drie
    # regels lager ook. Wat u hier wel kunt is bellen, mailen of uw vraag
    # achterlaten, en dat is nu wat er staat. "Metaalwerk" erbij, want wie alleen
    # de koppen scant moet zien waarover hij hier iets kan vragen.
    #
    # 45 tekens, en dat past: de h1 loopt op tot 5rem in een halve container en
    # breekt daar over twee of drie regels. De kop lijnt onderaan uit in een vak
    # met een minimumhoogte, dus extra regels groeien naar boven in ruimte die er
    # al is. Dezelfde hero draagt op diensten.html een kop van 49 tekens.
    "hero_titel": "Bel, mail of stel uw vraag over uw metaalwerk",

    # Twee alinea's in de .article-body naast het formulier, in dezelfde
    # verhouding als bij MADEGRO: een alinea van circa 170 tekens (hier 175) en
    # daaronder een korte regel van circa 45 tekens (hier 60).
    #
    # Alinea 1 begint bij wat u op deze pagina kunt doen: overleggen, via het
    # formulier of per telefoon. Dat is de fase waarin deze pagina staat; de
    # offerteroute loopt via het portaal en staat een paar regels lager. Pas
    # daarna komt wat een prijs nodig heeft: het CAD-bestand in de formaten uit
    # BRIEF.md (het portaal leest STEP, DXF en DWG in, eventueel met een
    # PDF-tekening) plus materiaal en aantal, want zonder die twee valt er niets
    # te calculeren. "CAD-bestand" staat er voor de afkortingen, zodat een
    # inkoper die STEP, DXF en DWG niet kent alsnog weet wat hij bij zijn
    # ontwerper moet opvragen. "Vul het formulier in" en niet "hieronder", want
    # op breed scherm staat het formulier rechts.
    #
    # Alinea 2 vervangt de MADEGRO-regel "We reageren binnen één werkdag". Een
    # reactietermijn staat niet op vormametaal.nl en zou verzonnen zijn. Op deze
    # plek hoort de tweede vraag van de aanvraagfase: wat kost het mij om te
    # vragen. Het antwoord staat wél in de bron (stap 3: een vrijblijvende
    # offerte, het werk start pas na uw akkoord) en het is het sterkste argument
    # om nu op verzenden te drukken. De openingstijden stonden hier eerder, maar
    # die staan in het vierde vlak hieronder al voluit.
    "intro": '''            <p>Wilt u uw opdracht eerst bespreken? Vul het formulier in of bel ons. Voor een prijs hebben wij uw CAD-bestand nodig (STEP, DXF of DWG), met het materiaal en het aantal erbij.</p>
            <p>Aanvragen is vrijblijvend: het werk start pas na uw akkoord.</p>''',

    # De regel onder de intro, op de plek van MADEGRO's .contact-direct (79
    # tekens zichtbare tekst; deze regel is er 76). De tweede belofte uit de
    # brontekst: wie een prijs wil, moet weten waar zijn aanvraag heen gaat. De
    # tweede zinshelft zegt het expliciet, want dat is de enige verwarring die
    # deze pagina kan geven: het formulier ernaast heeft geen uploadveld.
    # "Daar loopt de aanvraag" stond hier eerder en liet in het midden of dat
    # naast dit formulier of in plaats daarvan was.
    #
    # TODO-CONTENT: het webadres van het portaal zelf staat niet in BRIEF.md.
    # Deze regel is daarom platte tekst zonder link, net als elke andere
    # portaalvermelding in inhoud/ (diensten.html is niet het portaal en mag zo
    # ook niet heten). Zodra de portaal-URL bekend is, hoort "ons portaal" hier
    # een <a href="..."> te worden.
    "portaal_regel": '''Wilt u een offerte? Die vraagt u aan in ons portaal, niet via dit formulier.''',

    # De vier vlakken van de vlakkenrij, in vaste volgorde: geel, grijs, wit,
    # groen. Elk vlak houdt de MADEGRO-vorm aan: één regel met het gegeven en
    # daaronder één korte regel context van circa 25 tekens.
    #
    # Vlak 1 en 2 zijn aanklikbaar, zodat een bezoeker op een telefoon direct kan
    # bellen of mailen.
    #
    # De contextregel bij vlak 1 zei eerder "Op werkdagen bereikbaar" en zei
    # daarmee hetzelfde als vlak 4, drie plekken verder, maar vager. Nu zegt hij
    # waarvoor u belt: overleg over uw opdracht ("Bel of mail ons als u wilt
    # overleggen. Wij denken met u mee over uw opdracht" uit de brief).
    #
    # TODO-CONTENT bij e-mail: MADEGRO had hier "Antwoord binnen één werkdag".
    # Op vormametaal.nl staat geen reactietermijn op een bericht, dus die regel
    # is een uitnodiging in plaats van een belofte. Er stond "Voor vragen over uw
    # aanvraag", en dat sloot precies de bezoeker uit die nog niets heeft
    # aangevraagd: die leest dan dat dit adres niet voor hem is. De brief zegt
    # alleen "Bel of mail ons als u wilt overleggen" en beperkt e-mail nergens
    # tot lopend werk. Niet "Voor uw aanvraag", want een offerteaanvraag loopt
    # volgens dezelfde brief via het portaal. Wordt er intern een reactietermijn
    # afgesproken, dan kan die hier komen.
    #
    # Vlak 3 heeft één regel meer dan de andere drie: het adres is zelf al twee
    # regels, en de derde regel is de enige plek op deze pagina waar staat wat u
    # met dat adres kunt. Afhalen is stap 5 uit de brief ("Uw producten worden
    # geleverd, of staan klaar om af te halen") en Dammaten 14 is het enige
    # adres dat er is. Er stond "Hier kunt u ook afhalen" zonder te zeggen wat;
    # nu staat het onderwerp erin, in het woord uit de brief. De vlakken lijnen onderaan uit binnen een minimumhoogte
    # van 280px, dus die extra regel groeit naar boven en verschuift niets.
    #
    # Vlak 4 draagt de openingstijden in plaats van de bedrijfsnaam met
    # KvK-nummer die MADEGRO hier had; het KvK-nummer van Vorma Metaal staat niet
    # in de bron.
    "gegevens": [
        ("Telefoon",
         '<a href="tel:+31547227000">0547 227 000</a><br>Voor overleg over uw opdracht'),
        ("E-mail",
         '<a href="mailto:info@vormametaal.nl">info@vormametaal.nl</a><br>Stuur ons uw vraag'),
        ("Adres",
         "Dammaten 14<br>7472 DJ Goor<br>Uw producten kunt u hier ook afhalen"),
        ("Openingstijden",
         "maandag t/m vrijdag: 07:30&ndash;16:30<br>zaterdag en zondag: gesloten"),
    ],
}
