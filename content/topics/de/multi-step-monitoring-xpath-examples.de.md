{
  "hero": {
    "title": "XPath-Beispiele beim Multi-step Monitoring"
  },
  "title": "XPath-Beispiele beim Multi-step Monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/xpath-beispiele-beim-multi-step-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-xpath-examples"
}

In diesem Artikel findest Du einige Beispiele für das Extrahieren von Inhalten aus XML-Antworten mithilfe von XPath. Diese XPath-Abfragen ermöglichen Dir, eine XML-Antwort zu untersuchen, die von Deiner API oder Deinem Webservice im Rahmen eines [Multi-step API Monitorings](/support/kb/synthetic-monitoring/api-monitoring/multi-step) ausgegeben wird. Eine XPath-Abfrage definiert, welcher Teil der XML-Antwort Dich interessiert. Es ist üblicherweise ein Wert, der in einem der XML-Knoten enthalten ist. Du kannst den extrahierten Wert dahingehend prüfen, ob er [bestimmte Bedingungen erfüllt](/support/kb/synthetic-monitoring/api-monitoring/multi-step-pruefpunkte) (anhand von Assertions), oder zur späteren Nutzung [in einer Variablen speichern](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variablen).

Die XPath-Version in den Einrichtungen der Multi-step API Monitorings ist XPath 1.0. Das heißt, dass Funktionen, die in späteren XPath-Versionen eingeführt wurden, nicht unterstützt werden.

## Beispiel 1: Einfaches XML

Nehmen wir eine API oder einen Webservice, die Informationen über einen Produktbestand zurückgeben können. Wenn wir eine Anfrage an diese API stellen, wird sie Daten zu einem oder mehreren Produkten ausgeben. Gehen wir einmal davon aus, dass sie dieses einfache XML-Dokument erzeugt, wenn wir Daten zu Produkt P-12345 abfragen:

    <?xml version="1.0" encoding="utf-8"?>
      <Products>
        <ProductInfo Id="P-12345">
          <Name>Product 12345</Name>
          <Price>99.90</Price>
        </ProductInfo>
      </Products>

Der Wurzelknoten lautet **Products** und in ihm ist ein einzelner **ProductInfo**-Knoten, der das Produkt repräsentiert, nach dem wir gefragt haben. Darin sind ein **Name**-Knoten und ein **Price**-Knoten, beide mit Textinhalt.

Sobald wir das XML-Dokument von der API erhalten haben, können wir seinen Inhalt verifizieren, um festzustellen, ob die API richtig funktioniert. Beispielsweise können wir durch das Dokument zum **Name**-Knoten scrollen, um den Namen des Produkts zu extrahieren. Die folgende XPath-Abfrage ruft diesen Wert ab:

`/Products/ProductInfo/Name/text()`

Beachte, wie dieses Beispiel jeden Knoten in der Hierarchie nennt, um zum **Name**-Knoten zu gelangen und schließlich die **text()**-Funktion zu nutzen, um den Text innerhalb des **Name**-Knotens abzurufen.

Wenn wir diese XPath-Abfrage in einer Multi-step API Assertion verwenden, können wir verifizieren, dass der Wert tatsächlich im XML-Dokument existiert und den Wert hat, den wir erwarten:

![](/img/content/scr-MSA-xpath-assertion-example.min.png)

## Beispiel 2: Ein SOAP Envelope mit Präfixen

Wenn Deine API ein SOAP-Webservice ist, kann das zurückgegebene XML so ähnlich wie Folgendes aussehen:

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

Beachte, dass dieses XML-Dokument nicht nur die üblichen *xmlns*-Namensraumattribute enthält, die man bei SOAP XML erwartet, sondern auch einen Namensraum mit Präfix, **xmlns:product**, der die inneren Knoten mit der Produktinformation beschreibt. Dementsprechend hat jeder Knoten, angefangen mit dem **Envelope** bis hin zu den Produktdaten, ein Präfix. Auf die Knoten SOAP **Envelope** und **Body** wird sich anhand des Präfixes **soap:** bezogen. Der Knoten **GetProductInfoResponse** und alle seine inneren Knoten verwenden das Präfix **product:**.

