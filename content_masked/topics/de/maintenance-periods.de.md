{
  "hero": {
    "title": "Wartungszeiträume in der API"
  },
  "title": "Wartungszeiträume in der API",
  "url": "[URL_BASE_TOPICS]api/wartungszeitraeume-in-der-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Es gibt ein besonderes Set von API-Methoden, um Wartungszeiträume für ein Prüfobjekt oder für alle Prüfobjekte in einer Prüfobjektgruppe einzurichten.

## Object-Beschreibung für Wartungszeiträume

Die folgenden MaintenancePeriod-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8][HTML_TAG_9]Name[HTML_TAG_10][HTML_TAG_11]Beschreibung[HTML_TAG_12][HTML_TAG_13]Datentyp[HTML_TAG_14][HTML_TAG_15][HTML_TAG_16][HTML_TAG_17][HTML_TAG_18][HTML_TAG_19]Id[HTML_TAG_20][HTML_TAG_21]Die einzigartige Kennung des Wartungszeitraums[HTML_TAG_22][HTML_TAG_23]Integer[HTML_TAG_24][HTML_TAG_25][HTML_TAG_26][HTML_TAG_27]ScheduleMode[HTML_TAG_28][HTML_TAG_29]OneTime, Daily, Weekly oder Monthly[HTML_TAG_30][HTML_TAG_31]Enum[HTML_TAG_32][HTML_TAG_33][HTML_TAG_34][HTML_TAG_35]StartDateTime[HTML_TAG_36][HTML_TAG_37]Startdatum und -zeit (nur für einen einmal geplanten Zeitraum)[HTML_TAG_38][HTML_TAG_39]DateTime[HTML_TAG_40][HTML_TAG_41][HTML_TAG_42][HTML_TAG_43]EndDateTime[HTML_TAG_44][HTML_TAG_45]Enddatum und -zeit eines einmal geplanten Wartungszeitraums[HTML_TAG_46][HTML_TAG_47]DateTime[HTML_TAG_48][HTML_TAG_49][HTML_TAG_50][HTML_TAG_51]StartTime[HTML_TAG_52][HTML_TAG_53]Die Startzeit (“HH:mm”, eine 24-Stundennotation) eines sich wiederholenden (Daily, Weekly oder Monthly) Wartungszeitraums[HTML_TAG_54][HTML_TAG_55]String (“HH:mm”)[HTML_TAG_56][HTML_TAG_57][HTML_TAG_58][HTML_TAG_59]EndTime[HTML_TAG_60][HTML_TAG_61]Die Endzeit (“HH:mm”, eine 24-Stundennotation) eines sich wiederholenden (Daily, Weekly oder Monthly) Wartungszeitraums[HTML_TAG_62][HTML_TAG_63]String (“HH:mm”)[HTML_TAG_64][HTML_TAG_65][HTML_TAG_66][HTML_TAG_67]WeekDay[HTML_TAG_68][HTML_TAG_69]Der Tag der Woche für einen Wartungszeitraum[HTML_TAG_70]
(Sunday/Monday/[…]/Saturday)[HTML_TAG_71][HTML_TAG_72]Enum[HTML_TAG_73][HTML_TAG_74][HTML_TAG_75][HTML_TAG_76]MonthDay[HTML_TAG_77][HTML_TAG_78]Die Zahl des Tages für einen monatlichen Wartungszeitraum[HTML_TAG_79][HTML_TAG_80]Int (1-31)[HTML_TAG_81][HTML_TAG_82][HTML_TAG_83][HTML_TAG_84]MaintenanceType[HTML_TAG_85][HTML_TAG_86]DisableMonitoring (um das Prüfobjekt komplett zu deaktivieren) oder DisableNotifications (Monitoring wird weiterhin durchgeführt, aber Benachrichtigungen werden nicht gesendet)[HTML_TAG_87][HTML_TAG_88]Enum[HTML_TAG_89][HTML_TAG_90][HTML_TAG_91][HTML_TAG_92]

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

