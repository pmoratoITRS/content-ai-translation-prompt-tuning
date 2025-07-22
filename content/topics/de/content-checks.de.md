{
  "hero": {
    "title": "Inhaltsprüfungen"
  },
  "title": "Inhaltsprüfungen",
  "summary": "Bei der Einrichtung von Transaktionsprüfobjekten solltest du einige Dinge berücksichtigen.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/inhaltspruefung",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/content-checks"
}

Wenn du sicherstellen möchtest, dass deine Transaktionen reibungslos ablaufen, ist die *Prüfung von Übereinstimmungsmustern* das wertvollste Hilfsmittel, das dir zur Verfügung steht. Eine gut eingesetzte Überprüfung von Inhalten kann bei Transaktionen eine große Wirkung haben. Im Allgemeinen dienen Tests mit Übereinstimmungsmustern der Verifizierung, dass die zuvor ausgeführte Aktion (z. B. Klicken auf einen Link, An- oder Abmelden, Navigieren zu einer Seite) erfolgreich abgeschlossen wurde. Da Transaktionsprüfobjekte mithilfe eines Skripts ausgeführt werden, ist das Prüfen mit Übereinstimmungsmustern von unschätzbarem Wert, um sicherzustellen, dass die Transaktion problemlos funktioniert und dir korrekte Informationen zu deiner Website liefert.

**Inhaltsüberprüfungen sind kostenlos und wir empfehlen dir, sie zu nutzen!** Das Prüfen mit Übereinstimmungsmustern macht dein Transaktions-Monitoring nach jeder Aktion, bei der neue Inhalte auf der Seite generiert werden, noch wertvoller.

Da ein Übereinstimmungsmuster in deinem Transaktionsskript darauf wartet, dass der angegebene Inhalt lädt, erhältst du zwei zusätzliche Vorteile.

- Erstens weißt du, dass die Navigation zur richtigen Seite geführt hat, wenn du auf das Vorhandensein von seitenspezifischen Inhalten testest.
- Zweitens weißt du, dass die Seite korrekt und vollständig geladen hat, wenn du auf das vollständige Laden des angegebenen Objekts wartest. Das Verifizieren, dass das Objekt vollständig geladen wurde, verhindert ein übereiltes Fortschreiten der Transaktion zur nächsten Aktion.

## Wann machen Inhaltsüberprüfungen Sinn?

Im Allgemeinen dienen Tests mit Übereinstimmungsmustern der Verifizierung, dass die zuvor ausgeführte Aktion erfolgreich abgeschlossen wurde. Du solltest eine Inhaltsüberprüfung nach jeder Aktion vornehmen, bei der auf irgendeine Weise der Inhalt der Seite geändert wird. Mit der Prüfung von Übereinstimmungsmustern testest du ausdrücklich, ob bestimmte Aktionen des Skripts zum gewünschten Ergebnis im Browser führen. Beispiele für den Einsatz von Inhaltsprüfungen:

- nach Eingabe von Anmeldedaten und Klicken der Schaltfläche zum Anmelden
- nach Klicken eines Produktlinks auf einer E-Commerce-Website
- nach dem Abmelden
- nach dem Navigieren auf eine neue Seite

Du solltest Übereinstimmungsmuster auch prüfen, um zu verifizieren, dass ein automatisch ausgefülltes Textfeld richtig ist, eine Tabelle einwandfrei mit Daten ausgefüllt wurde oder ein Skript korrekt ausgeführt wurde.

## Inhaltsprüfungen hinzufügen

Du kannst Inhaltsprüfungen während des [Aufzeichnungsprozesses]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks#use-content-checks" lang="de" >}}) oder über den Schritte-Editor des Prüfobjekts einfügen.

Füge eine Inhaltsprüfung hinzu:

1. Öffne das Transaktionsprüfobjekt, das du ändern möchtest.
2. Wechsele zur Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}}.
3. Scrolle zu dem Schritt, dem du eine Inhaltsprüfungsaktion hinzufügen möchtest.
4. Klicke auf {{< AppElement type="buttonPrimary" >}} Aktion hinzufügen {{< /AppElement >}}. Du siehst in der Liste, dass der Aktionstyp zur Inhaltsprüfung über eine grüne „Test“-Bezeichnung verfügt.
![Screenshot Inhaltsprüfung bei Transaktion hinzufügen](/img/content/scr_transaction-add-content-check.min.png)
5. Wähle den entsprechenden Aktionstyp aus dem Pop-up-Fenster. Nach deiner Wahl erscheint die neue Aktion im Editor.
   ![Screenshot Inhaltsprüfung in Transaktionsschritt](/img/content/scr_transaction-content-check-element.min.png)
  Dieser Screenshot zeigt dir den Aktionstyp *Prüfe Elementinhalt*.
