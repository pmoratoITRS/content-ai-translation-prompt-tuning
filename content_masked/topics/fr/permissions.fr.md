{
  "hero": {
    "title": "Autorisations"
  },
  "title": "Autorisations",
  "summary": "Les membres de votre équipe ont des rôles et des responsabilités différents. Qu'en est-il des opérateurs dans l'application Uptrends ?",
  "url": "[URL_BASE_TOPICS]compte/utilisateurs/operateurs/autorisations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1] La disponibilité des types d'autorisations dépend de votre abonnement, ce qui signifie que certains types peuvent ne pas être disponibles. Toutes les autorisations sont disponibles pour les comptes **Enterprise**. [SHORTCODE_2]


Dans l'application, les utilisateurs sont appelés opérateurs. Chaque opérateur a un profil utilisateur avec ses coordonnées, ses paramètres personnels, et d'autres informations.
Les opérateurs sont membres d'un ou de plusieurs groupes d'opérateurs. Pour en savoir plus sur ce sujet, vous pouvez lire l'article sur les [opérateurs et groupes d'opérateurs]([LINK_URL_1]).

Comme les opérateurs ont des rôles et responsabilités différents, ils ont besoin d'autorisations différentes dans l'application Uptrends. Un exemple est le rôle commun d'administrateur, où l'opérateur a accès à tout. D'autres opérateurs peuvent avoir besoin d'accéder uniquement à certains produits ou moniteurs. Dans d'autres cas, vous voudrez tout simplement restreindre la visibilité des informations ou le droit de modifier les paramètres.

L'application Uptrends utilise deux approches en matière d'autorisations : les autorisations sur tout le système (globales) liées aux opérateurs ou groupes d'opérateurs et les autorisations liées à des éléments spécifiques. Pour faciliter la configuration, les autorisations globales et les autorisations basées sur des éléments peuvent être paramétrées depuis l'onglet [SHORTCODE_3] Autorisations [SHORTCODE_4] de l'opérateur ou du groupe d'opérateurs.

De plus, les [autorisations liées à des éléments]([LINK_URL_2]) peuvent être paramétrées directement depuis l'élément (moniteur, définition d'alerte, etc.).

Quel que soit l'emplacement choisi pour la configuration des autorisations, les paramètres s'appliquent dans tous les autres emplacements concernés.

## Qui peut gérer les autorisations ?
Seuls les opérateurs disposant de droits d'administrateur peuvent modifier les autorisations. L'opérateur doit être membre du groupe d'opérateurs *Administrateurs* où les *autorisations administratives* existent par défaut et sont obligatoires. Pour les comptes Enterprise, vous pouvez définir des [permissions par opérateur et groupe d'opérateurs]([LINK_URL_3]). Ces permissions vous permettent d’accorder des autorisations spécifiques aux opérateurs et aux groupes d'opérateurs.

## Gérer les autorisations

Nous vous recommandons de gérer les autorisations au niveau du groupe d'opérateurs. Il est également possible d'ajouter des autorisations à des opérateurs individuels. Mais, dans la plupart des situations, il sera plus facile d'ajouter l'opérateur au groupe d'opérateurs qui a déjà les autorisations définies, plutôt que d'ajouter toutes les autorisations à l'opérateur.

Le processus est le même pour l'octroi et la révocation des autorisations. Les étapes pour les groupes d'opérateurs sont décrites ci-dessous.

Pour accorder une autorisation, procédez comme suit :

1. Ouvrez le [hub de gestion des utilisateurs]([LINK_URL_4]) en cliquant sur [SHORTCODE_5] Configuration de compte > Opérateurs, groupes et sous-comptes[SHORTCODE_6] dans le menu. De là, cliquez sur [SHORTCODE_7] Afficher tous les groupes d'opérateurs [SHORTCODE_8] pour obtenir la liste des groupes d'opérateurs configurés pour votre compte.
2. Sélectionnez le groupe pour lequel vous souhaitez ajouter des autorisations.
   Les autorisations se trouvent dans l'onglet [SHORTCODE_9] Autorisations [SHORTCODE_10] accessible depuis la page *Groupe d'opérateurs*.
3. Choisissez les **autorisations sur tout le système** que vous souhaitez attribuer ou révoquer en cochant ou décochant les cases correspondantes.
   ![Autorisations d'un groupe d'opérateurs]([LINK_URL_5])
4. Définissez les [autorisations liées à des éléments]([LINK_URL_6]) pour les moniteurs, les définitions d'alerte et les autres éléments.
5. Cliquez sur [SHORTCODE_11] Enregistrer [SHORTCODE_12] avant de quitter la page.

## Types d'autorisations

Tous les types d'autorisations sont disponibles au niveau de l'opérateur et du groupe d'opérateurs, sauf indication contraire. Certaines autorisations sont obligatoires. Pour plus de détails, référez-vous aux descriptions des autorisations ci-dessous.

### Opérateur de base [ANCHOR_1]

