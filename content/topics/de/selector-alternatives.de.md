{
  "hero": {
    "title": "Selektoralternativen"
  },
  "title": "Selektoralternativen finden",
  "summary": "Manchmal funktionieren Selektoren nicht oder sie funktionieren nur teilweise. In diesem Artikel behandeln wir einige der üblichen Selektorprobleme und schlagen Möglichkeiten zur Behebung vor.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/selektoralternativen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/selector-alternatives"
}

Wenn du bestimmte Seitenelemente in deinem Transaktionsskript benennen musst, verwendest du entweder einen XPath- oder CSS-Selektor. Du hast eventuell mehrere Selektoren zur Auswahl, um ein übliches Element anzugeben, aber manche Selektoren können mehr Probleme erzeugen als andere. Um den richtigen zu finden, bedarf es einer klugen Auswahl von XPath- oder CSS-Selektoren.

Sofern du den Transaktions-Recorder verwendet hast, um die Klickpfade zu erfassen, wendet der [Rekorder Algorithmen an]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="de" >}}), um das auszuwählen, was er für die beste Selektoroption erachtet. Da der Transaktions-Recorder aber nur einen einzelnen Snapshot deiner Seitenstruktur erhält, ist der von ihm gewählte Selektor nicht unbedingt die beste Wahl für dich. In diesem Artikel sehen wir uns einige Situationen und Lösungen an, die du zurate ziehen kannst, wenn du nach Selektoralternativen suchst.

## Häufige Ursachen ungeeigneter Selektorenbestimmung

Viele Faktoren spielen eine Rolle und verursachen, dass dein Selektor sich nicht wie erwartet verhält. Beispielsweise ergeben deine Tests Fehler wie etwa „Element nicht gefunden." Da kann eine ungeeignete Selektorwahl die Ursache des Problems sein. Sehen wir uns einige der Gründe für Skriptfehler an:

### Dynamische IDs

Einige Elemente erhalten jedes Mal eine neue ID, wenn der Server eine Seite sendet. Wenn dein Selektor auf die dynamische ID verweist, sorgt der Selektor für einen Fehler, sobald das Skript versucht, das Element zu finden. Es gibt unterschiedliche Möglichkeiten, dieses Problem zu beheben.
  
Bei den folgenden Beispielen nutzen wir im HTML-Snippet ein Eingabe-Element zur Auswahl der Artikelmenge.

    <div class="quantity"> 
      <input type="number" id="quantity_5e5653081acc7" class="input-text qty text"
      step="1" min="1" max="" name="quantity" value="1" title="Qty" size="4" 
      pattern="[0-9]*"inputmode="numeric"
      aria-labelledby="Suraya Bay T-Shirt quantity"> 
    </div>

Die ID für die Eingabe ist zum Teil feststehend und zum Teil generiert, sodass ein Fehler erzeugt wird, wenn die ID, wie sie vom Transaktions-Recorder erfasst wurde, referenziert wird. Der Transaktions-Recorder empfiehlt:
XPath: `//input[@id="quantity_5e5653081acc7"])[1] ` CSS Selektor: `input#quantity_5e5653081acc7`
Beide schlagen fehl, wenn sie in der Transaktion verwendet werden. Dir stehen mehrere Optionen zur Problembehebung zur Verfügung.

-   **Verwende ein Element-Attribut, das sich nicht ändert**. Durch Verweisen auf ein anderes Element-Attribut, zum Beispiel den Elementnamen, kannst du einen dauerhaften Selektor einrichten.
`//input[@name="quantity"]`
-   **Verwende einen relativen Pfad, um im DOM zu navigieren.** Der obige HTML-Knoten ist in einem übergeordneten `<div>`-Knoten eingebettet. Wir können das Eingabeelement im übergeordneten Element anhand von XPath referenzieren. Der folgende Code ortet das übergeordnete Element, gefolgt vom untergeordneten Eingabeelement.
    //div[@class="quantity"]/input
-   **Verwende eine relative XPath-Angabe mit** `contains` oder `starts with`. Wenn die ID zum Teil feststeht und zum Teil dynamisch ist, beispielsweise `id="quantity_5e5653081acc7"`, wobei der Teil "`5e5653081acc7`" sich ändert, aber der Teil "`quantity_`" der ID derselbe bleibt, kannst du auf den Teil verweisen, der sich nicht ändert. Zum Beispiel 
    `//select[starts with (@id, "quantity_")]`
    oder  
    `//select[contains(@id, "quantity")]`
