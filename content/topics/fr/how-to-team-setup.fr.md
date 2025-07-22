{
"hero": {
"title": "Comment créer une équipe dans votre compte"
},
"title": "Comment créer une équipe dans votre compte",
"summary": "Cet article explique comment créer une nouvelle équipe autonome dans votre compte Uptrends.",
"url": "/support/kb/compte/autorisations/comment-creer-une-equipe",
"translationKey": "https://www.uptrends.com/support/kb/permissions/how-to-team-setup"
}

L'exercice décrit dans cet article vise à créer une nouvelle équipe autonome dans votre compte Uptrends. La procédure de configuration se compose des tâches suivantes :

- Créer un nouveau groupe d'opérateurs
- Créer un nouveau groupe de moniteurs et attribuer les autorisations
- Attribuer les autorisations d'alerte et d'intégration
- Accorder uniquement l'accès aux moniteurs pertinents
- Attribuer des autorisations de moniteurs spécifiques

**Astuce :** Référez-vous au résumé intitulé "Dans cet article" (sur la gauche) pour passer facilement d'une tâche à l'autre.

{{< callout >}} **Remarque :** Vous devez avoir le statut d'administrateur pour réaliser toutes les étapes de la configuration. {{< /callout >}}

## Créer un nouveau groupe d'opérateurs

Pour créer le nouveau groupe :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Ajouter un groupe d'opérateurs {{< /AppElement >}} dans la section "Vous avez x groupes d'opérateurs".
3. Dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}, ajoutez un nom pour le groupe d'opérateurs dans le champ **Description**. Dans cet exemple, nous utiliserons le nom "Équipe A".
4. Ajoutez tous les opérateurs qui se trouvent déjà dans votre compte et doivent faire partie de l'équipe. Pour ajouter un opérateur, cochez la case en face de son nom.
   Si les opérateurs ne sont pas encore créés, ce n'est pas un problème. Vous pourrez les ajouter au groupe ultérieurement, si nécessaire.
5. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Le nouveau groupe d'opérateurs "Équipe A" a bien été créé, et plusieurs opérateurs y ont été ajoutés.

## Créer un groupe de moniteurs et attribuer les autorisations

Comme le groupe d'opérateurs "Équipe A" vient d'être créé, il n'a pas d'autorisations sur les autres groupes de moniteurs, et ses membres peuvent uniquement créer des moniteurs qui feront partie du groupe "Moniteurs A". En tant qu'administrateur, c'est donc à vous d'ajouter des moniteurs existants au groupe "Moniteurs A", comme expliqué dans la section [Créer le groupe de moniteurs](#create-monitor-group). C'est la seule action que l'équipe ne peut effectuer seule.

### Créer le groupe de moniteurs {id="create-monitor-group"}

La prochaine étape consiste à créer le nouveau groupe de moniteurs qui sera géré par la nouvelle équipe.

1. Accédez au menu {{< AppElement type="menuitem" >}} Configuration de compte > Groupes de moniteurs {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="button" >}} Ajouter un groupe de moniteurs {{< /AppElement >}} en haut à droite.
3. Saisissez un nom pour le groupe de moniteurs dans le champ **Description**. Dans cet exemple, nous utiliserons le nom "Moniteurs A".
4. Dans la liste **Moniteurs inclus dans ce groupe** en bas, ajoutez des moniteurs au groupe en affichant le groupe et en cochant la case en face du nom de moniteur.
   Si les moniteurs n'ont pas encore été définis dans le compte, ils pourront toujours être ajoutés ultérieurement par vous ou la nouvelle équipe.
5. (Facultatif) Vous pouvez définir le nombre maximum de moniteurs (par type) que peut contenir un groupe de moniteurs. Si vous ne souhaitez pas restreindre le nombre de moniteurs dans le groupe, cochez l'option **Autoriser un nombre illimité de moniteurs**. Veuillez noter que le groupe ne peut jamais contenir plus de moniteurs que votre compte (pour vérifier votre nombre de moniteurs, ouvrez {{< AppElement type="menuitem" >}} Configuration de compte > Paramètres de compte > Abonnement {{< /AppElement >}}). Cela étant, les moniteurs peuvent se trouver dans plusieurs groupes.
6. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Le nouveau groupe de moniteurs "Moniteurs A" est désormais disponible.

### Attribuer les autorisations

Au stade où nous en sommes, vous disposez d'un groupe d'opérateurs "Équipe A" et d'un groupe de moniteurs "Moniteurs A". Cependant, les membres du groupe d'opérateurs "Équipe A" ne peuvent pas encore gérer les moniteurs du groupe Moniteurs A.

