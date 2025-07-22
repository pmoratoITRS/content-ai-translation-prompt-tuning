{
  "hero": {
    "title": "Automatische variabelen"
  },
  "title": "Automatische variabelen",
  "summary": "Een lijst met automatische variabelen voor gebruik in transactie- en multi-step API-controleregels",
  "url": "/support/kb/synthetic-monitoring/transacties/automatische-variabelen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/automatic-variables"
}

Met Uptrends' controleregeltypes [Transactie]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}}) en [Multi-step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}) kunt u een stroom doorlopen die uit verschillende stappen bestaat, hetzij over een pagina op het web, hetzij door rechtstreeks met een API te communiceren. In sommige gevallen moet u mogelijk data van variabelen verstrekken. Een bepaald formulier in een van uw transacties vereist bijvoorbeeld een tijdstempel, of u moet een unieke ID genereren om in een van de API-requests te gebruiken. Uptrends ondersteunt een aantal **automatische variabelen** die voor u worden gecreëerd. De meeste zijn feitelijk functies die een waarde genereren die u kunt gebruiken in uw HTTP-requests, invullen in tekstvelden of toevoegen aan selectors in uw transactiecontroleregels.

## Generieke automatische variabelen

De volgende automatische variabelen zijn beschikbaar voor de controleregeltypes **Transactie** en **Multi-step API**:

### Datum en tijd

{{< Code/Symbol type="variable" >}}{{@DateTime(format,offset)}}{{< /Code/Symbol >}} : deze variabele genereert dynamische datum/tijd-waarden, in overeenstemming met het formaat dat u specificeert en met een optionele offset. De datum/tijd (zonder offset) is altijd de huidige tijd uitgedrukt in de UTC-standaard (gecoördineerde universele tijd). 

Om de datum/tijd naar uw wensen op te maken, stelt u de parameter `format` in op:
  
- een waarde die wordt ondersteund door .NET date-notatie, bijv. `dd/MM/yyyy` of `MM/dd/yyyy`
- `Iso`, voor het formaat ISO 8601
- `Unix`, voor Unix epoch time

De optionele `offset` parameter kan worden gebruikt om de datum/tijd opnieuw te berekenen op basis van een bepaald verschil (in seconden) of een datum/tijd-functie. Als u de offsetparameter weglaat, wordt er geen offset toegepast. Om de datum/tijd opnieuw te berekenen gebruikt u de volgende opties: 

- Stel de offset-parameter in op een positief of negatief aantal seconden. Het opgegeven aantal seconden wordt opgeteld bij of afgetrokken van de huidige datum/tijd-waarde. Een typisch gebruiksscenario is om de datum/tijd in een andere tijdzone te berekenen of om naar een andere dag voor of na de huidige datum/tijd te gaan.

  Zie de onderstaande tabel voor enkele voorbeelden.

- Gebruik een datum/tijd-functie om de laatste of eerste dag van de huidige, vorige of volgende maand te berekenen ten opzichte van de opgegeven datum/tijd-waarde. De mogelijke waarden voor de offset zijn:
  - `LastDayOfMonth`
  - `FirstDayOfMonth`
  - `LastDayOfPreviousMonth`
  - `FirstDayOfPreviousMonth`
  - `LastDayOfNextMonth`
  - `FirstDayOfNextMonth`

De volgende tabel toont enkele voorbeelden, gebaseerd op het idee dat het nu 24 februari 2018 22:30 UTC is.
| Expressie                                  | Waarde                        | Beschrijving                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| `{{@DateTime(dd-MM-yyyy HH:mm)}}`           | 24-02-2018 22:30             | Nu, in het formaat dd-MM-yyyy HH:mm               |
| `{{@DateTime(dd-MM-yyyy HH:mm,-18000)}}`    | 24-02-2018 17:30             | Nu, in Eastern Standard Time (UTC-5)         |
| `{{@DateTime(ISO)}}`                        | 2018-02-24T22:30:00.0000000Z | Nu, in het formaat ISO 8601                       |
| `{{@DateTime(UNIX)}}`                       | 1519511400                   | Nu, in Unix epoch time                       |
| `{{@DateTime(MM/dd/yyyy,-86400)}}`          | 02/23/2018                   | Gisteren, in het formaat MM/dd/yyyy               |
| `{{@DateTime(MM/dd/yyyy,86400)}}`           | 02/25/2018                   | Morgen, in het formaat MM/dd/yyyy                |
| `{{@DateTime(MM/dd/yyyy,FirstDayOfMonth)}}` | 02/01/2018                   | Eerste dag van deze maand, in het formaat MM/dd/yyyy |
| `{{@DateTime(MM/dd/yyyy,LastDayOfMonth)}}`  | 02/28/2018                   | Laatste dag van deze maand, in het formaat MM/dd/yyyy  |

