{
  "hero": {
    "title": "Variablen in Transaktionen nutzen"
  },
  "title": "Variablen in Transaktionen nutzen",
  "summary": "Ein Leitfaden, wie Variablen in Transaktionen genutzt werden.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/transaktionsvariablen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-variables",
  "tableofcontents": true
}

In einigen Fällen musst du einen Wert, den dein Transaktionsprüfobjekt während der Ausführung des Skripts erfasst, eventuell speichern und wiederverwenden. In einem solchen Fall kannst du die Transaktion so konfigurieren, dass der Wert als **Variable** gespeichert wird und später vom Skript wieder genutzt wird. Wenn die Transaktion beispielsweise einen Prozess durchläuft, der eine Bestellnummer generiert, kannst du die Transaktion anweisen, diese in einer Variable zu speichern und dann mit einer Bestellnummer zu vergleichen, die später im Ablauf der Transaktion auf einer Bestätigungsseite angegeben wird. Damit kannst du sicherstellen, dass das Backend seine Aufgabe korrekt erfüllt hat.

## Eine Variable erzeugen

Um eine Variable zu erzeugen, nutze die [Aktion „Prüfe Elementinhalt“]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks#test-element-content" lang="de" >}}). Variablen werden auf Grundlage des vollständigen Inhalts eines der Elemente der Seite erstellt. Um das zu speichernde Element zu benennen, musst du entweder [einen CSS-Selektor oder eine XPath-Abfrage]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="de" >}}) verwenden.

1. Füge die Aktion [Prüfe Elementinhalt]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-action" lang="de" >}}) an der entsprechenden Stelle im Transaktionsskript ein. Der Elementinhalt, den du als Variable speichern möchtest, muss auf der Seite zum Zeitpunkt der Transaktion vorhanden sein.
2. Verweise die Inhaltsprüfung auf das richtige Element auf der Seite mit [einem CSS-Selektor oder einer XPath-Abfrage]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="de" >}}). Solltest du hierbei Hilfe benötigen, [wende dich an das Support-Team]({{< ref path="/contact" lang="de" >}}).
3. Die [Inhaltsprüfung]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}) prüft, ob das angegebene Element vorhanden ist, und verifiziert, dass der Inhalt einem bestimmten Wert entspricht (du kannst dabei reguläre Ausdrücke verwenden).
4. Gib für die Option **Variable zuordnen** den Namen der Variable in doppelte geschwungene Klammern ein: `{{variableName}}`

In dem Beispiel unten wird im zweiten Schritt der Transaktion eine Bestellung aufgegeben (durch Klicken auf ein Element mit Kennung `#confirmPurchase` in Schritt 2.1), auf Vorhandensein des Elements `#orderNumber` geprüft und verifiziert, dass der Inhalt mit einem regulären Ausdruck übereinstimmt (in Schritt 2.2). Schließlich wird die Variable `{{orderNumberLong}}` anhand der Option **Variable zuordnen** gespeichert. Die Variable enthält den gesamten Wert des Elements (in diesem Fall ist dies *"Your order number is: 1234"*).

![Erstellen einer Transaktionsvariable](/img/content/scr-transaction-variable-creation.min.png)

## Eine Variable anpassen

In Fällen wie beim obigen Beispiel kann der in der Variable erfasste Inhalt unnötigen Text enthalten. In diesem Fall ist der interessante Teil der Zeichenfolge in der Variable nur die Nummer selbst. Der Variableninhalt kann angepasst werden, indem du einen regulären Ausdruck anwendest, um bestimmte Teile zu behalten oder zu entfernen. Weitere Informationen findest du im Knowledge-Base-Artikel zur [Aktion „Inhalt der Variable anpassen“]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="de" >}}).

1. Füge, nachdem die Variable im Transaktionsskript erstellt wurde, die Aktion **Inhalt der Variable anpassen** hinzu.
2. Fügen den Namen der Variable wie zuvor definiert (`{{orderNumberLong}}` im obigen Beispiel) hinzu.
3. Wähle aus: **Behalte** oder **entferne** alles, das dem Muster des regulären Ausdrucks entspricht.
4. Füge den regulären Ausdruck hinzu.

![Transformieren einer Variable](/img/content/scr-transform-trn-variable.min.png)

Das Ergebnis dieser Aktion, wie im obigen Beispiel angewendet, ist die isolierte Bestellnummer: *1234*. Beachte, dass dies die bestehende Variable überschreibt.

## Variablen verwenden

Da die Variable nun definiert und optional angepasst wurde, kann sie an anderer Stelle der Transaktion verwendet werden. Auf Variablen kann zu jeder Zeit nach ihrer Erstellung mit ihrem Namen verwiesen werden. Beispielsweise kann die isolierte Bestellnummer aus dem Beispiel als Wert in einer **Übernehmen**-Aktion genutzt und in ein Suchfeld eingegeben werden, um zu bestätigen, dass die Bestellung erfolgreich aufgegeben wurde. Beziehe dich einfach auf den Namen der Variablen (in diesem Fall `{{orderNumberLong}}`).


![Verwenden einer Transaktionsvariable](/img/content/scr-trn-variable-use.min.png)