Pour cela, vous devez d'abord leur attribuer les autorisations nécessaires. Suivez les étapes suivantes :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher tous les groupes d'opérateurs {{< /AppElement >}}.
3. Sélectionnez le groupe d'opérateurs "Équipe A".
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
5. Dans la section **Permissions de moniteur**, sélectionnez le groupe de moniteurs "Moniteurs A" dans la liste.
   ![capture d'écran ajouter une permission de moniteur à l'équipe](/img/content/scr-add-monitor-to-team.min.png)
6. Dans la barre correspondant à "Moniteurs A", déplacez le curseur sur l'autorisation *Créer et supprimer*.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.


Le groupe d'opérateurs "Équipe A" peut désormais créer des moniteurs.

À partir de cette étape, le statut d'administrateur (général) n'est plus nécessaire pour créer de nouveaux moniteurs pour l'équipe. Les membres du groupe d'opérateurs "Équipe A" peuvent désormais gérer leurs moniteurs et en créer de nouveaux si nécessaire.

## Attribuer les autorisations d'alerte et d'intégration

Une fois que le groupe d'opérateurs et le groupe de moniteurs ont été créés, les membres du groupe "Équipe A" peuvent commencer à paramétrer la surveillance. La configuration des alertes est une étape essentielle, car elle permet de s'assurer que les opérateurs reçoivent des notifications et peuvent réagir rapidement en cas de problème. C'est pourquoi l'équipe doit être capable de créer et/ou de modifier des définitions d'alerte et des intégrations. Comme cet article porte sur la création d'une équipe autonome, les membres du groupe "Équipe A" doivent pouvoir gérer intégralement ces éléments.

Suivez les étapes suivantes pour attribuer les autorisations relatives aux définitions d'alerte et aux intégrations aux membres du groupe "Équipe A" :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher tous les groupes d'opérateurs {{< /AppElement >}} dans la section "Vous avez x groupes d'opérateurs".
3. Cliquez sur le groupe d'opérateurs "Équipe A".
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
5. Dans la section **Autorisations sur tout le système**, sélectionnez les autorisations **Créer des définitions d'alerte** et **Créer des intégrations**.
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas à gauche de l'écran.

Les membres du groupe "Équipe A" peuvent désormais créer des définitions d'alerte et des intégrations.

### Attribuer les autorisations pour les alertes existantes

Grâce aux autorisations que vous venez d'ajouter, les membres de l'équipe peuvent créer les définitions d'alerte et les intégrations qui leur sont nécessaires. Aucun droit d'administrateur n'est nécessaire pour modifier les alertes définies pour l'équipe. Cependant, il est possible que votre équipe ait besoin d'accéder à des définitions d'alerte ou à des intégrations qui existaient avant sa création dans votre compte. Cette tâche est réservée à un profil d'administrateur.

Pour ajouter le groupe "Équipe A" aux définitions d'alerte existantes :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher tous les groupes d'opérateurs {{< /AppElement >}} dans la section "Vous avez x groupes d'opérateurs".
3. Cliquez sur le groupe d'opérateurs "Équipe A".
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
   ![capture d'écran des autorisations par groupe d'opérateurs](/img/content/scr_team-setup-alertdefinition-permissions.min.png)
5. Dans la section **Autorisations de définition d'alerte**, utilisez le menu déroulant pour sélectionner et ajouter toutes les définitions d'alerte existantes que le groupe "Équipe A" doit pouvoir gérer.
6. Si vous avez ajouté une définition par erreur ou si le groupe "Équipe A" ne doit plus gérer une définition, cliquez sur la croix à côté de la définition pour retirer l'autorisation.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.


Pour ajouter le groupe "Équipe A" à des intégrations existantes :

