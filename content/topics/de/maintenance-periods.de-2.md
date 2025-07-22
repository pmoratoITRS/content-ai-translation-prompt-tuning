{
  "hero": {
    "title": "Wartungszeiträume"
  },
  "title": "Wartungszeiträume",
  "summary": "Durch Einrichten von Wartungszeiträumen können Warnmeldungen oder Prüfobjekte vorübergehend deaktiviert werden, um den Erhalt von Fehlermeldungen zu vermeiden.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-management/wartungszeitraeume",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/maintenance-periods",
  "tableofcontents": true
}

Du möchtest wahrscheinlich keine Warnmeldungen erhalten, während deine Server, Websites oder Webservices für eine Wartung heruntergefahren werden. Nehmen wir an, es gibt einen bestimmten Zeitraum, in dem dein Team Routinewartungen an der Website, den Webservern oder dem Webservice des Unternehmens durchführt. Während dieses Zeitraums sind möglicherweise Verfügbarkeit und Performance betroffen und deine Prüfobjekte lösen eventuell Alarme aus.

## Wartungszeiträume

Indem du einen Wartungszeitraum bei deinen Prüfobjekten einrichtest, kannst du im Vorhinein bestimmte Daten und Uhrzeiten konfigurieren und festlegen, ob du die Alarmierungen (oder die Prüfobjekte) vorübergehend deaktivierst, um Fehlermeldungen zu vermeiden.

![Wartungszeiträume für Prüfobjekte](/img/content/gif-monitor-maintenance-periods.gif)


Für die Wartungszeiträume kannst du die Häufigkeit einstellen. Zeiträume können als einmaliges Ereignis oder in täglichen, wöchentlichen oder monatlichen Intervallen konfiguriert werden. Oder, wenn deine Server regelmäßig am letzten Tag des Monats heruntergefahren werden, kannst du die Anzahl der Alarme verwalten, die du an diesem Tag erhältst. Sieh dir das Thema [Wiederholung am letzten Tag des Monats]({{< ref path="#lastday" lang="de" >}}) an, um mehr dazu zu erfahren.

Beachte, dass bei der Einrichtung von Wartungszeiträumen die Uhrzeit und das Datum des Haupt-Accounts bei Uptrends verwendet werden. Datum und Uhrzeit des lokalen Computers (an dem du die Bearbeitung des Wartungszeitraums vornimmst) werden ignoriert. Damit wird es einfacher, wenn du mit Operatoren unterschiedlicher Zeitzonen zusammenarbeitest, da die Wartungszeiträume nun nur auf Datum und Uhrzeit vom Uptrends Account beruhen.

### Wartungszeiträume einrichten

Du richtest Wartungszeiträume für jedes Prüfobjekt einzeln ein. Um Wartungszeiträume festzulegen:

1.  Scrolle zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2.  Rufe durch Klicken die Einstellungen des Prüfobjekts auf, bei dem eine Wartung durchgeführt werden soll.
3.  Klicke auf die Registerkarte {{< AppElement type="tab" >}}Wartungszeiträume{{< /AppElement >}}.
4.  Klicke auf {{< AppElement type="button" >}}Neuen Wartungszeitraum hinzufügen{{< /AppElement >}}.

![Einrichten eines Wartungszeitraums](/img/content/scr-Maintenance-period-setup.min.png)

5.  Gib optional für den Wartungszeitraum eine Beschreibung ein.
6.  Lege das **Intervall** (*Einmalig, Täglich, Wöchentlich, Monatlich*) fest.
7.  Gib Datum und Uhrzeit bei **Von** und **Bis** ein. Diese Optionen ändern sich je nach **Intervall**-Angabe im vorherigen Schritt.
8.  Entscheide im Feld **Wartungsart**, ob nur Benachrichtigungen oder das Prüfobjekt komplett deaktiviert werden sollen.
9.  Klicke auf {{< AppElement type="button" >}}Übernehmen{{< /AppElement >}}.
10.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}} unten links, um die an den Prüfobjekteinstellungen vorgenommenen Änderungen zu sichern.

### Nur Benachrichtigungen oder das Prüfobjekt komplett deaktivieren

Das Einrichtungsfenster **Wartungszeitraum hinzufügen** ermöglicht die Wahl einer **Wartungsart**: **Nur Benachrichtigungen deaktivieren** oder **Überwachung komplett deaktivieren**. 

- Wenn du die Benachrichtigungen deaktivierst, wird das Monitoring fortgesetzt und auftretende Fehler werden im Ereignisprotokoll angezeigt. Es werden aber keine Alarmierungen gesendet. 
- Wenn du die Überwachung komplett deaktivierst, wird das Monitoring nicht fortgesetzt. Auftretende Fehler werden nicht im Ereignisprotokoll erfasst und es werden keine Alarmierungen gesendet.  

### Wiederholung am letzten Tag des Monats {id="lastday"}

