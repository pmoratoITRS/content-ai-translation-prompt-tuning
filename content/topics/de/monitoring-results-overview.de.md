{
  "hero": {
    "title": "Überblick über die Überwachungsergebnisse"
  },
  "title": "Überblick über die Überwachungsergebnisse",
  "url": "/support/kb/synthetic-monitoring/monitoring-ergebnisse/uberblick-uber-die-uberwachungsergebnisse",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/monitoring-results-overview",
  "sectionlist": false
}

Bei der Ausführung von Prüfobjekten gibt es unterschiedliche Ergebnisarten oder Berichte, abhängig vom Prüfobjekttyp und deinen Einstellungen. Die [Kontrolldetails]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="de" >}}) enthalten viele Werte, und es gibt sie für alle Prüfobjekte. Einige Ergebnisse gelten eventuell nur für einige Prüfobjekttypen, zum Beispiel gibt es die Wasserfall-Grafik für den Full Pagecheck wie auch für Transaktionsprüfobjekte, aber nicht für andere Prüfobjekttypen.

## Messwerte

Mit den **Core Web Vitals** und **W3C Navigation Timings** verfügst du über zwei Sets von Metriken, die auf internationalen Standards beruhen. Mit diesen Metriken kannst du die Performance deiner Website besser deuten und herausfinden, was verbessert werden muss, um eine höhere Position in den Rankings von Suchmaschinen zu erzielen.

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}})
- [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}})

Beachte, dass du diese Metriken in einem benutzerdefinierten Dashboard anzeigen kannst, indem du eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="de" >}}) hinzufügst.

## Wasserfallberichte

Die Wasserfall-Grafik ist eine Visualisierung der Monitoring-Ergebnisse in einem Balkendiagramm und zeigt im Detail, wann Seitenobjekte geladen wurden und wie lange es dauerte. Es ist ein gutes Tool für die Fehlerbehebung und um herauszufinden, was das Laden der Seite verzögert hat. Diese Knowledge-Base-Artikel halten weitere Infos zu Wasserfällen bereit:

- [Die Wasserfall-Grafik]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}})
- [Die Zeiten in Wasserfall-Grafiken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="de" >}})
- [Interpretation der Ergebnisse des Wasserfallberichts]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="de" >}})

## Weitere Problembehebung

Die Ergebnisse der Prüfung werden in den Kontrolldetails des Prüfobjekts gesammelt. Sie können als Startpunkt für eine Fehlerbehebung dienen.

- [Kontrolldetails]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="de" >}})

Darüber hinaus enthalten die Prüfergebnisse die Seitenquelle (HTML-Quelle) und das Konsolenprotokoll (vom Laden der Seite). Diese Daten sind bei den Prüfergebnissen von Transaktions- und Full Pagecheck-Prüfobjekten verfügbar. Du musst die Funktion eventuell aktivieren. Weitere Informationen findest du im Knowledge-Base-Artikel.

- [Seitenquelle und Konsolenprotokoll]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="de" >}})

Die Wasserfall-Grafik bietet gute Einblicke in das Laden deiner Seitenobjekte. Es kann jedoch schwerfallen, sich vorzustellen, was sich in den einzelnen Schritten ereignet. Der Zeitstrahl mit Screenshots zeigt dir, wie die Seite in unterschiedlichen Schritten während des Ladevorgangs aussieht.

- [Der Zeitstrahl mit Screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="de" >}})
