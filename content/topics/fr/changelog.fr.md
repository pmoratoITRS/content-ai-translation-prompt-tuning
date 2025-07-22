{
"hero": {
"title": "Journal des modifications de l'API"
},
"title": "Journal des modifications de l'API",
"summary": "Découvrez les changements, les mises à jour et les améliorations de l'API d'Uptrends",
"url": "/support/kb/api/changelog",
"translationKey": "https://www.uptrends.com/support/kb/api/changelog",
"type": "story"
}

{{< Features/Story >}}

L'API d'Uptrends est améliorée et complétée au fil du temps. Selon les besoins relatifs aux fonctionnalités, nous ajoutons de nouveaux endpoints et de nouvelles méthodes.

Lors de l'ajout d'une nouvelle fonctionnalité, notre objectif est de rester compatible avec les versions antérieures. Cependant, des changements sont parfois inévitables et une nouvelle version de l'API peut ne pas être compatible avec ce que vous avez codé et utilisé jusqu'à présent. Pensez donc à vérifier régulièrement le journal des modifications de l'API pour rester au courant des changements et agir en conséquence si nécessaire.

Si vous voulez consulter la documentation de l'API, reportez-vous aux articles de la catégorie [API d'Uptrends]({{< ref path="support/kb/api" lang="fr" >}}).

De même, si vous souhaitez connaître les changements apportés à l'application Uptrends, consultez le [journal des modifications général]({{< ref path="changelog" lang="fr" >}}).

## Mai 2025

### Changement important à venir : retrait de champs d'API

Conformément à nos efforts continus pour optimiser l'API d'Uptrends, les champs suivants des endpoints [Monitor](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) seront retirés à compter du **27 août 2025** :

- `GET` et `POST` `/Monitor`
- `GET`, `PUT` et `PATCH` `/Monitor/{monitorGuid}`
- `GET` et `POST` `/Monitor/MonitorGroup/{monitorGroupGuid}`

Les champs suivants seront désormais traités comme des [types de conditions d'erreur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview" lang="fr" >}}) dans le tableau `ErrorConditions`. Les champs connexes seront fusionnés sous la forme d'une seule entrée qui remplacera leur fonction individuelle :

| Champs retirés | Nouveaux champs |
|--|--|
| `AlertOnLoadTimeLimit1`, `LoadTimeLimit1`| {{< tableformatter >}} [LoadTimeLimit1]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}}) |
| `AlertOnLoadTimeLimit2`, `LoadTimeLimit2` | [LoadTimeLimit2]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}}) |
|`AlertOnMaximumBytes`, `MaximumBytes` | [TotalMaxBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="fr" >}}) |
|`AlertOnMinimumBytes`, `MinimumBytes` | [TotalMinBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="fr" >}}) |
|`AlertOnMaximumSize`, `ElementMaximumSize` | [PageElementMaxSizeWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="fr" >}}) |
|`AlertOnPercentageFail`, `FailedObjectPercentage` | [PageElementFailedWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="fr" >}})
|`ExpectedHttpStatusCode`, `ExpectedHttpStatusCodeSpecified` | [HttpStatus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="fr" >}}) |

Voici un exemple de nouvelle réponse d'API. Nous vous recommandons de modifier vos appels d'API pour utiliser le tableau `ErrorConditions`. Vous utiliserez ainsi la structure d'API la plus récente, ce qui favorisera le bon fonctionnement de l'API.

```json
{
  ...
  "ErrorConditions": [
    {
      "ErrorConditionType": "LoadTimeLimit1",
      "Value": "2500",
      "Effect": "Indicate"
    },
    {
      "ErrorConditionType": "LoadTimeLimit2",
      "Value": "5000",
      "Effect": "Error"
    },
    {
      "ErrorConditionType": "TotalMaxBytes",
      "Value": "5000000"
    },
    {
      "ErrorConditionType": "TotalMinBytes",
      "Value": "5000"
    },
    {
      "ErrorConditionType": "PageElementMaxSizeWithPercentage",
      "Value": "200000",
      "Percentage": "10"
    },
    {
      "ErrorConditionType": "PageElementFailedWithPercentage",
      "Percentage": "10"
    },
    { "ErrorConditionType": "HttpStatus",       
      "Value": "200"     
    }
  ],
 ...
}
```

