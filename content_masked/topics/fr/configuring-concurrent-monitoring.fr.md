{
  "hero": {
    "title": "Configuration de la surveillance simultanée"
  },
  "title": "Configuration de la surveillance simultanée",
  "summary": "Un guide sur comment configurer la surveillance simultanée dans Uptrends.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/surveillance-simultanee/configuration-surveillance-simultanee",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

La surveillance simultanée vous permet de configurer vos moniteurs de manière à ce qu'ils effectuent plusieurs vérifications en même temps, à partir de plusieurs points de contrôle. Cela signifie que vous pouvez recueillir rapidement et de manière fiable des informations concernant la disponibilité de votre site web à partir de plusieurs emplacements. Chaque type de moniteur peut être configuré comme un moniteur de Surveillance simultanée. La configuration de la surveillance simultanée est pratiquement la même que celle de la surveillance standard, avec quelques différences majeures et quelques réserves à garder à l'esprit. Pour plus d'informations sur le fonctionnement de la surveillance simultanée, consultez [cet article]([LINK_URL_1]).  
  
Vous pouvez créer de nouveaux moniteurs de surveillances simultanées, mais il est également possible d'activer la fonction de surveillance simultanée pour les moniteurs existants. L'activation de la surveillance simultanée fonctionne de la même manière dans les deux cas.

## Mise en place de la surveillance simultanée

1.  Activer la surveillance simultanée. Dans l'onglet [SHORTCODE_3]Principal[SHORTCODE_4] de la fenêtre de paramétrage d'un moniteur existant ou de création d'un nouveau moniteur, vous trouverez la case à cocher **Surveillance simultanée**. Activez l'option en cliquant sur le bouton radio correspondant.
2.  Deux nouveaux champs apparaissent : **Seuil d'erreur non confirmé** et **Seuil d'erreur confirmé**. Ces seuils représentent le pourcentage de points de contrôle qui peuvent détecter une erreur avant que le résultat global de la surveillance ne soit répertorié comme *non confirmé* ou *confirmé* respectivement. Les erreurs fonctionnent légèrement différemment pour la surveillance simultanée - [voir cet article pour une description complète]([LINK_URL_2]). Nous avons rempli les cases avec des valeurs par défaut, mais vous pouvez les modifier si nécessaire. Gardez à l'esprit que le seuil d'erreur non confirmé doit toujours être inférieur ou égal au seuil d'erreur confirmé.  
      
    ![]([LINK_URL_3])
3.  Ensuite il faut revoir les paramètres de vos points de contrôle. Dans l'onglet [SHORTCODE_5]Checkpoints[SHORTCODE_6] , sélectionnez les points de contrôle qui exécuteront la vérification simultanément. Nous autoriserons un maximum de 50 points de contrôle pour tout moniteur de Surveillance simultanée. [SHORTCODE_1]**Remarque :** En ce qui concerne la sélection des points de contrôle, vous avez 2 options qui seront présentées dans l'écran de sélection des points de contrôle:
    1.  La première option consiste à disposer de tous les points de contrôle. Dans ce cas, vous devez sélectionner un minimum de 5 points de contrôle.
    2.  La seconde option est de n'utiliser que des points de contrôle *à haute disponibilité*. Cet ensemble limité de points de contrôle a une disponibilité accrue, puisque nous exploitons plusieurs serveurs sur ces sites. Cela élimine pratiquement le risque qu'en raison d'un entretien ou d'un temps d'arrêt, un ou plusieurs emplacements ne soient pas disponibles pour les contrôles simultanés. C'est important car, si un emplacement devait disparaître, cela pourrait affecter vos règles d'alerte de surveillance simultanée. Lorsque vous choisissez d'utiliser un ensemble de points de contrôle *à haute disponibilité*, le nombre minimum de points de contrôle est de 3.[SHORTCODE_2] 
4.  Si vous créez un nouveau moniteur, n'oubliez pas de remplir les autres champs obligatoires, en fonction du type de moniteur sélectionné. Cliquez sur [SHORTCODE_7]Enregistrer[SHORTCODE_8] en bas à gauche de la fenêtre pour enregistrer le moniteur.  
      
    Le moniteur devrait immédiatement commencer à produire des résultats. Nous avons quelques informations supplémentaires sur [comment interpréter vos résultats de surveillance simultanée ici]([LINK_URL_4]).

## Ce qu'il faut garder à l'esprit

-   Lorsque vous fixez vos seuils d'erreur (non) confirmée, gardez à l'esprit le nombre de points de contrôle sélectionnés. Utiliser des valeurs de 40 % et 50 % respectivement n'a pas de sens si vous n'avez sélectionné que 3 points de contrôle, car il ne sera pas possible d'obtenir un taux d'erreur de 40-50 % avec une telle configuration.
-   Les moniteurs de surveillance simultanée ne suivent pas le [schéma régulier]([LINK_URL_5]) d'erreurs de *Ok - Non confirmé - Confirmé*. En raison des seuils d'erreur, un moniteur peut passer directement de *Ok à Confirmé*. La mesure sera plus robuste, car toute erreur aura été confirmée depuis plusieurs emplacements simultanément.
-   Lorsque vous mettez en place une surveillance simultanée, pensez que le coût d'une surveillance simultanée est basé sur le nombre total de points de contrôle sélectionnés. Par exemple, si vous effectuez une transaction de 4 crédits sur 3 points de contrôle à haute disponibilité, le coût total sera de 4x3=12. Le coût total du moniteur est affiché à côté de son nom dans la fenêtre [Moniteurs]([LINK_URL_6]).
