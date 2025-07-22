{
  "title": "Introductie nieuwe alertingvariabelen",
  "date": "2025-02-19",
  "url": "/changelog/februari-2025-alertvariabele-updates",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-alert-variable-updates"
}

De volgende alertingvariabelen zijn nu beschikbaar voor gebruik:

- **@alert.numberOfConsecutiveErrors** – bevat het totale aantal opeenvolgende fouten (bevestigde fouten) van de alert. Dit retourneert `2` wanneer de API-respons `{"numberOfConsecutiveErrors": "2"}` is.
- **@alert.checkpointName** – bevat de naam of locatie van het controlestation waar de alert voor het laatst is gecontroleerd. Deze retourneert `Ghent, Belgium` wanneer de API-respons `{"checkpointName": "Ghent, Belgium"}` is.
- **@alert.responseHeaders** – bevat de responsheaders van de alert in sleutel-waardeparen. Deze retourneert bijvoorbeeld `{"Content-Type": "text/html"}` vanuit de API-responsheader, vergelijkbaar met hoe de waarden worden geretourneerd voor `@alert.responseBody`.

Merk op dat de waarde van de `@alert.responseHeaders` leeg kan zijn als [Gegevensbescherming persoonlijke locatie]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}) is ingeschakeld op een persoonlijke controlestationlocatie die de alertcheck uitvoert. Zie [Systeemvariabelen voor alerting]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="nl" >}}) voor meer informatie.