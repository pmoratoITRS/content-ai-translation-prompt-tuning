{
  "title": "Converteer Uptime-controleregels eenvoudig naar API-controleregels op de API-hub",
  "date": "2025-04-24",
  "url": "/changelog/april-2025-api-suggesties",
  "translationKey": "https://www.uptrends.com/changelog/april-2025-api-suggestions"
}

De [API-hub](https://app.uptrends.com/Hubs/Api) bevat nu een functie die automatisch uw bestaande controleregels scant en identificeert welke controleregels kunnen worden omgezet naar [API-controleregels]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}). Als er HTTP- of HTTPS-controleregels worden gedetecteerd die een API-eindpunt lijken te controleren, biedt de hub de optie om automatisch een nieuwe API-controleregel voor u te creëren.

Deze functionaliteit upgradet elke [Uptime-controleregel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}}) direct naar een volledig geconfigureerde API-controleregel zonder de oorspronkelijke controleregel te verwijderen of te wijzigen. U kunt zo nodig de actie op elk moment ongedaan maken. Bovendien hoeft u niet alles handmatig helemaal opnieuw te maken, Uptrends verzorgt de volledige configuratie en repliceert dezelfde instellingen van uw bestaande controleregels.

Na de conversie kunt u de configuratie bekijken en inschakelen voor gebruik. Raadpleeg het knowledgebase-artikel [Multi-step API-hub]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="nl" >}}) voor meer informatie.

![Tegel API-suggesties](/img/content/scr-api-suggestions.min.png)