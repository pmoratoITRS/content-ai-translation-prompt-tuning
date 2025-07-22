{
  "title": "Neue MSA-Funktion: Fehlerhandhabung",
  "date": "2024-12-18",
  "url": "/changelog/dezember-2024-msa-fehlerbehandlung-funktion",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-error-handling-feature"
}

Wir haben zur Benutzeroberfläche im MSA Visuellen Schritte-Editor einen neuen Bereich zur „Fehlerbehandlung“ eingerichtet. Diese Funktion bietet mehr Flexibilität bei der Handhabung von MSA-Schrittfehlern, sodass du eine bessere Kontrolle hast und besser für dynamische Webserver-Verhalten anpassen kannst.

![Kontrollkästchen MSA-Fehlerbehandlung](/img/content/scr-error-handling-checkbox.min.png)

Die Auswahl des Kontrollkästchens **Nach einem Fehler fortfahren** ermöglicht dir, Fehler, die während eines MSA-Prüfobjektschritts auftreten, zu ignorieren. Dies bedeutet, wenn ein bestimmter Schritt einen Fehler meldet (beispielsweise eine fehlgeschlagene Anfrage, ein Anfrage-Timeout oder eine fehlgeschlagene Assertion), dass das Prüfobjekt fortfährt, die übrigen Schritte auszuführen. Solche Fehler werden nur in den **Schritt-Ergebnissen** sichtbar und als „Ein Fehler ist während dieses Schritts aufgetreten“ angezeigt. Dies wir nicht in den Dashboards **Fehler Übersicht** oder in Berichten wiedergegeben.  

Diese Art der Fehlerbehandlung ähnelt der von Transaktionsprüfobjekten. Weitere Informationen findest du im Knowledge-Base-Artikel [Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="de" >}}).

