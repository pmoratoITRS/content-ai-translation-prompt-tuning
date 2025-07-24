{
  "hero": {
    "title": "Overzicht Transactiemonitoring"
  },
  "title": "Overzicht Transactiemonitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/overzicht-transactiemonitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Transactiemonitoring, ook wel web application monitoring genoemd, wordt gebruikt om het correct functioneren van gebruikersinteracties op uw website te controleren. De interactie kan een simpele login zijn of alle acties die nodig zijn om een product in uw webshop te kopen. 

Om deze gebruikersinteracties te monitoren, moet u ze in een script plaatsen dat telkens opnieuw kan worden uitgevoerd om te controleren of alles nog steeds werkt zoals verwacht. Uptrends biedt de transaction recorder (als een Chrome-extensie) om op een eenvoudige manier een script te bouwen. Nadat u het script heeft opgenomen, kunt u het zelf bijschaven (self-service transacties) of Uptrends' support vragen het script te verfijnen (full-service transacties). Als u goed bent in scripten, kunt u besluiten het opnemen over te slaan en uw eigen script meteen in een transactiecontroleregel plaatsen.

Wanneer u een transactieopname uploadt naar uw Uptrends-account, wordt er een transactiecontroleregel gemaakt met wat basisinformatie. U zult een aantal instellingen aan uw behoeften moeten aanpassen.

Zodra u uw transactiecontroleregel heeft getest en tevreden bent over de manier waarop deze werkt, gaat u verder en stelt u er [alerting]([LINK_URL_1]) voor in. Dit is immers waar het om gaat: gewaarschuwd worden wanneer dingen niet werken zoals verwacht.

[SHORTCODE_1]
We hebben een stapsgewijze tutorial [Gebruikersreis in een winkel]([LINK_URL_2]) met uitleg vanaf de basis tot transactiemonitoring en het controleren van monitoringdata.
[SHORTCODE_2]

## 1. Introductie

Als webapplicatie-/transactiemonitoring nieuw is voor u, kunt u achtergrondinformatie vinden in de volgende artikelen:

- Krijg een introductie in [Wat is Web Application Monitoring?]([LINK_URL_3])
- Lees [waarom u web application monitoring zou moeten gebruiken]([LINK_URL_4])
- Controleer of web application monitoring [de juiste oplossing]([LINK_URL_5]) voor u is

## 2. Uw transactiemonitoring plannen

Inzicht in de werking van uw transacties, de functionaliteit die u moet testen en de impact van uw monitoring op uw systemen is een essentieel onderdeel van het plannen van uw transacties. Mogelijk moet u ook andere teams van uw bedrijf betrekken bij het opzetten van transactiemonitoring.

- [Breng mogelijke transactiepaden in kaart]([LINK_URL_6])
- Beslis [wat te testen]([LINK_URL_7])
- [Waarschuwingen, tips en trucs]([LINK_URL_8]): dingen om rekening mee te houden en op te letten bij het opzetten van uw monitoring
- [Redenen waarom u mogelijk hulp nodig heeft]([LINK_URL_9]) van andere teams binnen uw bedrijf

## 3. Uw transacties opnemen

Het op de juiste manier gebruiken van de [transaction recorder]([LINK_URL_10]) leidt tot schonere opnamen en een snellere set-up van de controleregel.

- [Download en gebruik de transaction recorder]([LINK_URL_11])
- Volg de [stapsgewijze winkelwagentutorial]([LINK_URL_12]) om te leren hoe u de transaction recorder gebruikt
- Kies tussen [full-service en self-service transacties]([LINK_URL_13])

## 4. Uw transactiescript bewerken en testen

Nadat u uw transactie heeft opgenomen en ervoor heeft gekozen het script zelf te testen (u kunt uw tests ook door ons support team laten uitvoeren), moet u problemen met het resulterende script oplossen, inhoudcontroles instellen als u dat nog niet heeft gedaan en de vault-gebruikersrechten aanpassen voor nieuw gecreëerde items. Tot slot moet u de controleregel in staging mode in de gaten houden voordat u uw controleregel naar production verplaatst.

- Meer informatie over de editor, stappen en acties is te vinden in [De stap-editor begrijpen]([LINK_URL_14])

- Acties vormen de kern van transacties. Meer informatie over acties:
   - [Pagina-interacties - navigeren, klikken, instellen, etc.]([LINK_URL_15])
   - [Test-acties - inhoudcontroles en wachten]([LINK_URL_16])
   - [Bediening-acties - schakelen tussen (inline) frames of tabbladen]([LINK_URL_17])
   - [Bediening-acties - aanpassen variabele-inhoud]([LINK_URL_18])
   - [Negeer fouten voor optionele stappen en acties]([LINK_URL_19])
   - [Selectors gebruiken]([LINK_URL_20]) en [selectoralternatieven]([LINK_URL_21])
   - [Transactievariabelen]([LINK_URL_22]) en [inhoud variabele aanpassen]([LINK_URL_23])

- In de oefening [Uw script testen en bewerken]([LINK_URL_24]) vindt u meer informatie over de *Test starten*-functionaliteit, omgaan met dynamische ID's en time-out fouten. De les bevat ook een [Checklist voor testen]([LINK_URL_25]).

- Een paar andere zaken waarmee u te maken kunt krijgen, afhankelijk van uw set-up en transacties:
  - [Beheer gevoelige waarden]([LINK_URL_26]) die automatisch aan de vault zijn toegevoegd tijdens het opnemen
  - [Beheer vaultrechten (automatisch gecreëerde secties)]([LINK_URL_27])
  - Transactiemonitoring voor [mobiel instellen]([LINK_URL_28])
  - Werken met een [shadow DOM]([LINK_URL_29]) in uw transactie
  - Werken met [sms-gebaseerde 2FA]([LINK_URL_30]) of [op eenmalig wachtwoord gebaseerde 2FA]([LINK_URL_31]) in uw transactie

  - Toevoegen van [extra kengetallen]([LINK_URL_32]) zoals [Core Web Vitals]([LINK_URL_33]) en [W3C Navigatietijden]([LINK_URL_34]) aan uw transactieresultaten.

  - Bypass of omzeil het standaard DNS-systeem door een [DNS bypass]([LINK_URL_35]) in uw transactie te gebruiken.

## 5. Resultaten van transactiemonitoring

Zodra uw transacties worden gemonitord ontvangt u feedback. Er zijn een aantal bronnen die u kunt bekijken om erachter te komen wat er misgaat, wanneer er dingen misgaan.

- [Screenshots]([LINK_URL_36])

- [Watervallen]([LINK_URL_37])

- [W3C Navigatietijden]([LINK_URL_38])

- [Core Web Vitals]([LINK_URL_39])

- [Fouten analyseren]([LINK_URL_40])

## 6. Problemen oplossen

Wanneer de transactiemonitoring niet naar verwachting werkt, zijn hier een paar dingen om te controleren: 

- [A/B-tests uitsluiten]([LINK_URL_41])

- [Gebruik incognito-modus]([LINK_URL_42])

- [Waarschuwingen, tips en trucs]([LINK_URL_43])

## Credits

Transactiecontroleregels gebruiken transactiecredits waarmee u controleregels kunt creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]([LINK_URL_44]) voor meer informatie.
