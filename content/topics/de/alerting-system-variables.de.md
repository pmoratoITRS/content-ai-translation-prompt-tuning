{
  "hero": {
    "title": "Variablen für das Alarmierungssystem"
  },
  "title": "Variablen für das Alarmierungssystem",
  "summary": "Eine Übersicht verfügbarer Systemvariablen, die bei (benutzerdefinierten) Integrationen eingesetzt werden können",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/warnmeldungen-systemvariablen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/alerting-system-variables",
  "tableofcontents": false
}

Dieser Artikel enthält einen Überblick über alle verfügbaren **Systemvariablen**, die zur Eingabe relevanter Informationen – beispielsweise, welches Prüfobjekt sie ausgelöst hat, welcher Fehler aufgetreten ist oder den Alarm selbst – in eine ausgehende Warnmeldung verwendet werden können. Weitere Informationen, wie du diese Systemvariablen nutzen kannst findest du in unserem Artikel [Den richtigen Nachrichteninhalt erzeugen]({{< ref path="support/kb/alerting/integrations/custom-integrations/building-the-right-message-content" lang="de" >}}).

Hinweis: Um die hier aufgeführten Variablen zu nutzen, müssen sie in doppelten geschwungenen Klammern in den Nachrichteninhalt eingefügt werden. Beispiel: `{{@alert.alertGuid}}`.

