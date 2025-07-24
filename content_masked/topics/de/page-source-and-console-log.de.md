{
  "hero": {
    "title": "Seitenquelle und Konsolenprotokoll"
  },
  "title": "Seitenquelle und Konsolenprotokoll",
  "summary": "Wo du die Seitenquelle und das Konsolenprotokoll bei FPCs und Transaktionsprüfobjekten findest",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/seitenquelle-konsolen-protokoll",
  "translationKey": "[URL_1]
}

Bei [Transaktionsprüfobjekten]([LINK_URL_1]) und [Full-Page-Check-Prüfobjekten]([LINK_URL_2]) hast du die Option, die **Seitenquelle** (das HTML-Dokument, wie es vom Checkpoint empfangen wird) sowie auch das **Konsolenprotokoll** anzuzeigen, das erzeugt wurde, während die Seite lud.


## Full Page Check

Bei Full Page Checks (FPCs) sind die Seitenquelle und das Konsolenprotokoll bei jedem Prüfobjektergebnis unter der [Wasserfall-Grafik]([LINK_URL_3]) zu finden. Die Seitenquelle steht immer zur Verfügung, aber das Konsolenprotokoll ist nur verfügbar, wenn es tatsächlich Einträge im Konsolenprotokoll im Browser gab, als die Seite geladen wurde. In der Regel erstellt der Browser Einträge in das Konsolenprotokoll, wenn etwas falsch läuft, beispielsweise, wenn ein bestimmtes Element nicht korrekt geladen werden kann oder wenn ein Javascript-Fehler auftritt.

![Beispiel eines Konsolenprotokolls, das einen Fehler anzeigt]([LINK_URL_4])

## Transaktionsprüfobjekte

Bei Transaktionsprüfobjekten müssen die Seitenquelle und das Konsolenprotokoll ausdrücklich aktiviert werden.
### Einrichten der Seitenquellen- und Konsolenprotokollerfassung bei Transaktionsprüfobjekten

Um die Seitenquelle und die Konsolenprotokolldaten für einen bestimmten Schritt der Transaktion anzuzeigen, musst du für den Schritt zunächst die Option **Wasserfall** aktivieren (mehr dazu in unserem Leitfaden [Mit Transaktions-Wasserfällen arbeiten]([LINK_URL_5])). Dann ist die Option **Page Source** (Seitenquelle) verfügbar. Das Aktivieren dieser Option sorgt dafür, dass Prüfobjektergebnisse sowohl die Seitenquelleninformationen und jegliche Konsolenprotokolldaten enthält, die während der Ausführung des Schrittes eventuell erzeugt wurden.

![Aktivieren der Seitenquelle im Transaktions-Editor]([LINK_URL_6])

### Anzeige der Seitenquellen- und Konsolenprotokolldaten bei Transaktionen

Nachdem du die Option für die Seitenquelle für einen Transaktionsschritt aktiviert hast, findest du die Informationen in den Prüfobjektergebnissen, die nach dem Schritt erzeugt wurden. Suche die Transaktion in deinem [Prüfobjektprotokoll]([LINK_URL_7]) oder navigiere zum Transaktions-Dashboard und klicke auf ein Prüfobjektergebnis, nachdem du die Option Seitenquelle aktiviert hast.


![Symbole für Seitenquelle und Konsolenprotokoll in den Prüfergebnissen]([LINK_URL_8])

Um die Informationen über die Seitenquelle zu öffnen, klicke auf das dritte Symbol, **[HTML_TAG_1]**, im Prüfobjektergebnis. Du findest das Konsolenprotokoll, indem du auf das letzte Symbol, **>_**, klickst, aber es ist nicht immer verfügbar.

