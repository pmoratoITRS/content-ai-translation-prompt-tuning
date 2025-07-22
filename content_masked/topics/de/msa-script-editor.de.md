{
  "hero": {
    "title": "Der Multi-step API-Skript-Editor"
  },
  "title": "Der Multi-step API-Skript-Editor",
  "summary":"Ein Überblick über den Skript-Editor des Multi-step API-Prüfobjekts",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/msa-skript-editor",
  "translationKey": "[URL_1]
}

Wie das [Transaktionsprüfobjekt]([LINK_URL_1]) verfügt auch der Prüfobjekttyp Multi-step API über eine Editorversion für die Skript-Ansicht als eine Alternative zum visuellen Standardeditor. Der Skript-Editor ermöglicht genauso wie der visuelle Editor Änderungen an den Schritten des Prüfobjekts, aber im JSON-Skript statt über die Benutzeroberfläche.

## Vorteile des Skript-Editors

Es gibt mehrere Vorteile beim Einsatz eines Skript-Editors gegenüber den Prüfobjektsänderungen über die Benutzeroberfläche:

- Power-User empfinden das direkte Bearbeiten eines Skripts einfacher als das Navigieren durch eine Benutzeroberfläche. Einige Nutzer ziehen eine Arbeitsweise ähnlich dem Einsatz einer Befehlszeile vor.
- Wenn ein Skript verfügbar ist, ist eine Automatisierung möglich, beispielsweise um deine [CI/CD-Prozesse]([LINK_URL_2]) einzubauen. Mit der [Uptrends API]([LINK_URL_3]) kannst du die Schritte des Prüfobjekts im selben Moment aktualisieren, wie du die API aktualisierst, die damit geprüft wird.
- Über den Skript-Editor kannst du eine lokale Kopie der Schritte deines Prüfobjekts erstellen, indem du das Skript einfach kopierst und es in eine lokale Datei einfügst. Eine lokale Kopie bietet eine Versionskontrolle, Sicherungen des Multi-step API-Prüfobjekts und ein einfaches Reproduzieren komplizierter Einrichtungen:

## Wechsel zum Skript-Editor

Rufe den Skript-Editor für ein beliebiges Multi-step API-Prüfobjekt auf, indem du zu den Prüfobjekten wechselst, die Registerkarte [SHORTCODE_1] Schritte [SHORTCODE_2] aufrufst und auf die Schaltfläche [SHORTCODE_3] WECHSLE ZUM SKRIPT [SHORTCODE_4] oben rechts klickst. Der Wechsel in und aus dem Skript-Editor löst eine Validierung aus, mit der sichergestellt wird, dass das JSON im Skript korrekt bleibt. Das Skript sieht folgendermaßen aus:

![Der Skript-Editor]([LINK_URL_4])

## Das Skript verstehen

Wie zu sehen, ist das Skript im Grunde eine JSON-formatierte Reihe einzelner Schritte, die die konfigurierte Request-Methode, URL, Header und Request Body sowie die Authentifizierungsoptionen enthalten. Darüber hinaus enthält jeder Schritt-Eintrag die Definitionen für jegliche Variablen, die aus der Antwort erzeugt wurden, sowie Assertions die zu ihr erstellt wurden. Alle notwendigen Änderungen können direkt im Skript-Editor vorgenommen werden.

Ein einzelner Schritt wird in etwa folgendermaßen aussehen:

[CODE_BLOCK_1]

Das Hinzufügen weiterer Schritte ist genauso einfach wie das Einfügen weiterer Einträge in das Array – mit der vollständigen oben dargestellten Schrittdefinition.

Nach dem Array mit den Schritten, enthält die Schrittdefinition auch Informationen zu [vordefinierten Variablen]([LINK_URL_5]) oder [benutzerdefinierten Funktionen]([LINK_URL_6]), die du eingerichtet hast:

[CODE_BLOCK_2]
