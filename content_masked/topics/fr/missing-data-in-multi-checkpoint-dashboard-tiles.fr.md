{
  "hero": {
    "title": "Données manquantes dans les tuiles multi-checkpoint"
  },
  "title": "Données manquantes dans les tuiles multi-checkpoint",
  "summary": "Apprenez pourquoi des fois vous n'aurez pas de données ou de données incomplètes dans les tuiles de votre tableaux de bord qui affichent les résultats pour plusieurs points de contrôle.",
  "url": "[URL_BASE_TOPICS]dashboards-et-rapports/dashboards/donnees-manquantes-dans-les-tuiles-multi-checkpoint",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Nos listes de données et diagrammes Multi-Checkpoint affichent certaines métriques en fonction des points de contrôle utilisés pour les tests. Ces tuiles de données sont idéales pour identifier les problèmes de latence et d’autres problèmes régionaux. Parfois il arrive qu'il y a des données manquantes ou incomplètes dans ces tuiles. Ce phénomène peut avoir plusieurs causes différentes.

## Les sélections de points de contrôle pour moniteurs et pour tableaux de bord sont en conflit

Lors de la configuration de votre moniteur, vous avez sélectionné les points de contrôle que vous souhaitez utiliser pour le moniteur ; de plus, en haut de chaque tableau de bord, vous avez la possibilité de sélectionner les points de contrôle utilisés pour l'affichage des données du tableau de bord. Si les points de contrôle sélectionnés pour le ou les moniteur(s) ne sont pas inclus dans la sélection des points de contrôle du tableau de bord, vous allez obtenir soit un ensemble de données incomplet, soit pas de données du tout. Modifiez la sélection des points de contrôle du tableau de bord pour inclure le ou les moniteurs sélectionnés pour la tuile.

Si ce n'est pas le cas, il se peut que vous ayez trop de points de contrôle sélectionnés pour la tuile (continuez à lire).

[SHORTCODE_1]
**Remarque :** Vous ne verrez pas non plus de données dans la liste Multi-checkpoint pour les points de contrôle utilisés par le moniteur que vous n'avez pas inclus dans le tableau de bord.
[SHORTCODE_2]

## Trop de points de contrôle du tableau de bord sélectionnés lors de l’utilisation d'un diagramme Multi-checkpoint.

Par défaut, le tableau de bord affiche les données pour tous les points de contrôle, mais la tuile avec le diagramme Multi-checkpoint ne peut afficher que dix points de contrôle à la fois. Si vous laissez le tableau de bord par défaut ou si vous avez sélectionné un grand nombre de points de contrôle et que votre moniteur n'en utilise que quelques-uns, vous ne verrez peut-être aucune donnée ou bien vous ne verrez des données que pour quelques points de contrôle. La tuile affiche les dix premiers points de contrôle en fonction de la sélection des points de contrôle du tableau de bord et affiche les données pour ces points de contrôle. S'il n'y a pas de données pour les 10 premiers points de contrôle, vous verrez le message "Aucune donnée disponible". Si, par hasard, un ou plusieurs points de contrôle sélectionnés pour votre moniteur font partie des 10 premiers points de contrôle sélectionnés pour le tableau de bord, vous verrez des données pour ces points de contrôle tout comme pour les autres points de contrôle - même s'il n'y a pas de données correspondantes. Pour voir toutes les données de cette tuile, vous devez ajuster la sélection des points de contrôle du tableau de bord de manière à refléter les points de contrôle utilisés par le moniteur (jusqu'à dix points de contrôle).
