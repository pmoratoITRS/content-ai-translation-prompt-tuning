{
  "hero": {
    "title": "Fehlerbedingungen – W3C-Messwertprüfungen"
  },
  "title": "Fehlerbedingungen – W3C-Messwertprüfungen",
  "summary": "Einsatz von Schwellwerten bei W3C Metriken, um Fehler auszulösen.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-w3c",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-w3c"
}

Das World Wide Web Consortium (oder kurz W3C) ist eine internationale Organisation, die sich mit der Entwicklung von Normen für das World Wide Web befasst. Als solche hat sie einen Standard für Browser und Webanwendungen definiert, um Zeitmessungen zum Laden von Webseiten durchzuführen und anzuzeigen.

Die Prüfobjekttypen mit dem [Browsertyp mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) messen und berichten die [W3C Navigation Timing-Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="de" >}}). Diese Messungen werden bei den Kontrolldetails des Prüfobjekts berichtet, und du kannst Fehlerbedingungen für sie einrichten. Daher sind Bedingungen für W3C-Metriken Teil der [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}).

Beachte, dass verschiedene Prüfobjekttypen unterschiedliche Fehlerbedingungen beinhalten. Sieh dir die Tabelle der [verfügbaren Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="de" >}}) an, um herauszufinden, welche Optionen für bestimmte Prüfobjekttypen möglich sind.

## Fehlerbedingungen auf Basis der W3C-Metriken definieren

Um Fehlerbedingungen auf Basis der W3C-Metriken zu definieren:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf den Prüfobjektnamen, um ihn zu bearbeiten.
3. Öffne die Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}}.
4. Erweitere die Kategorie der *Prüfe W3C Metriken*, indem du auf den Pfeil vor der Kategorie klickst.
 
   ![Screenshot Fehlerbedingung W3C-Metriken](/img/content/scr_errorconditions-w3cmetrics.min.png)

5. Aktiviere die Fehlerbedingungen, indem du die Kontrollkästchen markierst und einen Wert eingibst. Belasse alle Metriken deaktiviert, die nicht mit einer Fehlerbedingung verknüpft werden sollen.
6. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche.

## Die W3C-Metriken {id="w3c-metrics"}

Die W3C-Metriken, die von Prüfobjekttypen mit dem [Browsertyp mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) gemessen werden, werden im Knowledge-Base-Artikel [W3C Navigation Timing-Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="de" >}}) erläutert. Die Metriken entsprechen den Fehlerbedingungen in der Kategorie *Prüfe W3C Metriken*. Einzig der Messwert Load Event wird im Rahmen der W3C-Fehlerbedingungen nicht berücksichtigt. Unter dem nachfolgenden Abschnitt [Fehlerbedingung Load Event ]({{< ref path="#load-event" lang="de" >}}) erfährst du, wie du eine Fehlerbedingung hierfür einrichtest.

## Die Fehlerbedingung Load Event {id="load-event"}

Du vermisst vielleicht die Metrik Load Event unter den Fehlerbedingungen in der Kategorie *Prüfe W3C Metriken*. Wenn du eine Fehlerbedingung für diesen Messwert einrichten möchtest, ist dies für den Prüfobjekttyp [Full Pagecheck]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) möglich. Folge diesen Schritten:

1. Öffne die Prüfobjekteinstellungen.
2. Stelle sicher, dass du auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} den **Browsertyp** *Chrome mit extra Metriken* ausgewählt hast.
3. Aktiviere auf der Registerkarte {{< AppElement type="tab" >}} Erweitert {{< /AppElement >}} im Bereich *Messung* unter **Ladezeit basiert auf** den Wert *W3C Load Event*.
4. Setze auf der Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} die Schwellenwerte für **Prüfe Seitenladezeit**.

Der Knowledge-Base-Artikel [Fehlerbedingungen – Seitenladezeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) bietet weitere Infos über das Einrichten der Schwellenwerte von Ladezeiten.
