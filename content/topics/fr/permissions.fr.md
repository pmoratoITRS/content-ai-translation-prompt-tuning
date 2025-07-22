{
"hero": {
"title": "Autorisations"
},
"title": "Autorisations",
"summary": "Les membres de votre équipe ont des rôles et des responsabilités différents. Qu'en est-il des opérateurs dans l'application Uptrends ?",
"url": "/support/kb/compte/utilisateurs/operateurs/autorisations",
"translationKey": "https://www.uptrends.com/support/kb/account/users/operators/permissions"
}

{{< callout >}} La disponibilité des types d'autorisations dépend de votre abonnement, ce qui signifie que certains types peuvent ne pas être disponibles. Toutes les autorisations sont disponibles pour les comptes **Enterprise**. {{< /callout >}}


Dans l'application, les utilisateurs sont appelés opérateurs. Chaque opérateur a un profil utilisateur avec ses coordonnées, ses paramètres personnels, et d'autres informations.
Les opérateurs sont membres d'un ou de plusieurs groupes d'opérateurs. Pour en savoir plus sur ce sujet, vous pouvez lire l'article sur les [opérateurs et groupes d'opérateurs]({{< ref path="support/kb/account/users/operators/operator-groups" lang="fr" >}}).

Comme les opérateurs ont des rôles et responsabilités différents, ils ont besoin d'autorisations différentes dans l'application Uptrends. Un exemple est le rôle commun d'administrateur, où l'opérateur a accès à tout. D'autres opérateurs peuvent avoir besoin d'accéder uniquement à certains produits ou moniteurs. Dans d'autres cas, vous voudrez tout simplement restreindre la visibilité des informations ou le droit de modifier les paramètres.

L'application Uptrends utilise deux approches en matière d'autorisations : les autorisations sur tout le système (globales) liées aux opérateurs ou groupes d'opérateurs et les autorisations liées à des éléments spécifiques. Pour faciliter la configuration, les autorisations globales et les autorisations basées sur des éléments peuvent être paramétrées depuis l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}} de l'opérateur ou du groupe d'opérateurs.

De plus, les [autorisations liées à des éléments]({{< ref path="#item-based-permissions" lang="fr" >}}) peuvent être paramétrées directement depuis l'élément (moniteur, définition d'alerte, etc.).

Quel que soit l'emplacement choisi pour la configuration des autorisations, les paramètres s'appliquent dans tous les autres emplacements concernés.

## Qui peut gérer les autorisations ?
Seuls les opérateurs disposant de droits d'administrateur peuvent modifier les autorisations. L'opérateur doit être membre du groupe d'opérateurs *Administrateurs* où les *autorisations administratives* existent par défaut et sont obligatoires. Pour les comptes Enterprise, vous pouvez définir des [permissions par opérateur et groupe d'opérateurs]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="fr" >}}). Ces permissions vous permettent d’accorder des autorisations spécifiques aux opérateurs et aux groupes d'opérateurs.

## Gérer les autorisations

Nous vous recommandons de gérer les autorisations au niveau du groupe d'opérateurs. Il est également possible d'ajouter des autorisations à des opérateurs individuels. Mais, dans la plupart des situations, il sera plus facile d'ajouter l'opérateur au groupe d'opérateurs qui a déjà les autorisations définies, plutôt que d'ajouter toutes les autorisations à l'opérateur.

Le processus est le même pour l'octroi et la révocation des autorisations. Les étapes pour les groupes d'opérateurs sont décrites ci-dessous.

Pour accorder une autorisation, procédez comme suit :

1. Ouvrez le [hub de gestion des utilisateurs]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="fr" >}}) en cliquant sur {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes{{< /AppElement >}} dans le menu. De là, cliquez sur {{< AppElement type="buttonPrimary" >}} Afficher tous les groupes d'opérateurs {{< /AppElement >}} pour obtenir la liste des groupes d'opérateurs configurés pour votre compte.
2. Sélectionnez le groupe pour lequel vous souhaitez ajouter des autorisations.
   Les autorisations se trouvent dans l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}} accessible depuis la page *Groupe d'opérateurs*.
3. Choisissez les **autorisations sur tout le système** que vous souhaitez attribuer ou révoquer en cochant ou décochant les cases correspondantes.
   ![Autorisations d'un groupe d'opérateurs](/img/content/scr_operatorgroup-permissions-091624.min.png)
4. Définissez les [autorisations liées à des éléments]({{< ref path="#item-based-permissions" lang="fr" >}}) pour les moniteurs, les définitions d'alerte et les autres éléments.
5. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} avant de quitter la page.

## Types d'autorisations

Tous les types d'autorisations sont disponibles au niveau de l'opérateur et du groupe d'opérateurs, sauf indication contraire. Certaines autorisations sont obligatoires. Pour plus de détails, référez-vous aux descriptions des autorisations ci-dessous.

### Opérateur de base {id="basic-operator"}

