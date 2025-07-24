{
  "title": "Neue MSA-Funktion: Fehlerhandhabung",
  "date": "2024-12-18",
  "url": "[URL_BASE_CHANGELOG]dezember-2024-msa-fehlerbehandlung-funktion",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wir haben zur Benutzeroberfläche im MSA Visuellen Schritte-Editor einen neuen Bereich zur „Fehlerbehandlung“ eingerichtet. Diese Funktion bietet mehr Flexibilität bei der Handhabung von MSA-Schrittfehlern, sodass du eine bessere Kontrolle hast und besser für dynamische Webserver-Verhalten anpassen kannst.

![Kontrollkästchen MSA-Fehlerbehandlung]([LINK_URL_1])

Die Auswahl des Kontrollkästchens **Nach einem Fehler fortfahren** ermöglicht dir, Fehler, die während eines MSA-Prüfobjektschritts auftreten, zu ignorieren. Dies bedeutet, wenn ein bestimmter Schritt einen Fehler meldet (beispielsweise eine fehlgeschlagene Anfrage, ein Anfrage-Timeout oder eine fehlgeschlagene Assertion), dass das Prüfobjekt fortfährt, die übrigen Schritte auszuführen. Solche Fehler werden nur in den **Schritt-Ergebnissen** sichtbar und als „Ein Fehler ist während dieses Schritts aufgetreten“ angezeigt. Dies wir nicht in den Dashboards **Fehler Übersicht** oder in Berichten wiedergegeben.  

Diese Art der Fehlerbehandlung ähnelt der von Transaktionsprüfobjekten. Weitere Informationen findest du im Knowledge-Base-Artikel [Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen]([LINK_URL_2]).

