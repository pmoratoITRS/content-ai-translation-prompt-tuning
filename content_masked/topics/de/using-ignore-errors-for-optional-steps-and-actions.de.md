{
  "hero": {
    "title": "Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen"
  },
  "title": "Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen",
  "summary": "Deine Transaktionsskripte müssen in der Lage sein, auf dynamische Website-Änderungen zu reagieren. Das Ignorieren von Fehlern bietet dir die erforderliche Kontrolle, um Bedingungen bzw. das Übergehen in den Schritten und Aktionen deines Skripts einzufügen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/ignoriere-fehler-bei-optionalen-schritten-und-aktionen",
  "translationKey": "[URL_1]
}

Es ist selten, dass eine Website keine dynamischen Variationen im Klickpfad eines Nutzers aufweist. Eine Website kann aus vielen Gründen über dynamische Variation im Inhalt verfügen:

-   Unterschiedliche Seiten je nach Nutzerstandort
-   A/B-Tests
-   Änderungen bei Eingabefeldern
-   Cookie Walls
-   Vorübergehend eingefügte Seiten

Jede Variation im Klickpfad sorgt für Herausforderungen bei deinen Transaktionsskripten. Bedingungsaussagen in der Form von *ignoriere Fehler* können helfen, dynamische Seitenänderungen, wie wir sie oben aufgezeigt haben, zu umschiffen.

## Inwiefern ist „ignoriere Fehler“ gleich einer Bedingung?

Wenn du entscheidest, Fehler zu ignorieren, sagst du dem Prüfobjekt, eine Aktion zu versuchen, aber auf Grundlage vom Fehlschlagen (oder Erfolg) der Assertion oder Aktion eine andere Aktion folgen zu lassen. Betrachte die Option zum Ignorieren von Fehlern als eine Bedingungsaussage. Du kannst das Ignorieren von Fehlern sowohl auf Schritt-Ebene als auch bei einzelnen Aktionen einrichten.

-   **Ignorieren von Fehlern auf Schritt-Ebene** Mit der Bestimmung, Fehler auf Schritt-Ebene zu ignorieren, sagst du dem Skript, den Schritt aufzugeben und mit dem nächsten Schritt fortzufahren, wenn das Skript einen Fehler identifiziert: Wenn Aktion X bei dem Schritt Y erfolgreich ist, fahre fort; wenn Aktion X bei dem Schritt Y fehlschlägt, gib den Schritt auf und fahre fort mit Schritt Z.
-   **Ignorieren von Fehlern auf Aktions-Ebene**
     Mit der Bestimmung, Fehler auf Aktions-Ebene zu ignorieren, sagst du dem Skript, die nächste Aktion auszuführen, selbst wenn die Aktion fehlgeschlagen ist: Wenn Aktion X erfolgreich ist, fahre fort mit Aktion Y; wenn Aktion X fehlschlägt, fahre trotzdem mit Aktion Y fort.

## Wie funktionieren Schritte und Aktionen, die übergangen werden können?

Wenn deine Transaktion normalerweise auf einen Fehler trifft, wird das Skript gestoppt und Uptrends verzeichnet den Fehler. Der Fehler führt eventuell dazu, dass Uptrends eine Warnmeldung sendet, wenn der Fehler von einem weiteren Checkpoint bestätigt wird. Wenn du den Fehler als ignorierbar erklärst, wird das Skript mit dem nächsten Schritt oder mit der nächsten Aktion (abhängig davon, ob du den Fehler auf Schritt- oder Aktions-Ebene ignorieren lässt) weiter ausgeführt. Uptrends verzeichnet den Fehler im Prüfbericht, aber übergangene Fehler wirken sich nicht auf das Reporting für die Website aus.

### Fehler bei Schritten ignorieren

Das Ignorieren von Fehlern auf Schritt-Ebene zu aktivieren, führt dazu, dass das Skript den aktuellen Schritt nicht weiter ausführt und zum nächsten Schritt weitergeht, wenn eine Aktion einen Fehler aufweist. Abbildung 1 stellt beispielsweise eine Transaktion mit einer Cookie Wall dar. Für die Cookie Wall ist es erforderlich, dass der Nutzer eine Akzeptieren-Schaltfläche klickt, wenn die Wall erscheint. Allerdings erscheint die Wall nicht für alle Nutzer.

