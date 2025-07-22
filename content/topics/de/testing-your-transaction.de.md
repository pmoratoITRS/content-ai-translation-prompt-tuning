{
  "hero": {
    "title": "Testen und Bearbeiten deines Transaktionsskripts"
  },
  "title": "Testen und Bearbeiten deines Transaktionsskripts",
  "summary": "Wenn du dich nach Aufzeichnen der Transaktion dazu entscheidest, sie selbst zu bearbeiten und zu testen, hilft dir dieser Leitfaden.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/tutorial-record-user-journey-in-shop/testen-der-transaktion",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction"
}

In dieser Übung gehst du durch den Bearbeitungs- und Testablauf für eine einfache Transaktion. Dabei werden einige Fehler behoben.

Die hier verwendeten Beispiele entstammen einer früheren Übung: [Aufzeichnen der User Journey bei Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="de" >}}). Wenn du diese Übung noch nicht abgeschlossen hast, solltest du das jetzt nachholen oder du kannst das [Skript in den Step-Editor hineinkopieren]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/test-script" lang="de" >}}).

## Manuelles Testen im Entwicklungsmodus

Es gibt drei Prüfobjektmodi: Development, Staging und Produktion. Das Testen im Entwicklungsmodus ist der wichtigste Schritt, den du ausführen kannst, bevor du das Transaktionsskript in den Staging- oder Produktionsmodus überführst. Erfahre mehr über die [Prüfobjektmodi]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}).

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf.
2. Öffne das Transaktionsprüfobjekt, das vom Transaktions-Recorder hochgeladen wurde.
3. Stelle sicher, dass du dich auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} befindest.
4. Setze im Abschnitt *Status* den *Modus* auf „Development“.
5. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche.

{{< callout >}}
**Tipp**: Halte die Taste [Strg] bzw. Ctrl gedrückt, während du auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}} klickst, um das Prüfobjektfenster nach dem Speichern geöffnet zu lassen. Andernfalls wirst du nach dem Speichern zum Überblick der *Prüfobjekte* zurückgeführt.
{{< /callout >}}

## Das Testen mit „Jetzt testen“ starten

Gleich ob du ein Skript direkt aus dem Transaktions-Recorder hast, Änderungen an einem Skript vornimmst oder Probleme bei einem Skript in Produktion behebst, du kannst es mithilfe der {{< AppElement type="buttonSecondary" >}}Jetzt testen{{< /AppElement >}}-Schaltfläche testen. Um auf Probleme zu prüfen, kannst du so einen schnellen Test ausführen.

1. Öffne das Transaktionsprüfobjekt, das für dieses Tutorial erstellt wurde.
2. Klicke auf {{< AppElement type="buttonSecondary" >}}Jetzt testen{{< /AppElement >}} am Ende der Seite. Das Pop-up-Fenster *Testen von:* erscheint.
3. Wähle einen Checkpoint, von dem der Test ausgeführt wird.
4. Klicke auf {{< AppElement type="button" >}} Jetzt testen {{< /AppElement >}}.

{{< callout >}}
**Wichtig**: Ein erfolgreich verlaufener Test im Entwicklungsmodus heißt nicht, dass das Transaktionsskript stabil läuft. Befolge alle Testempfehlungen, bevor du ein Transaktionsskript in den Produktionsmodus überführst.
{{< /callout >}}

Wenn du den Test angestoßen hast, scrollt der Editor automatisch zum Anfang der Seite und der Checkpoint fügt dein Prüfobjekt zur Testschleife hinzu. Sobald der Test startet, kannst du sehen, wie der Checkpoint die Schritte deines Skripts ausführt. Sollte dein Skript den Test erfolgreich ausführen, ist das gut. Aber es sind weitere Tests erforderlich.

Wenn du das Beispielskript verwendest, wirst du sehen, dass *Schritt 1* (Navigieren) und *Schritt 2* (Auf ein Element klicken) ohne Probleme ausgeführt wurden, aber *Schritt 3* hat bei der Aktion 3.3 nicht funktioniert.

