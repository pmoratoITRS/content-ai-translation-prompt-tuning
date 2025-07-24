{
  "hero": {
    "title": "Gegevensbescherming persoonlijke locatie"
  },
  "title": "Gegevensbescherming persoonlijke locatie",
  "summary": "Wat zijn de maatregelen voor gegevensbescherming op persoonlijke locaties?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-locaties-gegevensbescherming",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In dit knowledgebase-artikel vindt u uitleg over het implementeren van gegevensbescherming op uw persoonlijke locaties. Eén van de maatregelen die zijn geïmplementeerd in Uptrends’ persoonlijke locaties is het voorkomen dat snapshots worden geüpload naar de cloud. U kunt ook pagina-inhoud uitschakelen, HTTP request en response headers en resolved IP-adressen verbergen in details van de controle.

## Het Docker Compose-bestand bewerken

Installeer eerst uw controlestation, als u dat nog niet heeft gedaan, door de stappen te volgen die worden uitgelegd in [Een Docker-controlestation installeren]([LINK_URL_1]).

1. Maak een back-up van het uitgepakte Docker Compose-bestand. Houd er rekening mee dat als u wijzigingen aanbrengt in het verstrekte composebestand, dit op eigen risico is. Neem contact op met [Support]([LINK_URL_2]) als u twijfelt. 
2. Open het bestand docker-compose.yml en verwijder de comment-tag `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]- AllowScreenshotsInResults=false[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]- AllowPageContentInResults=false[INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10]- AllowHttpHeadersInResults=false[INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13]- AllowResolvedIpAddressesInResults=false[INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16]- AllowResolvedIpAddressesInResults=false` in de lijst met Checkpoint environment variabelen. Sla het bestand op en start de Docker-container handmatig opnieuw op, zoals beschreven in de laatste stap van de bewerkingsinstructies hierboven, om de wijzigingen in de gegevensbeschermingsinstellingen in de Uptrends-app weer te geven.

Als deze waarde is ingesteld op 'false' wordt het uitvoeren van DNS-controleregels geblokkeerd op controlestationservers op uw persoonlijke locatie.

[SHORTCODE_3] **Let op**: Niet alle instellingen dekken elk controleregeltype, voor eenvoudige HTTP(S)-controleregels bijvoorbeeld werken alleen foutscreenshots; de resolved IP-instellingen zijn niet van toepassing op dit type controleregel. 
[SHORTCODE_4]

## Status van gegevensbeschermingsinstellingen 

Het tabblad [Controlestationstatus]([LINK_URL_9]) in de Uptrends-app toont de status van de gegevensbeschermingsinstellingen. Een rood kruis betekent dat gegevens niet worden weergegeven, dus dat gegevensbescherming is ingeschakeld. Houd er rekening mee dat dit een alleen-lezen weergave is, de instellingen kunnen alleen in het Docker-bestand worden aangepast. 

![Instellingen voor gegevensbescherming op het tabblad Controlestationstatus]([LINK_URL_10])