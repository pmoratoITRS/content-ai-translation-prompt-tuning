{
"hero": {
"title": "État des checkpoints"
},
"title": "État des checkpoints",
"summary": "À tout moment, vous pouvez vérifier l'état des checkpoints de vos emplacements privés. Uptrends vous indique si tout fonctionne bien ou si une action de votre part est nécessaire.",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/etat-checkpoints-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-checkpoint-health"
}

Pour effectuer la surveillance, les checkpoints de vos [emplacements privés]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}) doivent fonctionner correctement. L'onglet {{< AppElement type="tab" >}} Santé du point de contrôle {{< /AppElement >}} contient des informations sur les principaux aspects qui peuvent influer sur le fonctionnement du checkpoint. Ces informations concernent notamment le logiciel installé ainsi que des métriques spécifiques à l'hôte. Le présent article vous en dit plus sur les informations disponibles.

## Où puis-je trouver les informations sur l'état du checkpoint ?

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Dans la liste des emplacements privés, affichez l'emplacement dont vous souhaitez vérifier le checkpoint.
3. Cliquez sur le checkpoint et sélectionnez l'onglet {{< AppElement type="tab" >}} Santé du point de contrôle {{< /AppElement >}}.

![capture d'écran de l'onglet Santé du point de contrôle](/img/content/scr_private-location-checkpoint-health.min.png)

Cet onglet ne s'affiche qu'une fois le checkpoint correctement installé. Avant cela, seul l'onglet {{< AppElement type="tab" >}} Installation {{< /AppElement >}} est visible. Pour installer le checkpoint, suivez les instructions fournies dans l'article [Installer un checkpoint Docker]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="fr" >}}).

## Logiciel Uptrends

Cette section vous indique si le logiciel Uptrends a été installé correctement et si les différents services de surveillance sont opérationnels. Chaque composante de la section **Logiciel Uptrends** peut être active ou inactive. Toutes doivent être actives pour que le checkpoint puisse exécuter des tâches de surveillance.

Le conteneur de checkpoint sert à effectuer tous les contrôles qui ne sont pas basés sur un navigateur.
Le conteneur du processeur de transaction sert à effectuer les contrôles de type Real Browser Check ([Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) ou [moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}})).
Le conteneur de relais sert de relais de communication entre les autres conteneurs et les services cloud d'Uptrends.

Veuillez noter qu'Uptrends publie des images de conteneurs correspondant aux numéros de version, et ne teste que ces combinaisons. Il est déconseillé de tester des versions différentes.

## Navigateurs

Pour que le checkpoint fonctionne, les navigateurs que vous souhaitez utiliser pour les contrôles Real Browser Check ([Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) et [moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}})) doivent être installés.

Cette section vous indique les navigateurs installés et leurs versions. Vous pouvez ainsi vérifier qu'il s'agit des dernières versions.
Les images de conteneurs fournies par Uptrends contiennent les navigateurs les plus récents. Pensez à actualiser vos conteneurs aussi souvent que nécessaire.

## Détails de l'hôte

La machine (virtuelle) qui héberge votre checkpoint doit être en bon état et compter suffisamment de mémoire pour réaliser des tâches de surveillance.

Ces informations système vous permettent de vérifier l'absence de goulots d'étranglement.

## Configuration de l'hôte

Dans cette section, vous pourrez configurer plus en détail l'hôte des emplacements privés, comme les serveurs DNS, le fuseau horaire et les paramètres de langue.

## Paramètres de protection des données

Cette section indique si la protection des données est activée. La présence d'une coche verte signifie que les données s'affichent, et donc que la protection des données n'est pas activée. Pour en savoir plus sur l'application de la protection des données à vos checkpoints privés, lisez cet [article sur la protection des données]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}).

