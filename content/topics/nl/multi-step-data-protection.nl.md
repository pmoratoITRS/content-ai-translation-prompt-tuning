{
  "hero": {
    "title": "Gegevensbescherming in Multi-step API's"
  },
  "title": "Gegevensbescherming in Multi-step API's",
  "summary": "Weet hoe uw Multi-step API-monitoringinformatie wordt beschermd.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-gegevensbescherming",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-data-protection",
  "tableofcontents": false,
  "sectionlist": "true"
}

Wanneer u een synthetic controleregel in Uptrends uitvoert, voert de server vanaf die controlestationlocatie monitoringtests uit. Op het niveau van de controlestationserver haalt Uptrends alle monitoringresultaten op en slaat deze rechtstreeks op het Uptrends-platform op.

De meeste organisaties hebben strikte regels met betrekking tot gegevensprivacy en geven er de voorkeur aan om uit te sluiten dat gevoelige informatie in welke vorm dan ook wordt opgehaald of verzonden. Met de functie **Gegevensbescherming** kunt u uitsluiten dat specifieke monitoringdetails worden verzameld en opgeslagen in Uptrends. Deze functie biedt een extra beveiligingslaag, waardoor gevoelige informatie niet extern wordt verzonden (of de Controlestation-server verlaat).

![MSA Gegevensbescherming-selectievakje](/img/content/scr-data-protection-checkbox.min.png)

Standaard wordt de volgende informatie verzameld en weergegeven als onderdeel van uw MSA-monitoringresultaten:

- HTTP Request en Response headers van uw website
- HTTP Response-inhoud van uw website
- Resolved IP-adresverbindingsgegevens van uw website

Als u een van de selectievakjes uitschakelt, wordt voorkomen dat de bijbehorende informatie naar het Uptrends-platform wordt verzonden. In plaats daarvan wordt een bericht weergegeven waarin staat dat dergelijke data niet worden verzameld vanwege het gegevensbeschermingsbeleid van uw bedrijf.

![Uitgeschakelde MSA Gegevensbescherming](/img/content/scr-data-protection-disabled-checkbox.min.png)

## Gerelateerde artikelen

Raadpleeg [dit knowledgebase-artikel]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}) voor meer informatie over gegevensbescherming op persoonlijke locaties.
