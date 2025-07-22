{
  "hero": {
    "title": "Dynamische waarden in URL’s en POST-inhoud"
  },
  "title": "Dynamische waarden in URL’s en POST-inhoud",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/dynamische-waarden-in-url-en-post-inhoud",
  "summary": "Uitleg over het opnemen van dynamische waarden in URL's of request bodies.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Dynamische waarde in URL of request body

Uptrends kan [dynamische datumwaarden]([LINK_URL_1]) genereren in URL's of inhoud van HTTP requests, voor de meeste controleregeltypes. Tijdstempels worden vaak gebruikt omdat het niet alleen unieke waarden zijn, ze bevatten ook informatie over wanneer de request werd uitgevoerd. Dit kan handig zijn voor webservices waarbij een andere waarde moet worden ingevoerd als onderdeel van de request body voor een HTTP POST of de request-URL, bijvoorbeeld:

[INLINE_CODE_1]

In plaats van een datum met vaste waarde in te voeren, kunnen we de volgende notatie gebruiken om waarden te genereren op basis van de datum/tijd van vandaag:

[INLINE_CODE_2]

Let wel, **andere formaat-waarden zijn ook mogelijk**. Bovendien kunnen we offsets gebruiken om andere waarden te berekenen. U vindt meer informatie over de notatie en hoe u offsets op uw datumwaarden toepast in ons artikel over [automatische variabelen]([LINK_URL_2]).


## Cache busting

**Content caching** kan ongelofelijk nuttig zijn voor elke webmaster, omdat het de algehele performance kan verbeteren door in de loop van de tijd minder resources te gebruiken. Maar als u een website of service monitort, kan het door caching lastig zijn om te weten of een van uw pagina-elementen werkelijk up of down is.

Door een willekeurige URL-waarde in te voegen, kunt u de cache verversen (busten) van elke *HTTP-*, *Webservice-* of *Full Page Check-*aanroep en ervoor zorgen dat er geen eerdere inhoud in de cache wordt opgeslagen.

[SHORTCODE_1]
**Opmerking:** De volgende informatie gaat over server side caching aan uw kant, niet aan de kant van Uptrends' website monitoring service.
[SHORTCODE_2]

### Hoe werkt cache busting?

Cache busting wordt mogelijk gemaakt door de token [INLINE_CODE_3] te gebruiken (zie ons [Knowledge Base-artikel over automatische variabelen voor meer informatie)]([LINK_URL_3]). Om deze functie te gebruiken voert u de token gewoon in als onderdeel van de URL bij de controleregelinstellingen, bijvoorbeeld:

[INLINE_CODE_4]

Die wordt opgelost als iets van:

[INLINE_CODE_5]
