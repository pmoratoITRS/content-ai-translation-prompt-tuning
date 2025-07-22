{
  "hero": {
    "title": "Spécification des régions pour les points de contrôle"
  },
  "title": "Spécification des régions pour les points de contrôle",
  "summary": "Comment spécifier vos points de contrôle lorsque votre compte vous limite à des régions entières.",
  "url": "/support/kb/api/specification-des-regions-pour-les-points-de-controle",
  "translationKey": "https://www.uptrends.com/support/kb/api/specifying-checkpoint-regions"
}

Les comptes qui peuvent sélectionner seulement des régions entières pour les moniteurs de leurs points de contrôle (par opposition à une sélection sans restriction des points de contrôle individuels), doivent spécifier une valeur particulière lors de la création ou la mise à jour des moniteurs dans l'API.

  
Dans le champ Checkpoints (qui consiste normalement en une liste d'identifiants, séparés par des virgules, des points de contrôle), spécifiez l'une de ces phrases:

-   Europe uniquement : `` `{"Regions":[1004]}` ``
-   Amérique du Nord uniquement : `` `{"Regions":[1005]}` ``
-   Les deux : laisser le champ vide, ou spécifier `` `{"Regions":[1004,1005]}` ``