### Actualisation de l'endpoint Private Checkpoint Health

L'endpoint `GET /PrivateCheckpointHealth` renvoie désormais le champ `Warnings`, qui contient tous les avertissements liés au checkpoint du serveur. Pour en savoir plus, vous pouvez consulter la [documentation sur l'endpoint Private Location Checkpoint de l'API v4 d'Uptrends](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/PrivateLocation/PrivateLocation_GetSpecifiedPrivateCheckpointHealth).

## Avril 2025

### Ajout de nouveaux points de terminaison d'API pour les emplacements privés

Un nouvel ensemble d'endpoints d'API a été ajouté pour vous aider à gérer la configuration de vos emplacements privés, y compris les informations sur l'état de santé et les checkpoints. Pour en savoir plus, consultez la documentation de l'[API v4 d'Uptrends sur les emplacements privés](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json).

## Mars 2025

### Mise à jour de l'API Monitor Group

L'endpoint `/MonitorGroup` fournit désormais le nombre de crédits utilisés par [type de moniteur]({{< ref path="/support/kb/basics/monitor-types" lang="fr" >}}) :
- `UsedBasicMonitorQuota` : fournit le nombre de crédits utilisés par les [moniteurs de disponibilité et les moniteurs de base]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}).
- `UsedBrowserMonitorQuota` : fournit le nombre de crédits utilisés par les [moniteurs de navigateur et les moniteurs Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="fr" >}}).
- `UsedTransactionMonitorQuota` : fournit le nombre de crédits utilisés par les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}).
- `UsedApiMonitorQuota` : fournit le nombre de crédits utilisés par les [moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) et les [moniteurs utilisant Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="fr" >}}).

Auparavant, l'API MonitorGroup API fournissait uniquement le nombre total de crédits disponibles pour chaque catégorie de moniteur. Elle renvoie désormais le nombre de crédits utilisés par chaque catégorie de moniteur.

## Février 2025

### Nouveauté concernant la valeur du paramètre Cursor

Le paramètre Cursor de l'API est une valeur de chaîne qui fonctionne comme un curseur pour parcourir les données de la réponse de l'API.

Les curseurs se présentent désormais sous la forme d'une chaîne plus longue afin de renforcer la sécurité des données. Les nouveaux curseurs créés suivent ce nouveau format, et les anciens curseurs continueront de fonctionner jusqu'au 1er avril 2025. Après cette période, ils ne pourront plus être utilisés. Nous vous recommandons de créer de nouvelles valeurs de curseurs pour que vos curseurs fonctionnent correctement.

Notez que le paramètre Cursor est disponible dans les endpoints des commandes [Monitor Check]({{< ref path="/support/kb/api/monitorcheck-api" lang="fr" >}}) et Alert de l'API.

## Janvier 2025

### Mise à jour de l'API Monitor

L'endpoint `/Monitor` renvoie désormais la valeur `LastModifiedDate`, qui contient la date et l'heure de la dernière modification du moniteur. Auparavant, l'API Monitor renvoyait uniquement la valeur `CreatedDate`.

## Novembre 2024

### Mise à jour de l'endpoint VaultItem

Les endpoints `POST/v4/VaultItem`, `PUT/v4/VaultItem/{vaultItemGuid}` et `PATCH/v4/VaultItem/{vaultItemGuid}` acceptent désormais le champ `SecretEncodingMethod` lors de la modification ou de la création d'un élément de coffre-fort [Configuration du mot de passe à usage unique]({{< ref path="/support/kb/account/vault#one-time-password" lang="fr" >}}). Ce nouveau champ accepte les valeurs *Hex* ou *Base32*. Le format *Base32* est la méthode de codage sélectionnée par défaut si le champ `SecretEncodingMethod` n'est pas précisé.

