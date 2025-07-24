{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "De beschikbare API-methodes voor het manipuleren van controleregelgroepen.",
  "url": "[URL_BASE_TOPICS]api/monitorgroup-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Deze pagina beschrijft de beschikbare API-methodes voor het manipuleren van controleregelgroepen. Raadpleeg [Uptrends Controleregelgroep API]([LINK_URL_1]) voor meer informatie.

## Beschrijving van het MonitorGroup-object

Het volgende MonitorGroup-object wordt gebruikt in de MonitorGroupAPI-eindpunten:

| Naam               | Beschrijving                                                                         | Datatype |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | De unieke identificatie voor de controleregelgroep.                                       | Tekenreeks |
| [INLINE_CODE_2]      | De naam van de controleregelgroep.                                              | Tekenreeks |
| [INLINE_CODE_3]            | [SHORTCODE_1] 
Geeft aan of de controleregelgroep de standaard [Alle controleregels]([LINK_URL_2])-groep is. [SHORTCODE_2] | Booleaans  |
| [INLINE_CODE_4] | Geeft aan of het aantal credits voor de controleregelgroep onbeperkt is of niet.  |  Booleaans  |
| [INLINE_CODE_5] |[SHORTCODE_3] 
Retourneert het aantal credits dat is gebruikt voor [Uptimecontroleregels]([LINK_URL_3]). [SHORTCODE_4] | Geheel getal |
| [INLINE_CODE_6]            | [SHORTCODE_5] 
Retourneert het aantal credits dat is gebruikt voor [Browsercontroleregels (Full-Page Check)]([LINK_URL_4]). [SHORTCODE_6] | Geheel getal |
| [INLINE_CODE_7]            | [SHORTCODE_7]
Retourneert het aantal credits dat is gebruikt voor [Transactiecontroleregels]([LINK_URL_5]).  [SHORTCODE_8] | Geheel getal |
| [INLINE_CODE_8]            | [SHORTCODE_9] 
Retourneert het aantal credits dat is gebruikt voor [Multi-step API (MSA)]([LINK_URL_6]) en [Postman]([LINK_URL_7])-controleregels. [SHORTCODE_10] | Geheel getal |
| [INLINE_CODE_9]            | Retourneert het aantal credits dat wordt gebruikt door bestaande accounts die één creditprijstarief gebruiken. | Geheel getal |

### De groep Alle controleregels

De groep **Alle controleregels** is een controleregel- of systeemgroep die standaard al uw controleregels bevat. Gebruik de Guid van deze groep om bewerkingen te beheren die van invloed zijn op alle controleregels, zoals het starten of stoppen van alle controleregels of alerts.
Merk op dat u het lidmaatschap van deze groep niet kunt wijzigen.


## Eindpunten voor controleregelgroepbeheer

De volgende API-eindpunten zijn beschikbaar voor het maken, wijzigen en verwijderen van controleregelgroepen, evenals de controleregels binnen die groepen.

| Requesttype | Eindpunt                                                 | Gebruik                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | [INLINE_CODE_10]                                          | Verkrijgt alle controleregelgroepen                                        |
| POST         | [INLINE_CODE_11]                                          | Creëert een nieuwe controleregelgroep                                    |
| GET          | [INLINE_CODE_12]                       | Verkrijgt de details van een controleregelgroep                            |
| PUT          | [INLINE_CODE_13]                       | Werkt een bestaande controleregelgroep bij                              |
| DELETE       | [INLINE_CODE_14]                       | Verwijdert een controleregelgroep                                        |
| GET          | [INLINE_CODE_15]               | Verkrijgt een lijst met alle controleregels die lid zijn van een controleregelgroep |
| POST         | [INLINE_CODE_16] | Voegt de gespecificeerde controleregel toe aan de controleregelgroep                |
| DELETE       | [INLINE_CODE_17] | Verwijdert de gespecificeerde controleregel uit de controleregelgroep           |

## Extra controleregelgroepbewerkingen

De volgende API-eindpunten zijn beschikbaar voor het uitvoeren van bewerkingen op alle controleregels in een groep:

| Requesttype | Eindpunt                                                            | Gebruik                                                                       |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | [INLINE_CODE_18]                  | Stopt alle controleregels in de gespecificeerde controleregelgroep                           |
| POST         | [INLINE_CODE_19]                 | Start alle controleregels in de gespecificeerde controleregelgroep                          |
| POST         | [INLINE_CODE_20]             | Stopt alerting voor alle controleregels in de gespecificeerde controleregelgroep              |
| POST         | [INLINE_CODE_21]            | Start alerting voor alle controleregels in de gespecificeerde controleregelgroep             |
| POST         | [INLINE_CODE_22] | Voegt de verstrekte onderhoudsperiode toe aan alle controleregels in de gespecificeerde groep |
