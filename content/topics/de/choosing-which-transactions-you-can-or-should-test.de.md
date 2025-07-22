{
  "hero": {
    "title": "Welche Transaktionen getestet werden sollten oder getestet werden können"
  },
  "title": "Welche Transaktionen getestet werden sollten oder getestet werden können",
  "url": "/support/kb/synthetic-monitoring/transaktionen/welche-transaktionen-getestet-werden-koennen-sollten",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/choosing-which-transactions-you-can-or-should-test"
}

Die Bestimmung, welche Transaktionen beim Web Application Monitoring getestet werden sollten, ist ein wichtiger erster Schritt bei der Einrichtung einer erfolgreichen Transaktions-Monitoring-Strategie.

## Welche Transaktionen kann ich überwachen?

Die Frage sollte eigentlich lauten „Welche Transaktionen kann ich NICHT mit dem Web Application Monitoring überwachen." Mit einem Webanwendungs-Monitoring kannst du nahezu jede Aktion prüfen, die ein Nutzer auf deiner Website oder bei deinem Service ausführen muss. Das gibt dir eine große Auswahl an Monitoring-Möglichkeiten. Einige der üblichen Transaktionen, die du mit dem Web Application Monitoring verifizieren solltest, sind

-   An- und Abmeldefunktion
-   Suchfunktion
-   Termineinrichtung oder Reservierungen
-   Warenkorb-Transaktionen: Hinzufügen, Entfernen und Auswahl von Produktvariationen
-   Formular ausfüllen und einreichen, insbesondere solche, die mit anderen Services wie Adressenverifizierung oder Versandkostenberechnung verknüpft sind
-   Finanztransaktionen

## Auswahl der geeignetsten Transaktionen für ein Monitoring

Deine Website verfügt wahrscheinlich über viele Nutzerszenarien. Du kannst aber nicht jedes Szenario testen, wie also triffst du die beste Wahl? Natürlich **solltest du solche Transaktionen testen, die für den Erfolg deiner Website wichtig sind und auf die sich deine Nutzer verlassen** (viele haben wir bereits oben genannt). Du solltest deine [Nutzerszenarien skizzieren]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="en" >}}) und in bestimmte Aufgaben gliedern, beispielsweise das Anmelden oder einen Artikel zu einem Warenkorb hinzuzufügen. Erstelle Prüfobjekte, die sich auf eindeutige Bereiche deines Systems beziehen.  Getrennte Prüfobjekte zur Überwachung jedes Aspekts eines Nutzerszenarios bieten bessere Berichte und Warnmeldungen. Um beispielsweise einen Warenkorb zu testen, navigiere zur Seite, füge dem Warenkorb einen Artikel hinzu, überprüfen den Warenkorb und beende die Transaktion. Mit diesem Prüfobjekt überwachst du die Verfügbarkeit der Seite, die mit dem Produkt und Nutzerdaten verbundenen Datenbanken sowie die Transaktionsladezeiten. Du solltest Transaktionen prüfen, die

-   auf Server zugreifen, um die Website-Verfügbarkeit, Korrektheit der Antwort und Antwortzeiten zu prüfen;
-   Datenbankzugang und -antworten erfordern –  wenn dein System mehr als eine Datenbank nutzt, richte Prüfobjekte ein, die jede Datenbank ansprechen;
-   externe Services und Funktionen nutzen –  wenn deine Transaktion beispielsweise Services von Fremdanbietern nutzt, etwa Standort- und Adressenprüfung, solltest du diese alle auf Verfügbarkeit überwachen.

**Hinweis:** Die Überwachung der von dir gewählten Transaktionen kann unerwartete Nebeneffekte haben. Lies unseren Artikel [Transaktions-Monitoring – Vorbehalte, Tipps und Tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}}), bevor du ein Prüfobjekt in den Produktions- oder Staging-Modus setzt.

## Eine Anmerkung zur Auswahl von Teststandorten

Wie du wahrscheinlich weißt, kann sich der Standort des Nutzers enorm auf die Transaktions-Performance und den Erfolg auswirken. Bedenke die Auswahl deiner Checkpoint-Standorte sorgfältig. Wir empfehlen nicht, für ein einzelnes Prüfobjekt die ganze Bandbreite der verfügbaren Checkpoints zu aktivieren. Eine umfassende Auswahl kann die Identifizierung von Performance-Problemen und Fehlern, die sich auf ein bestimmtes Gebiet beschränken, erschweren. Hier sagen wir dir, warum.

1.  Wenn du ein großes Testgebiet ausgewählt hast, erreicht eine fehlgeschlagene Prüfung an einem einzelnen Checkpoint eventuell nicht die Alarmierungsphase. Wenn ein Checkpoint eine nicht erfüllte Fehlerbedingung erkennt, wählt Uptrends einen anderen Checkpoint nach dem Zufallsprinzip aus deinen gewählten Teststandorten aus, um den Fehler zu verifizieren. Wenn diese Prüfung zur Verifizierung in einer anderen Region durchgeführt wird, kann Uptrends den Fehler eventuell nicht bestätigen, sodass keine Warnmeldung ausgelöst wird. Daher kann ein standortbedingter Fehler fortbestehen, bis du in deinen Prüfobjektprotokollen ein Muster feststellst, oder bis eine Prüfung zur Verifizierung in derselben Region durchgeführt wird, in der das Problem zuerst auftrat.

    **Hinweis:** Wählst du zu wenige Checkpoints, kann sich das ebenfalls auf die Wirksamkeit des Monitorings auswirken. Du musst mindestens drei Checkpoints für ein Prüfobjekt aktivieren, wir empfehlen jedoch mehr. Bedenke bei jeder Transaktion die Auswahl deiner Checkpoint-Standorte sorgfältig.

2.  Performance hängt sehr vom Standort eines Nutzers ab – aufgrund von Netzwerklatenz und -qualität. An einigen Standorten kann es zu langsamen Antwortzeiten kommen, die unbemerkt bleiben, weil sie gerade eben das Minimum der Antwortzeit überschreiten, oder die schlechten Antwortzeiten bleiben unbestätigt und es wird keine Meldung gesendet. Die mangelnde Häufigkeit der Prüfungen bedeutet, das langsame Antwortzeiten sich bei Performance-Berichten nicht stark auswirken und daher leicht zu übersehen sind.

**Lösung**: Dupliziere das Prüfobjekt  und richte bei den Kopien die Prüfung spezieller Regionen ein. Damit erhältst du Berichte, die das Nutzererlebnis in der jeweiligen Region besser darstellen. Mit der geringeren Anzahl Checkpoints kann Uptrends lokale Probleme erfassen und sie dir melden; bei breit gestreuten Checkpoint-Gebieten können diese ansonsten unbemerkt bleiben.
