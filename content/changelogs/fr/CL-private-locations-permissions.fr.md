{
"title": "Présentation des droits liés aux emplacements privés",
"date": "2025-01-29",
"url": "/changelog/janvier-2025-droits-emplacements-prives",
"translationKey": "https://www.uptrends.com/changelog/january-2025-private-locations-permissions"
}

Les [emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="fr" >}}) vous permettent d'exécuter des vérifications de moniteur à l'intérieur de votre serveur et de votre pare-feu, ce qui les distingue des [checkpoints publics par défaut d'Uptrends]({{< ref path="/checkpoints" lang="fr" >}}).

Par défaut, tous les opérateurs ont accès à tous les emplacements de checkpoints privés. Les opérateurs peuvent créer, mettre à jour, désactiver et supprimer des checkpoints à tout moment. Il est essentiel de gérer le niveau de visibilité et les droits des différents opérateurs.

Avec la nouvelle fonction de **gestion des emplacements privés**, vous pouvez définir des autorisations pour certains opérateurs et groupes d'opérateurs :

- Créer : cette option autorise les opérateurs à consulter et à créer des emplacements privés.
- Éditer : cette option autorise les opérateurs et les groupes d'opérateurs à consulter, modifier et supprimer des emplacements privés.
- Utiliser : cette option autorise les opérateurs et les groupes d'opérateurs à sélectionner l'emplacement privé en tant que checkpoint pour exécuter les moniteurs.

Si un opérateur possède l'une des autorisations ci-dessus, l'emplacement privé est visible dans l'onglet {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} du moniteur et accessible depuis le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.

![GIF Droits liés aux emplacements privés](/img/content/gif-private-locations-permissions.gif)