1. Ouvrez {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Cliquez sur l'intégration que le groupe "Équipe A" doit pouvoir utiliser et/ou modifier.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
4. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter une autorisation {{< /AppElement >}}.
5. Dans la fenêtre contextuelle, sélectionnez le groupe d'opérateurs "Équipe A", puis cliquez sur l'autorisation que vous souhaitez attribuer.
   Sélectionnez **Utiliser l'intégration** si l'équipe doit pouvoir utiliser l'intégration dans une définition d'alerte.
   Sélectionner **Modifier l'intégration** si l'équipe doit pouvoir gérer tous les aspects de l'intégration, et la supprimer.
6. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter {{< /AppElement >}}.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Reproduisez ces mêmes étapes pour toutes les intégrations dont vous souhaitez attribuer l'accès au groupe "Équipe A".

Les membres du groupe "Équipe A" peuvent désormais créer ou modifier des définitions d'alerte, et y ajouter des intégrations. Selon votre choix, ils peuvent aussi modifier les intégrations.

## Accorder uniquement l'accès aux moniteurs pertinents

{{< callout >}} **Remarque** : Cette action est nécessaire uniquement lors de la création d'une équipe dans votre compte. {{< /callout >}}

Dans cet exercice, vous allez apprendre à configurer une équipe autonome de telle sorte que ses membres pourront se concentrer sur les données de surveillance qui les concernent. Comme vous allez le voir, cela nécessite une opération particulière.

Tout compte Uptrends contient le groupe d'opérateurs "Tout le monde". Tous les opérateurs dans votre compte sont des membres de ce groupe, et peuvent accéder par défaut aux données de surveillance de tous les moniteurs. Vous ne pouvez pas supprimer le groupe "Tout le monde", et vous ne pouvez pas supprimer des opérateurs dans ce groupe.

L'astuce consiste donc à partager les opérateurs du groupe "Tout le monde" entre le groupe "Équipe A" et un nouveau groupe appelé "Opérateurs principaux".

Ainsi, vous pourrez ensuite retirer l'autorisation d'afficher toutes les données pour le groupe "Tout le monde" et définir des autorisations pour les groupes individuels ("Équipe A", "Opérateurs principaux") selon vos besoins.

Pour cela, commencez par créer un nouveau groupe d'opérateurs appelé "Opérateurs principaux" :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Ajouter un groupe d'opérateurs {{< /AppElement >}} dans la section "Vous avez x groupes d'opérateurs".
3. Dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}, ajoutez un nom pour le groupe d'opérateurs dans le champ **Description**. Pour cet exercice, utilisez le nom "Opérateurs principaux".
4. Ajoutez tous les opérateurs qui ne doivent pas faire partie de la nouvelle équipe ("Équipe A"). Pour ajouter un opérateur, cochez la case en face de son nom.
5. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Modifiez ensuite les autorisations d'affichage dans le groupe "Tous les moniteurs" :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher tous les groupes d'opérateurs {{< /AppElement >}} dans la section "Vous avez x groupes d'opérateurs".
3. Sélectionnez le groupe d'opérateurs "Tout le monde".
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
5. Dans la section **Permissions de moniteur**, supprimez la barre "Tous les moniteurs" (pour l'autorisation *Afficher les données*) en cliquant sur la croix à son extrémité.
   ![capture d'écran supprimer les autorisations d'affichage](/img/content/scr-remove-view-permission-from-everyone.min.png)
6. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.
7. Revenez dans la liste **Groupes d'opérateurs** et sélectionnez le groupe "Opérateurs principaux".
8. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
9. Dans la section **Permissions de moniteur**, accordez l'autorisation *Afficher les données* au groupe "Tous les moniteurs" en choisissant ce groupe dans la liste puis en déplaçant le curseur jusqu'à cette autorisation.
10. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Dans les étapes ci-dessus, vous avez retiré l'accès à toutes les données des moniteurs pour le groupe "Équipe A", puis restitué les droits d'affichage des données originaux à tous les autres opérateurs (membres du groupe "Opérateurs principaux") qui ne sont pas membres du groupe "Équipe A".

Par conséquent, les membres du groupe "Équipe A" ont des droits d'affichage limités, et peuvent uniquement afficher les moniteurs du groupe "Moniteurs A". En revanche, les autres opérateurs ont récupéré la vue d'ensemble initiale.

Il est possible qu'un opérateur appartenant à plusieurs groupes d'opérateurs ait accès à plus de données, car les autres groupes d'opérateurs peuvent disposer d'autres autorisations.

## Attribuer des autorisations de moniteurs spécifiques

Avec les paramètres décrits ci-dessus, vous avez créé une équipe que vous avez associée à un groupe de moniteurs. Les membres de cette équipe peuvent créer et modifier des moniteurs dans ce groupe, et créer les définitions d'alerte et les intégrations dont ils peuvent avoir besoin. L'équipe est donc autonome, et presque aucune intervention de l'administrateur n'est requise. Toutefois, il est possible que l'équipe ait besoin d'afficher ou de modifier les données de moniteurs d'autres équipes.

Pour permettre au nouveau groupe "Équipe A" d'accéder à d'autres moniteurs, vous devez attribuer les autorisations requises aux groupes de moniteurs des autres équipes. Par exemple, s'il existe une "Équipe B" associée à un groupe de moniteurs "Moniteurs B", vous pouvez ouvrir le groupe d'opérateurs "Équipe A" et, dans l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}} dans la section **Permissions de moniteur**, ajouter le groupe de moniteurs "Moniteurs B" depuis la liste, et accorder l'autorisation **Afficher les données** à l'Équipe A en déplaçant le curseur sur cette autorisation.
Ainsi, le groupe "Équipe A" pourra afficher les données de surveillance du groupe "Équipe B", mais sans pouvoir les modifier. Cela permet aux équipes de collaborer tout en maintenant un accès limité.

