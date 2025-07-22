{
  "hero": {
    "title": "URL-Handhabung bei Uptrends RUM"
  },
  "title": "URL-Handhabung bei Uptrends RUM",
  "summary": "Hast du dich je gefragt, wie Uptrends URLs beim Real User Monitoring handhabt? Du findest die Antwort in diesem Artikel.",
  "url": "/support/kb/rum/url-handhabung-bei-uptrends-rum",
  "translationKey": "https://www.uptrends.com/support/kb/rum/url-handling-in-uptrends-rum"
}

Uptrends RUM ermöglicht dir, Performance-Metriken in vielen unterschiedlichen Gruppierungen echter Nutzer anzuzeigen. Die Gruppierung nach Seite bietet dir großartige Einblicke in Statistiken für bestimmte Seiten, die möglicherweise wegen Problemen wie langsamer Ladezeiten Beachtung erfordern.

Uptrends sieht sich die URL an, um zu bestimmen, welche Seite Dein Besucher aufgerufen hat. Viele moderne Websites verwenden automatisch generierte URLs, die zu einer enormen Vielzahl an einzigartigen URLs führen können. Da es nicht nützlich ist, Daten für zehntausende von Seiten zu erfassen, **haben wir standardmäßig die Höchstzahl einzigartiger Seiten pro Website auf 10.000 begrenzt**. Wird diese Zahl überschritten, werden neue einzigartige Seiten unter „Sonstige“ registriert.

## URL-Normalisierung

Um die Zahl einzigartiger URLs, die wir verfolgen müssen, während wir die unterschiedlichen Seiten deiner Website ordentlich trennen, zu verringern, wenden wir einen **URL-Normalisierungsprozess** an. URL-Normalisierung bedeutet, dass die URLs, die du bei Uptrends RUM siehst, sich leicht von den tatsächlichen URLs deiner Website unterscheiden können. Insbesondere

-   ignorieren wir den Unterschied zwischen `http://` und  `https://`
-   entfernen wir den Abfrage-String (z. B. ?`?parameter=value` am Ende).
-   entfernen wir Fragmente (z. B. `#fragment` am Ende), es sei denn, die Option **URL-Fragment einschließen** ist bei den RUM-Einstellungen aktiviert
-   entfernen wir doppelte Schrägstriche von Pfadteilen der URL
-   ersetzen wir Segmente (Teile des Pfads, die durch Schrägstriche delimitiert sind), die vollständig aus Zahlen oder GUIDs mit Sternchen bestehen (`***`)
-   ersetzen wir lange Nummern (>4 Ziffern) und GUIDs in Segmenten mit Sternchen. Zum Beispiel `www.mysite.com/coupon-12345` und `www.mysite.com/coupon-123456` werden beide zu `www.mysite.com/coupon-***`
    URLs mit GUIDs wie `www.mysite.com/coupon-19740f6e-e7e6-41f2-84e4-de0b290eb05e` werden zu `www.mysite.com/coupon-***` mit den drei Sternchen als Ersatz der gesamten GUID.

## Feedback

Wir freuen uns auf deine Fragen und Feedback. Zögere nicht, dich an [uns zu wenden](/contact), insbesondere wenn du denkst, dass Uptrends RUM die unterschiedlichen Seiten deiner Website nicht optimal nachhält.