Um die Cookie Wall zu handhaben, richten wir einen ignorierbaren Fehler im Schritt ein. In diesem Fall stellt eine Inhaltsprüfung fest, ob die Website eine Cookie Wall (in Schritt X in Abbildung 1 dargestellt) eingefügt hat. Gibt es eine Cookie Wall, verzeichnet die Inhaltsprüfung einen Erfolg, das Prüfobjekt klickt auf die Schaltfläche zum Akzeptieren der Bedingungen und das Skript wird mit Ausführung von Schritt Y fortgesetzt. Findet die Inhaltsprüfung keine Cookie Wall, verzeichnet Schritt X einen Fehler, aber das Prüfobjekt fährt trotzdem mit Schritt Y fort. Bei Schritt Y wurde das Ignorieren von Fehlern nicht aktiviert, sodass alle Fehler, die bei Schritt Y auftreten, dafür sorgen, dass das Prüfobjekt das Skript nicht weiter ausführt und Uptrends verzeichnet den Fehler.

![]([LINK_URL_1])

*Abbildung 1:* Einsatz der Option, Fehler zu ignorieren, um festzustellen, ob eine Cookie Wall besteht, und dies zu handhaben.

### Fehler bei Aktionen ignorieren

Wenn du Fehler bei einzelnen Aktionen ignorierst, fährt das Skript mit der nächsten Aktion fort. Abbildung 2 stellt eine Transaktion mit einem A/B-Test dar. In Schritt X erfordert das Skript, dass die Aktionen 1 und 2 erfolgreich ausgeführt werden, aber die Aktionen 3 und 4 gelten nur für Version A der Seite. Wenn du Fehler für die Aktionen 3 und 4 nicht ignorierst, wird das Skript jedes Mal einen Fehler feststellen, wenn der Server Seite B sendet.

![]([LINK_URL_2])

Abbildung 2: Ablaufdiagramm für eine Transaktion mit einem A/B-Test.

## Beispiele

Sehen wir uns einige übliche Beispiele an. Dein jeweiliger Fall erfordert eventuell eine andere Lösung. [Lasse uns wissen]([LINK_URL_3]), wenn du Hilfe bei deiner Lösung benötigst.

[SHORTCODE_1]
**Hinweis**: Als allgemeine Regel gilt, Fehler bei Aktionen zu ignorieren, wenn es sich um eine einzelne Aktion handelt, und Fehler bei einem Schritt zu ignorieren, wenn mehr als eine Aktion auf Basis einer Bedingung übergangen werden muss.
[SHORTCODE_2]

### Use case: Unterschiedliche Klickpfade aufgrund des Nutzerstandorts

Gelegentlich verhalten sich Websites abhängig vom Nutzerstandort aus verschiedenen Gründen wie etwa behördliche Bestimmungen, Verfügbarkeit von Produkten in einer Region oder der Sprache unterschiedlich. Wenn sich ein Nutzer beispielsweise in der EU befindet, muss die Website die Bestätigung einholen, dass der Nutzer die Bedingungen der personenbezogenen Datenerfassung von Besuchern zur Kenntnis nimmt. Die Website blendet ein Pop-up ein, bei dem der Nutzer ein Feld zur Bestätigung der Kenntnisnahme markieren muss. Der Nutzer muss auch auf eine Schaltfläche zum Fortfahren klicken.

#### Lösung: Ignorierbarer Schritt

Bei diesem Beispiel muss der Nutzer zwei Aktionen ausführen, um vollständig auf die Website zuzugreifen, daher ist ein ignorierbarer Schritt eine gute Wahl.

1.  Füge einen Schritt an dem Punkt der Transaktion ein, an dem der Nutzer die Eingabeaufforderung erhält.
2.  Aktiviere bei dem Schritt die Option, Fehler zu ignorieren.
3.  Füge eine Klickaktion ein, bei der das Kontrollkästchen markiert wird.
4.  Füge eine Klickaktion ein, bei dem die Schaltfläche zum Fortfahren geklickt wird.

Schlägt die Klickaktion in Schritt 3 fehl, wurde dem Nutzer die Eingabeaufforderung nicht angezeigt. Das Skript verlässt den Schritt und fährt mit der ersten Aktion im nächsten Schritt fort. Andernfalls akzeptiert das Prüfobjekt die Bedingungen, indem es die entsprechenden Aktionen ausführt, und die Transaktion wird wie üblich ausgeführt.

### Use case: A/B-Tests

Ein A/B-Test ermöglicht dir, Nutzerinteraktionen anhand zweier unterschiedlicher Versionen derselben Seite zu vergleichen. Im Vergleich zu Seite B erfordert Seite A vom Nutzer vielleicht die Eingabe weiterer persönlicher Daten. Der Test stellt fest, welche Seite mehr Konversionen bringt. Der Server liefert Nutzern unterschiedliche Seitenversionen nach dem Zufallsprinzip. Die Änderungen bei den unterschiedlichen Seiten können bewirken, dass das Prüfobjekt einen Fehler feststellt.

