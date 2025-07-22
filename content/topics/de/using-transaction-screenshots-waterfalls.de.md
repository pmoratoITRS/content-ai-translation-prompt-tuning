{
  "hero": {
    "title": "Transaktions-Screenshots und Wasserfälle nutzen"
  },
  "title": "Transaktions-Screenshots und Wasserfälle nutzen",
  "summary": "Um deine Transaktionsskripte eingehend zu testen und um eine Fehlerbehebung durchführen zu können, solltest du die Wasserfallberichte und Screenshots prüfen. Damit kannst du die Quelle von Fehlern identifizieren und die Tauglichkeit deiner Skripte für das Transaktions-Monitoring bestätigen. ",
  "url": "/support/kb/synthetic-monitoring/transaktionen/transaktions-screenshots-wasserfaelle-nutzen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-transaction-screenshots-waterfalls"
}

Uptrends‘ [Transaktionsprüfobjekte]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) bieten mehrere Optionen zur Analyse und Fehlerbehebung. Zwei dieser Optionen sind Screenshots und Wasserfallberichte. Sie haben eine wesentliche Funktion im Transaktions-Monitoring-Toolkit und sind grundlegend für die Ursachen- und Performance-Analyse.

{{< callout >}}
**Hinweis**: Screenshots und Wasserfallberichte sind für alle Nutzer über die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} verfügbar. Jedoch können nur Abonnenten der **Enterprise**- und **Business**-Pläne sie während des Staging- oder Produktionsmodus hinzufügen.
{{< /callout >}}

## Screenshots und Wasserfallberichte aktivieren

1.   Navigiere zu den Einstellungen des Transaktionsprüfobjekts, für das du Wasserfallberichte/Screenshots aktivieren möchtest (zum Beispiel über {{< AppElement type="menuitem" >}} Überwachung > Prüfobjekteinrichtung {{< /AppElement >}} im seitlichen Menü).
2.   Wähle auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}} den Schritt, für den du einen Wasserfall/Screenshot aktivieren möchtest.
3.   Markiere das entsprechende Kontrollkästchen, um einen Wasserfall oder Screenshot für den Schritt zu aktivieren.

  -  Hinweis: Du kannst auch Screenshots innerhalb der Schritte in Form [einer Aktion]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-an-action" lang="en" >}}) hinzufügen.

  - Um die [Seitenquelle und die Daten des Konsolenprotokolls]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="de" >}}) anzuzeigen, muss die Wasserfalloption aktiviert sein.

Beachte, dass für jeden hinzugefügten Wasserfallbericht und Screenshot jeweils ein [Credit für Transaktionsprüfobjekte]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}) berechnet wird.


{{< callout >}}
**Hinweis**: Du kannst Transaktionswasserfälle konfigurieren, sodass sie [zusätzliche Metriken anzeigen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#metrics" lang="de" >}}), indem du **Chrome mit extra Metriken** als Browser auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} der Prüfobjekteinstellungen auswählst.
{{< /callout >}}



Uptrends erzeugt in den folgenden Situationen einen Wasserfallbericht oder Screenshot:

-   **Im Falle eines Fehlers:** Wenn während einer Transaktion ein bestätigter Fehler auftritt, wird ein Screenshot (aber **kein** Wasserfallbericht) erzeugt. Dafür musst du nichts einrichten, dies geschieht automatisch für den ersten bestätigten Fehler.
-   **Für jedes Prüfobjektergebnis:** Wenn du einen Wasserfallbericht oder Screenshot bei einem bestimmten Schritt aktiviert hast, nachdem dieser Schritt abgeschlossen ist.

## Screenshots und Wasserfallberichte finden

Screenshots und Wasserfallberichte sind unverzichtbar, wenn es um die Fehlersuche und Fehlerbehebung bei Transaktionen geht. Du erhältst sie automatisch, wenn du die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} nutzt. Enterprise- und Business-Anwender erhalten beim ersten bestätigten Fehler einen Screenshot.

### Wo finde ich Screenshots und Wasserfallberichte während der Fehlersuche?

Du nutzt die Schaltfläche „Jetzt testen“ sehr häufig, wenn du deine Transaktion im Entwicklungsmodus testest. Ein bedeutendes Ergebnis der „Jetzt testen“-Funktion sind Screenshots und Wasserfallberichte. Um auf sie zuzugreifen, klicke auf die Schaltfläche **Testergebnisse verfügbar** oben bei jedem einzelnen Schritt, nachdem der manuelle Test ausgeführt wurde.

