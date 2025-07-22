{
  "hero": {
    "title": "Paginabron en console log"
  },
  "title": "Paginabron en console log",
  "summary": "Beschrijving van waar de paginabron en console log-informatie te vinden zijn in FPC's en transactiecontroleregels",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/paginabron-console-log",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/page-source-and-console-log"
}

Bij [transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}}) en [Full Page Check-controleregels]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) heeft u de optie om de **paginabron** te bekijken (d.w.z. het HTML-document zoals ontvangen door het controlestation), evenals de **console log** die werd gegenereerd toen we de pagina laadden. 


## In Full Page Checks

Bij Full Page Checks (FPC's) zijn de paginabroninformatie en de console log te vinden in elk controleregelresultaat, onder de [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}). U krijgt altijd de paginabroninformatie, maar de console log is alleen beschikbaar als er daadwerkelijk console log-vermeldingen in de browser waren toen de pagina werd geladen. Meestal genereert de browser console log-vermeldingen wanneer er iets misgaat – als bijvoorbeeld een bepaald element niet correct kan worden geladen of als er een javascript-fout wordt aangetroffen. 

![Voorbeeld van console log die een fout weergeeft](/img/content/scr-pagesource-consolelog.min.png)

## In transactiecontroleregels

Bij transactiecontroleregels moeten de paginabron- en console log-optie expliciet worden ingeschakeld. 
### Paginabron- en console log-registratie instellen in een transactie

Om paginabron- en console log-data voor een specifieke stap in een transactie weer te geven, moet u eerst de optie **Waterval** voor die stap inschakelen (zie onze handleiding over [werken met transactiewatervallen]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}})). Vervolgens wordt de optie **Paginabron** beschikbaar. Als u deze optie selecteert, betekent dit dat de resultaten van de controleregelcheck zowel de paginabroninformatie als eventuele console log-data bevatten die mogelijk zijn gegenereerd tijdens de uitvoering van die stap. 

![Paginabron selecteren in de transactie-editor](/img/content/scr-pagesource-in-transactions.min.png)

### Lokaliseren van de paginabron- en console log-informatie in een transactie

Nadat u de paginabronoptie voor een transactiestap heeft ingeschakeld, kunt u de informatie vinden in de resultaten van uw controleregelcheck die daarna zijn gegenereerd. Zoek de transactie in uw [Controleregel log]({{< AppUrl >}}//Report/ProbeLog) of navigeer naar het transactiedashboard en klik op een van de controleregelresultaten die zijn gegenereerd nadat u de optie Paginabron heeft ingeschakeld. 


![Paginabron- en console log-pictogrammen in transactie](/img/content/scr-pagesource-icons-transaction.min.png)

Om de paginabroninformatie voor deze specifieke stap te openen klikt u op het derde pictogram {{< AppElement type="iconSourceCode" >}}{{< /AppElement >}} in het resultaat van de controleregelcheck. U kunt de console log vinden door op het laatste pictogram {{< AppElement type="iconConsoleLog" >}}{{< /AppElement >}}, te klikken, maar die is mogelijk niet altijd beschikbaar.

