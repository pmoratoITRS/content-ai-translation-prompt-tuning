{
"hero": {
"title": "API MonitorGroup"
},
"title": "API MonitorGroup",
"summary": "Présentation des méthodes disponibles pour manipuler les groupes de moniteurs via l’API.",
"url": "/support/kb/api/monitorgroup-api",
"translationKey": "https://www.uptrends.com/support/kb/api/monitorgroup-api"
}

Cette page décrit les méthodes de l’API permettant de manipuler les groupes de moniteurs. Pour en savoir plus, consultez la [documentation de l'API MonitorGroup d'Uptrends](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorGroup).

## Description de l'objet MonitorGroup

L'objet MonitorGroup suivant est utilisé dans les points de terminaison de l'API MonitorGroup :

| Nom | Description | Type de données |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| `MonitorGroupGuid` | Identifiant unique du groupe de moniteurs | Chaîne |
| `Description` | Nom du groupe de moniteurs | Chaîne |
| `IsAll` | {{< tableformatter >}} |
Indique si le groupe de moniteurs correspond à l'option par défaut [Tous les moniteurs]({{< ref path="/support/kb/api/monitorgroup-api#all-monitors-group" lang="fr" >}}). {{< /tableformatter >}} | Booléen |
| `IsQuotaUnlimited` | Indique si le nombre de crédits pour le groupe de moniteurs est illimité ou non.  |  Booléen |
| `UsedBasicMonitorQuota` |{{< tableformatter >}}
Fournit le nombre de crédits utilisés par les [moniteurs de disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}). {{< /tableformatter >}} | Nombre entier |
| `UsedBrowserMonitorQuota`            | {{< tableformatter >}}
Fournit le nombre de crédits utilisés par les [moniteurs de navigateur (Full Page Check)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="fr" >}}). {{< /tableformatter >}} | Nombre entier |
| `UsedTransactionMonitorQuota`            | {{< tableformatter >}}
Fournit le nombre de crédits utilisés par les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}).  {{< /tableformatter >}} | Nombre entier |
| `UsedApiMonitorQuota`            | {{< tableformatter >}}
Fournit le nombre de crédits utilisés par les [moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) et les moniteurs [Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="fr" >}}). {{< /tableformatter >}} | Nombre entier |
| `UsedClassicQuota`            | Fournit le nombre de crédits utilisés par les comptes qui sont abonnés au forfait incluant une seule réserve de crédit. | Nombre entier |

### Groupe Tous les moniteurs

Le groupe **Tous les moniteurs** est un groupe de systèmes ou de moniteurs qui contient tous les moniteurs par défaut. Utilisez l'identifiant GUID de ce groupe pour gérer les opérations qui concernent tous les moniteurs. Par exemple, l'activation ou l'interruption de tous les moniteurs ou de toutes les alertes.
Notez que vous ne pouvez pas modifier la composition de ce groupe.


## Points de terminaison permettant de gérer le groupe de moniteurs

Les endpoints d'API suivants sont disponibles pour créer, modifier et supprimer des groupes de moniteurs, ainsi que les moniteurs qui font partie de ces groupes.

| Type de requête | Endpoint | Utilisation |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET | `/MonitorGroup` | Obtenir tous les groupes de moniteurs |
| POST | `/MonitorGroup` | Créer un nouveau groupe de moniteurs |
| GET | `/MonitorGroup/{monitorGroupGuid}` | Obtenir les détails d'un groupe de moniteurs |
| PUT | `/MonitorGroup/{monitorGroupGuid}` | Mettre à jour un groupe de moniteurs |
| DELETE | `/MonitorGroup/{monitorGroupGuid}` | Supprimer un groupe de moniteurs |
| GET | `/MonitorGroup/{monitorGroupGuid}/Members` | Obtenir une liste de tous les moniteurs faisant partie d'un groupe de moniteurs |
| POST | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Ajouter le moniteur spécifié à un groupe de moniteurs |
| DELETE | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Retirer le moniteur spécifié du groupe de moniteurs |

## Autres opérations liées aux groupes de moniteurs

Les endpoints d'API suivants permettent d'effectuer des opérations impliquant tous les moniteurs faisant partie d'un groupe :

| Type de requête | Endpoint | Utilisation |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitors` | Désactiver tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitors` | Activer tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitorAlerts` | Désactiver les alertes de tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitorAlerts` | Activer les alertes de tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | `/MonitorGroup/{monitorGroupGuid}/AddMaintenancePeriodToAllMembers` | Ajouter les périodes de maintenance indiquées à tous les moniteurs d'un groupe spécifié |
