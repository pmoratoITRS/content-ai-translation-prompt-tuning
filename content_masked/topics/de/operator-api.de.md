{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operatoren.",
  "url": "[URL_BASE_TOPICS]api/operator-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Operator-Einstellungen, d.h. nutzerspezifischen Anmelde-Accounts. Methoden zur Änderung der Dienstpläne eines Operators werden in einem separaten Abschnitt beschrieben. Im letzten Abschnitt dieser Seite beschreiben wir die Zeitzonen-API, die möglicherweise zur Aktualisierung bestimmter Zeitzoneneinstellungen eines Operators erforderlich sind.

## Beschreibung des Operator-Objekts

Die folgenden Operator-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                     | Beschreibung                                                                                                                                                                                                                                                                             | Datentyp |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1]           | Die einzigartige Kennung des Operators                                                                                                                                                                                                                                                | Guid      |
| [INLINE_CODE_2]                  | Die primäre E-Mail-Adresse und Login-Name des Operators                                                                                                                                                                                                                                    | String    |
| [INLINE_CODE_3]               | Das Passwort des Operators                                                                                                                                                                                                                                                                | String    |
| [INLINE_CODE_4]               | Der vollständige Name des Operators                                                                                                                                                                                                                                                        | String    |
| [INLINE_CODE_5]            | Die Mobiltelefonnummer des Operators                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_6]    | Die ausgehende Telefonnummer des Operators                                                                                                                                                                                                                                                   | String    |
| [INLINE_CODE_7] | Zeigt an, ob der Operator der Administrator des Accounts ist. Dies ist ein schreibgeschütztes Feld                                                                                                                                                                                          | Boolean   |
| [INLINE_CODE_8]            | Die Ersatz-E-Mail-Adresse des Operators                                                                                                                                                                                                                                             | String    |
| [INLINE_CODE_9]               | Zeigt an, ob dieser Operator derzeit aktiv ist                                                                                                                                                                                                                                   | Boolean   |
| [INLINE_CODE_10]            | Sofern angegeben, stellt dies das Gebietsschema für den Operator ein. Mögliche Werte: en-US, en-GB, fr-FR, de-DE, nl-NL oder frei bleibend. Wenn dieser Wert frei bleibt, wird das übergeordnete Gebietsschema/die Sprache des Accounts verwendet                                                                                     | String    |
| [INLINE_CODE_11]             | Optional. Die ID für die Zeitzoneneinstellung dieses Nutzers. Verfügbare Werte werden in der Beschreibung zur Zeitzonen-API unten genannt. Falls nicht angegeben, wird für diesen Nutzer die Zeitzoneneinstellung des Accounts verwendet                                                                                  | Short     |
| [INLINE_CODE_12]            | Der SMS-Anbieter des Operators. Mögliche Werte: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| [INLINE_CODE_13]       | Wird der SMS-Anbieter speziell für diesen Operator konfiguriert, zeigt dieses Feld, ob ein numerischer Sender verwendet werden soll                                                                                                                                                         | Boolean   |
| [INLINE_CODE_14]          | Der für Telefonalarmierung verwendete Anbieter                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_15]       | Wenn für deinen Account ein nativer Login (Benutzername/Passwort) verfügbar und konfiguriert ist, zeigt dies an, ob dieser Operator berechtigt ist, sich bei Uptrends mit seinem Uptrends-Benutzernamen und -Passwort anzumelden. Mögliche Werte: True, False oder frei bleibend, um die allgemeinen Account-Einstellungen zu verwenden | Boolean   |
| [INLINE_CODE_16]      | Wenn für deinen Account Single Sign-on verfügbar und konfiguriert ist, zeigt dies an, ob dieser Operator berechtigt ist, Single Sign-on zu nutzen. Mögliche Werte: True, False oder frei bleibend, um die allgemeinen Account-Einstellungen zu verwenden                                                               | Boolean   |

## Operator-Endpunkte

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Operatoren verfügbar.

| Anfragetyp | Endpunkt                                                 | Einsatz                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_17]                                              | Ruft alle Operatoren ab                                                                                               |
| GET          | [INLINE_CODE_18]                               | Ruft Informationen zu einem Operator ab                                                                                  |
| POST         | [INLINE_CODE_19]                                              | Erstellt einen neuen Operator                                                                                           |
| PUT          | [INLINE_CODE_20]                               | Aktualisiert einen bestehenden Operator                                                                                     |
| DELETE       | [INLINE_CODE_21]                               | Löscht einen bestehenden Operator. Hinweis: Ein mit dem verwendeten API-Account verbundener Operator kann nicht gelöscht werden |
| GET          | [INLINE_CODE_22]                  | Ruft den Dienstplan eines bestehenden Operators ab                                                                 |
| POST         | [INLINE_CODE_23]                  | Fügt einen Dienstplan zu einem bestehenden Operator hinzu                                                                    |
| PUT          | [INLINE_CODE_24] | Aktualisiert den angegebenen Dienstplan                                                                              |
| DELETE       | [INLINE_CODE_25] | Löscht den angegebenen Dienstplan                                                                              |

#### GET Operator

Diese GET-Anfrage ergibt eine Sammlung mit allen Operatoren, einschließlich des Account-Administrators.

[INLINE_CODE_26]

#### GET Operator/{operatorGuid}

