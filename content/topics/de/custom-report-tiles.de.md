{
  "hero": {
    "title": "Benutzerdefinierte Berichtskacheln"
  },
  "title": "Benutzerdefinierte Berichtskacheln",
  "summary": "Zeige deine Monitoring-Daten als Liste oder Diagramm in angepassten Dashboards anhand benutzerdefinierter Berichtskacheln.",
  "url": "/support/kb/dashboards-und-berichte/dashboards/benutzerdefinierte-berichtskacheln",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles"
}

Uptrends bietet eine große Bandbreite an Berichtskacheln, die für alle Monitoring-Anforderungen geeignet sind. Diese Berichtskacheln zeigen die Metriken deiner Prüfobjekte, Checkpoints und Fehlerstatus in komfortablen Diagrammen. Als Teil deiner [Dashboard-Einstellungen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards" lang="de" >}}) umfassen diese Kacheln verschiedene Typen wie tabellarische Listen von Daten, Kurven-, Balken- und Tortendiagrammen.

[Füge zunächst eine Berichtskachel]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="de" >}}) zu deinen Standard-Dashboards von Uptrends hinzu oder erstelle deine Einrichtung von Grund auf. Klicke dann auf das Symbol {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}}, um die Einstellungen der Kachel aufzurufen und die Konfiguration anzupassen.

Dieser Knowledge-Base-Artikel führt dich durch die unterschiedlichen Kacheltypen und ihre Einstellungen.

## Einfache Daten Liste oder Diagramm {id="simple-data-list-chart"}

Dieser Berichtstyp ermöglicht die Wahl von Prüfobjekten und Prüfobjektgruppen, um Metriken der Optionen **Allgemein**, **Core Web Vitals** und **W3C Navigation** anzuzeigen. Diese Metriken können abhängig vom Prüfobjekttyp und anderen Konfigurationseinstellungen variieren.

Um die **Core Web Vitals** und **W3C Navigation-Metriken** deiner Prüfobjekte zu aktivieren, stelle sicher, dass der [Browser-Typ]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="de" >}}) des Prüfobjekts **Chrome mit extra Metriken** ist. Stelle bei Transaktionsprüfobjekten sicher, dass auch [Leistungsmetriken]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="de" >}}) bei den **Wasserfall**-Einstellungen deiner Transaktionsschritte aktiviert ist.

Der Zeitraum vor dieser Änderung wird keine Messdaten zu **Core Web Vitals** und **W3C Navigation** wiedergeben. Du kannst den Berichtszeitraum in den Kacheleinstellungen so anpassen, dass nur ab der Zeit angezeigt wird, ab dem **Chrome mit extra Metriken** aktiviert wurde.

Ist dies konfiguriert, zeigen einfache Datenlisten oder -diagramme eine Grafik entsprechend den Metriken. Die Legende und Mouse-over über der Grafik bieten mehr Informationen über die Schritte. Um weitere Infos zu den zugehörigen Metriken zu erhalten, lies den Knowledge-Base-Artikel [Berechnung der Verfügbarkeit und Ausfallzeiten]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="de" >}}).

![Metriken Einfache Daten Liste oder Diagramm](/img/content/scr-data-metrics.min.png)  


### Allgemein

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:

- Gesamtzeit, Auflösungszeit, Verbindungszeit und Downloaddauer
- Verfügbarkeit in Prozent, Ausfallzeit in Prozent, Verfügbarkeit und Ausfallzeit
- Bestätigte und unbestätigte Fehler
- Überwachungen, Alarme und Gesamtzahl Bytes
- Verfügbarkeit in Prozent – SLA Zielwert, Gesamtzeit – SLA Zielwert, Operator-Response-Zeit – SLA Zielwert und Operator-Response-Zeit

![Allgemeine Metriken Einfaches Daten Diagramm](/img/content/scr_simple-data-chart.min.png)  

### Core Web Vitals

Das FPC- und das Transaktionsprüfobjekt erfassen beide Daten zu [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}), wenn der Browsertyp [Chrome mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="de" >}}) ausgewählt wurde.

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:

 - First Contentful Paint
 - Largest Contentful Paint
 - Time to Interactive
 - Total Blocking Time
 - Cumulative Layout Shift

![Metriken Einfaches Daten Diagramm für Core Web Vitals](/img/content/scr_simple-data-chart-steps.min.png)  


### W3C Navigation

