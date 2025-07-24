{
  "hero": {
    "title": "Automatische variabelen"
  },
  "title": "Automatische variabelen",
  "summary": "Een lijst met automatische variabelen voor gebruik in transactie- en multi-step API-controleregels",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/automatische-variabelen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met Uptrends' controleregeltypes [Transactie]([LINK_URL_1]) en [Multi-step API]([LINK_URL_2]) kunt u een stroom doorlopen die uit verschillende stappen bestaat, hetzij over een pagina op het web, hetzij door rechtstreeks met een API te communiceren. In sommige gevallen moet u mogelijk data van variabelen verstrekken. Een bepaald formulier in een van uw transacties vereist bijvoorbeeld een tijdstempel, of u moet een unieke ID genereren om in een van de API-requests te gebruiken. Uptrends ondersteunt een aantal **automatische variabelen** die voor u worden gecreëerd. De meeste zijn feitelijk functies die een waarde genereren die u kunt gebruiken in uw HTTP-requests, invullen in tekstvelden of toevoegen aan selectors in uw transactiecontroleregels.

## Generieke automatische variabelen

De volgende automatische variabelen zijn beschikbaar voor de controleregeltypes **Transactie** en **Multi-step API**:

### Datum en tijd

[SHORTCODE_1][SYSTEM_VAR_1][SHORTCODE_2] : deze variabele genereert dynamische datum/tijd-waarden, in overeenstemming met het formaat dat u specificeert en met een optionele offset. De datum/tijd (zonder offset) is altijd de huidige tijd uitgedrukt in de UTC-standaard (gecoördineerde universele tijd). 

Om de datum/tijd naar uw wensen op te maken, stelt u de parameter [INLINE_CODE_1] in op:
  
- een waarde die wordt ondersteund door .NET date-notatie, bijv. [INLINE_CODE_2] of [INLINE_CODE_3]
- [INLINE_CODE_4], voor het formaat ISO 8601
- [INLINE_CODE_5], voor Unix epoch time

De optionele [INLINE_CODE_6] parameter kan worden gebruikt om de datum/tijd opnieuw te berekenen op basis van een bepaald verschil (in seconden) of een datum/tijd-functie. Als u de offsetparameter weglaat, wordt er geen offset toegepast. Om de datum/tijd opnieuw te berekenen gebruikt u de volgende opties: 

- Stel de offset-parameter in op een positief of negatief aantal seconden. Het opgegeven aantal seconden wordt opgeteld bij of afgetrokken van de huidige datum/tijd-waarde. Een typisch gebruiksscenario is om de datum/tijd in een andere tijdzone te berekenen of om naar een andere dag voor of na de huidige datum/tijd te gaan.

  Zie de onderstaande tabel voor enkele voorbeelden.

- Gebruik een datum/tijd-functie om de laatste of eerste dag van de huidige, vorige of volgende maand te berekenen ten opzichte van de opgegeven datum/tijd-waarde. De mogelijke waarden voor de offset zijn:
  - [INLINE_CODE_7]
  - [INLINE_CODE_8]
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
  - [INLINE_CODE_11]
  - [INLINE_CODE_12]

De volgende tabel toont enkele voorbeelden, gebaseerd op het idee dat het nu 24 februari 2018 22:30 UTC is.
| Expressie                                  | Waarde                        | Beschrijving                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| [INLINE_CODE_13]           | 24-02-2018 22:30             | Nu, in het formaat dd-MM-yyyy HH:mm               |
| [INLINE_CODE_14]    | 24-02-2018 17:30             | Nu, in Eastern Standard Time (UTC-5)         |
| [INLINE_CODE_15]                        | 2018-02-24T22:30:00.0000000Z | Nu, in het formaat ISO 8601                       |
| [INLINE_CODE_16]                       | 1519511400                   | Nu, in Unix epoch time                       |
| [INLINE_CODE_17]          | 02/23/2018                   | Gisteren, in het formaat MM/dd/yyyy               |
| [INLINE_CODE_18]           | 02/25/2018                   | Morgen, in het formaat MM/dd/yyyy                |
| [INLINE_CODE_19] | 02/01/2018                   | Eerste dag van deze maand, in het formaat MM/dd/yyyy |
| [INLINE_CODE_20]  | 02/28/2018                   | Laatste dag van deze maand, in het formaat MM/dd/yyyy  |

### Willekeurige unieke identifier

[SHORTCODE_3][SYSTEM_VAR_10][SHORTCODE_4] : Deze variabele produceert een willekeurige waarde in de vorm [INLINE_CODE_21]. U kunt deze variabele gebruiken als u een willekeurige waarde moet opnemen in uw URL, POST data of HTTP header. Gebruikt u de variabele [SHORTCODE_5]@RandomGuid[SHORTCODE_6] in meerdere stappen, dan krijgt elke stap een andere willekeurige waarde. Elke keer dat de controleregel wordt uitgevoerd, krijgt u volledig nieuwe willekeurige waarden.

### Terugkerende willekeurige unieke identifier
[SHORTCODE_7][SYSTEM_VAR_11][SHORTCODE_8] : Deze unieke, willekeurig gegenereerde waarde kan tijdens de gehele transactie meerdere keren worden hergebruikt. In tegenstelling tot de hierboven genoemde [SHORTCODE_9]@RandomGuid[SHORTCODE_10], die elke keer een nieuwe waarde creëert, kunt u deze variabele gebruiken als u een terugkerende waarde moet opnemen in uw URL, POST data of HTTP header.
Dit kan bijvoorbeeld handig zijn bij het maken van een script voor een aanmeldingsproces, waarbij het gegenereerde e-mailadres en het bevestigde e-mailadres exact hetzelfde moeten zijn.

### Willekeurig geheel getal

[SHORTCODE_11][SYSTEM_VAR_12][SHORTCODE_12] : Deze variabele produceert een willekeurig geheel getal, tussen de minimum- en maximumwaarden die u opgeeft (min en max inbegrepen). Geeft u bijvoorbeeld [INLINE_CODE_22] op, dan produceert deze variabele een getal in het bereik 0..100.

### Willekeurige hoofdletters

[SHORTCODE_13][SYSTEM_VAR_14][SHORTCODE_14] : Met deze automatische variabele kunt u een willekeurige reeks alfabetische tekens genereren met een gespecificeerde lengte. Alle tekens zullen in hoofdletters zijn. Bijvoorbeeld: [INLINE_CODE_23] retourneert een willekeurige waarde in de vorm [INLINE_CODE_24].

### Willekeurige US Medicare Beneficiary Identifiers (MBI)

[SHORTCODE_15][SYSTEM_VAR_16][SHORTCODE_16] : Met deze automatische variabele kunt u US Medicare Beneficiary Identifiers genereren. De MBI is een reeks van 11 alfanumerieke tekens, bijvoorbeeld [INLINE_CODE_25]. Let wel, deze code wordt gegenereerd zonder streepjes. De MBI-code kan worden gebruikt door bedrijven in de Amerikaanse gezondheidszorg.

## Transactie-specifieke (legacy) variabelen

De volgende set automatische variabelen is ouder, maar kan nog steeds worden gebruikt. Deze variabelen zijn alleen beschikbaar voor **Transactie**-controleregels.

### Tijdstempels

[SHORTCODE_17]{timespan 0}{now dd-MM-yyyy}[SHORTCODE_18] : Om een **tijdstempel te genereren en in te stellen** (huidige datum) in een tekstveld op uw pagina.

[SHORTCODE_19]{timespan 1:0:0:0}{now dd-MM-yyyy}[SHORTCODE_20] : Om de **dag te verschuiven met 1** (morgen).

[SHORTCODE_21]{timespan 0:1:0:0}{now dd-MM-yyyy}[SHORTCODE_22] : Hetzelfde als hierboven, maar dan **verschuiven met 1 uur**.

[SHORTCODE_23]{timespan 0:0:1:0}{now dd-MM-yyyy}[SHORTCODE_24] en [SHORTCODE_25]{timespan 0:0:0:1}{now dd-MM-yyyy}[SHORTCODE_26] : Om de huidige tijd te verschuiven met respectievelijk één minuut of één seconde.

### Willekeurige waarde uit een reeks

[SHORTCODE_27]{random 1 2 3 4 5}[SHORTCODE_28] : Stel een willekeurige variabele in uit een reeks. Deze functie stelt een willekeurige waarde in van één tot vijf.

[SHORTCODE_29]{random apple banana orange}[SHORTCODE_30] : Deze functie stelt een willekeurige string in uit de geselecteerde reeks: ofwel [INLINE_CODE_26], [INLINE_CODE_27] of [INLINE_CODE_28] wordt ingesteld.

## Multi-step API-specifieke variabelen

De volgende variabelen en informatie zijn alleen van toepassing op het controleregeltype **Multi-step API**.

### Serveridentificatie (ID)

[SHORTCODE_31][SYSTEM_VAR_17][SHORTCODE_32] : Tijdens de uitvoering van een Multi-step API-controleregel voert deze variabele een numerieke waarde uit die de locatie van het Uptrends-controlestation die deze controle uitvoert, identificeert. Als de controle bijvoorbeeld wordt uitgevoerd op Uptrends' controlestation in Sydney, Australië, wordt de variabele [INLINE_CODE_29] uitgevoerd. De lijst met controlestationservers en hun corresponderende **Server ID's** is middels de [Uptrends API]([LINK_URL_3]) beschikbaar op het [Controlestation-eindpunt]([LINK_URL_4]).

### Redirect-URL

[SHORTCODE_33][SYSTEM_VAR_18][SHORTCODE_34] : In het geval dat een van de stappen in uw controleregel naar verwachting een redirect code retourneert en u die redirect respons wilt vastleggen en testen in plaats van deze automatisch te volgen, zal deze automatische variabele de URL bevatten waarnaar de redirect verwijst. Dit gebeurt alleen als u ervoor kiest om niet automatisch redirects te volgen, maar een assertion instelt die controleert op de juiste redirectcode. Deze procedure wordt hier gedetailleerder uitgelegd: [Multi-step monitoring - redirects verwerken]([LINK_URL_5]).

### Random float

[SHORTCODE_35][SYSTEM_VAR_19][SHORTCODE_36] : Gebruik deze functie om een getal met een floating point (drijvende komma) te genereren binnen het ingevoerde bereik (min/max). De precisie (aantal cijfers achter de komma) van de gegenereerde float wordt afgeleid van de hoogste precisie van de gebruikte [INLINE_CODE_30] en [INLINE_CODE_31] waarden. 

Bijvoorbeeld: [INLINE_CODE_32] genereert een random float tussen -1,2 en 3,0 met een precisie van 5, zoals 2,12345.

## Een automatisch gegenereerde waarde meerdere keren gebruiken

Sommige van deze variabele functies (met name de functies die willekeurige en datum/tijd-variabelen produceren) worden telkens wanneer u ze gebruikt opnieuw beoordeeld en zullen elke keer een nieuwe waarde genereren. Als u een bepaalde waarde wilt genereren en deze meerdere keren wilt gebruiken in uw meerstapsscenario, kunt u een voorgedefinieerde variabele definiëren (zoals besproken in het artikel [Variabelen bij Multi-step monitoring]([LINK_URL_6])) en een automatische variabele gebruiken als zijn waarde.

### Voorbeelden van voorgedefinieerde waarden waarbij automatische variabelen worden gebruikt

| Naam          | Waarde                           | Gebruik                                                                                                                                                                                                                           |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_33]  | [INLINE_CODE_34]     | Gebruik een datumwaarde als input voor een zoekopdracht.                                                                                                                                                                            |
| [INLINE_CODE_35] | [INLINE_CODE_36] | Gebruik een willekeurige guid-waarde in combinatie met vaste tekst om een e-mailadres te genereren dat elke keer anders is.                                                                                                                        |
| [INLINE_CODE_37] | [INLINE_CODE_38]         | Gebruik een willekeurig getal tussen 1 en 10 als het aantal te bestellen producten. In een volgende call kunt u deze variabele opnieuw gebruiken om de inhoud van een winkelwagen te controleren en te kijken of deze inderdaad de bestelde hoeveelheid bevat. |
