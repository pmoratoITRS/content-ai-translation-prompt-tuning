{
  "hero": {
    "title": "Nicht bestätigte und bestätigte Fehler"
  },
  "title": "Nicht bestätigte und bestätigte Fehler",
  "summary": "Was sind nicht bestätigte und bestätigte Fehler und wie werden sie in den Ausfallzeiten berücksichtigt",
  "url": "/support/kb/alarme/fehler/nicht-bestaetigte-und-bestaetigte-fehler",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/unconfirmed-and-confirmed-errors"
}

Eins der Highlights der Nutzung von Uptrends für das Monitoring von Servern und Websites ist unsere Fähigkeit, dein Team über Ausfälle oder auf die Performance bezogene Ereignisse informiert zu halten. Aber was macht einen Fehler zu einem nicht bzw. zu einem bestätigten Fehler?

## Der Unterschied zwischen einem nicht bestätigten und bestätigten Fehler

Ein **unbestätigter Fehler** ist ein Fehler, der gemeldet wurde, nachdem ein Prüfobjekt von einem Checkpoint-Standort getestet wurde, der aber noch nicht von einem zweiten Checkpoint-Standort verifiziert wurde.

Ein **bestätigter Fehler** ist ein Fehler, der von zwei Checkpoint-Standorten verifiziert wurde.

Dieser **Ausfall-Doublecheck** verhindert die Erzeugung von Falschmeldungen. Wenn der Doublecheck jedoch einen Fehler nicht bestätigt, wird angenommen, dass der erste nicht bestätigte Fehler ein temporäres Problem war.

{{< callout >}}
**Hinweis**: Nicht bestätigte Fehler werden gelb im Dashboard-Bericht des Prüfobjektprotokolls dargestellt. Bestätigte Fehler werden in Rot angezeigt. Keine Fehler wird grün angezeigt.
{{< /callout >}}

## Wie Fehler zur Ausfallzeiten und Alarmen beitragen

Es ist wichtig, zu beachten, dass der Uptrends-Service nur bestätigte (doppelt geprüfte) Fehler zum Ausfallalarmierungssystem hinzufügt.

Um zu steuern, wenn eine Alarmierung gesendet werden sollte, kannst du die Meldedefinition ändern oder eine eigene erstellen. Mehr über Meldedefinitionen findest du im Artikel [Meldedefinitionen]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}).
