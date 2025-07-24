{
  "hero": {
    "title": "Gegevensbescherming in Multi-step API's"
  },
  "title": "Gegevensbescherming in Multi-step API's",
  "summary": "Weet hoe uw Multi-step API-monitoringinformatie wordt beschermd.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-gegevensbescherming",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false,
  "sectionlist": "true"
}

Wanneer u een synthetic controleregel in Uptrends uitvoert, voert de server vanaf die controlestationlocatie monitoringtests uit. Op het niveau van de controlestationserver haalt Uptrends alle monitoringresultaten op en slaat deze rechtstreeks op het Uptrends-platform op.

De meeste organisaties hebben strikte regels met betrekking tot gegevensprivacy en geven er de voorkeur aan om uit te sluiten dat gevoelige informatie in welke vorm dan ook wordt opgehaald of verzonden. Met de functie **Gegevensbescherming** kunt u uitsluiten dat specifieke monitoringdetails worden verzameld en opgeslagen in Uptrends. Deze functie biedt een extra beveiligingslaag, waardoor gevoelige informatie niet extern wordt verzonden (of de Controlestation-server verlaat).

![MSA Gegevensbescherming-selectievakje]([LINK_URL_1])

Standaard wordt de volgende informatie verzameld en weergegeven als onderdeel van uw MSA-monitoringresultaten:

- HTTP Request en Response headers van uw website
- HTTP Response-inhoud van uw website
- Resolved IP-adresverbindingsgegevens van uw website

Als u een van de selectievakjes uitschakelt, wordt voorkomen dat de bijbehorende informatie naar het Uptrends-platform wordt verzonden. In plaats daarvan wordt een bericht weergegeven waarin staat dat dergelijke data niet worden verzameld vanwege het gegevensbeschermingsbeleid van uw bedrijf.

![Uitgeschakelde MSA Gegevensbescherming]([LINK_URL_2])

## Gerelateerde artikelen

Raadpleeg [dit knowledgebase-artikel]([LINK_URL_3]) voor meer informatie over gegevensbescherming op persoonlijke locaties.
