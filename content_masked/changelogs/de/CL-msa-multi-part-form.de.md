{
  "title": "Unterstützung von Multipart Form jetzt bei MSA-Prüfobjekten verfügbar",
  "date": "2025-01-08",
  "url": "[URL_BASE_CHANGELOG]januar-2025-msa-mehrteilige-formulare",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bei der [Einrichtung eines Multi-Step API-Prüfobjekts]([LINK_URL_1]) kannst du eine Menge (gesendete Daten) als Teil der Anfragedefinition bestimmen. Zuvor war mit Uptrends nur das Senden eines Content-Types zur selben Zeit möglich, obwohl das HTTP-Protokoll das Senden mehrerer Typen unterstützt. Zum Beispiel kann Reintext sowie auch eine binäre Datei im Rahmen eines einzelnen API-Abrufs gesendet werden.

Mit der neuen Option **Multipart Form** kannst du nun mehrere Arten Content im Request Body des MSA-Schritts einfügen. Diese Option setzt den [INLINE_CODE_1] Request Header auf [INLINE_CODE_2] und ermöglicht dir, mehrere Contents mit unterschiedlichen Typen anzugeben. Diese Typen können Reintexteinträge oder aus der [Vault]([LINK_URL_2]) abgerufene Dateien sein.

![MSA Multipart Form]([LINK_URL_3])