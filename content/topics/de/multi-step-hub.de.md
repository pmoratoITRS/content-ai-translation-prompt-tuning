{
  "hero": {
    "title": "Der Multi-Step API-Prüfobjekte-Hub"
  },
  "title": "Der Multi-Step API-Prüfobjekte-Hub",
  "summary": "Dein Ausgangspunkt, wenn du dir das Multi-Step API Monitoring näher ansehen möchtest.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-hub",
  "tableofcontents": false
}

Der **Multi-Step API (MSA) Hub** bietet einen allgemeinen Überblick über MSAs und deine MSA-Monitoring-Einrichtung. Um diese Seite zu öffnen, gehe zu {{< AppElement type="menuitem" >}} API > {{< /AppElement >}} [Entdecke das API Monitoring](https://app.uptrends.com/Hubs/Api). In der Seitenleiste findest du Links zu den zugehörigen Artikeln in der Knowledge Base.

![MSA Hub](/img/content/scr-msa-hub.min.png)

Die folgenden Bereiche zeigen deine API-Prüfobjekteinrichtung an:

- Die **API Prüfobjektkarten** geben die Anzahl deiner Prüfobjekteinrichtungen wieder. Klicken auf {{< AppElement type="buttonPrimary" >}} Alle API Prüfobjekte anzeigen {{< /AppElement >}} öffnet die Übersicht der API Prüfobjekte oder die {{< AppElement type="menuitem" >}}  API Prüfobjekteinrichtung {{< /AppElement >}}.

- Die Karte **API Prüfobjektstatus** zeigt die Anzahl der Prüfobjekte mit [bestätigten Fehlern]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}}) und aktiven Alarme. Klicken auf {{< AppElement type="buttonPrimary" >}} Prüfobjekt Status anzeigen {{< /AppElement >}} öffnet die Seite **Prüfobjektstatus**. Klicken auf {{< AppElement type="buttonPrimary" >}} Betrachte dauerhafte Alarme {{< /AppElement >}} öffnet die Seite **Aktuelle Alarmierungen**.

- Die Karte aktiver Prüfobjekte zeigt die API Prüfobjekte im [Staging- und Produktionsmodus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}).

- Die Karte API-Credits zeigt deine verfügbaren API-Credits. Um weitere Credits zu kaufen, lies den Artikel [Weitere Prüfobjekte und Credits hinzufügen]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="de" >}}).

Der Hub enthält auch eine Funktion, um automatisch deine bestehenden Prüfobjekte zu scannen und diejenigen zu identifizieren, die zu [API-Prüfobjekten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) umgewandelt werden können. Werden HTTP- oder HTTPS-Prüfobjekte erkannt, die einen API-Endpunkt zu überwachen scheinen, wird die Option angeboten, automatisch ein neues API-Prüfobjekt für dich zu erstellen.

Diese Funktion führt sofort ein Upgrade eines [Uptime-Prüfobjekts]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}) zu einem vollständig konfigurierten API-Prüfobjekt durch, ohne das ursprüngliche Prüfobjekt zu ändern oder zu löschen. Diese Aktion kann bei Bedarf jederzeit rückgängig gemacht werden. Es besteht zudem keine Notwendigkeit, alles von Grund auf nachzubilden. Uptrends übernimmt die komplette Einrichtung mit denselben Einstellungen des bestehenden Prüfobjekts.

Die Schaltfläche **Details ansehen** öffnet ein Pop-up, über das du deine bestehendes Prüfobjekt in ein API-Prüfobjekt umwandeln kannst. Sobald die Umwandlung beendet ist, erscheint ein weiteres Fenster. Hier kannst du die Konfiguration prüfen und das neu erstellte Prüfobjekt für den Einsatz aktivieren.