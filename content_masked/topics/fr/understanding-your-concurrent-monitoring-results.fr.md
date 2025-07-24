{
  "hero": {
    "title": "Comprendre les résultats de la surveillance simultanée"
  },
  "title": "Comprendre les résultats de la surveillance simultanée",
  "summary": "Cet article vous indique où trouver les résultats de la surveillance simultanée et comment les interpréter.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/surveillance-simultanee/comprendre-resultats-surveillance-simultanee",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les résultats des vérifications sont interprétés différemment d'une surveillance simultanée ou d'une surveillance standard. Plusieurs aspects des résultats des vérifications simultanées diffèrent de ceux de la surveillance standard. Un résultat de vérification simultanée se compose de plusieurs vérifications individuelles, chacune ayant ses propres métriques et résultats. Dans cet article, nous allons voir comment interpréter les détails des résultats pour tirer le meilleur parti de vos moniteurs de surveillance simultanée. Si vous cherchez à mettre en place une surveillance simultanée, lisez notre article sur [la configuration de la surveillance simultanée]([LINK_URL_1]).

## Emplacement des résultats de la surveillance simultanée

Dans le journal des moniteurs, vous pouvez repérer les résultats des vérifications de surveillance simultanée au moyen de l'icône ![]([LINK_URL_2]). Ces résultats n'indiquent pas de checkpoint dans la colonne **Checkpoint**, mais la mention *Plusieurs emplacements*. Par ailleurs, chaque moniteur de surveillance simultanée dispose de son propre dashboard, qui affiche les informations pertinentes le concernant. Pour accéder au dashboard d'un moniteur de surveillance simultanée, survolez l'infobulle qui apparaît lorsque vous survolez un résultat de vérification de moniteur et cliquez sur le lien *Dashboard*.

![]([LINK_URL_3])

## Interprétation des résultats de la surveillance simultanée

Pour consulter toutes les vérifications d'un moniteur, il suffit de cliquer sur sa ligne dans le journal des moniteurs.

![capture d'écran des détails d'un moniteur de surveillance simultanée]([LINK_URL_4])

Comme vous pouvez le voir, la fenêtre contextuelle détaillée énumère les checkpoints qui ont effectué les vérifications. La métrique **Temps de chargement** est la moyenne des temps de chargement issus des vérifications individuelles faites par chaque checkpoint. La ligne **Résultat** correspond à l'ensemble des vérifications. Si elles remplissent les conditions définies dans les paramètres du moniteur, la ligne présente le code de résultat *0 - OK*. Dans le cas contraire, elle signale une erreur. Les erreurs fonctionnent légèrement différemment pour la surveillance simultanée. [Vous trouverez plus d'informations à ce sujet dans cet article]([LINK_URL_5]).

Si vous souhaitez en savoir plus sur les mesures individuelles effectuées pour arriver à ce résultat global, vous pouvez trouver les détails des mesures individuelles en cliquant sur les noms des checkpoints. Par exemple, si nous cliquons sur *Birmingham - 2* dans la capture d'écran précédente, nous voyons les résultats détaillés des vérifications qui ont été faites à partir du checkpoint Birmingham - 2.

![capture d'écran montrant les mesures détaillées d'un checkpoint avec la surveillance simultanée]([LINK_URL_6])

Cette fenêtre contient des informations telles que la [ventilation de la durée totale]([LINK_URL_7]) de la vérification faite à partir de ce checkpoint spécifique. Il contient également un lien qui vous ramènera à l'ensemble du contrôle ( *Voir tous les tests*).

## Affichage des vérifications individuelles dans le journal des moniteurs

Par défaut, le journal des moniteurs n'affiche que l'ensemble des vérifications. Pour trouver les détails des différentes mesures, il faut passer par la fenêtre contextuelle comme décrit précédemment. Toutefois, vous pouvez configurer votre journal des moniteurs pour afficher à la fois l'ensemble des vérifications et chaque vérification individuelle. Pour ce faire, réglez le filtre du dashboard en haut à droite sur *Afficher les contrôles partiels*.![]([LINK_URL_8])

Vous pouvez également cliquer sur l'icône de la roue dentée en haut à droite de la tuile du journal des moniteurs (vous devrez peut-être passer la souris sur la tuile pour que cette icône n'apparaisse), et cocher l'option **Afficher les contrôles partiels**. Enregistrez la configuration en cliquant sur le bouton [SHORTCODE_1]Définir[SHORTCODE_2] en bas à droite de la fenêtre.

![]([LINK_URL_9])

Comme vous pouvez le voir, le journal des moniteurs contient maintenant à la fois l'ensemble des vérifications (comme indiqué par l'icône ![]([LINK_URL_10])), qui indique *plusieurs emplacements*, et chaque vérification individuelle avec son checkpoint respectif. Les mêmes informations sont affichées dans les tuiles de ventilation des erreurs.
