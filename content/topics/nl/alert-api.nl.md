{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Ga aan de slag met Alert API om de alertinformatie in uw Uptrends-account op te halen en ermee te werken.",
  "url": "/support/kb/api/alert-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-api",
  "sectionlist": true,
  "tableofcontents": true
}

De [Alert API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Alert/Alert_GetMonitorAlerts) bevat eindpunten die alertinformatie van een specifieke controleregel of controleregelgroepen verstrekken.

## Alertparameters

De volgende parameters zijn beschikbaar in de Alert API:

| Naam | Beschrijving |
|--|--|
| `monitorGuid` | De unieke ID van de controleregel. |
| `monitorGroupGuid` | De unieke ID van de controleregelgroep. |
| `IncludeReminders` | Een boolean die standaard is ingesteld op **false**. Indien ingesteld op **true**, bevat deze parameter de herinneringsalerts in de API-respons. |
| `Cursor`| {{< tableformatter >}}  Een tekenreeks (query)-waarde die wordt gebruikt voor het doorlopen van de dataset. Raadpleeg [Cursor]({{< ref path="/support/kb/api/alert-api#cursor" lang="nl" >}}) voor meer gedetailleerde uitleg. {{< /tableformatter >}}|
| `Sorting`| Een tekenreeks die de alerts sorteert in **Oplopende** of **Aflopende** volgorde. |
| `Take`| Een geheel getal van **0** tot **100**, dat het aantal geretourneerde alertrecords aangeeft. |
| `Start`| Een aangepaste datumparameter (JJJJ-mm-dd) die wordt gebruikt met de parameter `End` om de startdatum voor de geretourneerde alertrecords te specificeren. Deze parameter kan niet worden gebruikt in combinatie met PresetPeriod. |
| `End`| Een aangepaste datumparameter (JJJJ-mm-dd) die wordt gebruikt met de parameter `Start` om de einddatum voor de geretourneerde alertrecords te specificeren. Deze parameter kan niet worden gebruikt in combinatie met PresetPeriod. |
| `PresetPeriod`| {{< tableformatter >}} Een lijst met tijdsduur om alerts binnen een specifieke periode te filteren. Deze kan niet worden gebruikt in combinatie met de parameters `Start` en `End`. Raadpleeg [PresetPeriod]({{< ref path="/support/kb/api/alert-api#presetperiod" lang="nl" >}}) voor meer gedetailleerde uitleg.  {{< /tableformatter >}}|

### Cursor

De Cursor-parameter fungeert als een aanwijzer waarmee u de alert-dataset kunt doorlopen. Deze dient als een identifier van welke alertrecords zijn gegenereerd en naar welke alertrecords u vervolgens wilt gaan.

U heeft bijvoorbeeld in totaal 300 controleregelalerts en u wilt alerts ophalen van 101-200. Aangezien u met de Alert API maximaal 100 alertrecords per batch kunt ophalen, genereert het aanroepen van de eerste batch vanuit de API-respons het JSON-object **Cursors** met de waarden **Next** en **Self**:

```json
{
  ...

  "Cursors": {
    "Next": "qKLVZ/HGD2XeFkiwNFWJK+nRDuOjjBRipct8qOfRjRmGUG8F5P1WzrQ4p3JFfXoErs96xb+DS0SAPW+XDUi9Zw/zdo4uHXL3TYBhodxfQQul3L4mwDk=",
    "Self": "KYhsR26Se8cQbeQm+o3LXawJXu3Pe6NvSefBcMivZ5QA+rFcRUrHTErK+TrhrUN3Ss8QUing/+jUkjgl3QOvB3kf3AZ+EOubhya5s3CWF+HGWEQkQQ=="
  },
  ...
}

```

Gebruik voor dit voorbeeld de waarde **Next** om alerts op te halen vanaf de 101e alert en verder. Gebruik de waarde **Self** als cursor om de eerste batch alerts van 1 tot 100 op te halen.

{{< callout >}} **Opmerking:** De **Cursor** wordt per batch gegenereerd en niet per alertrecord. Als u de eerste batch alerts ophaalt zonder dat er nog opeenvolgende alertrecords over zijn, wordt er geen **Cursor** gegenereerd. Als er meer data beschikbaar zijn, wordt er een **Cursor** gecreëerd voor die specifieke batch. Gebruik de parameter **Take** om de batchgrootte op te geven, variërend van 1 tot 100 alertrecords. {{< /callout >}}

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

```json
{
      "Type": "Alert",
      "Id": "cd73d946-8577-44f7-b7ed-134ae2c0985e",
      "Attributes": {
        "AlertType": "Reminder",
        "MonitorGuid": "a591a38a-16e0-4dd2-9f15-d575b4c5a433",
        "Timestamp": "2025-01-02T05:39:21",
        "FirstError": "2024-12-11T20:11:01",
        "MonitorCheckId": 171204791912,
        "FirstErrorMonitorCheckId": 169412140540,
        "ErrorDescription": "Step 4 (https://galacticshirts.com): Element '.wn-product-btn' not found.",
        "IncidentKey": "9632cd34-0c13-4e2c-92cc-cca104432cd9-0-169412140545"
      },
      "Relationships": [
        {
          "Id": 171204791912,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/171204791912"
          }
        },
        {
          "Id": 169412140540,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/169412140540"
          }
        }
      ],
      ....
}
```

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
        "ErrorDescription": "Step 4 (https://galacticshirts.com): Element '.wn-product-btn' not found.",
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