Das FPC- und das Transaktionsprüfobjekt erfassen beide Daten zu [W3C Navigation]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}) und [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}), wenn der Browsertyp [Chrome mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="de" >}}) ausgewählt wurde.

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:
  - Request Start
  - Time to First Byte
  - DOM Interactive
  - DOM Completed
  - Load Event

![Metriken Einfache Daten Liste für W3C Navigation](/img/content/scr_simple-data-list.min.png)  


## Liste Prüfobjektdaten/Prüfobjekt Daten Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, Zeitraum und wähle dann, Folgendes anzuzeigen:

- SLA Verfügbarkeit in Prozent, Verfügbarkeit in Prozent – SLA Zielwert
- SLA Gesamtzeit, Gesamtzeit – SLA Zielwert, SLA Ausfallzeiten 
- SLA Operator-Response-Zeit, Operator-Response – SLA Zielwert
- Gesamtzeit, Überprüfungen, bestätigte Fehler, unbestätigte Fehler
- Verfügbarkeit in Prozent, Ausfallzeiten in Prozent
- Sortieren nach und Zeige Zeile für
  
![Screenshot Diagrammkachel für Prüfobjektdaten](/img/content/scr_monitor-data-chart.min.png)  
  
![Screenshot Listenkachel für Prüfobjektdaten](/img/content/scr_monitor-data-list.min.png)  

## Fehler Typ Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen und Zeitraumoptionen.  
  
![Screenshot Fehlertyp – Liste und Diagramm](/img/content/scr_error-type-list-chart.min.png)  

## Liste Checkpoint Daten/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, Zeitraum und wähle dann, Folgendes anzuzeigen: 

- Gesamtzeit, Auflösungszeit
- Verbindungszeit, Downloaddauer
- Überwachungen, bestätigte Fehler und Sortieren nach 
  
![Screenshot Diagrammkachel für Checkpoint-Daten](/img/content/scr_checkpoint-data-chart.min.png)

![Screenshot Listenkachel für Checkpoint-Daten](/img/content/scr_checkpoint-data-list.min.png)  

## Multicheckpoint Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, welche Metrik in der Liste oder dem Diagramm wiedergegeben werden soll.  
  

![Screenshot Diagrammkachel für Multicheckpoint-Daten](/img/content/scr_multi-checkpoint-chart-tile.min.png) 
  
![Screenshot Listenkachel für Multicheckpoint-Daten](/img/content/scr_multi-checkpoint-list-tile.min.png) 

## Multiprobe Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, welche Metrik in der Liste oder dem Diagramm wiedergegeben werden soll.  
  
![Screenshot Diagrammkachel für Multiprobe-Daten](/img/content/scr_multi-monitor-chart-tile.min.png)  

![Screenshot Listenkachel für Multiprobe-Daten](/img/content/scr_multi-monitor-list-tile.min.png)

## Details der letzten Überwachung {id="last-check-details"}

Zeige an, wann ein Prüfobjekt oder eine Prüfobjektgruppe das letzte Mal geprüft wurde, und wähle den Zeitraum, für den die Daten angezeigt werden sollen.  
![Screenshot benutzerdefinierte Berichtskacheln für Prüfobjekt-Kontrolldetails](/img/content/scr_custom-report-tiles-lastcheck.min.png)

## Prüfobjektprotokoll  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, wie Fehler gefiltert werden sollen sowie ob der Bericht als Datei exportiert werden soll.  
  
![Screenshot Kachel Prüfobjektprotokoll](/img/content/scr_monitor-log-tile.min.png) 

## Alarmierungshistorie 

Zeige die Historie der Alarmierungsbenachrichtigungen nach Prüfobjekt oder Prüfobjektgruppe an und filtere Daten nach Zeitraum. 

![Screenshot Kachel Alarmierungshistorie](/img/content/scr_alert-history-tile.min.png)

## Schrittdauer Liste/Diagramm  

Für Transaktions- und Multi-Step API-Prüfobjekte und jeweils ein Prüfobjekt zu einer Zeit. Zeigt die Dauer von Schritten über einen Zeitraum.
  
![Screenshot Diagrammkachel für Schrittdauer](/img/content/scr_step-duration-chart-tile.min.png)  

## Liste/Diagramm Durchschnittliche Dauer Schritte  

Für Transaktions- und Multi-Step API-Prüfobjekte und jeweils ein Prüfobjekt. Zeigt die durchschnittliche Dauer von Schritten.
  
![Screenshot Diagrammkachel für durchschnittliche Schrittdauer](/img/content/scr_average-step-duration-chart-tile.min.png)  
