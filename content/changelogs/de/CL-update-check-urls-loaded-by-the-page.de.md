{
  "title": "Zusätzliche Bedingungen zur Prüfung von URLs, die von der Seite geladen werden",
  "date": "2025-02-19",
  "url": "/changelog/februar-2025-zusaetzliche-bedingungen-von-der-seite-geladene-urls-ueberpruefen-fehlerbedingungen",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition"
}

[Von der Seite geladene URLs überprüfen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="de" >}}) ist eine Fehlerbedingung, die prüft, ob bestimmte Seitenobjekte von deiner Website geladen werden. Diese Seitenobjekte sind die URLs, die in deinem [Wasserfalldiagramm]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}) angezeigt werden, darunter für Bilder, Dateien und andere Website-Ressourcen.

Diese Fehlerbedingung ermöglicht nun, gesonderte Kriterien zur Überprüfung der Messwerte für jedes Seitenobjekt festzulegen. Durch Klicken der neuen Schaltfläche {{< AppElement type="editbutton" >}} +Zusätzliche Bedingung hinzufügen{{< /AppElement >}} kannst du nun die Antwortgröße des Seitenobjekts in Bytes (B), die Gesamtzeit in Millisekunden (ms) und den Statuscode angeben:

![Zusätzliche Bedingungen für von der Seite geladene URLs überprüfen](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

Möchtest du eine Fehlermeldung, wenn ein Bild länger als 2 Sekunden zum Laden benötigt oder wenn eine Datei einen Statuscode höher als 400 wiedergibt, kannst du jeweils spezifische Kriterien hinzufügen.

Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟ ist für [Browser- und Full Pagecheck-]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}) sowie [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) verfügbar. Beachte, dass bei Transaktionsprüfobjekten die [Wasserfall-Option in einem Schritt]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="de" >}}) ausgewählt sein muss, um zusätzliche Bedingungen einzurichten.