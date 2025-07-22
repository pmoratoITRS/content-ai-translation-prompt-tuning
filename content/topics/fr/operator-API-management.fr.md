{
"hero": {
"title": "Gestion des comptes API d'un opérateur"
},
"title": "Gestion des comptes API d'un opérateur",
"summary": "Ajouter ou supprimer des comptes API à un opérateur",
"url": "/support/kb/compte/utilisateurs/operateurs/gestion-API-operateur",
"translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-API-management"
}

Pour utiliser l'[API d'Uptrends]({{< ref path="support/kb/api" lang="fr" >}}), vous avez besoin d'un compte API (à distinguer de votre compte Uptrends). Les informations d'identification du compte API doivent être saisies selon le schéma d'*authentification de base* pour pouvoir exécuter un appel d'API. Pour savoir comment saisir les informations d'identification nécessaires pour effectuer des appels d'API, référez-vous aux instructions figurant dans la rubrique [Utilisation de votre compte API]({{< ref path="support/kb/api/authentication-v4#usage-API-account" lang="fr" >}}).

Dans les paramètres de l'opérateur, l'onglet {{< AppElement type="tab" >}} Gestion des API {{< /AppElement >}} vous permet de gérer tous les comptes API liés à cet opérateur.

{{< callout >}} **Remarque** : Vous ne pouvez pas récupérer les mots de passe via l'onglet *Gestion des API*, ni ailleurs dans votre compte. Assurez-vous de noter les mots de passe lors de la création d'un nouveau compte API. {{< /callout >}}

## Ajouter un compte API

Pour ajouter un nouveau compte API à un opérateur :

1. Pour ce faire, sélectionnez {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Voir tous les opérateurs {{< /AppElement >}}.
3. Dans la liste des opérateurs, cliquez sur celui pour lequel vous souhaitez ajouter un compte API.
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Gestion des API {{< /AppElement >}}.
5. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter un utilisateur d'API {{< /AppElement >}}.
6. Suivez les instructions et pensez à noter le mot de passe. Le compte API est ajouté à la liste des utilisateurs d'API :

   ![capture d'écran de l'onglet Gestion des API d'un opérateur](/img/content/scr_operator-API-management.min.png)

7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} au bas de la page pour enregistrer les changements apportés à l'opérateur.

Dans les paramètres de l'opérateur, l'onglet {{< AppElement type="tab" >}} Gestion des API {{< /AppElement >}} présente tous les comptes API liés à cet opérateur. Cet onglet indique aussi la date de création et la date de dernière utilisation du compte. La colonne *Dernière utilisation* peut indiquer les possibilités suivantes :

- **Utilisation inconnue** : cette mention s'affiche lorsque le compte API a été créé avant la mise en place de la fonctionnalité "Dernière utilisation".
- **Pas encore utilisé** : cette mention s'affiche lorsque le compte API a été créé après la mise en place de la fonctionnalité "Dernière utilisation", mais qu'il n'a pas encore été utilisé.
- **Date et heure** : l'horodatage de la dernière utilisation du compte API s'affiche lorsque le compte API a été créé et utilisé après la mise en place de la fonctionnalité "Dernière utilisation".

Il existe aussi une autre méthode (plus ancienne) qui consiste à ajouter un compte API en utilisant la méthode /Register de l'API d'Uptrends. Cette méthode n'est pas recommandée car elle est souvent moins commode. Sachez toutefois qu'elle continue de fonctionner. Si vous souhaitez l'utiliser, référez-vous aux instructions présentées dans la rubrique [Enregistrer un compte API]({{< ref path="support/kb/api/authentication-v4#register-API-account" lang="fr" >}}). Un compte ajouté via l'API s'affichera aussi dans l'onglet {{< AppElement type="tab" >}} Gestion des API {{< /AppElement >}} des paramètres de l'opérateur.

## Supprimer un compte API

Pour supprimer un compte API d'un opérateur :

1. Pour ce faire, sélectionnez {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Voir tous les opérateurs {{< /AppElement >}}.
3. Dans la liste des opérateurs, cliquez sur celui auquel vous souhaitez retirer un compte API.
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Gestion des API {{< /AppElement >}}.
5. Sur la ligne du compte à supprimer, cliquez sur le bouton {{< AppElement type="deletebutton" >}} Supprimer l'utilisateur de l'API {{< /AppElement >}}.
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.
