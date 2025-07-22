{
  "hero": {
    "title": "Postman API Monitoring instellen"
  },
  "title": "Postman API Monitoring instellen",
  "summary": "Stapsgewijze instructies voor het instellen van Postman API Monitoring.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring-instellen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/postman-api-monitoring"
}

Uptrends biedt de Postman API-controleregel, waarmee u uw bestaande Postman-werkruimtecollecties automatisch op het netwerk van Uptrends-controlestations kunt uitvoeren. U kunt eenvoudig Postman-scripts plannen en uitvoeren, de prestaties van uw API's testen en alles instellen zoals elke andere controleregel.

Met miljoenen gebruikers is Postman een standaard branchetool die ontwikkelaars gebruiken om API-tests te schrijven, documenteren en uit te voeren. Met deze tool kunt u HTTP-methoden testen (GET, POST, PUT, DELETE, PATCH) en headers, parameters, variabelen en nog veel meer toevoegen. U kunt ook meerdere requests groeperen en organiseren, zogenaamde Postman-collecties, en deze delen met anderen of voor later gebruik. Ga gewoon naar Postman en u kunt nu uw API-scripts uitvoeren met één druk op de knop elke keer dat u uw API's moet testen.

Met Uptrends hoeft u niet naar Postman te gaan en handmatig op een knop te drukken om uw scripts te testen, uw Postman API-controleregel doet het werk voor u. Deze controleregel neemt uw Postman-collectie van API-scripts, inclusief pre- en post-request-scripts, importeert ze met behulp van een API-URL of vanuit een JSON-bestand en voert ze vervolgens over de hele wereld uit, net als andere controleregeltypes.

## Voordelen van het gebruik van de Postman API-controleregel

Als uw organisatie Postman al gebruikt, profiteer dan van deze controleregel met deze voordelen in gedachten:

- **Automatische uitvoering van uw scripts**: U kunt uw Postman-scripts elke minuut, 5 minuten, uur en overal ter wereld uitvoeren in plaats van ze handmatig te moeten uitvoeren. We hebben meer dan 200 monitoring [controlestations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/" lang="nl" >}}) die u kunt selecteren en gebruiken om te testen.  

- **Geen opstarttijd**: Door simpelweg uw beschikbare en bestaande scripts in Uptrends te importeren, kunt u deze controleregel direct gebruiken. Het is niet nodig om die scripts om te zetten in een speciale Uptrends-smaak of andere aanpassingen te doen.

- **Niets nieuws om te leren**: Met uw achtergrond in Postman zult u het gemakkelijk vinden om deze controleregel te gebruiken. Wijs ons gewoon naar uw Postman-scripts en wij zullen u in een mum van tijd de resultaten geven.

- **Geen wijzigingen in uw huidige workflow**: U kunt uw scripts gewoon blijven onderhouden in Postman. Houd er rekening mee dat wanneer u wijzigingen aanbrengt in uw collectie, u deze gewoon weer ophaalt in Uptrends en u bent weer up-to-date.

{{< callout >}} Ondersteuning voor [Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/" lang="nl" >}}) is nog niet beschikbaar in de Postman API-controleregel. {{< /callout >}}

## Een Postman API-controleregel instellen

Er zijn twee manieren om de Postman API-controleregel in te stellen: [Postman-scripts importeren vanuit een JSON-bestand]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#import-from-a-json-file" lang="nl" >}}) of [Postman-scripts importeren met een API-URL]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#import-using-an-api-url" lang="nl" >}}).

{{< callout >}} **Opmerking:** Wanneer u Postman-scripts importeert met een API-URL, moet u de optie **Delen** > **Via API** selecteren. Deze optie is alleen beschikbaar voor betaalde Postman-accounts. {{< /callout >}}

### Importeren vanuit een JSON-bestand

Met deze optie kunt u tegelijkertijd een back-up maken van uw Postman-bestanden en wijzigingen van Postman naar Uptrends importeren.

Een controleregel instellen door een JSON-bestand te importeren:

1. Ga naar het menu {{< AppElement type="menuitem" >}} API > API-controleregels beheren (+) {{< /AppElement >}}.
2. Selecteer de optie **Postman API**.
3. Configureer uw [controleregelinstellingen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="nl" >}}) op basis van uw monitoringbehoeften.