Um einen Wartungsplan einzurichten, bei dem der Termin am letzten Tag des Monats liegt: 
![Einrichten eines Wartungszeitraums für den letzten Tag des Monats](/img/content/scr-maintenance-last-day-month.min.png)
1. Erstelle einen neuen Wartungszeitraum wie oben beschrieben. 
2. Wähle im Drop-down-Menü bei **Intervall** „Monatlich“.  
3. Wähle 31 im Drop-down-Menü bei **An Tag** aus und klicke auf {{< AppElement type="button" >}}Set{{< /AppElement >}}.  
4. Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die an den Prüfobjekteinstellungen vorgenommenen Änderungen zu sichern.

{{< callout >}}**Hinweis**: Selbst wenn ein Monat weniger als 31 Tage enthält, wird dieser Plan am letzten Tag jedes Monats ausgeführt.   {{< /callout >}}

#### Mit Prüfobjektvorlagen Wartungszeiträume effizient konfigurieren

Solltest du Wartungen für mehrere Prüfobjekte gleichzeitig planen, verwende eine [Prüfobjektvorlage]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="de" >}}). 

## Wartungszeiträume – Übersicht

Wenn du die Wartungszeiträume prüfen möchtest, die du oder ein Kollege zuvor erstellt haben, rufe *Accounteinstellungen > Wartungszeiträume* auf oder klicke auf **Alle ähnlichen Zeiträume wählen** auf der Registerkarte {{< AppElement type="tab" >}} Wartungszeiträume {{< /AppElement >}} des Prüfobjekts. 

Die Übersicht der **Wartungszeiträume** zeigt alle Wartungszeiträume deines Accounts, sodass du Zeiträume prüfen, nicht erwünschte löschen und Bereinigungen vornehmen kannst. Standardmäßig wird eine Liste für Wartungszeiträume all deiner Prüfobjekte angezeigt. Du kannst den Prüfobjektfilter {{< AppElement type="editbutton" >}} Alle Prüfobjekte {{< /AppElement >}} nutzen, um deine Auswahl zu verfeinern.

![Übersicht Wartungszeiträume](/img/content/scr-maintenance-period-filter.min.png)

Wartungszeiträume können ganz einfach anhand eines Drop-down-Menüs gefiltert werden. Es stehen Optionen wie **Alle Zeiträume**, **Ein Zeitraum** oder **Wiederkehrende Zeiträume** zur Verfügung. Du kannst sie auch einfach über eine Beschreibung über das Suchfeld filtern. Darüber hinaus kannst du andere [Kacheleinstellungen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/tile-filtering#tile-filtering" lang="de" >}}) anzeigen, indem du auf {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} oben rechts klickst.

{{< callout >}}**Hinweis**: Administratoren und Operatoren mit der [Berechtigung, für mindestens ein Prüfobjekt die Prüfobjekteinstellungen zu bearbeiten]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#permission-types" lang="de" >}}), können die Übersichtsseite **Wartungszeiträume** aufrufen. Diese Operatoren können bei Prüfobjekten, für die sie über die Berechtigung **Einstellungen bearbeiten** verfügen, Wartungszeiträume anzeigen, [bereinigen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods#clean-up-your-past-maintenance-periods" lang="de" >}}) oder [alle löschen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods#delete-all-maintenance-periods" lang="de" >}}). {{< /callout >}}

### Vergangene Wartungszeiträume bereinigen

1. Wähle *Einmalige Zeiträume* oder *Wiederkehrende Zeiträume*, nachdem du auf die Einstellungsschaltfläche {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} in der rechten oberen Ecke geklickt hast, und klicke auf {{< AppElement type="button" >}} Übernehmen {{< /AppElement >}}.
![Wähle anzuzeigende Zeiträume aus](/img/content/scr-maintenance-choose-periods.min.png)
2. Klicke auf die Schaltfläche {{< AppElement type="editbutton" >}}Bereinigen{{< /AppElement >}}.
3. Das Dialogfenster **Bereinigen** zeigt die Anzahl der Zeiträume an, die in der Vergangenheit liegen. 
4. Klicke auf {{< AppElement type="button" >}}OK{{< /AppElement >}}, um alle vergangenen Ereignisse zu löschen.

### Alle Wartungszeiträume löschen

Um alle Wartungszeiträume zu löschen, die aktuell aufgelistet sind:

1. Wähle *Einmalige Zeiträume* oder *Wiederkehrende Zeiträume*, nachdem du auf die Einstellungsschaltfläche {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} in der rechten oberen Ecke geklickt hast, und klicke auf {{< AppElement type="button" >}} Übernehmen {{< /AppElement >}}.
2. Klicke auf die Schaltfläche {{< AppElement type="editbutton" >}}Alle löschen{{< /AppElement >}}.
3. Das Dialogfenster **Alle löschen** wird die Anzahl der Zeiträume anzeigen, die ausgewählt sind und gelöscht werden (alle Zeiträume sind ausgewählt und werden gelöscht).
4. Klicke auf {{< AppElement type="button" >}}OK{{< /AppElement >}}, um alle Wartungszeiträume zu löschen.
