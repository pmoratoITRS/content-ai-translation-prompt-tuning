{
  "hero": {
    "title": "Aangepaste tegels"
  },
  "title": "Aangepaste tegels",
  "summary": "Toon uw monitoringdata als lijst of grafiek op aangepaste dashboards met aangepaste tegels",
  "url": "/support/kb/dashboards-en-rapportages/dashboards/aangepaste-tegels",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles"
}

Uptrends biedt een breed scala aan rapporttegels die geschikt zijn voor al uw monitoringbehoeften. Deze rapporttegels tonen op handige wijze de statistieken van uw controleregels, controlestations en foutstatus via diagrammen. Als onderdeel van uw [dashboardinstellingen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards" lang="nl" >}}) bevatten deze tegels verschillende typen, variërend van een tabel met informatie, lijngrafieken, staafdiagrammen en cirkeldiagrammen.

Om te beginnen [voegt u een rapporttegel toe]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="nl" >}}) aan uw standaard Uptrends-dashboards of maakt u uw set-up helemaal zelf. Klik na het toevoegen op het pictogram {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} om toegang te krijgen tot de tegelinstellingen en de configuratie aan te passen.

Dit knowledgebase-artikel leidt u door de verschillende typen rapporttegels en hun instellingen.

## Eenvoudige lijst of grafiek {id="simple-data-list-chart"}

Met dit type rapporttegel kunt u controleregels of controleregelgroepen selecteren om statistieken weer te geven uit de opties **Algemeen**, **Core Web Vitals** en **W3C Navigatie**. Deze statistieken kunnen variëren, afhankelijk van het controleregeltype en andere configuratie-instellingen.

Om de **Core Web Vitals** en **W3C Navigatiekengetallen** van uw controleregels in te schakelen, moet u ervoor zorgen dat het [browsertype]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="nl" >}}) van uw controleregel is gewijzigd in **Chrome met extra kengetallen**. Zorg ervoor dat u voor Transactiecontroleregels ook de [Prestatiekengetallen]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="nl" >}}) heeft ingeschakeld in de **Waterval**-instellingen van uw transactiestapinstellingen.

Houd er rekening mee dat de periode vóór deze wijziging geen data van **Core Web Vitals** en **W3C Navigatiekengetallen** weergeeft. U kunt de rapportageperiode aanpassen in de tegelinstellingen om alleen het bereik weer te geven waarin **Chrome met extra kengetallen** was ingeschakeld.

Na configuratie toont de Eenvoudige lijst of grafiek een grafiek die overeenkomt met de kengetallen. Controleer de legenda en hover over de grafiek voor meer informatie over de stappen. Raadpleeg het knowledgebase-artikel [Berekening van uptime en downtime]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="nl" >}}).

![Kengetallen Eenvoudige lijst of grafiek](/img/content/scr-data-metrics.min.png)  


### Algemeen

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:

- Totale tijd, resolve tijd, connectietijd en downloadtijd
- Uptimepercentage, downtime percentage, uptime en downtime
- Bevestigde en onbevestigde fouten
- Controles, alerts en totaal bytes
- SLA doel uptimepercentage, SLA doel totale tijd, SLA doel operator responstijd en operator responstijd

![Eenvoudige grafiek Algemene kengetallen](/img/content/scr_simple-data-chart.min.png)  

### Core Web Vitals

De controleregels FPC en Transactie verzamelen beide data van de [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) wanneer het browsertype is ingesteld op [Chrome met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="nl" >}}).

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:

 - First contentful paint
 - Largest contentful paint
 - Time to interactive
 - Total blocking time
 - Cumulative layout shift

![Eenvoudige grafiek Core Web Vitals-kengetallen](/img/content/scr_simple-data-chart-steps.min.png)  


### W3C Navigatie

De controleregels FPC en Transactie verzamelen beide data van de [W3C Navigatie]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}) en [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) wanneer het browsertype is ingesteld op [Chrome met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="nl" >}}).

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:
  - Request start
  - Time to first byte
  - DOM interactive
  - DOM completed
  - Load event

![Eenvoudige lijst W3C Navigatiekengetallen](/img/content/scr_simple-data-list.min.png)  


## Controleregel lijst of grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens wat u wilt weergeven:

- SLA uptimepercentage, SLA doel uptimepercentage
- SLA totale tijd, SLA doel totale tijd, SLA downtime
- SLA operator responstijd, SLA doel operator responstijd
- Totale tijd, Controles, Bevestigde fouten, Onbevestigde fouten
- Uptimepercentage, Downtimepercentage
- Sorteeropties en Regels tonen-opties
  
![screenshot tegel controleregel grafiek](/img/content/scr_monitor-data-chart.min.png)  
  
![screenshot tegel controleregel lijst](/img/content/scr_monitor-data-list.min.png)  

## Lijst van fouttypes of Fouttype grafiek  

Selecteer controleregels of controleregelgroepen en periode-opties.  
  
![screenshot fouttype lijst en grafiek](/img/content/scr_error-type-list-chart.min.png)  

## Controlestation lijst of grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies dan wat u wilt weergeven: 

- Totale tijd, Resolve tijd
- Connectietijd, Downloadtijd
- Controles, Bevestigde fouten en Sorteeropties 
  
![screenshot tegel controlestation grafiek](/img/content/scr_checkpoint-data-chart.min.png)

![screenshot tegel controlestation lijst](/img/content/scr_checkpoint-data-list.min.png)  

## Multicontrolestation lijst of/ grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens welk kengetal u in de hele lijst of grafiek wilt weergeven.  
  

![screenshot tegel multicontrolestation grafiek](/img/content/scr_multi-checkpoint-chart-tile.min.png) 
  
![screenshot tegel multicontrolestation lijst](/img/content/scr_multi-checkpoint-list-tile.min.png) 

## Multicontroleregel lijst of grafiek   

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens welk kengetal u via de lijst of grafiek wilt weergeven.  
  
![screenshot tegel multicontroleregel grafiek](/img/content/scr_multi-monitor-chart-tile.min.png)  

![screenshot tegel multicontroleregel lijst](/img/content/scr_multi-monitor-list-tile.min.png)

## Details Laatste controle {id="last-check-details"}

Geef weer wanneer een controleregel of controleregelgroepen voor het laatst zijn gecontroleerd en selecteer de periode waarover de data moeten worden weergegeven .  
![screenshot aangepaste tegels details controleregelcheck](/img/content/scr_custom-report-tiles-lastcheck.min.png)

## Controleregel log  

Selecteer controleregels of controleregelgroepen, periode en selecteer vervolgens hoe fouten moeten worden gefilterd en of het rapport moet worden opgenomen in een geëxporteerd bestand.  
  
![screenshot tegel controleregel log](/img/content/scr_monitor-log-tile.min.png) 

## Alerthistorie 

Toon de historie met alertmeldingen per controleregel of controleregelgroep en filter data op periode. 

![screenshot tegel alerthistorie](/img/content/scr_alert-history-tile.min.png)

## Lijst met staptijden of Staptijden grafiek  

Voor transactie- en Multi-step API-controleregels en slechts één controleregel tegelijk. Toont de duur van stappen in de tijd.
  
![screenshot tegel stapduur grafiek](/img/content/scr_step-duration-chart-tile.min.png)  

## Lijst met gemiddelde staptijden of Gemiddelde stapduur grafiek  

Voor transactie- en Multi-step API-controleregels en slechts één controleregel tegelijk. Toont de gemiddelde duur van stappen.
  
![screenshot tegel gemiddelde duur van stappen grafiek](/img/content/scr_average-step-duration-chart-tile.min.png)  
