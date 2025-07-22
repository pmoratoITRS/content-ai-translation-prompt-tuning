{
  "hero": {
    "title": "De effecten van Stagingmodus op rapporten en SLA-data"
  },
  "title": "De effecten van Stagingmodus op rapporten en SLA-data",
  "summary": "Een controleregel in Stagingmodus genereert data die uw rapportage op verschillende manieren beïnvloedt.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/de-effecten-van-Stagingmodus-op-rapporten-en-sla-data",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/the-effects-of-staging-mode-on-reports-and-sla-data"
}

Stagingmodus, waar we het in het artikel [Controleregelmodus](/support/kb/synthetic-monitoring/controleregel-instellingen/controleregelmodus) over hadden, is een geweldige manier om uw controleregels tet esten zonder dat ze uw uptime- en SLA-data beïnvloeden. Bovendien verstuurt Stagingmodus geen alerts. De controleregels doen metingen en werken als elke andere controleregel in productionmodus, maar u hoeft zich geen zorgen te maken dat ze uw rapportage verknoeien. Laten we eens kijken hoe controleregels in stagingmodus worden weergegeven in uw rapportage.

## Hoe beïnvloedt stagingmodus mijn dashboards Beschikbaarheid en Fouten?

Als u een optie selecteert in het dashboardmenu **Beschikbaarheid en Fouten**, ziet u data voor uw controleregels in stagingmodus, maar:

-   Data die zijn verzameld voor controleregels in stagingmodus dragen niet bij aan rapportages voor downtime, controletelling, foutentellingen; en,
-   Net als bij een uitgeschakelde controleregel is de gerapporteerde uptime altijd 100% voor de tijd dat u de controleregel in stagingmodus hebt staan.

## Hoe beïnvloedt stagingmodus mijn Performance dashboards?

Als u een optie selecteert in het dashboardmenu **Performance**, ziet u dat Uptrends de metingen opneemt voor de:

-   Resolve,
-   Connectie,
-   Download, en
-   Totale tijd.

## Hoe beïnvloedt stagingmodus mijn Controleregel log?

De controleresultaten van uw controleregels in stagingmodus worden wel weergegeven in uw **Controleregel log**. Uptrends markeert controles die zijn uitgevoerd door een controleregel in stagingmodus met een pictogram van een kegelvormige fles. 

## Hoe beïnvloedt stagingmodus mijn SLA-rapporten?

In uw SLA-rapporten rapporteert Uptrends een controleregel in stagingmodus op dezelfde manier als een uitgeschakelde controleregel met 100% uptime en nul bevestigde fouten en downtime. De SLA-rapporten bevatten geen fouten of downtime die door een controleregel in stagingmodus worden gegenereerd.