## Septembre 2024

### Mise à jour de l'endpoint VaultItem

L'endpoint `GET /v4/VaultItem` fournit désormais une nouvelle donnée `VaultItemUsedBy`, qui précise quels éléments ou moniteurs utilisent chaque élément de coffre-fort.

## Août 2024

### API Checkpoint

L'endpoint de l'API `/Checkpoint/Server/{serverId}` fournit aussi désormais les serveurs des emplacements privés.

### Mise à jour de l'endpoint VaultItem

L'endpoint `GET /v4/VaultItem` est désormais capable de fournir le même niveau de détail pour chaque élément de coffre-fort, tout comme c'est le cas pour un seul élément avec l'endpoint `GET /v4/VaultItem/{GUID}`.

## Juin 2024

### Changement important : l'API /Register pour les opérateurs utilisant uniquement l'authentification unique

L'API d'Uptrends nécessite un [enregistrement]({{< ref path="/support/kb/api/authentication-v4" lang="fr" >}}) avant de pouvoir être utilisée. Les opérateurs peuvent créer un ensemble d'identifiants spécifiques à l'API d'après leurs identifiants Uptrends habituels. Il existe deux méthodes pour enregistrer les identifiants spécifiques à l'API :

- Les opérateurs peuvent utiliser l'interface d'Uptrends habituelle et ajouter un utilisateur d'API dans l'onglet {{< AppElement type="tab" >}}Gestion des API{{< /AppElement >}} de leurs paramètres d'opérateur.
- Autrement, les opérateurs peuvent aussi enregistrer leurs identifiants dans l'API elle-même, au moyen d'une requête `POST /Register` par laquelle ils fourniront leurs identifiants Uptrends habituels.

