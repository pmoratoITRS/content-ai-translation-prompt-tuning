{
  "hero": {
    "title": "Einfacher Webseiten-Check im Vergleich zum Real Browser Check"
  },
  "title": "Einfacher Webseiten-Check im Vergleich zum Real Browser Check",
  "summary": "Erfahre mehr über die Unterschiede zwischen einem einfachen Webseiten-Check und einem Real Browser Check.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/einfacher-webseiten-check-im-vergleich-zum-real-browser-check",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Beim [Synthetic Monitoring]([LINK_URL_1]) hast Du die Wahl zwischen zwei Optionen des Monitorings Deiner Webseite: einfache Checks und Checks anhand eines echten Browsers. Was ist der Unterschied bei diesen beiden Monitoring-Typen? Der Hauptunterschied liegt darin, wie Uptrends die Antwort behandelt.

## Die kurze Antwort

Einfache Checks sehen sich nur die erste Antwort an: Seitenelemente wie Skripte, CSS-Dateien und Bilder werden nicht abgerufen oder ausgeführt. Real Browser Checks laden alle Seiteninhalte (Skripte, CSS-Dateien, Bilder und Inhalte externer Anbieter) in das tatsächliche Browser-Fenster.

## Einfache Checks

Wenn ein Checkpoint einen einfachen Check (HTTP/HTTPS) durchführt, sendet der Checkpoint eine Seitenanfrage. Der Checkpoint erhält eine Antwort und sucht nach einigen Hauptkomponenten. Auf der Grundlage Deiner Prüfobjekteinstellungen kann ein einfacher Check Folgendes untersuchen:

-   Ergebnis-Codes
-   Antwortzeit
-   Seitengröße in Byte
-   Übereinstimmungsmuster (Zeichenfolgen)

Das Prüfobjekt lädt die Antwortinhalte niemals in einen Browser, sodass Seitenelemente wie CSS-Dateien, Skriptdateien, externe Inhalte und Bilder nie heruntergeladen, analysiert und geladen werden. Mit einem einfachen Check erfährst Du nicht von möglichen Fehlern oder Performance-Problemen, die beim Abruf und Laden des vollständigen Inhalts auftreten können. Wir erfahren, dass die Website verfügbar ist, akzeptable Codes zurückgibt und eine Mindestgröße aufweist, einschließlich der genannten Inhalte. Ein einfacher Check kann so häufig wie einmal pro Minute ausgeführt werden und so eine genauere Auskunft über die Verfügbarkeit der Seite geben.

## Real Browser Checks

Wenn ein Checkpoint einen Real Browser Check (Prüfobjekt [Full Page Check]([LINK_URL_2]), [Transaktionsprüfobjekt]([LINK_URL_3])) ausführt, ruft der Checkpoint die Seite auf und lädt die Antwort in einen echten Browser. Der Checkpoint lädt den gesamten Seiteninhalt (Skripte, CSS-Dateien, zusätzliche HTML-Dateien, Bilder und Inhalte externer Anbieter). Jede Anfrage und Antwort wird auf Performance und Fehler geprüft. Der Real Browser Check kann so häufig wie einmal alle fünf Minuten ausgeführt werden und simuliert die Anzeige einer tatsächlichen Nutzererfahrung. Ein Real Browser Check bietet einen weniger genauen Einblick in die Verfügbarkeit als ein einfacher Check.
