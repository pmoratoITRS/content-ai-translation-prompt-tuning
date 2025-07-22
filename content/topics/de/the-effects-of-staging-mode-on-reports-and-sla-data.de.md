{
  "hero": {
    "title": "Die Auswirkung des Staging-Modus auf Berichte und SLA-Daten"
  },
  "title": "Die Auswirkung des Staging-Modus auf Berichte und SLA-Daten",
  "summary": "When a monitor runs in Staging mode the data it generates affects your reporting in different ways.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/die-auswirkung-des-staging-modus-auf-berichte-und-sla-daten",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/the-effects-of-staging-mode-on-reports-and-sla-data"
}

Der Staging-Modus, wie wir im Artikel [Prüfobjektmodi](/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/pruefobjektmodi) erläutert haben, ist eine großartige Möglichkeit, deine Prüfobjekte zu testen, ohne die Daten zu Verfügbarkeit und SLA zu beeinflussen. Im Staging-Modus werden auch keine Warnmeldungen versendet. Die Prüfobjekte erfassen Messungen und funktionieren wie jedes andere Prüfobjekt im Produktionsmodus, aber du musst dir keine Sorge machen, dass sie die Berichte verzerren. Sehen wir uns an, wie Prüfobjekte im Staging-Modus in deinen Berichten erscheinen.

## Wie wirkt sich der Staging-Modus auf die Verfügbarkeits- und Fehler-Dashboards aus?

Wenn du eine Option aus dem Dashboard-Menü **Verfügbarkeit & Fehler** wählst, wirst du Daten deiner Prüfobjekte im Staging-Modus sehen, aber:

-   Daten, die von Prüfobjekten im Staging-Modus erfasst werden, tragen nicht zu den Berichten zu Ausfallzeiten, Check-Zahl und Fehlerzahl bei und
-   wie bei einem deaktivierten Prüfobjekt ist die berichtete Verfügbarkeit immer 100 % für die Zeit, in der das Prüfobjekt im Staging-Modus ist.

## Wie wirkt sich der Staging-Modus auf die Performance-Dashboards aus?

Wenn du eine Option aus dem Dashboard-Menü **Performance** wählst, wirst du sehen, dass Uptrends die Messungen verzeichnet für:

-   Auflösung
-   Connect
-   Download und
-   Gesamtzeit

## Wie wirkt sich der Staging-Modus auf das Prüfobjektprotokoll aus?

Die Checkergebnisse deiner Prüfobjekte im Staging-Modus werden in deinem **Prüfobjektprotokoll** erfasst. Uptrends kennzeichnet die Checks, die im Staging-Modus erfasst werden, mit einem Glaskolben-Symbol. 

## Wie wirkt sich der Staging-Modus auf SLA-Berichte aus?

In deinen SLA-Berichten zeigt Uptrends ein Prüfobjekt im Staging-Modus auf dieselbe Weise, wie es ein deaktiviertes Prüfobjekt mit 100 % Verfügbarkeit sowie keine bestätigten Fehler und Ausfallzeiten darstellt. Die SLA-Berichte enthalten keine Fehler oder Ausfälle, die von einem Prüfobjekt im Staging-Modus verzeichnet werden.
