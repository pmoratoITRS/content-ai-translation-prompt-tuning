{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operatoren.",
  "url": "/support/kb/api/operator-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-api"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Operator-Einstellungen, d.h. nutzerspezifischen Anmelde-Accounts. Methoden zur Änderung der Dienstpläne eines Operators werden in einem separaten Abschnitt beschrieben. Im letzten Abschnitt dieser Seite beschreiben wir die Zeitzonen-API, die möglicherweise zur Aktualisierung bestimmter Zeitzoneneinstellungen eines Operators erforderlich sind.

## Beschreibung des Operator-Objekts

Die folgenden Operator-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                     | Beschreibung                                                                                                                                                                                                                                                                             | Datentyp |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| `OperatorGuid`           | Die einzigartige Kennung des Operators                                                                                                                                                                                                                                                | Guid      |
| `Email`                  | Die primäre E-Mail-Adresse und Login-Name des Operators                                                                                                                                                                                                                                    | String    |
| `Password`               | Das Passwort des Operators                                                                                                                                                                                                                                                                | String    |
| `FullName`               | Der vollständige Name des Operators                                                                                                                                                                                                                                                        | String    |
| `MobilePhone`            | Die Mobiltelefonnummer des Operators                                                                                                                                                                                                                                                     | String    |
| `OutgoingPhoneNumber`    | Die ausgehende Telefonnummer des Operators                                                                                                                                                                                                                                                   | String    |
| `IsAccountAdministrator` | Zeigt an, ob der Operator der Administrator des Accounts ist. Dies ist ein schreibgeschütztes Feld                                                                                                                                                                                          | Boolean   |
| `BackupEmail`            | Die Ersatz-E-Mail-Adresse des Operators                                                                                                                                                                                                                                             | String    |
| `IsOnDuty`               | Zeigt an, ob dieser Operator derzeit aktiv ist                                                                                                                                                                                                                                   | Boolean   |
| `CultureName`            | Sofern angegeben, stellt dies das Gebietsschema für den Operator ein. Mögliche Werte: en-US, en-GB, fr-FR, de-DE, nl-NL oder frei bleibend. Wenn dieser Wert frei bleibt, wird das übergeordnete Gebietsschema/die Sprache des Accounts verwendet                                                                                     | String    |
| `TimeZoneId`             | Optional. Die ID für die Zeitzoneneinstellung dieses Nutzers. Verfügbare Werte werden in der Beschreibung zur Zeitzonen-API unten genannt. Falls nicht angegeben, wird für diesen Nutzer die Zeitzoneneinstellung des Accounts verwendet                                                                                  | Short     |
| `SmsProvider`            | Der SMS-Anbieter des Operators. Mögliche Werte: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| `UseNumericSender`       | Wird der SMS-Anbieter speziell für diesen Operator konfiguriert, zeigt dieses Feld, ob ein numerischer Sender verwendet werden soll                                                                                                                                                         | Boolean   |
| `PhoneProvider`          | Der für Telefonalarmierung verwendete Anbieter                                                                                                                                                                                                                                                     | String    |
| `AllowNativeLogin`       | Wenn für deinen Account ein nativer Login (Benutzername/Passwort) verfügbar und konfiguriert ist, zeigt dies an, ob dieser Operator berechtigt ist, sich bei Uptrends mit seinem Uptrends-Benutzernamen und -Passwort anzumelden. Mögliche Werte: True, False oder frei bleibend, um die allgemeinen Account-Einstellungen zu verwenden | Boolean   |
| `AllowSingleSignon`      | Wenn für deinen Account Single Sign-on verfügbar und konfiguriert ist, zeigt dies an, ob dieser Operator berechtigt ist, Single Sign-on zu nutzen. Mögliche Werte: True, False oder frei bleibend, um die allgemeinen Account-Einstellungen zu verwenden                                                               | Boolean   |

## Operator-Endpunkte

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Operatoren verfügbar.

| Anfragetyp | Endpunkt                                                 | Einsatz                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | `/Operator`                                              | Ruft alle Operatoren ab                                                                                               |
| GET          | `/Operator/{operatorGuid}`                               | Ruft Informationen zu einem Operator ab                                                                                  |
| POST         | `/Operator`                                              | Erstellt einen neuen Operator                                                                                           |
| PUT          | `/Operator/{operatorGuid}`                               | Aktualisiert einen bestehenden Operator                                                                                     |
| DELETE       | `/Operator/{operatorGuid}`                               | Löscht einen bestehenden Operator. Hinweis: Ein mit dem verwendeten API-Account verbundener Operator kann nicht gelöscht werden |
| GET          | `/Operator/{operatorGuid}/DutySchedule`                  | Ruft den Dienstplan eines bestehenden Operators ab                                                                 |
| POST         | `/Operator/{operatorGuid}/DutySchedule`                  | Fügt einen Dienstplan zu einem bestehenden Operator hinzu                                                                    |
| PUT          | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Aktualisiert den angegebenen Dienstplan                                                                              |
| DELETE       | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Löscht den angegebenen Dienstplan                                                                              |

#### GET Operator

Diese GET-Anfrage ergibt eine Sammlung mit allen Operatoren, einschließlich des Account-Administrators.

`[  {  "OperatorGuid": "36fad910-6e9f-4886-b1a7-9b4637362cb8",  "FullName": "First Operator",  "Email": "FirstOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": true,  "BackupEmail": " FirstOperator@gmail.com ",  "IsOnDuty": true,  "SmsProvider": "UseAccountSetting",  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  },  {  "OperatorGuid": "23a75d1f-0dec-4963-86d8-0cee21267db4",  "UserName": "SecondOperator@acme.com",  "FullName": "Second Operator",  "Email": "SecondOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "SmsProvider": "SmsProviderEurope",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  }  ] `

#### GET Operator/{operatorGuid}

Diese GET-Anfrage ergibt die Informationen für den durch die Operator GUID spezifizierten Operator.

Beispiel-Ausgabe:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true  "AllowSingleSignon": false  } `

#### POST Operator

Diese Eingabe dient der Erstellung eines neuen Operators mit den bereitgestellten Informationen.

Beispiel-Eingabe:

`{  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

Die Antwort enthält den erstellten Operator, einschließlich der zugewiesenen Operator GUID:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### PUT Operator/{operatorGuid}

Diese Methode aktualisiert den durch die Operator GUID spezifizierten Operator mit den Daten, die in der Anfrage übermittelt werden.

Beispiel-Eingabe:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### DELETE Operator/{operatorGuid}

Diese Methode löscht den durch die Operator GUID spezifizierten Operator mit den Daten, die in der Anfrage übermittelt werden.

## Beschreibung des Operator-Dienstplan-Objekts

| Name            | Beschreibung                                                                                               | Datentyp |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `Id`            | Die einzigartige Kennung dieses Dienstplans Dieses Feld ist schreibgeschützt und wird automatisch generiert | Guid      |
| `ScheduleMode`  | Der Dienstplan-Modus. Mögliche Werte: OneTime, Daily, Weekly, Monthly                                       | String    |
| `StartDateTime` | Startdatum und -zeit (für einen einmaligen Plan)                                                         | DateTime  |
| `EndDateTime`   | Enddatum und -zeit (für einen einmaligen Plan)                                                           | DateTime  |
| `WeekDay`       | Der Tag der Woche (für einen wöchentlichen Plan) Mögliche Werte: Monday, Tuesday, ..., Sunday               | String    |
| `MonthDay`      | Der Tag im Monat (für einen monatlichen Plan)                                                            | Int       |
| `StartTime`     | Die Startzeit (für einen täglichen, wöchentlichen oder monatlichen Plan). Format: “HH:mm”, 24-Stunden-Format             | String    |
| `EndTime`       | Die Endzeit (für einen täglichen, wöchentlichen oder monatlichen Plan).  Format: “HH:mm”, 24-Stunden-Format               | String    |

## Endpunkte für den Operator-Dienstplan

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Dienstplänen für einen bestimmten Operator verfügbar:

#### GET Operator/{operatorGuid}/DutySchedule

Diese Methode ergibt eine Sammlung mit allen Dienstplänen für den angegebenen Operator.

Beispiel-Ausgabe:

`[  {  "Id": 2272,  "ScheduleMode": "Weekly",  "WeekDay": "Monday",  "StartTime": "08:00",  "EndTime": "16:30"  },  {  "Id": 2267,  "ScheduleMode": "Monthly",  "MonthDay": 15  "StartTime": "08:00",  "EndTime": "16:30"  }  ] `

#### POST Operator/{operatorGuid}/DutySchedule

Diese Methode erstellt einen neuen Dienstplan für den angegebenen Operator.

Beispiel-Eingabe (für einen wöchentlichen Plan):

`{  "ScheduleMode": "Weekly",  "WeekDay": "Thursday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

Wie du an diesem Beispiel siehst, werden nur die Parameter erwartet, die für den zu erstellenden Dienstplan relevant sind. Beispielsweise ist MonthDay für einen wöchentlichen Plan nicht relevant und StartDateTime und EndDateTime werden nur für einmalige Pläne benötigt.

Ein täglicher Plan erwartet keinen Wert für Wochentage, lediglich den ScheduleMode „Daily“ und eine Start- und Endzeit. Genauso erwartet ein monatlicher Dienstplan nur die Eingabe ScheduleMode „Monthly“, den Tag im Monat sowie die Start- und Endzeit.

Wenn du einen neuen Dienstplan einrichtest, enthält die Ausgabe die ID des neuen Plans. Beispiel-Ausgabe für einen täglichen Zeitplan:

`{  "Id": 2272,  "ScheduleMode": "Daily",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Diese Methode aktualisiert den Dienstplan mit der angegebenen Dienstplan-ID für den angegebenen Operator. Beispiel-Eingabe:

`{  "Id": 2273,  "ScheduleMode": "Weekly",  "WeekDay": "Wednesday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Diese Methode löscht den Dienstplan mit der angegebenen Dienstplan-ID für den angegebenen Operator.

## Beschreibung des Zeitzonen-Objekts

| Name                   | Beschreibung                                                                                      | Datentyp |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| `TimeZoneId`           | Die einzigartige Kennung der Zeitzone                                                         | Short     |
| `Description`          | Die Beschreibung für diese Zeitzone                                                               | String    |
| `OffsetFromUtc`        | Die Abweichung zum UTC in Minuten                                                                   | Short     |
| `HasDaylightSaving`    | Angabe, ob die Zeitzone Sommerzeit wiedergibt                                            | Boolean   |
| `DaylightSavingOffset` | Die Abweichung in Minuten zur Sommerzeit. Wird nicht angegeben, wenn HasDaylightSaving „false“ ist | Short     |

## Zeitzonen-Endpunkte

Anhand der folgenden Methoden können die Zeitzonen-Daten abgerufen werden. Du kannst diese Daten nutzen, um die zu verwendende Zeitzone zu bestimmen, wenn du die Zeitzonen-ID für die Operator-Einstellungen angeben möchtest.

#### GET Timezone

Diese GET-Anfrage ergibt eine Sammlung mit allen Zeitzonen.

Beispiel-Ausgabe:

`[  {  "TimezoneId": 1,  "Description": "GMT-04:00# Brazil West, Chile, Paraguay",  "OffsetFromUtc": -240,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 2,  "Description": "GMT\+06:00# Cocos Islands",  "OffsetFromUtc": 360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 3,  "Description": "GMT\+01:00 West Central Africa",  "OffsetFromUtc": 60,  "HasDaylightSaving": false  }  // (there will be many more)  ]`

#### GET Timezone/{timezoneId}

Diese Methode ruft die Zeitzonendaten für die Zeitzone mit der angegebenen ID ab.

Beispiel-Ausgabe:

`{  "TimezoneId": 56,  "Description": "GMT-06:00* Central time",  "OffsetFromUtc": -360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  }`
