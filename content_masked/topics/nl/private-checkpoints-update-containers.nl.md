{
  "hero": {
    "title": "Een Docker-container bijwerken"
  },
  "title": "Een Docker-container bijwerken",
  "summary": "Hoe werkt het bijwerken van een controlestation van een persoonlijke locatie Docker-container?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-controlestations-containers-bijwerken",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u [een door de gebruiker beheerd controlestation installeert]([LINK_URL_1]) wordt er een script gecreëerd en een geplande taak die de controlestationcontainer elk uur bijwerkt. Als u buiten dit schema moet bijwerken, kan een handmatige update worden uitgevoerd.

## Handmatig bijwerken

Zorg er eerst voor dat de stappen die worden uitgelegd in [Een Docker controlestation installeren]([LINK_URL_2]) vooraf zijn uitgevoerd.

1. Open een PowerShell-console **in admin modus**. 
2. Ga naar de map waar het bestand docker-compose.yml zich bevindt en voer de volgende opdrachten uit.
3. Typ [INLINE_CODE_1] in de opdrachtregel. 
4. Typ [INLINE_CODE_2] in de opdrachtregel. 
5. Typ [INLINE_CODE_3] in de opdrachtregel.

Tijdens het bijwerken nemen uw andere persoonlijke controlestations de controles over. Het dadelijk bijgewerkte controlestation hoeft niet te worden uitgeschakeld voor een succesvolle update. Aangezien u ten minste [één andere controlestation-instantie] ([SHORTCODE_3]) zou moeten hebben (nogmaals, dit wordt sterk aanbevolen) kunt u updaten zonder dat u andere wijzigingen hoeft aan te brengen, zoals het uitschakelen van controlestations, het stoppen van controleregels, enz.

[SHORTCODE_1]
Het is belangrijk om uw Docker-containers up-to-date te houden. De containers hebben een ingebouwde Chrome- en Edge-browser die up-to-date moeten worden gehouden om geen veiligheidsrisico te worden.
Uptrends zal een waarschuwing of fout weergeven als we van mening zijn dat uw containers verouderd zijn.  
[SHORTCODE_2]
