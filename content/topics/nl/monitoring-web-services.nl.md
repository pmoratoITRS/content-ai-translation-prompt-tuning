{
  "hero": {
    "title": "Webservices monitoren"
  },
  "title": "Webservices monitoren",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/webservices-monitoren",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/monitoring-web-services"
}

{{< callout >}} **Opmerking:** Voor API monitoring zijn de controleregeltypes **Webservice HTTP en Webservice HTTPS** niet langer beschikbaar voor nieuwe gebruikers. Uptrends raadt aan om in plaats daarvan de [Multi-step API-controleregel]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="nl" >}}) te gebruiken om uw API-gedrag optimaal te controleren. {{< /callout >}}

De Uptrends Webservice HTTP- en HTTPS-controleregels zijn een van de talrijke [controleregeltypes]({{< ref path="support/kb/basics/monitor-types" lang="nl" >}}) die Uptrends biedt. 

## Welke webservices worden ondersteund?

Uptrends ondersteunt *REST*, en *SOAP*, evenals elke webservice die bereikbaar is via *HTTP*, *HTTPS*.

## Hoe werken deze webservices met Uptrends??

-   We monitoren dat de webservicerespons HTTP 200 OK is en meten resolvetijd/verbindingstijd, downloadtijd en totale tijd, net als bij HTTP(S)-controleregels  
-   Webservice monitoring ondersteunt ook Basic Authentication, inhoudcontroles enzovoort  
-   De meeste webservicecontroleregels gebruiken HTTP POST-instellingen om POST-data naar de server te posten als onderdeel van het aanroepen van de webservice  
-   Doorgaans is bij SOAP-services een XML-document (SOAP-envelop) nodig als POST-data in de request body, evenals een specifieke HTTP-header die SOAP Action wordt genoemd.  
-   Bij sommige webservices is vereist dat HTTP-headers voor content type worden ingesteld

**Bijvoorbeeld**:

-   \`Content-Type: application/json\` als de POST-data JSON-data zijn  
-   \`Content-Type: text/xml\` of application/xml als de POST-data XML zijn (dit is standaard bij webservice-controleregels, anders dan bij gewone HTTP(S)-controleregels)
