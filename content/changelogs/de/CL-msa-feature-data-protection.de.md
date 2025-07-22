{
  "title": "Neue MSA-Funktion: Datenschutz",
  "date": "2024-12-18",
  "url": "/changelog/dezember-2024-msa-datenschutz-funktion",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-data-protection-feature"
}

Uptrends erfasst all deine MSA Monitoring-Ergebnisse der Checkpoint-Server, speichert diese direkt auf Uptrends Plattform und ruft sie von dort ab.

Mit der Funktion **Datenschutz** kannst du bestimmte Monitoring-Daten von der Sammlung und Speicherung auf der Uptrends Plattform ausschließen. Diese Funktion liefert eine zusätzliche Ebene der Sicherheit und sorgt dafür, dass sensible Daten deine Netzwerkumgebung nicht verlassen und nicht an extern übermittelt werden.

![Kontrollkästchen MSA Datenschutz](/img/content/scr-data-protection-checkbox.min.png)

Standardmäßig sind die folgenden Kontrollkästchen aktiviert und erlauben Uptrends, Daten im Rahmen deiner MSA Monitoring-Ergebnisse zu speichern und anzuzeigen:

– HTTP-Header sammeln – erfasst HTTP Request und Response Header deiner Website.
– Antwortinhalte sammeln – erfasst die HTTP Response-Inhalte deiner Website.
– Aufgelöste IP-Adresse sammeln – erfasst die aufgelöste IP-Adresse und Verbindungsdetails deiner Website.

Deaktivieren der Kontrollkästchen verhindert, dass zugehörige Daten an die Uptrends Plattform gesendet werden. Stattdessen wird ein Hinweis angezeigt.

Beachte bitte, dass die Funktion **Datenschutz** bereits für [Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}) verfügbar ist. Wir erweitern diese Funktion nun auf unser öffentliches Checkpoint-Netzwerk wie etwa für das MSA Monitoring.

