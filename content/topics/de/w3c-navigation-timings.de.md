{
  "hero": {
    "title": "W3C Navigation Timings"
  },
  "title": "W3C Navigation Timings",
  "summary": "Beschreibung der W3C Navigation Timing-Messwerte, wie sie im Full Pagecheck- oder Transaktions-Monitoring-Wasserfallbericht angezeigt werden",
  "url": "/support/kb/synthetic-monitoring/monitoring-ergebnisse/w3c-navigation-timings",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/w3c-navigation-timings"
}



Das **World Wide Web Consortium** (oder kurz W3C) ist eine internationale Organisation, die sich mit der Entwicklung von Normen für das World Wide Web befasst. Als solche hat sie einen Standard für Browser und Webanwendungen definiert, um Zeitmessungen zum Laden von Webseiten durchzuführen und anzuzeigen. Die vollständige Spezifikation des Standards findest du auf der [W3C-Website (Copyright © 2012, World Wide Web Consortium)](https://www.w3.org/TR/navigation-timing/).

Uptrends‘ Prüfobjekttypen [Full Pagecheck (FPC)](/support/kb/synthetic-monitoring/browser-monitoring) und [Transaktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="de" >}}) bieten die Möglichkeit, eine Auswahl an Messwerten zu W3C Navigation Timings (sowie zusätzliche Informationen wie die [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}})) anzuzeigen. Dieser Artikel gibt einen Überblick der dargestellten Messwerte und was sie genau bedeuten.

Zur Illustration zeigt die folgende Abbildung alle vom W3C definierten Navigation-Timing-Ereignisse auf einem Zeitstrahl.

![W3C Navigation Timings](/img/content/img-w3c-nav-timings.min.png)
(Copyright © 2012, [World Wide Web Consortium](https://www.w3.org))

## Messwerte

Dies ist ein Überblick der Messwerte zu W3C Navigation Timings, die du beim Full Pagecheck und Transaktionsprüfobjekt von Uptrends erhältst.

![W3C Navigation Timings in Uptrends](/img/content/scr-new-w3c-timings.png)

- **Request Start**: Gleich dem `requestStart` wie vom W3C definiert. Ein Zeitstempel, der angibt, wann der Browser die Ressource vom Webserver nach dem DNS-Lookup und der TCP-Verbindung anfragt.
- **Time to First Byte**: Gleich der Differenz von `navigationStart` und `responseStart` wie vom W3C definiert. Kurz gesagt, die Zeit zwischen der ersten Anfrage vom Browser zum Server und dem Empfang des ersten Bytes der folgenden Antwort im Browser. (Das umfasst alle Weiterleitungen und SSL/TCP-Verbindungen.)
- **DOM Interactive**: Gleich dem `domInteractive` wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann die Dokumentenbereitschaft auf „interaktiv“ gesetzt wurde, der Browser das Parsing der Seite gestoppt hat und der Nutzer mit ihr interagieren kann. Ressourcen wie Skripte, Bilder, Stylesheets oder Frames sind eventuell noch nicht vollständig geladen.
- **DOM Completed**: Gleich dem `domComplete` wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann das Parsing des Hauptdokuments erfolgt ist, das DOM vollständig geladen wurde und die Seitenbereitschaft auf „abgeschlossen“ gesetzt wurde.
- **Load Event**: Gleich dem `loadEventEnd` wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann das Ladeereignis des aktuellen Dokuments abgeschlossen wurde, einschließlich aller zugehörigen Ressourcen wie Stylesheets und Bilder.

## Dashboard-Berichte

Du kannst alle Metriken in einem benutzerdefinierten Dashboard anzeigen. Füge einfach eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="de" >}}) hinzu. Klicke dann auf die Schaltfläche für die Kacheleinstellungen {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} an der Kachel und wähle die gewünschten Werte durch Markieren der Kontrollkästchen.

Du kannst die W3C Navigation Timings von Transaktionen für jeden einzelnen Schritt anzeigen. Dazu musst du die Optionen *Wasserfall Grafik* und *Leistungsmetriken* für jeden Schritt aktivieren, den du in der Grafik sehen möchtest. Weitere Information hierzu findest du unter [Schritt-Einstellungen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="de" >}}).

![Screenshot Detail der Kacheleinstellungen](/img/content/scr_simple-data-metrics.min.png)
