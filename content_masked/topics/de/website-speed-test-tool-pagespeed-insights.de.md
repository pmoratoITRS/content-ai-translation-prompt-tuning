{
  "hero": {
    "title": "Test-Tool für Website-Ladezeit: PageSpeed Insights"
  },
  "title": "Test-Tool für Website-Ladezeit: PageSpeed Insights",
  "summary": "Uptrends' kostenloses Tool zur Messung der Website-Ladezeit zeigt Werte von Google PageSpeed Insights zusammen mit deinem Wasserfallbericht. Erfahre mehr über PageSpeed Insights und wie Google die Seitenauswertung berechnet.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/browser-monitoring/test-tool-fuer-website-ladezeit-pagespeed-insights",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dein kostenloser [Website-Ladetest]([LINK_URL_1]) umfasst die Seitenauswertung und Verbesserungsmöglichkeiten der Performance von [Google PageSpeed Insights]([LINK_URL_2]). Wir haben die Daten von Google bei den Testergebnissen von Uptrends aufgenommen, um dir alle Informationen zu geben, die du benötigst, um die Nutzerzufriedenheit mit deiner Website zu erhöhen. Uptrends gibt dir die Informationen zu deinen Seiten für jedes einzelne Element, sodass du mögliche Probleme bei diesen schnell findest und den Ladefortschritt der Seite anhand eines leicht verständlichen Wasserfallberichts sehen kannst.  

## Was ist PageSpeed Insights?

PageSpeed Insights ist ein Tool, das von Google für Webentwickler (und jede andere interessierte Person) bereitgestellt wird, die sich einen Überblick über die Website-Performance aus Google-Sicht wünschen. Google nennt auch Gelegenheiten zur Performance-Verbesserung, sodass du für deine Bemühungen der Ladezeitoptimierung Ansatzpunkte findest.

## Warum hat sich mein PageSpeed Insights-Wert geändert?

Wenn du unser kostenloses Tool zum Testen der Ladezeit bereits in der Vergangenheit genutzt hast, stellst du möglicherweise eine Änderung bei der Auswertung fest. Uptrends ruft den PageSpeed Insight-Wert und die resultierenden Empfehlungen von Google ab. Dein Wert hat sich geändert, weil Google die Berechnung des Werts in der [fünften Version der PageSpeed Insights API]([LINK_URL_3]) geändert hat.

Zuvor war der Wert von PageSpeed Insights primär auf die Gepflogenheiten zur Verminderung von Seitengrößen und Beschleunigung des Seitenaufbaus basiert. Die neue Version berücksichtigt diese, aber passt den Wert auf Grundlage anderer Faktoren an, die von Lighthouse-Diagnose-Tools (Labordaten) und tatsächlichen Nutzererfahrungen stammen.

## Wie berechnet Google meinen Seitenwert?

PageSpeed Insights ruft Daten aus vielen Quellen für mobile und Desktop-Ladezeiten ab, die zu einem Seitenwert und Empfehlungen zur Verbesserung der Seite führen.

### Labordaten

[Lighthouse]([LINK_URL_4]) erfasst und analysiert Daten über die Ladezeiten von Seiten und weist ihnen einen [Wert]([LINK_URL_5]) zu: ≥90 schnell, 50–89 durchschnittlich, ≤ 50 langsam. Lighthouse basiert den Wert auf:

-   [First Contentful Paint]([LINK_URL_6]): Der Zeitpunkt, an dem der Browser den ersten DOM-Inhalt darstellt.
-   [First Meaningful Paint]([LINK_URL_7]): Der Zeitpunkt, an dem der Nutzer denkt, dass der Hauptinhalt geladen wurde.
-   [Speed Index]([LINK_URL_8]): Wie schnell eine Seite sichtbar geladen wurde.
-   [First CPU Idle]([LINK_URL_9]): Zeitpunkt, an dem die meisten Benutzerschnittstellenelement interaktiv werden.
-   [Time to Interactive]([LINK_URL_10]): Die Seite zeigt nützlichen Inhalt, Event Handler wurden erfasst und die Seite reagiert innerhalb von 50 Millisekunden auf Nutzerinteraktionen.
-   [Estimated Input Latency]([LINK_URL_11]): Reaktionsbereitschaft bei Eingabe.

### Nutzerdaten

Nutzer des Chrome-Browsers von Google können einstellen, dass Chrome Daten über Seiten-Performances erfasst, während sie im Web navigieren. Wenn Google den Website-Wert berechnet, ruft es diese Daten ab, um zu sehen, wie echte Nutzer deine Seite erleben – basierend auf:

-   First Contentful Paint: Der Zeitpunkt, an dem der Browser den ersten DOM-Inhalt darstellt.
-   [First Input Delay]([LINK_URL_12]): Die Zeit zwischen der ersten Interaktion des Nutzers mit der Seite und der Reaktion der Seite.

Google vergleicht deine Seitenladezeiten mit denen konkurrierender Seiten und passt den Seitenwert entsprechend an.

### Page Audits

Google untersucht die Seite, wie sie aktuell besteht, und zeigt Elemente auf, die gut sind, sowie Einzelheiten, die deine Aufmerksamkeit erfordern könnten. Bei der Seitenüberprüfung findest du Informationen zu:

-   **Opportunities**, also Gelegenheiten oder Wege, wie du die Ladezeit verringern kannst
-   **Diagnostics** mit Hinweisen, wie gut deine Seite die Best Practices der Webentwicklung befolgt und
-   **Passed Audits** mit der Liste aller Prüfungen, die deine Seite erfolgreich durchlaufen ist.

Weitere Informationen zu Google PageSpeed Insights findest du bei [Stack Overflow]([LINK_URL_13]).

## Warum ist der PageSpeed Insights-Wert interessant?

Google stuft Seiten mit einem schnellen mobilen Performance-Wert höher ein, sodass du einen hohen Wert benötigst, um deine Website-SEO zu verbessern. Studien haben bestätigt, dass Nutzer vor allem schnelle Ladezeiten schätzen. Die Seiten-Performance ist direkt mit Abbruchraten, Nutzerzufriedenheit, Konversionsraten und Umsatz verknüpft.
