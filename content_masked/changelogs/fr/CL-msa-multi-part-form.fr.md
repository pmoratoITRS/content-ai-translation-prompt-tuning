{
  "title": "L'option Multi-part form est désormais disponible avec les moniteurs d'API multi-étapes",
  "date": "2025-01-08",
  "url": "[URL_BASE_CHANGELOG]janvier-2025-multi-part-form-moniteurs-api-multi-étapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lors de la [configuration d'un moniteur d'API multi-étapes]([LINK_URL_1]), vous pouvez préciser la charge utile (c'est-à-dire les données envoyées) dans une définition de requête. Auparavant, Uptrends prenait en charge uniquement un type de contenu à la fois, bien que le protocole HTTP permette d'envoyer plusieurs parties. Par exemple, dans un même appel d'API, vous pouvez envoyer du texte brut et un fichier binaire.

Avec la nouvelle option **Multi-part form**, vous pouvez désormais inclure plusieurs types de contenu dans le corps de requête des étapes de votre moniteur d'API multi-étapes. Cette option paramètre automatiquement l'en-tête de requête [INLINE_CODE_1] sur [INLINE_CODE_2], ce qui vous permet de spécifier plusieurs contenus de différents types. Ces types de contenus peuvent être des textes bruts ou des fichiers récupérés dans le [coffre-fort]([LINK_URL_2]).

![Option Multi-part form dans le moniteur d'API multi-étapes]([LINK_URL_3])