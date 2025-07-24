{
  "hero": {
    "title": "Übergang von User-Agent nach Client Hints"
  },
  "title": "Übergang von User-Agent nach Client Hints",
  "summary": "Uptrends‘ Real User Monitoring nutzt einen User Agent Request Header, um Nutzerdaten zu erfassen. Google verschiebt in zukünftigen Versionen von Chromium-basierten Browsern diesen User Agent-String nach Client Hints.",
  "url": "[URL_BASE_TOPICS]rum/client-hints",
  "translationKey": "[URL_1]
}

## Was ist ein User Agent?
Ein User Agent (UA) ist ein HTTP Request Header, der verwendet wird, um die Webseiten an die Spezifikationen des Browsers anzupassen. Erhält ein Webserver eine Anfrage für eine Webseite vom Browser des Clients, sendet der Browser einen Request Header mit dem User Agent-String. Dies übermittelt dem Server, welcher Browsertyp auf der anderen Seite vorliegt. Bevor er mit dem Senden der Seite antwortet, passt der Webserver die Webseite an, sodass der Inhalt auf diesen speziellen Browsertyp ausgerichtet ist.

Der User Agent-String für einen Chrome Request Header könnte zum Beispiel wie folgt aussehen:
[INLINE_CODE_1]

Nutzt du Uptrends‘ [Real User Monitoring]([LINK_URL_1]), wird ein kleines Skript zu den Seiten hinzugefügt, die du mit RUM überwachst. Rufen deine Nutzer dann die Webseite mit einem RUM-Skript auf, erfasst es über den HTTP User-Agent Request Header Informationen zum Browser, zur Plattform und zu seinen Funktionsfähigkeiten. Sobald die Seite komplett geladen ist, bündelt das Skript die erfassten Daten mit den Informationen zum Browser und Standort des Besuchers und sendet sie an dein Uptrends Dashboard.

## Warum Client Hints und was ändert sich?
Derzeit erfasst Uptrends anhand des User Agent-Strings Daten über den Browsertyp und die -version des Nutzers sowie Betriebssystem und -version des Geräts. Google Chrome verschiebt diesen String nach User-Agent Client Hints (UA-CH) bei allen Chrome-Geräten und Chromium-basierten Browsern, auch Microsoft Edge. Mit Client Hints werden diese Informationen in kleinere, getrennte Bereiche geteilt. Es gibt keinen längeren Datenstring mehr.

Google macht dies auf zwei Gründen: Es ist eine bessere Vorgehensweise, um den Datenschutz für den Webbesucher zu gewährleisten, und eine Methode, Daten an Entwickler in einem benutzerfreundlicheren Format zurückzugeben.

## Wie wirkt es sich auf das Real User Monitoring aus?
Uptrends wird auf diese Änderung vorbereitet sein und das Skript entsprechend anpassen. Auf Client-Seite ist **keine Handlung erforderlich**.

Die Informationen, die mit dem aktuellen User Agent erfasst werden, werden nach und nach verringert. Es bedeutet, dass zukünftig eventuell weniger Nutzerinformationen für das Monitoring zur Verfügung stehen. Sobald sich dies ändert und unsere Skripte auf Client-Seite angepasst werden müssen, werden wir dich davon unterrichten.

Wenn du mehr zu den Hintergründen zu dieser Verschiebung und die Phasen der UA-Beschränkungen bei Chromium M101 erfahren möchtest, gibt der [Artikel User-Agent Reduction on The Chromium Projects]([LINK_URL_2]) einen Einblick.

[SHORTCODE_1] **Hinweis**: Wenn du dir Sorgen über das RUM-Skript und Datenschutz machst, erfährst du mehr mit unserem Knowledge-Base-Artikel zum [Real User Monitoring und Datenschutz]([LINK_URL_3]) [SHORTCODE_2]
