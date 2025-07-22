{
  "hero": {
    "title": "Shadow DOM"
  },
  "title": "Arbeiten mit einem Shadow DOM",
  "summary": "Erfahre, wie du Interaktionen in einem Shadow DOM für deine Transaktionsprüfobjekte einrichtest.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/shadow-dom",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/shadow-dom"
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

```html
<html>
    <head>...</head>
    <body>
        ...
        <example-root-element id="exampleId" class="class example">
            #shadow-root (open)
                <a class="linkClass" href="https://www.exampledomain.com">Example link</a>
                <div>Some example text</div>
                <input type="text" id="exampleTextfield">
        </example-root-element>
        ...
    </body>
</html>
```

Dieser Abschnitt eines DOM enthält ein Shadow DOM, angezeigt durch den Knoten **#shadow-root (open)**. Das Shadow DOM enthält drei Elemente: einen Link (mit der Klasse 'linkClass'), eine Textzeichenfolge (das `<div>` mit „Some example text“) und ein Textfeld-Element `<input>` (mit ID „exampleTextfield“).

Das Shadow DOM ist an ein Element des Haupt-DOM des Dokuments geknüpft, so wie es immer bei einem Shadow DOM der Fall ist. In diesem Fall ist das Element (**Shadow Host** genannt) `<example-root-element>`, was über eine eigene ID und Klasse verfügt.

Wenn die Transaktion einen Schritt benötigt, bei dem ein Wert in das Textfeld eingegeben wird, müssen wir die Transaktion ausdrücklich anweisen, dass sie mit dem Shadow DOM agieren soll. Das geschieht folgendermaßen:

1. Füge [eine Aktion]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="de" >}}) des richtigen Typs hinzu. In diesem Beispiel geben wir Text ein, also verwenden wir die Aktion **Übernehmen**. Die gleichen Schritte gelten für die anderen Interaktionstypen.
2. Klicke in den Einstellungen der Aktion auf {{< AppElement type="button" >}} Spezifiziere einen Shadow DOM Host {{< /AppElement >}}.
3. Gib den Bezeichner für das Shadow Host Element ein. In diesem Fall können wir uns auf das Shadow Root-Element mit seiner ID *exampleId* beziehen. Bei der Angabe eines Shadow Hosts kannst du entweder einen CSS (`#exampleId`) oder XPath (`//example-root-element[@id='exampleId']`) Selektor nutzen.
4. Da wir nun die Transaktion angewiesen haben, mit diesem bestimmten Shadow DOM zu interagieren, können wir wie üblich fortfahren. Gib die Elemente an, für die die Übernehmenaktion ausgeführt werden soll. In diesem Fall nutzen wir die ID des Textfelds *exampleTextfield*. Bei der Angabe der Elemente in einem Shadow DOM **kannst du nur CSS-Selektoren nutzen**.
5. Gib schließlich den Text für das Textfeld ein und konfiguriere alle weiteren Optionen nach Bedarf.

![Shadow DOM Beispiel](/img/content/scr-transactions-shadow-dom-example.min.png)

Wenn du den [Transaktionsskript-Editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="en" >}}) (durch Klicken auf *Wechsle zum Skript* oben rechts im Schritte-Editor) nutzt, sieht die gleiche Aktion wie folgt aus:

```json
{
"set": {
    "value": "Fill out some text",
        "element": {
            "css": "#exampleTextfield",
            "alternatives": [],
            "shadowRoots": [
                {
                "css": "#exampleId"
                }
              ]
            },
    "description": "Shadow DOM example"
    }
}
```

### Geschachtelte Shadow DOMs

In manchen Fällen kann ein Shadow DOM in einem anderen Shadow DOM eingebettet sein. Deine Transaktion kann dies handhaben, indem du einfach einen weiteren eingebetteten Shadow DOM Host hinzufügst und die Shadow DOM-Selektoren in der Reihenfolge eingibst, in der sie auftreten.

![Geschachteltes Shadow DOM](/img/content/scr-transactions-shadow-dom-nesting.min.png)

Füge im Transaktionsskript-Editor einfach zusätzliche Werte zum Array shadowRoots hinzu:

```json
 "shadowRoots": [
    {
        "css": "#firstShadowDom"
    },
    {
        "css": "#secondShadowDom"
    }
]
```
