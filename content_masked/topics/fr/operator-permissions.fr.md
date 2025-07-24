{
  "hero": {
    "title": "Configuration des permissions des opérateurs et groupes d’opérateurs"
  },
  "title": "Configuration des permissions des opérateurs et groupes d’opérateurs",
  "url": "[URL_BASE_TOPICS]account/users/operators/permissions-operateurs",
  "summary": "Cet article vous explique comment configurer les permissions pour vos opérateurs et groupes d'opérateurs.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]La configuration des permissions des opérateurs est disponible uniquement pour les comptes **Enterprise**.[SHORTCODE_2]

Les **permissions des opérateurs et des groupes d'opérateurs** accordent davantage de contrôle et de flexibilité à ces derniers. Grâce à ces permissions, les administrateurs peuvent définir le niveau d’accès auquel les opérateurs ou les groupes d’opérateurs peuvent voir, créer (ou ajouter) et supprimer des opérateurs, mais aussi modifier les paramètres les concernant. Désormais, ces privilèges ne sont plus réservés aux administrateurs : ils deviennent accessibles aux opérateurs et aux groupes qui en disposent. Vous pouvez aussi accorder les permissions d’affichage, de création, de modification et de suppression à des comptes non administrateurs.

Par défaut, deux principaux [groupes d'opérateurs]([LINK_URL_1]) ont été configurés dans votre compte Uptrends : les groupes Administrateurs et Tout le monde. Le *groupe Administrateurs* désigne les opérateurs qui disposent de tous les accès et peuvent tout gérer dans votre compte Uptrends. Le *groupe Tout le monde* regroupe tous les opérateurs ajoutés à un compte. Tout le monde reçoit automatiquement la permission *Voir les opérateurs*. Ainsi, chaque opérateur, y compris les non-administrateurs, peut voir tous les autres opérateurs.

Dans certaines situations, des contraintes de confidentialité et de sécurité peuvent toutefois nécessiter de limiter la visibilité du *groupe Tout le monde*. C’est par exemple le cas si vous voulez limiter l’accès à des informations sensibles aux opérateurs autorisés, mais que vous avez ajouté des sous-traitants ou d’autres personnes en tant que membres de votre équipe Uptrends. Pour éviter les vulnérabilités et les risques, il est préférable de séparer les droits et de limiter l’accès public. Depuis les **permissions des opérateurs**, vous pouvez modifier le paramètre par défaut du *groupe Tout le monde* de telle façon que la permission en vertu de laquelle *tout le monde peut voir tout le monde* ne soit plus applicable.

Pour résumer, les **permissions des opérateurs** vous permettent de contrôler la visibilité et le niveau d’accès de vos opérateurs et groupes d’opérateurs. En ajustant les permissions, les équipes peuvent collaborer efficacement et accomplir des tâches propres à leur groupe, comme le partage de dashboard, la définition des alertes, la planification de rapports, etc. De même, les équipes peuvent accomplir leurs tâches de gestion de façon autonome, ce qui accroît la sécurité, la flexibilité et le contrôle dans votre organisation.

![Permissions des opérateurs pour les groupes Tout le monde et les non-administrateurs]([LINK_URL_2])

## Configurer les permissions des opérateurs et des groupes d'opérateurs
Les permissions des opérateurs peuvent être configurées individuellement au niveau des **opérateurs** ou collectivement au moyen des **groupes d'opérateurs**. Les membres qui appartiennent à un groupe d’opérateurs héritent automatiquement des paramètres de permissions.

[SHORTCODE_3] Tous les membres du groupe Administrateurs peuvent voir, créer et modifier les opérateurs, et ajouter de nouveaux opérateurs à un groupe. [SHORTCODE_4]

## Droits d’accès
Quatre niveaux d’accès peuvent être attribués à chaque opérateur et/ou groupe d’opérateur :
- Aucun : aucune permission n’est accordée à un opérateur ou à un groupe d’opérateurs. Pour limiter la visibilité d’un opérateur ou d’un groupe d’opérateurs, la visibilité par défaut du *groupe Tout le monde* lui-même doit d’abord être supprimée.
- Voir les opérateurs : cette permission autorise les opérateurs à afficher le groupe d’opérateurs et les opérateurs du groupe.
- Modifier les paramètres : cette permission permet aux opérateurs de modifier les paramètres de chaque opérateur du groupe.
- Créer et supprimer : cette permission permet aux opérateurs de créer et de supprimer des opérateurs dans le groupe.

### Configurer les autorisations par opérateur

1. Ouvrez le menu [SHORTCODE_6] Configuration de compte > Opérateurs et groupes [SHORTCODE_7].
2. Cliquez sur le bouton [SHORTCODE_8] Voir tous les opérateurs [SHORTCODE_9].
3. Sélectionnez le nom de l’opérateur dont vous souhaitez définir les permissions.
4. Sous l’onglet [SHORTCODE_10] Autorisations [SHORTCODE_11], vous trouverez la section *Permissions des opérateurs*. Ajoutez vos opérateurs en les sélectionnant dans le menu déroulant, puis ajustez les permissions au moyen du curseur. Pour supprimer des paramètres ou retirer un opérateur de la sélection, cliquez sur l’icône *X*.
   ![Paramètres de permissions des opérateurs]([LINK_URL_3])
5. Confirmez les changements en cliquant sur [SHORTCODE_12] Enregistrer [SHORTCODE_13] en bas de l'écran.

### Configurer les autorisations par groupe d’opérateurs

1. Ouvrez le menu [SHORTCODE_14] Configuration de compte > Opérateurs et groupes [SHORTCODE_15].
2. Cliquez sur le bouton [SHORTCODE_16] Afficher tous les groupes d'opérateurs [SHORTCODE_17].
3. Sélectionnez le nom du groupe d’opérateurs dont vous souhaitez définir les permissions.
4. Sous l’onglet [SHORTCODE_18] Autorisations [SHORTCODE_19], vous trouverez la section *Permissions des opérateurs*. Ajoutez vos groupes d'opérateurs en les sélectionnant dans le menu déroulant, puis ajustez les permissions au moyen du curseur. Pour supprimer des paramètres ou retirer un opérateur de la sélection, cliquez sur l’icône *X*.
   ![Paramètres de permissions des groupes d’opérateurs]([LINK_URL_4])
5. Confirmez les changements en cliquant sur [SHORTCODE_20] Enregistrer [SHORTCODE_21] en bas de l'écran.

[SHORTCODE_5] **Remarque :** le niveau de permission configuré dans les **permissions des opérateurs** se reflète aussi dans d’autres fonctionnalités où des opérateurs peuvent être sélectionnés, comme les *définitions d'alerte* et les *rapports planifiés*. Ainsi, la visibilité dont dispose chaque opérateur ou groupe d'opérateurs dépend largement des permissions qui lui sont accordées.
