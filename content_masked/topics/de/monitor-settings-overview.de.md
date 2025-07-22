{
  "hero": {
    "title": "Ubersicht der monitoreinstellungen"
  },
  "title": "Ubersicht der monitoreinstellungen",
  "summary": "Jedes Prüfobjekt hat einige allgemeine und einige individuelle Einstellungen (abhängig vom Prüfobjekttyp). Sieh dir an, welche Einstellungen verfügbar sind.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/ubersicht-der-monitoreinstellungen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

## Die Prüfobjekteinstellungen aufrufen

Um die Prüfobjekteinstellungen zu verwalten:

1. Gehe zu [SHORTCODE_1]Überwachung > Prüfobjekteinrichtung[SHORTCODE_2].
2. Suche nach dem Namen des Prüfobjekts, dessen Einstellungen du aufrufen möchtest, und klicke auf den zugehörigen Link in der Spalte *Prüfobjektname*. Gib (einen Teil des) Prüfobjektnamen, -typ, die -gruppe oder URL in das Suchfeld ein, um die Ergebnisse einzuschränken.
    Der Bildschirm Prüfobjektkonfiguration wird angezeigt. Er enthält Registerkarten mit all deinen Prüfobjekteinstellungen. Unten findest du Infos zu den verschiedenen Einstellungsregisterkarten.
3. Nimm die erforderlichen Änderungen auf den Registerkarten vor.
4. Klicke auf die [SHORTCODE_3]Speichern[SHORTCODE_4]-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

## Kategorien der Prüfobjekteinstellungen

Jeder Prüfobjekttyp erfüllt einen bestimmten Zweck, und nicht alle Einstellungen sind für alle Prüfobjekttypen anwendbar. Sieh dir die Einstellungen an, die für dein Prüfobjekt relevant sind:
- Haupteinstellungen
   - [Überwachungsintervall]([LINK_URL_1])
   - [Dynamische Werte in URL und Post-Inhalten]([LINK_URL_2])
   - [Prüfobjektmodus]([LINK_URL_3])
   - [Prüfobjekt-Anmerkungen]([LINK_URL_4])
   - [Prüfobjektvorlagen]([LINK_URL_5])
- [Schritte (Transaktionsprüfobjekte)]([LINK_URL_6])
- [Schritte (Multi-Step-Prüfobjekte)]([LINK_URL_7])
- [Fehlerbedingungen]([LINK_URL_8])
- Erweiterte Einstellungen
   - [Browsertypen]([LINK_URL_9])
   - [Blockierung von Google Analytics]([LINK_URL_10])
   - [Bandbreiten-Drosselung]([LINK_URL_11])
   - [DNS Bypass]([LINK_URL_12])
- [Nicht primäre Checkpoints]([LINK_URL_13])
- [Wartungszeiträume]([LINK_URL_14])
- [Mitglied von]([LINK_URL_15])
- [Prüfobjektberechtigungen]([LINK_URL_16])

## Dashboard Prüfobjekteinstellungen

Das **Dashboard Prüfobjekteinrichtung** liefert dir eine tabellarische Zusammenfassung aller von dir in der Uptrends Anwendung eingerichteten Prüfobjekte, sodass du einen Überblick über die einzelnen Prüfobjekte mit den Einstellungen erhältst. Das Dashboard ermöglicht dir, Prüfobjekteinrichtungen deines Accounts anzuzeigen, zu filtern und zu exportieren.

![Dashboard Übersicht Prüfobjekteinrichtung]([LINK_URL_17])

### Prüfobjekteinrichtung anzeigen
Du kannst ganz einfach deine Prüfobjekteinstellungen anzeigen und prüfen, darunter

- **Prüfobjektname** – der Name deiner Prüfobjekteinrichtung und die Anzahl der verbrauchten [Credits]([LINK_URL_18]) für das Prüfobjekt. Ein Glaskolben-Symbol bedeutet, dass das Prüfobjekt im *Staging*-Modus ist, während der Sechskantschlüssel angibt, dass das Prüfobjekt im *Entwicklungs*[modus]([LINK_URL_19]) ist.
- **Prüfobjekt-Dashboard** – enthält den Link *Gehe zu Dashboard*, der das entsprechende Dashboard für das Prüfobjekt aufruft.
- **Typ** – gibt den [Typ des Prüfobjekts]([LINK_URL_20]) (zum Beispiel Transaktions- oder Multi-Step API-Prüfobjekte) an.
- **Überwachungsintervall (Minuten)** – gibt an, wie häufig das Prüfobjekt ausgeführt wird.
- **URL/Netzwerk Adresse** – die Browseradresse oder IP-Adresse der Website, die du gerade überwachst.
- **Aktiv** – gibt wieder, ob das Prüfobjekt aktiviert oder deaktiviert ist. Du siehst ein *Ja*, wenn das Prüfobjekt aktiviert wurde und aktiv ist. Andernfalls siehst du ein *Nein*. Aktivierte und deaktivierte Prüfobjekte geben auch in Klammern den aktuellen [Modus]([LINK_URL_21]) an, also ob *Staging* oder *Development* (Entwicklung).
- **Erstellt am** – gibt Datum und Uhrzeit an, zu dem das Prüfobjekt erstellt wurde.
- **Zuletzt geändert** – gibt Datum und Uhrzeit an, zu dem zuletzt Aktualisierungen oder Änderungen an deinem Prüfobjekt gespeichert wurden.
- **Mitglied der Gruppen** – gibt an, zu welchen Prüfobjektgruppen das Prüfobjekt gehört.

### Prüfobjekteinrichtung filtern

Um die Anzahl der Prüfobjekte zu beschränken, klicke ins Filter-Textfeld und filtere nach Prüfobjektname, ‑typ, ‑gruppe und URL. Du kannst auch nach Prüfobjektmodus filtern, indem du einfach die Kontrollkästchen neben *Development, Staging und Produktion* aktivierst.

### Prüfobjekteinrichtung exportieren

Da das Dashboard **Prüfobjekteinrichtung** hilfreich für die Visualisierung und Gruppierung der allgemeinen Einrichtungsinformationen der Prüfobjekte ist, kannst du diese Daten für einen besseren Einblick und spätere Bezugnahme exportieren. Lies diesen [Knowledge-Base-Artikel]([LINK_URL_22]), um mehr über die Schritte zum Export deiner Dashboards zu erfahren.

Nachdem du die Daten im gewünschten Format exportiert hast, kannst du die Einzelheiten deiner Prüfobjekteinrichtung wie im vorherigen Abschnitt, [Dashboard Prüfobjekteinrichtungen]([LINK_URL_23]), beschrieben anzeigen. Du wirst weitere Spalten sehen, darunter:

- **Alarm bei Zeitlimit** – zeigt die Prüfobjekteinstellungen zu [Lade- und Laufzeit]([LINK_URL_24]) und ob die Fehlerbedingungen auf *Nur Farb-Code* im Ergebnis oder *Erzeuge einen Fehler* gesetzt wurden.
- **Zeitlimit** – zeigt die entsprechenden [Zeitschwellen in Millisekunden]([LINK_URL_25]) (konfiguriert und in Bezug auf die Einstellungen unter „Alarm bei Zeitlimit“).
- **Anmerkungen** – zeigt den Inhalt des *Anmerkungs*felds.