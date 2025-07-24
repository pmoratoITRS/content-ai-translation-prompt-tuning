{
  "hero": {
    "title": "Les effets du mode mise en scène sur les rapports et les données SLA"
  },
  "title": "Les effets du mode mise en scène sur les rapports et les données SLA",
  "summary": "When a monitor runs in Staging mode the data it generates affects your reporting in different ways.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/Les-effets-du-mode-mise-en-scene-sur-les-rapports-et-les-donnees-sla",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le mode mise en scène, comme nous l'avons expliqué dans l'article sur les [modes moniteur]([LINK_URL_1]), est un excellent moyen de tester vos moniteurs sans qu'ils n'affectent votre disponibilité ni vos données SLA. De plus, le mode mise en scène n'envoie pas d'alertes. Les moniteurs effectuent des mesures et fonctionnent comme n'importe quel autre moniteur en mode production, mais vous n'avez tout simplement pas à vous soucier des effets indésirables sur vos rapports. Voyons comment les moniteurs en mode mise en scène apparaissent dans vos rapports.

## Comment le mode mise en scène affecte-t-il mes tableaux de bord de Disponibilité et d'Erreurs ?

Lorsque vous sélectionnez une option dans le menu des tableaux de bord **Disponibilité** ou **Erreurs**, vous verrez les données de vos moniteurs en mode mise en scène, mais :

-   Les données collectées pour les moniteurs en mode mise en scène ne contribuent pas aux temps d'arrêt, aux nombre de vérifications, ni aux nombre d'erreurs; et,
-   Comme pour un moniteur désactivé, la disponibilité signalée est toujours égal à 100% pour la période pendant laquelle votre moniteur est dans ce mode.

## Comment le mode mise en scène affecte-t-il mes tableaux de bord des performances ?

Lorsque vous sélectionnez une option dans les tableaux de bord des performances, vous verrez que Uptrends inclut les mesures pour :

-   Resolve,
-   Connect,
-   Télécharger
-   Temps total.

## Comment le mode mise en scène affecte-t-il mon journal moniteur ?

Les résultats des vérifications de vos moniteurs en mode mise en scène apparaissent dans votre **journal moniteur**. Les vérifications effectuées en mode mise en scène sont indiqués par une icône en forme de flacon conique. 

## Comment le mode mise en scène affecte-t-il mes rapports SLA ?

Dans vos rapports SLA, un moniteur en mode mise en scène se comporte de la même manière qu'un moniteur désactivé, indiquant 100% de disponibilité, zéro erreurs confirmées et aucun temps d'arrêt. Les erreurs ou temps d'arrêt générés par un moniteur dans ce mode ne sont pas pris en compte dans les rapports SLA.