Diese GET-Anfrage ergibt die Informationen für den durch die Operator GUID spezifizierten Operator.

Beispiel-Ausgabe:

[INLINE_CODE_27]

#### POST Operator

Diese Eingabe dient der Erstellung eines neuen Operators mit den bereitgestellten Informationen.

Beispiel-Eingabe:

[INLINE_CODE_28]

Die Antwort enthält den erstellten Operator, einschließlich der zugewiesenen Operator GUID:

[INLINE_CODE_29]

#### PUT Operator/{operatorGuid}

Diese Methode aktualisiert den durch die Operator GUID spezifizierten Operator mit den Daten, die in der Anfrage übermittelt werden.

Beispiel-Eingabe:

[INLINE_CODE_30]

#### DELETE Operator/{operatorGuid}

Diese Methode löscht den durch die Operator GUID spezifizierten Operator mit den Daten, die in der Anfrage übermittelt werden.

## Beschreibung des Operator-Dienstplan-Objekts

| Name            | Beschreibung                                                                                               | Datentyp |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_31]            | Die einzigartige Kennung dieses Dienstplans Dieses Feld ist schreibgeschützt und wird automatisch generiert | Guid      |
| [INLINE_CODE_32]  | Der Dienstplan-Modus. Mögliche Werte: OneTime, Daily, Weekly, Monthly                                       | String    |
| [INLINE_CODE_33] | Startdatum und -zeit (für einen einmaligen Plan)                                                         | DateTime  |
| [INLINE_CODE_34]   | Enddatum und -zeit (für einen einmaligen Plan)                                                           | DateTime  |
| [INLINE_CODE_35]       | Der Tag der Woche (für einen wöchentlichen Plan) Mögliche Werte: Monday, Tuesday, ..., Sunday               | String    |
| [INLINE_CODE_36]      | Der Tag im Monat (für einen monatlichen Plan)                                                            | Int       |
| [INLINE_CODE_37]     | Die Startzeit (für einen täglichen, wöchentlichen oder monatlichen Plan). Format: “HH:mm”, 24-Stunden-Format             | String    |
| [INLINE_CODE_38]       | Die Endzeit (für einen täglichen, wöchentlichen oder monatlichen Plan).  Format: “HH:mm”, 24-Stunden-Format               | String    |

## Endpunkte für den Operator-Dienstplan

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Dienstplänen für einen bestimmten Operator verfügbar:

#### GET Operator/{operatorGuid}/DutySchedule

Diese Methode ergibt eine Sammlung mit allen Dienstplänen für den angegebenen Operator.

Beispiel-Ausgabe:

[INLINE_CODE_39]

#### POST Operator/{operatorGuid}/DutySchedule

Diese Methode erstellt einen neuen Dienstplan für den angegebenen Operator.

Beispiel-Eingabe (für einen wöchentlichen Plan):

[INLINE_CODE_40]

Wie du an diesem Beispiel siehst, werden nur die Parameter erwartet, die für den zu erstellenden Dienstplan relevant sind. Beispielsweise ist MonthDay für einen wöchentlichen Plan nicht relevant und StartDateTime und EndDateTime werden nur für einmalige Pläne benötigt.

Ein täglicher Plan erwartet keinen Wert für Wochentage, lediglich den ScheduleMode „Daily“ und eine Start- und Endzeit. Genauso erwartet ein monatlicher Dienstplan nur die Eingabe ScheduleMode „Monthly“, den Tag im Monat sowie die Start- und Endzeit.

Wenn du einen neuen Dienstplan einrichtest, enthält die Ausgabe die ID des neuen Plans. Beispiel-Ausgabe für einen täglichen Zeitplan:

[INLINE_CODE_41]

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Diese Methode aktualisiert den Dienstplan mit der angegebenen Dienstplan-ID für den angegebenen Operator. Beispiel-Eingabe:

[INLINE_CODE_42]

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Diese Methode löscht den Dienstplan mit der angegebenen Dienstplan-ID für den angegebenen Operator.

## Beschreibung des Zeitzonen-Objekts

| Name                   | Beschreibung                                                                                      | Datentyp |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_43]           | Die einzigartige Kennung der Zeitzone                                                         | Short     |
| [INLINE_CODE_44]          | Die Beschreibung für diese Zeitzone                                                               | String    |
| [INLINE_CODE_45]        | Die Abweichung zum UTC in Minuten                                                                   | Short     |
| [INLINE_CODE_46]    | Angabe, ob die Zeitzone Sommerzeit wiedergibt                                            | Boolean   |
| [INLINE_CODE_47] | Die Abweichung in Minuten zur Sommerzeit. Wird nicht angegeben, wenn HasDaylightSaving „false“ ist | Short     |

## Zeitzonen-Endpunkte

Anhand der folgenden Methoden können die Zeitzonen-Daten abgerufen werden. Du kannst diese Daten nutzen, um die zu verwendende Zeitzone zu bestimmen, wenn du die Zeitzonen-ID für die Operator-Einstellungen angeben möchtest.

#### GET Timezone

Diese GET-Anfrage ergibt eine Sammlung mit allen Zeitzonen.

Beispiel-Ausgabe:

[INLINE_CODE_48]

#### GET Timezone/{timezoneId}

Diese Methode ruft die Zeitzonendaten für die Zeitzone mit der angegebenen ID ab.

Beispiel-Ausgabe:

[INLINE_CODE_49]
