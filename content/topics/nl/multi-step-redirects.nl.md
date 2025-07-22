{
  "hero": {
    "title": "Multi-step monitoring - Redirects verwerken"
  },
  "title": "Multi-step monitoring",
  "summary": "Leer hoe u met redirects werkt binnen uw Multi-step API-controleregels.",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-redirects"
}

Met HTTP redirects kan een webserver de caller (de HTTP-client) doorsturen naar een andere URL dan oorspronkelijk was aangevraagd. Dit gebeurt door een statuscode in het 3xx-bereik te retourneren, samen met de nieuwe URL die door de client moet worden aangeroepen. Deze nieuwe URL wordt geretourneerd in de HTTP Response header met de naam Location.

Oorspronkelijke request en response:

`GET /p/P12345 HTTP/1.1` `HTTP/1.1 302 Redirect  Location: /ProductInfo?productId=P12345`

Request naar de nieuwe locatie:

`GET /ProductInfo?productId=P12345 HTTP/1.1` `HTTP/1.1 200 OK`

## Redirects controleren in een multi-step controleregel

In een [multi-step API-controleregel]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}) worden redirects zoals deze automatisch gevolgd. U hoeft zich geen zorgen te maken over de manier waarop uw API of webapplicatie inkomende requests verwerkt: u kunt zich concentreren op het controleren van het resultaat. Dit betekent dat als een stap om een URL vraagt die wordt omgeleid door uw server, we de tweede request als onderdeel van diezelfde stap zullen uitvoeren, en u kunt met het resultaat van de tweede request werken alsof er geen redirect in het midden was. Als de tweede request ook een redirect retourneert, volgen we die ook, tot een maximum van 50 opeenvolgende redirects. In elk geval krijgt u de response content en -headers die overeenkomen met de laatste request.

In sommige gevallen is dit automatische gedrag van het volgen van redirects mogelijk niet wat u nodig heeft. Als u bijvoorbeeld het redirectgedrag zelf wilt controleren (controle van de statuscode, de content van de Location Header, of een cookie wordt geretourneerd of enige andere waarde), wilt u over die waarden beschikken in plaats van meteen het tweede verzoek uit te voeren.

Als u een assertion toevoegt en specificeert dat de HTTP-responsecode gelijk is aan 301, 302, 303, 307 of 308, zullen we die redirect niet volgen. In plaats daarvan krijgt u direct toegang tot die response. U kunt vervolgens in dezelfde stap extra assertions en variabelen gebruiken om met die response te werken. Bijvoorbeeld:

### Assertions

{{< Code/Symbol type="source" >}}Status code{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}302{{< /Code/Symbol >}} 

{{< Code/Symbol type="source" >}}Response header{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Location{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Contains{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}productId=P12345{{< /Code/Symbol >}} 

![MSA redirect](/img/content/scr-MSA-redirect-check.min.png)

## De redirect handmatig volgen

Omdat we in een opstelling met meerdere stappen werken, kunnen we nog steeds doorgaan en de redirect handmatig uitvoeren nadat de redirect is gecontroleerd en optioneel waarden ervan zijn vastgelegd. Voeg gewoon een nieuwe stap toe en specificeer de nieuwe locatie als de URL.

Om dit te doen kunt u de waarde van de Location header vastleggen, opslaan in een variabele (bijvoorbeeld, {{< Code/Symbol type="variable" >}}{{location-value}}{{< /Code/Symbol >}}) en deze variabele gebruiken in de URL van de volgende stap. Dit kan echter lastig zijn: de waarde van de Location header is waarschijnlijk een relatieve URL, d.w.z. zonder een domeinnaam erin. Als u dit handmatig instelt, moet u dit compenseren door de domeinnaam op te nemen in de nieuwe URL:

`GET https://myapi.example.com/{{location-value}}`

Dit werkt wel, maar we kunnen het u gemakkelijker maken: wanneer we een Location header in een HTTP response detecteren, zullen we die waarde converteren naar een absolute URL (inclusief de domeinnaam van de oorspronkelijke request) en deze in een automatische variabele zetten, genaamd {{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}}. Deze variabele is klaar om in de volgende stap te worden gebruikt:

`GET {{@RedirectUrl}}`

## Parameters vastleggen van een redirect-URL

In sommige scenario's wilt u de redirect-URL mogelijk helemaal niet volgen, maar in plaats daarvan een parameterwaarde ervan vastleggen. Stel dat we in de oorspronkelijke response deze response header hebben ontvangen:

`Location: https://your.clientapp.com/auth?clientId=12345&code=SGV5LCB5b3UgZm91bmQgdGhpcyEgV2VsbCBkb25lIQ==`

Wat als u deze URL niet echt wilt volgen, maar die codeparameterwaarde wilt gebruiken die door uw server werd geretourneerd? Geen probleem: we leggen automatisch URL-parameters vast die we aantreffen in Location headers, en we zetten ze in automatische variabelen die u ergens anders kunt gebruiken. Het naamgevingsschema voor deze automatische variabelen is {{< Code/Symbol type="variable" >}}{{@RedirectUrl.&lt;parameter-name&gt;}}{{< /Code/Symbol >}}. In dit voorbeeld heeft u toegang tot {{< Code/Symbol type="variable" >}}{{@RedirectUrl.clientId}}{{< /Code/Symbol >}} en {{< Code/Symbol type="variable" >}}{{@RedirectUrl.code}}{{< /Code/Symbol >}}.
