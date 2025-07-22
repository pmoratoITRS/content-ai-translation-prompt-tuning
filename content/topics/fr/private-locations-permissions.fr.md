{
"hero": {
"title": "Configuration des autorisations liées aux emplacements privés"
},
"title": "Configuration des autorisations liées aux emplacements privés",
"summary": "Cet article vous explique comment configurer les autorisations liées aux emplacements privés pour les opérateurs et les groupes d'opérateurs.",
"url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/autorisations-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-permissions",
"sectionlist": false,
"tableofcontents": false
}

Les [emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="fr" >}}) vous permettent d'exécuter des vérifications de moniteur à l'intérieur de votre serveur et de votre pare-feu, ce qui les distingue des [checkpoints publics par défaut d'Uptrends]({{< ref path="/checkpoints" lang="fr" >}}). Pour chaque emplacement privé, les opérateurs peuvent créer, mettre à jour, désactiver et supprimer des checkpoints. Pour des raisons de sécurité et de confidentialité, il est essentiel de contrôler le niveau de visibilité et les autorisations des différents opérateurs.

Les **autorisations liées aux emplacements privés** vous permettent de définir les droits des opérateurs et des groupes d'opérateurs.

Pour gérer les droits liés aux emplacements privés :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs et groupes {{< /AppElement >}}.
2. Sélectionnez les opérateurs ou les groupes d'opérateurs dont vous souhaitez gérer les autorisations liées aux emplacements privés.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
4. Dans les **autorisations liées aux emplacements privés**, sélectionnez l'une des options suivantes :

- **Créer des emplacements privés** : cette option autorise les opérateurs et les groupes d'opérateurs à consulter et à créer des emplacements privés.
- **Utiliser l'emplacement privé** : sélectionnez un emplacement privé dans le menu déroulant et faites glisser le curseur pour permettre aux opérateurs et aux groupes d'opérateurs de sélectionner l'emplacement privé en tant que checkpoint pour exécuter les moniteurs.
- **Éditer l'emplacement privé** : sélectionnez un emplacement privé dans le menu déroulant et faites glisser le curseur pour permettre aux opérateurs et aux groupes d'opérateurs de consulter, de modifier et de supprimer des emplacements privés. Les opérateurs ayant cette autorisation peuvent aussi sélectionner l'emplacement privé en tant que checkpoint pour exécuter les moniteurs.

Par défaut, tous les administrateurs disposent de tous les droits liés aux emplacements privés. Les opérateurs ayant les autorisations **Utiliser** ou **Éditer** peuvent sélectionner des emplacements privés dans l'onglet {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} du moniteur. Les opérateurs ayant les autorisations **Créer** ou **Éditer** peuvent accéder aux emplacements privés depuis le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.

![GIF Droits liés aux emplacements privés](/img/content/gif-private-locations-permissions.gif)