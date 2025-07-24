{
  "hero": {
    "title": "Wartungszeiträume"
  },
  "title": "Wartungszeiträume",
  "summary": "Durch Einrichten von Wartungszeiträumen können Warnmeldungen oder Prüfobjekte vorübergehend deaktiviert werden, um den Erhalt von Fehlermeldungen zu vermeiden.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-management/wartungszeitraeume",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Du möchtest wahrscheinlich keine Warnmeldungen erhalten, während deine Server, Websites oder Webservices für eine Wartung heruntergefahren werden. Nehmen wir an, es gibt einen bestimmten Zeitraum, in dem dein Team Routinewartungen an der Website, den Webservern oder dem Webservice des Unternehmens durchführt. Während dieses Zeitraums sind möglicherweise Verfügbarkeit und Performance betroffen und deine Prüfobjekte lösen eventuell Alarme aus.

## Wartungszeiträume

Indem du einen Wartungszeitraum bei deinen Prüfobjekten einrichtest, kannst du im Vorhinein bestimmte Daten und Uhrzeiten konfigurieren und festlegen, ob du die Alarmierungen (oder die Prüfobjekte) vorübergehend deaktivierst, um Fehlermeldungen zu vermeiden.

![Wartungszeiträume für Prüfobjekte]([LINK_URL_1])


Für die Wartungszeiträume kannst du die Häufigkeit einstellen. Zeiträume können als einmaliges Ereignis oder in täglichen, wöchentlichen oder monatlichen Intervallen konfiguriert werden. Oder, wenn deine Server regelmäßig am letzten Tag des Monats heruntergefahren werden, kannst du die Anzahl der Alarme verwalten, die du an diesem Tag erhältst. Sieh dir das Thema [Wiederholung am letzten Tag des Monats]([LINK_URL_2]) an, um mehr dazu zu erfahren.

Beachte, dass bei der Einrichtung von Wartungszeiträumen die Uhrzeit und das Datum des Haupt-Accounts bei Uptrends verwendet werden. Datum und Uhrzeit des lokalen Computers (an dem du die Bearbeitung des Wartungszeitraums vornimmst) werden ignoriert. Damit wird es einfacher, wenn du mit Operatoren unterschiedlicher Zeitzonen zusammenarbeitest, da die Wartungszeiträume nun nur auf Datum und Uhrzeit vom Uptrends Account beruhen.

### Wartungszeiträume einrichten

Du richtest Wartungszeiträume für jedes Prüfobjekt einzeln ein. Um Wartungszeiträume festzulegen:

1.  Scrolle zu [SHORTCODE_5]Überwachung > Prüfobjekteinrichtung[SHORTCODE_6].
2.  Rufe durch Klicken die Einstellungen des Prüfobjekts auf, bei dem eine Wartung durchgeführt werden soll.
3.  Klicke auf die Registerkarte [SHORTCODE_7]Wartungszeiträume[SHORTCODE_8].
4.  Klicke auf [SHORTCODE_9]Neuen Wartungszeitraum hinzufügen[SHORTCODE_10].

![Einrichten eines Wartungszeitraums]([LINK_URL_3])

5.  Gib optional für den Wartungszeitraum eine Beschreibung ein.
6.  Lege das **Intervall** (*Einmalig, Täglich, Wöchentlich, Monatlich*) fest.
7.  Gib Datum und Uhrzeit bei **Von** und **Bis** ein. Diese Optionen ändern sich je nach **Intervall**-Angabe im vorherigen Schritt.
8.  Entscheide im Feld **Wartungsart**, ob nur Benachrichtigungen oder das Prüfobjekt komplett deaktiviert werden sollen.
9.  Klicke auf [SHORTCODE_11]Übernehmen[SHORTCODE_12].
10.  Klicke auf [SHORTCODE_13]Speichern[SHORTCODE_14] unten links, um die an den Prüfobjekteinstellungen vorgenommenen Änderungen zu sichern.

### Nur Benachrichtigungen oder das Prüfobjekt komplett deaktivieren

Das Einrichtungsfenster **Wartungszeitraum hinzufügen** ermöglicht die Wahl einer **Wartungsart**: **Nur Benachrichtigungen deaktivieren** oder **Überwachung komplett deaktivieren**. 

- Wenn du die Benachrichtigungen deaktivierst, wird das Monitoring fortgesetzt und auftretende Fehler werden im Ereignisprotokoll angezeigt. Es werden aber keine Alarmierungen gesendet. 
- Wenn du die Überwachung komplett deaktivierst, wird das Monitoring nicht fortgesetzt. Auftretende Fehler werden nicht im Ereignisprotokoll erfasst und es werden keine Alarmierungen gesendet.  

### Wiederholung am letzten Tag des Monats [ANCHOR_1]

Um einen Wartungsplan einzurichten, bei dem der Termin am letzten Tag des Monats liegt: 
![Einrichten eines Wartungszeitraums für den letzten Tag des Monats]([LINK_URL_4])
1. Erstelle einen neuen Wartungszeitraum wie oben beschrieben. 
2. Wähle im Drop-down-Menü bei **Intervall** „Monatlich“.  
3. Wähle 31 im Drop-down-Menü bei **An Tag** aus und klicke auf [SHORTCODE_15]Set[SHORTCODE_16].  
4. Klicke auf [SHORTCODE_17]Speichern[SHORTCODE_18], um die an den Prüfobjekteinstellungen vorgenommenen Änderungen zu sichern.

[SHORTCODE_1]**Hinweis**: Selbst wenn ein Monat weniger als 31 Tage enthält, wird dieser Plan am letzten Tag jedes Monats ausgeführt.   [SHORTCODE_2]

#### Mit Prüfobjektvorlagen Wartungszeiträume effizient konfigurieren

Solltest du Wartungen für mehrere Prüfobjekte gleichzeitig planen, verwende eine [Prüfobjektvorlage]([LINK_URL_5]). 

## Wartungszeiträume – Übersicht

Wenn du die Wartungszeiträume prüfen möchtest, die du oder ein Kollege zuvor erstellt haben, rufe *Accounteinstellungen > Wartungszeiträume* auf oder klicke auf **Alle ähnlichen Zeiträume wählen** auf der Registerkarte [SHORTCODE_19] Wartungszeiträume [SHORTCODE_20] des Prüfobjekts. 

Die Übersicht der **Wartungszeiträume** zeigt alle Wartungszeiträume deines Accounts, sodass du Zeiträume prüfen, nicht erwünschte löschen und Bereinigungen vornehmen kannst. Standardmäßig wird eine Liste für Wartungszeiträume all deiner Prüfobjekte angezeigt. Du kannst den Prüfobjektfilter [SHORTCODE_21] Alle Prüfobjekte [SHORTCODE_22] nutzen, um deine Auswahl zu verfeinern.

![Übersicht Wartungszeiträume]([LINK_URL_6])

Wartungszeiträume können ganz einfach anhand eines Drop-down-Menüs gefiltert werden. Es stehen Optionen wie **Alle Zeiträume**, **Ein Zeitraum** oder **Wiederkehrende Zeiträume** zur Verfügung. Du kannst sie auch einfach über eine Beschreibung über das Suchfeld filtern. Darüber hinaus kannst du andere [Kacheleinstellungen]([LINK_URL_7]) anzeigen, indem du auf [SHORTCODE_23] ... [SHORTCODE_24] oben rechts klickst.

[SHORTCODE_3]**Hinweis**: Administratoren und Operatoren mit der [Berechtigung, für mindestens ein Prüfobjekt die Prüfobjekteinstellungen zu bearbeiten]([LINK_URL_8]), können die Übersichtsseite **Wartungszeiträume** aufrufen. Diese Operatoren können bei Prüfobjekten, für die sie über die Berechtigung **Einstellungen bearbeiten** verfügen, Wartungszeiträume anzeigen, [bereinigen]([LINK_URL_9]) oder [alle löschen]([LINK_URL_10]). [SHORTCODE_4]

### Vergangene Wartungszeiträume bereinigen

1. Wähle *Einmalige Zeiträume* oder *Wiederkehrende Zeiträume*, nachdem du auf die Einstellungsschaltfläche [SHORTCODE_25] ... [SHORTCODE_26] in der rechten oberen Ecke geklickt hast, und klicke auf [SHORTCODE_27] Übernehmen [SHORTCODE_28].
![Wähle anzuzeigende Zeiträume aus]([LINK_URL_11])
2. Klicke auf die Schaltfläche [SHORTCODE_29]Bereinigen[SHORTCODE_30].
3. Das Dialogfenster **Bereinigen** zeigt die Anzahl der Zeiträume an, die in der Vergangenheit liegen. 
4. Klicke auf [SHORTCODE_31]OK[SHORTCODE_32], um alle vergangenen Ereignisse zu löschen.

### Alle Wartungszeiträume löschen

Um alle Wartungszeiträume zu löschen, die aktuell aufgelistet sind:

1. Wähle *Einmalige Zeiträume* oder *Wiederkehrende Zeiträume*, nachdem du auf die Einstellungsschaltfläche [SHORTCODE_33] ... [SHORTCODE_34] in der rechten oberen Ecke geklickt hast, und klicke auf [SHORTCODE_35] Übernehmen [SHORTCODE_36].
2. Klicke auf die Schaltfläche [SHORTCODE_37]Alle löschen[SHORTCODE_38].
3. Das Dialogfenster **Alle löschen** wird die Anzahl der Zeiträume anzeigen, die ausgewählt sind und gelöscht werden (alle Zeiträume sind ausgewählt und werden gelöscht).
4. Klicke auf [SHORTCODE_39]OK[SHORTCODE_40], um alle Wartungszeiträume zu löschen.
