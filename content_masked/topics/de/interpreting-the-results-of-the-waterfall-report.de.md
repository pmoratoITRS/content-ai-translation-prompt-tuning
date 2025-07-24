{
  "hero": {
    "title": "Interpretation der Ergebnisse des Wasserfallberichts"
  },
  "title": "Interpretation der Ergebnisse des Wasserfallberichts",
  "summary": "Sie haben den Wasserfallbericht vor sich: Wie erklären Ihnen, wie Sie die Ergebnisse des Monitorings interpretieren.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/interpretation-der-ergebnisse-des-wasserfallberichts",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Sobald Sie den Wasserfallbericht (siehe [Aufrufen des Wasserfallberichts]([LINK_URL_1])) aufgerufen haben, erhalten Sie eine Fülle von Daten über Ihre Seite und deren Elemente. Jedes Seitenelement erfordert eine Anfrage, eine TCP-Verbindung, einen HTTPS Handshake, eine Sende- und Warte-Zeit sowie eine Empfangs-Zeit. Sobald der Receive-Vorgang abgeschlossen ist, verarbeitet der Browser das Element. Eine einzelne Seite kann über hundert und mehr Elemente verfügen, die der Browser verarbeiten muss. Die Gesamtzeit dieser Elemente oder selbst nur einige langsame Elemente können verursachen, dass die Seite Ihre Höchstladezeit überschreitet. Wie Sie an dem folgenden Beispiel sehen, wurde bei diesem Full Page Check die Gesamtzeit von 2,5 Sekunden überschritten.

Der Berichtskopf liefert allgemeine Informationen über die Prüfung, darunter der verwendete Checkpoint, die URL und der im Test verwendete Browser. Sie sehen, dass der Punkt **Ergebnis** den besonderen Grund für die Fehlermeldung angibt. Dieser Test ergab eine Fehlermeldung mit dem Fehlercode 6000, da die Höchstladezeit überschritten wurde. Weitere Erläuterungen zu möglichen Fehlercodes finden Sie auf der Seite [Fehlertypen]([LINK_URL_2]).

![]([LINK_URL_3])

## Was genau hat also den Fehler verursacht?

Wenn Sie die Seite herunter scrollen, erhalten Sie eine Liste der Seitenelemente. Der Bericht listet die Seitenelemente in der Reihenfolge auf, in der sie im Browser geladen werden. Einige Teile werden nicht synchron geladen, andere Elemente sind abhängig und laden nicht, wenn nicht die jeweiligen anderen Elemente der Seite vollständig geladen sind. Rechts von jedem Element sehen Sie eine Balkengrafik. Jede Farbe im Balkendiagramm stellt einen anderen Verbindungsstatus dar. Indem die Elemente über einen Zeitstrahl positioniert werden, werden sie in einer Wasserfallansicht dargestellt. Die Farbbänder zeigen die Dauer an, die jedes Element zum Laden benötigte. Ein kurzer Blick auf den Bericht zeigt Ihnen schnell die Seitenelemente, die am längsten gebraucht haben, bis der Browser sie erhalten hatte.

In diesem Beispielbericht benötigten mehrere der Handshakes (goldfarbig angezeigt) zu lang, um vollständig zu laden. Die Elemente mit überlangen Handshake- und Warte-Zeiten umfassen eine Drittanbieter-Analyseanwendung und eine langsame Anfrage nach einer JavaScript-Datei. Obwohl diese Dateien am längsten zum Laden benötigten, werden Sie nach einem weiteren Blick auf den Wasserfallbericht sehen, dass andere Elemente mit kürzeren Handshake- und Warte-Zeiten eine kumulative Auswirkung auf die Gesamtzeit haben können.

![]([LINK_URL_4])

## Anzeige der Anfrage- und Antwort-Header

Ihre Anfrage- und Antwort-Header erzählen Ihnen die ganze Geschichte. Die Anzeige der Anfrage- und Antwort-Header gibt Ihnen Einblick, wonach der Browser gefragt hat und wie das Ergebnis dieser Anfrage aussieht. Um die Anfrage- und Antwort-Header für ein Element aufzurufen, klicken Sie auf das "\+"-Symbol rechts des Elementnamens in der Liste. Im folgenden Beispiel hat der Browser eine JavaScript-Datei aufgerufen, aber die Anfrage führte zu einer längeren Verzögerung beim Handshake und bei der Antwortzeit.

![]([LINK_URL_5])

## Berichtszusammenfassung

Am Ende des Wasserfallberichts können Sie eine Berichtszusammenfassung sehen. Die erste Spalte enthält die Farblegende für die Farbbalken im Wasserfallteil des Berichts. Rechts sehen Sie die Gesamtzeit und die durchschnittliche Zeit für jeden Verbindungsstatus. Des Weiteren liefert die Zusammenfassung Zahlen zu Elementtypen und Seitengesamtzahl.

![]([LINK_URL_6])

## Finden Sie die Elementquelle anhand von Domaingruppen

 

Wenn Ihr Prüfobjekt ein FPC\+-Prüfobjekt ist, können Sie schnell die Quelle des problematischen Elements erkennen.

1.  Merken Sie sich die Elementnummer des Elements aus dem Wasserfallbericht, das Sie untersuchen möchten.
2.  Klicken Sie auf die Schaltfläche Domaingruppen oben rechts vom Wasserfall.  
      
    ![]([LINK_URL_7])  
      
3.  Suchen Sie nach der Elementnummer in der Liste, um die Domaingruppen zu erfahren.    
    ![]([LINK_URL_8])