Cette autorisation est ajoutée par défaut à tout nouvel opérateur, et n'est pas visible dans les paramètres du groupe d'opérateurs.

Cette autorisation comprend le droit de se connecter, de visualiser les moniteurs et les tableaux de bord.

Seul un administrateur d'un compte Enterprise peut accorder ou supprimer cette autorisation, qui peut être appliquée pour des opérateurs individuels et pour des groupes.
Une fois l'autorisation supprimée, l'opérateur peut seulement se connecter et accéder à une [page de statut protégée]({{< ref path="/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages#protected-status-pages" lang="fr" >}}). Aucune autre action n'est plus disponible.

### Autorisations administratives

Cette autorisation est obligatoire pour le groupe d'opérateurs par défaut *Administrateurs* et ne peut être donnée à aucun autre groupe d'opérateurs ou opérateur individuel.

Si un opérateur doit disposer de droits administrateur, ajoutez-le au groupe d'opérateurs *Administrateurs*.

### Créer des définitions d'alerte {id="create-alert-definition"}

Si un opérateur (ou un groupe d'opérateurs) possède cette autorisation, il peut créer de nouvelles définitions d'alerte. Précisons ici que l'autorisation connexe [Modifier la définition d'alerte]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="fr" >}}) est définie dans la définition d'alerte elle-même, et non pas au niveau de l'opérateur ou du groupe d'opérateurs.

Une fois que vous avez créé une définition d'alerte, vous obtenez automatiquement l'autorisation **Modifier la définition d'alerte** pour cette définition. Vous pouvez ainsi modifier ensuite la définition d'alerte selon vos besoins.

Si vous possédez les autorisations **Créer des définitions d'alerte** et **Modifier la définition d'alerte**, vous avez aussi le droit de modifier les autorisations au niveau de la définition d'alerte. Vous pouvez ainsi partager votre définition d'alerte avec d'autres opérateurs.

Les administrateurs possèdent l'autorisation **Créer des définitions d'alerte** par défaut.

### Créer des intégrations {id="create-integration"}

Cette autorisation vous donne le droit de créer des intégrations d'une manière générale. Une fois que vous avez créé une intégration, vous obtenez automatiquement l'autorisation [Modifier l'intégration]({{< ref path="support/kb/alerting/integrations/integrations-permissions#edit-integration" lang="fr" >}}) correspondante. Il vous est ainsi possible de modifier l'intégration par la suite.

Les administrateurs disposent de l'autorisation **Créer des intégrations** par défaut.

### Opérateur financier {id="financial-operator"}

Un opérateur disposant de cette autorisation peut passer des commandes, afficher les factures et effectuer des paiements.   
Cet opérateur est informé de l'expiration du compte, de l'atteinte de la limite des crédits SMS et reçoit également des rappels de paiement.

Il est obligatoire d'avoir au moins un opérateur dans votre compte Uptrends avec cette autorisation. Elle est incluse dans les autorisations du groupe *Administrateurs* par défaut.
### Accès à Infra

Si vous avez un abonnement à Uptrends Infra, vous pouvez donner aux opérateurs l'accès à ce produit.

Cette autorisation est obligatoire pour le groupe d'opérateurs par défaut *Administrateurs*.
### Contact technique

L'autorisation est définie pour l'opérateur qui doit être contacté en cas de problème technique.

Il est obligatoire d'avoir au moins un opérateur avec le type d'autorisation *Contact technique*. Des autorisations de contact technique supplémentaires peuvent être ajoutées et supprimées, à condition que vous conserviez toujours au moins un opérateur avec cette autorisation.

### Gérer les emplacements privés {id="manage-private-locations"}

Les opérateurs ayant l'autorisation *Gérer les emplacements privés* peuvent créer, supprimer ou gérer des [emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}) sur le compte. Pour pouvoir créer un emplacement privé, les opérateurs doivent avoir accès à au moins un [groupe de moniteurs]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="fr" >}}) pour lequel ils disposent de l'autorisation *Créer et supprimer des moniteurs dans le groupe*.
L'autorisation *Gérer les emplacements privés* est incluse par défaut dans les autorisations du groupe *Administrateurs*.

### Gérer les modèles de moniteur {id="manage-monitor-templates"}

Les opérateurs qui disposent de l'autorisation *Gérer les modèles de moniteur* peuvent gérer et exécuter des [modèles de moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="fr" >}}) pour les moniteurs qu'ils sont autorisés à modifier. Aucun autre droit d'administrateur n'est requis.

## Autorisations liées à des éléments {id="item-based-permissions"}

Les autorisations suivantes sont liées à un élément, comme une intégration ou un moniteur, tandis que les autorisations sur tout le système s'appliquent globalement.

- [Définitions d'alerte]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="fr" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
   lang="fr" >}})
- [Intégrations]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="fr" >}})
- [Moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}})
- [Coffre-fort]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="fr" >}})
- [Opérateurs et groupes d'opérateurs]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="fr" >}})