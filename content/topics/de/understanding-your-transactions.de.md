{
  "hero": {
    "title": "Deine Transaktionen verstehen"
  },
  "title": "Deine Transaktionen verstehen",
  "summary": "Verstehen deiner Transaktionen, der vielen Pfade, die sie eventuell bieten, und das Wissen um die Vorbehalte, die du beim Einrichten eines Transaktions-Monitorings berücksichtigen solltest, führen zu einem besseren Monitoring und Ergebnis. ",
  "url": "/support/kb/synthetic-monitoring/transaktionen/deine-transaktionen-verstehen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-your-transactions"
}

Bevor du die Aufzeichnung und Skriptentwicklung deiner Transaktionen aufnimmst, solltest du einen Plan und ein gutes Verständnis deiner Transaktionen haben. Einen guten Plan zu erstellen, bevor du die Transaktion aufzeichnest, hilft dir bei der Aufzeichnung und dem Testen und vermeidet spätere Probleme.

## Die Transaktionen verstehen und skizzieren

Nicht alle Transaktionen laufen gleich ab. Eine gute Möglichkeit, deine Transaktionen eingehend zu verstehen, ist, sie zu skizzieren. Die ersten Schritte:

- Erstelle eine List der wichtigsten Aufgaben, die deine Nutzer auf deiner Website oder in deiner App ausführen müssen.
- Erzeuge ein Flussdiagramm der wichtigsten Aufgaben. Bedenke die unterschiedlichen Pfade, die Nutzer zum Erreichen unterschiedlicher Ziele auf deiner Website nehmen können (es kann auch mehrere Pfade für dasselbe Ziel geben).
- Stelle sicher, dass du sowohl die „Happy Paths“ (alles läuft nach Plan) und die „Unhappy Paths“ (Nutzer- und Systemfehler) skizzierst. Beispiele fehlgeschlagener Pfade umfassen Probleme wie eine ungültige Nutzer-Authentifizierung, nicht vorrätiger Bestand, ungültige Kreditkartendaten, ausgefallene unterstützende Systeme wie Händlerservices oder Datenbankfehler. Du solltest diese häufig auftretenden Probleme testen, um sicherzustellen, dass dein System korrekt antwortet.

Unten findest du wichtige Funktionen und User Journeys für eine einfache E-Commerce-Website. Das Diagramm beschreib mehrere „Happy Paths“, die ein Nutzer nehmen kann. Einige Aufgaben hängen von der erfolgreichen Erledigung anderer Aufgaben ab. Einige Aufgaben können noch weiter aufgeschlüsselt werden.

![](/img/content/3604c5bd-5c6e-4f07-acd7-0010408a7f18.png)

Um diese Beschreibung zu vereinfachen, konzentrieren wir uns auf die Shop-Funktion. Die Shop-Funktion umfasst die einfache Aufgabe, einen Artikel auszuwählen, in zum Warenkorb hinzuzufügen und den Warenkorb zu bearbeiten.

Du gerätst vielleicht in Versuchung, die Shop-Funktion zu erweitern und die Suche oder den Bezahlvorgang zu testen. Wir empfehlen, die Funktionen aufzuteilen, sodass du nur eine Aufgabe auf einmal prüfst.

![](/img/content/fc2b70c0-8ecf-4071-8f2b-67b3be0aa537.png)

## Was es noch zu bedenken gibt

Bevor du mit der Aufzeichnung deiner Transaktionen beginnst, beachte Folgendes:

-   Lies bitte den Artikel [Welche Transaktionen getestet werden sollten oder getestet werden können]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="de" >}}), um mehr darüber zu erfahren, welche Arten von Transaktionen du mit dem Transaktions-Monitoring überwachen kannst und solltest. Der Artikel enthält auch einen Hinweis zur Auswahl der Checkpoints für das Überwachen deiner Transaktionen.
-   Das Transaktions-Monitoring kann sich in der realen Welt für das Unternehmen auswirken, wenn Artikelbestände aufgebraucht werden und Händlergebühren auftreten. Bitte lies den Artikel [Transaktions-Monitoring – Vorbehalte, Tipps und Tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}}), bevor du ein Transaktionsprüfobjekt in den [Staging- oder Produktionsmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}) überführst.

Wenn all dies überwältigend erscheint, keine Sorge, unser [Support-Team]({{< ref path="contact" lang="de" >}}) steht bereit, dir über alle Hindernisse hinwegzuhelfen.
