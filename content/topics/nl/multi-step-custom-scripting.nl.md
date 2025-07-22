{
  "hero": {
    "title": "Multi-step API aangepaste scripting"
  },
  "title": "Multi-step API aangepaste scripting",
  "summary":"Een overzicht van de Aangepaste scripting-opties in Multi-step API monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-aangepaste-scripting",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-custom-scripting"
}

De Multi-step API (MSA)-controleregel beschikt over krachtige [ingebouwde functies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) die een gebruiksvriendelijke en no-code-oplossing bieden om het gedrag van uw API's te testen.

Hoewel u met een no-code-benadering een heel eind komt bij het bouwen van goede monitoring-setups, heeft u mogelijk een scripttaal nodig om diepgaande functionele tests uit te voeren en volledig te beschrijven wat u van uw API's verwacht. Bijvoorbeeld het toevoegen van een aangepaste logica of het verwerken van geavanceerder gedrag die niet kunnen worden bereikt in een UI-gebaseerde setup alleen.

Met de MSA-controleregel kunt u zowel klassieke no-code-functies als aangepaste scripting verwerken. U kunt ingebouwde UI functies gebruiken samen met hun scripting-tegenhangers. U hoeft uw controleregels niet helemaal opnieuw te maken als u bestaande API controleregels heeft en aangepaste scripting wilt toevoegen. Begin gewoon met het toevoegen van een aantal scripts en laat ze werken naast uw bestaande setup.

## Pre-Request- en Post-Response-scripts

Een API-controleregel bestaat uit één of meerdere stappen die in een reeks worden uitgevoerd. Voor elke MSA-stap (behalve Wacht-stappen) zijn twee scripteditors beschikbaar: de tabbladen {{< AppElement type="tab" >}} Pre-Request {{< /AppElement >}} en {{< AppElement type="tab" >}} Post-Response {{< /AppElement >}}:

- Met de **Pre-Request script**-editor kunt u scripts schrijven ter voorbereiding op het verzenden van een HTTP request. Dit is handig voor het voorbereiden en berekenen van waarden die u in de request wilt opnemen, zoals omgevingsvariabelen, URL-parameters, request headers of content body. Het script dat in deze editor is geschreven, wordt uitgevoerd *voordat* de API request naar de server wordt verzonden.

- Met de **Post-Response script**-editor kunt u scripts schrijven om de HTTP response die van de API terugkomt te verifiëren en te verwerken. Dit is handig voor het schrijven van aangepaste logica om response headers te controleren, de volledigheid en consistentie van uw content te valideren en die contentdata te gebruiken om voor te bereiden op volgende stappen. Het script dat in deze editor is geschreven, wordt alleen uitgevoerd *nadat* de API response succesvol is ontvangen van de server. Als er een verbindingsfout optreedt, wordt het script niet uitgevoerd en worden assertions of variabelen in het tabblad {{< AppElement type="tab" >}} Response {{< /AppElement >}} niet gevalideerd.

Deze editors bevatten ook de volgende functies:
![Tabbladen Aangepaste scripting](/img/content/API-monitoring-custom-scripting-editors-min.png)

- Regelnummering — geeft numerieke waarden weer die de scripts of codes per regel identificeren.
- Codemarkering — geeft codes weer in een kleurgecodeerd formaat om syntaxisfouten en trefwoorden eenvoudig te identificeren.
- Codeaanvulling — stelt automatisch mogelijke codecombinaties voor om het schrijven van scripts te ondersteunen.
- Snippets-paneel — biedt een lijst met nuttige codefragmenten die u automatisch kunt invoegen in uw code-editor nadat u ze heeft geselecteerd.

## Snippets

Met de **Pre-Request**- en **Post-Response**-editors kunt u scripts invoegen en uitvoeren die zijn geschreven in JavaScript. Naast het volledige scala aan mogelijkheden dat standaard Javascript biedt, kunt u ook **Snippets** gebruiken.