À ce jour, les opérateurs qui [se connectent uniquement au moyen de l'authentification unique]({{< ref path="/support/kb/account/settings/single-sign-on-overview" lang="fr" >}}) ne peuvent plus utiliser la deuxième méthode pour enregistrer leurs identifiants d'API. En effet, ces opérateurs ne possèdent pas d'identifiants Uptrends classiques.

Dans un tel cas, nous recommandons de créer un compte opérateur distinct et de l'utiliser pour enregistrer les identifiants de l'API.

## Octobre 2023

### Breaking change : métriques sur le chargement des pages pour la surveillance basée sur navigateur

**Remarque :** ce communiqué concerne un **breaking change** apporté à la commande *MonitorCheck* de l'API. Le changement sera implémenté le **mercredi 8 novembre**.

La commande [MonitorCheck de l'API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorCheck) permet de récupérer des informations détaillées sur les vérifications effectuées par les points de contrôle. Pour la surveillance basée sur navigateur, le [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) peut être récupéré par l'appel `GET /MonitorCheck/{monitorCheckId}/Waterfall`, qui récupère toutes les métriques du graphique en cascade, dont les indicateurs [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) et les [temps de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}), dès lors que ces éléments figurent dans les résultats de la recherche.

Actuellement, la commande MonitorCheck de l'API restitue les indicateurs Core Web Vitals et les temps de navigation du W3C dans deux objets JSON distincts : `PageLoadMetrics` et `W3CNavigationTiming`. À l'avenir, ces objets distincts seront combinés dans un seul tableau `PageLoadMetricsCollection`, comme dans l'exemple ci-dessous :

```json
  "Attributes": {
    "PageLoadMetricsCollection": [
      {
        "CumulativeLayoutShift": 0.029,
        "FirstContentfulPaint": 2914,
        "LargestContentfulPaint": 3014,
        "TotalBlockingTime": 819,
        "TimeToInteractive": 12516,
        "TimeToFirstByte": 2068,
        "SendStart": 2059,
        "LoadEventEnd": 6721,
        "DomInteractive": 2652,
        "DomComplete": 6719
      }
    ],
    ...
  }
```


### Spécifier les variables dans les définitions d'alertes au moyen de l'API

Lorsque des [alertes]({{< ref path="/support/kb/alerting" lang="fr" >}}) sont configurées au moyen d'une [intégration personnalisée]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="fr" >}}) dans Uptrends, les opérateurs peuvent utiliser l'interface pour spécifier certaines variables requises [dans le niveau d'escalade de la définition d'alerte]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#specifying-variables-per-escalation-level" lang="fr" >}}), plutôt que dans les options d'intégration. Ainsi, les utilisateurs peuvent utiliser une seule intégration pour différents scénarios, par exemple pour envoyer à différentes équipes des alertes sur différents ensembles de moniteurs, avec le même contenu dans le message.

Lorsque l'option permettant de spécifier des variables dans le niveau d'escalade est sélectionnée dans les paramètres d'intégration, la variable doit être configurée lors de la configuration de l'intégration pour pouvoir être utilisée dans les paramètres de la définition d'alerte. Pour cela, un champ textuel supplémentaire s'affiche dans la liste de sélection des intégrations, dans les paramètres liés aux définitions d'alerte.

Jusqu'à présent, cette option n'était pas proposée lors de la configuration des définitions d'alerte dans l'API. Nous avons ajouté une nouvelle option à la requête `/AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration` (qui vous permet de définir quelles intégrations sont liées à chaque niveau d'escalade dans la définition d'alerte). La nouvelle propriété sera la suivante :

```json
{
    ...
    "VariableValues": {
        "ApiUrl": "https://api.escalationlevel-specific-url.com/alerts"
    },
    ...
}
```

Cette propriété est l'équivalent de cette option dans l'interface de l'application :

![Configuration de la variable d'intégration dans la définition d'alerte](/img/content/scr-api-cl-conf-variables-in-escalation-level.min.png)


## Septembre 2023

### Changement lié aux adresses IPv6

Précédemment, lorsque vous utilisiez l'API Checkpoints pour récupérer des informations sur les points de contrôle, les adresses IPv4 des checkpoints s'affichaient sous la forme d'une liste simple dans un tableau, tandis que les adresses IPv6 (le cas échéant) étaient présentées sous la forme d'une liste d'objets. Par exemple, les adresses IP du checkpoint d'Amsterdam étaient présentées comme suit :

```json
     "Ipv4Addresses": [
        "178.217.84.4",
        "188.241.149.95",
        "66.212.22.2",
        "185.145.63.225",
        "5.182.210.227",
        "5.182.210.168"
    ],
    "IpV6Addresses": [
        {
            "IpAddress": "2a01:5cc0:1:2::4"
        },
        {
            "IpAddress": "2607:fcd0:cd40:1400::2"
        }
    ],
```

Uptrends a corrigé cette incohérence et fournit désormais les adresses IPv6 sous le même format :

```json
    "IpV6Addresses": [
        "2a01:5cc0:1:2::4",
        "2607:fcd0:cd40:1400::2",
    ],
```

Si vous avez automatisé la récupération des adresses IP des checkpoints (p. ex., pour établir une liste blanche), **ce changement pourrait avoir des conséquences pour vous**.

## Janvier 2023

La version 3 de l'API n'est plus disponible depuis janvier 2023. [Sa documentation]({{< ref path="/support/kb/api" lang="fr" >}}) reste accessible dans notre base de connaissances, mais l'API ne fonctionne plus. Si certains de vos scripts ou procédures utilisent toujours la version, ils ne sont plus fonctionnels. Nous vous recommandons de passer au plus vite à la version 4. Pour en savoir plus sur le passage de la version 3 à la version 4, consultez notre [guide dédié]({{< ref path="/support/kb/api" lang="fr" >}}).

**Mise à jour de mai 2023 :** La documentation de la version 3 de notre API a été retirée et n'est plus accessible.

## Décembre 2022

### Date de création du moniteur disponible via l'API

L'[endpoint /Monitor](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) peut être utilisé pour récupérer les définitions des moniteurs dans votre compte (via *GET /Monitor/{monitorGuid}*), entre autres informations. La réponse inclura désormais la valeur `CreatedDate`, qui indique la date de création du moniteur.


## Novembre 2022

### Légers changements apportés au endpoint /Register

Comme vous l'avez peut-être lu dans le [journal des changements récents d'Uptrends]({{< ref path="/changelog" lang="fr" >}}), cette version permet de [créer et supprimer les identifiants de l'API d'Uptrends directement depuis l'application Uptrends]({{< ref path="/changelog#2022-11-manage-uptrends-api-credentials-via-ui" lang="fr" >}}). Afin de faire correspondre la version 4 de l'API d'Uptrends et l'interface utilisateur, nous avons ajouté deux nouvelles options au endpoint /Register :

- Il est désormais possible d'ajouter une description lors de l'enregistrement d'un nouveau compte API, au moyen du champ `Description`.
- Lorsque l'opérateur émettant l'appel possède les droits requis, il est aussi possible de créer un compte API pour un autre opérateur au moyen du champ `operatorGuid`.

## Septembre 2022

### Changement à venir : horodatage dans la réponse de l'API

Actuellement, les horodatages inclus dans la réponse de tout appel d'[API v4]({{< ref path="/support/kb/api" lang="fr" >}}) sont convertis au format JSON selon l'une des méthodes suivantes :

- Le nombre de millisecondes est égal à 0 : _2022-09-21T13:08:47_
- Le nombre de millisecondes n'est pas égal à 0 : _2022-09-21T13:08:47<b>.682</b>_

Cette incohérence peut entraîner des problèmes lors de l'analyse et du traitement automatiques des données contenant ces horodatages. C'est pourquoi nous avons apporté ce changement : le nombre de millisecondes ne s'affichera plus dans les horodatages inclus dans la réponse de l'API. À l'avenir, tous les horodatages auront le format suivant : _2022-09-21T13:08:47_.

## Juin 2022

### Adresses IP à venir des checkpoints

Grâce à l'API d'Uptrends, vous pouvez récupérer les adresses IP des checkpoints afin d'automatiser la création d'une liste blanche. Auparavant, les réponses à ces requêtes adressées à notre [API Checkpoint](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Checkpoint) prenaient la forme d'une liste des adresses IP actuelles des points de contrôle. Cependant, le réseau de checkpoints d'Uptrends ne cesse d'évoluer. De nouveaux checkpoints sont ajoutés, des checkpoints existants sont déplacés ou retirés, ou des adresses IP sont modifiées. Autrement dit, la liste des adresses IP que vous utilisez pour constituer votre liste blanche risque de devenir obsolète jusqu'à la prochaine synchronisation, ce qui peut entraîner des erreurs.

Pour éviter cela, nous enregistrons désormais les adresses IP à venir et nous les incluons dans la réponse de l'API. Ainsi, votre liste blanche est actualisée à l'avance.

### Relations dans l'API Statistics

Les réponses de l'[API Statistics](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics) (qui permet de récupérer des données statistiques sur vos moniteurs ou groupes de moniteurs) vont désormais inclure des métadonnées concernant la réponse de l'API. Le tableau `Relationships` existe déjà pour d'autres endpoints de l'API. Il contient des informations supplémentaires sur la requête, comme un lien vers la requête de l'API Monitor ou MonitorGroup qui permet de récupérer des informations sur un moniteur ou un groupe de moniteurs.


```json
        "Relationships": [
            {
                "Id": "4c3a9529-7934-4978-9c36-c377b232g7hb",
                "Type": "Monitor",
                "Links": {
                    "Self": "/Monitor/4c3a9529-7934-4978-9c36-c377b232g7hb"
                }
            }  
        ]
```

## Mai 2022

### Correction des paramètres de début et de fin dans la commande Statistics de l'API

Notre API vous permet de récupérer les statistiques liées au moniteur grâce à la commande [Statistics](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics/Statistics_GetMonitorStatistics). Vous pouvez sélectionner une période prédéfinie pour la récupération des données (avec des valeurs telles que `Last24Hours`), ou personnaliser une période avec des paramètres d'URL désignant le début et la fin de la période. Par exemple, l'opération `GET /Statistics/Monitor/{monitorGuid}?Start=2022-04-08&End=2022-04-09` récupère les données statistiques d'un moniteur pour la période précisée.

Dans la version précédente, il y avait un problème avec l'indicateur des minutes dans les horaires de début et de fin, qui pouvait entraîner des résultats incomplets (voire vides) dans la réponse de l'API. Ce problème est désormais résolu.

## Février 2022

### Mise à jour de la commande Status de l'API

La commande [Status de l'API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Status/Status_GetMonitorStatus) récupère les informations sur le statut d'un moniteur donné d'après la dernière vérification du moniteur. Cet endpoint peut être utilisé pour obtenir des informations sur le statut actuel du moniteur. Nous avons modifié la réponse pour ajouter une valeur `TotalTime` (Temps total), qui fournit des informations sur les [mesures de temps total]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="fr" >}}) issues de la dernière vérification du moniteur.

## Janvier 2022

### Renvoi des données de moniteur correctes

Lorsqu'un opérateur non administrateur disposant de [l'autorisation **Afficher les données**]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}}) sur un certain moniteur récupérait cette définition de moniteur via l'API (via `GET /Monitor/{monitorGuid}`), la réponse n'incluait pas toutes les données pertinentes. C'était une erreur, car ces mêmes données étaient déjà disponibles via l'interface utilisateur mais pas l'API. Ce problème est maintenant corrigé. Désormais, lorsque ces opérateurs récupèrent un moniteur, la réponse inclut des valeurs pour *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive* et *GenerateAlert*.

