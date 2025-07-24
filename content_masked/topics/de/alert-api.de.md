{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Nutze unsere Alert API, um Alarmierungsinformationen aus deinem Uptrends Account abzurufen und mit ihnen zu arbeiten.",
  "url": "[URL_BASE_TOPICS]api/alert-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true,
  "tableofcontents": true
}

Die [Alert API]([LINK_URL_1]) enthält Endpunkte, die Alarmierungsinformationen eines bestimmten Prüfobjekts oder von Prüfobjektgruppen liefern.

## Alarmparameter

Die folgenden Parameter sind mit der Alert API verfügbar:

| Name | Beschreibung |
|--|--|
| [INLINE_CODE_1] | Die einzigartige Kennung des Prüfobjekts. |
| [INLINE_CODE_2] | Die einzigartige Kennung der Prüfobjektgruppe. |
| [INLINE_CODE_3] | Eine boolesche Option, standardmäßig auf **false** gesetzt. Wenn auf **true** gesetzt, enthält dieser Parameter die Erinnerungs-Alarme in der API-Antwort. |
| [INLINE_CODE_4]| [SHORTCODE_1]  Ein Zeichenketten-(Abfrage)-Wert, der verwendet wird, um Teile des Datensets zu übergehen. Eine detaillierte Erläuterung findest du unter [Cursor]([LINK_URL_2]). [SHORTCODE_2]|
| [INLINE_CODE_5]| Eine Zeichenkette, die Alarme in **aufsteigender** oder **absteigender** Reihenfolge ordnet. |
| [INLINE_CODE_6]| Ein Integer von **0** bis **100**, der die Anzahl zurückgegebener Alarmierungsdatensätze beziffert. |
| [INLINE_CODE_7]| Ein benutzerdefinierter Datumsparameter (YYYY-mm-dd), der mit dem [INLINE_CODE_8]-Parameter verwendet wird, um das Startdatum für die zurückgegebenen Alarmierungsdatensätze anzuzeigen. Dieser Parameter kann nicht zugleich mit PresetPeriod verwendet werden. |
| [INLINE_CODE_9]| Ein benutzerdefinierter Datumsparameter (YYYY-mm-dd), der mit dem [INLINE_CODE_10]-Parameter verwendet wird, um das Enddatum für die zurückgegebenen Alarmierungsdatensätze anzuzeigen. Dieser Parameter kann nicht zugleich mit PresetPeriod verwendet werden. |
| [INLINE_CODE_11]| [SHORTCODE_3] Eine Liste von Zeiträumen, um Alarme eines bestimmten Zeitraums zu filtern. Dies kann nicht gleichzeitig mit den Parametern [INLINE_CODE_12] und [INLINE_CODE_13] verwendet werden. Eine detaillierte Erläuterung findest du unter [PresetPeriod]([LINK_URL_3]).  [SHORTCODE_4]|

### Cursor

Der Cursor-Parameter fungiert als Zeiger, mit dem du das Alarmierungs-Datenset überfahren kannst. Es dient als Kennung dessen, welche Alarmierungsdaten generiert wurden  und welcher Alarmierungsdatensatz als Nächstes folgt.

Du hast beispielsweise insgesamt 300 Prüfobjektalarme und möchtest die Alarme 101–200 abrufen. Da die Alert API dir erlaubt, maximal 100 Alarmierungsdatensätze pro Batch abzurufen, erzeugt die erste Sendung der API-Antwort das **Cursors** JSON-Objekt mit den Werten **Next** und **Self**:

[CODE_BLOCK_1]

Im Rahmen dieses Beispiels verwenden wir den Wert **Next**, um den 101. Alarm und aufwärts abzurufen. Der Wert **Self** wird als Cursor verwendet, um das erste Batch der Alarme 1 bis 100 abzurufen.

[SHORTCODE_5] **Hinweis:** Der **Cursor** wird pro Batch und nicht pro Alarmierungsdatensatz erzeugt. Wenn du das erste Batch an Alarmen abrufst, ohne dass es nachfolgende Alarmierungsdatensätze gibt, wird kein **Cursor** erzeugt. Sind weitere Daten verfügbar, wird ein **Cursor** für jedes Batch erzeugt. Verwende den **Take**-Parameter, um die Batch-Größe von 1 bis 100 Alarmierungsdatensätze zu bestimmen. [SHORTCODE_6]

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

[CODE_BLOCK_2]

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
