# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

UIT = pathlib.Path(__file__).resolve().parent.parent  # hoofdmap van de site, één niveau boven _generator

# ============================================================ contact.html
# In het e-mailvlak van de gegevensrij staat geen reactietermijn. Er stond
# "Antwoord binnen &eacute;&eacute;n werkdag"; die termijn staat nergens op
# vormametaal.nl en was dus verzonnen. De tweede regel zegt nu wat u meestuurt.
inhoud = f'''{patroonhero("01", "contact", "Contact", "Contact")}

  <section class="band background--white" id="s02-formulier">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <div class="article-body">
            <p>Stuur uw CAD-bestand mee (STEP, DXF of DWG, eventueel met een PDF-tekening) en vermeld het materiaal en het aantal. Dan kunnen wij meteen beoordelen of het maakbaar is.</p>
            <p>Weet u nog niet welke bewerkingen u nodig heeft? Beschrijf het onderdeel; wij bepalen de route. Een aanvraag is vrijblijvend: het werk start pas na uw akkoord.</p>
          </div>
          <p class="contact-direct">Liever meteen iemand spreken? Bel
            <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a> of mail naar
            <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>

        <div class="col-lg-8 col-12">
          <div class="contact-formulier-wikkel">
            <div data-contactformulier data-onderwerp="overig"></div>
            <noscript>
              <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons op
                <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
            </noscript>
          </div>
        </div>
      </div>
    </div>
  </section>

{vlakkenrij("03", "gegevens", "Onze gegevens", [
    ("Telefoon",
     f'<a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a><br>Ma t/m vr 07:30&ndash;16:30'),
    ("E-mail",
     f'<a href="mailto:{EMAIL}">{EMAIL}</a><br>Stuur uw tekening mee'),
    ("Adres",
     f"{ADRES_STRAAT}<br>{ADRES_POSTCODE} {ADRES_PLAATS}"),
    ("Openingstijden",
     "<br>".join(f"{d}: {t}" for d, t in OPENINGSTIJDEN)),
])}
'''

(UIT / "contact.html").write_text(pagina(
    bestand="contact.html",
    titel="Contact | Vorma Metaal",
    omschrijving="Vraag een offerte aan bij Vorma Metaal. Stuur uw CAD-bestand in STEP, DXF of DWG mee; wij beoordelen de maakbaarheid en offreren vrijblijvend.",
    namespace="contact",
    pagina_css="contact.css",
    css_naam="contact",
    inhoud=inhoud,
), encoding="utf-8")

# ======================================================= tekstpagina's
# Geen f-string: dit blok bevat {EMAIL} twee keer en verder accolades die
# letterlijk moeten blijven. De sleutel wordt hieronder vervangen, zodat er
# geen onvervangen plaatshouder in de geleverde pagina kan staan.
PRIVACY = '''  <section class="tekstband" id="s01-privacybeleid">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Privacybeleid</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wie verwerkt uw gegevens</h2>
        <p>Vorma Metaal, Dammaten 14, 7472 DJ Goor. Voor vragen over dit beleid kunt u terecht bij <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Welke gegevens en waarom</h2>
        <h3>Contactformulier</h3>
        <p>Vult u het formulier in, dan verwerken wij uw naam, bedrijfsnaam, e-mailadres, telefoonnummer, het gekozen onderwerp en uw bericht. Die gegevens gebruiken we alleen om uw vraag te beantwoorden en, als dat tot een opdracht leidt, om die uit te voeren.</p>
        <p>Grondslag: uw toestemming, en bij een lopende opdracht de uitvoering van de overeenkomst.</p>

        <h3>Bezoekgegevens</h3>
        <p>De site plaatst geen analytische of marketingcookies zolang u daar geen toestemming voor geeft. Uw keuze bewaren wij in de lokale opslag van uw browser onder de naam <span class="invulveld">vorma-cookies-v1</span>. Dat is geen cookie: het gaat niet mee naar de server.</p>

        <h2>Hoe lang we het bewaren</h2>
        <p>Berichten via het formulier bewaren we tot twee jaar na het laatste contact. Gegevens die bij een opdracht horen bewaren we zolang de wet dat vraagt, voor de administratie zeven jaar.</p>

        <h2>Met wie we het delen</h2>
        <p>We verkopen geen gegevens. We delen ze alleen met partijen die nodig zijn om te leveren: de partij die deze site host, en de partij die het contactformulier verwerkt.</p>
        <div class="invulblok">
          <p>De hostingpartij en de partij die het formulier verwerkt moeten hier met naam genoemd worden, met de vermelding of er een verwerkersovereenkomst ligt.</p>
        </div>

        <h2>Uw rechten</h2>
        <p>U mag uw gegevens inzien, corrigeren of laten verwijderen, en u mag bezwaar maken tegen de verwerking. Stuur een mail naar <a href="mailto:{EMAIL}">{EMAIL}</a>; wij reageren binnen een maand. Bent u het niet eens met hoe wij ermee omgaan, dan kunt u klagen bij de Autoriteit Persoonsgegevens.</p>

        <h2>Beveiliging</h2>
        <p>De site gaat over https en de gegevens uit het formulier komen alleen terecht bij wie ze nodig heeft.</p>
        <div class="invulblok">
          <p>Beschrijf hier alleen de maatregelen die daadwerkelijk zijn ingericht. Wat er nog niet is, hoort er niet in te staan.</p>
        </div>
      </div>
    </div>
  </section>'''

