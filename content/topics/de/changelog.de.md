{
  "hero": {
    "title": "API Changelog"
  },
  "title": "API Changelog",
  "summary": "Lies über die Änderungen, Aktualisierungen und Verbesserungen der Uptrends API",
  "url": "/support/kb/api/changelog",
  "translationKey": "https://www.uptrends.com/support/kb/api/changelog",
  "type": "story" 
}

{{< Features/Story >}}

Die Funktionen der Uptrends API werden mit der Zeit verbessert und erweitert. Dementsprechend werden wir neue Endpunkte und Methoden für neue Funktionen hinzufügen.

Bei der Einrichtung neuer Funktionen achten wir darauf, immer rückwärtskompatibel zu bleiben. Änderungen sind jedoch nicht immer vermeidbar und eine neue Version der API wird eventuell nicht mit dem Code kompatibel sein, den du bisher geschrieben und genutzt hast. Schaue regelmäßig im API Changelog nach, um über alle Änderungen auf dem Laufenden zu sein und diese, falls notwendig, zu berücksichtigen.

Zur Dokumentation der API lies unsere Artikel in der Kategorie [Uptrends API]({{< ref path="support/kb/api" lang="de" >}}).

Sollten dich die Änderungen an der Uptrends Anwendung interessieren, schaue in unserem [allgemeinen Changelog]({{< ref path="/changelog" lang="de" >}}) nach.

## Mai 2025

### Neue Code-relevante Änderung: auslaufende API-Felder

Im Rahmen unserer laufenden Bemühungen, die Uptrends API zu optimieren, werden bestimmte Felder bei den folgenden [Prüfobjekt](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor)-Endpunkten ab **27. August 2025** nicht fortgeführt:

- `GET` und `POST` `/Monitor`
- `GET`, `PUT` und `PATCH` `/Monitor/{monitorGuid}`
- `GET` und `POST` `/Monitor/MonitorGroup/{monitorGroupGuid}`

Die folgenden nicht fortgesetzten Felder werden nun als [Fehlerbedingungstypen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview" lang="de" >}}) unter dem Array `ErrorConditions` behandelt. Zugehörige Felder werden in einen einzelnen Eintrag zusammengeführt und ersetzen die vorherige Nutzung als eigenes Feld:

| Nicht fortgesetzte Felder | Ersetzt mit Feld |
|--|--|
| `AlertOnLoadTimeLimit1`, `LoadTimeLimit1`| {{< tableformatter >}} [LoadTimeLimit1]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) |
| `AlertOnLoadTimeLimit2`, `LoadTimeLimit2` | [LoadTimeLimit2]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) |
|`AlertOnMaximumBytes`, `MaximumBytes` | [TotalMaxBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="de" >}}) |
|`AlertOnMinimumBytes`, `MinimumBytes` | [TotalMinBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="de" >}}) | 
|`AlertOnMaximumSize`, `ElementMaximumSize` | [PageElementMaxSizeWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="de" >}}) |
|`AlertOnPercentageFail`, `FailedObjectPercentage` | [PageElementFailedWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="de" >}})
|`ExpectedHttpStatusCode`, `ExpectedHttpStatusCodeSpecified` | [HttpStatus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="de" >}}) |

Unten ist ein Beispiel einer aktualisierten API-Antwort. Es empfiehlt sich, deine API-Aufrufe anzupassen, sodass sie das `ErrorConditions`-Array enthalten. Das entspricht der neuesten API-Struktur und gewährleistet eine korrekte API-Funktion.

```json
{
  ...
  "ErrorConditions": [
    {
      "ErrorConditionType": "LoadTimeLimit1",
      "Value": "2500",
      "Effect": "Indicate"
    },
    {
      "ErrorConditionType": "LoadTimeLimit2",
      "Value": "5000",
      "Effect": "Error"
    },
    {
      "ErrorConditionType": "TotalMaxBytes",
      "Value": "5000000"
    },
    {
      "ErrorConditionType": "TotalMinBytes",
      "Value": "5000"
    },
    {
      "ErrorConditionType": "PageElementMaxSizeWithPercentage",
      "Value": "200000",
      "Percentage": "10"
    },
    {
      "ErrorConditionType": "PageElementFailedWithPercentage",
      "Percentage": "10"
    },
    { "ErrorConditionType": "HttpStatus",       
      "Value": "200"     
    }
  ],
 ...
}
```

