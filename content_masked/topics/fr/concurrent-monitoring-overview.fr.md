{
  "hero": {
    "title": "Vue d'ensemble de la surveillance simultanée"
  },
  "title": "Vue d'ensemble de la surveillance simultanée",
  "summary": "Page d'accueil pour toutes les informations sur la surveillance simultanée.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/surveillance-simultanee/vue-densemble-de-la-surveillance-simultanee",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false,
  "sectionlist": false
}

Dans Uptrends, la surveillance peut se faire de deux manières : standard ou simultanée.

La Surveillance Simultanée vous permet, pour un même moniteur, d'exécuter simultanément un certain nombre de vérifications à partir de différents points de contrôle, afin de décider plus rapidement et de manière plus fiable si une erreur peut être considérée comme une erreur confirmée. Dans cette section, vous trouverez des informations détaillées sur la configuration de la surveillance simultanée et sur la manière d'interpréter ses résultats afin d'obtenir une vue plus complète des performances et de la disponibilité de votre page.

## Comment est-ce que la surveillance simultanée m'aide ?

La surveillance simultanée présente plusieurs avantages par rapport à la surveillance standard.

- **La détection d'erreur et l'envoi d'alertes sont plus rapides :** La détection des erreurs devient plus flexible grâce à la surveillance simultanée. C'est vous qui décidez combien d'échecs (de vérification) constituent une erreur, donc des alertes peuvent être envoyées instantanément dès le premier test, plutôt que d'avoir à attendre un deuxième test pour confirmer l'erreur. Tout va plus vite, ce qui vous permet d'être plus efficace pour résoudre les éventuels problèmes.
- **Plus de données :** Les moniteurs simultanés fonctionnent aux mêmes intervalles que les moniteurs réguliers, mais au lieu d'exécuter une seule vérification, ils en exécutent plusieurs simultanément. Le nombre de vérifications individuelles augmente sensiblement, ce qui vous aide à mieux affiner les métriques de disponibilité et de performance pertinentes.
- **Fiabilité supérieure :** Les erreurs intermittentes ou localisées peuvent être difficiles à détecter. Il est possible qu'un problème ait disparu au moment de la deuxième vérification, ou que le deuxième point de contrôle ne rencontre pas le même problème. Ces incertitudes disparaissent avec les vérifications simultanées - ce qui signifie que si un moniteur simultané signale une erreur, vous pouvez être certain que quelque chose ne va pas.