|  Variable   | Beschreibung    |  Beispielwert   |
| --- | --- | --- |
| `@account.accountId` | Deine Uptrends Account-ID. | `299840` |
| `@alert.alertGuid` | Einzigartige ID dieses Alarms. | `cbfc7769-edb2-46a7-89d0-1e1b1fb0815b` |
| `@alert.checkpointName` | Enthält den Checkpoint-Namen oder Standort, wo der Alarm zuletzt überprüft wurde. | `Ghent, Belgium` |
| `@alert.description` | Textbeschreibung des Fehlers, der die Warnmeldung ausgelöst hat. Enthält gegebenenfalls die Schrittnummer. | `Step 1: Navigate to https://www.galacticresorts.com failed.` |
| `@alert.downtimeDuration` | Die Zeit zwischen dem ersten Fehler und dem Zeitstempel des aktuellen (OK) Alarms. | `48:03:21` |
| `@alert.errorTypeId` | {{< tableformatter >}} Die Fehlertyp-ID des Fehlers, der diesen Alarm ausgelöst hat. Unter [Fehlertypen]({{< ref path="/support/kb/alerting/errors/error-types" lang="de" >}}) findest du eine Liste der Fehlertypen. {{< /tableformatter >}} | `5407` |
| `@alert.failureMessage` | Die benutzerdefinierte Fehlermeldung für die jeweilige Aktion bei einem Transaktionsschritt, die den Fehler ausgelöst hat.  | `Login failed` |
| `@alert.firstError` | Das gleiche Datum mit Uhrzeit wie @alert.firstErrorUtc, aber in der Zeitzone deines Accounts. Ebenfalls nach ISO 8601 formatiert. | `2018-11-08T10:21:58` |
| `@alert.firstErrorCheckId` | Die ID des ersten Fehlers, der die Alarmierung ausgelöst hat. | `30833627687` |
| `@alert.firstErrorCheckUrl` | Die URL des Deep Links, der dich zu den Details des Fehlers führt, der die Warnmeldung ausgelöst hat. | `https://app.uptrends.com/Report/ProbeLog/Check/30833627687` |
| `@alert.firstErrorDescription` | Die Fehlerbeschreibung aus der ersten Prüfung, die eine Fehlermeldung ergab. Enthält gegebenenfalls die Schrittnummer. | `Step 1: Navigate to https://www.galacticresorts.com failed.` |
| `@alert.firstErrorFormatted` | Das gleiche Datum mit Uhrzeit wie @alert.firstErrorUtc, aber in Zeitzone und kulturellen Gepflogenheiten deines Accounts. | `8/28/2020 12:23 PM` |
| `@alert.firstErrorUtc` | Datum und Uhrzeit des ursprünglichen Fehlers, der diese Warnmeldung ausgelöst hat, in UTC-Zeit und nach ISO 8601 formatiert. | `2018-11-08T16:21:58` |
| `@alert.firstErrorUtcFormatted` | Datum und Uhrzeit des ursprünglichen Fehlers, der diese Warnmeldung ausgelöst hat, in UTC-Zeit und nach den in deinem Account verwendeten Gepflogenheiten formatiert. | `8/28/2020 10:23 PM` |
| `@alert.numberOfConsecutiveErrors` | Enthält die Gesamtzahl aufeinanderfolgender Fehler (bestätigte Fehler) des Alarms. | `2` |
| `@alert.resolvedIpAddress` | Die IP-Adresse, die verwendet wurde, um die Prüfung auszuführen. Dies kann eine IPv4- oder IPv6-Adresse sein. | `178.217.84.4 OR 2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@‌alert.responseHeaders` | {{< tableformatter >}} Enthält die Antwort-Header des Alarms in Schlüssel-Wert-Paaren. Beachte, dass der Wert dieser Variable leer sein kann, wenn [Datenschutz für Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}) bei einem privaten Standort, der die Alarmprüfung durchführt, aktiviert ist. {{< /tableformatter >}} | `Content-Type": "text/html` |
| `@alert.responseBody` | {{< tableformatter >}} Enthält den erhaltenen Antworttext, sofern verfügbar. Beachte dass der Antworttext Zeichen enthalten kann, die kodiert werden müssen [anhand von @JsonEncode oder @XmlEncode]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-formatting" lang="de" >}}). Der Antwortinhalt wird abgeschnitten, wenn er über 1 MB beträgt. {{< /tableformatter >}} | `{"Status": "error"}` |
| `@alert.serverIpv4` | Die IPv4-Adresse des Servers, von dem die Prüfung ausgeführt wurde. | `178.217.84.4` |
| `@alert.serverIpv6` | Die IPv6-Adresse des Servers, von dem die Prüfung ausgeführt wurde. | `2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@alert.sslValidUntil` | Gibt in SSL-Prüfobjektmeldungen Datum mit Uhrzeit wieder, wann das SSL-Zertifikat abläuft. | `2024-11-07T15:05:43` |
| `@alert.timestamp` | Das gleiche Datum mit Uhrzeit wie @alert.timestampUtc, aber in der Zeitzone deines Accounts. Ebenfalls nach ISO 8601 formatiert. | `2018-11-08T10:26:58` |
| `@alert.timestampFormatted` | Das gleiche Datum mit Uhrzeit wie @alert.timestampUtc, aber nach der in deinem Account verwendeten Zeitzone und den verwendeten Gepflogenheiten formatiert. | `8/28/2020 12:23 PM` |
| `@alert.timestampUtc` | Datum und Uhrzeit der Warnmeldung, in UTC-Zeit und nach ISO 8601 formatiert. | `2018-11-08T16:26:58` |
| `@alert.timestampUtcFormatted` | Datum und Uhrzeit der Warnmeldung, in UTC-Zeit und nach den in deinem Account verwendeten Gepflogenheiten formatiert. | `8/28/2020 10:23 PM` |
| `@alert.type` | Der Typ dieser Warnmeldung:<br>;<br>- Alarm: Ein neuer Fehler wurde erkannt.<br>- OK: Der ursprüngliche Fehler wurde behoben.<br>- Erinnerung: Der ursprüngliche Fehler besteht fort. | `Alert` \| `Ok` \| `Reminder` |
| `@alertDefinition.guid` | Die einzigartige ID der Meldedefinition, die zur Erzeugung dieser Warnmeldung führte. | `2C97E464-6112-435B-8C8D-6DEF1E18273A` |
| `@alertDefinition.name` | Der Name der Meldedefinition, die zur Erzeugung dieser Warnmeldung führte. | `Default Alert` |
| `@CustomField(customFieldReference)` | {{< tableformatter >}} Ein Hinweis auf ein [benutzerdefiniertes Feld]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#including-external-ids-or-custom-data" lang="de" >}}), das verwendet werden kann, um benutzerdefinierte Daten für einzelne Prüfobjekte aufzunehmen. {{< /tableformatter >}} | `Alert for Ops team` |
| `@escalationLevel.id` | Die ID der Eskalationsstufe, die zur Erzeugung dieser Warnmeldung führte. | `1` |
| `@escalationLevel.message` | Die benutzerdefinierte Nachricht, die in der Eskalationsstufe festgelegt wurde. | `Please use checklist THX-1138 to investigate this issue.` |
| `@incident.key` | Einzigartige ID des Ereignisses, zu dem diese Warnmeldung erfolgte. Eine Fehlerwarnmeldung und eine Ok-Meldung haben denselben Ereignisschlüssel. | `ba8ffcb7-5de0-489e-b649-f00f0b447e80-0-30099055746` |
| `@monitor.dashboardUrl` | Die URL eines Deep Links, der dich zum Dashboard dieses Prüfobjekts führt. | `https://app.uptrends.com/Probe/Dashboard?probeGuids=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.editUrl` | Die URL eines Deep Links, der dich zu den Einstellungen dieses Prüfobjekts führt. | `https://app.uptrends.com/Report/Probe?probeGuid=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.monitorGuid` | Die einzigartige ID des Prüfobjekts deines Accounts, das die Warnmeldung ausgelöst hat. | `849b2046-213d-43ad-9efc-5af1faaeb222` |
| `@monitor.name` | Der Name des Prüfobjekts deines Accounts, das die Warnmeldung ausgelöst hat. | `GalacticResorts.com - DNS` |
| `@monitor.notes` | Benutzerdefinierte Anmerkungen, die in den Einstellungen des Prüfobjekts eingegeben wurden. | `Please check Amazon Route53 DNS entries` |
| `@monitor.type` | Enthält den Prüfobjekttyp. | `Transaction` |
| `@monitor.url` | Die URL oder Netzwerkadresse, die dieses Prüfobjekt testet. | `https://galacticresorts.com` |