PRIVACY = PRIVACY.replace("{EMAIL}", EMAIL)
assert "{" not in PRIVACY.replace("{EMAIL}", ""), "onvervangen plaatshouder in PRIVACY"

(UIT / "privacybeleid.html").write_text(pagina(
    bestand="privacybeleid.html",
    titel="Privacybeleid | Vorma Metaal",
    omschrijving="Hoe Vorma Metaal omgaat met uw gegevens.",
    namespace="privacybeleid",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=PRIVACY,
    body_klasse="tekstpagina",
), encoding="utf-8")

COOKIES = f'''  <section class="tekstband" id="s01-cookies">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Cookies</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wat deze site plaatst</h2>
        <p>Op dit moment plaatst deze website geen analytische of marketingcookies. Er draait geen statistiekentool en er staat geen advertentiepixel op de pagina.</p>
        <p>Het enige dat wordt opgeslagen is uw eigen keuze in de cookiemelding. Die bewaren we in de lokale opslag van uw browser onder de naam <span class="invulveld">vorma-cookies-v1</span>, zodat u de vraag niet bij elk bezoek opnieuw krijgt.</p>

        <h2>De drie categorie&euml;n</h2>
        <h3>Functioneel</h3>
        <p>Nodig om de site te laten werken, waaronder het onthouden van uw keuze. Hiervoor is geen toestemming vereist.</p>
        <h3>Analytisch</h3>
        <p>Bedoeld om te zien welke pagina&rsquo;s bezocht worden, zodat de site verbeterd kan worden. Er staat een statistiekentool klaar die pas laadt nadat u analytische cookies heeft aangezet.</p>
        <div class="invulblok">
          <p>Welke statistiekentool er gebruikt gaat worden en welk meet-ID daarbij hoort, moet hier nog ingevuld worden. Zolang dat veld leeg is, laadt er niets.</p>
        </div>
        <h3>Marketing</h3>
        <p>Voor advertenties en het meten van het effect daarvan. Op dit moment niet in gebruik.</p>

        <h2>Uw keuze wijzigen</h2>
        <p>U kunt uw keuze op elk moment aanpassen of intrekken.</p>
        <p><button type="button" class="cookie-knop cookie-knop--donker" data-cookie-instellingen>Cookie-instellingen openen</button></p>

        <h2>Wat er verder gebeurt</h2>
        <p>De pagina laadt de scripts voor de pagina-overgangen van een extern adres. Dat zet geen cookies, maar ontvangt wel het IP-adres van uw bezoeker:</p>
        <ul>
          <li>cdn.jsdelivr.net</li>
        </ul>
        <p>De lettertypen staan op onze eigen server; daar gaat dus niets naartoe. Meer over gegevens staat in het <a href="privacybeleid.html">privacybeleid</a>.</p>
      </div>
    </div>
  </section>'''

(UIT / "cookies.html").write_text(pagina(
    bestand="cookies.html",
    titel="Cookies | Vorma Metaal",
    omschrijving="Welke cookies Vorma Metaal gebruikt en hoe u uw keuze aanpast.",
    namespace="cookies",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=COOKIES,
    body_klasse="tekstpagina",
), encoding="utf-8")

print("contact.html, privacybeleid.html en cookies.html geschreven")
