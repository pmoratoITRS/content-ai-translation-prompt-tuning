{
  "hero": {
    "title": "Variablen in Transaktionen nutzen"
  },
  "title": "Variablen in Transaktionen nutzen",
  "summary": "Ein Leitfaden, wie Variablen in Transaktionen genutzt werden.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/transaktionsvariablen",
  "translationKey": "[URL_1]
  "tableofcontents": true
}

In einigen Fällen musst du einen Wert, den dein Transaktionsprüfobjekt während der Ausführung des Skripts erfasst, eventuell speichern und wiederverwenden. In einem solchen Fall kannst du die Transaktion so konfigurieren, dass der Wert als **Variable** gespeichert wird und später vom Skript wieder genutzt wird. Wenn die Transaktion beispielsweise einen Prozess durchläuft, der eine Bestellnummer generiert, kannst du die Transaktion anweisen, diese in einer Variable zu speichern und dann mit einer Bestellnummer zu vergleichen, die später im Ablauf der Transaktion auf einer Bestätigungsseite angegeben wird. Damit kannst du sicherstellen, dass das Backend seine Aufgabe korrekt erfüllt hat.

## Eine Variable erzeugen

Um eine Variable zu erzeugen, nutze die [Aktion „Prüfe Elementinhalt“]([LINK_URL_1]). Variablen werden auf Grundlage des vollständigen Inhalts eines der Elemente der Seite erstellt. Um das zu speichernde Element zu benennen, musst du entweder [einen CSS-Selektor oder eine XPath-Abfrage]([LINK_URL_2]) verwenden.

1. Füge die Aktion [Prüfe Elementinhalt]([LINK_URL_3]) an der entsprechenden Stelle im Transaktionsskript ein. Der Elementinhalt, den du als Variable speichern möchtest, muss auf der Seite zum Zeitpunkt der Transaktion vorhanden sein.
2. Verweise die Inhaltsprüfung auf das richtige Element auf der Seite mit [einem CSS-Selektor oder einer XPath-Abfrage]([LINK_URL_4]). Solltest du hierbei Hilfe benötigen, [wende dich an das Support-Team]([LINK_URL_5]).
3. Die [Inhaltsprüfung]([LINK_URL_6]) prüft, ob das angegebene Element vorhanden ist, und verifiziert, dass der Inhalt einem bestimmten Wert entspricht (du kannst dabei reguläre Ausdrücke verwenden).
4. Gib für die Option **Variable zuordnen** den Namen der Variable in doppelte geschwungene Klammern ein: [INLINE_CODE_1]

In dem Beispiel unten wird im zweiten Schritt der Transaktion eine Bestellung aufgegeben (durch Klicken auf ein Element mit Kennung [INLINE_CODE_2] in Schritt 2.1), auf Vorhandensein des Elements [INLINE_CODE_3] geprüft und verifiziert, dass der Inhalt mit einem regulären Ausdruck übereinstimmt (in Schritt 2.2). Schließlich wird die Variable [INLINE_CODE_4] anhand der Option **Variable zuordnen** gespeichert. Die Variable enthält den gesamten Wert des Elements (in diesem Fall ist dies *"Your order number is: 1234"*).

![Erstellen einer Transaktionsvariable]([LINK_URL_7])

## Eine Variable anpassen

In Fällen wie beim obigen Beispiel kann der in der Variable erfasste Inhalt unnötigen Text enthalten. In diesem Fall ist der interessante Teil der Zeichenfolge in der Variable nur die Nummer selbst. Der Variableninhalt kann angepasst werden, indem du einen regulären Ausdruck anwendest, um bestimmte Teile zu behalten oder zu entfernen. Weitere Informationen findest du im Knowledge-Base-Artikel zur [Aktion „Inhalt der Variable anpassen“]([LINK_URL_8]).

1. Füge, nachdem die Variable im Transaktionsskript erstellt wurde, die Aktion **Inhalt der Variable anpassen** hinzu.
2. Fügen den Namen der Variable wie zuvor definiert ([INLINE_CODE_5] im obigen Beispiel) hinzu.
3. Wähle aus: **Behalte** oder **entferne** alles, das dem Muster des regulären Ausdrucks entspricht.
4. Füge den regulären Ausdruck hinzu.

![Transformieren einer Variable]([LINK_URL_9])

Das Ergebnis dieser Aktion, wie im obigen Beispiel angewendet, ist die isolierte Bestellnummer: *1234*. Beachte, dass dies die bestehende Variable überschreibt.

## Variablen verwenden

Da die Variable nun definiert und optional angepasst wurde, kann sie an anderer Stelle der Transaktion verwendet werden. Auf Variablen kann zu jeder Zeit nach ihrer Erstellung mit ihrem Namen verwiesen werden. Beispielsweise kann die isolierte Bestellnummer aus dem Beispiel als Wert in einer **Übernehmen**-Aktion genutzt und in ein Suchfeld eingegeben werden, um zu bestätigen, dass die Bestellung erfolgreich aufgegeben wurde. Beziehe dich einfach auf den Namen der Variablen (in diesem Fall [INLINE_CODE_6]).


![Verwenden einer Transaktionsvariable]([LINK_URL_10])



