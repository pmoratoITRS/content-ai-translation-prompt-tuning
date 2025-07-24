{
  "hero": {
    "title": "Die Zeiten in Wasserfall-Grafiken"
  },
  "title": "Die Zeiten in Wasserfall-Grafiken",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/wasserfall-zeiten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Für manche Arten von Prüfobjekten erhältst du eine Wasserfall-Grafik als Ergebnis des Prüfobjekttests. Die Wasserfall-Grafik ist ein [Wasserfalldiagramm]([LINK_URL_1]), die eine grafische Repräsentation der Ladedauer von Seitenobjekten ist.

Wenn du mit der Maus über das Diagramm fährst, siehst du Details zu den Zeiten je Objekt.

![Screenshot Pop-up Wasserfall-Grafik]([LINK_URL_2])

## Schritte des Ladevorgangs

Die Zeiten werden einer Anzahl von Schritten zugeordnet, die erforderlich sind, um das Seitenobjekt zu laden. Für die Farbcodierung findest du über dem Wasserfalldiagramm eine Legende mit den Farben der Schritte.

![Screenshot Legende Wasserfall-Grafik]([LINK_URL_3])

Alle Zeitangaben erfolgen in Millisekunden. Die einzelnen Schritte während eines Ladevorgangs werden nachfolgend beschrieben.

### Start

Der *Start time*-Wert ist der einzige Wert in dieser Reihe, bei dem es sich nicht um einen Zeitraum, sondern um einen Zeitpunkt handelt. Genauer gesagt ist es der Zeitpunkt, zu dem das Laden des entsprechenden Seitenobjekts innerhalb der gesamten Zeitenfolge der Seite begonnen hat.

### Warteschlange

Die Zeitangabe *Warteschlange* ist die Dauer, in der eine Anfrage in der Warteschlange stand.

Es gibt unterschiedliche Gründe für eine Warteschlange:

- Es bestehen Anfragen mit höherer Priorität. Beispielsweise haben Bilder eine geringere Priorität als Skripte oder Stylesheets.
- Die Anfrage wartet darauf, dass ein TCP Socket frei wird.
- Es sind bereits 6 TCP-Verbindungen offen für denselben Origin. Dies gilt nur bei HTTP/1.0 und HTTP/1.1.
- Der Browser weist im Laufwerk-Cache Platz zu.

### Auflösungszeit

Die Zeit, die der Browser benötigte, um das DNS-Lookup für das Seitenobjekt durchzuführen. Das DNS-Lookup ist die Umwandlung des Domain-Namens oder der URL in die zugehörende IP-Adresse.

### TCP Connect (Verbindung)

*TCP Connect* ist die Zeit, die benötigt wird, um die tatsächliche TCP-Verbindung zwischen Client und IP-Adresse des Webservers herzustellen.

### HTTPS Handshake

Ein Handshake besteht aus einer Anzahl von untergeordneten Schritten, die notwendig sind, um eine sichere Kommunikation zwischen Client und Server zu initiieren. Dieser Schritt wird auch TLS Handshake genannt.

### Senden

Sobald eine Verbindung aufgebaut ist und eine sichere Kommunikation eingerichtet wurde, sendet der Client eine Anfrage an den Webserver.

### Warten

Die Zeit zwischen dem Senden einer Anfrage und der Antwort des Webservers.

### Empfangen

Dieser Schritt erfasst die Zeit, die benötigt wurde, um die Antwort vom Webserver zu empfangen.

### Zeitüberschreitung

Diese Zeitangabe erscheint nur, wenn eine Anfrage fehlgeschlagen ist. In dem Fall zeigt sie den Zeitraum, in dem der Client keine Antwort erhielt. Es wird dann nur eine Startzeit und einen Zeitüberschreitungswert geben, keine weiteren Zeitmessungen.
