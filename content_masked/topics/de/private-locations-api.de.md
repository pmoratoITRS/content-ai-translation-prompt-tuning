{
  "hero": {
    "title": "Private Locations API"
  },
  "title": "Private Locations API",
  "summary": "Die verfügbaren API-Methoden für Private Locations.",
  "url": "[URL_BASE_TOPICS]api/private-locations-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Private Locations API umfasst eine Reihe an Endpunkten, die Informationen zum Status und Betrieb deiner eingerichteten Private Locations bieten. Diese Endpunkte ermöglichen das Überwachen der Verfügbarkeit, Performance und Konnektivität von jedem Checkpoint.

## Status von Private Location und privatem Checkpoint

Private Location Status und Status von privatem Checkpoint sind zwei zusammenhängende Konzepte, die bei der Arbeit mit der API austauschbar sind. Der Endpunkt [INLINE_CODE_1] gibt statusbezogene Informationen für einen einzelnen, bestimmten Checkpoint im Rahmen deiner Private Location zurück. Dagegen bietet der Endpunkt [INLINE_CODE_2] einen Überblick des Status aller einzelnen privaten Checkpoints, die mit einer gegebenen Private Location in Verbindung stehen. Damit kannst du jeden Checkpoint einzeln überwachen oder eine Gesamtübersicht ihres allgemeinen Status erhalten.

## Serverinformationen

Die API liefert detaillierte Informationen über den Serverstatus, einschließlich Folgendem:

- Funktionsfähige Server – die Anzahl voll funktionsfähiger Server ohne Fehler oder Warnmeldungen
- Fehlerhafte Server – die Anzahl Server, bei denen Fehler oder Warnmeldungen bestehen oder die nicht richtig eingerichtet sind
- Anzahl Server – die Gesamtzahl Server an einem privaten Standort oder an einem bestimmten Checkpoint
- Checkpoint-Name – der Name des Checkpoints, der mit dem privaten Standort in Verbindung steht
- Status – der aktuelle Status des Servers: [INLINE_CODE_3], [INLINE_CODE_4] oder [INLINE_CODE_5]
- Statusdetails – Datum und Uhrzeit, zu denen der Server zuletzt aktiv war
- Warnungen – zeigt Warnmeldungen an, zum Beispiel, wenn der Server ein Update, eine Installation oder andere Maßnahmen erfordert

## Berechtigungen

Mit der API können die Berechtigungen für Private Locations geändert werden. Über diesen Endpunkt kannst du prüfen, ob dein Berechtigungstyp dir ermöglicht, Private Locations zu nutzen oder zu bearbeiten. Mehr zu den Berechtigungen erfährst du unter [Einrichten von Berechtigungen für Private Locations]([LINK_URL_1]).

Weitere Informationen findest du zudem in der [Uptrends Private Locations API]([LINK_URL_2]).