[HTML_TAG_93][HTML_TAG_94][HTML_TAG_95][HTML_TAG_96][HTML_TAG_97][HTML_TAG_98][HTML_TAG_99][HTML_TAG_100][HTML_TAG_101][HTML_TAG_102]Anfragetyp[HTML_TAG_103][HTML_TAG_104][HTML_TAG_105][HTML_TAG_106]Endpunkt[HTML_TAG_107][HTML_TAG_108][HTML_TAG_109][HTML_TAG_110]Einsatz[HTML_TAG_111][HTML_TAG_112][HTML_TAG_113][HTML_TAG_114][HTML_TAG_115][HTML_TAG_116][HTML_TAG_117]GET[HTML_TAG_118][HTML_TAG_119]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_120][HTML_TAG_121]Findet alle Wartungszeiträume für ein Prüfobjekt.[HTML_TAG_122][HTML_TAG_123][HTML_TAG_124][HTML_TAG_125]POST[HTML_TAG_126][HTML_TAG_127]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_128][HTML_TAG_129]Speichert den neuen angegebenen Wartungszeitraum für das spezifizierte Prüfobjekt[HTML_TAG_130][HTML_TAG_131][HTML_TAG_132][HTML_TAG_133]PUT[HTML_TAG_134][HTML_TAG_135]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_136]
{maintenancePeriodId}[HTML_TAG_137][HTML_TAG_138]Aktualisiert den spezifizierten Wartungszeitraum für das spezifizierte Prüfobjekt[HTML_TAG_139][HTML_TAG_140][HTML_TAG_141][HTML_TAG_142]DELETE[HTML_TAG_143][HTML_TAG_144]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_145]
{maintenancePeriodId}[HTML_TAG_146][HTML_TAG_147]Löscht den spezifizierten Wartungszeitraum für das spezifizierte Prüfobjekt[HTML_TAG_148][HTML_TAG_149][HTML_TAG_150][HTML_TAG_151]POST[HTML_TAG_152][HTML_TAG_153]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_154]
Cleanup/{beforeDate}[HTML_TAG_155][HTML_TAG_156]Löscht alle einmaligen Wartungszeiträume für das spezifizierte Prüfobjekt, die älter als das spezifizierte Datum sind[HTML_TAG_157][HTML_TAG_158][HTML_TAG_159][HTML_TAG_160]POST[HTML_TAG_161][HTML_TAG_162]MonitorGroup/{monitorGroupGuid}/[HTML_TAG_163]
MaintenancePeriod[HTML_TAG_164][HTML_TAG_165]Fügt den angegebenen Wartungszeitraum zu allen Prüfobjekten in der spezifizierten Gruppe hinzu[HTML_TAG_166][HTML_TAG_167][HTML_TAG_168][HTML_TAG_169]

### GET Monitor

[INLINE_CODE_1]

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

[INLINE_CODE_2]

Diese Methode erzeugt einen Wartungszeitraum, der im Abfragetext angegeben wurde und dem Prüfobjekt mit der angegebenen GUID zugewiesen wird.

Eine POST-Abfrage erwartet eine Objektstruktur wie in den Beispielen unter „Object-Beschreibung für Wartungszeiträume“ angegeben. Wie dort gezeigt ist die Struktur abhängig vom Wartungszeitraumtyp (OneTime, Daily, Weekly oder Monthly). Des Weiteren sollte das Feld „Id“ nicht angegeben sein. Ein neuer Id-Wert wird automatisch generiert.

### PUT Monitor

[INLINE_CODE_3]

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

[INLINE_CODE_4]

Diese Methode wird den Wartungszeitraum mit der in maintenancePeriodId spezifizierten Id aus dem Prüfobjekt mit der angegebenen monitorGuid löschen.

### POST Monitor

[INLINE_CODE_5]

Diese Methode wird alle **einmaligen** Zeitpläne mit einer vor dem in beforeDate angegebener StartDateTime aus dem Prüfobjekt mit der angegebenen monitorGuid entfernen.

### POST MonitorGroup

[INLINE_CODE_6]

Diese Methode wird den im Abfragetext angegebenen Wartungszeitraum zu allen Prüfobjekten der Prüfobjektgruppe mit der angegebenen Guid der Prüfobjektgruppe hinzufügen.

Erwartete Eingabe (Beispiel für einen wöchentlichen Wartungszeitraum):

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
