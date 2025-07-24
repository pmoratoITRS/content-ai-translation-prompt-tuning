{
  "hero": {
    "title": "Seiteninteraktionen"
  },
  "title": "Seiteninteraktionen",
  "summary": "Beim Transaktionsprüfobjekt hast du die Möglichkeit, vier unterschiedliche Interaktions- oder Aktionstypen hinzuzufügen. In diesem Artikel sehen wir uns diese vier Typen genauer an. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/seiteninteraktionen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Einer der wichtigsten Aspekte, die das Transaktions-Monitoring von unseren anderen Monitorings unterscheidet, ist die Fähigkeit, mit Seiten zu interagieren. Anhand des Web Application Monitorings führt Uptrends eine Reihe von Aufgaben wie Klicken auf Seitenelementen, Ausfüllen von Formularen, Eingabe von Anmeldedaten, Upload von Dateien und andere Arten von Nutzeraktionen aus, um den Nutzerweg zu testen.

Mit Self-Service Transactions kannst du ein Skript erstellen, das mit deiner Seite mithilfe der vier verfügbaren Aktionstypen bzw. Interaktionen kommuniziert. Die vier Hauptseiteninteraktionen, die wir in diesem Artikel besprechen, sind *[Navigieren]([LINK_URL_1])*, *[Klicken]([LINK_URL_2])*, *[Hover]([LINK_URL_3])* (Mausbewegung über ein Element) und *[Übernehmen]([LINK_URL_4])*. Die **Übernehmen**-Interaktion ermöglicht auch den *[Datei-Upload]([LINK_URL_5])*. Es gibt auch [andere Aktionen]([LINK_URL_6]), darunter Inhaltsprüfung, Bildschirmaufnahme (Screenshot) und Erstellen eines Wasserfallberichts.

## Navigieren [ANCHOR_1]

Navigation ist die erste Aktion, die aufgezeichnet bzw. zu einem Transaktionsskript hinzugefügt wird. Jede Transaktion beginnt mit dem Navigieren zu einer URL, bevor die Funktionstüchtigkeit der Website getestet wird. Die Navigationsaktion weist den Browser an, eine URL aufzurufen. Das Prüfobjekt wartet dann (einen angemessenen Zeitraum), bis die Seite vollständig geladen ist.

In den meisten Fällen enthält eine Transaktion zu Beginn diese eine Navigationsaktion. Manchmal ist jedoch eine zweite Navigation innerhalb der Transaktion erforderlich. Werden zusätzliche Navigationsschritte benötigt, empfehlen wir, diese Navigationsaktionen in eigenen entsprechenden Schritten zu handhaben. Wenn du Navigationsaktionen in ihren eigenen Schritten einfügst, kannst du einen besseren Überblick darüber behalten, was an welcher Stelle der Transaktion passiert. Du kannst die Zeitmessungen von Uptrends schneller pro Schritt analysieren.

Es sollte erwähnt werden, dass eine Navigationsaktion einen [Transaktionscredit]([LINK_URL_7]) erfordert.

### Navigationsoptionen

Dies sind die verfügbaren Optionen für die Navigationsaktionen (siehe Abbildung unten):

-   **URL**: die für die Navigation benötigte URL (erforderlich).
-   **Beschreibung**: eine Beschreibung der Aktion für Berichtszwecke.
-   **Fehlermeldungen**: Die Meldung, die im Falle eines Fehlers in den Fehlerberichten aufgenommen wird.
-   **Ergebnis**: Kontrollkästchen, das Uptrends anweist, den **zurückgegebenen HTTP-Statuscode zu ignorieren**.
-   **Warte-Timeout**: ein Wert, mit dem du angibst, wie lang Uptrends warten soll, bis die Seite vollständig geladen ist. Der Standard (und Höchstwert) ist 60 Sekunden.

Die Einstellung **Ergebnis** unterscheidet sich von allen anderen Aktionstypen. Standardmäßig gewährleistet die Navigationsaktion, dass die Seite korrekt geladen wurde und dass das Prüfobjekt einen fehlerfreien HTTP-Statuscode (jeder Statuscode unter 400) erhalten hat. Jeder Statuscode ab 400 erzeugt für die Navigationsaktion einen Fehler und bewirkt, dass die Transaktion nicht weiter ausgeführt wird. Möchtest du, dass die Transaktion fortgesetzt wird, obwohl ein Fehler-Statuscode zurückgegeben wurde, aktiviere die Option **Ignoriere den zurückgegebenen HTTP-Statuscode**, die Uptrends anweist, die Transaktion ungeachtet des Statuscodes auszuführen.

![]([LINK_URL_8])

### Auf Navigationsaktionen mit Inhaltsprüfungen folgen

Um sicherzustellen, dass die Transaktion nach der Navigationsaktion auf der richtigen Seite erfolgt, füge einen Inhaltstest als nächste Aktion hinzu. Mit einer Inhaltsprüfung erhältst du Gewissheit, dass deine Transaktion auf der gewünschten Seite getestet wird, dass diese Seite vollständig geladen ist und dass die Seite die Elemente anzeigt, die dem Prüfobjekt ermöglichen, weiter mit der Seite zu kommunizieren, bevor die nächste Aktion ausgeführt wird.

### Wasserfallberichte mit Navigationsaktionen nutzen

Da eine Navigationsaktion eine komplett neue Seite lädt, kann es sinnvoll sein, bestimmte Werte zu den Seitenladezeiten zu erhalten. Aktiviere dafür die Option Wasserfallbericht in dem Schritt, der die Navigationsaktion enthält. Jeder Wasserfallbericht, den du zu einer Transaktion hinzufügst, benötigt ein [Credit für Transaktionen]([LINK_URL_9]).

## Klicken [ANCHOR_2]

Die **Klickaktion** weist den Browser an, auf ein bestimmtes Seitenelement anhand eines CSS- oder XPath-Selektors zu klicken. Es gibt verschiedene mögliche Einsatzbereiche für eine Klickaktion:

-   Optionen auswählen
-   Untermenüs öffnen
-  Kontrollkästchen aktivieren 
-   Links klicken, über die die Transaktion auf die nächste Seite geleitet wird.

Daher ist die Klickaktion ein fester Bestandteil jeder Transaktion.

Im großen Ganzen fällt eine Klickaktion in eine von zwei Kategorien:

-   Entweder führen Klickaktionen auf eine neue Seite (Links oder Schaltflächen) oder
-   Klickaktionen führen eine Aktion auf der vorliegenden Seite aus.

Ein Klick kann gegebenenfalls ebenfalls ein [Transaktionscredit]([LINK_URL_10]) erfordern.

### Optionen für Klickaktionen

Die verfügbaren Einstellungen für die Klickaktionen sind unter anderem (siehe Abbildung unten):

-  **Beschreibung**: eine Beschreibung der Aktion für Berichtszwecke.
-  **Fehlermeldungen**: Die Meldung, die im Falle eines Fehlers in den Fehlerberichten aufgenommen wird.
-   **Fehlerbehandlung**: Die Auswahl des Kontrollkästchens **Ignoriere Fehler, die in dieser Aktion auftreten** weist das Prüfobjekt an, alle möglicherweise bei dieser Aktion vorkommenden Fehler, wie beispielsweise ein nicht gefundenes klickbares Element, zu ignorieren.
-   **Warte bis**: Bevor eine Klickaktion ausgeführt werden kann, muss das vom Prüfobjekt zu klickende Element auf der Seite geladen und sichtbar sein (in CSS-Begriffen ausgedrückt, muss das Element angezeigt (display) werden und sichtbar (visibility) sein). Für diese *Wartebedingungen* gibt es einen [speziellen Artikel in der Knowledge Base]([LINK_URL_11]), der dir Informationen zu den unterschiedlichen Optionen bietet.
-   **Warte-Timeout**: Du kannst angeben, wie lange das Prüfobjekt warten soll, damit die **Warte bis**-Anforderung erfüllt ist. Die Standard-Wartezeit beträgt 30 Sekunden. Du kannst diesen Standard mit einer maximalen Wartezeit von 60 Sekunden überschreiben.
- **Shadow DOM Host**: Wenn das Objekt, mit dem eine Interaktion erfolgen muss, sich in einem Shadow DOM befindet, muss eine Transaktion so konfiguriert sein, dass sie das Objekt in diesem Shadow DOM sucht. Weitere Informationen findest du im Knowledge-Base-Artikel zum [Arbeiten mit einem Shadow DOM bei Transaktionen]([LINK_URL_12]).

![Seiteninteraktionen – Klicken]([LINK_URL_13])


[SHORTCODE_1]
**Hinweis**: Wenn du die \[Eingabetaste\] statt eines Mausklicks für das Betätigen der Sende-Schaltfläche verwendest, kann der Transaktionsrekorder die Interaktion nicht erfassen. Als Abhilfe kannst du die Aktion [*Tastenereignis*]([LINK_URL_14]) nutzen. Zeichne zunächst die Transaktion auf und füge dann das *Tastenereignis* manuell im Schritte-Editor hinzu. 
[SHORTCODE_2]


## Übernehmen [ANCHOR_3]

Die **Übernehmenaktion** sagt dem Prüfobjekt, für bestimmte Elemente Werte einzugeben. Für die Übernehmenaktion gibt es mehrere Einsatzbereiche:

- **Ausfüllen von Textfeldern und von Optionsfeldern**: Anmeldedaten und andere Zeichenfolgen, die häufig in Eingabefeldern benötigt werden.
   Wenn die Übernehmenaktion eine Funktion für automatisches Ausfüllen auslöst, beispielsweise wenn du eine Postleitzahl oder einen Suchbegriff eingibst, schlägt die Seite eventuell eine vollständige Adresse oder häufig gesuchte Begriffe vor. In Fällen einer automatischen Vervollständigung solltest du eventuell eine Inhaltsprüfung hinzufügen, um sicherzustellen, dass die Vervollständigungsfunktion korrekt funktioniert hat. Füge zudem eine Klickaktion hinzu, um die gewünschte Option auszuwählen.
- **Optionen aus einem Drop-down-Menü wählen**: Üblicherweise verfügen *Auswahl*elemente mehrere vordefinierte *[HTML_TAG_1]*-Elemente mit jeweils eigenen Werten. Weise das Skript mittels eines CSS- oder XPath-Selektors auf das Auswahlelement hin. Du kannst entweder das *ID*-Attribut, *Wert*-Attribut oder den Textinhalt eines Optionselements eingeben.
- **Hochladen von Dateien aus der Vault**: In bestimmten Fällen kann ein Datei-Upload erforderlich sein, um den Transaktionsablauf richtig zu prüfen. Ein Beispiel wäre das Ausfüllen eines Beschwerdeformulars, das einen Screenshot erfordert, oder das Testen der Upload-Fähigkeiten eines Online-Repositorys. Deine Transaktion kann eine Datei aus der [Account Vault]([LINK_URL_15]) hochladen. Hinweise, wie du Datei-Uploads einrichtest, findest du [weiter unten auf dieser Seite]([LINK_URL_16]).

Wenn du eine [*Übernehmen*aktion]([LINK_URL_17]) zu einem Schritt hinzufügst, sieht dies so aus:

![Seiteninteraktionen – Übernehmen]([LINK_URL_18])

Die *Einstellungen* werden unter [Optionen für Übernehmenaktionen]([LINK_URL_19]) erläutert.

Zunächst musst du definieren, welches Element übernommen werden soll und mit welchem Wert. Gib einen [CSS-Selektor oder XPath Query]([LINK_URL_20]) für das Element ein, für das du einen Wert eingeben (oder eine Datei hochladen) möchtest.

Klicke auf das Auslassungszeichen, um das Dialogfenster **Wähle einen Wert** zu öffnen.

![Screenshot des Auswahlmenüs zur Übernehmenaktion]([LINK_URL_21])

Die Optionen sind [Klartext oder Variablen]([LINK_URL_22]), [Vault Anmeldedaten]([LINK_URL_23]), [One-Time Passwort]([LINK_URL_24]) und [Vault Datei Upload]([LINK_URL_25]).

### Klartext oder Variablen [ANCHOR_4]

Du kannst einfachen Text oder Variablen oder eine Kombination beider verwenden, um den Wert eines Elements anzugeben. Es gibt zwei Arten von Variablen: automatische Variablen und benutzerdefinierte Variablen.
#### Automatische Variablen

Du kannst die Übernehmenaktion verwenden, um dynamisch generierte Daten wie Zeitstempel und zufällige Zeichenfolgen aus einem Array einzugeben. Diese automatischen Variablen sollten folgendermaßen eingegeben werden: [SHORTCODE_7][SYSTEM_VAR_1][SHORTCODE_8]  
  
![DateTime Variablenbeispiel]([LINK_URL_26])

Solltest du bei deiner Transaktion automatische Variablen nutzen, findest du hier die [vollständige Liste verfügbarer automatischer Variablen]([LINK_URL_27]).

#### Benutzerdefinierte Variablen 

Weitere Informationen findest du in unserem Artikel zur [Nutzung von Transaktionsvariablen]([LINK_URL_28]).

### Datei-Upload bei Transaktionen [ANCHOR_5]

Damit deine Transaktion Dateien hochlädt, musst du zunächst die Datei(en) zur Vault hinzufügen. Hinweise, wie du Dateien zu deiner Vault hinzufügst, findest du in unserem [Artikel zur Vault]([LINK_URL_29]).

Sobald du die Datei zu deiner Vault hinzugefügt hast, kannst du die Transaktion für den Datei-Upload konfigurieren. Das Hochladen von Dateien nutzt die **Übernehmenaktion**. Du musst diese Aktion zu deiner Transaktion hinzufügen und dann für den Datei-Upload konfigurieren.

1.  Navigiere zum relevanten Transaktionsschritt-Editor, indem du die Prüfobjektoptionen aufrufst und dann zur Registerkarte [SHORTCODE_5]Schritte[SHORTCODE_6] wechselst.

2.  Füge eine **Übernehmenaktion** zu dem Schritt hinzu, in dem die Datei hochgeladen werden soll.

3.  Gib den richtigen [CSS- oder XPath-Selektor]([LINK_URL_30]) an, um das Element zum Datei-Upload auszuwählen.

    [SHORTCODE_3]**Hinweis**: Meistens handelt es sich bei dem Datei-Upload-Element, mit dem auf der Seite kommuniziert werden soll, um ein [INLINE_CODE_1]-Element. In einigen Fällen können diese Elemente auf der Seite verborgen werden und der Nutzer klickt stattdessen auf einen Link oder eine Schaltfläche. Die **Übernehmenaktion** sollte am tatsächlichen Datei-Upload-Element auf der Seite ausgeführt werden. Da solche Elemente nicht immer sichtbar sind, empfiehlt es sich in der Regel, die **Warte bis**-Option in der **Übernehmenaktion** von seinem Standardwert *Das Element sichtbar und aktiv ist* auf *Das Element existiert* zu setzen.[SHORTCODE_4]

4.  Klicke auf die Auslassungsschaltfläche neben **Neuer Wert**, um das Dialogfenster zu öffnen, in dem du den Elementwert angeben kannst.

5.  Klicke auf **Vault Datei Upload** und wähle die korrekte Datei. Sind in deiner Vault mehr als eine Datei vorhanden, werden sie nach Vault Bereichen aufgelistet.

    ![Screenshot des Auswahlmenüs zur Übernehmenaktion]([LINK_URL_31])

Damit ist die Transaktion mit einem Datei-Upload eingerichtet. Nun kannst du die Transaktionseinrichtung wie üblich fortsetzen.

![Datei-Upload]([LINK_URL_32])

### Optionen bei der Übernehmenaktion [ANCHOR_6]

Dir stehen mehrere Einstellungen für eine Übernehmenaktion zur Verfügung.

-  **Beschreibung** – eine Beschreibung der Aktion für Berichtszwecke.
- **Fehlermeldung** – die Meldung, die im Falle eines Fehlers in den Fehlerberichten aufgenommen wird.
- **Fehlerbehandlung** – die Auswahl des Kontrollkästchens **Ignoriere Fehler, die in dieser Aktion auftreten** weist das Prüfobjekt an, alle möglicherweise bei dieser Aktion vorkommenden Fehler, wie beispielsweise ein nicht gefundenes klickbares Element, zu ignorieren.
- **Warte bis** – bevor eine Klickaktion ausgeführt werden kann, muss das vom Prüfobjekt zu klickende Element auf der Seite geladen und sichtbar sein (in CSS-Begriffen ausgedrückt, muss das Element angezeigt (display) werden und sichtbar (visibility) sein). Für diese *Wartebedingungen* gibt es einen [speziellen Artikel in der Knowledge Base]([LINK_URL_33]), der dir Informationen zu den unterschiedlichen Optionen bietet.
- **Warte-Timeout** – du kannst angeben, wie lange das Prüfobjekt warten soll, damit die Warte bis-Anforderung erfüllt ist. Die Standard-Wartezeit beträgt 30 Sekunden. Du kannst diesen Standard mit einer maximalen Wartezeit von 60 Sekunden überschreiben.
- **Variable zuweisen** – gib einen Variablennamen im Format [INLINE_CODE_2] ein. Diese Variable enthält den Wert, der innerhalb der Aktion gesetzt wurde. Du kannst diese Variable dann in einem späteren Schritt oder einer Aktion verwenden.
- **Shadow DOM Host** – wenn das Objekt, mit dem eine Interaktion erfolgen muss, sich in einem Shadow DOM befindet, muss eine Transaktion so konfiguriert sein, dass sie das Objekt in diesem Shadow DOM sucht. Weitere Informationen findest du im Knowledge-Base-Artikel zum [Arbeiten mit einem Shadow DOM bei Transaktionen]([LINK_URL_34]).

## Hover [ANCHOR_7]

Wenn eine Seite Elemente enthält, die vom Nutzer erfordern, dass er mit der Maus über sie fährt, um eine Aktion wie Auswählen eines Untermenüs oder Auswahl von einem Drop-down-Menü auszuführen, benötigst du eine **Hover-Aktion**. Bevor ein Nutzer oder ein Prüfobjekt mit einem hinterlegten Element wie Links in einem Drop-down-/Pull-down-Menü interagieren kann, muss das Element auf der Seite sichtbar sein.

Da der Cursor während einer Transaktionsaufzeichnung immer auf der Seite in Bewegung ist, würde der Transaktionsrekorder fortlaufend Hover-Elemente aufnehmen, die du später entfernen müsstest. Statt möglicherweise hunderte Hover-Ereignisse entfernen zu müssen, nimmt der Rekorder keine Hover-Aktionen auf. Du musst daher alle erforderlichen Hover-Aktionen nach der Aufzeichnung hinzufügen.

In dem Beispiel unten musst du zunächst mit der Maus über dem Einkaufswagen schweben, um das Menü mit der Checkout-Option zu erhalten.

![Hover-Beispiel]([LINK_URL_35])

### Optionen für Hover-Aktionen

Dir stehen die folgenden Einstellungen für eine Hover-Aktion zur Verfügung (siehe Abbildung unten):

- **Beschreibung**: eine Beschreibung der Aktion für Berichtszwecke.
- **Fehlermeldungen**: Die Meldung, die im Falle eines Fehlers in den Fehlerberichten aufgenommen wird.
- **Fehlerbehandlung**: Die Auswahl des Kontrollkästchens **Ignoriere Fehler, die in dieser Aktion auftreten** weist das Prüfobjekt an, alle möglicherweise bei dieser Aktion vorkommenden Fehler, wie beispielsweise ein nicht gefundenes klickbares Element, zu ignorieren.
- *Warte bis**: Bevor eine Klickaktion ausgeführt werden kann, muss der Browser das Element auf der Seite laden und sichtbar machen. Für diese *Wartebedingungen* gibt es einen [speziellen Artikel in der Knowledge Base]([LINK_URL_36]), der dir Informationen zu den unterschiedlichen Optionen bietet.
- **Warte-Timeout**: Du kannst angeben, wie lange das Prüfobjekt warten soll, damit die Warte bis-Anforderung erfüllt ist. Die Standard-Wartezeit beträgt 30 Sekunden. Du kannst diesen Standard mit einer maximalen Wartezeit von 60 Sekunden überschreiben.
- **Shadow DOM Host**: Wenn das Objekt, mit dem eine Interaktion erfolgen muss, sich in einem Shadow DOM befindet, muss eine Transaktion so konfiguriert sein, dass sie das Objekt in diesem Shadow DOM sucht. Weitere Informationen findest du im Knowledge-Base-Artikel zum [Arbeiten mit einem Shadow DOM bei Transaktionen]([LINK_URL_37]).

![Seiteninteraktionen – Hover]([LINK_URL_38])

### Nach Hover-Aktionen Inhaltsprüfungen nutzen

Um zu prüfen, ob eine Hover-Aktion erfolgreich war und beispielsweise das Untermenü korrekt geladen hat, kannst du eine Inhaltsprüfung in Betracht ziehen. Damit verifizierst du, dass das Prüfobjekt mit dem Menü interagieren kann, bevor es weiter ausgeführt wird.


## Tastenereignis [ANCHOR_8]

Die Aktion *Tastenereignis* ermöglicht dir, einen einzelnen Tastendruck zu einem Transaktionsschritt hinzuzufügen. Diese Aktion kann praktisch sein, wenn es auf der Webseite ein Element gibt, das kein Klick-Element (Schaltfläche) ist, zum Beispiel, um einen Suchbegriff zu senden, wenn das Suchfeld keine Sende-Schaltfläche hat. 

Füge bei einem Transaktionsschritt eine neue Aktion hinzu und wähle die Aktion *Tastenereignis* aus der Liste der Seiteninteraktionen. Bei der neuen Aktion musst du ein Zeichen aus der Liste verfügbarer Zeichen auswählen. Gib bitte einen [CSS Selektor oder XPath]([LINK_URL_39]) an, um das Element zu identifizieren, wo die Taste eingegeben werden soll. 

### Optionen für Tastenereignis-Aktionen

Die folgenden Einstellungen sind für die Aktion *Tastenereignis* in einem Schritt verfügbar:

- **Beschreibung** – eine Beschreibung der Aktion für Berichtszwecke.
- **Fehlermeldung** – die Meldung, die im Falle eines Fehlers in den Fehlerberichten aufgenommen wird.
- **Fehlerbehandlung** – die Auswahl des Kontrollkästchens **Ignoriere Fehler, die in dieser Aktion auftreten** weist das Prüfobjekt an, alle möglicherweise bei dieser Aktion vorkommenden Fehler, wie beispielsweise ein nicht gefundenes klickbares Element, zu ignorieren.
- **Warte bis** – bevor eine Aktion ausgeführt werden kann, muss das mit dem Prüfobjekt zu interagierende Element auf der Seite geladen und sichtbar sein (in CSS-Begriffen ausgedrückt, muss das Element angezeigt (display) werden und sichtbar (visibility) sein). Für diese *Wartebedingungen* gibt es einen [speziellen Artikel in der Knowledge Base]([LINK_URL_40]), der dir Informationen zu den unterschiedlichen Optionen bietet.
- **Warte-Timeout** – du kannst angeben, wie lange das Prüfobjekt warten soll, damit die Warte bis-Anforderung erfüllt ist. Die Standard-Wartezeit beträgt 30 Sekunden. Du kannst diesen Standard mit einer maximalen Wartezeit von 60 Sekunden überschreiben.
- **Shadow DOM Host** – wenn das Objekt, mit dem eine Interaktion erfolgen muss, sich in einem Shadow DOM befindet, muss eine Transaktion so konfiguriert sein, dass sie das Objekt in diesem Shadow DOM sucht. Weitere Informationen findest du im Knowledge-Base-Artikel zum [Arbeiten mit einem Shadow DOM bei Transaktionen]([LINK_URL_41]).

![Tastenereignis – Beispiel]([LINK_URL_42])
