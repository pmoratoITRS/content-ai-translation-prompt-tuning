{
  "hero": {
    "title": "Die Wasserfall-Grafik"
  },
  "title": "Die Wasserfall-Grafik",
  "url": "/support/kb/synthetic-monitoring/monitoring-ergebnisse/wasserfall-grafik",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/waterfall-chart"
}

Die Wasserfall-Grafik ist eine visuelle Repräsentation der Testergebnisse eines Prüfobjekts in Bezug auf das Laden von Seitenobjekten. Die Wasserfall-Grafik gehört zu den Kontrolldetails.

Bei Full Pagechecks (FPCs) wird der Wasserfallbericht standardmäßig mitgeliefert. Bei Transaktionsprüfobjekten kannst du bei jedem Schritt entscheiden, ob eine Wasserfall-Grafik hinzugefügt werden soll. Unser Knowledge-Base-Artikel [Transaktions-Screenshots und Wasserfälle nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}) sagt dir mehr dazu, wie das funktioniert.

## Wasserfälle zur Fehlerfindung nutzen

Es ist eine Sache, die Gesamtzeit-Performance der Seite zu kennen, aber der Wasserfall schlüsselt die Ladezeit für jedes Seitenobjekt auf.

-   Du siehst die Zeiten für Auflösung, TCP-Verbindung, HTTPS Handshake, Send, Wait und Receive sowie Zeitüberschreitungen für jedes Objekt. Die Zeiten werden im Knowledge-Base-Artikel  [Zeiten in Wasserfall-Grafiken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="de" >}}). erläutert.
-   Du siehst den Ladefortschritt der Seite. Langsame Objekte sowie solche, die das Laden blockieren, lassen sich leicht mit der Wasserfall-Grafik erkennen.
-   Du kannst nicht geladene Seitenobjekte identifizieren. Prüfe die Anfrage- und Antwort-Header auf Hinweise zum fehlgeschlagenen Laden. Beispielsweise kannst du feststellen, ob ein CDN-Knoten den falschen Inhalt gesendet hat oder ob die Antwort zu langsam war.

## Wo ist die Wasserfall-Grafik zu finden? {id="where-is-the-waterfall-chart-located"}

Sowohl bei FPCs als auch bei Transaktionsprüfobjekten ist die Wasserfall-Grafik den Kontrolldetails zugeordnet. Wie du darauf zugreifst, unterscheidet sich jedoch leicht. Folge den unten genannten Schritten.

### Eine FPC-Wasserfall-Grafik öffnen

Um den Wasserfallbericht zu öffnen, rufe die Kontrolldetails des Prüfobjekts auf. Folge diesen Schritten:

1. Wechsle zum Dashboard *Prüfobjektprotokoll*. Du kannst die Seite schnell aufrufen, wenn du „Prüfobjektprotokoll“ in das Suchfeld der Navigation eingibst.

2. Öffne eins der Ergebnisse des FPC-Prüfobjekts, indem du auf die entsprechende Zeile klickst.

3. Die Kontrolldetails werden angezeigt, der Wasserfallbericht befindet sich am Ende.

### Die Wasserfall-Grafik eines Schritts bei Transaktionsprüfobjekten öffnen

Der Wasserfallbericht befindet sich in den Kontrolldetails des Prüfobjekts.

1. Wechsle zum *Prüfobjektprotokoll* und öffne das Ergebnis eines Transaktionsprüfobjekts.

2. Du findest die **Ergebnisse für jeden Schritt** am Ende. Klicke auf das Wasserfall-Symbol {{< AppElement type="iconWaterfall" >}}{{< /AppElement >}}, um die Wasserfall-Grafik zu öffnen.

### Wasserfall-Grafik – Beispiel

Wenn du einen Wasserfallbericht öffnest, wird das Diagramm ähnlich dem im Bild aussehen.

![Screenshot Wasserfalldiagramm](/img/content/scr_waterfall_chart-overview.min.png)

## Was wird in der Wasserfall-Grafik angezeigt? {id="what-is-presented-in-the-waterfall-chart"}