4. Selecteer in het tabblad {{< AppElement type="tab" >}} Postman-collectie {{< /AppElement >}} de optie  
**Importeer vanuit een JSON-bestand**. Om uw JSON-bestand te exporteren vanuit Postman raadpleegt u [Export collections from Postman](https://learning.postman.com/docs/getting-started/importing-and-exporting/exporting-data#export-collections).

5. Klik op de knop {{< AppElement type="buttonSecondary" >}} Bestand kiezen {{< /AppElement >}} en importeer uw JSON-bestand. 

Na het importeren wordt de sectie **Collectiedetails** automatisch gevuld met dezelfde informatie die in Postman werd getoond. Details zoals de Collectienaam, ID en requests zijn nu zichtbaar.

![JSON-bestand importeren](/img/content/scr_postman-import-json-file.min.png)

6. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel te bevestigen.

U bent klaar met uw controleregel. Gebruik de knop **Test starten** in uw controleregel-editor om de [controleregelresultaten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#monitor-results" lang="nl" >}}) te testen en te bekijken.

### Importeren met een API URL

Met deze optie kunt u wijzigingen van Postman naar Uptrends importeren met een API-URL, wat handig is voor live testen. Met één klik werkt u uw collectie bij en bespaart u geheugenruimte.

Een controleregel instellen met de API-URL van de Postman-collectie:

1. Ga naar het menu {{< AppElement type="menuitem" >}} API > API-controleregels beheren (+) {{< /AppElement >}}.
2. Selecteer de optie **Postman API**.
3. Configureer uw [controleregelinstellingen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="nl" >}}) op basis van uw monitoringbehoeften.

4. Selecteer in het tabblad {{< AppElement type="tab" >}} Postman-collectie de optie {{< /AppElement >}} **Importeer met een API-URL**.

5. Plak de Postman API-URL in het lege tekstveld. Raadpleeg [Share using the Postman API](https://learning.postman.com/docs/collaborating-in-postman/sharing#share-using-the-postman-api) om de Postman API-URL op te halen.

6. Klik op de knop {{< AppElement type="buttonSecondary" >}} COLLECTIE OPHALEN {{< /AppElement >}} om de data van uw URL op te halen.

Zodra dit is gelukt, wordt de sectie **Collectiedetails** automatisch gevuld met dezelfde informatie die in Postman werd getoond. Details zoals de Collectienaam, ID en requests zijn nu zichtbaar.

![Importeren met een API-URL](/img/content/scr_postman-import-api-url.min.png)

{{< callout >}} **Opmerking:** U moet elke keer dat u uw collectie bijwerkt op de knop {{< AppElement type="buttonSecondary" >}} COLLECTIE OPHALEN {{< /AppElement >}} klikken. Dit zorgt ervoor dat Uptrends uw laatste wijzigingen oppikt en de bestaande Postman-scripts die worden gemonitord, overschrijft. {{< /callout >}}

7. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel te bevestigen.

U bent klaar met uw controleregel. Gebruik de knop **Test starten** in uw controleregel-editor om de [controleregelresultaten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#monitor-results" lang="nl" >}}) te testen en te bekijken..

Raadpleeg de [Postman-documentatie](https://learning.postman.com/docs/collaborating-in-postman/sharing) voor meer informatie.

## Controleregelresultaten

De **testresultaten van de Postman API-controleregel** lijken sterk op de resultaten van de Multi-step API-monitoringresultaten. In de sectie **Details van de controle** weerspiegelt elke stap elke request in de Postman-collectie met specifieke items die hieronder worden weergegeven:

- **Stapduur**: de tijd in milliseconden van hoe lang een stap duurt
- **Stap-assertions**: de werkelijke testresultaten op basis van uw pre-request- en post-response-scripts parallel aan Postman-testresultaten. U kunt het totale aantal geslaagde en mislukte assertions zien, waarbij geslaagde resultaten worden gemarkeerd als groene vinkjes, terwijl mislukte resultaten worden gemarkeerd als een rood kruis.
- We tonen ook andere details, zoals request headers, request content en response headers op dezelfde manier als in Postman. Bijvoorbeeld Cache-control, Content-Length, Server, Date, en andere.

## Credits

Net als Multi-step API-controleregels gebruikt de Postman API-controleregel API-credits. Elke request in de collectie die u importeert gebruikt één credit.