### Private Checkpoint-Status-Update

Der Endpunkt `GET /PrivateCheckpointHealth` gibt nun das Feld `Warnings` aus, das alle Alarminformationen zum Checkpoint des Servers enthält. Weitere Informationen findest du in der [Uptrends API v4 Private Locations Checkpoint Status Dokumentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/PrivateLocation/PrivateLocation_GetSpecifiedPrivateCheckpointHealth).

## April 2025

### Einführung der Private Locations API

Wir haben ein neues Set an API-Endpunkten aufgenommen, damit du die Konfiguration deiner Private Locations besser handhaben kannst. Das umfasst den Status und Checkpoint-Informationen. Weitere Informationen findest du in der [Uptrends API v4 Private Locations Dokumentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json).

## März 2025

### Update MonitorGroup API 

Der Endpunkt `/MonitorGroup` gibt nun die Anzahl Credits pro [Prüfobjekttyp]({{< ref path="/support/kb/basics/monitor-types" lang="de" >}}) aus:
- `UsedBasicMonitorQuota` – gibt die Anzahl genutzter Credits für [Uptime- bzw. Basic-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}) aus.
- `UsedBrowserMonitorQuota` – gibt die Anzahl genutzter Credits für [Browser- bzw. Full-Page Check (FPC)-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}) aus.
- `UsedTransactionMonitorQuota` – gibt die Anzahl genutzter Credits für [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) aus.
- `UsedApiMonitorQuota` – gibt die Anzahl genutzter Credits für [Multi-Step API (MSA)-]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) und [Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="de" >}})-Prüfobjekte aus.

Zuvor gab die MonitorGroup API nur die Gesamtzahl verfügbarer Credits der Gruppe für jede Prüfobjektkategorie aus. Jetzt wird auch die Anzahl genutzter Credits der Gruppe für jede Prüfobjektkategorie angegeben.

## Februar 2025

### Cursor-Parameter-Wert – Update

Der API Cursor-Parameter ist ein Zeichenkettenwert, der als Zeiger funktioniert, um Daten aus der API-Antwort zu übergehen.

Cursor wurden nun in ein längeres Zeichenkettenformat aktualisiert, um eine sicherere Datenhandhabung zu gewährleisten. Alle neu erstellten Cursor haben nun das neue Format. Die alten Cursor-Formate werden weiterhin bis 1. April 2025 funktionieren. Danach können die alten Cursor nicht mehr verwendet werden. Es wird empfohlen, neue Cursor-Werte zu erzeugen, damit sie aktuell sind und wie erwartet funktionieren.

Beachte, dass der Cursor-Parameter an den Endpunkten der [Monitor Check API]({{< ref path="/support/kb/api/monitorcheck-api" lang="de" >}}) und Alert API verfügbar ist.

## Januar 2025

### Update Monitor API

Der Endpunkt `/Monitor` gibt nun `LastModifiedDate` aus, was Datum und Uhrzeit der letzten Aktualisierung des Prüfobjekts enthält. Zuvor konnte nur `CreatedDate` mit der Monitor API abgerufen werden.

## November 2024

### VaultItem – Update

`POST/v4/VaultItem`, `PUT/v4/VaultItem/{vaultItemGuid}` und `PATCH/v4/VaultItem/{vaultItemGuid}` akzeptieren nun das Feld `SecretEncodingMethod`, wenn das Vault Item [One-Time Passwort Konfiguration]({{< ref path="/support/kb/account/vault#one-time-password" lang="de" >}}) erstellt oder aktualisiert wird. Das neue Feld akzeptiert *Hex*- oder *Base32*-Zeichenfolgen als Wert. Das Base32-Format ist die Standardverschlüsselungsmethode, wenn das „SecretEncodingMethod‟-Feld nicht definiert ist.

## September 2024

### VaultItem – Update

`GET /v4/VaultItem` gibt nun ein zusätzliches Datenelement, `VaultItemUsedBy` aus. Es enthält Informationen darüber, welche Elemente oder Prüfobjekte jedes Vault Item verwenden.

## August 2024

### Checkpoints API

