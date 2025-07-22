{
  "hero": {
    "title": "Multi-step Monitoring – Assertions"
  },
  "title": "Multi-step Monitoring – Assertions",
  "summary": "Grundlagen zu Assertions beim Multi-step API Monitoring.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-pruefpunkte",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-assertions"
}

In der Einführung zum [Multi-step Monitoring](/support/kb/synthetic-monitoring/api-monitoring/multi-step) haben wir gesagt, dass Prüfpunkte (Assertions) die Definition von Tests hinsichtlich des Inhalts der HTTP-Antworten ermöglichen. Dadurch können das richtige Verhalten und die Performance-Limits der APIs überwacht werden. In diesem Abschnitt werden die Assertion-Möglichkeiten im Detail beschrieben.

Jede Assertion wird auf folgende Weise definiert:

{{< Code/Symbol type="source" >}}Quelle{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Merkmal{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Vergleich{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}Zielwert{{< /Code/Symbol >}}

Zum Beispiel:

{{< Code/Symbol type="source" >}}Response Body in JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Produkte[0].Preis{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is greater than{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}100{{< /Code/Symbol >}}

-   **Assertion-Quelle**: Dieses Feld bestimmt, welche Eigenschaft der HTTP-Antwort geprüft wird. [Die verfügbaren Optionen werden in diesem Artikel erläutert](/support/kb/synthetic-monitoring/api-monitoring/multi-step-quellen).
-   **Assertion-Merkmal**: Einige Quelloptionen für Assertions (insbesondere Inhaltsüberprüfung und Optionen in Bezug auf den Header) erfordern weitere Angaben hinsichtlich Inhalt und Header. Dies wird für jeden Quelltyp [detaillierter erläutert](/support/kb/synthetic-monitoring/api-monitoring/multi-step-quellen).
-   **Assertion-Vergleich**: Dieses Feld drückt den Testtyp aus, der ausgeführt werden soll. Standardmäßig führen wir einen Vergleich der Art X gleich Y aus, aber es gibt mehr Vergleichsmöglichkeiten für Text und Zahlen. [Die Liste der Vergleiche findest Du hier](/support/kb/synthetic-monitoring/api-monitoring/multi-step-vergleichsoperationen).
-  **Assertion-Zielwert**: Für die meisten Prüfpunkte gilt, dass ein Vergleich mit einem bestimmten, von Dir angegebenen Wert erfolgen sollte. Dieser Wert ist der Zielwert. Abhängig von der Assertion-Quelle und dem Vergleichstyp kann dieser Wert ein Textwert, ein numerischer Wert oder auch ein boolescher Wert (wahr oder falsch) sein. Du kannst auch eine [Referenz zu einer Variable](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variablen) angeben, die einen dieser Werte darstellt.

## Was passiert, wenn die Assertion-Bedingung nicht erfüllt wurde?

Alle Prüfpunkte bzw. Assertions in einem Schritt werden abgearbeitet, sobald die HTTP-Anfrage ausgeführt und die Antwort analysiert wurde. In der Regel wird jeder Prüfpunkt für diesen Schritt bewertet, selbst wenn ein vorheriger Prüfpunkt einen Fehler meldete. Es ist also möglich, dass mehrere Prüfpunkte einen Ausfall für einen Schritt melden.

Wenn ein oder mehrere Prüfpunkte einen Fehler zurückgeben, wird die Ausführung des Prüfobjekts sofort gestoppt. Alle nachfolgenden Schritte werden nicht ausgeführt und das Prüfobjekt meldet einen Fehler. Der Fehlercode und die Beschreibung hängen von der Art des Ausfalls ab. Wenn mehrere Prüfpunkte einen Fehler zurückgeben, wird der erste von der Liste als wichtigster erachtet.

Manchmal kann es notwendig sein, die Ausführung einer Assertion ein zweites Mal zu versuchen, z. B., wenn du denkst, dass es an einem Zeitproblem gelegen haben kann, das zu einem falsch negativen Ergebnis führte. Eine Assertion wiederholt zu bewerten, ist möglich, und die Einzelheiten werden unter [Wiederholen bis erfolgreich]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step#msaretry" lang="de" >}}) erläutert.
