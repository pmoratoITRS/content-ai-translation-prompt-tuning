{
"title": "L'option Multi-part form est désormais disponible avec les moniteurs d'API multi-étapes",
"date": "2025-01-08",
"url": "/changelog/janvier-2025-multi-part-form-moniteurs-api-multi-étapes",
"translationKey": "https://www.uptrends.com/changelog/january-2025-msa-multi-part-form"
}

Lors de la [configuration d'un moniteur d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}), vous pouvez préciser la charge utile (c'est-à-dire les données envoyées) dans une définition de requête. Auparavant, Uptrends prenait en charge uniquement un type de contenu à la fois, bien que le protocole HTTP permette d'envoyer plusieurs parties. Par exemple, dans un même appel d'API, vous pouvez envoyer du texte brut et un fichier binaire.

Avec la nouvelle option **Multi-part form**, vous pouvez désormais inclure plusieurs types de contenu dans le corps de requête des étapes de votre moniteur d'API multi-étapes. Cette option paramètre automatiquement l'en-tête de requête `Content-Type` sur `multipart/form-data`, ce qui vous permet de spécifier plusieurs contenus de différents types. Ces types de contenus peuvent être des textes bruts ou des fichiers récupérés dans le [coffre-fort]({{< ref path="/support/kb/account/vault" lang="fr" >}}).

![Option Multi-part form dans le moniteur d'API multi-étapes](/img/content/scr-multi-part-form-msa.min.png)