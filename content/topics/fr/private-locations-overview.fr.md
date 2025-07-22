{
"hero": {
"title": "Vue d'ensemble des emplacements privés"
},
"title": "Vue d'ensemble des emplacements privés",
"summary": "Utilisez les emplacements privés pour gérer vos checkpoints.",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/apercu-des-sites-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-overview",
"sectionlist": false
}

{{< callout >}} **Annonce :** Uptrends vous propose d'essayer gratuitement les emplacements privés pendant 30 jours ! Pour en savoir plus, reportez-vous à la section [Essai des emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview#private-locations-trial" lang="fr" >}}). {{< /callout >}}

La plupart du temps, Uptrends surveille vos sites web, vos applications et vos API au moyen de son réseau mondial d'[emplacements de checkpoints publics](/checkpoints). Toutefois, il peut arriver que vous deviez réaliser des activités de monitoring en interne. Dans ces situations, Uptrends vous fournit des **emplacements privés** qui vous permettent d'utiliser des moniteurs pour effectuer des vérifications sur votre propre serveur et à l'intérieur de votre pare-feu.

Les **emplacements privés** vous permettent de créer, de définir et de regrouper vos checkpoints selon un besoin, une fonction ou un emplacement (ville, pays ou continent) spécifique. Afin de vous donner un contrôle total, Uptrends vous fournit les instructions d'installation du logiciel et vous confie la responsabilité de gérer l'infrastructure matérielle interne, l'installation, les mises à jour et les autres [exigences liées à la configuration]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="fr" >}}).

Pour accéder aux **emplacements privés** dans l'application web d'Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.

![capture d'écran des emplacements privés](/img/content/scr_private-locations-v3.min.png)

## Ajouter des emplacements privés

Pour ajouter un nouvel emplacement :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter un emplacement {{< /AppElement >}}.
3. Indiquez le nom de l'emplacement depuis lequel vous voulez effectuer la surveillance.
4. Choisissez un [groupe de moniteurs]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="fr" >}}) pour lequel vous disposez de l'autorisation de créer des moniteurs. Les moniteurs de l'état de santé de l'emplacement seront créés dans ce groupe. Les groupes de moniteurs ayant les autorisations nécessaires sont listés dans le menu déroulant.
5. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Ajouter un emplacement privé {{< /AppElement >}}.

Le nouvel emplacement est créé et ajouté à la liste des emplacements privés. Deux checkpoints non configurés et non installés sont ajoutés par défaut. Consultez la [FAQ]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq#two-default-private-checkpoints" lang="fr" >}}) si vous souhaitez savoir pourquoi deux checkpoints sont ajoutés (au lieu d'un seul).

Pour renommer un emplacement privé, cliquez sur le bouton {{< AppElement type="iconSettings" >}} {{< /AppElement >}} à côté du nom.

## Ajouter un checkpoint

Tout nouvel emplacement privé contient automatiquement deux checkpoints. Vous pouvez commencer par les installer ou ajouter d'autres checkpoints (immédiatement ou ultérieurement).

Pour ajouter un **checkpoint** :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Ajouter un point de contrôle {{< /AppElement >}} dans l'emplacement souhaité.
3. Choisissez un groupe de moniteurs pour lequel vous disposez de l'autorisation de créer des moniteurs. Le moniteur de l'état de santé du checkpoint sera créé dans ce groupe.
4. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Ajouter un point de contrôle {{< /AppElement >}}.

Pour renommer un **checkpoint** :

Cliquez sur le checkpoint pour ouvrir sa page, cliquez sur le bouton de modification {{< AppElement type="iconSettings" >}} {{< /AppElement >}} derrière le nom et saisissez le nouveau nom.

Dans l'application web d'Uptrends, le checkpoint que vous ajoutez existe uniquement sous forme de représentation numérique. Le checkpoint qui réalisera les vérifications doit aussi être installé.

Pour installer un checkpoint, reportez-vous aux instructions [Installer un checkpoint Docker]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="fr" >}}). Pour en savoir plus sur les emplacements privés, lisez l'article [Comment utiliser les checkpoints des emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="fr" >}}).

## Essai des emplacements privés

L'**essai des emplacements privés** proposé par Uptrends est accessible pour tous les utilisateurs. L'essai vous permet de créer et de configurer vos **emplacements privés** pour les tester et les utiliser avec vos moniteurs existants.

Pour que vous ayez suffisamment de temps pour vous préparer, l'essai reste ouvert jusqu'à ce que vous ayez terminé d'installer votre premier emplacement privé sur la plateforme d'Uptrends. Pour cela, vous devez avoir rempli toutes les [exigences nécessaires]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="fr" >}}) et [configuré et installé un checkpoint privé dans un conteneur Docker]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="fr" >}}).

Une fois votre premier emplacement privé opérationnel, votre essai gratuit de 30 jours commence. La date de fin de l'essai s'applique que les **emplacements privés** aient été ou non utilisés par un checkpoint de monitoring.

Pour prolonger l'essai ou souscrire un abonnement, veuillez contacter votre chargé de compte ou l'[équipe de support](/contact).
