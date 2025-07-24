{
  "hero": {
    "title": "Dashboard- und Kachelfilter"
  },
  "title": "Dashboard- und Kachelfilter",
  "summary": "Zeige eigens ausgewählte Monitoring-Daten, indem du Filter bei einem Dashboard oder bei einzelnen Kacheln anwendest.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/dashboards/kachel-filter",
  "translationKey": "[URL_1]
}

Es gibt zwei unterschiedliche Möglichkeiten, wie du deine Dashboard-Daten filtern kannst: nach einzelnen Kacheln (damit kannst du zwei ähnliche Kacheln nebeneinander sehen, aber mit unterschiedlichen Einstellungen) oder mit einem Filter über das gesamte Dashboard.

## Dashboards filtern

Um für ein ganzes Dashboard einen Filter einzurichten, öffne das jeweilige Dashboard und nutze dann die Filteroptionen des Schnellmenüs (oben rechts am Dashboard).

![Screenshot Dashboard-Filter]([LINK_URL_1])


Du siehst mehrere Filteroptionen, die sich je nach Dashboard ändern, einschließlich:

- **Filter nach Prüfobjekt**
  Dieser Filter ist praktisch, wenn du nur Daten zu bestimmten Prüfobjekten anzeigen möchtest. Du kannst eins oder mehrere Prüfobjekte oder [Prüfobjektgruppen]([LINK_URL_2]) auswählen.
- **Filter nach Fehler**
  Anhand dieses Filters kannst du alles anzeigen: nur [unbestätigte/bestätigte Fehler]([LINK_URL_3]), nur bestätigte Fehler oder nur erfolgreiche Prüfungen (OK-Ergebnisse).
- **Filter für Teilprüfungen**
  Ein Filter für das [Parallel-Monitoring]([LINK_URL_4]), mithilfe dessen du Teilprüfungen anzeigen oder ausblenden kannst.
- **Checkpoint-Filter**
  Zeigt nur Daten nach bestimmten [Checkpoints]([LINK_URL_5]) an.
- **Filter nach Datum/Uhrzeit**
  Stelle den Filter auf einen bestimmten Zeitraum ein.

## Kachelfilter

Innerhalb einer einzelnen Kachel filtern:

1. Rufe das Dashboard auf, in dem sich die Kachel befindet, die du filtern möchtest.
2. Klicke bei der entsprechenden Kachel auf das Dreipunkte-Menü [SHORTCODE_3] [SHORTCODE_4], um die Einstellungen aufzurufen.
   Ein Pop-up-Fenster mit einer Reihe von Registerkarten und Konfigurationsoptionen, die zur Kachel gehören, erscheint.  

    ![Screenshot Kacheleinstellungen]([LINK_URL_6])

   Welche Registerkarten und Optionen verfügbar sind, ist abhängig vom [Kacheltyp]([LINK_URL_7]). Es kann eines oder eine Kombination von Folgendem sein:

   **Kachel**
   Die Optionen auf der [SHORTCODE_5]Kachel[SHORTCODE_6]-Registerkarte beziehen sich nur auf die Art, wie Daten in der Kachel dargestellt werden.

   **Gruppen und Prüfobjekte**
   Die Registerkarte [SHORTCODE_7]Gruppen und Prüfobjekte[SHORTCODE_8] ermöglicht dir, zugehörige Daten zum Kontext des Dashboards (normalerweise der Standard) anzuzeigen oder sie zu filtern und nur Daten für eine Reihe von Prüfobjekten oder Prüfobjektgruppen anzuzeigen.

   **Checkpoints**
    Filtere Daten nach dem oder den Checkpoints aus, die die Prüfungen durchgeführt haben. Die Schritte für den [Checkpoint-Filter]([LINK_URL_8]) findest du weiter unten beschrieben.

   **Zeitraum**
   Die Registerkarte [SHORTCODE_9]Zeitraum[SHORTCODE_10] lässt dich nach dem Zeitraum filtern, für den Daten angezeigt werden. Standardmäßig ist dies nach Kontext des Dashboards eingestellt.
3. Richte alle Filter ein, die du für die Kachel anwenden möchtest.
4. Klicke im Dialogfenster der Einstellungen auf [SHORTCODE_11] Übernehmen [SHORTCODE_12].
5. Wichtig: Deine Änderungen werden nicht automatisch gespeichert. Wenn du Änderungen an einzelnen Kacheln oder an den Dashboards vornimmst, achte darauf, sie anhand der Schaltfläche [SHORTCODE_13]Speichern[SHORTCODE_14] oben rechts in deinem Dashboard zu sichern.



[SHORTCODE_1] **Hinweis**: Der Knowledge-Base-Artikel [Benutzerdefinierte Berichtskacheln hinzufügen]([LINK_URL_9]) erläutert, wie du einzelne Kacheln zu Dashboards hinzufügst. [SHORTCODE_2]

## Checkpoint-Filter für Kacheln [ANCHOR_1]

Checkpoint-Filter sind für folgende [Kacheltypen]([LINK_URL_10]) verfügbar:
- Einfache Daten Liste/Diagramm
- Liste Checkpoint Daten/Diagramm
- Multicheckpoint Liste/Diagramm
- Prüfdauer Liste/Diagramm
- Prüfobjektprotokoll

Um einen Checkpoint-Filter bei einer Kachel anzuwenden:

1. Rufe im Menü [SHORTCODE_15] Dashboards [SHORTCODE_16] auf.
2. Wähle ein Dashboard.
3. Klicke auf das Dreipunkte-Menü [SHORTCODE_17] [SHORTCODE_18] einer Kachel, um die Einstellungen aufzurufen.
4. Wechsele zur Registerkarte [SHORTCODE_19] Checkpoints [SHORTCODE_20].

   ![Screenshot Checkpoint-Auswahl einer Kachel]([LINK_URL_11])

5. Wähle den/die Checkpoint(s) aus, für den/die die Kachel Daten anzeigen soll.
   Du kannst einzelne Checkpoints, Checkpoint-Regionen oder Länder (innerhalb einer Region) auswählen.
6. Klicke auf [SHORTCODE_21] Übernehmen [SHORTCODE_22].
7. Klicke auf [SHORTCODE_23] Speichern [SHORTCODE_24] oben rechts in dem Dashboard.

**Hinweis:** Es bestehen zwei Ausnahmen für Checkpoint-Filter:
- Extra Metriken mit der Kennzeichnung „Nur FPC und Transaktionen“. Ist eine dieser Optionen auf der Registerkarte [SHORTCODE_25]Kachel[SHORTCODE_26] zusammen mit einem Checkpoint-Filter ausgewählt, zeigt Uptrends eine Warnmeldung.
- Ist unter **Zeit-Gruppierung** [SHORTCODE_27] Anzeige nach Uhrzeit[SHORTCODE_28] auf der Registerkarte [SHORTCODE_29] Zeitraum [SHORTCODE_30] ausgewählt und wurde der Checkpoint-Filter aktiviert, wird eine Warnmeldung angezeigt.
![]([LINK_URL_12])
