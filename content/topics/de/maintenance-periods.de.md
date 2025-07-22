{
  "hero": {
    "title": "Wartungszeiträume in der API"
  },
  "title": "Wartungszeiträume in der API",
  "url": "/support/kb/api/wartungszeitraeume-in-der-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/maintenance-periods"
}

Es gibt ein besonderes Set von API-Methoden, um Wartungszeiträume für ein Prüfobjekt oder für alle Prüfobjekte in einer Prüfobjektgruppe einzurichten.

## Object-Beschreibung für Wartungszeiträume

Die folgenden MaintenancePeriod-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th>Name</th><th>Beschreibung</th><th>Datentyp</th></tr></thead><tbody><tr class="odd"><td>Id</td><td>Die einzigartige Kennung des Wartungszeitraums</td><td>Integer</td></tr><tr class="even"><td>ScheduleMode</td><td>OneTime, Daily, Weekly oder Monthly</td><td>Enum</td></tr><tr class="odd"><td>StartDateTime</td><td>Startdatum und -zeit (nur für einen einmal geplanten Zeitraum)</td><td>DateTime</td></tr><tr class="even"><td>EndDateTime</td><td>Enddatum und -zeit eines einmal geplanten Wartungszeitraums</td><td>DateTime</td></tr><tr class="odd"><td>StartTime</td><td>Die Startzeit (“HH:mm”, eine 24-Stundennotation) eines sich wiederholenden (Daily, Weekly oder Monthly) Wartungszeitraums</td><td>String (“HH:mm”)</td></tr><tr class="even"><td>EndTime</td><td>Die Endzeit (“HH:mm”, eine 24-Stundennotation) eines sich wiederholenden (Daily, Weekly oder Monthly) Wartungszeitraums</td><td>String (“HH:mm”)</td></tr><tr class="odd"><td>WeekDay</td><td>Der Tag der Woche für einen Wartungszeitraum<br />
(Sunday/Monday/[…]/Saturday)</td><td>Enum</td></tr><tr class="even"><td>MonthDay</td><td>Die Zahl des Tages für einen monatlichen Wartungszeitraum</td><td>Int (1-31)</td></tr><tr class="odd"><td>MaintenanceType</td><td>DisableMonitoring (um das Prüfobjekt komplett zu deaktivieren) oder DisableNotifications (Monitoring wird weiterhin durchgeführt, aber Benachrichtigungen werden nicht gesendet)</td><td>Enum</td></tr></tbody></table>

Wenn ein Wartungszeitraum durch die API zurückgegeben wird, sind alle Eigenschaften vorhanden, aber abhängig vom ScheduleMode werden einige Felder in Bezug auf Start- und Enddaten/-zeiten nicht verwendet.

Für einen einmaligen Wartungszeitraum müssen wir Start- und Enddatum *und* -zeit wissen, sodass die Angaben StartDateTime und EndDateTime verwendet werden. Für sich wiederholende Wartungszeiträume sind die Felder Start- und Endzeiten angebracht und, abhängig vom Zeitplantyp, die Eigenschaften WeekDay oder MonthDay.