6. Gib die Einstellungen für deine Inhaltsprüfung ein. Die Einstellungsoption variieren je nach ausgewähltem Aktionstyp. Der Abschnitt [Typen von Inhaltsprüfungen]({{< ref path="#content-check-types" lang="de" >}}) bietet weitere Informationen zu den Optionen eines Typs.
7. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen zu sichern.

Die obigen Anweisungen sind für den visuellen Editor. Du kannst Schritte im [Skripteditor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="de" >}}) hinzufügen und ändern.

## Typen von Inhaltsprüfungen {id="content-check-types"}

Derzeit besteht die Möglichkeit, zwischen unterschiedlichen Inhaltsprüfungen auszuwählen.

### Prüfe Elementinhalt {id="test-element-content"}

Beim Aktionstyp *Prüfe Elementinhalt* testet Uptrends ein bestimmtes Element auf der Seite auf Inhalt, den du angibst. Die Aktion *Prüfe Elementinhalt* ermöglicht spezifischere und robustere Tests als der Aktionstyp *Prüfe Dokumentinhalt*. Wir empfehlen für die meisten Szenarien den Typ *Prüfe Elementinhalt*. Die Aktion *Prüfe Elementinhalt* erfordert, auf ein bestimmtes Objekt auf der Seite zu verweisen. Dies geschieht mit CSS- oder XPath-Selektoren und dem Definieren eines Inhalt-Strings, den das Objekt enthalten sollte. Damit wird ein sehr verlässlicher Test ausgeführt und verifiziert, dass die zuvor anhand des Skripts erfolgten Aktionen erfolgreich abgeschlossen wurden.

Die Aktion *Prüfe Elementinhalt* erfordert CSS- oder XPath-Selektoren, um auf ein bestimmtes Objekt zu verweisen, bei dem du den Inhalt prüfen möchtest.

![Screenshot Testaktion Prüfe Elementinhalt oben](/img/content/scr_transaction-action-content-check-main.min.png)

Du siehst ein Drop-down-Menü, um zwischen den beiden Selektorentypen zu wechseln. Weitere Infos zu Selektoren findest du in den Knowledge-Base-Artikeln [Selektoren nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="de" >}}) und [Selektoralternativen]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="de" >}}).

Nachdem du einen Selektorentyp (CSS/XPath) ausgewählt und den Selektor eingegeben hast, wählst du eine Übereinstimmungsbedingung unter den folgenden Optionen:

- beinhaltet
- enthält nicht (siehe auch [Negative Inhaltsprüfungen]({{< ref path="#negation-content-checks" lang="de" >}}))
- stimmt mit Regular Expression überein
- stimmt nicht mit Regular Expression überein (siehe auch [Negative Inhaltsprüfungen]({{< ref path="#negation-content-checks" lang="de" >}}))

Zum Abschluss der Einrichtung gibst du den Text, auf den du beim angegebenen Element prüfen möchtest, im Feld **Beispieltext** ein.

Die anderen Aktionseinstellungen sind optional.

**Beschreibung** – füge eine Beschreibung für deine Inhaltsprüfung hinzu, z. B. „Test, ob Anmeldung erfolgreich war.“

**Fehlermeldung** – was wird angezeigt, wenn die Inhaltsprüfung einen Fehler generiert, z. B. „Anmeldung war nicht erfolgreich.“

**Warte bis** – gib eine Wartebedingung für diesen Test des Prüfobjekts ein. Erfahre mehr im Artikel [Warte auf Element]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="de" >}}). Hinweis: Das Feld „Warte bis“ ist nicht für den Aktionstyp *Prüfe Dokumentinhalt* verfügbar.

**Warte-Timeout** – der Wert in Millisekunden, der angibt, wie lange Uptrends warten soll, bis der Inhalt erscheint. Der Standard ist 30 Sekunden. Wir empfehlen für die meisten Fälle, die Standardeinstellung zu nutzen. In bestimmten Fällen kann es jedoch nützlich sein, den Timeout-Wert zu erhöhen. Der Höchstwert für das Warte-Timeout beträgt 60 Sekunden. Achte darauf, den Timeout-Wert nicht zu stark zu erhöhen, da es eine absolute Obergrenze gibt, innerhalb der eine komplette Transaktion abgeschlossen sein sollte. Wichtig: Das Erhöhen oder Verringern des Warte-Timeouts wirkt sich nicht auf die Zeitmessungen für die Transaktion aus.

**Variable zuweisen** – gib einen Variablennamen im Format `{{name}}` ein. Lies unseren Artikel zur [Nutzung von Transaktionsvariablen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="de" >}}), um weitere Infos zu erhalten.