Cette autorisation est ajoutée par défaut à tout nouvel opérateur, et n'est pas visible dans les paramètres du groupe d'opérateurs.

Cette autorisation comprend le droit de se connecter, de visualiser les moniteurs et les tableaux de bord.

Seul un administrateur d'un compte Enterprise peut accorder ou supprimer cette autorisation, qui peut être appliquée pour des opérateurs individuels et pour des groupes.
Une fois l'autorisation supprimée, l'opérateur peut seulement se connecter et accéder à une [page de statut protégée]([LINK_URL_7]). Aucune autre action n'est plus disponible.

### Autorisations administratives

Cette autorisation est obligatoire pour le groupe d'opérateurs par défaut *Administrateurs* et ne peut être donnée à aucun autre groupe d'opérateurs ou opérateur individuel.

Si un opérateur doit disposer de droits administrateur, ajoutez-le au groupe d'opérateurs *Administrateurs*.

### Créer des définitions d'alerte [ANCHOR_2]

Si un opérateur (ou un groupe d'opérateurs) possède cette autorisation, il peut créer de nouvelles définitions d'alerte. Précisons ici que l'autorisation connexe [Modifier la définition d'alerte]([LINK_URL_8]) est définie dans la définition d'alerte elle-même, et non pas au niveau de l'opérateur ou du groupe d'opérateurs.

Une fois que vous avez créé une définition d'alerte, vous obtenez automatiquement l'autorisation **Modifier la définition d'alerte** pour cette définition. Vous pouvez ainsi modifier ensuite la définition d'alerte selon vos besoins.

Si vous possédez les autorisations **Créer des définitions d'alerte** et **Modifier la définition d'alerte**, vous avez aussi le droit de modifier les autorisations au niveau de la définition d'alerte. Vous pouvez ainsi partager votre définition d'alerte avec d'autres opérateurs.

Les administrateurs possèdent l'autorisation **Créer des définitions d'alerte** par défaut.

### Créer des intégrations [ANCHOR_3]

Cette autorisation vous donne le droit de créer des intégrations d'une manière générale. Une fois que vous avez créé une intégration, vous obtenez automatiquement l'autorisation [Modifier l'intégration]([LINK_URL_9]) correspondante. Il vous est ainsi possible de modifier l'intégration par la suite.

Les administrateurs disposent de l'autorisation **Créer des intégrations** par défaut.

### Opérateur financier [ANCHOR_4]

Un opérateur disposant de cette autorisation peut passer des commandes, afficher les factures et effectuer des paiements.   
Cet opérateur est informé de l'expiration du compte, de l'atteinte de la limite des crédits SMS et reçoit également des rappels de paiement.

Il est obligatoire d'avoir au moins un opérateur dans votre compte Uptrends avec cette autorisation. Elle est incluse dans les autorisations du groupe *Administrateurs* par défaut.
### Accès à Infra

Si vous avez un abonnement à Uptrends Infra, vous pouvez donner aux opérateurs l'accès à ce produit.

Cette autorisation est obligatoire pour le groupe d'opérateurs par défaut *Administrateurs*.
### Contact technique

L'autorisation est définie pour l'opérateur qui doit être contacté en cas de problème technique.

Il est obligatoire d'avoir au moins un opérateur avec le type d'autorisation *Contact technique*. Des autorisations de contact technique supplémentaires peuvent être ajoutées et supprimées, à condition que vous conserviez toujours au moins un opérateur avec cette autorisation.

### Gérer les emplacements privés [ANCHOR_5]

Les opérateurs ayant l'autorisation *Gérer les emplacements privés* peuvent créer, supprimer ou gérer des [emplacements privés]([LINK_URL_10]) sur le compte. Pour pouvoir créer un emplacement privé, les opérateurs doivent avoir accès à au moins un [groupe de moniteurs]([LINK_URL_11]) pour lequel ils disposent de l'autorisation *Créer et supprimer des moniteurs dans le groupe*.
L'autorisation *Gérer les emplacements privés* est incluse par défaut dans les autorisations du groupe *Administrateurs*.

### Gérer les modèles de moniteur [ANCHOR_6]

Les opérateurs qui disposent de l'autorisation *Gérer les modèles de moniteur* peuvent gérer et exécuter des [modèles de moniteur]([LINK_URL_12]) pour les moniteurs qu'ils sont autorisés à modifier. Aucun autre droit d'administrateur n'est requis.

## Autorisations liées à des éléments [ANCHOR_7]

Les autorisations suivantes sont liées à un élément, comme une intégration ou un moniteur, tandis que les autorisations sur tout le système s'appliquent globalement.

- [Définitions d'alerte]([LINK_URL_13])
- [Dashboards]([LINK_URL_14])
- [Intégrations]([LINK_URL_15])
- [Moniteurs]([LINK_URL_16])
- [Coffre-fort]([LINK_URL_17])
- [Opérateurs et groupes d'opérateurs]([LINK_URL_18])