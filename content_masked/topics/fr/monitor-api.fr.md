{
  "hero": {
    "title": "API Moniteur"
  },
  "title": "API Moniteur",
  "url": "[URL_BASE_TOPICS]api/api-moniteur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les endpoints (points d'entrée) qui font partie de l'API Moniteur vous aident à gérer vos paramètres de moniteur dans Uptrends. Les moniteurs dans Uptrends définissent ce qui doit être surveillé. En règle générale, un moniteur vérifie une seule page web, ou une séquence d'appels d'API, ou un chemin de clic d'utilisateur final dans un site web.

L'API Moniteur a plusieurs endpoints qui vous permettent de créer, modifier, cloner ou supprimer des définitions de moniteur. Ces endpoints sont décrits ci-dessous.

## Getting started

### Pour commencer

-   Pour accéder à l'API, vous devez disposer d'un compte API.
-   Vous pouvez découvrir/essayer les endpoints de l'API Moniteur dans notre [environnement Swagger]([LINK_URL_1]).
-   Chaque méthode API est décrite ci-dessous.
-   Pour la plupart de ces méthodes, vous travaillerez avec un objet moniteur qui contient les paramètres d'un moniteur. La description des paramètres et des champs se trouvent dans l'article [objet moniteur]([LINK_URL_2]).

## GET /Monitor

Renvoie la liste des moniteurs actuellement présents dans le compte.

[INLINE_CODE_1]

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

[INLINE_CODE_2]

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

Met à jour la définition du moniteur spécifié. Le corps de la requête doit contenir une liste partielle des champs que vous souhaitez mettre à jour. Vous utiliserez généralement cette requête pour mettre à jour un ou plusieurs champs. Dans le corps de la requête, mettez uniquement les champs que vous souhaitez mettre à jour. Le champ [INLINE_CODE_3] est facultative. Si vous le spécifiez, il doit correspondre au MonitorGuid que vous spécifiez dans l'URL.

La requête PATCH suivante est utilisée pour désactiver un moniteur, en spécifiant une nouvelle valeur pour son champ [INLINE_CODE_4].

[INLINE_CODE_5]

Corps de la réponse :

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "IsActive": false
    }

## PUT /Monitor/{monitorGuid}

Met à jour la définition du moniteur spécifié. Le corps de la requête doit contenir la liste complète de tous les champs du moniteur. Vous effectuerez généralement une requête GET d'abord pour obtenir la définition existante du moniteur que vous souhaitez mettre à jour, vous apportez les modifications nécessaires dans ce contenu et ensuite vous le renvoyez à l'aide de cette demande PUT.

La demande PUT suivante est utilisée pour modifier les champs Name et [INLINE_CODE_6]du moniteur, mais les autres champs doivent également être répertoriés, car nous faisons une demande PUT, pas une demande PATCH partielle.

[INLINE_CODE_7]

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

[INLINE_CODE_8]

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
    "Url": "[URL_1]
    }

## DELETE /Monitor/{monitorGuid}

Supprime le moniteur spécifié.

[INLINE_CODE_9]

## POST /Monitor/{monitorGuid}/Clone

Crée un clone (un double) du moniteur spécifié. Le moniteur copié sera initialement inactif, vous pouvez donc apporter des modifications avant de l'activer.

### Paramètres facultatifs

-   **includeMaintenancePeriods**: true ou false (par défaut : true). Indique s'il faut copier ou non les périodes de maintenance existantes du moniteur source dans le clone.
-   **includeMonitorGroups**: true ou false (par défaut : true). Indique s'il faut ou non copier les appartenances aux groupes de moniteurs dans le clone. Si true est spécifié, la nouvelle copie fera partie des mêmes groupes de moniteurs que le moniteur source. Si false est spécifié, il ne fera partie que du groupe *All monitors*.

La requête POST suivante crée une copie d'un moniteur existant et spécifie que les périodes de maintenance ne doivent pas être copiées à partir de la source, mais que le nouveau moniteur doit faire partie des mêmes groupes de moniteurs.

[INLINE_CODE_10]

## Autres API liés aux moniteurs

-   Si les données de moniteur (c'est-à-dire des données de vérification produites par un moniteur) vous intéressent, veuillez consulter l'[API MonitorCheck]([LINK_URL_3]).
-   Les moniteurs peuvent être organisés en groupes. Regardez l'API [MonitorGroup]([LINK_URL_4]).
-   Les moniteurs ont des horaires de marche/arrêt automatisés appelés *périodes de maintenance*. Regardez l'[API des Périodes de maintenance]([LINK_URL_5]).
