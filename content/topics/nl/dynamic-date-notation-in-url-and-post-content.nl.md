{
  "hero": {
    "title": "Dynamische waarden in URL’s en POST-inhoud"
  },
  "title": "Dynamische waarden in URL’s en POST-inhoud",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/dynamische-waarden-in-url-en-post-inhoud",
  "summary":"Uitleg over het opnemen van dynamische waarden in URL's of request bodies.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/dynamic-values-in-url-and-post-content"
}

## Dynamische waarde in URL of request body

Uptrends kan [dynamische datumwaarden]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables#date-and-time" lang="nl" >}}) genereren in URL's of inhoud van HTTP requests, voor de meeste controleregeltypes. Tijdstempels worden vaak gebruikt omdat het niet alleen unieke waarden zijn, ze bevatten ook informatie over wanneer de request werd uitgevoerd. Dit kan handig zijn voor webservices waarbij een andere waarde moet worden ingevoerd als onderdeel van de request body voor een HTTP POST of de request-URL, bijvoorbeeld:

`... <StartDate>2023-02-27</StartDate> ...`

In plaats van een datum met vaste waarde in te voeren, kunnen we de volgende notatie gebruiken om waarden te genereren op basis van de datum/tijd van vandaag:

`... <StartDate>{{@DateTime(dd-MM-yyyy)}}</StartDate> ...`

Let wel, **andere formaat-waarden zijn ook mogelijk**. Bovendien kunnen we offsets gebruiken om andere waarden te berekenen. U vindt meer informatie over de notatie en hoe u offsets op uw datumwaarden toepast in ons artikel over [automatische variabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}).


## Cache busting

**Content caching** kan ongelofelijk nuttig zijn voor elke webmaster, omdat het de algehele performance kan verbeteren door in de loop van de tijd minder resources te gebruiken. Maar als u een website of service monitort, kan het door caching lastig zijn om te weten of een van uw pagina-elementen werkelijk up of down is.

Door een willekeurige URL-waarde in te voegen, kunt u de cache verversen (busten) van elke *HTTP-*, *Webservice-* of *Full Page Check-*aanroep en ervoor zorgen dat er geen eerdere inhoud in de cache wordt opgeslagen.

{{< callout >}}
**Opmerking:** De volgende informatie gaat over server side caching aan uw kant, niet aan de kant van Uptrends' website monitoring service.
{{< /callout >}}

### Hoe werkt cache busting?

Cache busting wordt mogelijk gemaakt door de token `{{@RandomGuid}}` te gebruiken (zie ons [Knowledge Base-artikel over automatische variabelen voor meer informatie)]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables#random-unique-identifier" lang="nl" >}}). Om deze functie te gebruiken voert u de token gewoon in als onderdeel van de URL bij de controleregelinstellingen, bijvoorbeeld:

`http://www.example.com?myvalue={{@RandomGuid}}`

Die wordt opgelost als iets van:

`http://www.example.com?myvalue=37f1f109-58a2-4bea-adfb-9aed54619453`
