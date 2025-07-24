{
  "hero": {
    "title": "Multi-step monitoring - Redirects verwerken"
  },
  "title": "Multi-step monitoring",
  "summary": "Leer hoe u met redirects werkt binnen uw Multi-step API-controleregels.",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met HTTP redirects kan een webserver de caller (de HTTP-client) doorsturen naar een andere URL dan oorspronkelijk was aangevraagd. Dit gebeurt door een statuscode in het 3xx-bereik te retourneren, samen met de nieuwe URL die door de client moet worden aangeroepen. Deze nieuwe URL wordt geretourneerd in de HTTP Response header met de naam Location.

Oorspronkelijke request en response:

[INLINE_CODE_1] [INLINE_CODE_2]

Request naar de nieuwe locatie:

[INLINE_CODE_3] [INLINE_CODE_4]

## Redirects controleren in een multi-step controleregel

In een [multi-step API-controleregel]([LINK_URL_1]) worden redirects zoals deze automatisch gevolgd. U hoeft zich geen zorgen te maken over de manier waarop uw API of webapplicatie inkomende requests verwerkt: u kunt zich concentreren op het controleren van het resultaat. Dit betekent dat als een stap om een URL vraagt die wordt omgeleid door uw server, we de tweede request als onderdeel van diezelfde stap zullen uitvoeren, en u kunt met het resultaat van de tweede request werken alsof er geen redirect in het midden was. Als de tweede request ook een redirect retourneert, volgen we die ook, tot een maximum van 50 opeenvolgende redirects. In elk geval krijgt u de response content en -headers die overeenkomen met de laatste request.

In sommige gevallen is dit automatische gedrag van het volgen van redirects mogelijk niet wat u nodig heeft. Als u bijvoorbeeld het redirectgedrag zelf wilt controleren (controle van de statuscode, de content van de Location Header, of een cookie wordt geretourneerd of enige andere waarde), wilt u over die waarden beschikken in plaats van meteen het tweede verzoek uit te voeren.

Als u een assertion toevoegt en specificeert dat de HTTP-responsecode gelijk is aan 301, 302, 303, 307 of 308, zullen we die redirect niet volgen. In plaats daarvan krijgt u direct toegang tot die response. U kunt vervolgens in dezelfde stap extra assertions en variabelen gebruiken om met die response te werken. Bijvoorbeeld:

### Assertions

[SHORTCODE_1]Status code[SHORTCODE_2] [SHORTCODE_3]Is equal to[SHORTCODE_4] [SHORTCODE_5]302[SHORTCODE_6] 

[SHORTCODE_7]Response header[SHORTCODE_8] [SHORTCODE_9]Location[SHORTCODE_10] [SHORTCODE_11]Contains[SHORTCODE_12] [SHORTCODE_13]productId=P12345[SHORTCODE_14] 

![MSA redirect]([LINK_URL_2])

## De redirect handmatig volgen

Omdat we in een opstelling met meerdere stappen werken, kunnen we nog steeds doorgaan en de redirect handmatig uitvoeren nadat de redirect is gecontroleerd en optioneel waarden ervan zijn vastgelegd. Voeg gewoon een nieuwe stap toe en specificeer de nieuwe locatie als de URL.

Om dit te doen kunt u de waarde van de Location header vastleggen, opslaan in een variabele (bijvoorbeeld, [SHORTCODE_15]{{location-value}}[SHORTCODE_16]) en deze variabele gebruiken in de URL van de volgende stap. Dit kan echter lastig zijn: de waarde van de Location header is waarschijnlijk een relatieve URL, d.w.z. zonder een domeinnaam erin. Als u dit handmatig instelt, moet u dit compenseren door de domeinnaam op te nemen in de nieuwe URL:

[INLINE_CODE_5]

Dit werkt wel, maar we kunnen het u gemakkelijker maken: wanneer we een Location header in een HTTP response detecteren, zullen we die waarde converteren naar een absolute URL (inclusief de domeinnaam van de oorspronkelijke request) en deze in een automatische variabele zetten, genaamd [SHORTCODE_17][SYSTEM_VAR_1][SHORTCODE_18]. Deze variabele is klaar om in de volgende stap te worden gebruikt:

[INLINE_CODE_6]

## Parameters vastleggen van een redirect-URL

In sommige scenario's wilt u de redirect-URL mogelijk helemaal niet volgen, maar in plaats daarvan een parameterwaarde ervan vastleggen. Stel dat we in de oorspronkelijke response deze response header hebben ontvangen:

[INLINE_CODE_7]

Wat als u deze URL niet echt wilt volgen, maar die codeparameterwaarde wilt gebruiken die door uw server werd geretourneerd? Geen probleem: we leggen automatisch URL-parameters vast die we aantreffen in Location headers, en we zetten ze in automatische variabelen die u ergens anders kunt gebruiken. Het naamgevingsschema voor deze automatische variabelen is [SHORTCODE_19][SYSTEM_VAR_3][SHORTCODE_20]. In dit voorbeeld heeft u toegang tot [SHORTCODE_21][SYSTEM_VAR_4][SHORTCODE_22] en [SHORTCODE_23][SYSTEM_VAR_5][SHORTCODE_24].
