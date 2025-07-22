{
  "hero": {
    "title": "Multi-step API aangepaste scripting"
  },
  "title": "Multi-step API aangepaste scripting",
  "summary": "Een overzicht van de Aangepaste scripting-opties in Multi-step API monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-aangepaste-scripting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De Multi-step API (MSA)-controleregel beschikt over krachtige [ingebouwde functies]([LINK_URL_1]) die een gebruiksvriendelijke en no-code-oplossing bieden om het gedrag van uw API's te testen.

Hoewel u met een no-code-benadering een heel eind komt bij het bouwen van goede monitoring-setups, heeft u mogelijk een scripttaal nodig om diepgaande functionele tests uit te voeren en volledig te beschrijven wat u van uw API's verwacht. Bijvoorbeeld het toevoegen van een aangepaste logica of het verwerken van geavanceerder gedrag die niet kunnen worden bereikt in een UI-gebaseerde setup alleen.

Met de MSA-controleregel kunt u zowel klassieke no-code-functies als aangepaste scripting verwerken. U kunt ingebouwde UI functies gebruiken samen met hun scripting-tegenhangers. U hoeft uw controleregels niet helemaal opnieuw te maken als u bestaande API controleregels heeft en aangepaste scripting wilt toevoegen. Begin gewoon met het toevoegen van een aantal scripts en laat ze werken naast uw bestaande setup.

## Pre-Request- en Post-Response-scripts

Een API-controleregel bestaat uit één of meerdere stappen die in een reeks worden uitgevoerd. Voor elke MSA-stap (behalve Wacht-stappen) zijn twee scripteditors beschikbaar: de tabbladen [SHORTCODE_1] Pre-Request [SHORTCODE_2] en [SHORTCODE_3] Post-Response [SHORTCODE_4]:

- Met de **Pre-Request script**-editor kunt u scripts schrijven ter voorbereiding op het verzenden van een HTTP request. Dit is handig voor het voorbereiden en berekenen van waarden die u in de request wilt opnemen, zoals omgevingsvariabelen, URL-parameters, request headers of content body. Het script dat in deze editor is geschreven, wordt uitgevoerd *voordat* de API request naar de server wordt verzonden.

- Met de **Post-Response script**-editor kunt u scripts schrijven om de HTTP response die van de API terugkomt te verifiëren en te verwerken. Dit is handig voor het schrijven van aangepaste logica om response headers te controleren, de volledigheid en consistentie van uw content te valideren en die contentdata te gebruiken om voor te bereiden op volgende stappen. Het script dat in deze editor is geschreven, wordt alleen uitgevoerd *nadat* de API response succesvol is ontvangen van de server. Als er een verbindingsfout optreedt, wordt het script niet uitgevoerd en worden assertions of variabelen in het tabblad [SHORTCODE_5] Response [SHORTCODE_6] niet gevalideerd.

Deze editors bevatten ook de volgende functies:
![Tabbladen Aangepaste scripting]([LINK_URL_2])

- Regelnummering — geeft numerieke waarden weer die de scripts of codes per regel identificeren.
- Codemarkering — geeft codes weer in een kleurgecodeerd formaat om syntaxisfouten en trefwoorden eenvoudig te identificeren.
- Codeaanvulling — stelt automatisch mogelijke codecombinaties voor om het schrijven van scripts te ondersteunen.
- Snippets-paneel — biedt een lijst met nuttige codefragmenten die u automatisch kunt invoegen in uw code-editor nadat u ze heeft geselecteerd.

## Snippets

Met de **Pre-Request**- en **Post-Response**-editors kunt u scripts invoegen en uitvoeren die zijn geschreven in JavaScript. Naast het volledige scala aan mogelijkheden dat standaard Javascript biedt, kunt u ook **Snippets** gebruiken.

**Snippets** zijn speciale functies waarmee u toegang krijgt tot data van HTTP requests (tijdens het Pre-Request-proces) en HTTP responses (tijdens het Post-Response-proces). U kunt er ook log statements mee uitvoeren, berekende data opslaan als [Custom metrics]([LINK_URL_3]) en tests uitvoeren op stapdata. Deze speciale functies zijn toegankelijk via een uniek object genaamd [INLINE_CODE_1].

## Algemene of basis ut-objecten

In deze sectie is de lijst met algemene [INLINE_CODE_2]-objecten als volgt

- [INLINE_CODE_3] geeft toegang tot het API request object.
- [INLINE_CODE_4] geeft toegang tot het API response object.
- [INLINE_CODE_5] is de verzameling variabelen die u in alle API-stappen kunt gebruiken. Gebruik deze om waarden van de ene stap naar de volgende door te geven. Alle [Voorgedefinieerde variabelen]([LINK_URL_4]) of variabelen die u gebruikt in het tabblad [SHORTCODE_7] Response [SHORTCODE_8] worden opgenomen in deze objectverzameling.
- [INLINE_CODE_6] is een helperfunctie die de opgegeven logs naar de console log stuurt. Logt wanneer de pre-request scripts worden uitgevoerd, zijn te vinden in het **Pre-Request script Console log**, terwijl logs voor post-response scripts zijn te vinden in het **Post-response script Console log**.
- [INLINE_CODE_7] is de hoofdfunctie voor het vastleggen van testuitvoer. Alle testuitvoer die u definieert binnen elke [INLINE_CODE_8]-call, wordt vastgelegd en vermeld als een **Assertions**-resultaat, samen met de assertions die u definieert op het tabblad [SHORTCODE_9] Response [SHORTCODE_10] van elke stap.
- [INLINE_CODE_9] is een verzameling numerieke waarden rechtstreeks uit een API response. U kunt uw eigen aangepaste metrische variabele definiëren om waarden op te slaan of te berekenen uit een API response. Deze waarde wordt weergegeven in de details van de monitorcontrole voor elke meting en kan ook worden vermeld en in kaart worden gebracht in dashboards.
- Met [INLINE_CODE_10] kunt u MD5- en SHA-hashes genereren voor veilige dataverwerking en -overdracht. Het kan ook worden gebruikt om certificaatintrekkingslijsten (Certificate Revocation Lists, CRL's) te parseren.

U bent nu bekend met de algemene [INLINE_CODE_11]-basisobjecten. In deze sectie worden de kenmerken van elk [INLINE_CODE_12]-object gedetailleerd besproken.

### Request

Attributes van [INLINE_CODE_13]:

- [INLINE_CODE_14] — de URL van de request ophalen of instellen
- [INLINE_CODE_15] — de HTTP-methode van de request ophalen of instellen (zoals GET en POST)
- [INLINE_CODE_16] — een onbewerkte tekstversie van de request body ophalen of instellen

### Request headers

Functies van [INLINE_CODE_17]:

- [INLINE_CODE_18] — retourneert of de header bestaat en een specifieke waarde heeft
- [INLINE_CODE_19]— retourneert de waarde van de header. Retourneert een lege string als de header niet bestaat
- [INLINE_CODE_20] — creëert een nieuwe header met de opgegeven [INLINE_CODE_21] (alleen als de header nog niet was ingesteld)
- [INLINE_CODE_22] — voegt de header in met de opgegeven [INLINE_CODE_23] (als de header nog niet bestaat) of werkt de header bij met de opgegeven waarde (als de header al bestaat)
- [INLINE_CODE_24] — verwijdert de header

### Response

Attributes van [INLINE_CODE_25]:

- [INLINE_CODE_26] — haalt de numerieke HTTP response-statuscode op (zoals 200, 404, 500)
- [INLINE_CODE_27]  — haalt de HTTP statusbeschrijving op (zoals OK)
- [INLINE_CODE_28] — haalt de omvang van de response op in bytes
- [INLINE_CODE_29] — retourneert een byte-array met de response body. Responses zijn beperkt tot 100 MB

Functies van [INLINE_CODE_30]:

- [INLINE_CODE_31] — retourneert een onbewerkte tekstversie van de response body
- [INLINE_CODE_32] — retourneert een object door de responsetekst te parseren als JSON

### Response headers

Functies van [INLINE_CODE_33]:

- [INLINE_CODE_34] — retourneert of de header bestaat
- [INLINE_CODE_35] — retourneert de waarde van de header. Retourneert een lege string als de header niet bestaat

### Variabelen

Functies van [INLINE_CODE_36]:

- [INLINE_CODE_37] — retourneert of de variabele bestaat
- [INLINE_CODE_38] — retourneert de waarde van de variabele. Retourneert een lege string als de variabele niet bestaat
- [INLINE_CODE_39] — creëert de variabele (als deze niet bestaat) en slaat de opgegeven [INLINE_CODE_40] op in de variabele [INLINE_CODE_41]

### Custom metrics

Functies van [INLINE_CODE_42]:

- [INLINE_CODE_43] — retourneert de waarde van de custom metric variabele. Retourneert een lege string als de custom metric niet bestaat
- [INLINE_CODE_44] — slaat de opgegeven [INLINE_CODE_45] op in de custom metric variabele [INLINE_CODE_46]

Raadpleeg voor meer informatie de knowledgebase-artikelen [Vrije kengetallen instellen]([LINK_URL_5]) en [Variabelen bij Multi-step monitoring]([LINK_URL_6]) knowledge base articles.

### Test of Assert

Uptrends ondersteunt de Expect- en Should-interfaces van Chai JS, zie [Chai - Should]([LINK_URL_7]) en [Chai - Expect]([LINK_URL_8]) om te lezen hoe u verschillende waardetests en vergelijkingen kunt uitdrukken:

- [INLINE_CODE_47] + verschillende expressies
- [INLINE_CODE_48] + verschillende expressies  

Alle [INLINE_CODE_49] en [INLINE_CODE_50] expressies zullen (als ze op zichzelf worden gebruikt) een fout genereren als niet aan de gewenste criteria wordt voldaan en zullen de uitvoering van de controleregel stoppen. Alle aanvullende assertions die in de rest van het script zijn gedefinieerd zullen niet worden uitgevoerd.

Gebruik [INLINE_CODE_51] om de volledige set assertions uit te voeren, ongeacht of een van de eerdere assertions mislukt:

- [INLINE_CODE_52] — de uitvoer (succes of mislukking) van een [INLINE_CODE_53] of [INLINE_CODE_54] die is gedefinieerd in de gespecificeerde testFunction, komt terecht in de assertions-uitvoer van de controleregel. Bovendien zorgt [INLINE_CODE_55] ervoor dat de uitvoering van het script niet wordt stopgezet wanneer een assertion mislukt.

## Hashing

Functies van [INLINE_CODE_56]:

- [INLINE_CODE_57] — genereert een MD5-hash van de gespecificeerde waarde
- [INLINE_CODE_58] — genereert een SHA-1-hash van de gespecificeerde waarde
- [INLINE_CODE_59] — genereert een SHA-256-hash van de gespecificeerde waarde
- [INLINE_CODE_60] — genereert een SHA-512-hash van de gespecificeerde waarde

Met de scriptingmethodes voor het genereren van MD5- en SHA-hashes kunt u waarden veilig opslaan en verzenden, waardoor gegevensbescherming door hashing wordt gewaarborgd. 

Voorbeeld:

[CODE_BLOCK_1]

- [INLINE_CODE_61] — parseert een certificaatintrekkingslijst (Certificate Revocation List, CRL) en retourneert de metadata ervan. Een CRL-bestand moet als invoer worden verstrekt aan de functie [INLINE_CODE_62]. Als u bijvoorbeeld het veld [INLINE_CODE_63] wilt lezen uit een CRL-bestand of CRL-URL, kunt u de functie als volgt gebruiken:

[CODE_BLOCK_2]