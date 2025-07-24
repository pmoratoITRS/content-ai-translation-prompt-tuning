{
  "hero": {
    "title": "Die Ergebnisse deines Parallel-Monitorings"
  },
  "title": "Die Ergebnisse deines Parallel-Monitorings",
  "summary": "Wo du die Ergebnisse des Parallel-Monitorings findest und was sie bedeuten. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/parallel-monitoring/ergebnisse-parallel-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Beim Parallel-Monitoring werden die Prüf-Ergebnisse etwas anders aufgebaut, als beim Standard-Monitoring. Es gibt mehrere Punkte bei den Prüf-Ergebnissen des Parallel-Monitorings, die es von den Ergebnissen eines Standard-Monitorings unterscheiden. Das Ergebnis eines Parallel-Prüfobjekts besteht aus mehreren einzelnen Prüfungen, jede mit eigenen Werten und Resultaten. In diesem Artikel sehen wir uns an, wie die Prüfungsdaten interpretiert werden können, um dein Parallel-Monitoring optimal auszuschöpfen. Wenn du das Parallel-Monitoring aufnehmen möchtest, findest du [hier einen Leitfaden]([LINK_URL_1]), wie du es einrichten kannst..

## Ergebnisse des Parallel-Monitorings identifizieren

Im Prüfobjektprotokoll kannst du die Prüf-Ergebnisse eines Parallel-Prüfobjekts anhand des ![]([LINK_URL_2])-Symbols erkennen. Diese Ergebnisse führen keine Checkpoints in der Spalte **Checkpoint**, sondern *Mehrere Standorte* auf. Alternativ dazu verfügt jedes Parallel-Prüfobjekt über sein eigenes spezielles Dashboard, das entsprechende Daten unabhängig vom Prüfobjekttyp anzeigt. Du erreichst das Parallel-Monitoring-Dashboard durch Zeigen auf den QuickInfo-Tag eines Prüfergebnisses. Klicke in dem erscheinenden QuickInfo-Feld auf *Dashboard*.

![]([LINK_URL_3])

## Die Ergebnisse deines Parallel-Monitorings interpretieren

Klicke auf den Eintrag eines Prüfobjekts im Prüfobjektprotokoll, um das Gesamtergebnis der Prüfung anzuzeigen.

![Screenshot Prüfobjektdetails Parallel-Monitoring]([LINK_URL_4])

Das Bild zeigt, dass das Pop-up-Fenster für die gesamten Prüfungsdaten die Checkpoints nennt, die die Prüfung ausgeführt haben. Der angezeigte Wert für **Gesamtzeit** ist der Durchschnittswert der Ladezeiten aller einzelnen Prüfungen, von jedem einzelnen Checkpoint. Das gezeigte **Ergebnis** ist das Gesamtergebnis der Prüfung. Wenn das Gesamtergebnis der Prüfung die in den Prüfobjekteinstellungen festgelegten Bedingungen erfüllt, melden wir den Ergebniscode *0 - OK*. Andernfalls melden wir einen Fehler. Fehler funktionieren beim Parallel-Monitoring etwas anders – [hier findest du eine vollständige Beschreibung]([LINK_URL_5]).

Einen detaillierten Überblick zu den einzelnen Messungen, die wir für das Gesamtergebnis durchgeführt haben, erhältst du durch Klicken auf die Checkpoint-Namen. Zum Beispiel: Wenn wir auf *Birmingham-2* im vorherigen Screenshot klicken würden, sähen wir die detaillierten Ergebnisse der Prüfung, der vom Checkpoint in Birmingham-2 ausgeführt wurde.

![Screenshot Parallel-Monitoring einzelne Checkpoint-Details]([LINK_URL_6])

Dieser Überblick enthält Daten wie die detaillierte [Aufschlüsselung der Gesamtzeit]([LINK_URL_7]) der Prüfung, die von diesem speziellen Checkpoint ausgeführt wurde. Er enthält auch einen Link, der dich zum Gesamtergebnis der Prüfung (*Alle Überwachungen anzeigen*) zurückführt.

## Einzelne Prüfungen im Prüfobjektprotokoll anzeigen

Standardmäßig zeigt das Prüfobjektprotokoll nur das Gesamtergebnis der Prüfung. Detaillierte Informationen zu den einzelnen Messungen findest du, wenn du das Pop-up-Fenster für die Prüfung wie zuvor beschrieben nutzt. Du kannst in deinem Prüfobjektprotokoll einstellen, dass sowohl das Gesamtergebnis wie auch das Ergebnis jeder einzelnen Prüfung angezeigt werden. Nutze dafür den Dashboard-Filter oben rechts und aktiviere *Teilprüfungen anzeigen*.

![]([LINK_URL_8])

Oder klicke auf das Zahnradsymbol oben rechts in der Kachel des Prüfobjektprotokolls (eventuell musst du erst mit der Maus über die Kachel fahren, damit es erscheint) und aktiviere **Teilprüfungen anzeigen**. Speichere die Konfiguration durch Klicken auf [SHORTCODE_1]Übernehmen[SHORTCODE_2] unten rechts vom eingeblendeten Optionsmenü.

![]([LINK_URL_9])

Das Prüfobjektprotokoll enthält nun beides: die Gesamtmessungen (durch das Symbol ![]([LINK_URL_10]) gekennzeichnet), die *Mehrere Standorte* angeben, und jede einzelne Prüfung, die den jeweiligen Checkpoint angibt. Dieselben Informationen werden in den verfügbaren Kacheln zur Fehleraufschlüsselung angezeigt.