Der API-Endpunkt `/Checkpoint/Server/{serverId}` gibt nun auch Server privater Standorte an.

### VaultItem – Update

Der Endpunkt `GET /v4/VaultItem` kann nun genauso viele Daten für jedes Vault Item zurückgeben, ähnlich wie Daten für ein einzelnes Item über `GET /v4/VaultItem/{GUID}` ausgegeben werden.

## Juni 2024

### Code-relevante Änderung: die /Register API für Operatoren, die sich nur per SSO anmelden

Für die Uptrends API ist eine [Registrierung]({{< ref path="/support/kb/api/authentication-v4" lang="de" >}}) erforderlich, bevor sie genutzt werden kann. Operatoren können eine Reihe API-spezifischer Anmeldedaten erzeugen, basierend auf ihren üblichen Uptrends Anmeldedaten. Es gibt zwei Möglichkeiten, eine Reihe von API-Anmeldedaten zu registrieren:

– Operatoren können über die normale Uptrends Benutzeroberfläche einen API-Nutzer auf der Registerkarte {{< AppElement type="tab" >}}API-Management{{< /AppElement >}} in den Operator-Einstellungen hinzufügen.
– Alternativ können sich Operatoren in der API selbst für Anmeldedaten registrieren, in dem sie eine `POST /Register`-Anfrage unter Angabe ihrer regulären Uptrends Anmeldedaten eingeben.

Ab diesem Update steht Operatoren, die sich nur mit [Single Sign-on (SSO) anmelden können]({{< ref path="/support/kb/account/settings/single-sign-on-overview" lang="de" >}}), die zweite Möglichkeit, sich für API-Anmeldedaten zu registrieren, nicht mehr zur Verfügung, da sie keine „regulären“ Uptrends Anmeldedaten haben. 

In diesem Fall empfehlen wir, einen separaten Operator-Account einzurichten und diesen zur Registrierung für API-Anmeldedaten zu verwenden. 

## Oktober 2023

### Code-relevante Änderung: Metrik Seitenladezeiten für browserbasiertes Monitoring

**Hinweis:** Das Folgende ist eine **code-relevante Änderung** für die *MonitorCheck* API. Die Änderung ist ab **Mittwoch, 8. November** in Kraft.

Die Uptrends [MonitorCheck API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorCheck) kann verwendet werden, um detaillierte Informationen zu den einzelnen Überwachungen der Prüfobjekte abzurufen. Für das browserbasierte Monitoring kann das [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}) über den Befehl `GET/MonitorCheck/{monitorCheckId}/Waterfall` abgerufen werden. Dies gibt alle Wasserfall-Messwerte wieder, einschließlich [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}) und [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}), sofern sie in den Prüfergebnissen enthalten sind. 

Derzeit gibt die MonitorCheck API Core Web Vitals und W3C Navigation Timings in zwei getrennten JSON-Objekten aus: `PageLoadMetrics` und `W3CNavigationTiming`. Zukünftig werden diese beiden Objekte zu einem einzelnen Array, `PageLoadMetricsCollection`, wie folgt kombiniert:

```json
  "Attributes": {
    "PageLoadMetricsCollection": [
      {
        "CumulativeLayoutShift": 0.029,
        "FirstContentfulPaint": 2914,
        "LargestContentfulPaint": 3014,
        "TotalBlockingTime": 819,
        "TimeToInteractive": 12516,
        "TimeToFirstByte": 2068,
        "SendStart": 2059,
        "LoadEventEnd": 6721,
        "DomInteractive": 2652,
        "DomComplete": 6719
      }
    ],
    ...
  }
```


### Variablen von Meldedefinitionen über die API angeben

Bei der Konfiguration der [Alarmierung]({{< ref path="/support/kb/alerting" lang="de" >}}) über eine [benutzerdefinierte Integration]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="de" >}}) in Uptrends können Operatoren die Benutzeroberfläche verwenden, um bestimmte erforderliche Variablen [in der Eskalationsstufe der Meldedefinition]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#specifying-variables-per-escalation-level" lang="de" >}}) anzugeben, statt diese in den Optionen der Integration einzurichten. Damit können Nutzer eine einzige Integration für verschiedene Szenarien einsetzen, zum Beispiel Warnmeldungen für unterschiedliche Prüfobjekte an verschiedene Teams, aber mit demselben Nachrichteninhalt.