## Août 2021

### Annonce : suppression prochaine de la version 3 de notre API

L'[API d'Uptrends]({{< ref path="support/kb/api" lang="fr" >}}) prend actuellement en charge deux versions côte à côte. La version 3 est l'ancienne version de notre API, et la version 4 est la version actuellement recommandée. Avec un ensemble de fonctionnalités beaucoup plus complet, la version 4 est au centre de notre développement depuis un certain temps. Nous avons donc décidé de déconseiller la version 3 de notre API, qui sera retirée et deviendra indisponible d'ici **décembre 2022**.

Pour les clients qui utilisent encore activement la version 3 de notre API, notez qu'elle restera disponible jusqu'à cette date. Cependant, nous vous recommandons de passer à la version 4 dès que possible. Pour vous aider, nous avons rédigé un [guide de mise à niveau de l'API v3 vers v4]({{< ref path="support/kb/api" lang="fr" >}}), qui couvrira les principales différences entre les deux versions de l'API et vous indiquera comment les intégrer dans vos scripts et logiciels.

## Juillet 2021

### Modification sans rétrocompatibilité : changements dans la réponse d'autorisation OperatorGroup

L'API d'Uptrends vous permet de gérer les [autorisations pour les opérateurs et les groupes d'opérateurs] ({{< ref path="support/kb/account/users/operators/permissions" lang="fr" >}}) en attribuant des rôles tels que **Administrateur**, **Opérateur financier**, ou en permettant un **Accès Infra**. La commande [OperatorGroup de l'API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/OperatorGroup) contient plusieurs options pour récupérer, ajouter ou supprimer de telles autorisations.

Nous avons modifié la manière dont les autorisations sont spécifiées pour les groupes d'opérateurs dans l'API, ce qui pourrait affecter toute action automatisée - création, suppression ou récupération d'informations - sur les autorisations de groupes d'opérateurs que vous avez configurées. Actuellement, la récupération d'informations sur les autorisations fonctionne avec une requête :

`GET /OperatorGroup/{operatorGroupGuid}/Authorization`

ce qui renvoie une réponse de cette nature (en fonction des autorisations configurées pour ce groupe d'opérateurs)

```json
[
      {
        "AuthorizationId": "{authIdGuid1}",
        "AuthorizationType": "FinancialOperator",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    {
        "AuthorizationId": "{authIdGuid2}",
        "AuthorizationType": "AllowInfra",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    ...
]
```

À l'avenir, cette même requête aura une réponse simplifiée, répertoriant simplement les autorisations accordées et aucune autre information. La réponse ne contiendra plus d'`operatorGroupGuid` ou d'`AuthorizationId` (ce dernier disparaîtra complètement, ce qui signifie que les autorisations n'auront plus de GUID individuel attribué). Elle ressemblera à ceci :

```json
{
    "FinancialOperator",
    "AllowInfra",
    ...
}
```

L'ajout d'une nouvelle autorisation de groupe d'opérateurs se fait actuellement en envoyant une requête POST à :

`/OperatorGroup/{operatorGroupGuid}/Authorization`
avec un corps de requête spécifiant un "AuthorizationType". Les valeurs actuellement disponibles pour AuthorizationType pour les groupes d'opérateurs sont disponibles dans [l'interface utilisateur Swagger de l'API d'Uptrends](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/), dans la section **Models** (en bas), puis **OperatorGroupAuthorizationType**.

