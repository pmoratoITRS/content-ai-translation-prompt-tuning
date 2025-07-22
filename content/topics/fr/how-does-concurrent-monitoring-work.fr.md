{
  "hero": {
    "title": "Comment fonctionne la surveillance simultanée ?"
  },
  "title": "Comment fonctionne la surveillance simultanée ?",
  "summary": "Vue d'ensemble de la surveillance simultanée",
  "url": "/support/kb/surveillance-synthetique/surveillance-simultanee/comment-fonctionne-surveillance-simultanee",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/how-does-concurrent-monitoring-work"
}

Dans Uptrends, il existe deux façons de surveiller le temps de fonctionnement, les performances et le comportement correct de vos sites web, services web et serveurs : la surveillance standard et la surveillance simultanée.

## Surveillance standard

Une vérification de moniteur est effectuée à partir d'un point de contrôle. Si une erreur se produit, c'est considéré comme une erreur non confirmée. Immédiatement après, la même vérification de moniteur est effectuée à partir d'un point de contrôle différent. Si la même erreur est de nouveau reçue, le résultat est une erreur confirmée. Seules les erreurs confirmées peuvent donner lieu à des alertes et des messages (SMS, courrier électronique, Slack, autres systèmes tiers).

## Surveillance simultanée

Un certain nombre de vérifications de moniteur sont effectués en même temps (simultanément) plutôt que l'une après l'autre. C'est vous qui définissez le nombre de contrôles effectués simultanément et à partir de quels points de contrôle.

Il existe également deux limites qui correspondent à un pourcentage des points de contrôle renvoyant une erreur : une limite pour le cas où une erreur est considérée comme une erreur non confirmée et une autre limite pour le cas où une erreur est considérée comme une erreur confirmée. C'est à vous de décider quel pourcentage est suffisant pour signaler une erreur. Si le premier niveau (par exemple 30 %) est atteint, l'erreur est classée comme une erreur non confirmée. Si le deuxième niveau est atteint (par exemple 60 %), vous verrez une erreur confirmée.

Lorsqu'un pourcentage significatif (défini par l'utilisateur) de contrôles a renvoyé une erreur, le résultat est immédiatement une erreur confirmée. Une alerte peut être générée et une notification envoyée rapidement.

## Domaine d'application

La surveillance simultanée fonctionne dans le cadre suivant :

- Elle est disponible pour tous les types de moniteurs.
- Les contrôles faits par le moniteur doivent être effectués aux fréquences de surveillance habituelles, qui sont de 1 minute pour les moniteurs de base et de 5 à 15 minutes pour les moniteurs de navigateurs.
- Pour la surveillance simultanée, des règles spéciales s'appliquent pour la sélection des points de contrôle : soit au moins 5 choisis parmi tous les points de contrôle, soit au moins 3 choisis parmi les points de contrôle marqués comme étant à *haute disponibilité*. Les points de contrôle à *haute disponibilité* sont généralement les emplacements où plus d'un serveur est disponible.
- Dans tous les cas, le nombre maximum de points de contrôle sélectionnés est de 50.

## Résultats de surveillance

Sur la base de contrôles simultanés, Uptrends calcule une mesure globale (avec des métriques de base). Les données peuvent être utilisées comme celles d'autres moniteurs, par exemple dans des tableaux de bord, dans les alertes ou les calculs SLA.

Les mesures individuelles seront disponibles à ces endroits :

- Le *Journal du moniteur*
- Lorsque vous consultez la mesure globale dans le *Journal du moniteur*, vous obtenez une fenêtre contextuelle (popup) qui pointe vers les mesures partielles.
- Pour chaque mesure individuelle, nous enregistrerons les informations de débogage habituelles (captures d'écran, cascades, traceroute, etc.)

## Avantages et inconvénients

Les avantages de la surveillance simultanée sont une détection d'erreur plus rapide et une fiabilité plus élevée. Notez que cette dernière dépend du nombre de points de contrôle utilisés.

Un inconvénient possible (pour certains) est que nous n'agrégions pas les étapes de transaction (pour les transactions) et que nous ne calculions pas une moyenne de la cascade à des fins de reporting (pour les FPC, full page checks).

La surveillance simultanée a un prix plus élevé. Cependant, vous obtiendrez en retour une détection plus rapide et une plus grande fiabilité. Consultez les exemples ci-dessous pour vous faire une idée des prix.

## Formules d'abonnement

La fonctionnalité sera disponible dans les plans d'abonnement suivants : Business et Enterprise.  
Si vous voulez utiliser la surveillance simultanée, vous devez choisir individuellement les points de contrôle pour les vérifications. C'est possible dans les plans Business et Enterprise. Les autres plans ne proposent pas cette option et ne sont donc pas adaptés à la surveillance simultanée.

Le calcul des crédits utilisés pour la surveillance simultanée est expliqué dans l'article de la base de connaissance [Tarification pour la surveillance simultanée]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring/pricing-calculation-examples" lang="fr" >}}).