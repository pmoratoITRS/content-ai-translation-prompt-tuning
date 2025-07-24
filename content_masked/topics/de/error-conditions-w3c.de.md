{
  "hero": {
    "title": "Fehlerbedingungen – W3C-Messwertprüfungen"
  },
  "title": "Fehlerbedingungen – W3C-Messwertprüfungen",
  "summary": "Einsatz von Schwellwerten bei W3C Metriken, um Fehler auszulösen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-w3c",
  "tableofcontents": true,
  "translationKey": "[URL_1]
}

Das World Wide Web Consortium (oder kurz W3C) ist eine internationale Organisation, die sich mit der Entwicklung von Normen für das World Wide Web befasst. Als solche hat sie einen Standard für Browser und Webanwendungen definiert, um Zeitmessungen zum Laden von Webseiten durchzuführen und anzuzeigen.

Die Prüfobjekttypen mit dem [Browsertyp mit extra Metriken]([LINK_URL_1]) messen und berichten die [W3C Navigation Timing-Metriken]([LINK_URL_2]). Diese Messungen werden bei den Kontrolldetails des Prüfobjekts berichtet, und du kannst Fehlerbedingungen für sie einrichten. Daher sind Bedingungen für W3C-Metriken Teil der [Fehlerbedingungen]([LINK_URL_3]).

Beachte, dass verschiedene Prüfobjekttypen unterschiedliche Fehlerbedingungen beinhalten. Sieh dir die Tabelle der [verfügbaren Fehlerbedingungen]([LINK_URL_4]) an, um herauszufinden, welche Optionen für bestimmte Prüfobjekttypen möglich sind.

## Fehlerbedingungen auf Basis der W3C-Metriken definieren

Um Fehlerbedingungen auf Basis der W3C-Metriken zu definieren:

1. Gehe zu [SHORTCODE_1]Überwachung > Prüfobjekteinrichtung[SHORTCODE_2].
2. Klicke auf den Prüfobjektnamen, um ihn zu bearbeiten.
3. Öffne die Registerkarte [SHORTCODE_3]Fehlerbedingungen[SHORTCODE_4].
4. Erweitere die Kategorie der *Prüfe W3C Metriken*, indem du auf den Pfeil vor der Kategorie klickst.
 
   ![Screenshot Fehlerbedingung W3C-Metriken]([LINK_URL_5])

5. Aktiviere die Fehlerbedingungen, indem du die Kontrollkästchen markierst und einen Wert eingibst. Belasse alle Metriken deaktiviert, die nicht mit einer Fehlerbedingung verknüpft werden sollen.
6. Klicke auf die [SHORTCODE_5]Speichern[SHORTCODE_6]-Schaltfläche.

## Die W3C-Metriken [ANCHOR_1]

Die W3C-Metriken, die von Prüfobjekttypen mit dem [Browsertyp mit extra Metriken]([LINK_URL_6]) gemessen werden, werden im Knowledge-Base-Artikel [W3C Navigation Timing-Metriken]([LINK_URL_7]) erläutert. Die Metriken entsprechen den Fehlerbedingungen in der Kategorie *Prüfe W3C Metriken*. Einzig der Messwert Load Event wird im Rahmen der W3C-Fehlerbedingungen nicht berücksichtigt. Unter dem nachfolgenden Abschnitt [Fehlerbedingung Load Event ]([LINK_URL_8]) erfährst du, wie du eine Fehlerbedingung hierfür einrichtest.

## Die Fehlerbedingung Load Event [ANCHOR_2]

Du vermisst vielleicht die Metrik Load Event unter den Fehlerbedingungen in der Kategorie *Prüfe W3C Metriken*. Wenn du eine Fehlerbedingung für diesen Messwert einrichten möchtest, ist dies für den Prüfobjekttyp [Full Pagecheck]([LINK_URL_9]) möglich. Folge diesen Schritten:

1. Öffne die Prüfobjekteinstellungen.
2. Stelle sicher, dass du auf der Registerkarte [SHORTCODE_7] Allgemein [SHORTCODE_8] den **Browsertyp** *Chrome mit extra Metriken* ausgewählt hast.
3. Aktiviere auf der Registerkarte [SHORTCODE_9] Erweitert [SHORTCODE_10] im Bereich *Messung* unter **Ladezeit basiert auf** den Wert *W3C Load Event*.
4. Setze auf der Registerkarte [SHORTCODE_11]Fehlerbedingungen[SHORTCODE_12] die Schwellenwerte für **Prüfe Seitenladezeit**.

Der Knowledge-Base-Artikel [Fehlerbedingungen – Seitenladezeit]([LINK_URL_10]) bietet weitere Infos über das Einrichten der Schwellenwerte von Ladezeiten.
