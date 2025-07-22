{
  "hero": {
    "title": "Prüfobjektmodi"
  },
  "title": "Prüfobjektmodi",
  "summary": "Uptrends bietet drei neue Prüfobjektemodi: Entwicklung, Staging und Produktion.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/pruefobjektmodi",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-mode"
}

Wenn du ein neues Prüfobjekt einrichtest, aktivierst du es in der Regel direkt in deinem Monitoring-Account. Sobald es aktiviert ist, erzeugt das Prüfobjekt jede Minute Messungen (abhängig vom eingestellten Monitoring-Intervall). Diese Messungen siehst du wiederum im Prüfobjektprotokoll und Uptrends erzeugt Warnmeldungen, wenn ein Fehler auftritt. In vielen Fällen funktioniert ein umgehend aktiviertes Prüfobjekt sehr gut. Aber die direkte Aktivierung ist nicht immer optimal. 

## Produktionsmodus oder nicht – das ist die Frage

Wenn du beispielsweise eine neue Transaktion freigeben möchtest, arbeitest du wahrscheinlich einige Zeit an ihr, bevor du sie veröffentlichst, also in Produktion stellst. In der Zwischenzeit sollte die Transaktion eine Zeit lang getestet werden, um ihre Stabilität zu verifizieren, ohne dass sie falsch positive Meldungen erzeugt (Fehlermeldungen). Falsch positive Meldungen haben eine unerwünschte Auswirkung auf deine SLAs und anderen Verfügbarkeitszahlen im gesamten Account.

Ein ähnlicher Fall ist das Ersetzen einer bestehenden Transaktion durch ein aktualisiertes Skript, sobald du deine aktualisierte Website veröffentlichst. Dann sollte auch diese Transaktion gut vorbereitet und startbereit sein. Solange das neue Transaktionsskript jedoch inaktiv ist, nutzt das Prüfobjekt wertvolle Transaktions-Credits, die zur verfügbaren Gesamtzahl zählen. Du kannst zusätzliche Credits kaufen, aber es gibt eine effizientere Möglichkeit, deine Prüfobjekte zu organisieren.

## Prüfobjekt-Lebenszyklen mit Prüfobjektmodi verwalten

Es gibt drei neue Prüfobjektemodi: **Development** (Entwicklung), **Staging** und **Produktion**. Du kannst zwischen diesen Modi bei allen Prüfobjekttypen (nicht nur bei Transaktionsprüfobjekten) wechseln, wenn du einen Professional-, Business- oder Enterprise-Account hast. Bei allen anderen Accounts ist der Prüfobjektmodus der Produktionsmodus.

Zu welchen Gelegenheiten sind die unterschiedlichen Prüfobjektmodi also vorteilhaft?

### Entwicklungsmodus

Prüfobjekte im Entwicklungsmodus sind immer inaktiv. Du kannst keine Ausführung für Prüfobjekte im Entwicklungsmodus einrichten und das Prüfobjekt erzeugt keine Ergebnisse im Prüfobjektprotokoll. Das bedeutet auch, dass sie kostenlos sind! Du kannst beliebig viele Prüfobjekte im Entwicklungsmodus einrichten – ohne zusätzliche Kosten. Alle historischen Daten eines bestehenden Prüfobjekts werden jedoch gelöscht, sobald du das Prüfobjekt in den Entwicklungsmodus setzt.

Prüfobjekte im Entwicklungsmodus sind nützlich für das Erstellen und Testen von Entwürfen. Nehmen wir an, du erstellst eine neue Transaktion oder ein Prüfobjekt für eine Multi-step API und musst manuelle Tests innerhalb des Editors ausführen. Auf Grundlage der Testergebnisse kannst du die Transaktion weiter verfeinern, bis du mit den Testergebnissen zufrieden bist. Bis du das Prüfobjekt in den Staging- oder Produktionsmodus setzt, kostet es dich nichts. Und das Prüfobjekt wirkt sich nicht auf deine Verfügbarkeitswerte aus.

Dementsprechend kannst du im Entwicklungsmodus mehrere (inaktive) Kopien behalten, ohne zusätzliche Prüfobjekte, Transaktionsschritte oder API-Schritte zu kaufen. Du kannst Prüfobjekte sehr lange im Entwicklungsmodus behalten. Wenn du jedoch bereit bist, ein Prüfobjekt aus dem inaktiven Entwicklungsmodus in den Staging- oder Produktionsmodus zu befördern, benötigt dein Account entsprechende Credits, um es zu aktivieren. Oder du tauscht es gegen ein anderes Prüfobjekt aus.

### Staging-Modus

Der Staging-Modus ist üblicherweise der nächste Schritt im Lebenszyklus eines Prüfobjekts. Im Gegensatz zum Entwicklungsmodus erlaubt dir der Staging-Modus, ein Prüfobjekt zur normalen Ausführung einzurichten. Sobald es aktiviert wurde, erzeugt das Prüfobjekt neue Messungen wie jedes andere Prüfobjekt. Die Ergebnisse sind wie gewohnt im Prüfobjektprotokoll zu sehen. Das Schöne an einem Staging-Modus ist, dass du sehen kannst, wie stabil die Monitoring-Ergebnisse sind, aber sie wirken sich nicht auf die Verfügbarkeitsrate deines Accounts oder auf die SLAs aus und Uptrends sendet keine Warnmeldungen. Du führst deine Prüfobjekte sozusagen in einer Sandbox-Umgebung aus. Die Messungen sind real, aber Verfügbarkeit, SLAs, historische Statistiken und die Warnmeldeliste bleiben frei ([erfahre mehr](/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/die-auswirkung-des-staging-modus-auf-berichte-und-sla-daten)).

Sobald du ein Prüfobjekt in den Staging-Modus setzt, zählt es bei der Gesamtzahl deiner Prüfobjekte/Credits deines Accounts. Normalerweise beförderst du ein Prüfobjekt im Staging-Modus in den Produktionsmodus, sobald du sicher bist, dass das Prüfobjekt stabil ist. Andernfalls nutzt du nicht die Vorteile der vollen Funktionsreihe, während die Kosten dieselben wie bei einem Prüfobjekt im Produktionsmodus sind.

### Produktionsmodus {id="monitormodeproduction"}

Der Produktionsmodus ist der Standardmodus. Im Produktionsmodus wird das Prüfobjekt regulär ausgeführt, die Verfügbarkeit wird auf die allgemeine Account-Verfügbarkeit angerechnet, die Prüfobjekt-Ergebnisse werden bei den SLA-Berechnungen berücksichtigt und du erhältst Warnmeldungen.
