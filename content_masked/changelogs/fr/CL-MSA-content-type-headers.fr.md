{
  "title": "Ajout automatique d'en-têtes Content-Type dans les moniteurs d'API multi-étapes",
  "date": "2024-01-17",
  "url": "[URL_BASE_CHANGELOG]janvier-2024-en-tete-content-type-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Notre type de moniteur [API multi-étapes]([LINK_URL_1]) permet aux utilisateurs d'interagir directement avec leurs principales API. Pour certains cas clients liés à la surveillance, les données doivent être envoyées à l'API, par exemple lors de l'exécution d'une requête POST pour créer un nouvel objet, ou d'une requête PUT/PATCH pour modifier un objet existant. Dans ces cas, il est important d'inclure un en-tête [INLINE_CODE_1] pour informer l'API de destination du type de données à venir (JSON, XML, form data, etc.). Ainsi, l'API sait comment analyser la requête. Généralement, la réception d'un corps de requête sans en-tête [INLINE_CODE_2] engendre une erreur de la part de l'API.

Jusqu'à présent, ces en-têtes devaient être ajoutés manuellement dans les étapes du moniteur d'API multi-étapes. Désormais, Uptrends détecte automatiquement le type de contenu et ajoute l'en-tête [INLINE_CODE_3] approprié, selon que le corps de requête contient des données JSON, XML ou des données de formulaire. Ce changement aidera les utilisateurs à configurer des requêtes POST, PUT et PATCH dans leurs moniteurs d'API multi-étapes.