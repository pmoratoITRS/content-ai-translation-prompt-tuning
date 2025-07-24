{
  "hero": {
    "title": "Spécification des régions pour les points de contrôle"
  },
  "title": "Spécification des régions pour les points de contrôle",
  "summary": "Comment spécifier vos points de contrôle lorsque votre compte vous limite à des régions entières.",
  "url": "[URL_BASE_TOPICS]api/specification-des-regions-pour-les-points-de-controle",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les comptes qui peuvent sélectionner seulement des régions entières pour les moniteurs de leurs points de contrôle (par opposition à une sélection sans restriction des points de contrôle individuels), doivent spécifier une valeur particulière lors de la création ou la mise à jour des moniteurs dans l'API.

  
Dans le champ Checkpoints (qui consiste normalement en une liste d'identifiants, séparés par des virgules, des points de contrôle), spécifiez l'une de ces phrases:

-   Europe uniquement : `[INLINE_CODE_1]{"Regions":[1004]}[INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]{"Regions":[1005]}[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]{"Regions":[1004,1005]}[INLINE_CODE_8]`