Damit können wir eine XPath-Abfrage definieren, die über einen vollständig qualifizierten Knoten-Selektor für jeden Knoten in dem Pfad verfügt, den wir auswählen möchten. Die folgende XPath-Abfrage gibt den Wert 99,90 aus:

`/soap:Envelope/soap:Body/product:GetProductInfoResponse/product:GetProductInfoResult/product:ProductInfo/product:Price/text()`

Beachte, dass wir jedes Präfix für jeden Knoten in unserer Abfrage nennen müssen. Wenn wir ein Präfix auslassen, wird die XPath-Abfrage fehlschlagen, da XPath 1.0 erfordert, dass wir jeden Knoten mit vollem Namen, einschließlich seines Präfixes, nennen. Wir können diese Abfrage jedoch vereinfachen, da in dem Dokument nur ein Knoten für Produkt und nur ein Knoten **Price** vorhanden sind. Da hier alles eindeutig ist, können wir direkt zum Knoten **Price** mit dem unterordnenden Operator // navigieren:

`//product:Price/text()`

Beachte, dass das Präfix **product:** trotzdem verwendet werden muss.

Bisher haben wir den inneren Text eines Knotens extrahiert. Und wenn Du den Wert eines Attributs (etwa ein ID-Attribut mit Wert „P-12345“) extrahieren möchtest? Dann kannst Du den XPath-Operator @ nutzen. Diese XPath-Abfrage gibt den Wert P-12345 aus:

`//product:ProductInfo/@Id`

## Beispiel 3: SOAP-Daten mit mehreren Objekten

Bei unserem vorherigen Beispiel war alles eindeutig, da es in dem XML-Dokument für alles ein Präfix sowie nur ein einziges Objekt **product:ProductInfo** gab. Aber was passiert, wenn wir eine SOAP-Methode haben, die eine Liste von Objekten ausgibt? Nehmen wir dieses XML-Dokument, in dem mehr als ein Produkt aufgelistet wird (nur zwei, um es kurz zu halten):

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
              <product:ProductInfo Id="P-24680">
                <product:Name>Product 24680</product:Name>
                <product:Price>45.99</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

Wenn wir das erste Produkt und seinen Preis wählen möchten, könnten wir die folgende Abfrage verwenden, bei der 99,90 ausgegeben wird. Beachte, dass XPath-Arrays 1-basiert sind, also verwenden wir einen Indexwert von 1:

`//product:ProductInfo[1]/product:Price/text()`

Dementsprechend könnten wir den Preis des letzten Produkts wählen, wobei 45,99 ausgegeben würde:

`//product:ProductInfo[last()]/product:Price/text()`

Wir könnten auch ein Produkt aufgrund seines Product **Id-**Attributs wählen. Diese Abfrage findet ein Produkt mit Id gleich P-24680 und wählt seinen Preis, wobei 45,99 ausgegeben würde:

`//product:ProductInfo[@Id="P-24680"]/product:Price/text()`

## Beispiel 4: XML-Daten mit leeren Präfixen

Für dieses Beispiel nutzen wir wieder SOAP-Daten, aber es gilt für jedes XML-Dokument mit den gleichen Merkmalen. Bei unseren vorherigen SOAP-Beispielen hatten wir Glück, dass jeder Knoten über ein Präfix verfügte. Aber die XML-Antwort Deiner API kann XML ausgeben, bei dem nicht überall ein Präfix vorhanden ist.

Bei XPath 1.0 muss jeder Knoten, der einem Namensraum angehört, einschließlich seines Präfixes, spezifiziert werden. Dies wird schwierig, wenn einige Knoten über ein leeres Präfix verfügen. Du kannst in einer XPath-Abfrage kein leeres Präfix spezifizieren, sodass die Auswahl dieser Knoten etwas knifflig ist.

Nehmen wir das folgende XML, bei dem Präfixe für die Knoten SOAP Envelope und Body vorhanden sind, aber nicht für die inneren Knoten. Beachte, dass keine zusätzlichen Namensräume für die Produktknoten definiert wurden:

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
          <GetProductInfoResponse>
            <GetProductInfoResult>
              <ProductInfo Id="P-12345">
                <Name>Product 12345</Name>
                <Price>99.90</Price>
              </ProductInfo>
            </GetProductInfoResult>
          </GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

