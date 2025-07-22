{
  "hero": {
    "title": "Gegevensbescherming persoonlijke locatie"
  },
  "title": "Gegevensbescherming persoonlijke locatie",
  "summary": "Wat zijn de maatregelen voor gegevensbescherming op persoonlijke locaties?",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-locaties-gegevensbescherming",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-data-protection"
}

In dit knowledgebase-artikel vindt u uitleg over het implementeren van gegevensbescherming op uw persoonlijke locaties. Eén van de maatregelen die zijn geïmplementeerd in Uptrends’ persoonlijke locaties is het voorkomen dat snapshots worden geüpload naar de cloud. U kunt ook pagina-inhoud uitschakelen, HTTP request en response headers en resolved IP-adressen verbergen in details van de controle.

## Het Docker Compose-bestand bewerken

Installeer eerst uw controlestation, als u dat nog niet heeft gedaan, door de stappen te volgen die worden uitgelegd in [Een Docker-controlestation installeren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="nl" >}}).

1. Maak een back-up van het uitgepakte Docker Compose-bestand. Houd er rekening mee dat als u wijzigingen aanbrengt in het verstrekte composebestand, dit op eigen risico is. Neem contact op met [Support]({{< ref path="/contact" lang="nl" >}}) als u twijfelt. 
2. Open het bestand docker-compose.yml en verwijder de comment-tag ``#`` vóór de gegevensbeschermingsvariabele(n) in de Checkpoint-service die u wilt inschakelen. Door de tag te verwijderen wordt gegevensbescherming ingesteld voor het geselecteerde item in de environmentlijst. 


 ```
 Checkpoint:
    container_name: Checkpoint
    image: uptrends.azurecr.io/win2022/checkpoint
    depends_on:
      - TransactionProcessor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: "json-file"
      options:
        max-size: 10m
        max-file: "3"
    environment:
     - ServerId=
     - Password=
     - HasIpv6Support=false
#    - AllowScreenshotsInResults=false
#    - AllowPageContentInResults=false
#    - AllowHttpHeadersInResults=false
#    - AllowResolvedIpAddressesInResults=false
  
 ```    
3. Sla uw bestand op. 
4. Start de container handmatig opnieuw op door de opdracht ```docker-compose down``` uit te voeren en vervolgens ```docker-compose up``` uit te voeren op de opdrachtregel van de map waar het bewerkte Compose-bestand zich bevindt. Controleer de gewijzigde instellingen in de Uptrends-app in het gedeelte [Instellingen gegevensbescherming](#data-protection-settings-status) op het tabblad {{< AppElement type="tab" >}} Controlestationstatus {{< /AppElement >}}.
 
### Voorkomen dat (fout)screenshots en filmstrips worden geüpload naar de cloud
Nadat de instelling actief is, zal de **details van de controle** in Uptrends een tekst weergeven om u te informeren dat screenshots niet worden verzameld vanwege het gegevensbeschermingsbeleid van uw bedrijf. 

Dit geldt voor alle screenshots, waaronder [tijdlijn screenshotss]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}}) (ook wel filmstrips genoemd) en de [foutscreenshots]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="nl" >}}) voor een HTTP(S)-controleregel.

Om screenshots in resultaten uit te schakelen verwijdert u de tag ``#`` vóór `- AllowScreenshotsInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.

{{< callout >}} **Belangrijk**: Het uitschakelen van screenshots betekent precies dat: er worden geen screenshots gemaakt. Dus bij het [oplossen van een fout]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#further-troubleshooting" lang="nl" >}}) zal deze informatiebron niet beschikbaar zijn.
 {{< /callout >}}

### Pagina-inhoud uitschakelen 
Deze instelling zorgt ervoor dat er geen inhoud wordt weergegeven in de [paginabron en console log]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="nl">}}). Data-URL's worden altijd weergegeven zonder data in de resultaten. 

Om pagina-inhoud in resultaten uit te schakelen verwijdert u de tag ``#`` vóór `- AllowPageContentInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.

### HTTP request en response headers verbergen
Nadat deze instelling actief is, worden er geen HTTP request en response headers weergegeven in de watervalgrafiek details van de controle.

Om HTTP request en response headers te verbergen verwijdert u de tag ``#`` vóór `- AllowHttpHeadersInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.
![Gegevensbescherming verborgen HTTP request en response headers in watervalgrafiek](/img/content/scr-data-protection-waterfall-headers.min.png)

### Resolved IP-adressen uitschakelen voor request en response headers
Deze instelling zorgt ervoor dat de rapportheaders in een controleresultaat geen resolved IP-adressen weergeven. Let wel, dit werkt niet als er een letterlijk IP-adres in plaats van een domeinwaarde staat in het URL-veld van uw controleregel(s). 

Om resolved IP-adressen te verbergen verwijdert u de tag ``#`` vóór `- AllowResolvedIpAddressesInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.

### Resolved IP-adressen uitschakelen in details van de controle 
Deze instelling zorgt ervoor dat overal waar een IP-adres is resolved, dit niet wordt weergegeven bij **Resolved IP-adres**.   

Om resolved IP-adressen te verbergen verwijdert u de tag ``#`` vóór `- AllowResolvedIpAddressesInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.

Als deze waarde is ingesteld op 'false' wordt het uitvoeren van DNS-controleregels geblokkeerd op controlestationservers op uw persoonlijke locatie.

{{< callout >}} **Let op**: Niet alle instellingen dekken elk controleregeltype, voor eenvoudige HTTP(S)-controleregels bijvoorbeeld werken alleen foutscreenshots; de resolved IP-instellingen zijn niet van toepassing op dit type controleregel. 
{{< /callout >}}

## Status van gegevensbeschermingsinstellingen 

Het tabblad [Controlestationstatus]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="nl" >}}) in de Uptrends-app toont de status van de gegevensbeschermingsinstellingen. Een rood kruis betekent dat gegevens niet worden weergegeven, dus dat gegevensbescherming is ingeschakeld. Houd er rekening mee dat dit een alleen-lezen weergave is, de instellingen kunnen alleen in het Docker-bestand worden aangepast. 

![Instellingen voor gegevensbescherming op het tabblad Controlestationstatus](/img/content/scr_private-location-checkpoint-health-data-protected.min.png)