**Shadow DOM Host** – gib einen [Shadow DOM]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="de" >}}) Host und sogar eingebettete Shadow DOMs an.

Wenn du direkt mit dem JSON-Transaktionsskript im [Skripteditor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="de" >}}) arbeitest, muss der Prüfungstyp *Prüfe Elementinhalt* folgendes Format einhalten:

```json
{
  "testElementContent": {
    "value": "Example text",
    "testType": "Contains",
    "element": {
      "xpath": "[@id='exampleId']",
      "alternatives": [],
      "shadowRoots": []
    },
    "timeoutMs": 3000,
    "description": "Description of this action"
  }
}
```

Wenn Parameter wie `timeoutMs`, `description` und `failureMessage` optional sind, kannst du sie auslassen. Die verfügbaren `testType`-Parameterwerte sind `Contains`, `DoesNotContain`, `MatchesRegex` und `DoesNotMatchRegex`. Dieses Beispiel verifiziert, dass das (Beispiel-)Element mit dem XPath-Selektor `//*[@id=’exampleId’]` den String „Example text“ beinhaltet. Natürlich kannst du auch den CSS-Selektor nutzen: Nutze den Wert `“css”:”#exampleId”`, statt `"xpath": "[@id='exampleId']"`.

### Prüfe Dokumentinhalt

Der Aktionstyp *Prüfe Dokumentinhalt* ist der einfachste verfügbare Test. Der Typ *Prüfe Dokumentinhalt* sucht eine komplette Seite auf einen bestimmten Inhalt ab, ganz gleich, ob der Inhalt sichtbar ist (oder nicht). Nicht jeder Text, der im Seitendokument oder DOM vorhanden ist, erscheint auf der Seite. Da der Testtyp *Prüfe Dokumentinhalt* das HTML-Dokument prüft, und nicht die im Browser angezeigten Inhalte, kannst du nach „unsichtbarem“ Text suchen lassen. Da der Typ *Prüfe Dokumentinhalt* nicht die geladenen Inhalte prüft, kannst du nicht die CSS- oder XPath-Selektoren nutzen, um auf bestimmte Objekte zu verweisen. Er unterstützt jedoch reguläre Ausdrücke, um auf bestimmte Muster im DOM-Inhalt zu prüfen.

Entscheidest du dich, direkt mit dem JSON-Transaktionsskript statt des visuellen Editors zu arbeiten, muss der Aktionstyp *Prüfe Dokumentinhalt* folgendes Format haben:
```json
    { 
    "testDocumentContent": { 
      "value": "Example content in the DOM", 
      "testType": "Contains",
      "timeoutMs": 30000, 
      "description": "This check will test the page DOM for the specified content.", 
      "failureMessage": "Example failure message" 
      } 
    }
```
Beachte, dass die Parameter `timeoutMs`, `description` und `failureMessage` optional sind, sodass du sie auslassen kannst.

### Warte auf Element

Der Aktionstyp *Warte auf Element* ist fast identisch mit dem Typ *Prüfe Elementinhalt*, abgesehen davon, dass in diesem Fall das Element keinen Textinhalt erfordert. Du kannst den Typ *Warte auf Element* nutzen, um leere Objekte zu testen, zum Beispiel &lt;div&gt;-Objekte ohne Text, Bilder und Schaltflächen.

Arbeitest du direkt mit dem JSON-Transaktionsskript, muss der Aktionstyp *Warte auf Element* folgendes Format haben:
```json
    {
      "waitForElement": {
        "element": {
          "xpath": "//*[@id='exampleId']" 
        },
        "timeoutMs": 30000,
        "description": "Verify that the element with the indicated XPath selector exists on the page.",
        "failureMessage": "Example failure message"
      }
    }
```
Beachte, dass die Parameter `timeoutMs`, `description` und `failureMessage` optional sind, sodass du sie auslassen kannst.

## Negative Inhaltsprüfungen {id="negative-content-checks"}

Statt zu bestätigen, dass bestimmte Inhalte im DOM oder auf der Seite **erscheinen**, musst du vielleicht verifizieren, dass bestimmte Inhalte auf der Seite **NICHT existieren**. Beispielsweise kannst du eine Warnmeldung erhalten, wenn eine bestimmte Fehlermeldung auf deiner Seite angezeigt wird. Um festzustellen, dass bestimmte nicht auf der Seite angezeigt werden, nutzt du eine *negative Inhaltsprüfung*. Wenn der angegebene Inhalt auf der Seite erscheint, meldet das Prüfobjekt einen Fehler.

Nutze für eine negative Inhaltsprüfung sowohl den Typ *Prüfe Dokumentinhalt* wie auch den Typ *Prüfe Elementinhalt*. Setze dann die Bedingung von der Standardauswahl **beinhaltet** auf entweder **enthält nicht** oder **stimmt nicht mit Regular Expression überein**.