À l'avenir, de nouvelles autorisations peuvent être ajoutées à un groupe d'opérateurs en envoyant une requête POST à :

`/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}`
sans inclure un corps de requête.

La suppression d'une autorisation d'un groupe d'opérateurs se fait actuellement en envoyant une requête DELETE à `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationGuid}`, mais comme indiqué ci-dessus, "authorizationGuid" disparaîtra entièrement en tant qu'entité et ne pourra plus être utilisé. À la place, vous pourrez supprimer des autorisations en vous y référant directement par leur nom dans l'URL de la requête : `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}`

## Février 2021

### Modification sans rétrocompatibilité : valeurs sensibles dans les moniteurs d'API multi-étapes

Notre [type de moniteur API multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="fr" >}}) vous permet d'exécuter plusieurs requêtes HTTP consécutives, où chaque nouvelle requête utilise des données récupérées d'une requête précédente pour effectuer sa tâche. Souvent, l'une des étapes va consister à présenter des justificatifs d'identité pour avoir accès à une ressource particulière. Dans le passé, ces informations d'identification étaient ajoutées à la définition du moniteur en tant que variables prédéfinies, puis marquées comme *sensibles*.

Afin d'améliorer la sécurité de la gestion de ces justificatifs, nous n'allons plus utiliser cette méthode. Au lieu de cela, les justificatifs seront placés dans le [coffre-fort]({{< ref path="support/kb/account/vault" lang="fr" >}}). Avec ce changement, l'option permettant de marquer des variables prédéfinies comme sensibles dans les moniteurs API multi-étapes devient obsolète et sera supprimée.

Cela modifiera la manière dont vous pourrez créer ou interagir avec les moniteurs API multi-étapes par le biais de notre API. Actuellement, la définition de moniteur pour ce type de moniteur contient un tableau "PredefinedVariables", où chacune des variables individuelles a une valeur booléenne vrai/faux "Sensitive". Dans un avenir proche, ce booléen sera supprimé de la définition. Si vous souhaitez créer ou mettre à jour un moniteur API multi-étapes existant dans votre compte par le biais de l'API d'Uptrends, ce champ ne doit plus apparaître.

### Changement : noms des chemins d'accès

Pour Uptrends APIv4, la manière de nommer les chemins n'est pas toujours cohérente. Dans la plupart des cas, le singulier est utilisé, mais parfois c'est le pluriel. L'itinéraire ne contient plus que du singulier,
par exemple, `/MonitorGroup/{monitorGroupGuid}/Member` plutôt que `/MonitorGroup/{monitorGroupGuid}/Members`.

Les anciens chemins fonctionneront toujours pour la compatibilité ascendante.

{{< /Features/Story >}}
