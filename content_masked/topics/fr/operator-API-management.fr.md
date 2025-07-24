{
  "hero": {
    "title": "Gestion des comptes API d'un opérateur"
  },
  "title": "Gestion des comptes API d'un opérateur",
  "summary": "Ajouter ou supprimer des comptes API à un opérateur",
  "url": "[URL_BASE_TOPICS]compte/utilisateurs/operateurs/gestion-API-operateur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Pour utiliser l'[API d'Uptrends]([LINK_URL_1]), vous avez besoin d'un compte API (à distinguer de votre compte Uptrends). Les informations d'identification du compte API doivent être saisies selon le schéma d'*authentification de base* pour pouvoir exécuter un appel d'API. Pour savoir comment saisir les informations d'identification nécessaires pour effectuer des appels d'API, référez-vous aux instructions figurant dans la rubrique [Utilisation de votre compte API]([LINK_URL_2]).

Dans les paramètres de l'opérateur, l'onglet [SHORTCODE_3] Gestion des API [SHORTCODE_4] vous permet de gérer tous les comptes API liés à cet opérateur.

[SHORTCODE_1] **Remarque** : Vous ne pouvez pas récupérer les mots de passe via l'onglet *Gestion des API*, ni ailleurs dans votre compte. Assurez-vous de noter les mots de passe lors de la création d'un nouveau compte API. [SHORTCODE_2]

## Ajouter un compte API

Pour ajouter un nouveau compte API à un opérateur :

1. Pour ce faire, sélectionnez [SHORTCODE_5] Configuration de compte > Opérateurs, groupes et sous-comptes [SHORTCODE_6].
2. Cliquez sur le bouton [SHORTCODE_7] Voir tous les opérateurs [SHORTCODE_8].
3. Dans la liste des opérateurs, cliquez sur celui pour lequel vous souhaitez ajouter un compte API.
4. Ouvrez l'onglet [SHORTCODE_9] Gestion des API [SHORTCODE_10].
5. Cliquez sur le bouton [SHORTCODE_11] Ajouter un utilisateur d'API [SHORTCODE_12].
6. Suivez les instructions et pensez à noter le mot de passe. Le compte API est ajouté à la liste des utilisateurs d'API :

   ![capture d'écran de l'onglet Gestion des API d'un opérateur]([LINK_URL_3])

7. Cliquez sur le bouton [SHORTCODE_13] Enregistrer [SHORTCODE_14] au bas de la page pour enregistrer les changements apportés à l'opérateur.

Dans les paramètres de l'opérateur, l'onglet [SHORTCODE_15] Gestion des API [SHORTCODE_16] présente tous les comptes API liés à cet opérateur. Cet onglet indique aussi la date de création et la date de dernière utilisation du compte. La colonne *Dernière utilisation* peut indiquer les possibilités suivantes :

- **Utilisation inconnue** : cette mention s'affiche lorsque le compte API a été créé avant la mise en place de la fonctionnalité "Dernière utilisation".
- **Pas encore utilisé** : cette mention s'affiche lorsque le compte API a été créé après la mise en place de la fonctionnalité "Dernière utilisation", mais qu'il n'a pas encore été utilisé.
- **Date et heure** : l'horodatage de la dernière utilisation du compte API s'affiche lorsque le compte API a été créé et utilisé après la mise en place de la fonctionnalité "Dernière utilisation".

Il existe aussi une autre méthode (plus ancienne) qui consiste à ajouter un compte API en utilisant la méthode /Register de l'API d'Uptrends. Cette méthode n'est pas recommandée car elle est souvent moins commode. Sachez toutefois qu'elle continue de fonctionner. Si vous souhaitez l'utiliser, référez-vous aux instructions présentées dans la rubrique [Enregistrer un compte API]([LINK_URL_4]). Un compte ajouté via l'API s'affichera aussi dans l'onglet [SHORTCODE_17] Gestion des API [SHORTCODE_18] des paramètres de l'opérateur.

## Supprimer un compte API

Pour supprimer un compte API d'un opérateur :

1. Pour ce faire, sélectionnez [SHORTCODE_19] Configuration de compte > Opérateurs, groupes et sous-comptes [SHORTCODE_20].
2. Cliquez sur le bouton [SHORTCODE_21] Voir tous les opérateurs [SHORTCODE_22].
3. Dans la liste des opérateurs, cliquez sur celui auquel vous souhaitez retirer un compte API.
4. Ouvrez l'onglet [SHORTCODE_23] Gestion des API [SHORTCODE_24].
5. Sur la ligne du compte à supprimer, cliquez sur le bouton [SHORTCODE_25] Supprimer l'utilisateur de l'API [SHORTCODE_26].
6. Cliquez sur le bouton [SHORTCODE_27] Enregistrer [SHORTCODE_28] en bas de l'écran.
