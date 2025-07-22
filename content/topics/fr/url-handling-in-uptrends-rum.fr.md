{
  "hero": {
    "title": "Gestion des URL dans Uptrends RUM"
  },
  "title": "Gestion des URL dans Uptrends RUM",
  "summary": "Vous êtes-vous déjà demandé comment Uptrends gère les URL dans RUM ? Lisez cet article !",
  "url": "/support/kb/rum/gestion-url-dans-uptrends-rum",
  "translationKey": "https://www.uptrends.com/support/kb/rum/url-handling-in-uptrends-rum"
}

Uptrends RUM vous permet de visualiser les mesures de performance de vos utilisateurs véritables dans de nombreux groupements différents. Le regroupement par page vous donne un excellent aperçu des statistiques pour des pages spécifiques qui peuvent nécessiter une attention particulière en raison de problèmes tels que des temps de chargement lents.

Uptrends examine l'URL pour déterminer quelle page votre visiteur a consultée. De nombreux sites web modernes utilisent des URL générées automatiquement, ce qui peut conduire à un nombre extrêmement élevé d'URL uniques. Comme il ne serait pas utile de recueillir des données pour des dizaines de milliers de pages, **nous avons plafonné le nombre maximal de pages uniques par site web à 10 000 par défaut**. Lorsque vous dépassez ce nombre, nous enregistrons les nouvelles pages uniques sous une rubrique "Autres".

## Normalisation des URL

Pour réduire le nombre d'URL uniques dont nous devons assurer le suivi tout en séparant correctement les différentes pages de votre site web, nous appliquons un **processus de normalisation des URL**. La normalisation des URL signifie que les URL que vous voyez dans le RUM d'Uptrends peuvent différer légèrement des URL réelles que votre site web utilise. En particulier, nous :

- Ignorons la différence entre `http://` et `https://`
- Supprimons la chaîne de requête (par exemple, `?paramètre=valeur` à la fin)
- Supprimons les fragments (par exemple, `#fragment` à la fin), sauf si l'option **Inclure un fragment d'URL** est activée dans les paramètres du site web RUM
- Supprimons les doubles barres obliques de la partie path de l'URL
- Remplaçons les segments (parties du chemin délimitées par des barres obliques) entièrement constitués de chiffres ou de GUID par des astérisques (`***`)
- Remplaçons les grands nombres (&gt;4 chiffres) et les GUID dans les segments par des astérisques. Par example, `www.mysite.com/coupon-12345` et `www.mysite.com/coupon-123456` deviennent tous les deux `www.mysite.com/coupon-***`  
   Des URL avec des GUID tels que `www.mysite.com/coupon-19740f6e-e7e6-41f2-84e4-de0b290eb05e` deviennent `www.mysite.com/coupon-***` avec les trois astérisques remplaçant l'ensemble du GUID.

## Commentaires

Vos questions et vos commentaires sont les bienvenus. N'hésitez pas à [nous contacter](/contact), surtout si vous remarquez qu'Uptrends RUM ne suit pas de manière optimale les différentes pages de votre site web.