Dies funktioniert noch wie erwartet, da die Knoten ohne Präfix nicht in dem Namensraum sind. Diese XPath-Abfrage gibt den Wert 99,90 aus:

`//Price/text()`

Sehen wir uns nun eine Variation an, bei der ein zusätzlicher Namensraum vorhanden ist. Beachte das Attribut xmlns="http://myproduct.com" auf der Wurzelebene, bei dem kein Präfix angegeben ist (d. h., es hat ein leeres Präfix):

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns="http://myproduct.com">
        <soap:Body>
          <GetProductInfoResponse>
            <GetProductInfoResult>
              <ProductInfo Id="P-12345">
                <Name>Product 12345</Name>
                <Price>99.90</Price>
              </ProductInfo>
            </GetProductInfoResult>
          </GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

In diesem Fall sind die inneren Knoten Teil des Namensraums, aber wir können sie nicht auf übliche Weise auswählen, da ihr Namensraum-Präfix leer ist. Daher funktioniert die folgende Abfrage nicht und gibt einen leeren Wert zurück:

`//Price/text()`

Leider gibt es keine Möglichkeit, in einer XPath-Abfrage ein leeres Präfix zu spezifizieren. Aber es gibt einen Weg, wie man das Problem des leeren Präfixes vermeidet. Wir können die XPath-Funktion **local-name()** verwenden, wodurch wir einen Knoten anhand seines Namens wählen können, ohne sein Präfix anzugeben:

`//*[local-name()="Price"]/text()`

Die Struktur dieser Anfrage:

// unterordnender Operator: wählt alle untergeordneten Knoten von der Wurzel  
\* Wildcard-Operator: jeder Knoten, unabhängig vom Knotennamen  
`[local-name()="Price"]`: wählt nur Knoten, die einen lokalen Namen (d. h., es schließt alle Präfixe aus) gleich Price haben  
`text()`: select the inner text of the selected node(s)

Sehen wir unsere vorherigen Beispiele an, bei dem mehrere Knoten ProductInfo im XML vorkamen. Wir können mehrere Strategien kombinieren, um die für uns interessanten Knoten auszuwählen. Bei dieser Abfrage wird der Knoten ProductInfo mit Id gleich P-24680 gewählt und dann der innere Text seines Price-Knotens abgerufen:

`//*[local-name()="ProductInfo"][@Id="P-24680"]/*[local-name()="Price"]/text()`

## Beispiel 5: XPath-Funktionen

Bei den vorherigen Beispielen haben wir XPath-Abfragen genutzt, um das Vorhandensein eines oder mehrerer Knoten in einem XML-Dokument zu verifizieren und den Inhalt eines Knoten oder eines Knotenattributs auszugeben. Neben der Suche nach Knoten und ihren Inhalten kannst Du mit XPath auch bestimmte Funktionen ausführen. Bedenke, dass nur Funktionen von XPath 1.0 verfügbar sind. Hier sind einige Beispiele:

| **Funktion**                                                                                                                                                                                                                                                                                                                  | **Beispiel-Abfrage**                  | **Wert** |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|----------|
| Die Funktion **count()** zählt, wie viele Knoten anhand des von Dir spezifizierten Arguments gefunden wurden. Es gibt einen numerischen Wert aus, den Du in einer Assertion nutzen kannst. Beispielsweise kannst Du eine Assertion einrichten, die prüft, ob die Anzahl der ausgegebenen Produkte größer oder gleich 100 ist. | count(//ProductInfo)                  | 2        |
| Die Funktion **contains()** prüft, ob der ausgewählte Zeichenfolgen-Wert die untergeordnete Zeichenfolge enthält, die Du spezifiziert hast. Sie gibt entweder Wahr oder Falsch aus.                                                                                                                                           | contains(//ProductInfo/Name, "12345") | True     |
| Die Funktion **sum()** berechnet die Summe der (numerischen Werte) ausgewählten Knoten.                                                                                                                                                                                                                                       | sum(//ProductInfo/Price)              | 145.89   |
