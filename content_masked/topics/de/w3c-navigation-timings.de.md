{
  "hero": {
    "title": "W3C Navigation Timings"
  },
  "title": "W3C Navigation Timings",
  "summary": "Beschreibung der W3C Navigation Timing-Messwerte, wie sie im Full Pagecheck- oder Transaktions-Monitoring-Wasserfallbericht angezeigt werden",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/w3c-navigation-timings",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Das **World Wide Web Consortium** (oder kurz W3C) ist eine internationale Organisation, die sich mit der Entwicklung von Normen für das World Wide Web befasst. Als solche hat sie einen Standard für Browser und Webanwendungen definiert, um Zeitmessungen zum Laden von Webseiten durchzuführen und anzuzeigen. Die vollständige Spezifikation des Standards findest du auf der [W3C-Website (Copyright © 2012, World Wide Web Consortium)]([LINK_URL_1]).

Uptrends‘ Prüfobjekttypen [Full Pagecheck (FPC)]([LINK_URL_2]) und [Transaktionen]([LINK_URL_3]) bieten die Möglichkeit, eine Auswahl an Messwerten zu W3C Navigation Timings (sowie zusätzliche Informationen wie die [Core Web Vitals]([LINK_URL_4])) anzuzeigen. Dieser Artikel gibt einen Überblick der dargestellten Messwerte und was sie genau bedeuten.

Zur Illustration zeigt die folgende Abbildung alle vom W3C definierten Navigation-Timing-Ereignisse auf einem Zeitstrahl.

![W3C Navigation Timings]([LINK_URL_5])
(Copyright © 2012, [World Wide Web Consortium]([LINK_URL_6]))

## Messwerte

Dies ist ein Überblick der Messwerte zu W3C Navigation Timings, die du beim Full Pagecheck und Transaktionsprüfobjekt von Uptrends erhältst.

![W3C Navigation Timings in Uptrends]([LINK_URL_7])

- **Request Start**: Gleich dem [INLINE_CODE_1] wie vom W3C definiert. Ein Zeitstempel, der angibt, wann der Browser die Ressource vom Webserver nach dem DNS-Lookup und der TCP-Verbindung anfragt.
- **Time to First Byte**: Gleich der Differenz von [INLINE_CODE_2] und [INLINE_CODE_3] wie vom W3C definiert. Kurz gesagt, die Zeit zwischen der ersten Anfrage vom Browser zum Server und dem Empfang des ersten Bytes der folgenden Antwort im Browser. (Das umfasst alle Weiterleitungen und SSL/TCP-Verbindungen.)
- **DOM Interactive**: Gleich dem [INLINE_CODE_4] wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann die Dokumentenbereitschaft auf „interaktiv“ gesetzt wurde, der Browser das Parsing der Seite gestoppt hat und der Nutzer mit ihr interagieren kann. Ressourcen wie Skripte, Bilder, Stylesheets oder Frames sind eventuell noch nicht vollständig geladen.
- **DOM Completed**: Gleich dem [INLINE_CODE_5] wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann das Parsing des Hauptdokuments erfolgt ist, das DOM vollständig geladen wurde und die Seitenbereitschaft auf „abgeschlossen“ gesetzt wurde.
- **Load Event**: Gleich dem [INLINE_CODE_6] wie vom W3C definiert. Ein Zeitstempel, der anzeigt, wann das Ladeereignis des aktuellen Dokuments abgeschlossen wurde, einschließlich aller zugehörigen Ressourcen wie Stylesheets und Bilder.

## Dashboard-Berichte

Du kannst alle Metriken in einem benutzerdefinierten Dashboard anzeigen. Füge einfach eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]([LINK_URL_8]) hinzu. Klicke dann auf die Schaltfläche für die Kacheleinstellungen [SHORTCODE_1] [SHORTCODE_2] an der Kachel und wähle die gewünschten Werte durch Markieren der Kontrollkästchen.

Du kannst die W3C Navigation Timings von Transaktionen für jeden einzelnen Schritt anzeigen. Dazu musst du die Optionen *Wasserfall Grafik* und *Leistungsmetriken* für jeden Schritt aktivieren, den du in der Grafik sehen möchtest. Weitere Information hierzu findest du unter [Schritt-Einstellungen]([LINK_URL_9]).

![Screenshot Detail der Kacheleinstellungen]([LINK_URL_10])
