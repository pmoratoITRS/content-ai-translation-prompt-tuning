{
  "hero": {
    "title": "Fehlerbehandlung bei Multi-Step APIs"
  },
  "title": "Fehlerbehandlung bei Multi-Step APIs",
  "summary":"Fehler bei Multi-Step API-Prüfobjekten handhaben und ignorieren.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-fehlerbehandlung",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-error-handling"
}

Es kann Situationen geben, in denen es zu unerwarteten oder dynamischen Webserver-Verhalten kommt, während du Multi-Step API (MSA)-Prüfobjekte testest oder ein Prüfobjekt ausgeführt wird. Einige dieser Reaktionen können Zeitüberschreitungen bei Abfragen oder fehlgeschlagene Assertions sein, die deine Prüfobjekte daran hindern, andere Abfragen auszuführen.

Wenn du beispielsweise ein MSA-Prüfobjekt eingerichtet hast, um Informationen von einer E-Commerce-Plattform abzurufen, hat dieses Prüfobjekt vielleicht vier /GET-Abfrageschritte in folgender Abfolge:

1. GET /product – gibt alle Produkte und ihre Daten aus.
2. GET /products/{productID} – gibt ein bestimmtes Produkt und seine Daten aus.
3. GET /users – gibt alle Nutzer und ihre Daten aus.
4. GET /users/{userID} – gibt einen bestimmten Nutzer und seine Daten aus.

Die obige Konfiguration zeigt, dass Schritt 1 und 2 Produktdaten abfragen, während Schritt 3 und 4 Nutzerdaten abfragen. Wird dieses Prüfobjekt ausgeführt und bei Schritt 2 tritt ein Fehler auf, wie etwa eine Abfrage-Zeitüberschreitung oder eine Änderung des Endpunktnamens, verhindert der Fehler, dass das Prüfobjekt die nächsten Schritte ausführt.

In diesem Moment ist die Funktion der **Fehlerbehandlung** praktisch. Selbst wenn Schritt 2 einen Fehler verursacht, sollten die Daten von Schritt 3 und 4 abgerufen werden, da diese unabhängig von den vorherigen /GET-Abfragen sind. Der Fehler sollte das Prüfobjekt nicht daran hindern, die verbleibenden Schritte auszuführen.

## Fehlerhandhabung

Die Funktion **Fehlerbehandlung** des MSA ermöglicht dir, API-Fehler flexibel zu steuern und zu handhaben. Bei jedem MSA-Schritt deines Prüfobjekts hast du die Möglichkeit, das Kontrollkästchen **Ausführung fortsetzen und Fehler ignorieren** zu aktivieren, um Fehler in der Schrittausführung zu ignorieren:

![Kontrollkästchen MSA-Fehlerbehandlung](/img/content/scr-error-handling-checkbox.min.png)

Indem du die Option aktivierst, fährt dein Prüfobjekt automatisch mit dem nächsten Schritt fort, auch wenn ein Fehler im Schritt aufgetreten sein sollte. Dein Prüfobjekt ignoriert Fehler. Das heißt, diese Fehler werden nicht aufgezeichnet oder in einem deiner [Fehler Übersichts-Dashboards]({{< ref path="/support/kb/alerting/errors/errors-overview" lang="de" >}}) oder in [Berichten]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="de" >}}) aufgeführt. Alle ignorierten Fehler werden nur im Pop-up-Fenster **Kontrolldetails** aufgezeigt, wenn du die Option **Jetzt testen** ausführst, und in den Prüfobjektprotokollen.

Dieses Konzept wird in der folgenden Darstellung eines Prüfobjektergebnisses des vorigen Beispiels gezeigt. Beachte, wie Schritt 2 aufgrund eines Status 404 Not Found fehlgeschlagen ist. Wird das Kontrollkästchen **Ausführung fortsetzen und Fehler ignorieren** nicht aktiviert, schlägt das Prüfobjekt an der Stelle fehl, an der ein Fehler auftritt (Schritt 2). Dieser Fehler verhindert die weitere Ausführung des Prüfobjekts und der verbleibenden Schritte:

![Deaktivierte MSA-Fehlerbehandlung](/img/content/scr-disabled-error-handling.min.png)

Wenn **Ausführung fortsetzen und Fehler ignorieren** jedoch in Schritt 2 aktiviert ist, ignoriert das Prüfobjekt den Schritt mit dem Fehler und fährt mit der Überprüfung der verbleibenden Schritte fort:

![Aktivierte MSA-Fehlerbehandlung](/img/content/scr-enabled-error-handling.min.png)

## Verwandte Artikel

Informationen zur Fehlerbehandlung bei Transaktionsprüfobjekten findest du im Knowledge-Base-Artikel [Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="de" >}}).
