{
  "hero": {
    "title": "Verteilung der Checkpoint-Überprüfungen"
  },
  "title": "Verteilung der Checkpoint-Überprüfungen",
  "summary": "Wie funktioniert das Uptrends Checkpoint-System? ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/verteilung-checkpoint-ueberpruefungen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends verfügt über eines der größten [Checkpoint-Netzwerke für das Monitoring von Servern und Websites]([LINK_URL_1]) in der Branche. Es war nie leichter, deine Websites, Server und Webservices von einer Vielzahl Standorten weltweit zu überwachen.

**Aber wie funktioniert Uptrends’ Checkpoint-System?**

## Checkpoint-Algorithmus

Wenn du ein Prüfobjekt zur Nachverfolgung hinzufügst, hast du die Möglichkeit, eine Reihe von Checkpoints aus unserem globalen Monitoring-Netzwerk auszuwählen, von denen du den Service-Status aus überprüfst.

Die Überprüfungen, die von diesen Checkpoints ausgeführt werden, erfolgen zufällig und werden niemals von einem Checkpoint zweimal in Folge ausgeführt.

Im Falle eines nicht bestätigten Fehlers führt der Service von Uptrends einen Ausfall-Double-Check über einen anderen Checkpoint aus, um sicherzustellen, dass der Fehler tatsächlich existent ist.

-   Wenn dieser Checkpoint ebenfalls einen Fehler meldet, wird der Fehler bestätigt und als solches im [SHORTCODE_1]Fehlerprotokoll des Prüfobjekts[SHORTCODE_2] verzeichnet.
-   Wenn dieser Checkpoint keinen Fehler meldet, wird angenommen, dass der Ausfall temporär war.

## Ringunterstützung (Monitoring, das von Checkpoints in einer festen Reihenfolge ausgeführt wird)

Wir unterstützen keine 'Ringtests'.
