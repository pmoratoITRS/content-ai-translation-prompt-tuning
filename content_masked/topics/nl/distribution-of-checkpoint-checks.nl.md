{
  "hero": {
    "title": "Distributie van controlestationchecks"
  },
  "title": "Distributie van controlestationchecks",
  "summary": "Hoe werkt het Uptrends controlestationsysteem?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/distributie-van-controlestationchecks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends heeft een van de grootste server- en [website monitoring controlestationnetwerken]([LINK_URL_1]) in de branche. Het is nog nooit zo eenvoudig geweest uw websites, servers en webservices te monitoren vanaf een verscheidenheid aan locaties over de hele wereld.

**Maar hoe werkt Uptrends' controlestationsysteem?**

## Controlestation-algoritme

Wanneer u een controleregel toevoegt voor tracking, kunt u een reeks controlestations kiezen uit ons mondiale monitoring netwerk om van daaruit uw servicestatus te controleren.

De controles die worden uitgevoerd selecteren een willekeurig controlestation, en selecteren nooit twee keer achter elkaar hetzelfde controlestation.

In het geval van een onbevestigde fout voert de Uptrends-service een tweede controle op downtime uit via een ander controlestation om te controleren of het inderdaad om een fout gaat.

- Wanneer dat controlestation ook een fout rapporteert, is de fout bevestigd en wordt deze als zodanig vermeld in de [SHORTCODE_1]Controleregel log[SHORTCODE_2].
- Rapporteert dat controlestation geen fout, dan wordt verondersteld dat de downtime tijdelijk was.

## Ondersteuning voor round-robin (monitoringchecks uitgevoerd door controlestations in een vaste volgorde)

Uptrends ondersteunt geen 'round robin'-optie.