![](/img/content/5e8923ca-fa6e-44ad-a8ef-02c744d36adb.png)

Scrolle nach dem Klicken auf **Testergebnisse verfügbar** auf der Seite hinunter zu **Debug Information**. Der Bericht beinhaltet automatisch die Fehlerdetails aus den manuellen Tests.

Klicke auf die Grafik, um den Screenshot oder den Wasserfall zu öffnen.

![Screenshot und Wasserfall nach “Jetzt testen”](/img/content/scr-waterfall-screenshot-after-test-now.min.png)

### Wo finde ich Screenshots und Wasserfall-Grafik in meinen Berichten?

Enterprise- und Business-Anwender finden die Staging- und Produktions-Screenshots im Bericht unter den Kontrolldetails. Navigiere im Uptrends Menü zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjektprotokoll{{< /AppElement >}}, um dein Prüfobjektprotokoll anzuzeigen.

**Screenshots**: Ein Kamera-Symbol bei deinem Prüfobjektprotokoll zeigt dir, dass ein Screenshot aufgenommen wurde.

**Wasserfallberichte**: Wenn du deinen Transaktionsskripten Wasserfalldiagramme hinzugefügt hast, enthält jeder Check ein oder mehr Diagramme. Das Prüfobjektprotokoll hat kein Symbol.

![](/img/content/f7f72770-69e4-4f8b-8b34-ed7c6a09848b.png)

Um den Screenshot oder den Wasserfallbericht anzuzeigen:

1. Klicke, um den Kontrolldetailbericht zu öffnen.
2. Scrolle zum Abschnitt **Kontrolldetails**.
3. Klicke auf das Symbol für Kamera oder Wasserfall bei den Schrittergebnissen.

![](/img/content/70d49d55-56e4-4989-9259-1bea703b0bb3.png)

## Screenshots zur Fehlerfindung nutzen

Damit du die am Bildschirm sichtbaren Ergebnisse verfolgen kannst, wird während des Tests ein Screenshot aufgenommen. Der Screenshot zeigt, wie der Ansichtsbereich ausgesehen hat – nach einem erfolgreichen Schritt oder nach einem Seitenfehler. Wenn die Aktion weiter unten auf der Seite stattfindet, kannst du vor dem Klick-Event eine Scroll-Aktion einfügen.

Sieh dir den Screenshot an, um Folgendes zu verifizieren:

-   **Erwarteter Inhalt wurde geladen.** Prüfe nach einer Navigation auf korrekten Inhalt.
-   **Dynamische Inhalte, die aus Nutzereingaben resultieren**, funktionieren einwandfrei. Wenn beispielsweise eine Auswahl einer Farbe erfolgen muss, bevor die Größenoptionen verfügbar werden, verifiziere, dass das Element richtig ausgefüllt ist.
-   **Maskierte Felder funktionieren wie erwartet.** Ist die Formatierung korrekt?
-   **Das Responsive Design ändert sich.** Wenn deine Website sich auf Responsive Design stützt, musst du eventuell die Browser-Auflösung in deinen Prüfobjekteinstellungen anpassen. Indem du die Browser-Auflösung anpasst, kannst du sicherstellen, dass du das richtige Seitenlayout erhältst. Beispielsweise solltest du, wenn dein Menü sich auf ein Hamburger-Symbol verringert, sobald das Browser-Fenster kleiner wird, zusätzliche Klick- oder Hover-Aktionen hinzufügen. Passe bei dem Prüfobjekt die Browser-Auflösung auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} an.

## Wasserfälle zur Fehlerfindung nutzen

Der Wasserfallbericht liefert detaillierte Informationen zu den anfänglichen Ladezeiten der Seite. Er zeigt genau, wie lang es gedauert hat, jedes Seitenobjekt abzurufen und zu verarbeiten, zusammen mit den Anfrage- und Antwort-Headern. Anhand von Wasserfalldiagrammen kannst du Probleme schnell identifizieren. Unser Artikel [Die Wasserfall-Grafik]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart#what-is-presented-in-the-waterfall-chart" lang="de" >}}) hält weitere Informationen zu dem bereit, was in dem Wasserfalldiagramm enthalten ist und wie es zur Fehlerbehebung verwendet werden kann.

![](/img/content/d4dee11f-d9f9-464c-a988-4d0c4254100b.png)