**Snippets** zijn speciale functies waarmee u toegang krijgt tot data van HTTP requests (tijdens het Pre-Request-proces) en HTTP responses (tijdens het Post-Response-proces). U kunt er ook log statements mee uitvoeren, berekende data opslaan als [Custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="nl" >}}) en tests uitvoeren op stapdata. Deze speciale functies zijn toegankelijk via een uniek object genaamd `ut`.

## Algemene of basis ut-objecten

In deze sectie is de lijst met algemene `ut`-objecten als volgt

- `ut.request` geeft toegang tot het API request object.
- `ut.response` geeft toegang tot het API response object.
- `ut.variables` is de verzameling variabelen die u in alle API-stappen kunt gebruiken. Gebruik deze om waarden van de ene stap naar de volgende door te geven. Alle [Voorgedefinieerde variabelen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}) of variabelen die u gebruikt in het tabblad {{< AppElement type="tab" >}} Response {{< /AppElement >}} worden opgenomen in deze objectverzameling.
- `ut.log()` is een helperfunctie die de opgegeven logs naar de console log stuurt. Logt wanneer de pre-request scripts worden uitgevoerd, zijn te vinden in het **Pre-Request script Console log**, terwijl logs voor post-response scripts zijn te vinden in het **Post-response script Console log**.
- `ut.test()` is de hoofdfunctie voor het vastleggen van testuitvoer. Alle testuitvoer die u definieert binnen elke `ut.test()`-call, wordt vastgelegd en vermeld als een **Assertions**-resultaat, samen met de assertions die u definieert op het tabblad {{< AppElement type="tab" >}} Response {{< /AppElement >}} van elke stap.
- `ut.customMetrics` is een verzameling numerieke waarden rechtstreeks uit een API response. U kunt uw eigen aangepaste metrische variabele definiëren om waarden op te slaan of te berekenen uit een API response. Deze waarde wordt weergegeven in de details van de monitorcontrole voor elke meting en kan ook worden vermeld en in kaart worden gebracht in dashboards.
- Met `ut.crypto` kunt u MD5- en SHA-hashes genereren voor veilige dataverwerking en -overdracht. Het kan ook worden gebruikt om certificaatintrekkingslijsten (Certificate Revocation Lists, CRL's) te parseren.

U bent nu bekend met de algemene `ut`-basisobjecten. In deze sectie worden de kenmerken van elk `ut`-object gedetailleerd besproken.

### Request

Attributes van `ut.request`:

- `.url` — de URL van de request ophalen of instellen
- `.method` — de HTTP-methode van de request ophalen of instellen (zoals GET en POST)
- `.body` — een onbewerkte tekstversie van de request body ophalen of instellen

### Request headers

Functies van `ut.request.headers`:

- `.has(header, value)` — retourneert of de header bestaat en een specifieke waarde heeft
- `.get(header)`— retourneert de waarde van de header. Retourneert een lege string als de header niet bestaat
- `.add(header, value)` — creëert een nieuwe header met de opgegeven `value` (alleen als de header nog niet was ingesteld)
- `.upsert(header, value)` — voegt de header in met de opgegeven `value` (als de header nog niet bestaat) of werkt de header bij met de opgegeven waarde (als de header al bestaat)
- `.remove(header)` — verwijdert de header

### Response

Attributes van `ut.response`:

- `.code` — haalt de numerieke HTTP response-statuscode op (zoals 200, 404, 500)
- `.status`  — haalt de HTTP statusbeschrijving op (zoals OK)
- `.responseSize` — haalt de omvang van de response op in bytes
- `.bytes` — retourneert een byte-array met de response body. Responses zijn beperkt tot 100 MB

Functies van `ut.response`:

- `.text()` — retourneert een onbewerkte tekstversie van de response body
- `.json()` — retourneert een object door de responsetekst te parseren als JSON

### Response headers

Functies van `ut.response.headers`:

- `.has(header)` — retourneert of de header bestaat
- `.get(header)` — retourneert de waarde van de header. Retourneert een lege string als de header niet bestaat

### Variabelen

Functies van `ut.variables`:

- `.has(key)` — retourneert of de variabele bestaat
- `.get(key)` — retourneert de waarde van de variabele. Retourneert een lege string als de variabele niet bestaat
- `.set(key, value)` — creëert de variabele (als deze niet bestaat) en slaat de opgegeven `value` op in de variabele `key`

### Custom metrics

Functies van `ut.customMetrics`:

- `.get(key)` — retourneert de waarde van de custom metric variabele. Retourneert een lege string als de custom metric niet bestaat
- `.set(key, value)` — slaat de opgegeven `value` op in de custom metric variabele `key`

Raadpleeg voor meer informatie de knowledgebase-artikelen [Vrije kengetallen instellen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="nl" >}}) en [Variabelen bij Multi-step monitoring]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}) knowledge base articles.

