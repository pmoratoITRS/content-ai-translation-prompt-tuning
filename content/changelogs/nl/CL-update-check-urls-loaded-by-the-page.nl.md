{
  "title": "Extra condities voor Controleer de URL's die door de pagina worden ingeladen",
  "date": "2025-02-19",
  "url": "/changelog/februari-2025-extra-condities-controleer-urls-ingeladen-door-de-pagina-foutconditie",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition"
}

De conditie [Controleer de URL's die door de pagina worden ingeladen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="nl" >}}) is een foutconditie die controleert of specifieke pagina-elementen op uw website worden geladen. Deze pagina-elementen zijn de URL's die worden weergegeven in uw [Watervalgrafiek]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}), waaronder afbeeldingen, bestanden en andere websiteresources.

Met deze foutconditie kunt u nu extra criteria instellen voor het controleren van de statistieken van elk pagina-element. Door op de nieuwe knop {{< AppElement type="editbutton" >}} +Extra conditie toevoegen{{< /AppElement >}} te klikken, kunt u nu de responsgrootte van het pagina-element in bytes (B), de totale tijd in milliseconden (ms) en de statuscode opgeven:

![Extra condities voor Controleer de URL's die door de pagina worden ingeladen](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

Als u fouten wilt krijgen wanneer uw afbeelding langer dan 2 seconden laadt of als een bestand resulteert in een statuscode hoger dan 400, kunt u specifieke criteria voor elk toevoegen.

De conditie Controleer de URL's die door de pagina worden ingeladen, is beschikbaar voor [Browser- of Full Page Check-controleregels]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="nl" >}}) en [Transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}). Let op: bij transactiecontroleregels moet u de [optie Waterval in een stap]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="nl" >}}) selecteren om de aanvullende condities in te stellen.