{
  "hero": {
    "title": "Périodes de maintenance dans l'API"
  },
  "title": "Périodes de maintenance dans l'API",
  "url": "/support/kb/api/periodes-de-maintenance-dans-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/maintenance-periods"
}

Il existe un ensemble spécifique de méthodes API permettant de manipuler les périodes de maintenance d'un moniteur ou de tous les moniteurs d'un groupe de moniteurs.

## Description de l'objet Période de Maintenance

L'objet suivant MaintenancePeriod est utilisé dans les méthodes API décrites ci-dessous :

| Nom               | Description                                                                                                                                                              | Type données     |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `Id`              | L'identifiant unique pour cette période de maintenance                                                                                                                   | Integer          |
| `ScheduleMode`    | OneTime, Daily, Weekly or Monthly                                                                                                                                        | Enum             |
| `StartDateTime`   | Une date et une heure de début (applicable uniquement à une période planifiée ponctuelle)                                                                                | DateTime         |
| `EndDateTime`     | La date et l'heure de fin d'une période de maintenance planifiée ponctuelle                                                                                              | DateTime         |
| `StartTime`       | L’heure de début ("HH:mm", notation 24 heures) pour une période de maintenance récurrente (Daily, Weekly ou Monthly)                                                     | String (“HH:mm”) |
| `EndTime`         | L’heure de fin ("HH:mm", notation 24 heures) pour une période de maintenance récurrente (Daily, Weekly ou Monthly)                                                       | String (“HH:mm”) |
| `WeekDay`         | Le jour de la semaine pour une période de maintenance hebdomadaire (Sunday/Monday/\[…\]/Saturday)                                                                        | Enum             |
| `MonthDay`        | Le numéro du jour pour une période de maintenance mensuelle                                                                                                              | Int (1-31)       |
| `MaintenanceType` | DisableMonitoring (pour désactiver complètement le moniteur) ou DisableNotifications (la surveillance aura toujours lieu, mais les notifications ne seront pas envoyées) | Enum             |

Quand une période de maintenance est retournée via l'API, toutes les propriétés seront présentes, mais en fonction de la ScheduleMode, certains champs liés aux dates ou heures de début et de fin ne seront pas utilisés.

Pour une période de maintenance ponctuelle, nous devons connaître les dates *et* heures de début et de fin, donc le StartDateTime et EndDateTime propriétés seront utilisées. Pour les périodes de maintenance récurrentes, les champs heure de début et de fin sont pertinents et, en fonction du type de la planification, les propriétésWeekDay ou MonthDay.

Par exemple, un planning quotidien ressemblerait à ceci :

    {
    "Id": 123, 
    "ScheduleMode": "Daily", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

Les propriétés qui ne sont pas pertinentes pour ce type de planification (DateTime, WeekDay et MonthDay) sont laissées de côté.

Un planning hebdomadaire ressemblerait à ceci :

    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

Un planning mensuel ressemblerait à ceci :

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Un planning ponctuel ressemblerait à ceci :

    {
    "Id": 124, 
    "ScheduleMode": "OneTime", 
    "StartDateTime": "2018-09-24T22:00",
    "EndDateTime": "2018-09-24T22:00", 
    "MaintenanceType": "DisableMonitoring" 
    }

## Les endpoints d'une période de maintenance

Les endpoints API suivants sont disponibles :

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th>Type de requête</th><th>Endpoint</th><th>Utilisation</th></tr></thead><tbody><tr class="odd"><td>GET</td><td><code>Monitor/{monitorGuid}/MaintenancePeriod</code></td><td>Trouve toutes les périodes de maintenance pour un moniteur.</td></tr><tr class="even"><td>POST</td><td><code>Monitor/{monitorGuid}/MaintenancePeriod</code></td><td>Enregistre la nouvelle période de maintenance fournie pour le moniteur spécifié</td></tr><tr class="odd"><td>PUT</td><td><code>Monitor/{monitorGuid}/MaintenancePeriod/</code><br />
<code>{maintenancePeriodId}</code></td><td>Met à jour le planning de maintenance spécifié pour le moniteur spécifié</td></tr><tr class="even"><td>DELETE</td><td><code>Monitor/{monitorGuid}/MaintenancePeriod/</code><br />
<code>{maintenancePeriodId}</code></td><td>Supprime la période de maintenance spécifiée du moniteur spécifié</td></tr><tr class="odd"><td>POST</td><td><code>Monitor/{monitorGuid}/MaintenancePeriod/</code><br />
<code>Cleanup/{beforeDate}</code></td><td>Efface toutes les périodes de maintenance ponctuelles du moniteur spécifié, antérieures à la date spécifiée.</td></tr><tr class="even"><td>POST</td><td><code>MonitorGroup/{monitorGroupGuid}/</code><br />
<code>MaintenancePeriod</code></td><td>Ajoute la période de maintenance fournie à tous les moniteurs du groupe spécifié</td></tr></tbody></table>

### GET Monitor

`GET Monitor/{monitorGuid}/MaintenancePeriod`

Cette requête GET retournera une collection contenant toutes les périodes de maintenance planifiées pour le moniteur avec le GUID fourni.

Exemple de retour :

    [
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }, 
    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
    ]

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod`

Cette méthode créera la période de maintenance fournie dans le corps de la requête et l'attribuera au moniteur dont le GUID est fourni.

Une requête POST attend une structure d'objet telle que fournie dans les exemples de la rubrique « Description de l'objet Période de Maintenance ». Comme indiqué, la structure dépend du type de la période de maintenance (OneTime, Daily, Weekly ou Monthly). De plus, le champ Id ne doit pas être fourni. Une nouvelle valeur d'identifiant sera générée automatiquement.

### PUT Monitor

`PUT Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Cette méthode met à jour la période de maintenance dont l'Id est fourni, avec les valeurs fournies dans le corps de la demande.

Valeurs attendues (exemple pour une période de maintenance mensuelle) :

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Notez bien que l'identifiant de la période de maintenance doit être fourni dans le corps ainsi que dans le paramètre maintenancePeriodId. Si l'identifiant dans le paramètre ne correspond pas à l'identifiant de la période de maintenance dans le corps de la demande, une exception sera retournée.

### DELETE Monitor

`DELETE Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Cette méthode supprimera la période de maintenance, dont l’identifiant est spécifié dans maintenancePeriodId, du moniteur identifié par le monitorGuidfourni.

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate}`

Cette méthode supprimera toute planification **ponctuelle,** dont le StartDateTime est antérieur à la date indiquée dans beforeDate, du moniteur identifié par le monitorGuid fourni.

### POST MonitorGroup

`POST MonitorGroup/{monitorGroupGuid}/MaintenancePeriod`

Cette méthode ajoute la période de maintenance fournie dans le corps de la demande à tous les moniteurs du groupe de moniteurs identifié par le Guid fourni.

Valeurs attendues (exemple pour une période de maintenance hebdomadaire :

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