Wenn die Option zur Angabe von Variablen in der Eskalationsstufe in den Integrationseinstellungen aktiviert wird, müssen die Variablen stattdessen bei der Einrichtung der Integration bei den Einstellungen der Meldedefinition konfiguriert werden. Dafür erscheint ein zusätzliches Textfeld in der Liste zur Auswahl der Integration in den Meldedefinitionseinstellungen. 

Bisher war diese Option bei der Konfiguration von Meldedefinitionen über die API nicht verfügbar. Wir haben eine neue Option zur Abfrage `/AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration` (mit der du angibst, welche Integrationen zu welcher Eskalationsstufe der Meldedefinition gehören) hinzugefügt. Das neue Merkmal lautet:

```json
{
    ...
    "VariableValues": {
        "ApiUrl": "https://api.escalationlevel-specific-url.com/alerts"
    },
    ...
}
```

Dieses Merkmal ist äquivalent mit der Option in der Benutzeroberfläche der Anwendung:

![Konfigurieren einer Integrationsvariable in einer Meldedefinition](/img/content/scr-api-cl-conf-variables-in-escalation-level.min.png)


## September 2023

### Änderung: IPv6-Adressen von Checkpoints

Zuvor wurden bei der Nutzung der Checkpoint API zum Abrufen von Checkpoint-Informationen die IPv4-Adressen des Checkpoints als einfache Liste in einem Array angezeigt. Die IPv6-Adressen (sofern vorhanden) waren eine Liste von Objekten. Beispielsweise wurden die IP-Adressen des Checkpoints Amsterdam früher wie folgt gelistet:

```json
     "IpV4Addresses": [
        "178.217.84.4",
        "188.241.149.95",
        "66.212.22.2",
        "185.145.63.225",
        "5.182.210.227",
        "5.182.210.168"
    ],
    "IpV6Addresses": [
        {
            "IpAddress": "2a01:5cc0:1:2::4"
        },
        {
            "IpAddress": "2607:fcd0:cd40:1400::2"
        }
    ],
```

Uptrends hat dies nun vereinheitlicht und gibt IPv6-Adressen auf dieselbe Weise an:

```json
    "IpV6Addresses": [
        "2a01:5cc0:1:2::4",
        "2607:fcd0:cd40:1400::2",
    ],
```

Beachte bitte, dass dies bei einem automatisierten Abruf von Checkpoint-IP-Adressen, z. B. für Whitelists, eine **code-relevante Änderung** sein kann.

## Januar 2023

Version 3 unserer API wird seit Januar 2023 nicht länger unterstützt und wurde deaktiviert. Die [Dokumentation zu Version 3]({{< ref path="/support/kb/api" lang="de" >}}) ist noch in unserer Knowledge Base zu finden, aber diese API-Version selbst wird nicht mehr funktionieren. Wenn du noch aktive Skripte oder Prozesse hast, die API Version 3 verwenden, werden diese einen Fehler melden, und wir empfehlen, so bald wie möglich zu Version 4 zu wechseln. Der [Upgrade-Leitfaden]({{< ref path="/support/kb/api" lang="de" >}}) enthält weitere Infos zum Wechsel von API v3 nach API v4.

**Update Mai 2023:** Die Dokumentation für Version 3 unserer API wurde entfernt und kann nicht mehr aufgerufen werden. 

## Dezember 2022

### Erstellungsdatum mithilfe der API überwachen

Der [/Monitor Endpunkt](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) kann unter anderem verwendet werden, um die Prüfobjektdefinitionen deines Accounts (über *GET /Monitor/{monitorGuid}*) abzurufen. Die Antwort wird nun auch ein `CreatedDate` enthalten, welches angibt, wann das Prüfobjekt eingerichtet wurde.


## November 2022

### Kleine Änderungen am /Register Endpunkt