![Screenshot Testergebnis mit Fehler](/img/content/scr_transaction-tutorial-failedTest.min.png)

{{< callout >}}
**Tipp**: Während des manuellen Testens über die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} enthalten deine Testergebnisse Wasserfalldiagramme und Screenshots, um dir bei der Fehlerbehebung zu helfen. Klicke auf {{< AppElement type="button" >}}Testergebnisse verfügbar{{< /AppElement >}}, um die Screenshots und Wasserfallberichte anzuzeigen. Wird das Prüfobjekt in den Staging- oder Produktionsmodus verschoben, können nur Nutzer mit Business oder Enterprise Account optional Wasserfallberichte und Screenshots zu Schritten hinzufügen.
{{< /callout >}}

## Problembehebung beim Skript

Eine Transaktion kann im Entwicklungsmodus aus vielen Gründen einen Fehler zurückgeben, beispielsweise fehlende Inhalte oder es gibt eine nicht angemessene Selektorenauswahl für Elemente, Registerkarten und Frames. Zeitliche Probleme und fehlende Interaktionen könnten ebenfalls eine Rolle spielen. Sieh dir die folgenden Tipps für die häufigsten Probleme an.

### Problem: Element nicht gefunden aufgrund dynamischer IDs

Beim Test des Beispielskripts kannst du bei den Testergebnissen sehen, dass das Prüfobjekt das im CSS-Selektor spezifizierte Element nicht finden konnte. Die Aktion sagt dem Checkpoint, die Menge zu ändern, aber da das Prüfobjekt das Element nicht findet, schlägt die Aktion fehl. Der Knowledge-Base-Artikel [Selektoralternativen]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="de" >}}) hält weitere Infos zu Selektoren bereit.

![Screenshot fehlgeschlagene Aktion](/img/content/scr_transaction-tutorial-failedstep.min.png)

Der vollständige CSS-Selektor lautet:

`#quantity_6346b8b92ac97`

Das Prüfobjekt wartet bei der Seite auf ein Element mit der ID „quantity_6346b8b92ac97“. Wenn es erscheint, setzt das Prüfobjekt den Wert des Elements auf „2“. Das Element mit der ID „quantity_6346b8b92ac97“ erschien jedoch nicht. Warum? Der Selektor sucht nach einer bestimmten ID, aber der Server generiert die ID des Elements dynamisch. Jedes Mal, wenn die Seite lädt, vergibt der Server für das Element eine andere ID. Um dies zu beheben, gibt es andere Möglichkeiten als die ID, um ein Element zu identifizieren.

### Lösung: Einen anderen Selektor verwenden

Um das Problem zu umgehen, das durch dynamische IDs entsteht, benötigst du einen anderen Selektor. Klicke auf die Ellipsen-Schaltfläche {{< AppElement type="button" >}}…{{< /AppElement >}} im Selektorenfeld, um eine Liste anderer möglicher Selektoren anzuzeigen.

![Screenshot Details fehlgeschlagener Aktion](/img/content/scr_transaction-tutorial-failedstep-detail.min.png)

Ein Pop-up-Fenster mit [Selektoralternativen]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="de" >}}) wird geöffnet:

![Alternative Selektoren](/img/content/scr_transaction-tutorial-alternativeselectors.min.png)

In diesem Fall wirst du feststellen, dass mehrere der Selektoren den dynamisch erzeugten Wert verwenden, sodass du diese direkt ausschließen kannst. Zwei Optionen enthalten nicht die dynamische ID: *name* und *xpath:idRelative*. Der Recorder nimmt automatisch die Selektoren auf Grundlage seiner Einschätzung, welcher Selektor am besten funktionieren wird. In diesem Fall ist das die zweite Empfehlung: „name“ könnte besser zur Identifizierung des Elements funktionieren. Der Name-Wert ist ein Elementattribut. Ist es auf deiner Seite einzigartig, ist dieser Selektor wahrscheinlich die beste Wahl.

