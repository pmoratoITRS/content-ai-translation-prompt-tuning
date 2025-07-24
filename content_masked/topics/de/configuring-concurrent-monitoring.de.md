{
  "hero": {
    "title": "Konfiguration des Parallel-Monitorings"
  },
  "title": "Konfiguration des Parallel-Monitorings",
  "summary": "Ein Leitfaden zur Konfiguration des Parallel-Monitorings bei Uptrends",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/parallel-monitoring/konfiguration-parallel-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mit dem Parallel-Monitoring kannst du deine Prüfobjekte so konfigurieren, dass sie mehrere Prüfungen gleichzeitig von mehreren Checkpoints ausführen. Das bedeutet, dass du schnell und zuverlässig Informationen von mehreren Standorten hinsichtlich der Verfügbarkeit erhältst. Jeder Prüfobjekttyp kann für das Parallel-Monitoring konfiguriert werden. Die Einrichtung des Parallel-Monitorings ist großteils dieselbe wie für das Standard-Monitoring, aber es gibt einige wichtige Unterschiede und einige Einschränkungen zu berücksichtigen. Weitere Informationen zur Funktionsweise des Parallel-Monitorings findest du in [diesem Artikel]([LINK_URL_1]).  
  
Du kannst neue Parallel-Prüfobjekte einrichten, aber es ist auch möglich, das Parallel-Monitoring für bestehende Prüfobjekte zu aktivieren. Die Aktivierung des Parallel-Monitorings funktioniert in beiden Fällen gleich.

## Einrichten des Parallel-Monitorings

1.  Aktiviere das Parallel-Monitoring. Auf der Registerkarte [SHORTCODE_3]Allgemein[SHORTCODE_4] der Prüfobjekteinstellungen bzw. bei der Erstellung eines neuen Prüfobjekts findest du die Option **Parallel-Monitoring**. Aktiviere die Option durch Klicken des entsprechenden Optionsschalters.
2.  Es werden zwei neue Felder eingeblendet: **Schwellwert unbestätigter Fehler** und **Schwellwert bestätigter Fehler**. Diese Schwellwerte repräsentieren den prozentualen Anteil von Checkpoints, die einen Fehler erkennen können, bevor das Ergebnis des Parallel-Prüfobjekts insgesamt entsprechend als *unbestätigter* oder *bestätigter* Fehler aufgeführt wird. Fehler funktionieren bei Parallel-Prüfobjekten etwas anders – [dieser Artikel enthält eine vollständige Beschreibung]([LINK_URL_2]). Wir haben einige Standardwerte eingegeben, aber du kannst diese nach Bedarf anpassen. Beachte, dass der Schwellwert für unbestätigte Fehler immer unter oder gleich dem Schwellwert für bestätigte Fehler sein muss.  
      
    ![]([LINK_URL_3])
3.  Überprüfe als Nächstes bitte deine Checkpoint-Einstellungen. Wähle auf der Registerkarte [SHORTCODE_5]Checkpoints[SHORTCODE_6] die Checkpoints, die den Check simultan ausführen sollen. Du kannst bis zu 50 Checkpoints für jedes Parallel-Prüfobjekt auswählen.
4.  [SHORTCODE_1]**Hinweis:** Bei der Auswahl von Checkpoints für das Parallel-Monitoring hast du zwei Möglichkeiten, die auf dem Auswahlbildschirm der Checkpoints ersichtlich sein werden:
    1.  Die erste Option ist, alle Checkpoints verfügbar zu haben. In diesem Fall beträgt die Mindestzahl der zu wählenden Checkpoints für dein Parallel-Prüfobjekt 5.
    2.  Alternativ kannst bestimmen, nur Checkpoints *hoher Verfügbarkeit* zu verwenden. Diese eingeschränkte Reihe von Checkpoints haben eine erhöhte Verfügbarkeit, da wir an diesen Standorten mehrere Server betreiben. Das eliminiert praktisch den Umstand, dass ein oder mehrere Standorte aufgrund von Wartungsarbeiten oder Ausfällen für dein Parallel-Monitoring nicht verfügbar sind. Dies ist wichtig, denn wenn ein Standort ausfällt, kann sich das auf die Alarmierungsregeln des Parallel-Monitoring auswirken. Wenn du eine Reihe der Checkpoints *hoher Verfügbarkeit* nutzen möchtest, ist die Mindestzahl der Checkpoints 3.[SHORTCODE_2] 
5.  Solltest du ein neues Prüfobjekt erstellen, fülle die übrigen Pflichtfelder aus, abhängig vom gewählten Prüfobjekttyp. Klicke auf [SHORTCODE_7]Speichern[SHORTCODE_8] links unten, um das Prüfobjekt zu speichern.  
      
    Das Prüfobjekt sollte direkt beginnen, aggregierte Ergebnisse zu generieren. Weitere Informationen, wie du die Ergebnisse des Parallel-Monitorings interpretierst, findest du [hier]([LINK_URL_4]).

## Zu beachten

-   Wenn du die Schwellwerte für (un)bestätigte Fehler festlegst, berücksichtige die Anzahl ausgewählter Checkpoints. Es macht keinen Sinn, Werte wie 40 % und 50 % einzusetzen, wenn du nur 3 Checkpoints ausgewählt hast, da es mit einer solchen Einrichtung unmöglich sein wird, eine Fehlerrate von 40–50 % erhalten.
-   Parallel-Prüfobjekte folgen nicht dem [üblichen Muster]([LINK_URL_5]) des *Ok-unbestätigten-bestätigten* Fehlers. Aufgrund der Fehlerschwellwerteneinstellungen springt ein Parallel-Prüfobjekt eventuell direkt von *Ok > bestätigt*. Die Messung wird aussagekräftiger sein, da ein Fehler von mehreren Standorten gleichzeitig bestätigt wurde.
-   Wenn du ein Parallel-Monitoring einrichtest, beachte, dass ein Parallel-Prüfobjekt nach der Gesamtzahl ausgewählter Checkpoints bepreist wird. Wenn du zum Beispiel eine Transaktion mit 4 Credits bei 3 Checkpoints hoher Verfügbarkeit ausführst, beläuft sich der Gesamtpreis auf 4x3=12 Credits. Die Gesamtkosten für ein Prüfobjekt kannst du dem [Prüfobjekte-Überblick]([LINK_URL_6]) entnehmen.