### Willekeurige unieke identifier

{{< Code/Symbol type="variable" >}}{{@RandomGuid}}{{< /Code/Symbol >}} : Deze variabele produceert een willekeurige waarde in de vorm `AB0AD14D-9611-41A8-9C25-7D94B895CFF1`. U kunt deze variabele gebruiken als u een willekeurige waarde moet opnemen in uw URL, POST data of HTTP header. Gebruikt u de variabele {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} in meerdere stappen, dan krijgt elke stap een andere willekeurige waarde. Elke keer dat de controleregel wordt uitgevoerd, krijgt u volledig nieuwe willekeurige waarden.

### Terugkerende willekeurige unieke identifier
{{< Code/Symbol type="variable" >}}{{@UniqueGuid}}{{< /Code/Symbol >}} : Deze unieke, willekeurig gegenereerde waarde kan tijdens de gehele transactie meerdere keren worden hergebruikt. In tegenstelling tot de hierboven genoemde {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}}, die elke keer een nieuwe waarde creëert, kunt u deze variabele gebruiken als u een terugkerende waarde moet opnemen in uw URL, POST data of HTTP header.
Dit kan bijvoorbeeld handig zijn bij het maken van een script voor een aanmeldingsproces, waarbij het gegenereerde e-mailadres en het bevestigde e-mailadres exact hetzelfde moeten zijn.

### Willekeurig geheel getal

{{< Code/Symbol type="variable" >}}{{@RandomInt(min,max)}}{{< /Code/Symbol >}} : Deze variabele produceert een willekeurig geheel getal, tussen de minimum- en maximumwaarden die u opgeeft (min en max inbegrepen). Geeft u bijvoorbeeld `{{@RandomInt(0,100)}}` op, dan produceert deze variabele een getal in het bereik 0..100.

### Willekeurige hoofdletters

{{< Code/Symbol type="variable" >}}{{@RandomChar(length)}}{{< /Code/Symbol >}} : Met deze automatische variabele kunt u een willekeurige reeks alfabetische tekens genereren met een gespecificeerde lengte. Alle tekens zullen in hoofdletters zijn. Bijvoorbeeld: `{{@RandomChar(5)}}` retourneert een willekeurige waarde in de vorm `GPLMQ`.

### Willekeurige US Medicare Beneficiary Identifiers (MBI)

{{< Code/Symbol type="variable" >}}{{@RandomUSMedicare}}{{< /Code/Symbol >}} : Met deze automatische variabele kunt u US Medicare Beneficiary Identifiers genereren. De MBI is een reeks van 11 alfanumerieke tekens, bijvoorbeeld `1EG4TE5MK73`. Let wel, deze code wordt gegenereerd zonder streepjes. De MBI-code kan worden gebruikt door bedrijven in de Amerikaanse gezondheidszorg.

## Transactie-specifieke (legacy) variabelen

De volgende set automatische variabelen is ouder, maar kan nog steeds worden gebruikt. Deze variabelen zijn alleen beschikbaar voor **Transactie**-controleregels.

### Tijdstempels

