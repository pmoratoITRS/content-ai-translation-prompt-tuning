{
  "hero": {
    "title": "Fehlende Daten bei den Dashboard-Kacheln für Multicheckpoints"
  },
  "title": "Fehlende Daten bei den Dashboard-Kacheln für Multicheckpoints",
  "summary": "Erfahre, warum gelegentlich keine oder unvollständige Daten in den Dashboard-Kacheln für Multicheckpoints angezeigt werden.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/dashboards/fehlende-daten-bei-den-dashboard-kacheln-fuer-multicheckpoints",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Unsere Listen und Diagramme zu Multicheckpoints zeigen ausgewählte Werte anhand der Checkpoints, die den Test durchgeführt haben. Diese Datenkacheln lassen wunderbar Latenz und andere regionale Probleme erkennen. Gelegentlich erhalten wir eine Frage hinsichtlich fehlender oder unvollständiger Daten in diesen Kacheln. Es gibt unterschiedliche Ursachen für dieses Problem.

## Dashboard- und Monitoring-Checkpoint-Auswahl verhalten sich konträr zueinander

Als Du ein Prüfobjekt einrichtet hast, hast Du auch die Checkpoints ausgewählt, die das Prüfobjekt nutzen sollte. Zudem hast Du die Möglichkeit, am oberen Rand des Dashboards die Checkpoints auszuwählen, die für die Berechnung der Daten auf eben diesem Dashboard verwendet werden. Wenn die für das bzw. die Prüfobjekte ausgewählten Checkpoints nicht in der Checkpoint-Auswahl auf der Dashboard-Seite enthalten sind, erhältst Du entweder keine oder unvollständige Datensets. Gleiche die Dashboard-Checkpoints an, sodass sie die für das bzw. die Prüfobjekte ausgewählten Checkpoints enthalten. Ist dies nicht der Fall, hast Du eventuell zu viele Checkpoints für die Kachel ausgewählt (lies weiter).

[SHORTCODE_1]
**Hinweis**: Du wirst auch keine Daten in der Multicheckpoint-Liste für Checkpoints sehen, die von dem Prüfobjekt genutzt werden, das Du nicht für das Dashboard ausgewählt hast.
[SHORTCODE_2]

## Bei Nutzung des Multicheckpoint-Diagramms zu viele Dashboard-Checkpoints ausgewählt

Die Standardeinstellung für das Dashboard zeigt Daten für alle Checkpoints, aber die Kachel für Multicheckpoint-Diagramme kann nur zehn Checkpoints gleichzeitig anzeigen. Belässt Du das Dashboard in seinen Standardeinstellungen oder hast Du eine zu große Anzahl Checkpoints ausgewählt, aber Dein Prüfobjekt verwendet nur wenige, siehst Du eventuell auch keine Daten oder nur Daten für einige Checkpoints. Die Kachel nimmt die ersten zehn Checkpoints, basierend auf der Checkpoint-Auswahl des Dashboards, und zeigt die Daten für diese Checkpoints. Wenn für die ersten zehn Checkpoints keine Daten vorhanden sind, siehst Du die Meldung „Es sind keine Daten verfügbar“. Wenn einer oder mehrere Checkpoints, die Du für Dein Prüfobjekt ausgewählt hast, zu den ersten zehn für das Dashboard gewählten Checkpoints gehören, siehst Du die Daten für diese Checkpoints zusammen mit den anderen Checkpoints der ersten zehn, selbst wenn für sie keine Daten vorhanden sind. Um alle Daten in dieser Kachel zu sehen, musst Du die Checkpoint-Auswahl für das Dashboard anpassen, sodass sie den Checkpoints des Prüfobjekts (bis zu zehn Checkpoints) entspricht.
