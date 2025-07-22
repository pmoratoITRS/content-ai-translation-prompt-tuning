{
  "hero": {
    "title": "Groupes de moniteurs"
  },
  "title": "Groupes de moniteurs",
  "summary": "Créez des groupes de moniteurs pour simplifier la configuration des alertes et des rapports.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/gestion-moniteurs/groupes-moniteurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les groupes de moniteurs vous aident à vous organiser et vous simplifient la tâche. Une fois que vous avez configuré vos groupes de moniteurs, vous pouvez plus rapidement et plus facilement [appliquer des modèles]([LINK_URL_1]), ajouter des moniteurs aux [définitions d'alerte]([LINK_URL_2]) et configurer les dashboards et les rapports.

## Configurer des groupes de moniteurs

À l'exception du groupe *Tous les moniteurs*, tous les autres groupes sont modifiables. Un moniteur peut appartenir à plusieurs groupes de moniteurs. Vous pouvez configurer vos groupes de moniteurs de différentes façons. Voici quelques exemples inspirés de ce que font les autres utilisateurs.

**Type de moniteur** : il peut être utile de configurer des groupes de moniteurs par [type de moniteur]([LINK_URL_3]) : moniteurs de performance de site web, moniteurs de performances mobiles, moniteurs de disponibilité, moniteurs d'API, moniteurs de transactions et moniteurs de certificats. Ce type de groupe est particulièrement utile pour configurer des rapports.

**Par emplacement** : si vous souhaitez obtenir vos rapports en fonction de l'emplacement géographique, il peut être intéressant de regrouper vos moniteurs par région ou pays. En règle générale, ces moniteurs partagent les mêmes checkpoints, ce qui facilite leur gestion à l'aide de modèles de moniteur.

**Par centre de données** : si vous avez des sites associés à différents centres de données, vous pouvez configurer des groupes en fonction du centre de données. Ainsi, vous pourrez rapidement vérifier les performances et la disponibilité en fonction du centre de données. Le regroupement par centre de données peut être utile pour configurer des périodes de maintenance à l'aide de modèles de moniteur.

**Par importance** : vous pouvez regrouper les moniteurs en fonction de l'importance du moniteur. Par exemple, la disponibilité de votre blog n'aura pas la même importance que votre page de connexion. Par conséquent, la configuration de groupes de moniteurs en fonction de l'importance de l'URL est une excellente façon d'organiser les moniteurs et de hiérarchiser vos rapports.

**Par domaine** : vous gérez peut-être plusieurs domaines ou sous-domaines. L'organisation basée sur le domaine facilite la gestion des niveaux des alertes.

**Par fonction** : plusieurs comptes regroupent leurs moniteurs selon la fonction de l'URL, tels que les pages de connexion, les pages d'accueil et les pages d'assistance.

## Vue d'ensemble des groupes de moniteurs

La page **Groupes de moniteurs** vous donne une vue d'ensemble de groupes de moniteurs configurés dans votre compte. Pour l'ouvrir, passez par le menu [SHORTCODE_1] Configuration de compte > Groupes de moniteurs [SHORTCODE_2].

![capture d'écran du dashboard groupes de moniteurs]([LINK_URL_4])

Cette page montre tous les groupes de moniteurs pour lesquels vous disposez au moins d'une *autorisation d'affichage*. Plusieurs [types d'autorisations]([LINK_URL_5]) sont disponibles pour les moniteurs et les groupes de moniteurs.

Le groupe *Tous les moniteurs* existe par défaut dans tout compte Uptrends. Il contient tous les moniteurs de votre compte et ne peut être modifié ni supprimé. Il peut être intéressant de créer un groupe similaire au groupe *Tous les moniteurs*. Ce groupe contiendra aussi (presque) tous les moniteurs, mais avec la possibilité de modifier les autorisations et de supprimer des moniteurs. Pour connaître la marche à suivre, lisez comment configurer un [groupe de moniteurs par défaut]([LINK_URL_6]).

La vue d'ensemble contient des informations sur les *moniteurs utilisés*, qui vous indiquent le nombre maximum de moniteurs (par type) configurés dans vos groupes de moniteurs. Vous pouvez aussi choisir d'autoriser un nombre illimité de moniteurs et de n'appliquer aucune limite par type de moniteur.

**Exemples**

- Si aucune limite n'est définie et que 4 moniteurs de base sont utilisés, il sera indiqué : "Moniteurs de base : 4".
- Si la limite est fixée à 10 moniteurs de base et que 4 moniteurs sont utilisés, il sera indiqué : "Moniteurs de base : 4/10".

## Créer un nouveau groupe de moniteurs

Pour créer un nouveau groupe de moniteurs :

1. Ouvrez [SHORTCODE_3] Configuration de compte > Groupes de moniteurs [SHORTCODE_4].
2. Cliquez sur le bouton [SHORTCODE_5] Ajouter un groupe de moniteurs [SHORTCODE_6] en haut à droite.
   Vous pouvez aussi cliquer sur le signe plus (+) dans le menu [SHORTCODE_7] Configuration de compte > Groupes de moniteurs [SHORTCODE_8].

   La page *Nouveau groupe de moniteurs* s'affiche.

   ![capture d'écran]([LINK_URL_7])

3. Saisissez un nom dans le champ **Description**.
4. Déterminez si vous souhaitez limiter le nombre de moniteurs qu'il sera possible d'ajouter au groupe. Si vous ne souhaitez pas appliquer de limite, choisissez *Autoriser un nombre illimité de moniteurs*. Il est à noter que le nombre total de moniteurs dans tous les groupes ne peut jamais être supérieur au nombre de moniteurs dans votre compte.
5. Ajoutez les moniteurs qui doivent appartenir à ce groupe. Pour cela, cliquez sur le groupe de moniteurs existant dans la section *Moniteurs inclus dans ce groupe* pour afficher la liste, puis cliquez sur les noms des moniteurs. Sachez que vous pouvez aussi ajouter un moniteur à un groupe de moniteurs directement depuis le moniteur en question. Ouvrez l'onglet [SHORTCODE_9] Membre de [SHORTCODE_10] pour apporter ces changements.
6. Dans l'onglet [SHORTCODE_11] Autorisations [SHORTCODE_12], ajoutez l'opérateur ou le groupe d'opérateurs et ses autorisations dans le groupe de moniteurs. Vous trouverez plus d'informations sur ces options dans l'article de notre base de connaissances intitulé [Autorisations de moniteurs]([LINK_URL_8]).
7. Cliquez sur [SHORTCODE_13] Enregistrer [SHORTCODE_14] en bas de l'écran.


Les groupes de moniteurs sont aussi très utiles pour créer une équipe et attribuer à chaque membre (opérateur) les autorisations nécessaires. L'article [Comment créer une équipe dans votre compte]([LINK_URL_9]) décrit la marche à suivre.