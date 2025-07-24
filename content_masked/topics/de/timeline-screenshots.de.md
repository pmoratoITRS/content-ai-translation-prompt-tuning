{
  "hero": {
    "title": "Zeitstrahl mit Screenshots"
  },
  "title": "Zeitstrahl mit Screenshots",
  "summary": "Beschreibung Zeitstrahl-Screenshots, wie sie im Wasserfalldiagramm angezeigt werden",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/timeline-screenshots",
  "translationKey": "[URL_1]
  "TableOfContents": false
}

Das Laden einer Seite in einem Browser wird in mehreren Schritten ausgeführt. Während mehr Seitenobjekte geladen werden, zeigt der Browser den Seiteninhalt und verändert ihr Layout, bis das Laden beendet ist und dein Prüfobjekt (hoffentlich) ein Ok verzeichnet. Eine [Wasserfall-Grafik]([LINK_URL_1]) ist eine gute Darstellung dessen, was während des Ladens der Seite passiert. Da aber viele Objekte gleichzeitig laden, kann es schwer sein, eine Vorstellung davon zu erhalten, wie das tatsächlich im Browser aussieht.

Deshalb verfügt unser [Prüfobjekttyp Full Page Check (FPC)]([LINK_URL_2]) mit der Einstellung **Chrome mit extra Metriken** als Browsertyp über **Timeline Screenshots** (auch **Filmstrip** genannt). Dies ist eine Reihe von Screenshots des Browsers, die exakt zeigt, wie die Seite zu unterschiedlichen Zeiten des Ladevorgangs aussah.

![Timeline Screenshots]([LINK_URL_3])

Wenn in deinem Wasserfallbericht beunruhigende Vorgänge verzeichnet sind, wie etwa nicht ladende Bilder oder Skripte, die das Laden des übrigen Teils der Seite aufhalten, kannst du den Wasserfall-Zeitstrahl mit dem entsprechenden Screenshot abgleichen, um zu sehen, wie die Seite zu dem Zeitpunkt aussah.

## Wann werden Timeline Screenshots aufgezeichnet?

Die in Uptrends gezeigten Timeline Screenshots werden direkt in Chrome aufgenommen. Im Rahmen seiner Standardfunktionen erfasst Chrome eigene Screenshots, wenn eine Performance-Aufzeichnung über seine Entwicklerschnittstelle ausgeführt wird. Von dieser von Chrome erfassten Reihe versuchen wir, die relevantesten anzuzeigen:

- Wir nehmen die ersten Screenshots auf, nachdem bestimmte Meilensteine passiert wurden (erster/letzter Screenshot, First Contentful Paint, Largest Contentful Paint, Time to Interactive).
- Wir entscheiden basierend auf der Gesamtzeit des Prüfobjekts, wie viele Screenshots angezeigt werden, aber das Minimum sind sechs.
