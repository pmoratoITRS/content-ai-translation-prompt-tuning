{
"hero": {
"title": "API Private locations"
},
"title": "API Private locations",
"summary": "Présentation des méthodes disponibles pour manipuler les emplacements privés via l'API.",
"url": "/support/kb/api/emplacements-prives-api",
"translationKey": "https://www.uptrends.com/support/kb/api/private-locations-api"
}

L'API Private locations inclut un ensemble d'endpoints qui fournissent des informations sur la santé et le statut opérationnel de vos emplacements privés. Ces endpoints vous permettent de surveiller la disponibilité, la performance et la connectivité de chaque point de contrôle.

## Endpoints Private Location Health et Private Checkpoint Health

La santé de l'emplacement privé et la santé du point de contrôle sont deux concepts liés et parfois interchangeables dans le contexte de l'API. L'endpoint `/PrivateCheckpointHealth` renvoie des informations sur la santé d'un checkpoint spécifique de votre emplacement privé. L'endpoint `/PrivateLocationHealth`, pour sa part, fournit une vue d'ensemble de l'état de santé de tous les checkpoints d'un emplacement privé. Ainsi, vous pouvez surveiller chaque checkpoint séparément ou connaître l'état de santé de tous les checkpoints.

## Endpoint Server Information

Cet endpoint d'API fournit des informations détaillées sur l'état de votre serveur :

- Healthy servers (Serveurs en bonne santé) : nombre de serveurs fonctionnels, sans erreur ni avertissement
- Unhealthy servers (Serveurs en mauvaise santé) : nombre de serveurs présentant des erreurs, des avertissements ou un problème de configuration
- Number of servers (Nombre de serveurs) : nombre total de serveurs exécutés sur un emplacement privé ou par un checkpoint spécifique
- Checkpoint name (Nom du checkpoint) : nom du checkpoint associé à l'emplacement privé
- Status (État) : état actuel de votre serveur : `Available`, `NotAvailable` ou `Maintenance`.
- Status details (Détails du statut) : date et heure de la dernière activité de votre serveur
- Warnings (Avertissements) : informations relatives aux avertissements, par exemple si le serveur nécessite une mise à jour, une installation ou une autre action

## Endpoint Authorization

Cet endpoint d'API vous permet de manipuler les autorisations des emplacements privés. Utilisez-le pour vérifier si votre type d'autorisation permet d'utiliser ou de modifier les emplacements privés. Pour en savoir plus sur les autorisations, vous pouvez lire l'article [Configuration des autorisations liées aux emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-permissions" lang="fr" >}}).

Pour en savoir plus, reportez-vous à l'[API Private Locations d'Uprends](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/PrivateLocation).