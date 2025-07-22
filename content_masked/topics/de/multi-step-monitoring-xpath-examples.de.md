{
  "hero": {
    "title": "XPath-Beispiele beim Multi-step Monitoring"
  },
  "title": "XPath-Beispiele beim Multi-step Monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/xpath-beispiele-beim-multi-step-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In diesem Artikel findest Du einige Beispiele für das Extrahieren von Inhalten aus XML-Antworten mithilfe von XPath. Diese XPath-Abfragen ermöglichen Dir, eine XML-Antwort zu untersuchen, die von Deiner API oder Deinem Webservice im Rahmen eines [Multi-step API Monitorings]([LINK_URL_1]) ausgegeben wird. Eine XPath-Abfrage definiert, welcher Teil der XML-Antwort Dich interessiert. Es ist üblicherweise ein Wert, der in einem der XML-Knoten enthalten ist. Du kannst den extrahierten Wert dahingehend prüfen, ob er [bestimmte Bedingungen erfüllt]([LINK_URL_2]) (anhand von Assertions), oder zur späteren Nutzung [in einer Variablen speichern]([LINK_URL_3]).

Die XPath-Version in den Einrichtungen der Multi-step API Monitorings ist XPath 1.0. Das heißt, dass Funktionen, die in späteren XPath-Versionen eingeführt wurden, nicht unterstützt werden.

## Beispiel 1: Einfaches XML

Nehmen wir eine API oder einen Webservice, die Informationen über einen Produktbestand zurückgeben können. Wenn wir eine Anfrage an diese API stellen, wird sie Daten zu einem oder mehreren Produkten ausgeben. Gehen wir einmal davon aus, dass sie dieses einfache XML-Dokument erzeugt, wenn wir Daten zu Produkt P-12345 abfragen:

    [HTML_TAG_1]
      [HTML_TAG_2]
        [HTML_TAG_3]
          [HTML_TAG_4]Product 12345[HTML_TAG_5]
          [HTML_TAG_6]99.90[HTML_TAG_7]
        [HTML_TAG_8]
      [HTML_TAG_9]

Der Wurzelknoten lautet **Products** und in ihm ist ein einzelner **ProductInfo**-Knoten, der das Produkt repräsentiert, nach dem wir gefragt haben. Darin sind ein **Name**-Knoten und ein **Price**-Knoten, beide mit Textinhalt.

Sobald wir das XML-Dokument von der API erhalten haben, können wir seinen Inhalt verifizieren, um festzustellen, ob die API richtig funktioniert. Beispielsweise können wir durch das Dokument zum **Name**-Knoten scrollen, um den Namen des Produkts zu extrahieren. Die folgende XPath-Abfrage ruft diesen Wert ab:

[INLINE_CODE_1]

Beachte, wie dieses Beispiel jeden Knoten in der Hierarchie nennt, um zum **Name**-Knoten zu gelangen und schließlich die **text()**-Funktion zu nutzen, um den Text innerhalb des **Name**-Knotens abzurufen.

Wenn wir diese XPath-Abfrage in einer Multi-step API Assertion verwenden, können wir verifizieren, dass der Wert tatsächlich im XML-Dokument existiert und den Wert hat, den wir erwarten:

![]([LINK_URL_4])

## Beispiel 2: Ein SOAP Envelope mit Präfixen

Wenn Deine API ein SOAP-Webservice ist, kann das zurückgegebene XML so ähnlich wie Folgendes aussehen:

    [HTML_TAG_10]
      [HTML_TAG_11]
        [HTML_TAG_12]
          [HTML_TAG_13]
            [HTML_TAG_14]
              [HTML_TAG_15]
                [HTML_TAG_16]Product 12345[HTML_TAG_17]
                [HTML_TAG_18]99.90[HTML_TAG_19]
              [HTML_TAG_20]
            [HTML_TAG_21]
          [HTML_TAG_22]
        [HTML_TAG_23]
      [HTML_TAG_24]

Beachte, dass dieses XML-Dokument nicht nur die üblichen *xmlns*-Namensraumattribute enthält, die man bei SOAP XML erwartet, sondern auch einen Namensraum mit Präfix, **xmlns:product**, der die inneren Knoten mit der Produktinformation beschreibt. Dementsprechend hat jeder Knoten, angefangen mit dem **Envelope** bis hin zu den Produktdaten, ein Präfix. Auf die Knoten SOAP **Envelope** und **Body** wird sich anhand des Präfixes **soap:** bezogen. Der Knoten **GetProductInfoResponse** und alle seine inneren Knoten verwenden das Präfix **product:**.

Damit können wir eine XPath-Abfrage definieren, die über einen vollständig qualifizierten Knoten-Selektor für jeden Knoten in dem Pfad verfügt, den wir auswählen möchten. Die folgende XPath-Abfrage gibt den Wert 99,90 aus:

[INLINE_CODE_2]

Beachte, dass wir jedes Präfix für jeden Knoten in unserer Abfrage nennen müssen. Wenn wir ein Präfix auslassen, wird die XPath-Abfrage fehlschlagen, da XPath 1.0 erfordert, dass wir jeden Knoten mit vollem Namen, einschließlich seines Präfixes, nennen. Wir können diese Abfrage jedoch vereinfachen, da in dem Dokument nur ein Knoten für Produkt und nur ein Knoten **Price** vorhanden sind. Da hier alles eindeutig ist, können wir direkt zum Knoten **Price** mit dem unterordnenden Operator // navigieren:

[INLINE_CODE_3]

Beachte, dass das Präfix **product:** trotzdem verwendet werden muss.

Bisher haben wir den inneren Text eines Knotens extrahiert. Und wenn Du den Wert eines Attributs (etwa ein ID-Attribut mit Wert „P-12345“) extrahieren möchtest? Dann kannst Du den XPath-Operator @ nutzen. Diese XPath-Abfrage gibt den Wert P-12345 aus:

[INLINE_CODE_4]

## Beispiel 3: SOAP-Daten mit mehreren Objekten

Bei unserem vorherigen Beispiel war alles eindeutig, da es in dem XML-Dokument für alles ein Präfix sowie nur ein einziges Objekt **product:ProductInfo** gab. Aber was passiert, wenn wir eine SOAP-Methode haben, die eine Liste von Objekten ausgibt? Nehmen wir dieses XML-Dokument, in dem mehr als ein Produkt aufgelistet wird (nur zwei, um es kurz zu halten):

    [HTML_TAG_25]
      [HTML_TAG_26]
        [HTML_TAG_27]
          [HTML_TAG_28]
            [HTML_TAG_29]
              [HTML_TAG_30]
                [HTML_TAG_31]Product 12345[HTML_TAG_32]
                [HTML_TAG_33]99.90[HTML_TAG_34]
              [HTML_TAG_35]
              [HTML_TAG_36]
                [HTML_TAG_37]Product 24680[HTML_TAG_38]
                [HTML_TAG_39]45.99[HTML_TAG_40]
              [HTML_TAG_41]
            [HTML_TAG_42]
          [HTML_TAG_43]
        [HTML_TAG_44]
      [HTML_TAG_45]

Wenn wir das erste Produkt und seinen Preis wählen möchten, könnten wir die folgende Abfrage verwenden, bei der 99,90 ausgegeben wird. Beachte, dass XPath-Arrays 1-basiert sind, also verwenden wir einen Indexwert von 1:

[INLINE_CODE_5]

Dementsprechend könnten wir den Preis des letzten Produkts wählen, wobei 45,99 ausgegeben würde:

[INLINE_CODE_6]

Wir könnten auch ein Produkt aufgrund seines Product **Id-**Attributs wählen. Diese Abfrage findet ein Produkt mit Id gleich P-24680 und wählt seinen Preis, wobei 45,99 ausgegeben würde:

[INLINE_CODE_7]

## Beispiel 4: XML-Daten mit leeren Präfixen

Für dieses Beispiel nutzen wir wieder SOAP-Daten, aber es gilt für jedes XML-Dokument mit den gleichen Merkmalen. Bei unseren vorherigen SOAP-Beispielen hatten wir Glück, dass jeder Knoten über ein Präfix verfügte. Aber die XML-Antwort Deiner API kann XML ausgeben, bei dem nicht überall ein Präfix vorhanden ist.

Bei XPath 1.0 muss jeder Knoten, der einem Namensraum angehört, einschließlich seines Präfixes, spezifiziert werden. Dies wird schwierig, wenn einige Knoten über ein leeres Präfix verfügen. Du kannst in einer XPath-Abfrage kein leeres Präfix spezifizieren, sodass die Auswahl dieser Knoten etwas knifflig ist.

Nehmen wir das folgende XML, bei dem Präfixe für die Knoten SOAP Envelope und Body vorhanden sind, aber nicht für die inneren Knoten. Beachte, dass keine zusätzlichen Namensräume für die Produktknoten definiert wurden:

    [HTML_TAG_46]
      [HTML_TAG_47]
        [HTML_TAG_48]
          [HTML_TAG_49]
            [HTML_TAG_50]
              [HTML_TAG_51]
                [HTML_TAG_52]Product 12345[HTML_TAG_53]
                [HTML_TAG_54]99.90[HTML_TAG_55]
              [HTML_TAG_56]
            [HTML_TAG_57]
          [HTML_TAG_58]
        [HTML_TAG_59]
      [HTML_TAG_60]

Dies funktioniert noch wie erwartet, da die Knoten ohne Präfix nicht in dem Namensraum sind. Diese XPath-Abfrage gibt den Wert 99,90 aus:

[INLINE_CODE_8]

Sehen wir uns nun eine Variation an, bei der ein zusätzlicher Namensraum vorhanden ist. Beachte das Attribut xmlns="[URL_1] auf der Wurzelebene, bei dem kein Präfix angegeben ist (d. h., es hat ein leeres Präfix):

    [HTML_TAG_61]
      [HTML_TAG_62]
        [HTML_TAG_63]
          [HTML_TAG_64]
            [HTML_TAG_65]
              [HTML_TAG_66]
                [HTML_TAG_67]Product 12345[HTML_TAG_68]
                [HTML_TAG_69]99.90[HTML_TAG_70]
              [HTML_TAG_71]
            [HTML_TAG_72]
          [HTML_TAG_73]
        [HTML_TAG_74]
      [HTML_TAG_75]

In diesem Fall sind die inneren Knoten Teil des Namensraums, aber wir können sie nicht auf übliche Weise auswählen, da ihr Namensraum-Präfix leer ist. Daher funktioniert die folgende Abfrage nicht und gibt einen leeren Wert zurück:

[INLINE_CODE_9]

Leider gibt es keine Möglichkeit, in einer XPath-Abfrage ein leeres Präfix zu spezifizieren. Aber es gibt einen Weg, wie man das Problem des leeren Präfixes vermeidet. Wir können die XPath-Funktion **local-name()** verwenden, wodurch wir einen Knoten anhand seines Namens wählen können, ohne sein Präfix anzugeben:

[INLINE_CODE_10]

Die Struktur dieser Anfrage:

// unterordnender Operator: wählt alle untergeordneten Knoten von der Wurzel  
\* Wildcard-Operator: jeder Knoten, unabhängig vom Knotennamen  
[INLINE_CODE_11]: wählt nur Knoten, die einen lokalen Namen (d. h., es schließt alle Präfixe aus) gleich Price haben  
[INLINE_CODE_12]: select the inner text of the selected node(s)

Sehen wir unsere vorherigen Beispiele an, bei dem mehrere Knoten ProductInfo im XML vorkamen. Wir können mehrere Strategien kombinieren, um die für uns interessanten Knoten auszuwählen. Bei dieser Abfrage wird der Knoten ProductInfo mit Id gleich P-24680 gewählt und dann der innere Text seines Price-Knotens abgerufen:

[INLINE_CODE_13]

## Beispiel 5: XPath-Funktionen

Bei den vorherigen Beispielen haben wir XPath-Abfragen genutzt, um das Vorhandensein eines oder mehrerer Knoten in einem XML-Dokument zu verifizieren und den Inhalt eines Knoten oder eines Knotenattributs auszugeben. Neben der Suche nach Knoten und ihren Inhalten kannst Du mit XPath auch bestimmte Funktionen ausführen. Bedenke, dass nur Funktionen von XPath 1.0 verfügbar sind. Hier sind einige Beispiele:

| **Funktion**                                                                                                                                                                                                                                                                                                                  | **Beispiel-Abfrage**                  | **Wert** |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|----------|
| Die Funktion **count()** zählt, wie viele Knoten anhand des von Dir spezifizierten Arguments gefunden wurden. Es gibt einen numerischen Wert aus, den Du in einer Assertion nutzen kannst. Beispielsweise kannst Du eine Assertion einrichten, die prüft, ob die Anzahl der ausgegebenen Produkte größer oder gleich 100 ist. | count(//ProductInfo)                  | 2        |
| Die Funktion **contains()** prüft, ob der ausgewählte Zeichenfolgen-Wert die untergeordnete Zeichenfolge enthält, die Du spezifiziert hast. Sie gibt entweder Wahr oder Falsch aus.                                                                                                                                           | contains(//ProductInfo/Name, "12345") | True     |
| Die Funktion **sum()** berechnet die Summe der (numerischen Werte) ausgewählten Knoten.                                                                                                                                                                                                                                       | sum(//ProductInfo/Price)              | 145.89   |
