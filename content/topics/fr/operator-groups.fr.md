{
"hero": {
"title": "Groupes d'opérateurs"
},
"title": "Groupes d'opérateurs",
"summary": "Vous rencontrez des difficultés pour configurer vos groupes d'opérateurs ? Découvrez comment d'autres utilisateurs d'Uptrends ont organisé leurs groupes.",
"url": "/support/kb/compte/utilisateurs/operateurs/groupes-d-operateurs",
"translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-groups"
}

Lorsque vous configurez vos [opérateurs]({{< ref path="support/kb/account/users/operators" lang="fr" >}}) dans votre compte Uptrends, il peut être judicieux de créer des groupes d'opérateurs personnalisés. Les groupes d'opérateurs vous permettent d'attribuer plus facilement l'accès aux rapports personnalisés. De plus, ils sont très pratiques pour [configurer vos définitions d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}). Cet article vous présente les deux groupes d'opérateurs déjà inclus dans votre compte, ainsi que quelques exemples de la manière dont vous pouvez organiser vos groupes d'opérateurs.

Les groupes d'opérateurs sont l'endroit où vous accordez des autorisations aux utilisateurs dans l'application Uptrends. Pour en savoir plus, vous pouvez lire notre article sur les [autorisations]({{< ref path="support/kb/account/users/operators/permissions" lang="fr" >}}).

## Ajout d'un groupe d'opérateurs

Voici comment ajouter un nouveau groupe d'opérateurs :

1. Passez par le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}} pour ouvrir le hub de gestion des utilisateurs({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="fr" >}}).
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Ajouter un groupe d'opérateurs {{< /AppElement >}}.
3. Saisissez un nom pour le groupe d'opérateurs dans le champ **Description**.
4. Utilisez la liste déroulante **Opérateurs inclus dans ce groupe** pour ajouter ou supprimer un ou des opérateurs en cliquant sur la case à côté de leur nom. Un opérateur peut appartenir à plusieurs groupes d'opérateurs.
5. Quand vous avez terminé l'ajout d'opérateurs, cliquez sur le bouton {{< AppElement type="button" >}} Enregistrer {{< /AppElement >}}.

## Groupes d'opérateurs Tout le monde et Administrateurs

Au départ, vous avez deux groupes d'opérateurs : le groupe Tout le monde et le groupe Administrateurs. Ces deux groupes remplissent des fonctions très différentes.

### Tout le monde

Le groupe Tout le monde inclut tout le monde, comme son nom l'indique. Tous les opérateurs configurés sur votre compte apparaîtront dans ce groupe. Vous ne pouvez pas modifier le groupe d'opérateurs Tout le monde. Utilisez ce groupe lorsque vous souhaitez définir des droits d'accès communs à tous vos opérateurs.

### Administrateurs

Si vous ajoutez un opérateur à ce groupe, vous lui accordez tous les droits pour accéder à tous les aspects de votre compte Uptrends. Ces opérateurs peuvent modifier les moniteurs et les dashboards, ajouter et supprimer des opérateurs, définir et modifier les définitions d'alertes, modifier les paramètres de compte et consulter les factures et demandes de devis pour des crédits SMS et des moniteurs supplémentaires. Soyez prudent lorsque vous ajoutez des utilisateurs à ce groupe très exclusif.

## Groupes personnalisés

Si vous ne savez pas comment organiser vos opérateurs, regardez comment certains de nos autres utilisateurs ont configuré les groupes dans leurs comptes.

### D'après l'organigramme

L'organigramme de votre entreprise est probablement un bon exemple pour définir vos groupes d'opérateurs. Nous voyons fréquemment des groupes d'opérateurs basés sur les services ou les équipes. Par exemple, vous pouvez créer un groupe d'opérateurs pour votre équipe DevOps, votre équipe de support ou votre équipe de gestion. Il peut être utile de diviser ces groupes en sous-équipes, par exemple, support : première équipe, support : deuxième équipe et support : troisième équipe.

### D'après la fonction occupée par l'opérateur

Vous pouvez trouver utile (en particulier pour les alertes) de créer des groupes d'opérateurs selon la fonction de l'opérateur. Par exemple, il n'est pas très utile d'attribuer des problèmes liés à l'API à votre concepteur web. Vous créerez plutôt un groupe d'opérateurs API pour envoyer directement les alertes relatives à votre API à l'équipe compétente. Il en va de même pour les problèmes de base de données, les problèmes de performances et les problèmes d'infrastructure réseau.

### D'après les niveaux de réponse/support

Lors de la configuration de vos définitions d'alertes, vous pouvez créer des groupes en fonction des niveaux de réponse. Par exemple, en mettant en place des groupes d'opérateurs pour le premier, deuxième et troisième niveau de support. En combinant ces groupes avec les horaires de repos et les escalades d'alerte, chaque niveau de support recevra l'alerte à mesure que le problème persiste.

### D'après les fournisseurs et les clients

Vous pouvez créer des groupes en fonction des fournisseurs et des clients auxquels vous avez donné accès à vos rapports Uptrends. Peut-être avez-vous un accord avec votre fournisseur de CDN pour répondre directement aux problèmes liés au CDN. De plus, les clients qui dépendent de vos services peuvent avoir besoin de connaître votre disponibilité et vos performances en accédant directement à vos rapports. Placer ces opérateurs spéciaux dans leurs propres groupes d'opérateurs peut faciliter la gestion de l'accès.
