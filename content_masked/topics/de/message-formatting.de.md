{
  "hero": {
    "title": "Nachrichtenformatierung"
  },
  "title": "Nachrichtenformatierung",
  "summary": "Benutzerdefinierte Integrationen – Korrektes Formatieren deiner Nachrichten",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/benutzerdefinierte-integrationen/nachrichtenformatierung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Da die ausgehenden Warnmeldungen meistens JSON-formatiert sind, müssen Regeln eingehalten werden, damit der JSON-Code gültig bleibt. Dafür müssen bestimmte Zeichen (wie Zeilenumbrüche oder Anführungszeichen) codiert werden, bevor sie in die ausgehende, JSON-formatierte Warnmeldung aufgenommen werden können. Erfolgt die Codierung nicht, würde das die JSON-Struktur der ausgehenden Nachricht zerstören, was dazu führen kann, dass der empfangene Endpunkt einen Fehler verzeichnet und die eingehende Warnmeldung nicht korrekt verarbeitet. Dieser Artikel behandelt die integrierten Funktionen zur automatischen Nachrichtenformatierung.


## Anwenden der automatischen Formatierung [ANCHOR_1]


Wenn beispielsweise das Prüfobjekt-Feld „Anmerkungen“ (die du zu der Warnmeldung anhand der Systemvariable @monitor.notes hinzufügen kannst) solche Zeichen (Zeilenumbrüche, Anführungszeichen usw.) enthält, würde dies so aufgelöst, dass es die JSON-Struktur der ausgehenden Nachricht zerstört.

  
Beispiel: 
[INLINE_CODE_1]
Würde aufgelöst als:

``[INLINE_CODE_2]  
``[INLINE_CODE_3][SYSTEM_VAR_2][INLINE_CODE_4]{ "Notes": "[SYSTEM_VAR_3])}}"}[INLINE_CODE_5]@JsonEncode[INLINE_CODE_6]{ "notes": "Monitor notes that include\na line break or \"a quote\"" }[INLINE_CODE_7][SYSTEM_VAR_4]` einbettest.


