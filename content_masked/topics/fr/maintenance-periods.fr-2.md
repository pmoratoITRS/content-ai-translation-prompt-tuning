{
  "hero": {
    "title": "Périodes de maintenance dans l'API"
  },
  "title": "Périodes de maintenance dans l'API",
  "url": "[URL_BASE_TOPICS]api/periodes-de-maintenance-dans-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Il existe un ensemble spécifique de méthodes API permettant de manipuler les périodes de maintenance d'un moniteur ou de tous les moniteurs d'un groupe de moniteurs.

## Description de l'objet Période de Maintenance

L'objet suivant MaintenancePeriod est utilisé dans les méthodes API décrites ci-dessous :

| Nom               | Description                                                                                                                                                              | Type données     |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [INLINE_CODE_1]              | L'identifiant unique pour cette période de maintenance                                                                                                                   | Integer          |
| [INLINE_CODE_2]    | OneTime, Daily, Weekly or Monthly                                                                                                                                        | Enum             |
| [INLINE_CODE_3]   | Une date et une heure de début (applicable uniquement à une période planifiée ponctuelle)                                                                                | DateTime         |
| [INLINE_CODE_4]     | La date et l'heure de fin d'une période de maintenance planifiée ponctuelle                                                                                              | DateTime         |
| [INLINE_CODE_5]       | L’heure de début ("HH:mm", notation 24 heures) pour une période de maintenance récurrente (Daily, Weekly ou Monthly)                                                     | String (“HH:mm”) |
| [INLINE_CODE_6]         | L’heure de fin ("HH:mm", notation 24 heures) pour une période de maintenance récurrente (Daily, Weekly ou Monthly)                                                       | String (“HH:mm”) |
| [INLINE_CODE_7]         | Le jour de la semaine pour une période de maintenance hebdomadaire (Sunday/Monday/\[…\]/Saturday)                                                                        | Enum             |
| [INLINE_CODE_8]        | Le numéro du jour pour une période de maintenance mensuelle                                                                                                              | Int (1-31)       |
| [INLINE_CODE_9] | DisableMonitoring (pour désactiver complètement le moniteur) ou DisableNotifications (la surveillance aura toujours lieu, mais les notifications ne seront pas envoyées) | Enum             |

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

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8][HTML_TAG_9]Type de requête[HTML_TAG_10][HTML_TAG_11]Endpoint[HTML_TAG_12][HTML_TAG_13]Utilisation[HTML_TAG_14][HTML_TAG_15][HTML_TAG_16][HTML_TAG_17][HTML_TAG_18][HTML_TAG_19]GET[HTML_TAG_20][HTML_TAG_21][HTML_TAG_22]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_23][HTML_TAG_24][HTML_TAG_25]Trouve toutes les périodes de maintenance pour un moniteur.[HTML_TAG_26][HTML_TAG_27][HTML_TAG_28][HTML_TAG_29]POST[HTML_TAG_30][HTML_TAG_31][HTML_TAG_32]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_33][HTML_TAG_34][HTML_TAG_35]Enregistre la nouvelle période de maintenance fournie pour le moniteur spécifié[HTML_TAG_36][HTML_TAG_37][HTML_TAG_38][HTML_TAG_39]PUT[HTML_TAG_40][HTML_TAG_41][HTML_TAG_42]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_43][HTML_TAG_44]
[HTML_TAG_45]{maintenancePeriodId}[HTML_TAG_46][HTML_TAG_47][HTML_TAG_48]Met à jour le planning de maintenance spécifié pour le moniteur spécifié[HTML_TAG_49][HTML_TAG_50][HTML_TAG_51][HTML_TAG_52]DELETE[HTML_TAG_53][HTML_TAG_54][HTML_TAG_55]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_56][HTML_TAG_57]
[HTML_TAG_58]{maintenancePeriodId}[HTML_TAG_59][HTML_TAG_60][HTML_TAG_61]Supprime la période de maintenance spécifiée du moniteur spécifié[HTML_TAG_62][HTML_TAG_63][HTML_TAG_64][HTML_TAG_65]POST[HTML_TAG_66][HTML_TAG_67][HTML_TAG_68]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_69][HTML_TAG_70]
[HTML_TAG_71]Cleanup/{beforeDate}[HTML_TAG_72][HTML_TAG_73][HTML_TAG_74]Efface toutes les périodes de maintenance ponctuelles du moniteur spécifié, antérieures à la date spécifiée.[HTML_TAG_75][HTML_TAG_76][HTML_TAG_77][HTML_TAG_78]POST[HTML_TAG_79][HTML_TAG_80][HTML_TAG_81]MonitorGroup/{monitorGroupGuid}/[HTML_TAG_82][HTML_TAG_83]
[HTML_TAG_84]MaintenancePeriod[HTML_TAG_85][HTML_TAG_86][HTML_TAG_87]Ajoute la période de maintenance fournie à tous les moniteurs du groupe spécifié[HTML_TAG_88][HTML_TAG_89][HTML_TAG_90][HTML_TAG_91]

### GET Monitor

[INLINE_CODE_10]

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

[INLINE_CODE_11]

Cette méthode créera la période de maintenance fournie dans le corps de la requête et l'attribuera au moniteur dont le GUID est fourni.

Une requête POST attend une structure d'objet telle que fournie dans les exemples de la rubrique « Description de l'objet Période de Maintenance ». Comme indiqué, la structure dépend du type de la période de maintenance (OneTime, Daily, Weekly ou Monthly). De plus, le champ Id ne doit pas être fourni. Une nouvelle valeur d'identifiant sera générée automatiquement.

### PUT Monitor

[INLINE_CODE_12]

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

[INLINE_CODE_13]

Cette méthode supprimera la période de maintenance, dont l’identifiant est spécifié dans maintenancePeriodId, du moniteur identifié par le monitorGuidfourni.

### POST Monitor

[INLINE_CODE_14]

Cette méthode supprimera toute planification **ponctuelle,** dont le StartDateTime est antérieur à la date indiquée dans beforeDate, du moniteur identifié par le monitorGuid fourni.

### POST MonitorGroup

[INLINE_CODE_15]

Cette méthode ajoute la période de maintenance fournie dans le corps de la demande à tous les moniteurs du groupe de moniteurs identifié par le Guid fourni.

Valeurs attendues (exemple pour une période de maintenance hebdomadaire :

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
