{
  "hero": {
    "title": "Mit Fehler-Snapshots arbeiten"
  },
  "title": "Mit Fehler-Snapshots arbeiten",
  "summary": "Fehler-Snapshots können bei der Fehlerbehebung helfen. Erfahre hier, wann sie verfügbar sind.",
  "url": "/support/kb/alarme/fehler/arbeit-mit-fehler-snapshots",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/working-with-error-snapshots"
}

Deine Website ist ausgefallen, aber du weißt nicht, warum. Du meldest dich bei deinem Uptrends Website Monitoring-Account an und folgerst, dass deine Besucher einem Verbindungsfehler unterliegen. Aber wie? Indem du die Fehlerdetails des Prüfobjekts und die Fehler-Snapshots untersuchst.

## Was ist ein Fehler-Snapshot?

Ein Fehler-Snapshot ist ein Screenshot, der vom Uptrends Service aufgezeichnet wird, um zu zeigen, was deine Besucher sehen, wenn sie ein Problem erleben.

![Screenshot der Kontrolldetails Mit Fehler-Snapshot](/img/content/scr_check-details-with-error-snapshot.min.png)

## Wie funktionieren Fehler-Snapshots?

Uptrends erstellt Fehler-Snapshots unter bestimmten Umständen.

- Snapshots werden nur für **HTTP(S)-** und **Webservice (HTTP(S))-** und **Transaktionsprüfobjekte** bereitgestellt.
- Uptrends erstellt Snapshots nur für bestimmte Fehler (z. B. Fehler bei Musterabgleich, aber nicht für Fehler bei Performance Limits). Wenn es ein Fehler der Infrastruktur wie etwa ein TCP-Verbindungsfehler ist, gibt es keinen Inhalt, den wir dir zeigen könnten.
- Der Uptrends Service erstellt nur Snapshots bei bestätigten Fehlern, die der **erste** in einer Reihe sind. Für Folgefehler gibt es keinen Snapshot.{{< callout >}}**Hinweis**: Es kann einige Minuten dauern, bevor Fehler-Snapshots nach dem Auftreten eines Fehlers sichtbar sind. In einigen Fällen ist ein Snapshot möglicherweise nicht verfügbar, abhängig vom Inhalt, den Uptrends erhält.{{< /callout >}}