### Test of Assert

Uptrends ondersteunt de Expect- en Should-interfaces van Chai JS, zie [Chai - Should](https://www.chaijs.com/guide/styles/#should "https://www.chaijs.com/guide/styles/#should") en [Chai - Expect](https://www.chaijs.com/guide/styles/#expect "https://www.chaijs.com/guide/styles/#expect") om te lezen hoe u verschillende waardetests en vergelijkingen kunt uitdrukken:

- `ut.expect(value)` + verschillende expressies
- `ut.should(value)` + verschillende expressies  

Alle `.expect()` en `.should()` expressies zullen (als ze op zichzelf worden gebruikt) een fout genereren als niet aan de gewenste criteria wordt voldaan en zullen de uitvoering van de controleregel stoppen. Alle aanvullende assertions die in de rest van het script zijn gedefinieerd zullen niet worden uitgevoerd.

Gebruik `ut.test()` om de volledige set assertions uit te voeren, ongeacht of een van de eerdere assertions mislukt:

- `ut.test(descriptionText, testFunction)` — de uitvoer (succes of mislukking) van een `.expect` of `.should` die is gedefinieerd in de gespecificeerde testFunction, komt terecht in de assertions-uitvoer van de controleregel. Bovendien zorgt `ut.test()` ervoor dat de uitvoering van het script niet wordt stopgezet wanneer een assertion mislukt.

## Hashing

Functies van `ut.crypto`:

- `.md5(value)` — genereert een MD5-hash van de gespecificeerde waarde
- `.sha1(value)` — genereert een SHA-1-hash van de gespecificeerde waarde
- `.sha256(value)` — genereert een SHA-256-hash van de gespecificeerde waarde
- `.sha512(value)` — genereert een SHA-512-hash van de gespecificeerde waarde

Met de scriptingmethodes voor het genereren van MD5- en SHA-hashes kunt u waarden veilig opslaan en verzenden, waardoor gegevensbescherming door hashing wordt gewaarborgd. 

Voorbeeld:

```js
var hashedMD5value = ut.crypto.md5("value here");
var hashedSHA1value = ut.crypto.sha1("value here");
```

- `.cert.parseCrl(bytes)` — parseert een certificaatintrekkingslijst (Certificate Revocation List, CRL) en retourneert de metadata ervan. Een CRL-bestand moet als invoer worden verstrekt aan de functie `.cert.parseCrl(bytes)`. Als u bijvoorbeeld het veld `NextUpdate` wilt lezen uit een CRL-bestand of CRL-URL, kunt u de functie als volgt gebruiken:

```js
  var crl = ut.crypto.cert.parseCrl(ut.response.bytes);
  var crlNextUpdate = new Date(crl.NextUpdate);
  ut.log(ut.crypto.cert.parseCrl(ut.response.bytes));

  // Assert the value of a variable
  ut.test("Variable {variable} should equal {value}", () => {
    expect(crlNextUpdate).at.least(new Date(2026, 1, 1));
  });
```