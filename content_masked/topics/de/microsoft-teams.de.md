{
  "hero": {
    "title": "Website Monitoring-Alarmierungen in Microsoft Teams erhalten"
  },
  "title": "Microsoft Teams-Integration",
  "summary": "Erhalte Website-Monitoring-Meldungen von Uptrends in Microsoft Teams.",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/microsoft-teams",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Microsoft Teams** ist der Hub für Teamarbeit in Microsoft 365. Du kannst (per Chat, Anruf, Video) kommunizieren und Informationen (Dateien, Terminpläne usw.) mit Teams teilen. Die Integration von Microsoft Teams in Uptrends ermöglicht automatische Benachrichtigungen von Uptrends. Zum Einrichten der Integration in beiden Systemen sind diese Schritte erforderlich:

1.  Einen *Workflow* bei Microsoft Teams einrichten
2.  Einrichten der Integration bei Uptrends
3.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Was passiert, wenn diese Integration eingerichtet ist? Unten siehst du ein Beispiel, wie die Integration in Microsoft Teams erscheint.

![Beispiel Alarmierung in Teams]([LINK_URL_1])

In dem Kanal von Microsoft Teams, für den die Integration definiert wurde, erhältst du eine Nachricht mit Einzelheiten zur erzeugten Warnmeldung. Von dieser Nachricht aus kannst du direkt zum Dashboard, Fehler oder Prüfobjekt bei Uptrends wechseln, um noch mehr Informationen zu erhalten und das Problem weiter zu untersuchen. Klicke auf eine Schaltfläche und du wirst direkt an die richtige Stelle in der Uptrends-Anwendung geleitet.

Hier sind die detaillierten Anweisungen, wie du diese Integration einrichten kannst!

## 1. Einen Workflow bei Microsoft Teams einrichten

1.  Rufe in Microsoft Teams den Kanal auf, in dem du Meldungen von Uptrends erhalten möchtest. Fahre mit der Maus über den Kanal, um [SHORTCODE_3]Weitere Optionen[SHORTCODE_4] ( ... ) anzuzeigen. Wähle [SHORTCODE_5] Workflow [SHORTCODE_6].
![Einen Workflow hinzufügen]([LINK_URL_2])
2.  Suche und wähle *„Posten in einem Kanal, wenn eine Webhookanforderung empfangen wird“*.
3.  Gib einen Namen für den Workflow ein.
4.  Klicke auf *Weiter*.
5. Überprüfe die Einstellungen bei **Microsoft Teams Team** und **Microsoft Teams Kanal** und klicke auf *Workflow hinzufügen*.
5.  Der Workflow sollte nach einigen Sekunden erzeugt worden sein. Eine URL wird am Ende des Formulars angezeigt:
![Teams Workflow URL]([LINK_URL_3])
6.  Kopiere die URL und speichere sie für den späteren Gebrauch. Du benötigst sie beim Einrichten der Integration bei Uptrends.
7.  Klicke auf [SHORTCODE_7]Fertig[SHORTCODE_8].

Damit ist die Einrichtung der Integration bei Microsoft Teams abgeschlossen.

## 2. Einrichten der Integration bei Uptrends

Um eine neue Integration für Microsoft Teams bei Uptrends hinzuzufügen, führe diese Schritte aus:

1.  Rufe [SHORTCODE_9]Alarmierung > Integrationen [SHORTCODE_10] auf.
2.  Klicke auf [SHORTCODE_11]Integration hinzufügen[SHORTCODE_12].
3.  Wähle Microsoft Teams als Integrations-Art.
![]([LINK_URL_4])
4.  Gib der Integration einen Namen.
5.  Füge die kopierte Webhook URL von Microsoft Teams in [SHORTCODE_13]Vordefinierte Variablen > WorkflowUrl[SHORTCODE_14] ein.
6.  Klicke auf [SHORTCODE_15]Speichern[SHORTCODE_16], um die neuen Einstellungen zu sichern. Die neue Integration mit Microsoft Teams wird auf der Integrationen-Seite erscheinen.

Damit ist die Einrichtung der Integration bei Uptrends abgeschlossen. Du kannst diese Integration nun zu deinen Meldedefinitionen hinzufügen.

[SHORTCODE_1]
**Tipp**: Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
[SHORTCODE_2]

## 3. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie zu einer oder mehreren Eskalationsstufen einer Meldedefinition hinzufügen, um entsprechende Benachrichtigungen zu erhalten.

1.  Wechsle nach [SHORTCODE_17]Alarme > Meldedefinitionen[SHORTCODE_18] und öffne die Definition, zu der die Integration hinzugefügt werden soll.
2.  Jede [SHORTCODE_19] Eskalationsstufen [SHORTCODE_20]-Registerkarte verfügt über das Element **Alarmierung durch Integrationen** mit einer Liste der verfügbaren Integrationen. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]([LINK_URL_5]), wie Eskalationsstufen funktionieren.
3.  Wähle die Integration(en), die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die **benutzerdefinierte Integration** für Microsoft Teams.
4.  Klicke auf [SHORTCODE_21]Speichern[SHORTCODE_22], um die Änderungen zu sichern.

**Und das war‘s schon!** Du hast die Integration von Microsoft Teams eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team]([LINK_URL_6]).
