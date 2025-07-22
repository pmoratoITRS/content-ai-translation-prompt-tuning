{
  "hero": {
    "title": "Mit SLA-Daten und -Berichten arbeiten"
  },
  "title": "Mit SLA-Daten und -Berichten arbeiten",
  "summary": "Erfahre, wie du SLA-Daten interpretierst und mit ihnen arbeitest. ",
  "url": "/support/kb/dashboards-und-berichte/sla/arbeiten-mit-sla-daten-und-berichten",
  "translationKey": "https://www.uptrends.com/support/kb/sla/working-with-sla-data-and-reports"
}

Uptrends bietet standardmäßig ein Dashboard mit einer **SLA Übersicht**, das sich über das Menü unter {{< AppElement type="menuitem" >}} Dashboards > Synthetics > SLA Übersicht {{< /AppElement >}} aufrufen lässt. Solltest du [benutzerdefinierte Dashboards zur SLA Übersicht]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-multiple-SLA-definitions#custom-sla-overview-dashboard" lang="de" >}}) eingerichtet haben, sind diese unter {{< AppElement type="menuitem" >}} Dashboards > Benutzerdefinierte Dashboards {{< /AppElement >}} zu finden.

Im Übersichts-Dashboard überprüfst du die Einhaltung der SLA, lädst PDF- und Excel-Dateien der SLA-Daten und planst regelmäßige SLA-Berichte.

## Die SLA Übersicht

Standardmäßig zeigt die **SLA Übersicht** deine SLA-Ziele und -Istwerte in Spaltenpaaren auf Basis des im Schnellmenü ausgewählten Zeitraums.

- **Verfügbarkeit - SLA Zielwert und Verfügbarkeit - SLA Istwert** – Deine SLA Ziel-Verfügbarkeitsrate wird durch das Verfügbarkeitsziel definiert. Die SLA Istwert-Verfügbarkeitsrate ist die tatsächliche Verfügbarkeitsrate, bei der alle ausgeschlossenen Zeiten berücksichtigt werden, die du in der SLA Definition angegeben hast.
- **Gesamtzeit - SLA Zielwert und Gesamtzeit - SLA Istwert** – Deine SLA Ziel-Gesamtzeit ist der Höchstwert in Sekunden, die eine Seite zum Laden benötigen darf, um die SLA einzuhalten. Die SLA Gesamtzeit ist die tatsächliche Durchschnittsladezeit in Sekunden für den Zeitraum.
- **Operator-Response-Zeit - SLA Zielwert und Operator-Response-Zeit - SLA Istwert** – Der SLA Operator-Response-Zielwert ist der Höchstwert, innerhalb dessen ein Operator ein Problem in Uptrends bestätigen kann. Der SLA-Operator-Response-Istwert ist die tatsächlich benötigte Antwortzeit.
- **Bestätigte Fehler** – Die Anzahl verifizierter Fehler, die für den Zeitraum aufgezeichnet wurden.
- **Ausfallzeit** – Die Summe der Ausfallzeit in Sekunden für den angezeigten Zeitraum.
- **Ausfallzeit in Prozent** – alle Ausfälle für den Zeitraum als Prozentwert.

{{< callout >}}
**Hinweis**: Solltest du in deinem **SLA Übersichts**-Bericht nur Striche und Nullen statt Daten sehen, sind die Einstellungen deiner Kachel/deines Dashboards mit den Daten kollidiert und haben zu ungültigen Daten geführt. [Mehr erfahren]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="de" >}}).
{{< /callout >}}

## Neuberechnung von SLA-Daten

Manchmal wird die Einrichtung eines Wartungsfensters oder einer temporären Ausschlusszeit in der SLA Definition vergessen. Das kann einen SLA-Bericht erheblichen verfälschen, aber du bleibst nicht auf den schlechten Daten sitzen.

### Am gleichen Tag

Wenn du deinen Fehler sofort bemerkst, kannst du [die Fehler in den Prüfobjektprotokollen löschen]({{< ref path="support/kb/alerting/errors/clearing-errors#clear-individual-errors" lang="de" >}}).

