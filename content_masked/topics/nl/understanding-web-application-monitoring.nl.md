{
  "hero": {
    "title": "Transactiemonitoring begrijpen"
  },
  "title": "Transactiemonitoring begrijpen",
  "summary": "In dit artikel leert u wat transactiemonitoring (ook wel web application monitoring genoemd) is, hoe het werkt en welke soorten transacties u kunt monitoren. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/web-application-monitoring-begrijpen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wat is transactiemonitoring, ook wel web application monitoring genoemd? U kunt een gedetailleerde beschrijving lezen in [Web application monitoring]([LINK_URL_1]) Kort samengevat:

*Web Application Monitoring is een synthetische controleregel of bot die gebruikersacties uitvoert op een website of webapplicatie met regelmatig geplande intervallen. De controleregel gebruikt een webbrowser (net als uw gebruikers) om te controleren of de site of applicatie correct functioneert en goed presteert.*

Dus vrijwel elke transactie die een gebruiker op uw site met een browser kan uitvoeren, kan een transactiecontroleregel ook doen met regelmatige intervallen. Transactiemonitoring controleert uw site 24 uur per dag, zeven dagen per week. Wanneer de transactie fout gaat of te lang duurt, geeft Uptrends' alertingsysteem u een seintje.

## Waarom zou u uw webapplicaties monitoren? [ANCHOR_1]

Waarom zou u transacties willen monitoren, u zult het immers merken als er iets misgaat. Zeker, uiteindelijk zult u het opmerken, maar welke schade wordt in de tussentijd aangericht aan gebruikersvertrouwen en reputatie?

### De hoge kosten van trage en falende webapplicaties

Als uw website of service niet goed werkt, stappen uw gebruikers gewoon over naar uw concurrenten. En ze stappen niet alleen over naar een concurrent, veel van hen komen nooit meer terug.

Falende webapplicaties kosten u meer aan toekomstige inkomsten dan aan directe inkomsten. Zou u genoeg vertrouwen hebben in een merk en uw persoonlijke gegevens geven als hun applicatie hapert en traag is?

Door uw transacties in de gaten te houden met transactiemonitoring weet u onmiddellijk wanneer er een probleem is. U kunt het probleem meteen oplossen voordat het gevolgen heeft voor uw gebruikers.

### Er kan meer fout gaan dan u denkt

Sommige bedrijven controleren hun transacties sporadisch gedurende de werkdag, maar wat gebeurt er nadat uw personeel 's avonds naar huis gaat? Natuurlijk, uw piekuren zijn dan wel voorbij, maar moet uw applicatie niet ook tijdens daluren werken? Uw werkdag eindigt, maar uw site werkt 24 uur per dag. Er kunnen veel verschillende dingen misgaan die u misschien niet opmerkt als u niet 24/7 monitort. Als u uw transacties 24 uur per dag controleert, kunt u voor verschillende problemen worden gewaarschuwd, zoals:

- Traag laden van pagina's en transacties als gevolg van voorraadupdates in de vroege ochtend of andere backend-processen. Processen die plaatsvinden wanneer u hoopt dat uw gebruikers het niet zullen merken (maar dat doen ze wel).
- Externe afhankelijkheden die niet correct werken:
  -   **Bedrijfseigenaren**: updates van productvoorraad, prijsberekeningen en bestelsystemen.
  -   **Systeemintegraties**: externe betaalproviders, locatieservices, SharePoint/Office365-integraties en externe rekenmodules.
  -   **E-commerce en web analytics**: Trackers voor gebruikersgedrag, Google Analytics en advertentiesystemen.

    Hoewel deze afhankelijkheden van derden op add-ons lijken, kunnen downtime, trage performance of slecht gedrag van externe systemen uw algehele prestaties beïnvloeden en zelfs de weergave en het gedrag van uw pagina's verstoren.

## Wat voor soort transacties kan ik monitoren?

Een betere vraag is: “Wat voor soort transacties kan ik niet monitoren met transactiemonitoring.” Hier zijn een paar voorbeelden van transacties die u mogelijk wilt overwegen om te monitoren op performance en functie.

- Succesvolle logins
- De zoekfunctie van uw site gebruiken
- De kalender gebruiken in een reserveringssysteem
- Winkelwagenfuncties: productopties toevoegen, verwijderen en selecteren
- Invullen van formulieren zoals bestelformulieren met koppelingen naar andere diensten zoals adresverificatie en verzendkostenberekeningen.
- Succesvolle financiële transacties: verbinding maken met merchant services, gebruikersinvoer valideren en geldige server responses ontvangen.

## Hoe kies ik de transacties die ik wil monitoren?

Uw site bevat waarschijnlijk erg veel mogelijke gebruikersscenario's. U kunt niet elk scenario testen, dus hoe maakt u een keuze? Natuurlijk wilt u de transacties testen die cruciaal zijn voor het succes van uw site en waarop uw gebruikers vertrouwen (veel daarvan zijn hierboven genoemd). Kies ook transacties die veel verschillende systemen en services vereisen om samen te komen om goed te functioneren en te presteren. Kies transacties die veel delen van uw systemen raken om te verifiëren:

- Beschikbaarheid en responstijden van ondersteunende servers
- Databasetoegang en responses: als er meer dan één database is, kies dan transacties die ze allemaal raken. Dit kan uw gebruikers-, product-, orderverwervings-, gebruikersgegevensdatabase of een andere database zijn waarvan uw systeem afhankelijk is.
- Beschikbaarheid en functie van externe diensten: bijvoorbeeld locatie- en adresverificatie, postcode opzoeken, voorraadbeheersystemen, logistiek, merchant services of klantrelatiebeheersystemen.

## Welke data gebruik ik voor tests?

Wanneer u kiest welke data u voor tests wilt gebruiken, wilt u wellicht testdata gebruiken. In het geval van een e-commercesite wilt u bijvoorbeeld product-ID's gebruiken die niet zijn gekoppeld aan echte producten in de voorraad om ongewenste gevolgen te voorkomen. We hebben een hele pagina over de valkuilen die u moet vermijden bij het monitoren van uw sites en services. Sommige van die problemen zijn een direct gevolg van de data die u kiest om te testen. Lees vooral de pagina [Waarschuwingen, tips en trucs]([LINK_URL_2]) voor meer informatie over mogelijke problemen en hun oplossingen, maar hier zijn enkele dataspecifieke problemen waarmee u rekening moet houden.

### E-commerce
Houd er bij het kiezen van producten voor uw tests rekening mee dat als uw voorraad opraakt, uw controleregel zal mislukken.

- Uw controleregel kan bestellingen genereren die uw beschikbare voorraad verbruiken. Deze bestellingen die afkomstig zijn van uw tests, kunnen gebruikers beletten om een product te kopen vanwege onvoldoende beschikbaarheid.
- Bestellingen die worden gegenereerd als gevolg van tests, kunnen ertoe leiden dat automatische bevoorradingssystemen meer producten bestellen.
- Het genereren van pickbonnen en verzendlabels die ertoe leiden dat de verzendafdeling testitems verpakt en zelfs verzendt.
- E-mails met aankoopbevestigingen kunnen iemands inbox vullen, zo niet de uwe.
- Het testen van betaalsystemen kan beschikbare tegoeden verbruiken en echte kosten voor merchant services genereren.

### Reserveringssystemen
Reserveringssystemen en vergelijkbare oplossingen hebben hun eigen uitdagingen.

- Uw controleregel kan uw beschikbare reserveringsslots opvullen, waardoor echte gebruikers niet kunnen plannen.
- E-mailbevestigingen vullen inboxen.
- Betaalde reserveringen kunnen creditcardkosten en servicekosten met zich meebrengen.

### Inloggegevens

U wilt inloggegevens veilig houden en geen duplicaten hebben vanwege automatisch gegenereerde inloggegevens. Houd deze aanbevelingen in gedachten:

- Kies inloggegevens zorgvuldig.
- Beperk de [gebruikersrechten]([LINK_URL_3]) van de testgebruiker en monitor het account nauwlettend op ongewone activiteiten.
- Bescherm inloggegevens in de Uptrends [vault]([LINK_URL_4]).
- Log de gebruiker uit aan het einde van de transactie om inlogconflicten te voorkomen wanneer dezelfde gebruiker bij de volgende test probeert in te loggen.

### Analyse en Real User Monitoring

Uw monitoring heeft invloed op uw analyses en Real User Monitoring-data. Dit kan echter worden opgelost door [URL en analytics blokkeren]([LINK_URL_5]) te gebruiken.

## Is een transactiecontroleregel altijd de beste keuze? [ANCHOR_2]

Een transactiecontroleregel is geweldig om ervoor te zorgen dat alles samenwerkt om het verwachte resultaat te creëren. Andere controleregeltypes kunnen u echter meer informatie geven over de algehele performances en beschikbaarheid van uw website of service.

### Website beschikbaarheid 

Transactiecontroleregels checken uw site slechts met tussenpozen van vijf minuten of meer, dus u kunt veel downtime verzamelen tussen transactiecontroles. Met controleregels voor beschikbaarheid kunt u de beschikbaarheid op webpagina's of webservices met veel kortere tussenpozen controleren. U heeft ook opties voor [geavanceerde beschikbaarheidscontroleregels]([LINK_URL_6]) voor databases, e-mailservers, FTP/SFTP-servers, SSL-certificaten en DNS responses.

### Website performance

Transactiemonitoring legt paginalaadtijden vast en als u ervoor kiest, kunt u watervalrapporten toevoegen om wat extra laadtijdgegevens te krijgen. Echter, performancemonitoring gaat, als het uw transacties betreft, meer over de responsiviteit van uw servers op uw gebruikersinteracties, zoals submits. [Web Performance Monitoring]([LINK_URL_7]) geeft u meer gedetailleerde data over de performance van een pagina vanaf de eerste request tot het voltooide laden van de pagina. Een controleregel van het type [Full Page Check]([LINK_URL_8]) geeft u gedetailleerde informatie over de laadtijd van één pagina. U kunt de voortgang en performance van het laden van de pagina voor de hele pagina en voor elk element bekijken. U krijgt niet alleen meer details over elke controle, maar Uptrends heeft ook uw performancedashboards geoptimaliseerd voor het weergeven van de laadtijddata voor één pagina voor snelle vergelijking. 

### API Monitoring

Uw transactie heeft hoogstwaarschijnlijk meerdere API calls. Terwijl sommige calls enkelvoudig zijn, kunnen andere meerdere requests hebben om een volledige transactie te voltooien. Door de API's apart van uw transacties te controleren met [API Monitoring]([LINK_URL_9]) kunnen API-problemen eerder aan het licht komen en krijgt u meer gegevens voor analyse van de kern van de oorzaak wanneer uw transactie mislukt.

Om de beschikbaarheid van uw webservices te monitoren, gebruikt u het controleregeltype Webservice HTTP of Webservice HTTPS, waarmee u elke minuut van de dag de beschikbaarheid van de API kunt controleren. U kunt alle aan de API gekoppelde service level agreements volgen en sneller reageren op beschikbaarheidsproblemen dan met transactiemonitoring.

De controleregel voor een reeks stappen wordt gedefinieerd met een [Multi-step API-controleregel (MSA-controleregel)]([LINK_URL_10]). Deze controleregel verifieert responses en performance voor volledige API-interacties (of er nu één of meerdere responses nodig zijn). U krijgt gedetailleerde informatie over de API responses met validatie. 

Web Application Monitoring richt zich op de volledige interactie tussen een gebruiker en een applicatie, terwijl Multi-step API zich richt op elke API-interactie buiten een webapplicatie. U kunt bijvoorbeeld een Multi-step API-controleregel gebruiken om de communicatie tussen een beveiligingssysteem en de serviceprovider te testen, of om transacties met uw creditcardverwerker te monitoren.

## Moet ik een softwareontwikkelaar zijn om transactiecontroleregels in te stellen? [ANCHOR_3]

Het helpt zeker, maar met uw vaardigheden en kennis over uw apps en services kunt u een heel eind komen, ook als u geen ontwikkelaar bent. Bekijk het artikel [Opties voor transactiescripts]([LINK_URL_11]) voor meer informatie over self-service en full-service transacties, en het scripten van transacties. Uw ontwikkelaars of DevOps-team moeten mogelijk:

- Scripts repliceren en aanpassen voor mirror-sites in meerdere talen of vergelijkbare workflows en functionaliteit.
- Scripts aanpassen voor aankomende site-updates voor implementatie gelijktijdig met uw site-updateschema dat wordt geactiveerd door uw CI/CD-systeem (continue integratie/continue implementatie.
- De Uptrends API gebruiken om uw monitoring-setup te benutten als een waardevolle aanwinst voor uw kwaliteitsborgingssysteem.
