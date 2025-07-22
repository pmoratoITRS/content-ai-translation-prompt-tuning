{
  "hero": {
    "title": "Interprétation des résultats du rapport en cascade"
  },
  "title": "Interprétation des résultats du rapport en cascade",
  "summary": "Maintenant que vous avez ouvert le rapport, nous allons apprendre comment interpréter les résultats.",
  "url": "/support/kb/surveillance-synthetique/resultats-surveillance/interpretation-des-resultats-du-rapport-en-cascade",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/interpreting-the-results-of-the-waterfall-report"
}

Une fois le rapport en cascade ouvert (voir [Ouverture du rapport en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart#where-is-the-waterfall-chart-located" lang="fr" >}})), vous verrez une grande quantité de données concernant votre page et ses éléments. Chaque élément de la page nécessite une requête, une connexion TCP, un HTTPS « handshake », un « send », un temps d'attente et un temps de réception. Une fois le temps de réception terminé, le navigateur traite l'élément. Une seule page peut contenir une centaine d'éléments ou plus que le navigateur doit traiter. Les temps de chargement cumulés de tous les éléments, ou simplement des temps de réponse longs de quelques éléments, peut faire en sorte que le temps de chargement maximal prévu pour votre page soit dépassé. Comme vous pouvez le voir dans l'exemple ci-dessous, ce FPC a dépassé le temps de charge maximal de 2,5 secondes.

L'en-tête du rapport donne des informations générales sur ce contrôle, dont le point de contrôle utilisé, l'URL et le navigateur utilisé pour le test. Vous remarquerez que la cause de l'erreur est indiquée par l'intitulé **Résultat**. Ce test en particulier a échoué en raison du dépassement du temps de charge maximale avec le code d'erreur 6000. Vous trouverez des explications sur les autres codes possibles sur la page [Error Types](/support/kb/alerter/erreurs/types-erreurs).

![](/img/content/3125b678-4eb5-43fd-a50d-d2c1b2da3e0e.jpg)

## Alors quoi exactement a causé l'erreur ?

En faisant défiler la page, vous verrez la liste des éléments de la page. Le rapport énumère les éléments de la page dans l'ordre où ils se chargent dans le navigateur. Certains éléments chargent de manière asynchrone et d'autres éléments ont des dépendances qui font qu'ils ne chargent pas avant que d'autres éléments aient fini de charger. A droite de chaque élément, vous voyez un graphique à barres. Chaque bande de couleur sur le graphique à barres représente un état de connexion différent. Le placement des éléments de manière chronologique donne la perspective d'une cascade. Les bandes de couleur indiquent le temps que prend chaque élément à charger. En balayant le rapport, vous pouvez voir rapidement les éléments de la page que le navigateur a mis le plus de temps à recevoir.

Dans cet exemple, plusieurs « handshakes » (indiqués en or) ont mis trop de temps à se terminer. Parmi les éléments à l'origine des « handshakes » et des temps d'attente excessifs se trouvent une application analytique tiers et une demande très peu réactive pour un fichier JavaScript. Même si ces fichiers ont été les plus longues, en regardant le reste du rapport, vous remarquerez d'autres éléments qui ont des « handshakes » et des temps d'attente qui, bien que plus courts, peuvent, en s'additionnant, affecter votre temps total de chargement.

![](/img/content/2fc286e2-26d2-4b40-96f8-462734d4c509.png)

## Affichage des en-têtes de requête et de réponse

Les en-têtes de requête et de réponse vous donnent l'historique complète. Un regard sur les en-têtes de requête et de réponse vous permet de voir exactement ce que le navigateur a demandé et le résultat de la demande. Pour ouvrir les en-têtes de requête et de réponse pour un élément, cliquez sur le symbole "\+" à droite du nom de l'élément dans la liste. Dans l'exemple ci-dessous, le navigateur demande un fichier JavaScript, mais la demande a donné lieu à un « handshake » et un temps de réponse très longs.

![](/img/content/68f3ff2b-15a3-4f5d-b1be-233bd9ca55e2.png)

## Résumé du rapport

Au bas du rapport en cascade, vous pouvez voir le résumé du rapport. La première colonne contient la légende des couleurs pour les barres de couleur du graphique en cascade. Au milieu vous pouvez voir le temps total et le temps moyen pour chacun des états de connexion. Le reste du pied de page vous donne le compte des éléments par type et le nombre total des pages.

![](/img/content/eed630d9-4882-441f-a303-8bdc9fefbfc1.png)

## Trouver la source de l'élément avec les groupes de domaine 

Si votre moniteur est de type FPC \+, vous pouvez voir rapidement la source de vos éléments à problèmes.

1.  Gardez en tête le numéro de l'élément du graphique en cascade que vous voulez examiner.
2.  Cliquez sur le bouton « Domains Group » (Groupe de Domaines) en haut à droite de la cascade.  
    ![](/img/content/97c81084-da4f-4099-b53f-e4bbd90bcc6a.png)  
      
3.  Repérez le numéro de l'élément dans la liste pour voir le groupe de domaine.  
    ![](/img/content/7213b1fb-861b-4b93-b85a-d03085b191a2.png)
