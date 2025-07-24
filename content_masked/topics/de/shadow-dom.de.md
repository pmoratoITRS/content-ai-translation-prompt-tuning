{
  "hero": {
    "title": "Shadow DOM"
  },
  "title": "Arbeiten mit einem Shadow DOM",
  "summary": "Erfahre, wie du Interaktionen in einem Shadow DOM für deine Transaktionsprüfobjekte einrichtest.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/shadow-dom",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In diesem Artikel sehen wir uns die Schritte zur Handhabung von Shadow DOMs auf deiner Seite bei der Konfiguration von Transaktionsprüfobjekten an.

## Das Document Object Model (DOM)

Ein **DOM (Document Object Model)** ist eine Repräsentation jedes Elements in einem Markup-Dokument (zum Beispiel ein HTML-Dokument für Webseiten). Wenn du eine Webseite lädst, erstellt dein Browser ein DOM auf Basis des HTML-Dokuments, wobei jedes einzelne Objekt in einer Baum-Struktur angeordnet wird. Du kannst das DOM für jede beliebige Seite anzeigen, indem du die *Entwicklertools* des Browsers (in der Regel über die Taste F12) und die Registerkarte „Elemente“ öffnest.

Das DOM wird als Live-Repräsentation des Dokuments gesehen (Änderungen am DOM ist gleich Änderungen auf der Webseite, wie sie im Browser angezeigt wird), sodass vorübergehende Änderungen an der Seite vorgenommen werden können, während sie im Browserfenster dargestellt wird, zum Beispiel der Einsatz von JavaScript.

## Shadow DOM

Dinge wie JavaScript und CSS gelten global für jeden Knoten innerhalb des DOM. In manchen Fällen kann dies jedoch zu Problemen führen. Wenn deine Seite beispielsweise über Webkomponenten (wiederverwendbare Elemente wie Tabellen oder Zahlungsmodule, die auf mehreren Seiten angezeigt werden können) verfügt, kann es zu Konflikten bei Markup oder Styles mit dem übrigen Teil der Seite kommen. Um dies zu vermeiden, ist es empfehlenswert, diese Webkomponenten einzukapseln: Stelle sicher, dass sie separat vom Hauptdokument bestehen können, um Konflikte zu vermeiden und den Code zu vereinfachen.

Eine Möglichkeit, dies zu erreichen, sind **Shadow DOMs**. Ein Shadow DOM ermöglicht einen separaten, verborgenen DOM-Strukturbaum an bestimmte Elemente im regulären DOM-Baum anzuheften. Ein Shadow DOM ist genauso strukturiert wie ein reguläres DOM, aber mit einem **Shadow Host** verbunden: einem Knoten im regulären DOM. Da ein Shadow DOM ein separater „Baum im Baum“ ist, kann der in ihm enthaltene Code sich nicht auf die Knoten im regulären DOM auswirken, und umgekehrt.

## Shadow DOMs für Transaktionen

Die Interaktionen eines Transaktionsskripts wirken auf die Knoten des Seiten-DOM. Da ein Shadow DOM von diesem getrennt ist, muss eine Transaktion so konfiguriert sein, dass sie mit dem Shadow DOM agiert, statt mit dem Haupt-DOM des Dokuments. Sehen wir uns ein Beispiel an und nehmen wir an, dass das DOM deiner Webseite Folgendes enthält:

[CODE_BLOCK_1]

Dieser Abschnitt eines DOM enthält ein Shadow DOM, angezeigt durch den Knoten **#shadow-root (open)**. Das Shadow DOM enthält drei Elemente: einen Link (mit der Klasse 'linkClass'), eine Textzeichenfolge (das [INLINE_CODE_1] mit „Some example text“) und ein Textfeld-Element [INLINE_CODE_2] (mit ID „exampleTextfield“).

Das Shadow DOM ist an ein Element des Haupt-DOM des Dokuments geknüpft, so wie es immer bei einem Shadow DOM der Fall ist. In diesem Fall ist das Element (**Shadow Host** genannt) [INLINE_CODE_3], was über eine eigene ID und Klasse verfügt.

Wenn die Transaktion einen Schritt benötigt, bei dem ein Wert in das Textfeld eingegeben wird, müssen wir die Transaktion ausdrücklich anweisen, dass sie mit dem Shadow DOM agieren soll. Das geschieht folgendermaßen:

1. Füge [eine Aktion]([LINK_URL_1]) des richtigen Typs hinzu. In diesem Beispiel geben wir Text ein, also verwenden wir die Aktion **Übernehmen**. Die gleichen Schritte gelten für die anderen Interaktionstypen.
2. Klicke in den Einstellungen der Aktion auf [SHORTCODE_1] Spezifiziere einen Shadow DOM Host [SHORTCODE_2].
3. Gib den Bezeichner für das Shadow Host Element ein. In diesem Fall können wir uns auf das Shadow Root-Element mit seiner ID *exampleId* beziehen. Bei der Angabe eines Shadow Hosts kannst du entweder einen CSS ([INLINE_CODE_4]) oder XPath ([INLINE_CODE_5]) Selektor nutzen.
4. Da wir nun die Transaktion angewiesen haben, mit diesem bestimmten Shadow DOM zu interagieren, können wir wie üblich fortfahren. Gib die Elemente an, für die die Übernehmenaktion ausgeführt werden soll. In diesem Fall nutzen wir die ID des Textfelds *exampleTextfield*. Bei der Angabe der Elemente in einem Shadow DOM **kannst du nur CSS-Selektoren nutzen**.
5. Gib schließlich den Text für das Textfeld ein und konfiguriere alle weiteren Optionen nach Bedarf.

![Shadow DOM Beispiel]([LINK_URL_2])

Wenn du den [Transaktionsskript-Editor]([LINK_URL_3]) (durch Klicken auf *Wechsle zum Skript* oben rechts im Schritte-Editor) nutzt, sieht die gleiche Aktion wie folgt aus:

[CODE_BLOCK_2]

### Geschachtelte Shadow DOMs

In manchen Fällen kann ein Shadow DOM in einem anderen Shadow DOM eingebettet sein. Deine Transaktion kann dies handhaben, indem du einfach einen weiteren eingebetteten Shadow DOM Host hinzufügst und die Shadow DOM-Selektoren in der Reihenfolge eingibst, in der sie auftreten.

![Geschachteltes Shadow DOM]([LINK_URL_4])

Füge im Transaktionsskript-Editor einfach zusätzliche Werte zum Array shadowRoots hinzu:

[CODE_BLOCK_3]
