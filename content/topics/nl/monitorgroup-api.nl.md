{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "De beschikbare API-methodes voor het manipuleren van controleregelgroepen.",
  "url": "/support/kb/api/monitorgroup-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorgroup-api"
}

Deze pagina beschrijft de beschikbare API-methodes voor het manipuleren van controleregelgroepen. Raadpleeg [Uptrends Controleregelgroep API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorGroup) voor meer informatie.

## Beschrijving van het MonitorGroup-object

Het volgende MonitorGroup-object wordt gebruikt in de MonitorGroupAPI-eindpunten:

| Naam               | Beschrijving                                                                         | Datatype |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| `MonitorGroupGuid` | De unieke identificatie voor de controleregelgroep.                                       | Tekenreeks |
| `Description`      | De naam van de controleregelgroep.                                              | Tekenreeks |
| `IsAll`            | {{< tableformatter >}} 
Geeft aan of de controleregelgroep de standaard [Alle controleregels]({{< ref path="/support/kb/api/monitorgroup-api#all-monitors-group" lang="nl" >}})-groep is. {{< /tableformatter >}} | Booleaans  |
| `IsQuotaUnlimited` | Geeft aan of het aantal credits voor de controleregelgroep onbeperkt is of niet.  |  Booleaans  |
| `UsedBasicMonitorQuota` |{{< tableformatter >}} 
Retourneert het aantal credits dat is gebruikt voor [Uptimecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}}). {{< /tableformatter >}} | Geheel getal |
| `UsedBrowserMonitorQuota`            | {{< tableformatter >}} 
Retourneert het aantal credits dat is gebruikt voor [Browsercontroleregels (Full-Page Check)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="nl" >}}). {{< /tableformatter >}} | Geheel getal |
| `UsedTransactionMonitorQuota`            | {{< tableformatter >}}
Retourneert het aantal credits dat is gebruikt voor [Transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}).  {{< /tableformatter >}} | Geheel getal |
| `UsedApiMonitorQuota`            | {{< tableformatter >}} 
Retourneert het aantal credits dat is gebruikt voor [Multi-step API (MSA)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) en [Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="nl" >}})-controleregels. {{< /tableformatter >}} | Geheel getal |
| `UsedClassicQuota`            | Retourneert het aantal credits dat wordt gebruikt door bestaande accounts die één creditprijstarief gebruiken. | Geheel getal |

### De groep Alle controleregels

De groep **Alle controleregels** is een controleregel- of systeemgroep die standaard al uw controleregels bevat. Gebruik de Guid van deze groep om bewerkingen te beheren die van invloed zijn op alle controleregels, zoals het starten of stoppen van alle controleregels of alerts.
Merk op dat u het lidmaatschap van deze groep niet kunt wijzigen.


## Eindpunten voor controleregelgroepbeheer

De volgende API-eindpunten zijn beschikbaar voor het maken, wijzigen en verwijderen van controleregelgroepen, evenals de controleregels binnen die groepen.

| Requesttype | Eindpunt                                                 | Gebruik                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | `/MonitorGroup`                                          | Verkrijgt alle controleregelgroepen                                        |
| POST         | `/MonitorGroup`                                          | Creëert een nieuwe controleregelgroep                                    |
| GET          | `/MonitorGroup/{monitorGroupGuid}`                       | Verkrijgt de details van een controleregelgroep                            |
| PUT          | `/MonitorGroup/{monitorGroupGuid}`                       | Werkt een bestaande controleregelgroep bij                              |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}`                       | Verwijdert een controleregelgroep                                        |
| GET          | `/MonitorGroup/{monitorGroupGuid}/Members`               | Verkrijgt een lijst met alle controleregels die lid zijn van een controleregelgroep |
| POST         | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Voegt de gespecificeerde controleregel toe aan de controleregelgroep                |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Verwijdert de gespecificeerde controleregel uit de controleregelgroep           |

## Extra controleregelgroepbewerkingen

De volgende API-eindpunten zijn beschikbaar voor het uitvoeren van bewerkingen op alle controleregels in een groep:

| Requesttype | Eindpunt                                                            | Gebruik                                                                       |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitors`                  | Stopt alle controleregels in de gespecificeerde controleregelgroep                           |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitors`                 | Start alle controleregels in de gespecificeerde controleregelgroep                          |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitorAlerts`             | Stopt alerting voor alle controleregels in de gespecificeerde controleregelgroep              |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitorAlerts`            | Start alerting voor alle controleregels in de gespecificeerde controleregelgroep             |
| POST         | `/MonitorGroup/{monitorGroupGuid}/AddMaintenancePeriodToAllMembers` | Voegt de verstrekte onderhoudsperiode toe aan alle controleregels in de gespecificeerde groep |