Die Wasserfall-Grafik zeigt in der ersten Spalte die Namen (URLs) der Seitenobjekte, dann die Größe des Seitenobjekts und dann die Ladezeiten, die während der Prüfung durch das Prüfobjekt für alle geladenen Objekte gemessen wurden.
Die Messungen werden chronologisch von links nach rechts dargestellt. Jedes Seitenobjekt belegt eine eigene Zeile.
Um ein Seitenobjekt zu laden, sind einige Schritte erforderlich.

Die einzelnen Schritte sind farblich markiert. Für die Farbcodierung findest du über dem Diagramm eine Legende.
Mehr darüber, was jeder Schritt bedeutet, findest du im Knowledge-Base-Artikel [Zeiten in Wasserfall-Grafiken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="de" >}}) erläutert.

Ein Wasserfalldiagramm eines Transaktionsprüfobjekts zeigt die Metriken [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}) und [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}) für jede Navigation in einem Transaktionsschritt. Diese Metriken werden über dem Wasserfalldiagramm angezeigt. Enthält ein Schritt mehrere Navigationsaktionen, zeigt das Diagramm die Metriken für alle Navigationen mit einer vertikalen grünen Linie. Führe den Mauszeige über die Linie, um die genauen Messwerte aufzurufen.

Unter dem Wasserfalldiagramm siehst du eine Zusammenfassung aller Zeiten nach Anfragetyp.

## Zeitangaben

Um detailliertere oder Hintergrundinformationen zu den Messungen zum Seitenobjekt zu erhalten, kannst du mit der Maus über die Messwerte für ein Objekt fahren und ein kleines Pop-up mit den Details zu diesem speziellen Objekt erscheint.

![Screenshot Pop-up Wasserfallzeiten](/img/content/scr_waterfall_chart-popup-detail.min.png)


## Ansicht Request und Response

Für jedes einzelne Objekt im Wasserfall kannst du auf das **+** klicken, um eine Ansicht mit Request- und Response-Informationen zu öffnen. Dieser Bereich enthält Informationen über die Anfrage, die für den Abruf des Objekts gestellt wurde, und über die Antwort.

Du findest die folgenden Infos:
- die Request URL, Methode und das verwendete Protokoll
- einen Überblick über die Request Header, einschließlich der Abfrage
- die IP-Adresse des antwortenden Servers
- eine Information über die (nicht) komprimierte Größe des Objekts
    - **Netzwerk-Größe**: die tatsächliche Anzahl Bytes, die heruntergeladen wurden (komprimierte Größe)
    - **Ressourcen-Größe/nicht komprimierte Größe**: Größe des Objekts nach Entkomprimierung, sofern zutreffend
- alle Response Header, die mit der Antwort geliefert wurden

Verwendest du einen [Full Pagecheck mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}), enthalten die Bereiche Request/Response die entsprechenden **TLS Informationen** für das Objekt. Darüber hinaus können diese Wasserfall-Grafiken weitere Objektdetails anzeigen, so etwa, wenn die Abfrage gecacht, vorgeladen oder abgebrochen wird, und sie unterstützen Daten-URIs (wenn das HTML der Seite Inline-Bilddaten enthält). Diese zusätzlichen Informationen sind im Bereich Request/Response für einzelne Objekte verfügbar, sofern zutreffend.

![Request-/Response-Anzeige](/img/content/scr-fpc-waterfall-requestresponse-panel.min.png)

## Weitere Optionen, um detailliertere Informationen zu erhalten

Klicke auf die Spalten mit der Nummer des Seitenobjekts (#), dem Objektnamen (URL) und der Objektgröße (Größe), um das Wasserfalldiagramm nach den Werten in diesen Spalten zu sortieren.

Wenn die Seite viele Objekte enthält, kann es erforderlich sein, das Diagramm nach (einem Teil) des Objektnamens zu filtern. Verwende das Feld **Filter**, um den Begriff einzugeben, nach dem gefiltert werden soll.

## Die Wasserfall-Grafik exportieren

Die Wasserfall-Grafik kann als PDF-Datei exportiert werden. Die PDF-Dateien dienen beispielsweise als Sicherung deiner Wasserfalldaten. Ein PDF-Export ist auch praktisch, wenn du die Wasserfall-Grafik Dritten gegenüber veröffentlichen möchtest, ohne ihnen die Dashboards zu zeigen.

Klicke auf **Als PDF exportieren** oben rechts über dem Diagramm, um ein PDF deiner Wasserfall-Grafik zu erzeugen und zu speichern.
