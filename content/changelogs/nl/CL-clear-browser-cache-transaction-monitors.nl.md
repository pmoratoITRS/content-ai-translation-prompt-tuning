{
  "title": "Introductie van Clear browser cache in transactiecontroleregels",
  "date": "2025-01-29",
  "url": "/changelog/januari-2025-clear-browser-cache-transactiecontroleregels",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-clear-browser-cache-transaction-monitors"
}

Uptrends [transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}) openen altijd een echte browser om gebruikersactiviteiten te simuleren om de prestaties van uw website te controleren. De browser start zonder data in de cache en slaat later cache op om tijdelijk websitebronnen op te slaan om het laadproces te versnellen.

Als u het gedrag van uw e-commercesite wilt vergelijken bij het laden van items in de winkelwagen voor bestaande gebruikers (met gecachete data) vergeleken met nieuwe bezoekers (zonder gecachete data), kan het wissen van de cache van de browser helpen.

Met de nieuwe stapactie **Browser cache legen** in transactiecontroleregels kunt u nu de cache van de browser leegmaken om pagina-elementen rechtstreeks vanaf de server opnieuw te laden in plaats vanuit de cache. Deze functie helpt u de prestaties van het eerste bezoek aan de website te controleren en garandeert dat UI-weergaven (zoals afbeeldingen, tekst en andere front-end-elementen) correct worden geladen. Deze stapactie kost geen transactiecredits, gebruik deze om uw monitoringbehoeften te verbeteren. Raadpleeg voor meer informatie de [Transactiestapeditor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}).

![Browser cache legen GIF](/img/content/gif-transaction-clear-browser-cache.gif)