Zum Beispiel würde ein täglicher Zeitplan folgendermaßen aussehen:

    {
    "Id": 123, 
    "ScheduleMode": "Daily", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

Die Eigenschaften, die nicht für diesen Zeitplantyp relevant sind (DateTime, WeekDay und MonthDay), werden ausgelassen.

Ein wöchentlicher Zeitplan würde folgendermaßen aussehen:

    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

Ein monatlicher Zeitplan würde folgendermaßen aussehen:

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Ein einmaliger Zeitplan würde folgendermaßen aussehen:

    {
    "Id": 124, 
    "ScheduleMode": "OneTime", 
    "StartDateTime": "2018-09-24T22:00",
    "EndDateTime": "2018-09-24T22:00", 
    "MaintenanceType": "DisableMonitoring" 
    }

## Wartungszeitrum-Endpunkte

Es gibt die folgenden API-Endpunkte:

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th><strong>Anfragetyp</strong></th><th><strong>Endpunkt</strong></th><th><strong>Einsatz</strong></th></tr></thead><tbody><tr class="odd"><td>GET</td><td>Monitor/{monitorGuid}/MaintenancePeriod</td><td>Findet alle Wartungszeiträume für ein Prüfobjekt.</td></tr><tr class="even"><td>POST</td><td>Monitor/{monitorGuid}/MaintenancePeriod</td><td>Speichert den neuen angegebenen Wartungszeitraum für das spezifizierte Prüfobjekt</td></tr><tr class="odd"><td>PUT</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
{maintenancePeriodId}</td><td>Aktualisiert den spezifizierten Wartungszeitraum für das spezifizierte Prüfobjekt</td></tr><tr class="even"><td>DELETE</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
{maintenancePeriodId}</td><td>Löscht den spezifizierten Wartungszeitraum für das spezifizierte Prüfobjekt</td></tr><tr class="odd"><td>POST</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
Cleanup/{beforeDate}</td><td>Löscht alle einmaligen Wartungszeiträume für das spezifizierte Prüfobjekt, die älter als das spezifizierte Datum sind</td></tr><tr class="even"><td>POST</td><td>MonitorGroup/{monitorGroupGuid}/<br />
MaintenancePeriod</td><td>Fügt den angegebenen Wartungszeitraum zu allen Prüfobjekten in der spezifizierten Gruppe hinzu</td></tr></tbody></table>

### GET Monitor

`GET Monitor/{monitorGuid}/MaintenancePeriod`

Diese GET-Anfrage ergibt eine Sammlung mit allen Wartungszeiträumen, die für das Prüfobjekt mit angegebener GUID geplant sind.

Beispiel-Ausgabe:

    [
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }, 
    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
    ]

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod`

Diese Methode erzeugt einen Wartungszeitraum, der im Abfragetext angegeben wurde und dem Prüfobjekt mit der angegebenen GUID zugewiesen wird.

Eine POST-Abfrage erwartet eine Objektstruktur wie in den Beispielen unter „Object-Beschreibung für Wartungszeiträume“ angegeben. Wie dort gezeigt ist die Struktur abhängig vom Wartungszeitraumtyp (OneTime, Daily, Weekly oder Monthly). Des Weiteren sollte das Feld „Id“ nicht angegeben sein. Ein neuer Id-Wert wird automatisch generiert.

### PUT Monitor

`PUT Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Diese Methode aktualisiert den Wartungszeitraum mit angegebener Wartungszeitraum-ID durch die im Abfragetext angegeben Werte.

Erwartete Eingabe (Beispiel für einen monatlichen Wartungszeitraum):

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Bitte beachte, dass die Id des Wartungszeitraums in der Abfrage genauso wie im maintenancePeriodId-Parameter angegeben werden muss. Wenn die Id im Parameter nicht mit der Id des Wartungszeitraums im Abfragetext übereinstimmt, wird eine Ausnahme zurückgegeben.

### DELETE Monitor

`DELETE Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Diese Methode wird den Wartungszeitraum mit der in maintenancePeriodId spezifizierten Id aus dem Prüfobjekt mit der angegebenen monitorGuid löschen.

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate}`

Diese Methode wird alle **einmaligen** Zeitpläne mit einer vor dem in beforeDate angegebener StartDateTime aus dem Prüfobjekt mit der angegebenen monitorGuid entfernen.

### POST MonitorGroup

`POST MonitorGroup/{monitorGroupGuid}/MaintenancePeriod`

Diese Methode wird den im Abfragetext angegebenen Wartungszeitraum zu allen Prüfobjekten der Prüfobjektgruppe mit der angegebenen Guid der Prüfobjektgruppe hinzufügen.

Erwartete Eingabe (Beispiel für einen wöchentlichen Wartungszeitraum):

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
