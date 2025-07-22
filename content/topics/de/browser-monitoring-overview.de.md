{
  "hero": {
    "title": "Browser Monitoring"
  },
  "title": "Browser Monitoring",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/ueberblick-ueber-die-browser-ueberwachung",
  "summary": "Der Prüfobjekttyp Full Pagecheck ist der umfassendste Prüfobjekttyp. Jedes Element wird in einem Browser geladen. Der Bericht stellt die Ergebnisse in einem detaillierten Wasserfalldiagramm dar.",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
  "sectionlist": true
}

Uptrends‛ Browser-Prüfobjekte, auch bekannt als Full Pagecheck (FPC), gehören zu den verschiedenen [Prüfobjekttypen]({{< ref path="support/kb/basics/monitor-types" lang="de" >}}), die Uptrends bereitstellt. Das Prüfobjekt Full Pagecheck liefert detaillierte Performance-Daten über deine Webseite für jedes einzelne Seitenelement. Ein FPC-Prüfobjekt lädt deine Seite in einen echten Browser, einschließlich Skripten, CSS, Bildern, Fremdanbieterelementen und anderen Website-Komponenten. Diese Prüfobjekt lädt die Seite komplett in einem echten Browser, um die Ladezeit deiner Website genau zu erfassen – so wie sie deine Endnutzer erleben.

Der FPC präsentiert Monitoring-Daten in den Kontrolldetails des Prüfobjekts, einschließlich eines [Wasserfalldiagramms]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}). Abhängig von dem [Browsertyp]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="de" >}}), den du für das Prüfobjekt ausgewählt hast, siehst du noch weitere Informationen ([extra Metriken und Funktionen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}})).

Wenn du externe Inhalte auf deiner Website überwachen möchtest, solltest du den [erweiterten Full Pagecheck]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="de" >}}) nutzen.

## Ein FPC-Prüfobjekt einrichten {id="set-up-fpc"}

Das Einrichten eines FPC-Prüfobjekts beginnt mit der Erstellung des Prüfobjekts und der anschließenden Auswahl des Browsertyps sowie Überwachungsintervalls. Dann folgt die Definition der Fehlerbedingungen, Auswahl der Checkpoints und Eingabe spezieller Optionen wie Wartungszeiträume.

Mehr zu den Grundlagen findest du im Artikel [Prüfobjekttypen – Website-Performance-Prüfobjekte]({{< ref path="support/kb/basics/monitor-types#browser-monitors" lang="de" >}}).

## Browser-Prüfobjekte (Full Pagecheck (FPC))

Es stehen mehrere Browser-Prüfobjekttypen zur Auswahl:

- [Full Pagecheck (FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) – ein Prüfobjekttyp, der alle Seitenelemente beim Laden der Seite prüft und die Daten in einem umfassenden [Wasserfalldiagramm]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}) darstellt.

- [Erweiterter Full Pagecheck bzw. Full Pagecheck \+ (FPC+)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="de" >}}) – eine Option im Rahmen des FPC-Prüfobjekts, bei der alle Seitenelemente während des Ladens der Seite geprüft werden, auch die Inhalte von Fremdanbietern. Dieses Prüfobjekt zeigt deine Daten ebenfalls in einem umfassenden [Wasserfalldiagramm]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}).

Der Abschnitt [Full Pagecheck]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) beschreibt, wie du das Prüfobjekt einrichtest und die Einstellungen vornimmst.

Die Prüfobjekteinstellungen werden in mehreren Knowledge-Base-Artikeln beschrieben. Unten findest du eine Liste.

### Haupteinstellungen

Alle Optionen auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} des Prüfobjekts sind die grundlegenden Einstellungen für das FPC-Prüfobjekt.


- [Überwachungsintervall]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}})
- [Parallel-Monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="de" >}})
- [Prüfobjektmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}})
- [Browsertypen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="de" >}})
- [Prüfobjekt-Anmerkungen (optional)]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="de" >}})

### Fehlerbedingungen

Ein FPC-Prüfobjekt testet standardmäßig die Verfügbarkeit der angegebenen Server-URL. Andere Prüfungen müssen im Prüfobjekt auf der Registerkarte {{< AppElement type="tab" >}} Fehlerbedingungen {{< /AppElement >}} festgelegt werden.

Der Knowledge-Base-Artikel [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) erläutert, wie Fehlerbedingungen funktionieren.

Insbesondere gibt es eine Tabelle dazu, [welche Fehlerbedingungen verfügbar sind ]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="de" >}}), sodass du einen Überblick über die Fehlerbedingungen beim Full Pagecheck hast.

### Prüfobjektberechtigungen

Mit Uptrends‘ [Berechtigungssystem]({{< ref path="support/kb/account/permissions" lang="de" >}}) lässt sich definieren, welche Teams oder Mitarbeiter auf welche Elemente Zugriff haben. Es gibt unterschiedliche Berechtigungen für Erstellung/Löschung, Anzeige und Bearbeitung.

- [Prüfobjektberechtigungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}})

### Weitere Prüfobjekteinstellungen

Die folgenden Einstellungen sind optional; das Prüfobjekt würde ohne diese Einstellungen funktionieren. Aber um das Monitoring-Potenzial voll auszuschöpfen und um es an deine Gegebenheiten anzupassen, sollten die folgenden Einstellungen konfiguriert werden.

- [Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/checkpoint-information" lang="de" >}})
- [Wartungszeiträume]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="de" >}})
- [Prüfobjektgruppen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="de" >}})


## Prüfobjektdaten und Berichte

Sobald dein Prüfobjekt eingerichtet und aktiviert ist (überwacht), sammelst du Daten zur Performance. Für jede Prüfung werden eine Anzahl Messungen erfasst und gespeichert. Diese Daten werden in den Kontrolldetails des Prüfobjekts angezeigt. Öffne die Kontrolldetails über {{< AppElement type="menuitem" >}}Überwachung > Prüfobjektprotokoll {{< /AppElement >}} und klicke auf die Listeneinträge.

### Kontrolldetails des Prüfobjekts

Die Kontrolldetails zeigen die [grundlegenden Ladezeitmetriken]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="de" >}}) (*Auflösung*, *Verbindung*, *Download* und *Gesamtzeit*). Deine FPC-Ergebnisse enthalten auch ein detailliertes [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}).

 Die Wasserfallgrafik ist eine visuelle Repräsentation der Seitenladezeiten für jedes einzelne geladene Objekt. Sie enthält Informationen wie IP-Adresse der Seitenquelle, alle Request und Response Header, die Objektgröße und einen detaillierten Überblick der [Ladezeiten für einzelne Objekte]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="de" >}}).

### Extra Metriken und Funktionen {id="chrome-extra-metrics"}

Für die [Browsertypen mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types#chrome-extra-metrics" lang="de" >}}) erhältst du sogar noch mehr Daten, so zum Beispiel [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}), [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}), [Timeline Screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="de" >}}) und die Option, einen [DNS Bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="de" >}}) zu nutzen.

Die vollständige Bandbreite zusätzlicher Daten und Funktionen wird im Knowledge-Base-Artikel
[Extra Metriken und Funktionen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) erläutert.

## Credits

Browser-Prüfobjekte verwenden Browser-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="de" >}}).