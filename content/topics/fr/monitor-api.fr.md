{
  "hero": {
    "title": "API Moniteur"
  },
  "title": "API Moniteur",
  "url": "/support/kb/api/api-moniteur",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitor-api"
}

Les endpoints (points d'entrée) qui font partie de l'API Moniteur vous aident à gérer vos paramètres de moniteur dans Uptrends. Les moniteurs dans Uptrends définissent ce qui doit être surveillé. En règle générale, un moniteur vérifie une seule page web, ou une séquence d'appels d'API, ou un chemin de clic d'utilisateur final dans un site web.

L'API Moniteur a plusieurs endpoints qui vous permettent de créer, modifier, cloner ou supprimer des définitions de moniteur. Ces endpoints sont décrits ci-dessous.

## Getting started

### Pour commencer

-   Pour accéder à l'API, vous devez disposer d'un compte API.
-   Vous pouvez découvrir/essayer les endpoints de l'API Moniteur dans notre [environnement Swagger](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor).
-   Chaque méthode API est décrite ci-dessous.
-   Pour la plupart de ces méthodes, vous travaillerez avec un objet moniteur qui contient les paramètres d'un moniteur. La description des paramètres et des champs se trouvent dans l'article [objet moniteur](/support/kb/api/les-champs-de-api-moniteur).

## GET /Monitor

Renvoie la liste des moniteurs actuellement présents dans le compte.

`GET /Monitor`

Corps de la réponse :

    [
    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // D'autres champs ici
    },
    // D'autres moniteurs ici
    ]

## GET /Monitor/{monitorGuid}

Renvoie un seul moniteur, identifié par le monitorGuid.

`GET /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Corps de la réponse :

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // D'autres champs ici
    }

## PATCH /Monitor/{monitorGuid}

Met à jour la définition du moniteur spécifié. Le corps de la requête doit contenir une liste partielle des champs que vous souhaitez mettre à jour. Vous utiliserez généralement cette requête pour mettre à jour un ou plusieurs champs. Dans le corps de la requête, mettez uniquement les champs que vous souhaitez mettre à jour. Le champ `MonitorGuid` est facultative. Si vous le spécifiez, il doit correspondre au MonitorGuid que vous spécifiez dans l'URL.

La requête PATCH suivante est utilisée pour désactiver un moniteur, en spécifiant une nouvelle valeur pour son champ `IsActive`.

`PATCH /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Corps de la réponse :

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "IsActive": false
    }

## PUT /Monitor/{monitorGuid}

Met à jour la définition du moniteur spécifié. Le corps de la requête doit contenir la liste complète de tous les champs du moniteur. Vous effectuerez généralement une requête GET d'abord pour obtenir la définition existante du moniteur que vous souhaitez mettre à jour, vous apportez les modifications nécessaires dans ce contenu et ensuite vous le renvoyez à l'aide de cette demande PUT.

La demande PUT suivante est utilisée pour modifier les champs Name et `IsActive`du moniteur, mais les autres champs doivent également être répertoriés, car nous faisons une demande PUT, pas une demande PATCH partielle.

`PUT /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Corps de la réponse :

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts product page",
    "IsActive": false,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // Remaining fields here    
    }

## POST /Monitor

Crée un nouveau moniteur. Le corps de la requête devrait contenir la liste complète de tous les champs de moniteur pour le type de moniteur que vous créez.

La toute première fois, il peut être utile de créer d'abord un moniteur dans l'application Uptrends, de récupérer la définition de ce moniteur à l'aide d'une demande GET et d'inspecter la structure de cette définition de moniteur en tant qu’exemple.

La requête POST suivante est utilisée pour créer un moniteur HTTPS de base qui s'exécute sur des points de contrôle en Europe :

`POST /Monitor`

Corps de la réponse :

    {
    "Name": "My new monitor",
    "IsActive": true,
    "GenerateAlert": true,
    "IsLocked": false,
    "CheckInterval": 5,
    "MonitorMode": "Production",
    "CustomFields": [],
    "SelectedCheckpoints": {
        "Regions": [
        1004
        ]
    },
    "UsePrimaryCheckpointsOnly": true,
    "MonitorType": "Https",
    "Notes": "Monitors uptime for the homepage",
    "AlertOnLoadTimeLimit1": true,
    "LoadTimeLimit1": 2500,
    "AlertOnLoadTimeLimit2": true,
    "LoadTimeLimit2": 5000,
    "RequestHeaders": [],
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
    "Username": "",
    "AuthenticationType": "None",
    "CheckCertificateErrors": true,
    "IpVersion": "IpV4",
    "AlertOnMinimumBytes": false,
    "MinimumBytes": 0,
    "HttpMethod": "Get",
    "CheckHttpStatusCode": false,
    "ExpectedHttpStatusCode": 401,
    "TlsVersion": "Tls12_Tls11_Tls10",
    "RequestBody": "",
    "Url": "https://galacticresorts.com"
    }

## DELETE /Monitor/{monitorGuid}

Supprime le moniteur spécifié.

`DELETE /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

## POST /Monitor/{monitorGuid}/Clone

Crée un clone (un double) du moniteur spécifié. Le moniteur copié sera initialement inactif, vous pouvez donc apporter des modifications avant de l'activer.

### Paramètres facultatifs

-   **includeMaintenancePeriods**: true ou false (par défaut : true). Indique s'il faut copier ou non les périodes de maintenance existantes du moniteur source dans le clone.
-   **includeMonitorGroups**: true ou false (par défaut : true). Indique s'il faut ou non copier les appartenances aux groupes de moniteurs dans le clone. Si true est spécifié, la nouvelle copie fera partie des mêmes groupes de moniteurs que le moniteur source. Si false est spécifié, il ne fera partie que du groupe *All monitors*.

La requête POST suivante crée une copie d'un moniteur existant et spécifie que les périodes de maintenance ne doivent pas être copiées à partir de la source, mais que le nouveau moniteur doit faire partie des mêmes groupes de moniteurs.

`POST /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e/Clone?includeMaintenancePeriods=false&includeMonitorGroups=true`

## Autres API liés aux moniteurs

-   Si les données de moniteur (c'est-à-dire des données de vérification produites par un moniteur) vous intéressent, veuillez consulter l'[API MonitorCheck](/support/kb/api/monitorcheck-api).
-   Les moniteurs peuvent être organisés en groupes. Regardez l'API [MonitorGroup](/support/kb/api/monitorgroup-api).
-   Les moniteurs ont des horaires de marche/arrêt automatisés appelés *périodes de maintenance*. Regardez l'[API des Périodes de maintenance](/support/kb/api/periodes-de-maintenance-dans-api).
