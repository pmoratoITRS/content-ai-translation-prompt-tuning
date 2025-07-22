{
"hero": {
"title": "Configuration des sous-comptes"
},
"title": "Configuration des sous-comptes",
"summary": "Dans cet article, nous décrivons le processus de configuration d'un nouveau sous-compte.",
"url": "/support/kb/compte/utilisateurs/les-sous-comptes/configuration-d-un-sous-compte",
"translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/sub-account-set-up"
}

## Création d'un sous-compte

Pour créer un nouveau sous-compte :

1. Ouvrez le hub des opérateurs en sélectionnant ({{< AppElement type="menuitem" >}}Configuration de compte > Opérateurs, groupes et sous-comptes{{< /AppElement >}}).
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Ajouter un sous-compte {{< /AppElement >}} dans la section des sous-comptes.

Renseignez ensuite les informations dans les onglets de la page *Nouveau sous-compte*.

## Principal
### Info sous-compte

1. Donnez un **Nom de sous-compte**. Lors de l'enregistrement, ce nom sera également utilisé pour générer un groupe de moniteurs et un groupe d'opérateurs.
2. Ajoutez une **Référence personnalisée** si vous le souhaitez.

### Autorisation

Dans cette section, vous définissez si les opérateurs de sous-comptes peuvent modifier ou ajouter des moniteurs.

1. Cochez la case **Autoriser la modification de moniteurs** pour permettre aux opérateurs d'ajuster les paramètres des moniteurs. L'activation de cette fonctionnalité permet également aux titulaires de sous-comptes d'ajouter des opérateurs supplémentaires, sans toutefois pouvoir supprimer les opérateurs.
2. Cochez la case **Autoriser l'ajout de moniteurs** si vous souhaitez autoriser les opérateurs de sous-compte à configurer leurs propres moniteurs. Si vous leur permettez d'installer des moniteurs, indiquez-en le nombre dans le champ **Nombre maximum de moniteurs**.

{{< callout >}}
**Remarque**: Lors de l'ajout d'un moniteur par un sous-compte, la création du nouveau moniteur n'est possible que s'il reste des moniteurs inutilisés dans le compte principal. Si le compte principal n'a pas assez de moniteurs disponibles, le sous-compte ne peut pas en ajouter de nouveaux, même s'il n'a pas atteint le nombre maximal de moniteurs.
{{< /callout >}}

### Informations sur les nouveaux moniteurs

La création d'un sous-compte nécessite de fournir les informations applicables pour un moniteur HTTP/HTTPS. Sélectionnez le **Type de moniteur** et fournissez **l'URL du moniteur** pour le nouveau moniteur. Uptrends ajoutera ce moniteur à un groupe de moniteurs portant le même nom que le sous-compte.

## SLA

Si vous avez un accord de niveau de service (SLA) avec le nouveau titulaire du sous-compte, définissez les valeurs dans l'onglet {{< AppElement type="tab" >}}SLA{{< /AppElement >}}. Si vous avez besoin d'un rappel sur la configuration des SLA, consultez notre [section sur les SLA]({{< ref path="support/kb/dashboards-and-reporting/sla" lang="fr" >}}).

## Moniteurs supplémentaires

Dans l'onglet {{< AppElement type="tab" >}}Moniteurs supplémentaires{{< /AppElement >}} vous pouvez ajouter des moniteurs existants à ce sous-compte. Vous pourrez aussi y revenir plus tard pour y ajouter de nouveaux moniteurs.

## Opérateurs

Dans cet onglet, vous pouvez ajouter des opérateurs existants au sous-compte en les sélectionnant dans la liste. Les opérateurs de sous-compte ne peuvent appartenir qu'à leur propre groupe de sous-compte et au groupe *Tout le monde*.

## Enregistrer

Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour enregistrer les nouveaux paramètres.

{{< callout >}}
**Remarque** : Si vous voulez que vos opérateurs de sous-compte reçoivent des alertes, il vous faut configurer une nouvelle [définition d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}), et si vous prévoyez d'utiliser des SMS ou des alertes par téléphone ou message vocal, pensez à ajouter les numéros de téléphone portable dans les [paramètres de l'opérateur]({{< ref path="support/kb/account/users/operators/operator-groups" lang="fr" >}}).
{{< /callout >}}
