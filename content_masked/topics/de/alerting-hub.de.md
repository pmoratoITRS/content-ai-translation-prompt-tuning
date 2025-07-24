{
  "hero": {
    "title": "Alarmierungs-Hub"
  },
  "title": "Alarmierungs-Hub",
  "summary": "Die Überblicksseite zum Thema Alarmierungen",
  "url": "[URL_BASE_TOPICS]alarme/alarmierungs-hub",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Die Alarmierung ist ein komplexes Thema und erfordert viele Einstellungen, die reibungslos ineinandergreifen, um das erwartete Ergebnis zu liefern. Sie stützt sich auf die korrekte Einrichtung von Fehlerbedingungen, Meldedefinition, Eskalationsstufen und Integrationen. Es sind einige Parameter einzugeben und der Hub soll dir dabei helfen.

Der Hub informiert dich über die Theorie des Alarmierens, indem er dich auf die grundlegenden Konzepte und andere relevante Themen in der Knowledge Base hinweist. Vom Hub aus kannst du direkt zu den entsprechenden Einstellungen in der Uptrends Anwendung springen. Der Hub zeigt dir auch die derzeitigen Status an: Gibt es aktive Warnmeldungen und sind die Einstellungen, auf die du dich verlässt, wie Meldedefinitionen und Integrationen, aktiviert? Und schließlich zeigt er dir, ob du noch über Credits für Benachrichtigungen verfügst.

Öffne den Alarmierungs-Hub über [SHORTCODE_1]Alarmierung > Entdecke die Alarmierung[SHORTCODE_2] im Hauptmenü.

![]([LINK_URL_1])

Der obere Bereich des Hubs und die Seitenleiste enthalten Links zu den grundlegenden Konzepten sowie wo und wie du Alarme einrichtest. Eine Reihe von Links führen zu Artikeln in der Knowledge Base. Andere Links bringen dich direkt zu den Bereichen der Anwendung, in denen du Definitionen erstellst, die für das Funktionieren von Alarmierungen erforderlich sind.

Der untere Bereich des Hubs sagt dir, wie es gerade um deine Alarmierungen steht, beispielsweise wie viele Prüfobjekte derzeit Alarme melden. Dieser Überblick ist individuell auf dich ausgerichtet und es gilt Folgendes

- Nur die Prüfobjekte oder Meldedefinitionen, bei denen du über die [Berechtigung zur Prüfobjekt-Anzeige]([LINK_URL_2]) oder [Berechtigung zur Bearbeitung der Meldedefinition]([LINK_URL_3]) verfügst, werden angezeigt.
- Nur Integrationen, bei denen du über die Berechtigung **Erstelle Integrationen** verfügst, werden angezeigt. Andere Integrationen werden hier nicht berücksichtigt.



Von hier aus kannst du direkt zu folgenden Themen springen:

-   Prüfobjekte, die auf der Liste der Alarme Priorität haben
-   Fortlaufende Alarme, die dich zum *Meldestatus*-Dashboard weiterleiten
-   Vollständige Alarmierungshistorie, die dich zum Dashboard *Alarmierungshistorie* bringt

Es werden auch einige statistische Werte zu deiner Alarmierungseinrichtung angezeigt, die dir einen schnellen Überblick geben. Die Statistiken zeigen die Anzahl

- aktiver Integrationen
- der [durch Meldedefinitionen abgedeckten Prüfobjekte]([LINK_URL_4]) (nur Prüfobjekte im [Produktionsmodus]([LINK_URL_5]))
- aktiver Meldedefinitionen
- verfügbarer Benachrichtigungs-Credits

Beachte in Bezug auf den Wert **Meldedefinitionen aktiv**, dass nur Definitionen bei diesem Wert berücksichtigt werden, die aktiv sind und mindestens über eine aktive Eskalationsstufe verfügen. Es ist kein Problem, für eine aktive Meldedefinition keine aktiven Eskalationsstufen einzurichten. Es werden dann gegebenenfalls Alarme generiert, die in der Uptrends Anwendung angezeigt werden, zum Beispiel in der Alarmierungshistorie, aber es werden keine Warnmeldungen an Operatoren ausgesendet. Diese Definition wird dann auch nicht in der Statistik unter **Meldedefinitionen aktiv** gezählt.

Es muss zudem mindestens eine Integration in einer Eskalationsstufe einer Meldedefinition festgelegt sein, bei der die Berechtigung **Nutze Integration** (oder eine höhere Berechtigungsstufe) für den aktuellen Operator gesetzt ist. Andernfalls wird die Meldedefinition nicht als aktiv angezeigt.
