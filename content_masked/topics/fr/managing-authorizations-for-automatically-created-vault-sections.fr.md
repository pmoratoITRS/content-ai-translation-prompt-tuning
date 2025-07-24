{
  "hero": {
    "title": "Gestion des autorisations pour les sections de coffre-fort créées automatiquement"
  },
  "title": "Gestion des autorisations pour les sections de coffre-fort créées automatiquement",
  "summary": "Lorsque vous enregistrez une transaction, Uptrends stocke vos informations sensibles dans une section du coffre-fort créée automatiquement avec des autorisations par défaut. Découvrez comment gérer les autorisations pour les éléments de coffre-fort créés automatiquement.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/gestion-autorisations-sections-automatiques-coffre-fort",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le [coffre-fort]([LINK_URL_1]) d'Uptrends vous offre un emplacement sécurisé pour stocker les certificats et les clés publiques ainsi que les informations d'identification nécessaires pour vos scripts de transaction. Lorsque vous créez un nouveau moniteur de transactions à l'aide de l'enregistreur de transactions ou si le service Support convertit un ancien moniteur au nouveau format de surveillance des transactions en libre-service, Uptrends place vos données sensibles dans le coffre-fort automatiquement. Votre script accédera à ces éléments du coffre-fort plutôt que d'avoir les valeurs sensibles visibles dans le script ou dans vos rapports ([en savoir plus]([LINK_URL_2]) sur la façon d'utiliser des valeurs sensibles dans votre script).

## Autorisations par défaut utilisées

Les éléments dans le coffre-fort sont stockés dans des sections. L'accès ou la modification des éléments dans chaque section du coffre-fort ne peut se faire que par les opérateurs (ou membres des [groupes d'opérateurs]([LINK_URL_3])) qui figurent dans la section *Autorisations*.

**Les nouveaux enregistrements et les scripts nouvellement convertis ont les autorisations par défaut appliquées aux nouvelles sections de coffre-fort créées automatiquement**. Les autorisations par défaut sont données au groupe Administrateurs et au groupe d'utilisateurs du sous-compte, le cas échéant.

Les nouveaux enregistrements téléchargés sont toujours mis dans une section de coffre-fort créée automatiquement avec les autorisations par défaut. Si vous avez modifié les autorisations, le prochain téléchargement crée une nouvelle section qui utilise les autorisations par défaut.

[SHORTCODE_1]
**Remarque** : pour éviter d'avoir de multiples sections générées automatiquement, laissez les autorisations définies aux valeurs par défaut, copiez les éléments de ces sections du coffre-fort dans une section personnalisée, puis supprimez-les de la section générée automatiquement.
[SHORTCODE_2]

## Modification des autorisations par défaut

Vous pouvez modifier les autorisations par défaut de n'importe laquelle de vos sections de coffre-fort pour les rendre plus ou moins restrictives en incluant ou en excluant des groupes ou des opérateurs.

1. Allez à [SHORTCODE_3] Configuration de compte > Coffre-fort [SHORTCODE_4].
2. Cliquez sur la section pour laquelle vous souhaitez modifier les autorisations.
3. Dans la tuile **Autorisations**, pour supprimer les autorisations, cliquez sur *Supprimer* à droite d'un opérateur ou d'un groupe.
4. Pour ajouter des autorisations, cliquez sur [SHORTCODE_5]\+ Ajouter une autorisation[SHORTCODE_6].
5. Sélectionnez le groupe ou l'opérateur.
6. Définissez le *Niveau d'autorisation* à *Voir seulement* ou *Contrôle complet*.
7. Cliquez sur [SHORTCODE_7] Ajouter [SHORTCODE_8].

![]([LINK_URL_4])
