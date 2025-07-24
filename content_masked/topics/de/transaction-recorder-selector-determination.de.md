{
  "hero": {
    "title": "Transaction Recorder – Selektorenbestimmung"
  },
  "title": "Transaction Recorder – Selektorenbestimmung",
  "summary": "Wenn du den Transaction Recorder verwendest, entscheidet der Recorder anhand mehrerer Faktoren darüber, wie einzelne Objekte der Seite zu identifizieren sind. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/transaction-recorder-selektoren-bestimmung",
  "translationKey": "[URL_1]
}

Wenn du den Transaction Recorder verwendest, gibt der Recorder eine lange Liste möglicher Selektoren zurück, die Uptrends in deinen Schritten der Self-Service Transaction nutzt, um Seitenobjekte zu identifizieren. Jeder Schritt und jede Aktion wird nur einen dieser Selektoren in deinem Skript einsetzen. Uptrends verwendet daher einen Algorithmus zur Auswahl des besten Selektors.

## Selektoren

Bei der Aufzeichnung deiner Transaktion mit dem Transaction Recorder, bei der du mit den verschiedenen Seitenobjekten interagierst, erzeugt der Recorder eine Liste möglicher Selektoren, um jedes Objekt zu identifizieren. Die Liste der möglichen Selektoren enthält verschiedene Text-, ID-, CSS- und XPath-Selektoren. Der Transaction Recorder erzeugt eine Liste der möglichen Selektoren für jedes Objekt. Der Recorder selbst verfügt aber nicht über eine Logik, um einen Selektor einem anderen vorzuziehen, sodass die Bestimmung von Uptrends‘ Servern während des Umwandlungsprozesses vorgenommen wird.

Um die besten Selektoren auszuwählen, berücksichtigt Uptrends die Werte der Selektoren und wählt einen Selektorwert und -typ, der nicht zu vage und nicht zu kompliziert ist sowie nicht zu häufig auf der Seite vorkommt.

[SHORTCODE_1]
**Hinweis**: Zeige die Selektoren an, indem du auf die Auslassungsschaltfläche [SHORTCODE_3]...[SHORTCODE_4] im Feld Selektorenwert klickst.
[SHORTCODE_2]

## Auswahlprozess

Die folgenden Schritte werden ausgeführt, um den besten Selektor zu finden:

1.  **Normalisierung**: Der Normalisierungsprozess filtert alle Selektoren heraus, die denselben Wert haben und nach denselben Attributen ausgewählt werden.
2.  **Entfernung nicht unterstützter Locators**: Bei dem Prozess werden alle Selektoren entfernt, die nicht von Self-Service Transactions unterstützt werden (Textselektoren).
3.  **Priorisierung der Elementtypen**: Der Prozess bevorzugt Selektoren auf Grundlage ihres Typs (nach Priorität geordnet): Text, ID, Name, CSS, XPath (Text), XPath (Attribute), XPath (Index), XPath (Node).
4.  **Priorisierung kürzerer Selektoren gegenüber längeren**: Uptrends priorisiert den Selektor auf Grundlage der Anzahl Zeichen im String und bevorzugt den kürzesten Selektor.
5.  **Priorisierung anhand der Zahl entsprechender Elemente**: Auf der Seite kann jeder Selektor mehrere Elemente haben, die derselben Beschreibung entsprechen. In diesem Prozess werden Selektoren auf Grundlage ihrer Eindeutigkeit priorisiert.
6.  **Priorisierung von Selektoren mit nur einer Entsprechung**: Uptrends gibt Selektoren die höchste Priorität, für die nur ein entsprechendes Element auf der Seite vorhanden ist.
7.  **Abschließende Auswahl**: Die sich ergebende Liste enthält nach Priorität geordnete Selektoren und Uptrends wählt für die Aktion den ersten Selektor in der Liste.
