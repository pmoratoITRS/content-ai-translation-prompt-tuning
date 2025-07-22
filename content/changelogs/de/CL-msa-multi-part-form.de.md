{
  "title": "Unterstützung von Multipart Form jetzt bei MSA-Prüfobjekten verfügbar",
  "date": "2025-01-08",
  "url": "/changelog/januar-2025-msa-mehrteilige-formulare",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-msa-multi-part-form"
}

Bei der [Einrichtung eines Multi-Step API-Prüfobjekts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) kannst du eine Menge (gesendete Daten) als Teil der Anfragedefinition bestimmen. Zuvor war mit Uptrends nur das Senden eines Content-Types zur selben Zeit möglich, obwohl das HTTP-Protokoll das Senden mehrerer Typen unterstützt. Zum Beispiel kann Reintext sowie auch eine binäre Datei im Rahmen eines einzelnen API-Abrufs gesendet werden.

Mit der neuen Option **Multipart Form** kannst du nun mehrere Arten Content im Request Body des MSA-Schritts einfügen. Diese Option setzt den `Content-Type` Request Header auf `multipart/form-data` und ermöglicht dir, mehrere Contents mit unterschiedlichen Typen anzugeben. Diese Typen können Reintexteinträge oder aus der [Vault]({{< ref path="/support/kb/account/vault" lang="de" >}}) abgerufene Dateien sein.

![MSA Multipart Form](/img/content/scr-multi-part-form-msa.min.png)