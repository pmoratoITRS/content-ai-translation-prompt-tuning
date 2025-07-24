{
  "hero": {
    "title": "Mise à jour d'un conteneur Docker"
  },
  "title": "Mise à jour d'un conteneur Docker",
  "summary": "Comment fonctionne la mise à jour d'un conteneur Docker pour les checkpoints des emplacements privés ?",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/points-de-controle/emplacements-prives/conteneurs-mise-a-jour-checkpoints-prives",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lorsque vous [installez un checkpoint géré par un utilisateur]([LINK_URL_1]), un script est créé, ainsi qu'une tâche qui met à jour le conteneur de checkpoints toutes les heures. Si vous avez besoin de réaliser une mise à jour en dehors de cette planification, une mise à jour manuelle est possible.

## Comment réaliser une mise à jour manuelle ?

Tout d'abord, assurez-vous que les étapes décrites dans l'article [Installer un checkpoint Docker]([LINK_URL_2]) ont été exécutées.

1. Ouvrez une console PowerShell **en mode admin**.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez les commandes suivantes.
3. Saisissez [INLINE_CODE_1] dans la ligne de commande.
4. Saisissez [INLINE_CODE_2] dans la ligne de commande.
5. Saisissez [INLINE_CODE_3] dans la ligne de commande.

Durant la mise à jour, les autres checkpoints privés assurent les vérifications. Il n'est pas nécessaire de désactiver le checkpoint en cours de mise à jour. Comme vous devez avoir au moins [une autre instance de checkpoint]([LINK_URL_3]) (conformément à nos recommandations), vous pouvez réaliser la mise à jour sans devoir effectuer d'autres changements tels que la désactivation des checkpoints, l'interruption des moniteurs, etc.

[SHORTCODE_1]
Il est important de tenir à jour vos conteneurs Docker. Les conteneurs possèdent un navigateur Chrome et Edge intégré qui doit être tenu à jour pour ne pas susciter de problème de sécurité.
Uptrends affiche un avertissement ou un message d'erreur si vos conteneurs sont considérés comme obsolètes.  
[SHORTCODE_2]
