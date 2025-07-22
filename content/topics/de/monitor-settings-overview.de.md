{
  "hero": {
    "title": "Ubersicht der monitoreinstellungen"
  },
  "title": "Ubersicht der monitoreinstellungen",
  "summary": "Jedes Prüfobjekt hat einige allgemeine und einige individuelle Einstellungen (abhängig vom Prüfobjekttyp). Sieh dir an, welche Einstellungen verfügbar sind.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/ubersicht-der-monitoreinstellungen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-settings-overview",
  "sectionlist": false
}

## Die Prüfobjekteinstellungen aufrufen

Um die Prüfobjekteinstellungen zu verwalten:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Suche nach dem Namen des Prüfobjekts, dessen Einstellungen du aufrufen möchtest, und klicke auf den zugehörigen Link in der Spalte *Prüfobjektname*. Gib (einen Teil des) Prüfobjektnamen, -typ, die -gruppe oder URL in das Suchfeld ein, um die Ergebnisse einzuschränken.
    Der Bildschirm Prüfobjektkonfiguration wird angezeigt. Er enthält Registerkarten mit all deinen Prüfobjekteinstellungen. Unten findest du Infos zu den verschiedenen Einstellungsregisterkarten.
3. Nimm die erforderlichen Änderungen auf den Registerkarten vor.
4. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

## Kategorien der Prüfobjekteinstellungen

Jeder Prüfobjekttyp erfüllt einen bestimmten Zweck, und nicht alle Einstellungen sind für alle Prüfobjekttypen anwendbar. Sieh dir die Einstellungen an, die für dein Prüfobjekt relevant sind:
- Haupteinstellungen
   - [Überwachungsintervall]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}})
   - [Dynamische Werte in URL und Post-Inhalten]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dynamic-date-notation-in-url-and-post-content" lang="de" >}})
   - [Prüfobjektmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}})
   - [Prüfobjekt-Anmerkungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="de" >}})
   - [Prüfobjektvorlagen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="de" >}})
- [Schritte (Transaktionsprüfobjekte)]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}})
- [Schritte (Multi-Step-Prüfobjekte)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}})
- [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}})
- Erweiterte Einstellungen
   - [Browsertypen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="de" >}})
   - [Blockierung von Google Analytics]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="de" >}})
   - [Bandbreiten-Drosselung]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling" lang="de" >}})
   - [DNS Bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="de" >}})
- [Nicht primäre Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="de" >}})
- [Wartungszeiträume]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="de" >}})
- [Mitglied von]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="de" >}})
- [Prüfobjektberechtigungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}})

## Dashboard Prüfobjekteinstellungen

Das **Dashboard Prüfobjekteinrichtung** liefert dir eine tabellarische Zusammenfassung aller von dir in der Uptrends Anwendung eingerichteten Prüfobjekte, sodass du einen Überblick über die einzelnen Prüfobjekte mit den Einstellungen erhältst. Das Dashboard ermöglicht dir, Prüfobjekteinrichtungen deines Accounts anzuzeigen, zu filtern und zu exportieren.

![Dashboard Übersicht Prüfobjekteinrichtung](/img/content/src_monitor-setup-dashboard-overview.min.png)

### Prüfobjekteinrichtung anzeigen
Du kannst ganz einfach deine Prüfobjekteinstellungen anzeigen und prüfen, darunter

- **Prüfobjektname** – der Name deiner Prüfobjekteinrichtung und die Anzahl der verbrauchten [Credits]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}) für das Prüfobjekt. Ein Glaskolben-Symbol bedeutet, dass das Prüfobjekt im *Staging*-Modus ist, während der Sechskantschlüssel angibt, dass das Prüfobjekt im *Entwicklungs*[modus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}) ist.
- **Prüfobjekt-Dashboard** – enthält den Link *Gehe zu Dashboard*, der das entsprechende Dashboard für das Prüfobjekt aufruft.
- **Typ** – gibt den [Typ des Prüfobjekts]({{< ref path="/support/kb/basics/monitor-types" lang="de" >}}) (zum Beispiel Transaktions- oder Multi-Step API-Prüfobjekte) an.
- **Überwachungsintervall (Minuten)** – gibt an, wie häufig das Prüfobjekt ausgeführt wird.
- **URL/Netzwerk Adresse** – die Browseradresse oder IP-Adresse der Website, die du gerade überwachst.
- **Aktiv** – gibt wieder, ob das Prüfobjekt aktiviert oder deaktiviert ist. Du siehst ein *Ja*, wenn das Prüfobjekt aktiviert wurde und aktiv ist. Andernfalls siehst du ein *Nein*. Aktivierte und deaktivierte Prüfobjekte geben auch in Klammern den aktuellen [Modus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}) an, also ob *Staging* oder *Development* (Entwicklung).
- **Erstellt am** – gibt Datum und Uhrzeit an, zu dem das Prüfobjekt erstellt wurde.
- **Zuletzt geändert** – gibt Datum und Uhrzeit an, zu dem zuletzt Aktualisierungen oder Änderungen an deinem Prüfobjekt gespeichert wurden.
- **Mitglied der Gruppen** – gibt an, zu welchen Prüfobjektgruppen das Prüfobjekt gehört.

### Prüfobjekteinrichtung filtern

Um die Anzahl der Prüfobjekte zu beschränken, klicke ins Filter-Textfeld und filtere nach Prüfobjektname, ‑typ, ‑gruppe und URL. Du kannst auch nach Prüfobjektmodus filtern, indem du einfach die Kontrollkästchen neben *Development, Staging und Produktion* aktivierst.

### Prüfobjekteinrichtung exportieren

Da das Dashboard **Prüfobjekteinrichtung** hilfreich für die Visualisierung und Gruppierung der allgemeinen Einrichtungsinformationen der Prüfobjekte ist, kannst du diese Daten für einen besseren Einblick und spätere Bezugnahme exportieren. Lies diesen [Knowledge-Base-Artikel]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="de" >}}), um mehr über die Schritte zum Export deiner Dashboards zu erfahren.

Nachdem du die Daten im gewünschten Format exportiert hast, kannst du die Einzelheiten deiner Prüfobjekteinrichtung wie im vorherigen Abschnitt, [Dashboard Prüfobjekteinrichtungen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-setup" lang="en" >}}), beschrieben anzeigen. Du wirst weitere Spalten sehen, darunter:

- **Alarm bei Zeitlimit** – zeigt die Prüfobjekteinstellungen zu [Lade- und Laufzeit]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) und ob die Fehlerbedingungen auf *Nur Farb-Code* im Ergebnis oder *Erzeuge einen Fehler* gesetzt wurden.
- **Zeitlimit** – zeigt die entsprechenden [Zeitschwellen in Millisekunden]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) (konfiguriert und in Bezug auf die Einstellungen unter „Alarm bei Zeitlimit“).
- **Anmerkungen** – zeigt den Inhalt des *Anmerkungs*felds.