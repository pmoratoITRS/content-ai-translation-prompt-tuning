{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Ga aan de slag met Alert API om de alertinformatie in uw Uptrends-account op te halen en ermee te werken.",
  "url": "[URL_BASE_TOPICS]api/alert-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true,
  "tableofcontents": true
}

De [Alert API]([LINK_URL_1]) bevat eindpunten die alertinformatie van een specifieke controleregel of controleregelgroepen verstrekken.

## Alertparameters

De volgende parameters zijn beschikbaar in de Alert API:

| Naam | Beschrijving |
|--|--|
| [INLINE_CODE_1] | De unieke ID van de controleregel. |
| [INLINE_CODE_2] | De unieke ID van de controleregelgroep. |
| [INLINE_CODE_3] | Een boolean die standaard is ingesteld op **false**. Indien ingesteld op **true**, bevat deze parameter de herinneringsalerts in de API-respons. |
| [INLINE_CODE_4]| [SHORTCODE_1]  Een tekenreeks (query)-waarde die wordt gebruikt voor het doorlopen van de dataset. Raadpleeg [Cursor]([LINK_URL_2]) voor meer gedetailleerde uitleg. [SHORTCODE_2]|
| [INLINE_CODE_5]| Een tekenreeks die de alerts sorteert in **Oplopende** of **Aflopende** volgorde. |
| [INLINE_CODE_6]| Een geheel getal van **0** tot **100**, dat het aantal geretourneerde alertrecords aangeeft. |
| [INLINE_CODE_7]| Een aangepaste datumparameter (JJJJ-mm-dd) die wordt gebruikt met de parameter [INLINE_CODE_8] om de startdatum voor de geretourneerde alertrecords te specificeren. Deze parameter kan niet worden gebruikt in combinatie met PresetPeriod. |
| [INLINE_CODE_9]| Een aangepaste datumparameter (JJJJ-mm-dd) die wordt gebruikt met de parameter [INLINE_CODE_10] om de einddatum voor de geretourneerde alertrecords te specificeren. Deze parameter kan niet worden gebruikt in combinatie met PresetPeriod. |
| [INLINE_CODE_11]| [SHORTCODE_3] Een lijst met tijdsduur om alerts binnen een specifieke periode te filteren. Deze kan niet worden gebruikt in combinatie met de parameters [INLINE_CODE_12] en [INLINE_CODE_13]. Raadpleeg [PresetPeriod]([LINK_URL_3]) voor meer gedetailleerde uitleg.  [SHORTCODE_4]|

### Cursor

De Cursor-parameter fungeert als een aanwijzer waarmee u de alert-dataset kunt doorlopen. Deze dient als een identifier van welke alertrecords zijn gegenereerd en naar welke alertrecords u vervolgens wilt gaan.

U heeft bijvoorbeeld in totaal 300 controleregelalerts en u wilt alerts ophalen van 101-200. Aangezien u met de Alert API maximaal 100 alertrecords per batch kunt ophalen, genereert het aanroepen van de eerste batch vanuit de API-respons het JSON-object **Cursors** met de waarden **Next** en **Self**:

[CODE_BLOCK_1]

Gebruik voor dit voorbeeld de waarde **Next** om alerts op te halen vanaf de 101e alert en verder. Gebruik de waarde **Self** als cursor om de eerste batch alerts van 1 tot 100 op te halen.

[SHORTCODE_5] **Opmerking:** De **Cursor** wordt per batch gegenereerd en niet per alertrecord. Als u de eerste batch alerts ophaalt zonder dat er nog opeenvolgende alertrecords over zijn, wordt er geen **Cursor** gegenereerd. Als er meer data beschikbaar zijn, wordt er een **Cursor** gecreëerd voor die specifieke batch. Gebruik de parameter **Take** om de batchgrootte op te geven, variërend van 1 tot 100 alertrecords. [SHORTCODE_6]

### PresetPeriod

De volgende opties zijn beschikbaar om alerts gemakkelijk te filteren binnen een specifieke tijdsduur:

- CurrentDay, CurrentWeek, CurrentMonth, CurrentQuarter, CurrentYear
- Previous Day, Previous Week, Previous Month, Previous Quarter, Previous Year
- Last2Hours, Last6Hours, Last12Hours, Last24Hours, Last48Hours
- Last7Days, Last30Days, Last60Days, Last90Days, Last365Days
- Last3Months, Last6Months, Last12Months, Last24Months

Houd er rekening mee dat de opgenomen periode voor de previous time, last hours, last days en last months alleen worden toegepast wanneer de volledige tijdsduur is voltooid.

Als u een **PresetPeriod** van **Last7Days** opgeeft en alertrecords genereert op een maandag om 8:00 uur, krijgt u de resultaten van zondag tot zondag, wat de laatste zeven voltooide dagen beslaat. Merk op dat de tijd (maandag) waarop u het rapport genereerde, niet is opgenomen omdat de hele dag nog niet voorbij was.

Als u op dezelfde manier een **PresetPeriod** van **Last12Months** opgeeft en records genereert op 25 januari 2025, krijgt u de resultaten van 31 december 2024 en de 11 maanden daarvoor. De alerts van januari 2024 en januari 2025 worden niet opgenomen in het rapport omdat het maandbereik van januari nog niet is voltooid.

## Alerteindpunten

De volgende API-methoden zijn beschikbaar:

### GET /Alert/Monitor/{monitorGuid}

Deze methode retourneert alertinformatie voor een specifieke controleregel.

[CODE_BLOCK_2]

### GET /Alert/MonitorGroup/{monitorGroupGuid}

Deze methode retourneert alertinformatie voor een specifieke controleregelgroep.

```json
{
  "Data": [
    {
      "Type": "Alert",
      "Id": "afd846be-ddbf-49e1-ad15-2eee5f6d7544",
      "Attributes": {
        "AlertType": "Error",
        "MonitorGuid": "a591a38a-16e0-4dd2-9f15-d575b4c5a433",
        "Timestamp": "2025-01-02T02:30:46",
        "FirstError": "2024-12-11T20:11:01",
        "MonitorCheckId": 171193848695,
        "FirstErrorMonitorCheckId": 169412140540,
        "ErrorDescription": "Step 4 ([URL_1]): Element '.wn-product-btn' not found.",
        "IncidentKey": "9632cd34-0c13-4e2c-92cc-cca104432cd9-0-169412140545"
      },
      "Relationships": [
        {
          "Id": 171193848695,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/171193848695"
          }
        },
        {
          "Id": 169412140540,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/169412140540"
          }
        }
      ]
    },
    .....
  ]
}
