{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operator-Gruppen.",
  "url": "/support/kb/api/monitorgroup-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorgroup-api"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Prüfobjektgruppen (Monitor Groups). Weitere Informationen findest du unter [Uptrends Monitor Group API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorGroup).

## MonitorGroup Objektbeschreibung

Das folgende MonitorGroup Objekt wird an den MonitorGroupAPI Endpunkten verwendet:

| Name               | Beschreibung                                                                         | Datentyp |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| `MonitorGroupGuid` | Die einzigartige Kennung der Prüfobjektgruppe.                                       | String |
| `Description`  | Der Name der Prüfobjektgruppe.                                              | String |
| `IsAll`            | {{< tableformatter >}} 
Gibt an, ob die Prüfobjektgruppe die Standardgruppe [Alle Prüfobjekte]({{< ref path="/support/kb/api/monitorgroup-api#all-monitors-group" lang="de" >}})
 ist. {{< /tableformatter >}} | Boolean  |
| `IsQuotaUnlimited` | Zeigt an, ob die Anzahl Credits für die Prüfobjektgruppe begrenzt ist.  |  Boolean  |
| `UsedBasicMonitorQuota` |{{< tableformatter >}} 
Gibt die Anzahl genutzter Credits für [Uptime-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}) aus. {{< /tableformatter >}} | Integer |
| `UsedBrowserMonitorQuota`            | {{< tableformatter >}} 
Gibt die Anzahl genutzter Credits für [Browser-(Full-Page Check)-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}) aus. {{< /tableformatter >}} | Integer |
| `UsedTransactionMonitorQuota`            | {{< tableformatter >}}
Gibt die Anzahl genutzter Credits für [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) aus.  {{< /tableformatter >}} | Integer |
| `UsedApiMonitorQuota`            | {{< tableformatter >}} 
Gibt die Anzahl genutzter Credits für [Multi-Step API (MSA)-]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) und [Postman-]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="de" >}})Prüfobjekte aus. {{< /tableformatter >}} | Integer |
| `UsedClassicQuota`            | Gibt die Anzahl an Credits aus, die von bestehenden Accounts verwendet wird, die eine Preisstufe für Credits nutzen. | Integer |

### Die Gruppe „Alle Prüfobjekte“

Die Gruppe **Alle Prüfobjekte** ist eine Prüfobjekt- oder Systemgruppe, die standardmäßig all deine Prüfobjekte enthält. Verwende die Guid dieser Gruppe, um Operationen zu verwalten, die alle Prüfobjekte betreffen, zum Beispiel den Start oder das Pausieren aller Prüfobjekte oder Alarme.
Beachte, dass du nicht die Mitglieder dieser Gruppe ändern kannst.


## Endpunkte zum Management einer Prüfobjektgruppe

Die folgenden API-Endpunkte sind zum Erstellen, Ändern und Entfernen von Prüfobjektgruppen sowie den Prüfobjekten in diesen Gruppen verfügbar.

| Abfragetyp | Endpunkt                                                 | Verwendung                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | `/MonitorGroup`                                          | Ruft alle Prüfobjektgruppen ab                                        |
| POST         | `/MonitorGroup`                                          | Erstellt eine neue Prüfobjektgruppe                                    |
| GET          | `/MonitorGroup/{monitorGroupGuid}`                       | Ruft die Informationen über eine Prüfobjektgruppe ab                            |
| PUT          | `/MonitorGroup/{monitorGroupGuid}`                       | Aktualisiert eine bestehende Prüfobjektgruppe                              |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}`                       | Löscht eine Prüfobjektgruppe                                        |
| GET          | `/MonitorGroup/{monitorGroupGuid}/Members`               | Ruft eine Liste aller Prüfobjekte ab, die Mitglied einer Prüfobjektgruppe sind |
| POST         | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Fügt ein bestimmtes Prüfobjekt der Prüfobjektgruppe hinzu                |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Entfernt das angegebene Prüfobjekt aus der Prüfobjektgruppe           |

## Weitere Operationen bei Prüfobjektgruppen

Die folgenden API-Endpunkte sind verfügbar, um Operationen bei allen einer Gruppe zugeordneten Prüfobjekten durchzuführen:

| Abfragetyp | Endpunkt                                                 | Verwendung                                                          |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitors`                  | Stoppt alle Prüfobjekte in der angegebenen Prüfobjektgruppe                           |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitors`                 | Startet alle Prüfobjekte in der angegebenen Prüfobjektgruppe                          |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitorAlerts`             | Stoppt  Alarmierungen für alle Prüfobjekte in der angegebenen Prüfobjektgruppe              |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitorAlerts`            | Startet Alarmierungen für alle Prüfobjekte in der angegebenen Prüfobjektgruppe             |
| POST         | `/MonitorGroup/{monitorGroupGuid}/AddMaintenancePeriodToAllMembers` | Fügt den angegebenen Wartungszeitraum zu allen Prüfobjekten in der angegebenen Gruppe |