Wie du vielleicht [über unser reguläres Changelog]({{< ref path="/changelog" lang="de" >}}) erfahren hast, haben wir mit diesem Release die Option hinzugefügt [Uptrends API Anmeldedaten über die Benutzeroberfläche zu erstellen und zu entfernen]({{< ref path="/changelog#2022-11-manage-uptrends-api-credentials-via-ui" lang="de" >}}). Um Uptrends API v4 mit der Benutzeroberfläche in Einklang zu bringen, haben wir zum /Register Endpunkt zwei neue Optionen hinzugefügt:

– Es ist jetzt möglich, wahlweise eine Beschreibung bei der Registrierung eines neuen API-Accounts über das Feld `Description` einzugeben.
– Es ist jetzt möglich, einen API-Account für einen anderen Operatoren zu erstellen, sofern der anfragende Operator über ausreichend Rechte verfügt, indem er das Feld `operatorGuid` verwendet.

## September 2022

### Bevorstehende Änderung: Zeitstempel bei der API-Antwort

Derzeit werden Zeitstempel, die Teil der Antwort bei einer [API v4]({{< ref path="/support/kb/api" lang="de" >}})-Abfrage sind, auf zwei Weisen in JSON konvertiert:

– Millisekundenzählung ist gleich 0:  _2022-09-21T13:08:47_
– Millisekundenzählung ist nicht gleich 0: _2022-09-21T13:08:47<b>.682</b>_

Dieser Unterschied kann zu Problemen führen, wenn Daten mit diesen Zeitstempeln automatisch geparst und verarbeitet werden. Daher gibt es nun eine Änderung: Die Millisekunden werden nicht mehr in den Zeitstempeln einer API-Antwort angezeigt. Zukünftig werden alle Zeitstempel das Format _2022-09-21T13:08:47_ haben.

## Juni 2022

### Zukünftig neue IP-Adressen von Checkpoints 

Die Uptrends API kann für einen Abruf von Checkpoint-IP-Adressen, z. B. für automatisierte Whitelists, genutzt werden. Zuvor enthielten Antworten zu solchen Anfragen hinsichtlich unserer [Checkpoint API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Checkpoint) in der Regel eine aktuelle Liste aller derzeitigen Checkpoint-IP-Adressen. Uptrends’ Checkpoint-Netzwerk ist jedoch laufend Änderungen unterworfen. Neue Checkpoints werden hinzugefügt, bestehende Checkpoints entfernt oder verschoben oder IP-Adressen ändern sich. Das konnte bedeuten, dass die Listen der IP-Adressen, die du für eine Whitelist verwenden wolltest, bis zur nächsten Synchronisation veraltet war und zu unnötigen Fehlern führte.

Wir listen nun zukünftige Checkpoint-IP-Adressen, sodass sie in der API-Antwort enthalten sind. Auf diese Weise wird deine Whitelist vorzeitig aktualisiert.

### Beziehungen in der Statistics API

Antworten der [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics) (die verwendet werden kann, um statistische Daten für Prüfobjekte oder Prüfobjektgruppen abzurufen) enthalten nun einige zusätzliche Metadaten zur Antwort. Das neue Array `Relationships` besteht bereits bei anderen API-Endpunkten. Es enthält zusätzliche Informationen zu Abfragen wie zum Beispiel einen Link zur Monitor- oder MonitorGroup API-Abfrage, um weitere Informationen über das Prüfobjekt oder die Prüfobjektgruppe selbst abzurufen.


```json
        "Relationships": [
            {
                "Id": "4c3a9529-7934-4978-9c36-c377b232g7hb",
                "Type": "Monitor",
                "Links": {
                    "Self": "/Monitor/4c3a9529-7934-4978-9c36-c377b232g7hb"
                }
            }  
        ]
```

## Mai 2022

### Fehlerbehebung bei Start-/Ende-Parametern in der Statistics API

Unsere API unterstützt das Abrufen statistischer Prüfobjektdaten mit der [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics/Statistics_GetMonitorStatistics). Du kannst entweder einen voreingestellten Zeitraum festlegen, für den die Daten abgerufen werden (mit verfügbaren Werten wie `Last24Hours`) oder einen benutzerdefinierten Zeitraum mit Start- und Ende-URL-Parametern angeben. Zum Beispiel ruft `GET /Statistics/Monitor/{monitorGuid}?Start=2022-04-08&End=2022-04-09` statistische Daten zum angegebenen Zeitraum für ein einzelnes Prüfobjekt ab.

