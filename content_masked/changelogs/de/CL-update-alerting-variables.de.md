{
  "title": "Einführung neuer Alarmierungsvariablen",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]februar-2025-alarmierungsvariablen-updates",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die folgenden Alarmierungsvariablen sind nun verfügbar:

- **@alert.numberOfConsecutiveErrors** – enthält die Gesamtzahl aufeinanderfolgender Fehler (bestätigter Fehler) des Alarms. Dies gibt [INLINE_CODE_1] aus, wenn die API-Antwort [INLINE_CODE_2] lautet.
- **@alert.checkpointName** – enthält den Checkpoint-Namen oder Standort, wo der Alarm zuletzt überprüft wurde. Dies gibt [INLINE_CODE_3] aus, wenn die API-Antwort [INLINE_CODE_4] lautet.
- **@‌alert.responseHeaders** – enthält die Antwort-Header des Alarms in Schlüssel-Wert-Paaren. Zum Beispiel gibt dies [INLINE_CODE_5] aus dem API-Antwort-Header aus, ähnlich wie die Werte für [INLINE_CODE_6] zurückgegeben werden. 

Beachte, dass der Wert für [INLINE_CODE_7] leer sein kann, wenn [Datenschutz für Private Locations]([LINK_URL_1]) bei einem privaten Standort, der die Alarmprüfung durchführt, aktiviert ist. Weitere Informationen findest du unter [Systemvariablen für Alarmierungen]([LINK_URL_2]).