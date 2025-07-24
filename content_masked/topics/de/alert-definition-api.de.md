{
  "hero": {
    "title": "Alert Definition API"
  },
  "title": "Alert Definition API",
  "url": "[URL_BASE_TOPICS]api/alert-definition-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mit der Alert Definition API kannst du die Einstellungen für eine bestimmte Meldedefinition verwalten. Eine Meldedefinition beschreibt, wie und an wen eine Warnmeldung gesendet wird. Beispielsweise kannst du eine Warnmeldung konfigurieren, die erzeugt wird, wenn ein Fehler mehr als fünf Minuten andauert. Du kannst wählen, wer per E-Mail und SMS benachrichtigt werden soll.

Die Alert Definition API unterstützt derzeit nur das Aktivieren und Deaktivieren einer Meldedefinition mit der Einstellung [INLINE_CODE_1].

## PUT /AlertDefinition/{alertDefinitionGuid}

Aktualisiert die durch die Guid angegebene Meldedefinition. Der Anfragetext für diese Anfrage sollte die vollständige Liste der Meldedefinitions-Felder enthalten – im Gegensatz zu einer PATCH-Anfrage, bei der du nur einen Teil der Felder spezifizierst. Die vollständige Liste besteht aus den Feldern [INLINE_CODE_2] und [INLINE_CODE_3]. Die folgende PUT-Anfrage deaktiviert die Meldedefinition, selbst wenn sie schon zuvor deaktiviert worden war.

[INLINE_CODE_4]

Anfragetext:

    {
      "AlertDefinitionGuid": "e06bcd76-b20f-42de-a2d4-5b2a4daad902",
      "IsActive": false
    }

## PATCH /AlertDefinition/{alertDefinitionGuid}

Aktualisiert die durch die Guid angegebene Meldedefinition. Der Anfragetext für diese Anfrage sollte eine Teilliste der Felder enthalten, die aktualisiert werden sollen. Üblicherweise wird diese Anfrage verwendet, um nur einige wenige Felder zu aktualisieren. Führe nur Felder in der Anfrage auf, die aktualisiert werden sollen. Das Feld [INLINE_CODE_5] ist optional. Wenn du es angibst, muss es der [INLINE_CODE_6] der URL entsprechen.

Die folgende PATCH-Anfrage wird verwendet, um eine Meldedefinition zu aktivieren, indem der Wert [INLINE_CODE_7] für das Feld [INLINE_CODE_8] angegeben wird.

[INLINE_CODE_9]

Anfragetext:

    {
      "IsActive": true
    }