Trifft die Transaktion bei einer negativen Inhaltsprüfung auf das angegebene Element oder den Inhalt, wird die Transaktion gestoppt und ein Fehler gemeldet. Erscheint das Element oder der Inhalt nicht, wird die Transaktion normal fortgesetzt.

## Qualität der Inhaltsprüfungen

Um mit deinen Inhaltsprüfungen die besten Ergebnisse zu erzielen, wähle ein einzigartiges Element auf der Seite, das einzigartigen Text resultierend aus einer vorherigen Aktion enthält. Eine nutzbringende Inhaltsprüfung ist ein definitiver und exklusiver Test einer Aktion. Bei den meisten Tests des Typs *Prüfe Elementinhalt* wird auf eine Kombination aus verlässlichem und einzigartigem **Selektor** und **Textwert** geprüft.

### Textwert

Die Auswahl eines einzigartigen Textwerts, auf den getestet wird, ist sowohl beim Typ *Prüfe Elementinhalt* wie auch beim Typ *Prüfe Dokumentinhalt* von entscheidender Bedeutung. Die Auswahl eines einzigartigen Textwerts trifft nicht auf den Aktionstyp *Warte auf Element* zu, da hier nicht auf Textwerte getestet wird.

Achte bei der Auswahl eines Textwerts darauf, dass dieser eine direkte Folge der vorangegangenen Aktion ist. Zum Beispiel:

-   Nach dem Klicken einer Anmeldeschaltfläche oder eines Abmeldelinks könntest du die folgende Seite auf das Vorhandensein eines Benutzernamens oder des zugehörigen Ab- bzw. Anmeldelinks prüfen.
-   Nach Klicken eines Links für eine Produktseite kannst du auf Produktinformationen oder das Vorhandensein einer Bestellschaltfläche prüfen.
-   Suche nach einem Link auf der nächsten Seite, den du für den nächsten Schritt benötigst.

**Wähle nicht Text, der auf jeder Seite angezeigt wird.** Setze beispielsweise keinen Fußzeilentext ein. Ein Fußzeilentext sagt nichts über den Fortgang der Transaktion aus.

Verwende einen [regulären Ausdruck](https://www.w3schools.com/jsref/jsref_obj_regexp.asp), wo dies sinnvoll ist. Wenn deine Seite zum Beispiel nach einer Suche „15 Ergebnis(se) gefunden“ anzeigt, richte eine Inhaltsprüfung für `.* result(s), found` ein und setze die Bedingung auf **stimmt mit Regular Expression überein**.

Wenn du den Text für deinen Test ausgewählt hast, wähle einen einzigartigen und verlässlichen (unberührt von Änderungen auf der Seite) CSS- oder XPath-Selektor aus.

### Selektoren

Die Auswahl eines verlässlichen und robusten Selektors ist wichtig für die beiden Testtypen *Prüfe Elementinhalt* und *Warte auf Element*. Da bei dem Testtyp *Prüfe Dokumentinhalt* nicht auf ein bestimmtes Objekt verwiesen wird, findet dieser Abschnitt dabei keine Anwendung.

Ein guter Selektor ist auf der Seite einzigartig. Das Einsetzen eines einzigartigen Werts sorgt dafür, dass Uptrends nach dem richtigen Element sucht. Wenn möglich, nutze das ID-Attribut des Elements, da dies sich im Allgemeinen einzig auf das gewählte Element bezieht. Zum Beispiel `//*[@id=’testId’]` oder `#testId`.

Mehr zu Selektoren findest du in den Knowledge-Base-Artikeln [Selektoren nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="de" >}}) und [Selektoralternativen]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="de" >}}).

## Vorbehalte, Fallstricke und Tipps

**Achte auf Groß- und Kleinschreibung**. Beim Einsatz von CSS erscheint Text häufig in Großbuchstaben auf der Seite, während im DOM die übliche Groß- und Kleinschreibung verwendet wird. Das heißt, der Selektor könnte `//span[text()='Hello']` lauten, aber der Text auf der Seite könnte als „HELLO“ erscheinen. Der Selektor sollte die Information des DOM wiedergeben und der von dir eingegebene String sollte widerspiegeln, was tatsächlich auf der Seite steht.

**Bei einigen Seiten werden dynamische IDs für die Elemente genutzt**. Wir könnten zum Beispiel einen Klick auf einen Span erfassen, der im DOM als
`<span id="example-12345">` erscheint.
Nach einem Neuladen der Seite wird dasselbe Element jedoch mit 
`<span id="example-12789">` angezeigt.
Verwende XPath, um dynamische IDs zu berücksichtigen, zum Beispiel
`//span[contains(@id,'example-')]`.