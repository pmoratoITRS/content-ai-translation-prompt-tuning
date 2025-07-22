{
  "hero": {
    "title": "Kontrolldetails"
  },
  "title": "Kontrolldetails",
  "summary": "Die Ergebnisse der Prüfung werden in den Kontrolldetails des Prüfobjekts präsentiert. Die verfügbaren Daten hängen vom Prüfobjekttyp ab.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/kontrolldetails",
  "translationKey": "[URL_1]
}

Die von einer Prüfung durch ein Prüfobjekt erfassten Daten werden als sogenannte „Kontrolldetails“ angezeigt. Sie bestehen aus den grundlegenden Informationen: ob der Check erfolgreich abgeschlossen wurde (OK) oder ob ein Fehler entdeckt wurde (basierend auf deinen [Fehlerbedingungen]([LINK_URL_1])). Detaillierte Informationen zur Prüfung selbst und zum Ergebnis werden ebenfalls angezeigt und können bei der Fehlerbehebung hilfreich sein.

## Was ist in den Kontrolldetails enthalten?

Die Informationen in den Kontrolldetails hängen vom Prüfobjekttyp ab. Es kann sich dabei um einen einfachen Statuscode für ein HTTP(S)-Prüfobjekt handeln. Komplexere Prüfobjekte enthalten möglicherweise Screenshots bei einem Full Pagecheck oder Ergebnisse für jeden Schritt einer Transaktion oder eines Multi-step API-Prüfobjekts – wie die beiden Beispiele unten.

Kontrolldetails („OK“) bei einem HTTPS-Prüfobjekt:

![Screenshot Kontrolldetails HTTPS-Prüfobjekt]([LINK_URL_2])

Kontrolldetails bei einem Transaktionsprüfobjekt, bei dem ein Fehler ausgegeben wurde:

![Screenshot Kontrolldetails Transaktionsprüfobjekt]([LINK_URL_3])

## Wo sind die Kontrolldetails zu finden?

Die Kontrolldetails sind an mehreren Orten verfügbar.

Wenn du eine Prüfung über die Schaltfläche [SHORTCODE_1] Jetzt testen [SHORTCODE_2] ausführst, erhältst du ein Pop-up-Fenster mit den Kontrolldetails.

Mehrere Dashboards zeigen eine Liste von Prüfungen. Ein Klick auf einen einzelnen Fehler oder eine Prüfung zeigt die Kontrolldetails. Du findest die Fehler oder Prüfungen hier:

- Dashboard unter [SHORTCODE_3] Dashboards > Synthetics > Fehler Übersicht [SHORTCODE_4]
- Dashboard unter [SHORTCODE_5] Überwachung > Prüfobjektstatus [SHORTCODE_6]
- Dashboard unter [SHORTCODE_7] Überwachung > Prüfobjektprotokoll [SHORTCODE_8]
- Die Kachel *Letzte Überwachungen*, eine [benutzerdefinierte Berichtskachel]([LINK_URL_4]), die du zu deinen [benutzerdefinierten Dashboards]([LINK_URL_5]) hinzufügen kannst
