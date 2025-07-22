{
  "hero": {
    "title": "Dashboard- und Kachelfilter"
  },
  "title": "Dashboard- und Kachelfilter",
  "summary": "Zeige eigens ausgewählte Monitoring-Daten, indem du Filter bei einem Dashboard oder bei einzelnen Kacheln anwendest.",
  "url": "/support/kb/dashboards-und-berichte/dashboards/kachel-filter",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/tile-filtering"
}

Es gibt zwei unterschiedliche Möglichkeiten, wie du deine Dashboard-Daten filtern kannst: nach einzelnen Kacheln (damit kannst du zwei ähnliche Kacheln nebeneinander sehen, aber mit unterschiedlichen Einstellungen) oder mit einem Filter über das gesamte Dashboard.

## Dashboards filtern

Um für ein ganzes Dashboard einen Filter einzurichten, öffne das jeweilige Dashboard und nutze dann die Filteroptionen des Schnellmenüs (oben rechts am Dashboard).

![Screenshot Dashboard-Filter](/img/content/scr_dashboard-filters.min.png)


Du siehst mehrere Filteroptionen, die sich je nach Dashboard ändern, einschließlich:

- **Filter nach Prüfobjekt**
  Dieser Filter ist praktisch, wenn du nur Daten zu bestimmten Prüfobjekten anzeigen möchtest. Du kannst eins oder mehrere Prüfobjekte oder [Prüfobjektgruppen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="de" >}}) auswählen.
- **Filter nach Fehler**
  Anhand dieses Filters kannst du alles anzeigen: nur [unbestätigte/bestätigte Fehler]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}}), nur bestätigte Fehler oder nur erfolgreiche Prüfungen (OK-Ergebnisse).
- **Filter für Teilprüfungen**
  Ein Filter für das [Parallel-Monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="de" >}}), mithilfe dessen du Teilprüfungen anzeigen oder ausblenden kannst.
- **Checkpoint-Filter**
  Zeigt nur Daten nach bestimmten [Checkpoints]({{< ref path="#checkpoint-filtering" lang="de" >}}) an.
- **Filter nach Datum/Uhrzeit**
  Stelle den Filter auf einen bestimmten Zeitraum ein.

## Kachelfilter

Innerhalb einer einzelnen Kachel filtern:

1. Rufe das Dashboard auf, in dem sich die Kachel befindet, die du filtern möchtest.
2. Klicke bei der entsprechenden Kachel auf das Dreipunkte-Menü {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}}, um die Einstellungen aufzurufen.
   Ein Pop-up-Fenster mit einer Reihe von Registerkarten und Konfigurationsoptionen, die zur Kachel gehören, erscheint.  

    ![Screenshot Kacheleinstellungen](/img/content/scr_tile-settings.min.png)

   Welche Registerkarten und Optionen verfügbar sind, ist abhängig vom [Kacheltyp]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="de" >}}). Es kann eines oder eine Kombination von Folgendem sein:

   **Kachel**
   Die Optionen auf der {{< AppElement type="tab" >}}Kachel{{< /AppElement >}}-Registerkarte beziehen sich nur auf die Art, wie Daten in der Kachel dargestellt werden.

   **Gruppen und Prüfobjekte**
   Die Registerkarte {{< AppElement type="tab" >}}Gruppen und Prüfobjekte{{< /AppElement >}} ermöglicht dir, zugehörige Daten zum Kontext des Dashboards (normalerweise der Standard) anzuzeigen oder sie zu filtern und nur Daten für eine Reihe von Prüfobjekten oder Prüfobjektgruppen anzuzeigen.

   **Checkpoints**
    Filtere Daten nach dem oder den Checkpoints aus, die die Prüfungen durchgeführt haben. Die Schritte für den [Checkpoint-Filter]({{< ref path="#checkpoint-filtering-tiles" lang="de" >}}) findest du weiter unten beschrieben.

   **Zeitraum**
   Die Registerkarte {{< AppElement type="tab" >}}Zeitraum{{< /AppElement >}} lässt dich nach dem Zeitraum filtern, für den Daten angezeigt werden. Standardmäßig ist dies nach Kontext des Dashboards eingestellt.
3. Richte alle Filter ein, die du für die Kachel anwenden möchtest.
4. Klicke im Dialogfenster der Einstellungen auf {{< AppElement type="button" >}} Übernehmen {{< /AppElement >}}.
5. Wichtig: Deine Änderungen werden nicht automatisch gespeichert. Wenn du Änderungen an einzelnen Kacheln oder an den Dashboards vornimmst, achte darauf, sie anhand der Schaltfläche {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}} oben rechts in deinem Dashboard zu sichern.



{{< callout >}} **Hinweis**: Der Knowledge-Base-Artikel [Benutzerdefinierte Berichtskacheln hinzufügen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="de" >}}) erläutert, wie du einzelne Kacheln zu Dashboards hinzufügst. {{< /callout >}}

## Checkpoint-Filter für Kacheln {id="checkpoint-filtering-tiles"}

Checkpoint-Filter sind für folgende [Kacheltypen]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="de" >}}) verfügbar:
- Einfache Daten Liste/Diagramm
- Liste Checkpoint Daten/Diagramm
- Multicheckpoint Liste/Diagramm
- Prüfdauer Liste/Diagramm
- Prüfobjektprotokoll

Um einen Checkpoint-Filter bei einer Kachel anzuwenden:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Dashboards {{< /AppElement >}} auf.
2. Wähle ein Dashboard.
3. Klicke auf das Dreipunkte-Menü {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} einer Kachel, um die Einstellungen aufzurufen.
4. Wechsele zur Registerkarte {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}}.

   ![Screenshot Checkpoint-Auswahl einer Kachel](/img/content/scr-cp-selection-tiles.min.png)

5. Wähle den/die Checkpoint(s) aus, für den/die die Kachel Daten anzeigen soll.
   Du kannst einzelne Checkpoints, Checkpoint-Regionen oder Länder (innerhalb einer Region) auswählen.
6. Klicke auf {{< AppElement type="button" >}} Übernehmen {{< /AppElement >}}.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} oben rechts in dem Dashboard.

**Hinweis:** Es bestehen zwei Ausnahmen für Checkpoint-Filter:
- Extra Metriken mit der Kennzeichnung „Nur FPC und Transaktionen“. Ist eine dieser Optionen auf der Registerkarte {{< AppElement type="tab" >}}Kachel{{< /AppElement >}} zusammen mit einem Checkpoint-Filter ausgewählt, zeigt Uptrends eine Warnmeldung.
- Ist unter **Zeit-Gruppierung** {{< AppElement type="dropdown" >}} Anzeige nach Uhrzeit{{< /AppElement >}} auf der Registerkarte {{< AppElement type="tab" >}} Zeitraum {{< /AppElement >}} ausgewählt und wurde der Checkpoint-Filter aktiviert, wird eine Warnmeldung angezeigt.
![](/img/content/scr-cp-tile-time-grouping.min.png)