{{< Code/Symbol type="variable" >}}{timespan 0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Om een **tijdstempel te genereren en in te stellen** (huidige datum) in een tekstveld op uw pagina.

{{< Code/Symbol type="variable" >}}{timespan 1:0:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Om de **dag te verschuiven met 1** (morgen).

{{< Code/Symbol type="variable" >}}{timespan 0:1:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Hetzelfde als hierboven, maar dan **verschuiven met 1 uur**.

{{< Code/Symbol type="variable" >}}{timespan 0:0:1:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} en {{< Code/Symbol type="variable" >}}{timespan 0:0:0:1}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Om de huidige tijd te verschuiven met respectievelijk één minuut of één seconde.

### Willekeurige waarde uit een reeks

{{< Code/Symbol type="variable" >}}{random 1 2 3 4 5}{{< /Code/Symbol >}} : Stel een willekeurige variabele in uit een reeks. Deze functie stelt een willekeurige waarde in van één tot vijf.

{{< Code/Symbol type="variable" >}}{random apple banana orange}{{< /Code/Symbol >}} : Deze functie stelt een willekeurige string in uit de geselecteerde reeks: ofwel `apple`, `banana` of `orange` wordt ingesteld.

## Multi-step API-specifieke variabelen

De volgende variabelen en informatie zijn alleen van toepassing op het controleregeltype **Multi-step API**.

### Serveridentificatie (ID)

{{< Code/Symbol type="variable" >}}{{@ServerId}}{{< /Code/Symbol >}} : Tijdens de uitvoering van een Multi-step API-controleregel voert deze variabele een numerieke waarde uit die de locatie van het Uptrends-controlestation die deze controle uitvoert, identificeert. Als de controle bijvoorbeeld wordt uitgevoerd op Uptrends' controlestation in Sydney, Australië, wordt de variabele `30` uitgevoerd. De lijst met controlestationservers en hun corresponderende **Server ID's** is middels de [Uptrends API]({{< ref path="support/kb/api" lang="nl" >}}) beschikbaar op het [Controlestation-eindpunt](https://api.uptrends.com/v4/Checkpoint).

### Redirect-URL

{{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}} : In het geval dat een van de stappen in uw controleregel naar verwachting een redirect code retourneert en u die redirect respons wilt vastleggen en testen in plaats van deze automatisch te volgen, zal deze automatische variabele de URL bevatten waarnaar de redirect verwijst. Dit gebeurt alleen als u ervoor kiest om niet automatisch redirects te volgen, maar een assertion instelt die controleert op de juiste redirectcode. Deze procedure wordt hier gedetailleerder uitgelegd: [Multi-step monitoring - redirects verwerken]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="nl" >}}).

### Random float

{{< Code/Symbol type="variable" >}}{{@RandomFloat(min,max)}}{{< /Code/Symbol >}} : Gebruik deze functie om een getal met een floating point (drijvende komma) te genereren binnen het ingevoerde bereik (min/max). De precisie (aantal cijfers achter de komma) van de gegenereerde float wordt afgeleid van de hoogste precisie van de gebruikte `min` en `max` waarden. 

Bijvoorbeeld: `{{@RandomFloat(-1.2,3.00000)}}` genereert een random float tussen -1,2 en 3,0 met een precisie van 5, zoals 2,12345.

## Een automatisch gegenereerde waarde meerdere keren gebruiken

Sommige van deze variabele functies (met name de functies die willekeurige en datum/tijd-variabelen produceren) worden telkens wanneer u ze gebruikt opnieuw beoordeeld en zullen elke keer een nieuwe waarde genereren. Als u een bepaalde waarde wilt genereren en deze meerdere keren wilt gebruiken in uw meerstapsscenario, kunt u een voorgedefinieerde variabele definiëren (zoals besproken in het artikel [Variabelen bij Multi-step monitoring]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}})) en een automatische variabele gebruiken als zijn waarde.

### Voorbeelden van voorgedefinieerde waarden waarbij automatische variabelen worden gebruikt

| Naam          | Waarde                           | Gebruik                                                                                                                                                                                                                           |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SearchDate`  | `{{@DateTime(dd-MM-yyyy)}}`     | Gebruik een datumwaarde als input voor een zoekopdracht.                                                                                                                                                                            |
| `UniqueEmail` | `{{@RandomGuid}}@mycompany.com` | Gebruik een willekeurige guid-waarde in combinatie met vaste tekst om een e-mailadres te genereren dat elke keer anders is.                                                                                                                        |
| `OrderAmount` | `{{@RandomInt(1, 10)}}`         | Gebruik een willekeurig getal tussen 1 en 10 als het aantal te bestellen producten. In een volgende call kunt u deze variabele opnieuw gebruiken om de inhoud van een winkelwagen te controleren en te kijken of deze inderdaad de bestelde hoeveelheid bevat. |