-   **Füge für deine Transaktionstests Elementattribute hinzu**. Lasse deine Entwickler fürs Testen spezielle Elementattribute hinzufügen, die sich nicht ändern. Nehmen wir an, du hast ein Element mit einer dynamischen ID wie  
    `<button id=”i2fe4owf” class=”btn”>`  
    In diesem Fall gibt es nichts Konkretes, anhand dessen du das Element identifizieren könntest, wie etwa ein Namensattribut. Wenn du ein weiteres Attribut wie zum Beispiel “data-test-id” mit einem statischen Wert hinzufügst, kannst du dieses Element immer finden. Ein zusätzliches Attribut kann folgendermaßen aussehen:  
    `<button id=”i2fe4owf” class=”btn” data-test-id =”shoppingcart-test-step2”>`
-   **Identifiziere Elemente mit mehreren Elementattributen**. Wenn dein Skript die Optionen `contains` oder `starts with` enthält, um ein Element zu identifizieren, und es nicht funktioniert, weil die anderen Elemente auf der Seite dasselbe Prefix oder Suffix mit dem dynamischen Teil verwenden, kannst du manchmal mehrere Attribute nutzen, um das Element mit XPath zu identifizieren.
    `//select[starts-with(@id, "quantity_" and contains(@class, "qty text")]```

### Mehrsprachige Websites

Unterhältst du eine Website in mehreren Sprachen, ändert die Seite häufig die Sprache je nach Standort des Nutzers. Wenn sich der von dir gewählte Checkpoint in einer Region befindet, die einen Sprachwechsel auslöst, kann das Transaktionsprüfobjekt einen Fehler melden, je nachdem wie du das Element identifiziert hast. Wenn die Sprache sich auf deinen Inhalt auswirkt, ist es besser, andere Optionen in deinen Selektoren zu verwenden als Label-Werte oder bestimmte Wörter auf der Seite.

### Dynamische Inhalte

Einige Websites verwenden dynamische Inhalte basierend auf saisonale Aktionen, Feiertage, Nutzeranmeldung sowie Cookie- oder Standort-Daten. Die Datenverschiebungen aufgrund von  verschiedenen dynamischen Inhalten können dafür sorgen, dass das Transaktionsprüfobjekt einen Fehler meldet. Dynamische Inhalte verhalten sich sehr ähnlich dynamischen IDs, aber die gesamten Elemente der Seite ändern sich mit jeder Server-Anfrage. Ein Beispiel sind Amazon-Seiten mit ihren sich laufend ändernden Produktempfehlungen. Aber auch, wenn die Einzelheiten sich ändern, ist die Struktur üblicherweise dieselbe. Sich auf Elemente anhand ihrer Position im DOM statt anhand der aktuellen Attribute zu beziehen, wird zu besseren Ergebnissen führen.

Nehmen wir zum Beispiel eine E-Commerce-Website, die Artikel auf der Seite aufgrund der Artikelbeliebtheit anzeigt. Die Artikel wechseln fast jedes Mal, wenn die Seite lädt. Statt einen Selektor zu verwenden, der einen Artikel über seinen Namen oder ein anderes seiner Attribute identifiziert, ist es wahrscheinlich besser, einen Selektor für einen relativen Pfad zu verwenden, der den ersten Artikel einer Liste wählt, egal welcher Artikel angezeigt wird.

### Verborgene Objekte

Fehler aufgrund verborgener Objekte sind nicht unbedingt das Ergebnis eines schlechten Selektors. Der Selektor funktioniert eventuell nicht, weil eine vorangehende Aktion fehlt. Wenn du also Fehlermeldungen erhältst, die angeben, dass das Skript das Objekt gefunden hat, aber das Objekt nicht sichtbar ist, benötigt dein Skript vielleicht eine zusätzliche Aktion, bevor die Interaktion versucht wird.  Bedenke, dass genau wie deine Nutzer auch das Skript nicht mit unsichtbaren Objekten interagieren kann.

**Hover-Aktion fehlt**:

Eine nicht vorhandene Hover-Aktion kann Fehler erzeugen. Ein Menüelement wird eventuell nicht sichtbar, bis der Nutzer den Mauszeiger auf ein Menüelement führt, um ein Einblend-Menü zu erzeugen. Das Hinzufügen eine Hover-Interaktion sorgt dafür, dass das Objekt sichtbar und verfügbar für die Interaktion wird.

