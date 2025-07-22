{
  "hero": {
    "title": "URL-Handhabung bei Uptrends RUM"
  },
  "title": "URL-Handhabung bei Uptrends RUM",
  "summary": "Hast du dich je gefragt, wie Uptrends URLs beim Real User Monitoring handhabt? Du findest die Antwort in diesem Artikel.",
  "url": "[URL_BASE_TOPICS]rum/url-handhabung-bei-uptrends-rum",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends RUM ermöglicht dir, Performance-Metriken in vielen unterschiedlichen Gruppierungen echter Nutzer anzuzeigen. Die Gruppierung nach Seite bietet dir großartige Einblicke in Statistiken für bestimmte Seiten, die möglicherweise wegen Problemen wie langsamer Ladezeiten Beachtung erfordern.

Uptrends sieht sich die URL an, um zu bestimmen, welche Seite Dein Besucher aufgerufen hat. Viele moderne Websites verwenden automatisch generierte URLs, die zu einer enormen Vielzahl an einzigartigen URLs führen können. Da es nicht nützlich ist, Daten für zehntausende von Seiten zu erfassen, **haben wir standardmäßig die Höchstzahl einzigartiger Seiten pro Website auf 10.000 begrenzt**. Wird diese Zahl überschritten, werden neue einzigartige Seiten unter „Sonstige“ registriert.

## URL-Normalisierung

Um die Zahl einzigartiger URLs, die wir verfolgen müssen, während wir die unterschiedlichen Seiten deiner Website ordentlich trennen, zu verringern, wenden wir einen **URL-Normalisierungsprozess** an. URL-Normalisierung bedeutet, dass die URLs, die du bei Uptrends RUM siehst, sich leicht von den tatsächlichen URLs deiner Website unterscheiden können. Insbesondere

-   ignorieren wir den Unterschied zwischen [INLINE_CODE_1] und  [INLINE_CODE_2]
-   entfernen wir den Abfrage-String (z. B. ?[INLINE_CODE_3] am Ende).
-   entfernen wir Fragmente (z. B. [INLINE_CODE_4] am Ende), es sei denn, die Option **URL-Fragment einschließen** ist bei den RUM-Einstellungen aktiviert
-   entfernen wir doppelte Schrägstriche von Pfadteilen der URL
-   ersetzen wir Segmente (Teile des Pfads, die durch Schrägstriche delimitiert sind), die vollständig aus Zahlen oder GUIDs mit Sternchen bestehen ([INLINE_CODE_5])
-   ersetzen wir lange Nummern (>4 Ziffern) und GUIDs in Segmenten mit Sternchen. Zum Beispiel [INLINE_CODE_6] und [INLINE_CODE_7] werden beide zu [INLINE_CODE_8]
    URLs mit GUIDs wie [INLINE_CODE_9] werden zu [INLINE_CODE_10] mit den drei Sternchen als Ersatz der gesamten GUID.

## Feedback

Wir freuen uns auf deine Fragen und Feedback. Zögere nicht, dich an [uns zu wenden]([LINK_URL_1]), insbesondere wenn du denkst, dass Uptrends RUM die unterschiedlichen Seiten deiner Website nicht optimal nachhält.
