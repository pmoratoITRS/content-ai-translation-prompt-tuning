{
  "hero": {
    "title": "Dynamische Werte in URLs und POST-Inhalten"
  },
  "title": "Dynamische Werte in URLs und POST-Inhalten",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/dynamische-werte-in-url-und-post-inhalten",
  "summary":"Ein Leitfaden zum Einbinden von dynamischen Werten in URLs oder in Abfrageinhalten.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/dynamic-values-in-url-and-post-content"
}

## Dynamische Werte in URLs oder Abfrageinhalten

Uptrends kann [dynamische Datumswerte]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables#date-and-time" lang="de" >}}) in URLs oder HTTP-Abfrageinhalten für die meisten Prüfobjekttypen generieren. Häufig werden Zeitstempel verwendet, da es sich dabei nicht nur um einzigartige Werte handelt, sondern weil sie auch Informationen darüber enthalten, wann die Abfrage ausgeführt wurde. Das kann nützlich für Webservices sein, die die Eingabe eines anderen Werts als Teil des Request Bodys für ein HTTP POST oder die Abfrage-URL erfordern, beispielsweise:

`... <StartDate>2023-02-27</StartDate> ...`

Statt einen festen Wert einzugeben, kann man folgende Notation verwenden, um Werte auf Grundlage des heutigen Datums/Uhrzeit zu erzeugen:

`... <StartDate>{{@DateTime(dd-MM-yyyy)}}</StartDate> ...`

Bitte beachte, dass **andere Wertformate ebenfalls möglich sind**. Darüber hinaus können wir Verschiebungen nutzen, um unterschiedliche Werte zu berechnen. Weitere Informationen zur Schreibweise und wie du Verschiebungen für deine Datumswerte anwendest, findest du im Artikel über [automatische Variablen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}}).


## Cache Busting

**Content Caching** kann unglaublich nützlich für jeden Webmaster sein, weil es mit der Zeit die allgemeine Performance mit Einsatz von weniger Ressourcen verbessern kann. Aber wenn du eine Website oder einen Service überwachst, kann es ein Cache schwieriger machen, zu erkennen, ob eins deiner Seitenelemente tatsächlich verfügbar ist.

Durch Einfügen eines zufälligen URL-Werts kannst du diesen Cache für jeden *HTTP-*, *Webservice-*, oder *Full Pagecheck*-Aufruf umgehen und sicherstellen, dass kein vorheriger Inhalt gespeichert ist.

{{< callout >}}
**Hinweis**: Die folgenden Informationen betreffen das Caching aus Server-Seite deinerseits, nicht den Website-Monitoring-Service von Uptrends.
{{< /callout >}}

### Wie funktioniert Cache Busting?

Cache Busting wird ermöglicht, indem das `{{@RandomGuid}}`-Token verwendet wird (weitere Infos findest du im [Knowledge-Base-Artikel zu automatischen Variablen )]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables#random-unique-identifier" lang="de" >}}). Um diese Funktion zu nutzen, gib einfach das Token als Teil der URL in die Prüfobjekteinstellungen ein, zum Beispiel:

`http://www.example.com?myvalue={{@RandomGuid}}`

Dies wird folgendermaßen aufgelöst:

`http://www.example.com?myvalue=37f1f109-58a2-4bea-adfb-9aed54619453`
