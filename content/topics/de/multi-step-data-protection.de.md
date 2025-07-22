{
  "hero": {
    "title": "Datenschutz bei Multi-Step APIs"
  },
  "title": "Datenschutz bei Multi-Step APIs",
  "summary": "Wie die Daten aus deinem Multi-Step API Monitoring geschützt werden können.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-datenschutz",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-data-protection",
  "tableofcontents": false,
  "sectionlist": "true"
}

Wann immer du ein Synthetic-Prüfobjekt mit Uptrends ausführst, führt der Server von dem Checkpoint-Standort Überwachungen durch. Uptrends ruft auf Level des Checkpoint-Servers alle Monitoring-Ergebnisse ab und speichert sie direkt auf der Uptrends Plattform.

Die meisten Organisationen verfügen über strenge Vorschriften hinsichtlich Datenschutz und ziehen es vor, sensible Daten nicht auf irgendeine Weise abzurufen oder zu senden. Mit der Funktion **Datenschutz** kannst du bestimmte Monitoring-Daten von der Sammlung und Speicherung bei Uptrends ausschließen. Diese Funktion bietet eine zusätzliche Ebene der Sicherheit und sorgt dafür, das sensible Daten nicht extern übertragen werden (oder den Checkpoint-Server verlassen).

![Kontrollkästchen MSA Datenschutz](/img/content/scr-data-protection-checkbox.min.png)

Standardmäßig werden die folgenden Daten erfasst und im Rahmen deiner MSA Monitoring-Ergebnisse angezeigt:

- HTTP-Anfrage- und Antwort-Header deiner Website
- HTTP-Antwort-Inhalte deiner Website
- Verbindungsdaten zur aufgelösten IP-Adresse deiner Website

Deaktivieren der Kontrollkästchen verhindert, dass zugehörige Daten an die Uptrends Plattform gesendet werden. Stattdessen wird eine Mitteilung mit dem Hinweis angezeigt, dass solche Daten aufgrund der Datenschutzrichtlinien deines Unternehmens nicht erfasst wurden.

![Deaktivierter MSA Datenschutz](/img/content/scr-data-protection-disabled-checkbox.min.png)

## Verwandte Artikel

Weitere Informationen zu Datenschutz bei Private Locations findest du [in diesem Knowledge-Base-Artikel]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}).
