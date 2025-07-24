{
  "hero": {
    "title": "Prüfobjekt-Abdeckung durch Alarmierung"
  },
  "title": "Prüfobjekt-Abdeckung durch Alarmierung",
  "summary": "Übersicht über alle Prüfobjekte mit Informationen, weshalb die Alarmierung für das Prüfobjekt abgedeckt ist oder nicht",
  "url": "[URL_BASE_TOPICS]alarme/pruefobjekt-alarmierung-abdeckung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Die Übersicht [Prüfobjekt-Abdeckung durch Alarmierung]([LINK_URL_1]) ist eine Liste deiner Prüfobjekte, die zeigt, für welche dieser Prüfobjekte Meldedefinitionen bestehen. Sie gibt detaillierte Informationen darüber, weshalb dies gegebenenfalls so ist oder eben nicht.

[SHORTCODE_1] **Hinweis**: **Prüfobjekt Abdeckung durch Alarmierungen** berücksichtigt deine Berechtigungen und bietet dir eine individualisierte Anzeige. Sie zeigt nur die Meldedefinitionen, für die du die Berechtigung zur Bearbeitung hast. Im Allgemeinen kann das für den Uptrends Account bedeuten, dass es eventuell ein Prüfobjekt gibt, das von einer Meldedefinition abgedeckt ist und Warnmeldungen aussendet. Im Überblick wird es jedoch als nicht abgedeckt angezeigt, weil du nicht über Zugriffsrechte auf diese Meldedefinition verfügst. [SHORTCODE_2]

Wenn du von Prüfobjekten eine Warnmeldung erwartest, sie aber keine erzeugen, oder sie erzeugen wider Erwarten eine Warnmeldung, kannst du an diesem Ort deine Fehlerbehebung in Angriff nehmen.

Öffne die Übersicht über [SHORTCODE_3]Alarmierung > Entdecke die Alarmierung[SHORTCODE_4], klicke dann auf die Statistik „Prüfobjekte in Produktion, die durch Alarmierung abgedeckt werden“.

![Screenshot der Statistik Alarmierungsabdeckung von Prüfobjekten]([LINK_URL_2])

Die Seite *Prüfobjekt Abdeckung durch Alarmierung* erscheint und die Prüfobjekte, die nicht von einer Alarmierungseinstellung abgedeckt sind, werden an erster Stelle der Liste mit einer roten Schattierung angezeigt.

![Screenshot Übersicht der Alarmierungsabdeckung von Prüfobjekten]([LINK_URL_3])

Warum sind diese Prüfobjekte nicht abgedeckt?
Es gibt mehrere Bedingungen für eine Abdeckung durch die Alarmierung:

- das Prüfobjekt ist aktiv
- die Alarmierung für das Prüfobjekt ist aktiv
- es gibt mindestens eine aktive Meldedefinition, die dem Prüfobjekt zugewiesen ist (direkt oder über eine Prüfobjektgruppe)
- bei der aktiven Meldedefinition ist mindestens eine Eskalationsstufe aktiviert

Überprüfe die Liste auf ein „Nein“ oder „inaktiv“ (Meldedefinitionen), um herausfinden, welche Bedingungen nicht erfüllt werden.
