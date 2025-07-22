{
  "hero": {
    "title": "Kontrolldetails"
  },
  "title": "Kontrolldetails",
  "summary": "Die Ergebnisse der Prüfung werden in den Kontrolldetails des Prüfobjekts präsentiert. Die verfügbaren Daten hängen vom Prüfobjekttyp ab.",
  "url": "/support/kb/synthetic-monitoring/monitoring-ergebnisse/kontrolldetails",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/check-details"
}

Die von einer Prüfung durch ein Prüfobjekt erfassten Daten werden als sogenannte „Kontrolldetails“ angezeigt. Sie bestehen aus den grundlegenden Informationen: ob der Check erfolgreich abgeschlossen wurde (OK) oder ob ein Fehler entdeckt wurde (basierend auf deinen [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}})). Detaillierte Informationen zur Prüfung selbst und zum Ergebnis werden ebenfalls angezeigt und können bei der Fehlerbehebung hilfreich sein.

## Was ist in den Kontrolldetails enthalten?

Die Informationen in den Kontrolldetails hängen vom Prüfobjekttyp ab. Es kann sich dabei um einen einfachen Statuscode für ein HTTP(S)-Prüfobjekt handeln. Komplexere Prüfobjekte enthalten möglicherweise Screenshots bei einem Full Pagecheck oder Ergebnisse für jeden Schritt einer Transaktion oder eines Multi-step API-Prüfobjekts – wie die beiden Beispiele unten.

Kontrolldetails („OK“) bei einem HTTPS-Prüfobjekt:

![Screenshot Kontrolldetails HTTPS-Prüfobjekt](/img/content/scr_check-details-https-monitor.min.png)

Kontrolldetails bei einem Transaktionsprüfobjekt, bei dem ein Fehler ausgegeben wurde:

![Screenshot Kontrolldetails Transaktionsprüfobjekt](/img/content/scr_check-details-transaction-monitor-041024.min.png)

## Wo sind die Kontrolldetails zu finden?

Die Kontrolldetails sind an mehreren Orten verfügbar.

Wenn du eine Prüfung über die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} ausführst, erhältst du ein Pop-up-Fenster mit den Kontrolldetails.

Mehrere Dashboards zeigen eine Liste von Prüfungen. Ein Klick auf einen einzelnen Fehler oder eine Prüfung zeigt die Kontrolldetails. Du findest die Fehler oder Prüfungen hier:

- Dashboard unter {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Fehler Übersicht {{< /AppElement >}}
- Dashboard unter {{< AppElement type="menuitem" >}} Überwachung > Prüfobjektstatus {{< /AppElement >}}
- Dashboard unter {{< AppElement type="menuitem" >}} Überwachung > Prüfobjektprotokoll {{< /AppElement >}}
- Die Kachel *Letzte Überwachungen*, eine [benutzerdefinierte Berichtskachel]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#last-check-details" lang="de" >}}), die du zu deinen [benutzerdefinierten Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-dashboards" lang="de" >}}) hinzufügen kannst
