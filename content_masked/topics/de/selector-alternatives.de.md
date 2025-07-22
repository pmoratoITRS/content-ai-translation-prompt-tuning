{
  "hero": {
    "title": "Selektoralternativen"
  },
  "title": "Selektoralternativen finden",
  "summary": "Manchmal funktionieren Selektoren nicht oder sie funktionieren nur teilweise. In diesem Artikel behandeln wir einige der üblichen Selektorprobleme und schlagen Möglichkeiten zur Behebung vor.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/selektoralternativen",
  "translationKey": "[URL_1]
}

Wenn du bestimmte Seitenelemente in deinem Transaktionsskript benennen musst, verwendest du entweder einen XPath- oder CSS-Selektor. Du hast eventuell mehrere Selektoren zur Auswahl, um ein übliches Element anzugeben, aber manche Selektoren können mehr Probleme erzeugen als andere. Um den richtigen zu finden, bedarf es einer klugen Auswahl von XPath- oder CSS-Selektoren.

Sofern du den Transaktions-Recorder verwendet hast, um die Klickpfade zu erfassen, wendet der [Rekorder Algorithmen an]([LINK_URL_1]), um das auszuwählen, was er für die beste Selektoroption erachtet. Da der Transaktions-Recorder aber nur einen einzelnen Snapshot deiner Seitenstruktur erhält, ist der von ihm gewählte Selektor nicht unbedingt die beste Wahl für dich. In diesem Artikel sehen wir uns einige Situationen und Lösungen an, die du zurate ziehen kannst, wenn du nach Selektoralternativen suchst.

## Häufige Ursachen ungeeigneter Selektorenbestimmung

Viele Faktoren spielen eine Rolle und verursachen, dass dein Selektor sich nicht wie erwartet verhält. Beispielsweise ergeben deine Tests Fehler wie etwa „Element nicht gefunden." Da kann eine ungeeignete Selektorwahl die Ursache des Problems sein. Sehen wir uns einige der Gründe für Skriptfehler an:

### Dynamische IDs

Einige Elemente erhalten jedes Mal eine neue ID, wenn der Server eine Seite sendet. Wenn dein Selektor auf die dynamische ID verweist, sorgt der Selektor für einen Fehler, sobald das Skript versucht, das Element zu finden. Es gibt unterschiedliche Möglichkeiten, dieses Problem zu beheben.
  
Bei den folgenden Beispielen nutzen wir im HTML-Snippet ein Eingabe-Element zur Auswahl der Artikelmenge.

    [HTML_TAG_1] 
      [HTML_TAG_2] 
    [HTML_TAG_3]

Die ID für die Eingabe ist zum Teil feststehend und zum Teil generiert, sodass ein Fehler erzeugt wird, wenn die ID, wie sie vom Transaktions-Recorder erfasst wurde, referenziert wird. Der Transaktions-Recorder empfiehlt:
XPath: [INLINE_CODE_1] CSS Selektor: [INLINE_CODE_2]
Beide schlagen fehl, wenn sie in der Transaktion verwendet werden. Dir stehen mehrere Optionen zur Problembehebung zur Verfügung.

-   **Verwende ein Element-Attribut, das sich nicht ändert**. Durch Verweisen auf ein anderes Element-Attribut, zum Beispiel den Elementnamen, kannst du einen dauerhaften Selektor einrichten.
[INLINE_CODE_3]
-   **Verwende einen relativen Pfad, um im DOM zu navigieren.** Der obige HTML-Knoten ist in einem übergeordneten [INLINE_CODE_4]-Knoten eingebettet. Wir können das Eingabeelement im übergeordneten Element anhand von XPath referenzieren. Der folgende Code ortet das übergeordnete Element, gefolgt vom untergeordneten Eingabeelement.
    //div[@class="quantity"]/input
-   **Verwende eine relative XPath-Angabe mit** [INLINE_CODE_5] oder [INLINE_CODE_6]. Wenn die ID zum Teil feststeht und zum Teil dynamisch ist, beispielsweise [INLINE_CODE_7], wobei der Teil "[INLINE_CODE_8]" sich ändert, aber der Teil "[INLINE_CODE_9]" der ID derselbe bleibt, kannst du auf den Teil verweisen, der sich nicht ändert. Zum Beispiel 
    [INLINE_CODE_10]
    oder  
    [INLINE_CODE_11]
-   **Füge für deine Transaktionstests Elementattribute hinzu**. Lasse deine Entwickler fürs Testen spezielle Elementattribute hinzufügen, die sich nicht ändern. Nehmen wir an, du hast ein Element mit einer dynamischen ID wie  
    [INLINE_CODE_12]  
    In diesem Fall gibt es nichts Konkretes, anhand dessen du das Element identifizieren könntest, wie etwa ein Namensattribut. Wenn du ein weiteres Attribut wie zum Beispiel “data-test-id” mit einem statischen Wert hinzufügst, kannst du dieses Element immer finden. Ein zusätzliches Attribut kann folgendermaßen aussehen:  
    [INLINE_CODE_13]
-   **Identifiziere Elemente mit mehreren Elementattributen**. Wenn dein Skript die Optionen [INLINE_CODE_14] oder [INLINE_CODE_15] enthält, um ein Element zu identifizieren, und es nicht funktioniert, weil die anderen Elemente auf der Seite dasselbe Prefix oder Suffix mit dem dynamischen Teil verwenden, kannst du manchmal mehrere Attribute nutzen, um das Element mit XPath zu identifizieren.
    [INLINE_CODE_16]`[INLINE_CODE_17][SYSTEM_VAR_1]` nutzt.

### Hilfe vom Support

Self-Service Transactions bedeuten nicht, dass du auf dich allein gestellt bist. Unser Support steht für dich bereit. Unser erfahrenes Team für Transaktionen kennt sich mit allen Situationen aus und ist großartig, wenn es um das Finden alternativer Selektoren geht. Reiche einfach ein [Support-Ticket]([LINK_URL_8]) ein und beschreibe die Herausforderung, der du dich gegenübersiehst.
