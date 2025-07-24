{
  "hero": {
    "title": "Valeurs dynamiques dans les URL et les requêtes POST"
  },
  "title": "Valeurs dynamiques dans les URL et les requêtes POST",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/valeurs-dynamiques-dans-url-et-requetes-posts",
  "summary": "Cet article vous explique comment utiliser les valeurs dynamiques dans les URL ou les corps de requête.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Valeur dynamique dans les URL ou les corps de requête

Pour la plupart des types de moniteurs, Uptrends peut générer des [valeurs de date dynamiques]([LINK_URL_1]) dans les URL ou le contenu des requêtes HTTP. Les horodatages sont souvent utilisés d'une part parce qu'il s'agit de valeurs uniques et d'autre part parce qu'ils contiennent des informations sur la date et l'heure d'exécution de la requête. Cela peut être utile pour les services web qui nécessitent qu'une valeur différente soit saisie dans le corps de la requête HTTP POST ou dans l'URL de requête, par exemple :

[INLINE_CODE_1]

Plutôt que d'entrer une date de valeur fixe, nous pouvons utiliser la notation suivante pour générer des valeurs en fonction de la date/heure d'aujourd'hui :

[INLINE_CODE_2]

Il convient de noter que **d'autres formats sont également possibles**. De plus, nous pouvons utiliser des décalages pour calculer des valeurs différentes. Pour en savoir plus sur la notation et l'application de décalages à vos valeurs de date, consultez notre article sur les [variables automatiques]([LINK_URL_2]).


## Méthode du cache busting

**La mise en cache du contenu** peut être extrêmement utile pour les webmasters, car elle permet d'améliorer les performances générales en utilisant moins de ressources sur la durée. Mais si vous surveillez un site web ou un service web, la mise en cache peut vous gêner lorsque vous cherchez à déterminer si un de vos éléments de page est disponible ou non.

En insérant une valeur d'URL aléatoire, vous pouvez intervenir sur les appels *HTTP*, *Web Service* ou *Full Page Check* pour vous assurer qu'aucun contenu précédent ne se trouve dans le cache.

[SHORTCODE_1]
**Remarque :** Les informations suivantes concernant le cache de votre serveur et non pas du service de surveillance web d'Uptrends.
[SHORTCODE_2]

### Comment fonctionne le cache busting ?

Le cache busting se base sur l'utilisation du jeton [INLINE_CODE_3] (pour en savoir plus, voir notre article sur les [variables automatiques)]([LINK_URL_3]). Pour utiliser cette fonctionnalité, il vous suffit d'inclure le jeton dans l'URL saisie dans les paramètres du moniteur. Par exemple :

[INLINE_CODE_4]

Cela produit un résultat de ce type :

[INLINE_CODE_5]
