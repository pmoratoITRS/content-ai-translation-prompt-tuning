{
"hero": {
"title": "Ajouter ou supprimer un opérateur"
},
"title": "Ajouter ou supprimer un opérateur",
"summary": "Découvrez comment ajouter et configurer un opérateur, ou le supprimer. Chaque opérateur doit être configuré correctement, c'est-à-dire avec ses coordonnées, ses informations de connexion et ses droits d'accès.",
"url": "/support/kb/compte/utilisateurs/operateurs/ajouter-ou-supprimer-un-operateur",
"translationKey": "https://www.uptrends.com/support/kb/account/users/operators/add-or-delete-operator"
}

Dans Uptrends, le [hub de gestion des utilisateurs]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="fr" >}}) est l'endroit idéal pour commencer à gérer les opérateurs (et les groupes d'opérateurs).

## Ajouter un opérateur

1. Ouvrez le [hub de gestion des utilisateurs]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="fr" >}}). Pour ce faire, sélectionnez {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}}Ajouter un opérateur{{< /AppElement >}}.
3. Dans la section **Configuration de l'opérateur**, vous pouvez décider de configurer le nouvel opérateur manuellement (directement dans l'application Uptrends) ou de lui envoyer une [invitation](#by-invitation) pour lui laisser le soin de remplir ses propres informations d'identification.
4. Si vous choisissez l'option *Configuration manuelle*, vous pouvez ajouter l'adresse e-mail, le mot de passe, le nom complet, l'adresse e-mail de secours et le numéro de téléphone mobile de l'opérateur (pour le numéro de téléphone, saisissez le signe \+ suivi du numéro sans tiret ni espace).
5. Une fois que vous avez terminé de configurer votre opérateur, cliquez sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.
6. Transmettez ainsi son mot de passe à l'opérateur. Aucun e-mail n'est envoyé automatiquement si vous choisissez la configuration manuelle du compte.


Pour en savoir plus sur toutes les options de configuration des opérateurs, consultez les articles dans la rubrique [Opérateurs et groupes d'opérateurs]({{< ref path="support/kb/account/users/operators" lang="fr" >}}).
### Sur invitation {id="by-invitation"}

L'invitation est envoyée avec l'adresse *e-mail* figurant dans les **informations de connexion** et elle contient un lien, sur lequel le nouvel utilisateur peut cliquer pour définir son mot de passe. L'invitation est valable pendant 21 jours. Au-delà, le lien devient inutilisable.

Vous pouvez renvoyer une invitation, par exemple si vous souhaitez rappeler au nouvel opérateur qu'il doit activer son compte ou si l'invitation a expiré.

Sur la page des paramètres de l'opérateur, vous pouvez consulter l'état de l'invitation.

Une autre option pour vérifier le statut de l'invitation consiste à consulter la page des opérateurs, que vous trouverez en cliquant sur {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.  Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Voir tous les opérateurs {{< /AppElement >}}. La page des opérateurs comporte une colonne qui affiche des informations sur la dernière connexion et le statut des invitations (en attente). La colonne *Dernière connexion* peut avoir les valeurs suivantes :

- Horodatage de la dernière connexion : le compte a été activé et utilisé.
- Invité : l'invitation a été envoyée et reste valide.
- Invitation expirée : l'invitation a été envoyée, mais 21 jours se sont écoulés sans que l'utilisateur clique sur le lien.
- Jamais connecté : l'invitation a été acceptée, mais l'utilisateur ne s'est jamais connecté.


{{< callout >}} **Remarque** : les opérateurs qui utilisent l'authentification unique (SSO) peuvent être ajoutés sur invitation seulement si les options de connexion Nom d'utilisateur/mot de passe et Authentification unique (Single sign-on) sont activées. {{< /callout >}}

## Supprimer un opérateur

Pour supprimer un opérateur :

1. Ouvrez le [hub de gestion des utilisateurs]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="fr" >}}). Selon votre type de compte, la marche à suivre pour accéder au hub peut varier.
- Pour les comptes **Enterprise**, cliquez sur {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.
- Pour tous les autres types de comptes, cliquez sur {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes > Voir tous les opérateurs {{< /AppElement >}}.

2. Cliquez sur {{< AppElement type="buttonPrimary" >}} Voir tous les opérateurs {{< /AppElement >}} pour afficher la liste de tous les opérateurs de votre compte.
3. Retrouvez l'opérateur que vous souhaitez supprimer dans la liste, et cliquez sur son nom. Vous pouvez aussi filtrer les résultats en saisissant la totalité ou le début du nom ou de l'adresse e-mail dans le champ de recherche.
4. Dans les paramètres de l'opérateur, cliquez sur {{< AppElement type="deletebutton" >}} Supprimer cet opérateur {{< /AppElement >}} en bas à gauche de l'écran.

L'opérateur sera supprimé. La suppression d'un opérateur fonctionne uniquement s'il n'est pas propriétaire d'un dashboard, d'une page de statut public ou d'un rapport planifié au sein du compte. Il ne doit pas non plus être lié à ces éléments. Généralement, si un opérateur a créé un de ces éléments, il devient automatiquement leur propriétaire. Le cas échéant, vous pouvez supprimer ces objets ou les attribuer à un autre opérateur. Vous pouvez aussi solliciter [l'équipe Support]({{< ref path="/contact" lang="fr" >}}).