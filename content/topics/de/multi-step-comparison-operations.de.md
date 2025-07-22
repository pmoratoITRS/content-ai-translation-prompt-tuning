{
  "hero": {
    "title": "Multi-step Monitoring – Vergleichsoperatoren"
  },
  "title": "Multi-step Monitoring – Vergleichsoperatoren",
  "summary": "Erfahre mehr über die Vergleichsoperatoren, die bei der Einrichtung eines Multi-Step API Monitorings verfügbar sind.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-vergleichsoperationen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-comparison-operations",
  "TableOfContents": false
}

Wenn du einen Prüfpunkt für einen der Schritte in einem [Multi-step API Monitoring-Setup]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) erstellst, musst du festlegen, welche Art von Testablauf ausgeführt werden soll. Wähle eine der unten genannten Optionen. In der Beschreibung zu jeder Option bezieht sich *Quelle* auf den Wert des HTTP-Antwortattributs, der untersucht werden soll. *Zielwert* ist der festgelegte Wert, mit dem verglichen wird.

-   **Ist identisch mit**: Der Quellwert muss gleich dem Zielwert sein. Wir führen einen Vergleich unabhängig von Groß- oder Kleinschreibung durch.

-   **Ist nicht identisch mit**: Der Quellwert darf NICHT gleich dem Zielwert sein. Wir führen einen Vergleich unabhängig von Groß- oder Kleinschreibung durch.

-   **Beinhaltet**: Der Quellwert muss den Zielwert enthalten. Der Quell- wie auch der Zielwert werden beide als Text interpretiert (auch wenn sie eine Zahl enthalten). Der Zielwert muss an einer beliebigen Stelle im Text des Quellwerts vorhanden sein.

-   **Beinhaltet nicht**: Der Quellwert darf NICHT den Zielwert enthalten.

-   **Ist kleiner als**: Quell- und Zielwert müssen beide eine Zahl sein und die Bedingung Quelle < Ziel muss wahr sein.

-   **Ist kleiner als oder gleich**: Quell- und Zielwert müssen beide eine Zahl sein und die Bedingung Quelle <= Ziel muss wahr sein.

-   **Ist größer als**: Quell- und Zielwert müssen beide eine Zahl sein und die Bedingung Quelle > Ziel muss wahr sein.

-   **Ist größer als oder gleich**: Quell- und Zielwert müssen beide eine Zahl sein und die Bedingung Quelle >= Ziel muss wahr sein.

-   **Ist leer**: Quelle muss Text oder eine Zahl enthalten.

-   **Ist nicht leer**: Quelle muss Text oder eine Zahl enthalten.

-   **Ist null**: Quelle muss den Wert `null` (z. B. `"source": null`) enthalten.

-   **Ist nicht null**: Quelle darf NICHT den Wert `null` enthalten.

-   **Existiert**: Quelle muss in der Antwort vorhanden sein.

-   **Existiert nicht**: Quelle darf NICHT in der Antwort vorhanden sein.

-   **Sollte ignoriert werden**: Zeigt an, dass kein automatischer Test mit dem Quellwert ausgeführt werden soll. Diese Option kann verwendet werden, um die automatischen Prüfpunkte für Statuscode und Response vollständig aufzuheben. (siehe [Quelltypen und Eigenschaften]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="de" >}}))
