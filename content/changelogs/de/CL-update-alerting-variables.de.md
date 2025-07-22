{
  "title": "Einführung neuer Alarmierungsvariablen",
  "date": "2025-02-19",
  "url": "/changelog/februar-2025-alarmierungsvariablen-updates",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-alert-variable-updates"
}

Die folgenden Alarmierungsvariablen sind nun verfügbar:

- **@alert.numberOfConsecutiveErrors** – enthält die Gesamtzahl aufeinanderfolgender Fehler (bestätigter Fehler) des Alarms. Dies gibt `2` aus, wenn die API-Antwort `{"numberOfConsecutiveErrors": "2"}` lautet.
- **@alert.checkpointName** – enthält den Checkpoint-Namen oder Standort, wo der Alarm zuletzt überprüft wurde. Dies gibt `Ghent, Belgium` aus, wenn die API-Antwort `{"checkpointName": "Ghent, Belgium"}` lautet.
- **@‌alert.responseHeaders** – enthält die Antwort-Header des Alarms in Schlüssel-Wert-Paaren. Zum Beispiel gibt dies `{"Content-Type": "text/html"}` aus dem API-Antwort-Header aus, ähnlich wie die Werte für `@alert.responseBody` zurückgegeben werden. 

Beachte, dass der Wert für `@‌alert.responseHeaders` leer sein kann, wenn [Datenschutz für Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}) bei einem privaten Standort, der die Alarmprüfung durchführt, aktiviert ist. Weitere Informationen findest du unter [Systemvariablen für Alarmierungen]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="de" >}}).