**Scroll-Aktion fehlt**:

Häufig werden Objekte auf Seiten nur geladen, wenn sie vom Nutzer benötigt werden, um die Illusion einer besseren Performance zu geben und den Datenverbrauch zu mindern. Während der Nutzer die Seite hinunterscrollt, werden die Inhalte geladen. Ohne eine Scroll-Aktion werden die Objekte nicht dargestellt und verfügbar gemacht, um mit dem Skript zu interagieren. Eine Scroll-Aktion hinzuzufügen, behebt das Problem. Denke daran, dass die Scroll-Aktion nur aktuell sichtbare Objekte sehen kann. Du musst eventuell zwei oder mehr Scroll-Aktionen hinzufügen, bevor das Zielobjekt auf der Seite sichtbar ist.

{{< callout >}}
**Hinweis**: Der Recorder erfasst Scrollen und [Hover-Aktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="de" >}}) nicht, sodass du diese Aktionen manuell zum Skript hinzufügen musst.
{{< /callout >}}

**Im DOM verborgen, aber auf dem Bildschirm sichtbar**:

Du erhältst vielleicht auch Fehlermeldungen aufgrund von Objekten, die du klar auf der Seite sehen kannst, aber das Objekt ist im DOM verborgen. Übliche Beispiele für dieses Problem sind Wahlschalter und Kontrollkästchen, die von Labeln verdeckt sind. Der Recorder erfasst die Klickaktion für den Wahlschalter oder das Kontrollkästchen. Obwohl diese Objekte nicht im DOM sichtbar sind, sind die Label sichtbar. Um das Problem zu beheben, ändere die Klickaktion auf das Label, das das Objekt überdeckt.

## Selektoren ändern

Wenn mit deinen Selektoren Probleme auftreten, kannst du mehrere Schritte unternehmen, um sie zu lösen.

### Die Selektoren-Auswahl nutzen

Bei der Umwandlung deiner Aufzeichnung in ein Skript entscheidet Uptrends mithilfe eines Algorithmus, welcher Selektor genutzt wird. Sollte der Recorder jedoch eine schlechte Wahl getroffen haben, musst du einschreiten. Bei Uptrends ist das ganz leicht, weil es eine Auswahl alternativer Selektoren gibt. Um die alternativen Selektoren aufzurufen

1.  Klicke beim Selektoren-Feld die graue Schaltfläche mit dem Ellipsen-Zeichen, um den Selektoren-Dialog zu öffnen.
![Selector finder button](/img/content/ed5d9588-d944-402f-9899-5ba46a574c2b.png)

2.  Wähle einen anderen Selektor aus der Liste.
![Selector finder dialog](/img/content/c8a2a635-1e85-4c3b-b84b-2b1edbe4dd15.png)

Du kannst jeden beliebigen Selektor aus der Liste wählen und ausprobieren. Wenn keiner von diesen für dich geeignet scheint, und du dich nicht mit dem Programmieren eines eigenen Selektors auskennst, kann unser [Support-Team](/contact) dir helfen, eine Lösung zu finden.

{{< callout >}}
**Hinweis**: Wenn du ein älteres Skript bearbeitest, sind die Selektoren in der Auswahl wahrscheinlich veraltet und du musst den neuen Selektor eventuell selbst programmieren. Wende dich an den [Support](/contact), wenn du Hilfe benötigst.
{{< /callout >}}

### Den Selektor selbst programmieren

Wenn dir die Arbeit mit Selektoren vertraut ist oder dir Entwickler zur Seite stehen, kannst du deine eigenen CSS- oder XPath-Selektoren programmieren. Gleich wer das Skript für deine Selektoren beisteuert, teste es ausgiebig.

Beachte, dass du [automatische Variablen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}}) bei dem Selektor verwenden kannst. Beispielsweise kannst du dem Selektor-Pfad eine zufällige Zahl hinzufügen, indem du die automatische Variable `{{@RandomInt(min,max)}}` nutzt.

### Hilfe vom Support

Self-Service Transactions bedeuten nicht, dass du auf dich allein gestellt bist. Unser Support steht für dich bereit. Unser erfahrenes Team für Transaktionen kennt sich mit allen Situationen aus und ist großartig, wenn es um das Finden alternativer Selektoren geht. Reiche einfach ein [Support-Ticket](/contact) ein und beschreibe die Herausforderung, der du dich gegenübersiehst.