Es gab ein Problem, bei dem die Minutenangabe der Start- und Ende-Zeitstempel nicht richtig abgebildet wurden, was zu unvollständigen (oder sogar leeren) Ergebnissen bei der API-Antwort führen konnte. Dieses Problem wurde nun behoben.

## Februar 2022

### Update: Status API

Die [Status API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Status/Status_GetMonitorStatus) ruft Statusinformationen für ein bestimmtes Prüfobjekt ab, basierend auf der letzten Prüfung des Prüfobjekts. Dieser Endpunkt kann als Information zu aktuellen Prüfobjektstatus verwendet werden. Wir haben die Antwort erweitert und sie umfasst nun einen Wert für `TotalTime` – Informationen über den [Messwert Gesamtzeit]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="de" >}}) für die letzte Prüfung des Prüfobjekts.

## Januar 2022

### Ausgabe der korrekten Monitoring-Daten

Wenn ein Operator, der nicht Administrator ist, mit der [Berechtigung **Daten anzeigen**]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}}) für ein bestimmtes Prüfobjekt diese Prüfobjektdefinition über die API (mit `GET /Monitor/{monitorGuid}`) abgerufen hat, enthielt die Antwort nicht alle relevanten Daten. Dies war nicht korrekt, da dieselben Daten bereits über die Benutzeroberfläche verfügbar waren, aber nicht über die API. Das wurde nun korrigiert. Wenn diese Operatoren nun ein Prüfobjekt abrufen, sind die Werte  *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive* und *GenerateAlert* enthalten.

## August 2021

### Ankündigung: Auslaufen von Version 3 unserer API

Die [Uptrends API]({{< ref path="support/kb/api" lang="de" >}}) unterstützt derzeit zwei Versionen nebeneinander. Version 3 ist eine ältere Vorgängerversion unserer API und wir empfehlen derzeit, Version 4 zu verwenden. Version 4 verfügt über einen sehr viel vollständigeren Funktionsumfang und ist seit Längerem Entwicklungsschwerpunkt. Wir haben daher entschieden, Version 3 unserer API auslaufen zu lassen. Sie wird ab **Dezember 2022** nicht länger verfügbar sein. 

Für Kunden, die derzeit noch Version 3 unserer API verwenden, weisen wir darauf hin, dass diese Version noch bis zum genannten Zeitpunkt unterstützt wird. Wir empfehlen jedoch, so bald wie möglich das Upgrade zu Version 4 durchzuführen. Um dir dabei zu helfen, haben wir einen [Upgrade-Leitfaden für den Wechsel von API v3 nach v4]({{< ref path="support/kb/api" lang="de" >}}), verfasst, der die Hauptunterschiede zwischen den zwei API-Versionen und wie du sie in deinen Skripten und deiner Software überbrückst behandelt. 

## Juli 2021

### Code-relevante Änderung: Änderung an der Antwort der OperatorGroup Autorisierung

Mit der Uptrends API kannst du [Berechtigungen für Operatoren und Operator-Gruppen]({{< ref path="support/kb/account/users/operators/permissions" lang="de" >}}) verwalten und Rollen wie **Administrator** oder **Ansprechpartner Finanzen** zuweisen sowie **Zugriff auf Infra** gewähren. Die [OperatorGroup API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/OperatorGroup) enthält mehrere Optionen, um Berechtigungen abzurufen, hinzuzufügen oder zu löschen. 

Wir haben die Art und Weise geändert, wie Berechtigungen für Operator-Gruppen in der API angegeben werden. Dies kann sich auf eine von dir eingerichtete automatisierte Erstellung, Entfernung oder den Abruf von Informationen über Berechtigungen von Operator-Gruppen auswirken. Derzeit erfolgt der Abruf von Informationen zu Berechtigungen durch:

`GET /OperatorGroup/{operatorGroupGuid}/Authorization`

was eine Antwort wie unten dargestellt zurückgibt (abhängig von den für die jeweilige Operator-Gruppe eingerichteten Berechtigungen):

```json
[
      {
        "AuthorizationId": "{authIdGuid1}",
        "AuthorizationType": "FinancialOperator",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    {
        "AuthorizationId": "{authIdGuid2}",
        "AuthorizationType": "AllowInfra",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    ...
]
```

