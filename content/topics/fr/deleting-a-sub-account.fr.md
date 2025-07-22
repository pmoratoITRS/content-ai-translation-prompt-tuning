{
"hero": {
"title": "Supprimer un sous-compte"
},
"title": "Supprimer un sous-compte",
"summary": "Voici quelques conseils utiles pour la suppression de sous-comptes.",
"url": "/support/kb/compte/utilisateurs/les-sous-comptes/supprimer-un-sous-compte",
"translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/deleting-a-sub-account"
}

La suppression d'un sous-compte est assez simple. Vous supprimez tout d'abord les opérateurs, puis vous supprimez le sous-compte. Cependant, voici quelques conseils pour faciliter la suppression des sous-comptes et des opérateurs de sous-compte, surtout si vous gérez plusieurs sous-comptes.

## Supprimer un sous-compte

Nous vous recommandons de supprimer les opérateurs de sous-compte avant de supprimer le sous-compte. Pourquoi ? Tant que le sous-compte est actif, vous pouvez facilement identifier ses opérateurs sur la page {{< AppElement type="menuitem" >}}Opérateurs{{< /AppElement >}}.

1. Ouvrez le hub des opérateurs en sélectionnant ({{< AppElement type="menuitem" >}}Configuration de compte > Opérateurs, groupes et sous-comptes{{< /AppElement >}}).
2. Ouvrez la page des paramètres du sous-compte en cliquant sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher tous les sous-comptes {{< /AppElement >}}.
3. Cliquez sur le sous-compte à supprimer.
2. Ouvrez l'onglet {{< AppElement type="tab" >}}Opérateurs{{< /AppElement >}}.
4. Supprimez les opérateurs (des instructions sont fournies dans l'article [Gestion des opérateurs de sous-compte]({{< ref path="support/kb/account/users/sub-accounts/sub-account-operator-management" lang="fr" >}})). La colonne **Membre des groupes** vous aidera à identifier les opérateurs des sous-comptes.
5. Passez par le menu {{< AppElement type="menuitem" >}}Configuration de compte > Groupes de moniteurs{{< /AppElement >}}.
6. Cliquez pour ouvrir le groupe de moniteurs correspondant au sous-compte.
7. Cliquez sur {{< AppElement type="deletebutton" >}}Supprimer ce groupe de moniteurs{{< /AppElement >}}.
8. Revenez à la page de paramétrage des sous-comptes.
9. Cliquez sur {{< AppElement type="deletebutton" >}}Supprimer ce sous-compte{{< /AppElement >}}.

{{< callout >}}
**Remarque** : Si vous retirez les opérateurs d'un sous-compte sans les supprimer, ces opérateurs auront seulement un accès en lecture seule du compte principal. Suivez la procédure décrite ci-dessus pour éviter les opérateurs de sous-comptes orphelins.
{{< /callout >}}