Tatsächlich funktioniert die Option *xpath:idRelative* in diesem Fall auch. Uptrends hat dir zwei gute Möglichkeiten bereitgestellt, die hervorragend im Entwicklungsmodus funktionieren. Aber ganz sicher, dass sie wirklich geeignet sind, bist du erst, wenn du das Skript in den Staging-Modus verschiebst. Aber es gibt noch mehr zu beachten, bevor du dein Prüfobjekt in den Staging- oder Produktionsmodus übergibst.

### Problem: Element nicht gefunden aufgrund mangelnder Nutzerinteraktion

Ähnlich wie dynamische IDs können auch dynamische Inhalte, die eine Nutzerinteraktion erfordern, damit ein Element sichtbar wird, für Probleme sorgen. Es kann sich als etwas schwierig herausstellen, sie zu identifizieren, aber du solltest zu Beginn die Einzelheiten deiner Nutzerinteraktionen genau unter die Lupe nehmen.

### Lösung: Hover-Aktionen hinzufügen

Einige Seitenelemente laden nicht oder werden nicht sichtbar, bis der Nutzer mit dem Mauszeiger darüberfährt. Wenn ein Nutzer beispielsweise mit der Maus über ein Menü fahren muss, damit die untergeordneten Menüpunkte sichtbar und anklickbar werden, muss das Skript diese Hover-Aktion ebenfalls ausführen. Allerdings kann der Transaktions-Recorder Hover-Aktionen nicht erfassen und wenn ein Element nicht auf der Seite sichtbar ist, kann das Skript nicht mit ihm interagieren. Du wirst eine Hover-Aktion manuell hinzufügen müssen, bevor die davon abhängige Interaktion erfolgen kann. Erfahre mehr über [Hover-Aktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="de" >}}) und wie du sie konfigurierst.

### Problem: Fehler aufgrund einer Zeitüberschreitung

Wird das Skript ausgeführt, sucht es und wartet auf das Laden von Elementen. Die Standard-Wartezeit beträgt 30 Sekunden, was in der Regel ausreichend Zeit ist. Sollten 30 Sekunden jedoch nicht genügen, kannst du zusätzliche Wartezeiten zu einer Aktion hinzufügen. Weitere Informationen zur Verwendung von Wartebedingungen findest du im Knowledge-Base-Artikel [Einsatz von Wartebedingungen]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="de" >}}).

### Lösung: Gründe und (mögliche) Lösungen für Zeitprobleme

Wenn du ein Zeitproblem festgestellt hast, kann es unterschiedliche Ursachen und Lösungen geben.

-  **Element steht noch nicht für Interaktionen zur Verfügung** – verlängere die Wartezeit.
-  **Transaktions-Zeitüberschreitung** – eine Transaktion verfügt über eine maximale Laufzeit. [Wende dich an den Support]({{< ref path="contact" lang="de" >}}). Er sieht sich dein Skript an und hilft dir, das Problem zu finden.

{{< callout >}}
**Wichtig**: Wir können nicht genug betonen, wie wichtig Inhaltsprüfungen für den Erfolg deines Transaktions-Monitorings sind. Füge bitte Übereinstimmungsprüfungen nach jeder Aktualisierung der Navigation oder Inhalte ein. Nutze sie vor jeder Interaktion. [Inhaltsprüfungen]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}) sind kostenlos, und machen das Transaktions-Monitoring robuster.
{{< /callout >}}

### Problem: Fehler bei Übernehmenaktion

Fehlende Klicks vor [Übernehmenaktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="de" >}}) können zu unerwarteten Fehlermeldungen führen. Vermeide Fehler, indem du immer eine [Klickaktion]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="de" >}}) für jede Übernehmenaktion einrichtest.

### Lösung: Klickaktion hinzufügen

