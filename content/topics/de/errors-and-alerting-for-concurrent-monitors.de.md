{
  "hero": {
    "title": "Fehler und Alarmierung beim Parallel-Monitoring"
  },
  "title": "Fehler und Alarmierung beim Parallel-Monitoring",
  "summary": "Wie funktionieren die Fehler-Bestimmung und Alarmierung beim Parallel-Monitoring?",
  "url": "/support/kb/synthetic-monitoring/parallel-monitoring/fehler-und-alarmierung-beim-parallel-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors"
}

Verglichen mit dem Standard-Monitoring funktioniert die Art und Weise, wie Fehler bei Parallel-Prüfobjekten bestimmt werden, etwas anders. Das Standard-Monitoring hält sich üblicherweise an eine Abfolge von *[OK (grün) – unbestätigter Fehler (gelb) – bestätigter Fehler (rot)]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}})* zur Bestimmung von Fehlern. Dabei werden bei jedem Prüfobjekt Alarme nach einer festgelegten Anzahl bestätigter Fehler erzeugt. Bei Parallel-Prüfobjekten werden Fehler jedoch anders bestimmt. Mit diesem Artikel sehen wir uns genauer an, wie Parallel-Prüfobjekte Fehler bestimmen. Hinweis: Sobald die Fehler bestimmt wurden, funktioniert die Alarmierung [auf dieselbe Weise wie beim Standard-Monitoring](/support/kb/alarme).

## Fehler-Schwelle beim Parallel-Monitoring

Wenn du ein Parallel-Prüfobjekt einrichtest (oder ein bestehendes Prüfobjekt auf Parallel-Modus umstellst), sind zwei neue Felder auszufüllen: **Schwellwert unbestätigter Fehler** und **Schwellwert bestätigter Fehler**. Zudem sind für ein Parallel-Prüfobjekt mindestens 3 Checkpoints hoher Verfügbarkeit oder 5 Checkpoints aus der kompletten Liste aller Checkpoints erforderlich. Zusammen genommen legen diese Einstellungen die Umstände fest, gemäß denen eine Prüfung durch ein Prüfobjekt den Status OK, unbestätigter Fehler oder bestätigter Fehler verzeichnet. Kurz gesagt meldet ein Parallel-Prüfobjekt Fehler, wenn die Anzahl der Checkpoints, die jeweils einen Fehler erkennen, die festgelegten Schwellen überschreiten.

Sehen wir uns beispielsweise ein HTTPS-Prüfobjekt an, für das eine Schwelle unbestätigter Fehler von 30 %, eine Schwelle bestätigter Fehler von 50 % festgelegt und 10 Checkpoints ausgewählt wurden.

-   Unter normalen Umständen würde jeder ausgewählte Checkpoint jeweils ein OK-Ergebnis melden. Keiner der Checkpoints, die den Test parallel ausführen, erkennen einen Fehler, sodass die Fehlerrate 0 % ist. In diesen Fällen ist das Gesamtergebnis des Parallel-Prüfobjekts *OK*.
-   Wenn zwei der ausgewählten Checkpoints ein Problem erkennen, beträgt die Fehlerrate 20 % (da 2 von 10 ausgewählten Checkpoints einen Fehler erkannt haben). Da keine der beiden Fehler-Schwellen berührt wurde, gilt das Gesamtergebnis der Prüfung immer noch als *OK*.
-   Wenn aber vier der ausgewählten Checkpoints ein Problem erkennen, beträgt die Fehlerrate 40 %. Dies übersteigt die Schwelle unbestätigter Fehler (30 %), aber nicht die Schwelle bestätigter Fehler (50 %). Das Gesamtergebnis der Prüfung lautet *unbestätigt* und löst daher ohne Ausnahme keine Alarmierung aus.
-   Wenn fünf (oder mehr) Checkpoints jeweils einen Fehler erkennen, entspricht die Fehlerrate der Schwelle bestätigter Fehler oder übersteigt diese. In dem Fall wird das Gesamtergebnis sofort als *bestätigter* Fehler verzeichnet. Das bedeutet, diese Fehler können Warnmeldungen auslösen, basierend auf den von dir festgelegten Meldedefinitionen.

Im Beispiel-Bild unten haben sechs ausgewählte Checkpoints (oder \~33 %) einen Fehler gemeldet. Dies übersteigt die Schwelle *unbestätigter* Fehler (25 % bei diesem Beispiel), aber nicht die Schwelle *bestätigter* Fehler (50 %). Das Gesamtergebnis der Prüfung lautet daher *unbestätigt* und löst keine Alarmierungen aus. ![](/img/content/5d220dc1-4e11-45a7-b13f-152bd67a10b1.png)

Mit anderen Worten: Das Parallel-Monitoring prüft Fehler nicht wie das Standard-Monitoring mit einer wiederholten Prüfung. Ein Standard-Prüfobjekt führt sofort nach Erkennen eines Fehlers einen weiteren Test von einem anderen Checkpoint-Standort aus, um den Fehler zu bestätigen. Beim Parallel-Monitoring übertreffen wir diese Zuverlässigkeit, indem wir den Test zum selben Zeitpunkt von mehreren Standorten ausführen. Wenn eine bestimmte Anzahl von ihnen einen Fehler meldet, kann mit Sicherheit angenommen werden, dass der Fehler tatsächlich vorliegt.

{{< callout >}}
**Hinweis:** Die Prüfungen der einzelnen Parallel-Prüfobjekte folgen nicht dem üblichen Muster *OK-unbestätigter-bestätigter Fehler*. Stattdessen sind einzelne Prüfungen entweder *OK* (grün) oder *Bestätigt* (rot). Da der Status deines Prüfobjekts aufgrund der von dir eingerichteten Fehler-Schwellen bestimmt wird, wird ein einzelner bestätigter Fehler keinen Alarm auslösen.
{{< /callout >}}

## Checkpoint-Ausfallzeiten berücksichtigen

Da unser [globales Netzwerk von Checkpoints](https://www.uptrends.de/checkpoints) recht groß ist, sind Ausfallzeiten unvermeidlich. Hauptsächlich liegt der Grund in geplanten Wartungen, aber gelegentlich sind bestimmte Checkpoints aus anderen Gründen zur Ausübung der Prüfung durch dein Prüfobjekt nicht verfügbar. Sollte dies bei einem der von dir für das Parallel-Monitoring gewählten Checkpoints vorkommen, während eine Prüfung ausgeführt wird, wird das Gesamtergebnis der Prüfung ein graues **?**-Symbol für den speziellen Checkpoint anzeigen. Die jeweilige Prüfung für diesen Checkpoint gilt als *ergebnislos* und wir berücksichtigen sie nicht bei der Gesamtfehlerzahl aus den jeweiligen Prüfungen zur Feststellung, ob sie die Fehler-Schwellen übersteigt. ![](/img/content/052d85fc-3b36-448c-b4bd-e30431fe53a8.png)
