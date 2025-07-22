{
  "title": "Im API-Hub Uptime-Prüfobjekte einfach in API-Prüfobjekte umwandeln",
  "date": "2025-04-24",
  "url": "/changelog/april-2025-api-vorschlaege",
  "translationKey": "https://www.uptrends.com/changelog/april-2025-api-suggestions"
}

Der [API-Hub](https://app.uptrends.com/Hubs/Api) enthält nun eine Funktion, die automatisch deine bestehenden Prüfobjekte scannt und diejenigen identifiziert, die zu [API-Prüfobjekten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) umgewandelt werden können. Werden HTTP- oder HTTPS-Prüfobjekte erkannt, die einen API-Endpunkt zu überwachen scheinen, wird die Option angeboten, automatisch ein neues API-Prüfobjekt für dich zu erstellen.

Diese Funktion führt sofort ein Upgrade eines [Uptime-Prüfobjekts]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}) zu einem vollständig konfigurierten API-Prüfobjekt durch, ohne das ursprüngliche Prüfobjekt zu ändern oder zu löschen. Diese Aktion kann bei Bedarf jederzeit rückgängig gemacht werden. Es besteht zudem keine Notwendigkeit, alles von Grund auf nachzubilden. Uptrends übernimmt die komplette Einrichtung mit denselben Einstellungen des bestehenden Prüfobjekts.

Nach der Umwandlung kannst du die Konfiguration überprüfen und aktivieren. Weitere Informationen findest du im Knowledge-Base-Artikel [Multi-Step API-Hub]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="de" >}}).

![Kachel API-Vorschläge](/img/content/scr-api-suggestions.min.png)