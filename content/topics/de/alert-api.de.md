{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Nutze unsere Alert API, um Alarmierungsinformationen aus deinem Uptrends Account abzurufen und mit ihnen zu arbeiten.",
  "url": "/support/kb/api/alert-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-api",
  "sectionlist": true,
  "tableofcontents": true
}

Die [Alert API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Alert/Alert_GetMonitorAlerts) enthält Endpunkte, die Alarmierungsinformationen eines bestimmten Prüfobjekts oder von Prüfobjektgruppen liefern.

## Alarmparameter

Die folgenden Parameter sind mit der Alert API verfügbar:

| Name | Beschreibung |
|--|--|
| `monitorGuid` | Die einzigartige Kennung des Prüfobjekts. |
| `monitorGroupGuid` | Die einzigartige Kennung der Prüfobjektgruppe. |
| `IncludeReminders` | Eine boolesche Option, standardmäßig auf **false** gesetzt. Wenn auf **true** gesetzt, enthält dieser Parameter die Erinnerungs-Alarme in der API-Antwort. |
| `Cursor`| {{< tableformatter >}}  Ein Zeichenketten-(Abfrage)-Wert, der verwendet wird, um Teile des Datensets zu übergehen. Eine detaillierte Erläuterung findest du unter [Cursor]({{< ref path="/support/kb/api/alert-api#cursor" lang="de" >}}). {{< /tableformatter >}}|
| `Sorting`| Eine Zeichenkette, die Alarme in **aufsteigender** oder **absteigender** Reihenfolge ordnet. |
| `Take`| Ein Integer von **0** bis **100**, der die Anzahl zurückgegebener Alarmierungsdatensätze beziffert. |
| `Start`| Ein benutzerdefinierter Datumsparameter (YYYY-mm-dd), der mit dem `End`-Parameter verwendet wird, um das Startdatum für die zurückgegebenen Alarmierungsdatensätze anzuzeigen. Dieser Parameter kann nicht zugleich mit PresetPeriod verwendet werden. |
| `End`| Ein benutzerdefinierter Datumsparameter (YYYY-mm-dd), der mit dem `Start`-Parameter verwendet wird, um das Enddatum für die zurückgegebenen Alarmierungsdatensätze anzuzeigen. Dieser Parameter kann nicht zugleich mit PresetPeriod verwendet werden. |
| `PresetPeriod`| {{< tableformatter >}} Eine Liste von Zeiträumen, um Alarme eines bestimmten Zeitraums zu filtern. Dies kann nicht gleichzeitig mit den Parametern `Start` und `End` verwendet werden. Eine detaillierte Erläuterung findest du unter [PresetPeriod]({{< ref path="/support/kb/api/alert-api#presetperiod" lang="de" >}}).  {{< /tableformatter >}}|

### Cursor

Der Cursor-Parameter fungiert als Zeiger, mit dem du das Alarmierungs-Datenset überfahren kannst. Es dient als Kennung dessen, welche Alarmierungsdaten generiert wurden  und welcher Alarmierungsdatensatz als Nächstes folgt.

Du hast beispielsweise insgesamt 300 Prüfobjektalarme und möchtest die Alarme 101–200 abrufen. Da die Alert API dir erlaubt, maximal 100 Alarmierungsdatensätze pro Batch abzurufen, erzeugt die erste Sendung der API-Antwort das **Cursors** JSON-Objekt mit den Werten **Next** und **Self**:

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

Im Rahmen dieses Beispiels verwenden wir den Wert **Next**, um den 101. Alarm und aufwärts abzurufen. Der Wert **Self** wird als Cursor verwendet, um das erste Batch der Alarme 1 bis 100 abzurufen.

{{< callout >}} **Hinweis:** Der **Cursor** wird pro Batch und nicht pro Alarmierungsdatensatz erzeugt. Wenn du das erste Batch an Alarmen abrufst, ohne dass es nachfolgende Alarmierungsdatensätze gibt, wird kein **Cursor** erzeugt. Sind weitere Daten verfügbar, wird ein **Cursor** für jedes Batch erzeugt. Verwende den **Take**-Parameter, um die Batch-Größe von 1 bis 100 Alarmierungsdatensätze zu bestimmen. {{< /callout >}}

### PresetPeriod

Es gibt die folgenden Optionen, um Alarme mit bestimmter Dauer zu filtern:

- CurrentDay, CurrentWeek, CurrentMonth, CurrentQuarter, CurrentYear
- Previous Day, Previous Week, Previous Month, Previous Quarter, Previous Year
- Last2Hours, Last6Hours, Last12Hours, Last24Hours, Last48Hours
- Last7Days, Last30Days, Last60Days, Last90Days, Last365Days
- Last3Months, Last6Months, Last12Months, Last24Months

Beachte, dass der eingeschlossene Zeitraum für die vorherige Zeit, die letzten Stunden, letzten Tage und letzten Monate nur angewandt werden, wenn die volle Dauer erfüllt ist.

Wenn du eine **PresetPeriod** von **Last7Days** angibst und Alarmierungsdatensätze an einem Montag um 8:00 Uhr generierst, umfassen deine Ergebnisse die Tage von Sonntag bis Sonntag, was die letzten sieben vollständigen Tage abdeckt. Beachte, dass der Tag (Montag), an dem du den Bericht erzeugt hast, nicht enthalten ist, da der Tag noch nicht vollständig verstrichen ist.

Genauso, wenn du **PresetPeriod** als **Last12Months** angibst und Datensätze am 25. Januar 2025 erzeugst. Du erhältst die Ergebnisse vom 31. Dezember 2024 und den 11 Monaten zuvor. Die Alarme von Januar 2024 und Januar 2025 werden nicht in dem Bericht enthalten sein, weil der Monat Januar noch nicht abgeschlossen ist.

## Alarm-Endpunkte

Es gibt die folgenden API-Methoden:

### GET /Alert/Monitor/{monitorGuid}

Diese Methode gibt die Alarminformationen für ein bestimmtes Prüfobjekt aus.

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

Diese Methode gibt die Alarminformationen für eine bestimmte Prüfobjektgruppe aus.

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
