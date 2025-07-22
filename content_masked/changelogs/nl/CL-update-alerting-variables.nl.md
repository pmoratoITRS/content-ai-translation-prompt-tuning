{
  "title": "Introductie nieuwe alertingvariabelen",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]februari-2025-alertvariabele-updates",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De volgende alertingvariabelen zijn nu beschikbaar voor gebruik:

- **@alert.numberOfConsecutiveErrors** – bevat het totale aantal opeenvolgende fouten (bevestigde fouten) van de alert. Dit retourneert [INLINE_CODE_1] wanneer de API-respons [INLINE_CODE_2] is.
- **@alert.checkpointName** – bevat de naam of locatie van het controlestation waar de alert voor het laatst is gecontroleerd. Deze retourneert [INLINE_CODE_3] wanneer de API-respons [INLINE_CODE_4] is.
- **@alert.responseHeaders** – bevat de responsheaders van de alert in sleutel-waardeparen. Deze retourneert bijvoorbeeld [INLINE_CODE_5] vanuit de API-responsheader, vergelijkbaar met hoe de waarden worden geretourneerd voor [INLINE_CODE_6].

Merk op dat de waarde van de [INLINE_CODE_7] leeg kan zijn als [Gegevensbescherming persoonlijke locatie]([LINK_URL_1]) is ingeschakeld op een persoonlijke controlestationlocatie die de alertcheck uitvoert. Zie [Systeemvariabelen voor alerting]([LINK_URL_2]) voor meer informatie.