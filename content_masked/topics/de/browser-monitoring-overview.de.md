{
  "hero": {
    "title": "Browser Monitoring"
  },
  "title": "Browser Monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/browser-monitoring/ueberblick-ueber-die-browser-ueberwachung",
  "summary": "Der Prüfobjekttyp Full Pagecheck ist der umfassendste Prüfobjekttyp. Jedes Element wird in einem Browser geladen. Der Bericht stellt die Ergebnisse in einem detaillierten Wasserfalldiagramm dar.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Uptrends‛ Browser-Prüfobjekte, auch bekannt als Full Pagecheck (FPC), gehören zu den verschiedenen [Prüfobjekttypen]([LINK_URL_1]), die Uptrends bereitstellt. Das Prüfobjekt Full Pagecheck liefert detaillierte Performance-Daten über deine Webseite für jedes einzelne Seitenelement. Ein FPC-Prüfobjekt lädt deine Seite in einen echten Browser, einschließlich Skripten, CSS, Bildern, Fremdanbieterelementen und anderen Website-Komponenten. Diese Prüfobjekt lädt die Seite komplett in einem echten Browser, um die Ladezeit deiner Website genau zu erfassen – so wie sie deine Endnutzer erleben.

Der FPC präsentiert Monitoring-Daten in den Kontrolldetails des Prüfobjekts, einschließlich eines [Wasserfalldiagramms]([LINK_URL_2]). Abhängig von dem [Browsertyp]([LINK_URL_3]), den du für das Prüfobjekt ausgewählt hast, siehst du noch weitere Informationen ([extra Metriken und Funktionen]([LINK_URL_4])).

Wenn du externe Inhalte auf deiner Website überwachen möchtest, solltest du den [erweiterten Full Pagecheck]([LINK_URL_5]) nutzen.

## Ein FPC-Prüfobjekt einrichten [ANCHOR_1]

Das Einrichten eines FPC-Prüfobjekts beginnt mit der Erstellung des Prüfobjekts und der anschließenden Auswahl des Browsertyps sowie Überwachungsintervalls. Dann folgt die Definition der Fehlerbedingungen, Auswahl der Checkpoints und Eingabe spezieller Optionen wie Wartungszeiträume.

Mehr zu den Grundlagen findest du im Artikel [Prüfobjekttypen – Website-Performance-Prüfobjekte]([LINK_URL_6]).

## Browser-Prüfobjekte (Full Pagecheck (FPC))

Es stehen mehrere Browser-Prüfobjekttypen zur Auswahl:

- [Full Pagecheck (FPC)]([LINK_URL_7]) – ein Prüfobjekttyp, der alle Seitenelemente beim Laden der Seite prüft und die Daten in einem umfassenden [Wasserfalldiagramm]([LINK_URL_8]) darstellt.

- [Erweiterter Full Pagecheck bzw. Full Pagecheck \+ (FPC+)]([LINK_URL_9]) – eine Option im Rahmen des FPC-Prüfobjekts, bei der alle Seitenelemente während des Ladens der Seite geprüft werden, auch die Inhalte von Fremdanbietern. Dieses Prüfobjekt zeigt deine Daten ebenfalls in einem umfassenden [Wasserfalldiagramm]([LINK_URL_10]).

Der Abschnitt [Full Pagecheck]([LINK_URL_11]) beschreibt, wie du das Prüfobjekt einrichtest und die Einstellungen vornimmst.

Die Prüfobjekteinstellungen werden in mehreren Knowledge-Base-Artikeln beschrieben. Unten findest du eine Liste.

### Haupteinstellungen

Alle Optionen auf der Registerkarte [SHORTCODE_1] Allgemein [SHORTCODE_2] des Prüfobjekts sind die grundlegenden Einstellungen für das FPC-Prüfobjekt.


- [Überwachungsintervall]([LINK_URL_12])
- [Parallel-Monitoring]([LINK_URL_13])
- [Prüfobjektmodus]([LINK_URL_14])
- [Browsertypen]([LINK_URL_15])
- [Prüfobjekt-Anmerkungen (optional)]([LINK_URL_16])

### Fehlerbedingungen

Ein FPC-Prüfobjekt testet standardmäßig die Verfügbarkeit der angegebenen Server-URL. Andere Prüfungen müssen im Prüfobjekt auf der Registerkarte [SHORTCODE_3] Fehlerbedingungen [SHORTCODE_4] festgelegt werden.

Der Knowledge-Base-Artikel [Fehlerbedingungen]([LINK_URL_17]) erläutert, wie Fehlerbedingungen funktionieren.

Insbesondere gibt es eine Tabelle dazu, [welche Fehlerbedingungen verfügbar sind ]([LINK_URL_18]), sodass du einen Überblick über die Fehlerbedingungen beim Full Pagecheck hast.

### Prüfobjektberechtigungen

Mit Uptrends‘ [Berechtigungssystem]([LINK_URL_19]) lässt sich definieren, welche Teams oder Mitarbeiter auf welche Elemente Zugriff haben. Es gibt unterschiedliche Berechtigungen für Erstellung/Löschung, Anzeige und Bearbeitung.

- [Prüfobjektberechtigungen]([LINK_URL_20])

### Weitere Prüfobjekteinstellungen

Die folgenden Einstellungen sind optional; das Prüfobjekt würde ohne diese Einstellungen funktionieren. Aber um das Monitoring-Potenzial voll auszuschöpfen und um es an deine Gegebenheiten anzupassen, sollten die folgenden Einstellungen konfiguriert werden.

- [Checkpoints]([LINK_URL_21])
- [Wartungszeiträume]([LINK_URL_22])
- [Prüfobjektgruppen]([LINK_URL_23])


## Prüfobjektdaten und Berichte

Sobald dein Prüfobjekt eingerichtet und aktiviert ist (überwacht), sammelst du Daten zur Performance. Für jede Prüfung werden eine Anzahl Messungen erfasst und gespeichert. Diese Daten werden in den Kontrolldetails des Prüfobjekts angezeigt. Öffne die Kontrolldetails über [SHORTCODE_5]Überwachung > Prüfobjektprotokoll [SHORTCODE_6] und klicke auf die Listeneinträge.

### Kontrolldetails des Prüfobjekts

Die Kontrolldetails zeigen die [grundlegenden Ladezeitmetriken]([LINK_URL_24]) (*Auflösung*, *Verbindung*, *Download* und *Gesamtzeit*). Deine FPC-Ergebnisse enthalten auch ein detailliertes [Wasserfalldiagramm]([LINK_URL_25]).

 Die Wasserfallgrafik ist eine visuelle Repräsentation der Seitenladezeiten für jedes einzelne geladene Objekt. Sie enthält Informationen wie IP-Adresse der Seitenquelle, alle Request und Response Header, die Objektgröße und einen detaillierten Überblick der [Ladezeiten für einzelne Objekte]([LINK_URL_26]).

### Extra Metriken und Funktionen [ANCHOR_2]

Für die [Browsertypen mit extra Metriken]([LINK_URL_27]) erhältst du sogar noch mehr Daten, so zum Beispiel [W3C Navigation Timings]([LINK_URL_28]), [Core Web Vitals]([LINK_URL_29]), [Timeline Screenshots]([LINK_URL_30]) und die Option, einen [DNS Bypass]([LINK_URL_31]) zu nutzen.

Die vollständige Bandbreite zusätzlicher Daten und Funktionen wird im Knowledge-Base-Artikel
[Extra Metriken und Funktionen]([LINK_URL_32]) erläutert.

## Credits

Browser-Prüfobjekte verwenden Browser-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]([LINK_URL_33]).