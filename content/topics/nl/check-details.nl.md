{
  "hero": {
    "title": "Details van de controle"
  },
  "title": "Details van de controle",
  "summary": "De resultaten van een controleregelcheck worden gepresenteerd in de details van de controle. De beschikbare informatie is afhankelijk van het controleregeltype.",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/details-van-de-controle",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/check-details"
}

De informatie die rond een controleregelcheck wordt verzameld, wordt weergegeven in zogenaamde "details van de controle". Deze bestaan uit de basisinformatie of de controle goed is verlopen (OK) of dat er een fout is gedetecteerd (op basis van uw [Foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}})). Meer gedetailleerde informatie over de controle zelf en het resultaat is ook aanwezig en kan u helpen bij het oplossen van de oorzaak van een fout.

## Wat is opgenomen in de details van de controle?

De informatie in de details van de controle is sterk afhankelijk van het controleregeltype. Het kan zo eenvoudig zijn als een statuscode voor een HTTP(S)-controleregel. Complexere controleregels kunnen screenshots bevatten voor een Full Page Check of resultaten voor elke stap in een transactie- of Multi-step API-controleregel, zie de twee voorbeelden hieronder.

Details van de controle ("OK") voor een HTTPS-controleregel:

![screenshot details van de controle https-controleregel](/img/content/scr_check-details-https-monitor.min.png)

Details van de controle voor een transactiecontroleregel die een fout heeft geretourneerd:

![screenshot details van de controle transactiecontroleregel](/img/content/scr_check-details-transaction-monitor-041024.min.png)

## Waar vindt u de details van de controle?

De details van de controle zijn beschikbaar op verschillende plaatsen.

Als u een controleregelcheck uitvoert met de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}} krijgt u een pop-up met de details van de controle.

Verschillende dashboards hebben een lijst met controles. Als u op een individuele fout of controle klikt, worden de details van de controle weergegeven. U kunt de fouten of controles hier vinden:

- Dashboard in {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Fouten overzicht {{< /AppElement >}} 
- Dashboard in {{< AppElement type="menuitem" >}} Monitoring > Statusdetails {{< /AppElement >}} 
- Dashboard in {{< AppElement type="menuitem" >}} Monitoring > Controleregel log {{< /AppElement >}} 
- Tegel *Details Laatste controle*, een [aangepaste rapporttegel]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#last-check-details" lang="nl" >}}) die u kunt toevoegen aan uw [aangepaste dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-dashboards" lang="nl" >}})