**Verwende nicht die Eingabetaste** – bei der Aufzeichnung deiner Transaktion hast du eventuell die Eingabetaste verwendet, statt auf die Sende-Schaltfläche zu klicken. Wenn du zum Beispiel die Suchfunktion nutzt, ist das gewöhnliche Vorgehen, die Eingabetaste zu drücke, statt die Such-Schaltfläche. Der Rekorder kann das Drücken der Eingabetaste nicht erfassen. Wenn du feststellst, dass dir dies während der Aufzeichnung unterlaufen ist, füge die Klickaktion hinzu. Wenn es keine Schaltflächenoption gibt, [wende dich an unseren Support]({{< ref path="contact" lang="de" >}}), um eine Lösung zu erarbeiten.

**Fehlende Klicks** – entferne keine Klicks, die vor der Eingabe von Werten in Felder erscheinen. Klick-Ereignisse lösen Wertemasken und andere Ereignisse im Browser aus. In manchen Fällen ist das Hinzufügen von zwei Klicks erforderlich, bevor ein Wert eingegeben wird.

Erfahre mehr über [Klickaktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="de" >}}).

## Test-Checkliste für Skripte

Bevor du dein Transaktionsprüfobjekt in die Staging-Phase übergibst, solltest du mehrere Dinge prüfen.

- **Füge [Inhaltsprüfungen]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}) hinzu.** Füge zu jedem Seitenwechsel Inhaltsprüfungen hinzu, um sicherzustellen, dass die richtige Seite mit dem zugehörigen Inhalt geladen wurde.
- **Prüfe die [Screenshots und Wasserfälle]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}).** Im Entwicklungsmodus wird für jeden Schritt ein Screenshot des Browser-Fensters und ein Wasserfalldiagramm erzeugt, um Seitenfluss, Inhalt und Korrektheit von Produkten/Elementen zu verifizieren.
- **Lies über die [Vorbehalte bei der Transaktionseinrichtung]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}})** nach. Stelle sicher, dass dein Monitoring sich nicht negativ auf dein Geschäft auswirkt.
- **Füge [Klickaktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="de" >}}) hinzu**, bevor du Werte in Textfelder eingibst.

## In den Staging-Modus wechseln

Wenn du dein Skript im Entwicklungsmodus bearbeitet und getestet hast, ist der nächste Schritt, es in den Staging-Modus zu setzen. Erfahre mehr über die [Prüfobjektmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}).

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf.
2. Öffne das Transaktionsprüfobjekt, das für dieses Tutorial erstellt wurde.
3. Stelle sicher, dass du dich auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} befindest.
4. Ändere den **Modus** auf „Staging“.
5.  Setze das Prüfobjekt durch Markieren des Kontrollkästchens auf **Aktiviert**.
6.  Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}.

Du solltest das neue Transaktionsprüfobjekt ein paar Wochen im Staging-Modus nutzen, um seine Stabilität insbesondere nach Website-Aktualisierungen zu testen. Die Tests mit dem ausgedehnteren Checkpoint-Netzwerk auszuführen, kann zudem lokale Probleme aufzeigen.

Obwohl die Tests im Staging-Modus keine Alarme generieren, kannst du die Prüfobjektprotokolle und das **Transaktions**-Dashboard anzeigen, um Fehler zu sehen, die dein Prüfobjekt möglicherweise entdeckt hat. Im *Prüfobjektprotokoll* (und in anderen Dashboards) siehst du ein Erlenmeyerkolben-Symbol neben deinem Prüfobjekt im Staging-Modus.

![Screenshot Prüfobjektprotokoll](/img/content/scr_transaction-tutorial-stagingmode.min.png)


Klicke auf den Zeitstempel des Fehlers, um den Bericht [Kontrolldetails]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/making-sense-of-your-transaction-dashboards-and-reports#tutorial-check-details" lang="de" >}}) zu öffnen, der dir Informationen zur Transaktion bis und einschließlich des Fehlers bietet.
