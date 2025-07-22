{
  "hero": {
    "title": "Overzicht monitoringsresultaten"
  },
  "title": "Overzicht monitoringsresultaten",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/overzicht-monitoringsresultaten",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/monitoring-results-overview",
  "sectionlist": false
}

Bij het uitvoeren van controleregelchecks zullen er verschillende soorten resultaten of rapporten zijn, afhankelijk van het controleregeltype en uw instellingen. De [details van de controle]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="nl" >}}) bevatten veel resultaten en ze bestaan voor alle controleregels. Sommige resultaten kunnen echter alleen van toepassing zijn op een aantal controleregeltypes, de waterval bijvoorbeeld bestaat zowel voor Full Page Check-controleregels als voor transactiecontroleregels, maar niet voor andere controleregeltypes.

## Kengetallen

Met de **Core Web Vitals** en **W3C-navigatietijden** beschikt u over twee reeksen kengetallen die zijn gebaseerd op internationale normen. De kengetallen stellen u in staat om de performance van uw website beter te begrijpen en erachter te komen wat er moet worden verbeterd om hoger te scoren in zoekmachine rankings.

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}})
- [W3C-navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}})

Merk op dat u deze kengetallen aan een aangepast dashboard kunt toevoegen door een aangepaste rapporttegel van het type [Eenvoudige lijst / grafiek]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="nl" >}}) toe te voegen.

## Waterval

De watervalgrafiek is een visualisatie van uw monitoringresultaten in een staafdiagram en laat in detail zien wanneer pagina-elementen zijn geladen en hoelang het duurde. Het is een goed hulpmiddel om problemen op te lossen en erachter te komen wat het laden van een pagina vertraagt. Bekijk de Knowledge Base-artikelen over watervallen:

- [Watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}})
- [Waterval timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="nl" >}})
- [De resultaten van het watervalrapport interpreteren]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="nl" >}})

## Verdere probleemoplossing

De resultaten van een controleregelcheck worden verzameld in de details van de controle. Ze kunnen het startpunt zijn voor het oplossen van problemen.

- [Details van de controle]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="nl" >}})

Daarnaast bevatten de controleresultaten de paginabron (HTML-bron) en de  console log (van het laden van de pagina). Deze informatie is beschikbaar in controleresultaten van transacties en Full Page Check-controleregels. Mogelijk moet u de functie inschakelen, raadpleeg het onderstaande Knowledge Base-artikel voor meer informatie.

- [Paginabron en console log]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="nl" >}})

De watervalgrafiek geeft u een goed inzicht in het laden van uw pagina-elementen. Het kan echter moeilijk zijn om u stap voor stap voor te stellen wat daar gebeurt. De screenshots van de tijdlijn kunnen u helpen te begrijpen hoe de pagina eruitziet bij verschillende stappen in het laadproces.

- [Tijdlijn screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}})
