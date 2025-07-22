{
  "hero": {
    "title": "Benutzerdefinierte Berichtskacheln"
  },
  "title": "Benutzerdefinierte Berichtskacheln",
  "summary": "Zeige deine Monitoring-Daten als Liste oder Diagramm in angepassten Dashboards anhand benutzerdefinierter Berichtskacheln.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/dashboards/benutzerdefinierte-berichtskacheln",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends bietet eine große Bandbreite an Berichtskacheln, die für alle Monitoring-Anforderungen geeignet sind. Diese Berichtskacheln zeigen die Metriken deiner Prüfobjekte, Checkpoints und Fehlerstatus in komfortablen Diagrammen. Als Teil deiner [Dashboard-Einstellungen]([LINK_URL_1]) umfassen diese Kacheln verschiedene Typen wie tabellarische Listen von Daten, Kurven-, Balken- und Tortendiagrammen.

[Füge zunächst eine Berichtskachel]([LINK_URL_2]) zu deinen Standard-Dashboards von Uptrends hinzu oder erstelle deine Einrichtung von Grund auf. Klicke dann auf das Symbol [SHORTCODE_1] [SHORTCODE_2], um die Einstellungen der Kachel aufzurufen und die Konfiguration anzupassen.

Dieser Knowledge-Base-Artikel führt dich durch die unterschiedlichen Kacheltypen und ihre Einstellungen.

## Einfache Daten Liste oder Diagramm [ANCHOR_1]

Dieser Berichtstyp ermöglicht die Wahl von Prüfobjekten und Prüfobjektgruppen, um Metriken der Optionen **Allgemein**, **Core Web Vitals** und **W3C Navigation** anzuzeigen. Diese Metriken können abhängig vom Prüfobjekttyp und anderen Konfigurationseinstellungen variieren.

Um die **Core Web Vitals** und **W3C Navigation-Metriken** deiner Prüfobjekte zu aktivieren, stelle sicher, dass der [Browser-Typ]([LINK_URL_3]) des Prüfobjekts **Chrome mit extra Metriken** ist. Stelle bei Transaktionsprüfobjekten sicher, dass auch [Leistungsmetriken]([LINK_URL_4]) bei den **Wasserfall**-Einstellungen deiner Transaktionsschritte aktiviert ist.

Der Zeitraum vor dieser Änderung wird keine Messdaten zu **Core Web Vitals** und **W3C Navigation** wiedergeben. Du kannst den Berichtszeitraum in den Kacheleinstellungen so anpassen, dass nur ab der Zeit angezeigt wird, ab dem **Chrome mit extra Metriken** aktiviert wurde.

Ist dies konfiguriert, zeigen einfache Datenlisten oder -diagramme eine Grafik entsprechend den Metriken. Die Legende und Mouse-over über der Grafik bieten mehr Informationen über die Schritte. Um weitere Infos zu den zugehörigen Metriken zu erhalten, lies den Knowledge-Base-Artikel [Berechnung der Verfügbarkeit und Ausfallzeiten]([LINK_URL_5]).

![Metriken Einfache Daten Liste oder Diagramm]([LINK_URL_6])  


### Allgemein

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:

- Gesamtzeit, Auflösungszeit, Verbindungszeit und Downloaddauer
- Verfügbarkeit in Prozent, Ausfallzeit in Prozent, Verfügbarkeit und Ausfallzeit
- Bestätigte und unbestätigte Fehler
- Überwachungen, Alarme und Gesamtzahl Bytes
- Verfügbarkeit in Prozent – SLA Zielwert, Gesamtzeit – SLA Zielwert, Operator-Response-Zeit – SLA Zielwert und Operator-Response-Zeit

![Allgemeine Metriken Einfaches Daten Diagramm]([LINK_URL_7])  

### Core Web Vitals

Das FPC- und das Transaktionsprüfobjekt erfassen beide Daten zu [Core Web Vitals]([LINK_URL_8]), wenn der Browsertyp [Chrome mit extra Metriken]([LINK_URL_9]) ausgewählt wurde.

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:

 - First Contentful Paint
 - Largest Contentful Paint
 - Time to Interactive
 - Total Blocking Time
 - Cumulative Layout Shift

![Metriken Einfaches Daten Diagramm für Core Web Vitals]([LINK_URL_10])  


### W3C Navigation

Das FPC- und das Transaktionsprüfobjekt erfassen beide Daten zu [W3C Navigation]([LINK_URL_11]) und [Core Web Vitals]([LINK_URL_12]), wenn der Browsertyp [Chrome mit extra Metriken]([LINK_URL_13]) ausgewählt wurde.

Wähle eine der folgenden Metriken, damit die Daten in einer Berichtskachel angezeigt werden:
  - Request Start
  - Time to First Byte
  - DOM Interactive
  - DOM Completed
  - Load Event

![Metriken Einfache Daten Liste für W3C Navigation]([LINK_URL_14])  


## Liste Prüfobjektdaten/Prüfobjekt Daten Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, Zeitraum und wähle dann, Folgendes anzuzeigen:

- SLA Verfügbarkeit in Prozent, Verfügbarkeit in Prozent – SLA Zielwert
- SLA Gesamtzeit, Gesamtzeit – SLA Zielwert, SLA Ausfallzeiten 
- SLA Operator-Response-Zeit, Operator-Response – SLA Zielwert
- Gesamtzeit, Überprüfungen, bestätigte Fehler, unbestätigte Fehler
- Verfügbarkeit in Prozent, Ausfallzeiten in Prozent
- Sortieren nach und Zeige Zeile für
  
![Screenshot Diagrammkachel für Prüfobjektdaten]([LINK_URL_15])  
  
![Screenshot Listenkachel für Prüfobjektdaten]([LINK_URL_16])  

## Fehler Typ Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen und Zeitraumoptionen.  
  
![Screenshot Fehlertyp – Liste und Diagramm]([LINK_URL_17])  

## Liste Checkpoint Daten/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, Zeitraum und wähle dann, Folgendes anzuzeigen: 

- Gesamtzeit, Auflösungszeit
- Verbindungszeit, Downloaddauer
- Überwachungen, bestätigte Fehler und Sortieren nach 
  
![Screenshot Diagrammkachel für Checkpoint-Daten]([LINK_URL_18])

![Screenshot Listenkachel für Checkpoint-Daten]([LINK_URL_19])  

## Multicheckpoint Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, welche Metrik in der Liste oder dem Diagramm wiedergegeben werden soll.  
  

![Screenshot Diagrammkachel für Multicheckpoint-Daten]([LINK_URL_20]) 
  
![Screenshot Listenkachel für Multicheckpoint-Daten]([LINK_URL_21]) 

## Multiprobe Liste/Diagramm  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, welche Metrik in der Liste oder dem Diagramm wiedergegeben werden soll.  
  
![Screenshot Diagrammkachel für Multiprobe-Daten]([LINK_URL_22])  

![Screenshot Listenkachel für Multiprobe-Daten]([LINK_URL_23])

## Details der letzten Überwachung [ANCHOR_2]

Zeige an, wann ein Prüfobjekt oder eine Prüfobjektgruppe das letzte Mal geprüft wurde, und wähle den Zeitraum, für den die Daten angezeigt werden sollen.  
![Screenshot benutzerdefinierte Berichtskacheln für Prüfobjekt-Kontrolldetails]([LINK_URL_24])

## Prüfobjektprotokoll  

Wähle Prüfobjekte oder Prüfobjektgruppen, einen Zeitraum und dann, wie Fehler gefiltert werden sollen sowie ob der Bericht als Datei exportiert werden soll.  
  
![Screenshot Kachel Prüfobjektprotokoll]([LINK_URL_25]) 

## Alarmierungshistorie 

Zeige die Historie der Alarmierungsbenachrichtigungen nach Prüfobjekt oder Prüfobjektgruppe an und filtere Daten nach Zeitraum. 

![Screenshot Kachel Alarmierungshistorie]([LINK_URL_26])

## Schrittdauer Liste/Diagramm  

Für Transaktions- und Multi-Step API-Prüfobjekte und jeweils ein Prüfobjekt zu einer Zeit. Zeigt die Dauer von Schritten über einen Zeitraum.
  
![Screenshot Diagrammkachel für Schrittdauer]([LINK_URL_27])  

## Liste/Diagramm Durchschnittliche Dauer Schritte  

Für Transaktions- und Multi-Step API-Prüfobjekte und jeweils ein Prüfobjekt. Zeigt die durchschnittliche Dauer von Schritten.
  
![Screenshot Diagrammkachel für durchschnittliche Schrittdauer]([LINK_URL_28])  
