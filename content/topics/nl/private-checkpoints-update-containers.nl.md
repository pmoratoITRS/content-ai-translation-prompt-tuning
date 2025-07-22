{
  "hero": {
    "title": "Een Docker-container bijwerken"
  },
  "title": "Een Docker-container bijwerken",
  "summary": "Hoe werkt het bijwerken van een controlestation van een persoonlijke locatie Docker-container?",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-controlestations-containers-bijwerken",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-update-containers"
}

Als u [een door de gebruiker beheerd controlestation installeert]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#script-content" lang="nl" >}}) wordt er een script gecreëerd en een geplande taak die de controlestationcontainer elk uur bijwerkt. Als u buiten dit schema moet bijwerken, kan een handmatige update worden uitgevoerd.

## Handmatig bijwerken

Zorg er eerst voor dat de stappen die worden uitgelegd in [Een Docker controlestation installeren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="nl" >}}) vooraf zijn uitgevoerd.

1. Open een PowerShell-console **in admin modus**. 
2. Ga naar de map waar het bestand docker-compose.yml zich bevindt en voer de volgende opdrachten uit.
3. Typ `docker-compose pull` in de opdrachtregel. 
4. Typ `docker-compose down` in de opdrachtregel. 
5. Typ `docker-compose up` in de opdrachtregel.

Tijdens het bijwerken nemen uw andere persoonlijke controlestations de controles over. Het dadelijk bijgewerkte controlestation hoeft niet te worden uitgeschakeld voor een succesvolle update. Aangezien u ten minste [één andere controlestation-instantie] ({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq#two-default-private-checkpoints" lang="nl" >}}) zou moeten hebben (nogmaals, dit wordt sterk aanbevolen) kunt u updaten zonder dat u andere wijzigingen hoeft aan te brengen, zoals het uitschakelen van controlestations, het stoppen van controleregels, enz.

{{< callout >}}
Het is belangrijk om uw Docker-containers up-to-date te houden. De containers hebben een ingebouwde Chrome- en Edge-browser die up-to-date moeten worden gehouden om geen veiligheidsrisico te worden.
Uptrends zal een waarschuwing of fout weergeven als we van mening zijn dat uw containers verouderd zijn.  
{{< /callout >}}