#### Lösung: Ignorierbare Aktionen

In diesem Fall muss das Prüfobjekt einige Aktionen ausführen, gleich welche Seite gesendet wurde, und eine oder mehrere Aktionen übergehen, die sich auf eine andere Seitenversion beziehen. A/B-Tests lassen sich folgendermaßen handhaben:

1.  Verwende für Interaktionen, die beiden Seiten gemeinsam sind, Aktionen, bei denen Fehler nicht ignoriert werden.
2.  Aktiviere bei den zusätzlichen Feldern, Fehler zu ignorieren.

Indem du die Aktionen so einrichtest, dass Fehler bei zusätzlichen Feldern ignoriert werden, kann die Transaktion weiter ausgeführt werden, gleich welche Version der Seite das Prüfobjekt erhält (Abbildung 2).

### Use case: Sich ändernde Feld-Optionen

Nehmen wir eine E-Commerce-Website für Bekleidung mit sich schnell änderndem Inventar an. Deine Transaktion nimmt den ersten Artikel, der bei einer Suche gelistet wird. Aber der erste Artikel ändert sich häufig. Obwohl jeder Artikel über ein Mengenfeld verfügt, haben nicht alle Artikel ein Größenfeld (z. B. ein Schal), eine Farbwahl (es gibt den Artikel nur in schwarz) oder weder das eine noch das andere (eine Handtasche). Die Änderungen bei verfügbaren Aktionen können dafür sorgen, dass das Prüfobjekt einen Fehler ausgibt, wenn es versucht, eine Farbe zu wählen, wenn die Farbe nicht zur Wahl steht.

#### Lösung: Ignorierbare Aktionen

Da nicht alle Auswahlfelder auf allen Seiten vorhanden sind, solltest du Fehler bei Aktionen ignorieren, die Werte für Elemente eingeben, die für die Transaktion nicht gelten. Sich ändernde Feld-Optionen kannst du wie folgt handhaben:

1.  Füge einen Schritt hinzu.
2.  Füge die entsprechenden Aktionen für jede mögliche Seiteninteraktion ein: Menge, Größe und Farbe.
3.  Belasse die Option zum Ignorieren von Fehlern für die Menge deaktiviert, aktiviere die Kontrollkästchen für das Ignorieren von Fehlern bei den Aktionen Größe und Farbe.

Das Skript versucht, jeden Wert einzugeben. Wenn das Element nicht vorhanden ist, schlägt die Aktion fehl, aber das Skript fährt mit der nächsten Aktion fort (Abbildung 2).

### Use case: Eingefügte Nachrichten-Seiten

Gelegentlich muss eine Website Nutzer über Vorgänge benachrichtigen, etwa bevorstehende Wartungen, Änderungen der Nutzungsbedingungen oder Werbeaktionen. Die Website fügt zeitlich beschränkte Seiten mit der Nachricht in den üblichen Klickpfad des Nutzers ein. Die Seite erfordert häufig eine Nutzeraktion, damit dieser die Benachrichtigung zur Kenntnis nimmt.

#### Lösung: Ignorierbare(r) Schritt oder Aktion

Bei diesem Use Case gibt es eventuell eine oder mehrere Nutzerinteraktionen, um mit der Transaktion fortzufahren.

**Erfordert die Kenntnisnahme eine einzelne Aktion, verwende eine ignorierbare Aktion**. Füge die Aktion an entsprechender Stelle ein und aktiviere die Option, Fehler bei der Aktion zu ignorieren.

**Erfordert die Kenntnisnahme mehrere Aktionen, verwende einen ignorierbaren Schritt**.

1.  Füge einen Schritt an der Stelle im Skript ein, an der die Nachricht erscheint.
2.  Aktiviere bei dem Schritt die Option, Fehler zu ignorieren.
3.  Füge die entsprechenden Aktionen zum Schließen der Seite hinzu: Akzeptiere die neuen Bedingungen, nimm die Nachricht zur Kenntnis und reiche die Antwort ein.

Ist der Schritt oder die Aktion erfolgreich, fährt die Transaktion fort. Schlägt der Schritt oder die Aktion fehl, gibt es keine Nachrichtenseite, es wird keine weitere Aktion benötigt und das Skript fährt mit der nächsten Aktion oder dem nächsten Schritt fort.