In Zukunft wird diese Abfrage eine vereinfachte Antwort zurückgeben, bei der die Berechtigungen, aber keine weiteren Informationen gelistet werden. In der Antwort werden weder `operatorGroupGuid` noch `AuthorizationId` (Letzteres wird komplett entfernt, Berechtigungen werden nicht länger über eine eigene GUID verfügen) enthalten sein. Die Antwort wird folgendermaßen aussehen:

```json
{
    "FinancialOperator",
    "AllowInfra",
    ...
}
```

Eine neue Berechtigung für eine Operator-Gruppe wird derzeit hinzugefügt durch Senden einer POST-Anfrage an:

 `/OperatorGroup/{operatorGroupGuid}/Authorization` 
 mit einem Request Body, der einen "AuthorizationType" angibt. Die derzeit verfügbaren Werte für AuthorizationType für Operator-Gruppen findest du in der [Uptrends API Swagger UI](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/), unter **Models** (unten) und dann **OperatorGroupAuthorizationType**.
 
 Zukünftig kann eine neue Berechtigung für eine Operator-Gruppe hinzugefügt werden durch Senden einer POST-Anfrage an: 

 `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}` 
 ohne einen Request Body einzufügen. 

Das Löschen einer Berechtigung aus einer Operator-Gruppe wird derzeit durch Senden einer DELETE-Anfrage an `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationGuid}` durchgeführt, aber wie oben erwähnt wird „authorizationGuid‟ als Einheit nicht länger unterstützt und kann nicht mehr genutzt werden. Stattdessen kannst du Berechtigungen löschen, indem du dich direkt mit ihrem Namen in der Anfrage-URL auf sie beziehst: `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}`

## Februar 2021

### Code-relevante Änderung: sensible Werte bei Multi-Step API-Prüfobjekten

Unser [Prüfobjekttyp Multi-Step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="de" >}}) ermöglicht dir, mehrere aufeinanderfolgende HTTP-Anfragen auszuführen, bei denen jede neue Anfrage ein oder mehrere abgerufene Datenteile aus vorherigen Anfragen nutzt, um die Aufgabe auszuführen. Häufig gehört zu einem der Schritte das Senden von Anmeldedaten, um Zugriff auf eine bestimmte Ressource zu erhalten. Früher wurden diese Anmeldedaten als vordefinierte Variablen zur Prüfobjektdefinition hinzugefügt und als *sensibel* gekennzeichnet.

Um die Sicherheit der Handhabung solcher Anmeldedaten zu steigern, geben wir diese Vorgehensweise auf. Stattdessen werden Anmeldedaten in der [Vault]({{< ref path="support/kb/account/vault" lang="de" >}}) abgelegt. Mit dieser Änderung wird bei Multi-Step API-Prüfobjekten die Kennzeichnung vordefinierter Variablen als sensibel überflüssig und wir werden diese Funktion entfernen.

Dies wird sich darauf auswirken, wie du über unsere API Multi-Step API-Prüfobjekte erstellen und mit ihnen interagieren kannst. Derzeit enthält die Prüfobjektdefinition für diesen Prüfobjekttyp ein Array „PredefinedVariables“, bei dem jede einzelne Variable über einen booleschen Wahr-Falsch-„Sensibel“-Ausdruck verfügt. In nächster Zukunft wird dieser boolesche Ausdruck aus der Definition entfernt. Wenn du ein Multi-Step API-Prüfobjekt in deinem Account mithilfe der Uptrends API erstellen oder aktualisieren möchtest, wird dieses Feld nicht mehr verfügbar sein. 

### Änderung: umbenanntes Routing
 
 Bei Uptrends APIv4 ist die Vorgehensweise, Routes zu benennen, nicht einheitlich. In den meisten Fällen werden Singular-Begriffe genutzt, aber in einigen Fällen waren diese auch in der Plural-Form. Die Route enthält nun nur Singular-Elemente, 
 zum Beispiel `/MonitorGroup/{monitorGroupGuid}/Member` statt `/MonitorGroup/{monitorGroupGuid}/Members`.

 Aus Gründen der Rückwärtskompatibilität unterstützen wir weiterhin die alten Routes.

{{< /Features/Story >}}
