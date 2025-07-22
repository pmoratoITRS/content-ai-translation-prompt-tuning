{
"hero": {
"title": "Groupes de moniteurs"
},
"title": "Groupes de moniteurs",
"summary": "Créez des groupes de moniteurs pour simplifier la configuration des alertes et des rapports.",
"url": "/support/kb/surveillance-synthetique/gestion-moniteurs/groupes-moniteurs",
"translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-groups"
}

Les groupes de moniteurs vous aident à vous organiser et vous simplifient la tâche. Une fois que vous avez configuré vos groupes de moniteurs, vous pouvez plus rapidement et plus facilement [appliquer des modèles]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="fr" >}}), ajouter des moniteurs aux [définitions d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}) et configurer les dashboards et les rapports.

## Configurer des groupes de moniteurs

À l'exception du groupe *Tous les moniteurs*, tous les autres groupes sont modifiables. Un moniteur peut appartenir à plusieurs groupes de moniteurs. Vous pouvez configurer vos groupes de moniteurs de différentes façons. Voici quelques exemples inspirés de ce que font les autres utilisateurs.

**Type de moniteur** : il peut être utile de configurer des groupes de moniteurs par [type de moniteur]({{< ref path="support/kb/basics/monitor-types" lang="fr" >}}) : moniteurs de performance de site web, moniteurs de performances mobiles, moniteurs de disponibilité, moniteurs d'API, moniteurs de transactions et moniteurs de certificats. Ce type de groupe est particulièrement utile pour configurer des rapports.

**Par emplacement** : si vous souhaitez obtenir vos rapports en fonction de l'emplacement géographique, il peut être intéressant de regrouper vos moniteurs par région ou pays. En règle générale, ces moniteurs partagent les mêmes checkpoints, ce qui facilite leur gestion à l'aide de modèles de moniteur.

**Par centre de données** : si vous avez des sites associés à différents centres de données, vous pouvez configurer des groupes en fonction du centre de données. Ainsi, vous pourrez rapidement vérifier les performances et la disponibilité en fonction du centre de données. Le regroupement par centre de données peut être utile pour configurer des périodes de maintenance à l'aide de modèles de moniteur.

**Par importance** : vous pouvez regrouper les moniteurs en fonction de l'importance du moniteur. Par exemple, la disponibilité de votre blog n'aura pas la même importance que votre page de connexion. Par conséquent, la configuration de groupes de moniteurs en fonction de l'importance de l'URL est une excellente façon d'organiser les moniteurs et de hiérarchiser vos rapports.

**Par domaine** : vous gérez peut-être plusieurs domaines ou sous-domaines. L'organisation basée sur le domaine facilite la gestion des niveaux des alertes.

**Par fonction** : plusieurs comptes regroupent leurs moniteurs selon la fonction de l'URL, tels que les pages de connexion, les pages d'accueil et les pages d'assistance.

## Vue d'ensemble des groupes de moniteurs

La page **Groupes de moniteurs** vous donne une vue d'ensemble de groupes de moniteurs configurés dans votre compte. Pour l'ouvrir, passez par le menu {{< AppElement type="menuitem" >}} Configuration de compte > Groupes de moniteurs {{< /AppElement >}}.

![capture d'écran du dashboard groupes de moniteurs](/img/content/scr-monitor-groups-overview.min.png)

Cette page montre tous les groupes de moniteurs pour lesquels vous disposez au moins d'une *autorisation d'affichage*. Plusieurs [types d'autorisations]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#permission-types" lang="fr" >}}) sont disponibles pour les moniteurs et les groupes de moniteurs.

Le groupe *Tous les moniteurs* existe par défaut dans tout compte Uptrends. Il contient tous les moniteurs de votre compte et ne peut être modifié ni supprimé. Il peut être intéressant de créer un groupe similaire au groupe *Tous les moniteurs*. Ce groupe contiendra aussi (presque) tous les moniteurs, mais avec la possibilité de modifier les autorisations et de supprimer des moniteurs. Pour connaître la marche à suivre, lisez comment configurer un [groupe de moniteurs par défaut]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#default-monitor-group" lang="fr" >}}).

La vue d'ensemble contient des informations sur les *moniteurs utilisés*, qui vous indiquent le nombre maximum de moniteurs (par type) configurés dans vos groupes de moniteurs. Vous pouvez aussi choisir d'autoriser un nombre illimité de moniteurs et de n'appliquer aucune limite par type de moniteur.

**Exemples**

- Si aucune limite n'est définie et que 4 moniteurs de base sont utilisés, il sera indiqué : "Moniteurs de base : 4".
- Si la limite est fixée à 10 moniteurs de base et que 4 moniteurs sont utilisés, il sera indiqué : "Moniteurs de base : 4/10".

## Créer un nouveau groupe de moniteurs

Pour créer un nouveau groupe de moniteurs :

1. Ouvrez {{< AppElement type="menuitem" >}} Configuration de compte > Groupes de moniteurs {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="button" >}} Ajouter un groupe de moniteurs {{< /AppElement >}} en haut à droite.
   Vous pouvez aussi cliquer sur le signe plus (+) dans le menu {{< AppElement type="menuitem" >}} Configuration de compte > Groupes de moniteurs {{< /AppElement >}}.

   La page *Nouveau groupe de moniteurs* s'affiche.

   ![capture d'écran](/img/content/scr_monitor-group-settings.min.png)

3. Saisissez un nom dans le champ **Description**.
4. Déterminez si vous souhaitez limiter le nombre de moniteurs qu'il sera possible d'ajouter au groupe. Si vous ne souhaitez pas appliquer de limite, choisissez *Autoriser un nombre illimité de moniteurs*. Il est à noter que le nombre total de moniteurs dans tous les groupes ne peut jamais être supérieur au nombre de moniteurs dans votre compte.
5. Ajoutez les moniteurs qui doivent appartenir à ce groupe. Pour cela, cliquez sur le groupe de moniteurs existant dans la section *Moniteurs inclus dans ce groupe* pour afficher la liste, puis cliquez sur les noms des moniteurs. Sachez que vous pouvez aussi ajouter un moniteur à un groupe de moniteurs directement depuis le moniteur en question. Ouvrez l'onglet {{< AppElement type="tab" >}} Membre de {{< /AppElement >}} pour apporter ces changements.
6. Dans l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}, ajoutez l'opérateur ou le groupe d'opérateurs et ses autorisations dans le groupe de moniteurs. Vous trouverez plus d'informations sur ces options dans l'article de notre base de connaissances intitulé [Autorisations de moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}}).
7. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.


Les groupes de moniteurs sont aussi très utiles pour créer une équipe et attribuer à chaque membre (opérateur) les autorisations nécessaires. L'article [Comment créer une équipe dans votre compte]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="fr" >}}) décrit la marche à suivre.