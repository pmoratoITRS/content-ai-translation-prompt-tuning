{
  "hero": {
    "title": "Wie funktioniert das Parallel-Monitoring?"
  },
  "title": "Wie funktioniert das Parallel-Monitoring?",
  "summary": "Eine Übersicht zum Parallel-Monitoring",
  "url": "/support/kb/synthetic-monitoring/parallel-monitoring/wie-funktioniert-parallel-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/how-does-concurrent-monitoring-work"
}

Bei Uptrends gibt es zwei Möglichkeiten des Monitorings der Verfügbarkeit, Performance und richtigen Funktion von Websites, Webservices und Servern: das Standard-Monitoring und das Parallel-Monitoring.

## Das Standard-Monitoring

Eine Prüfung durch ein Prüfobjekt wird von einem einzelnen Checkpoint aus durchgeführt. Tritt ein Fehler auf, wird er als unbestätigter Fehler betrachtet. Dann wird dieselbe Prüfung von einem anderen Checkpoint durchgeführt. Wenn dieser Checkpoint ebenfalls denselben Fehler meldet, wird das Ergebnis als bestätigter Fehler erachtet. Nur bestätigte Fehler lösen einen Alarm und das Senden von Benachrichtigungen (durch SMS, E-Mail, Slack, andere externe Systeme) aus.

## Das Parallel-Monitoring

Mehrere Prüfungen durch ein Prüfobjekt werden gleichzeitig (parallel) ausgeführt, nicht nacheinander. Du legst fest, wie viele Prüfungen parallel und von welchen Checkpoints erfolgen.

Es gibt zudem zwei prozentuale Mindestwerte. Diese sind der Prozentsatz der Checkpoints, die einen Fehler melden: Ein Wert, der wiedergibt, wann ein Fehler als unbestätigter Fehler erachtet wird, und ein weiterer Wert, der wiedergibt, wann ein Fehler als bestätigter Fehler gilt. Du entscheidest, wie viel Prozent erreicht sein müssen, um einen Fehler zu melden. Wird der erste Wert erreicht (zum Beispiel 30 %), gilt der Fehler als unbestätigter Fehler. Wird der zweite Wert erreicht (zum Beispiel 60 %), wird hingegen ein bestätigter Fehler angezeigt.

Wenn ein bedeutender (vom Nutzer definierter) Prozentsatz von Prüfungen einen Fehler wiedergibt, wird das Ergebnis sofort als bestätigter Fehler erachtet. Dann kann ein Alarm ausgelöst und sofort eine Benachrichtigung ausgesendet werden.

## Anwendungsbereich

Das Parallel-Monitoring lässt sich im folgenden Rahmen einsetzen:

-   Es ist für alle Prüfobjekttypen verfügbar.
-   Die Prüfungen eines Prüfobjekts müssen zu üblichen Monitoring-Frequenzen erfolgen. Diese sind jede Minute für grundlegende Prüfobjekte und alle 5 bis 15 Minuten für Browser-Prüfobjekte.
-   Für das Parallel-Monitoring gelten besondere Regeln bei der Auswahl von Checkpoints: Du wählst entweder aus allen Checkpoints (mindestens 5) oder du wählst aus den Checkpoints, die als *hoch verfügbar* (mindestens 3) markiert sind. Checkpoints *hoher Verfügbarkeit* sind im Allgemeinen die Standorte, an denen mehr als ein Server für den Test verfügbar ist.
-   In jedem Fall können maximal 50 Checkpoints ausgewählt werden.

## Monitoring-Daten

Auf Grundlage der parallelen Prüfungen errechnet Uptrends eine Gesamtmessung (mit grundlegenden Werten). Die Daten können so verwendet werden wie von anderen Prüfobjekten, z. B. in Dashboards, Warnmeldungen oder SLA-Berechnungen.

Die einzelnen Messungen werden an diesen Stellen verfügbar sein:

- im *Prüfobjektprotokoll*
- beim Öffnen der Gesamtmessung im *Prüfobjektprotokoll*. Du erhältst ein Detail-Pop-up, das auf die Teilmesswerte verweist
- pro Einzelmessung, für die wir die üblichen Debug-Informationen (Screenshots, Wasserfälle, Traceroutes usw.) aufzeichnen

## Vor- und Nachteile

Der Vorteil eines Parallel-Monitorings ist, dass es einen Fehler schneller und mit größerer Zuverlässigkeit entdeckt. Beachte, dass Letzteres von der Anzahl der verwendeten Checkpoints abhängt.

Ein Nachteil könnte sein, dass wir Transaktionsschritte nicht aggregieren oder einen Durchschnittswert des Wasserfallberichts zu Berichtszwecken berechnen (bei Transaktionen, Full Page Checks usw.).

Das Parallel-Monitoring kostet etwas mehr. Dafür bietet es jedoch eine schnellere Fehleraufdeckung und höhere Zuverlässigkeit. Die folgenden Beispiele vermitteln einen Eindruck zu den Preisen.

## Abonnements

Die Funktion wird in den folgenden Abonnements enthalten sein: Business und Enterprise.
Um das Parallel-Monitoring zu nutzen, musst du die Checkpoints für die gleichzeitigen Prüfungen einzeln auswählen. Das ist bei den Abos Business und Enterprise möglich. Andere Abos bieten diese Option nicht und sind daher nicht geeignet für das Parallel-Monitoring.

Die Berechnung der für das Parallel-Monitoring genutzten Credits wird in dem KB-Artikel [Preise für das Parallel-Monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring/pricing-calculation-examples" lang="de" >}}) erläutert.