### In den vergangenen Tagen (bis zu 90 Tagen)

Das Löschen von Fehlern aus SLA-Berichten vom vorherigen und jedem weiteren Tag zuvor ist etwas komplizierter. Uptrends speichert SLA-Daten separat von den regulären Monitoring-Daten. Am Ende jedes Tages werden deine SLA-Daten extrahiert, sodass das Löschen von Fehlern in den Prüfobjektprotokollen vom vorherigen Tag nichts an den SLA-Berichten ändert.

Du kannst dir jedoch von Uptrends helfen lassen, das Problem zu beheben. Folge den Schritten unter [Mehrere Fehler löschen]({{< ref path="support/kb/alerting/errors/clearing-errors#bulk-error-clearance" lang="de" >}}) und fülle ein Formular mit den erforderlichen Informationen aus. Auf Grundlage der Informationen wird in Uptrends’ Ticket-System ein Ticket erstellt. Bedenke jedoch, dass es etwas dauern kann, bis wir die Fehler gelöscht und die SLA-Daten neu berechnet haben. Sobald der Vorgang abgeschlossen ist, erhältst du eine Nachricht vom Ticket-System.

## Download oder Freigabe von SLA Übersichts-Berichten

Du hast verschiedene Möglichkeiten, SLA-Berichtsdaten als Datei herunterzuladen oder die SLA Übersichts-Daten per E-Mail zu teilen.

### Download

Du kannst die Inhalte des SLA Übersichts-Dashboards jederzeit als PDF und im Excel-Format herunterladen.

Im Fenster eines Standard- oder benutzerdefinierten Dashboards **SLA Übersicht**:

1.  Lege die Datenparameter und Prüfobjekte für den Download im Schnellmenü fest.
2.  Klicke auf das Hamburger-Symbol {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}}.
3.  Klicke im Menü entweder auf {{< AppElement type="menuitem" >}}PDF exportieren{{< /AppElement >}} oder {{< AppElement type="menuitem" >}}Excel exportieren{{< /AppElement >}}.
4.  Warte, bis Uptrends den Bericht generiert hat (je nach Datenumfang kann dies etwas dauern). Du findest die Datei in deinem Download-Ordner.

### Senden einer einmaligen E-Mail

Du kannst Daten von deinem SLA-Dashboard per E-Mail versenden und zwischen PDF-, Excel- oder HTML-Format wählen.

1. Öffne das SLA-Dashboard, von dem du die Daten versenden möchtest.
2. Klicke auf das Hamburger-Symbol {{< AppElement type="iconFeather" >}}{{< /AppElement >}} und dann auf {{< AppElement type="menuitem" >}}Per E-Mail versenden{{< /AppElement >}}.
3. Gib die E-Mail-Adressen der Empfänger ein, wähle den Dateityp und füge nach Wunsch Anmerkungen hinzu.
4. Klicke auf {{< AppElement type="button" >}} Bericht senden {{< /AppElement >}}.

### Regelmäßig E-Mails durch geplante Berichte senden {id="scheduling-reports"}

Du kannst unter **Geplante Berichte** regelmäßige Berichte einrichten, die an dich selbst oder an andere Operatoren in deinem Account gesendet werden. Dein Bericht wird an die Empfängerliste des Standard- oder benutzerdefinierten Dashboards **SLA Übersicht** gesendet:

1.  Klicke auf das Hamburger-Symbol {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}}.
2.  Klicke auf {{< AppElement type="menuitem" >}}Bericht planen{{< /AppElement >}}, um einen geplanten Bericht zu definieren.
3.  Fülle die Felder auf den Registerkarten {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} und {{< AppElement type="tab" >}}Empfänger{{< /AppElement >}} aus.
4.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.
5.  Verwalte deine Einstellungen für geplante Berichte unter {{< AppElement type="menuitem" >}} Accounteinstellungen > Geplante Berichte {{< /AppElement >}}.
