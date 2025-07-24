{
  "hero": {
    "title": "Gestion des erreurs dans les moniteurs d'API multi-étapes"
  },
  "title": "Gestion des erreurs dans les moniteurs d'API multi-étapes",
  "summary": "Cet article vous explique comment gérer et ignorer les erreurs dans les moniteurs d'API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/gestion-erreurs-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lorsque vos moniteurs d'API effectuent des tests ou des modifications, vos serveurs web peuvent présenter des comportements dynamiques inattendus. Parmi ces comportements, les expirations de délai de réponse et les échecs d'assertion peuvent empêcher vos moniteurs de traiter d'autres requêtes.

Par exemple, imaginons que vous ayez configuré un moniteur d'API multi-étapes pour récupérer des informations auprès d'une plateforme d'e-commerce. Ce moniteur inclut quatre étapes de requête /GET dans l'ordre suivant :

1. GET /product : fournit tous les produits et les informations les concernant.
2. GET /products/{productID} : fournit un produit spécifique et les informations le concernant.
3. GET /users : fournit tous les utilisateurs et les informations les concernant.
4. GET /users/{userID} : fournit un utilisateur spécifique et les informations le concernant.

La configuration ci-dessus montre que la première et la deuxième étapes fournissent des informations sur les produits, tandis que la troisième et la quatrième fournissent des informations sur les utilisateurs. Si vous exécutez ce moniteur et que l'étape 2 échoue à cause d'une erreur, comme l'expiration d'un délai de requête ou un changement dans un nom d'endpoint, l'erreur empêche le moniteur d'exécuter les étapes suivantes.

C'est là que la fonctionnalité **Gestion des erreurs** peut vous aider. Même si l'étape 2 a causé une erreur, vous pouvez récupérer les informations des étapes 3 et 4, car elles ne dépendent pas des précédentes requêtes /GET. L'erreur ne doit pas empêcher votre moniteur d'exécuter les étapes suivantes.

## Gestion des erreurs

La fonction **Gestion des erreurs** des moniteurs d'API multi-étapes vous permet de contrôler et de gérer vos erreurs d'API de façon flexible. Pour chaque étape de votre moniteur d'API multi-étapes, vous pouvez cocher la case **Continuer l'exécution et ignorer les erreurs** pour ignorer les erreurs survenues lors de cette étape.

![Case à cocher Gestion des erreurs dans le moniteur d'API multi-étapes]([LINK_URL_1])

Une fois cette option activée, si une erreur survient lors d'une étape, votre moniteur ignore automatiquement cette étape et passe à la suivante. Votre moniteur ignore les erreurs, ce qui signifie que ces dernières ne sont pas enregistrées ou visibles dans votre dashboard [Vue d'ensemble des erreurs]([LINK_URL_2]) ni dans vos [rapports]([LINK_URL_3]). Les erreurs ignorées s'affichent uniquement dans la fenêtre contextuelle **Voir les détails** lorsque vous utilisez la fonction **Tester maintenant** et dans les journaux de moniteurs.

Pour présenter ce concept autrement, l'image ci-dessous montre le résultat du moniteur pour la situation décrite ci-dessus. Comme vous pouvez le voir, l'étape 2 a échoué en raison d'une erreur 404 "page introuvable". Si la case **Continuer l'exécution et ignorer les erreurs** est décochée, le moniteur s'interrompt lorsqu'il rencontre une erreur (ici, à l'étape 2). Cette erreur bloque l'exécution du moniteur et les étapes suivantes ne sont pas exécutées.

![Désactivation de la gestion des erreurs dans le moniteur MSA]([LINK_URL_4])

En revanche, si vous cochez la case **Continuer l'exécution et ignorer les erreurs** à l'étape 2, le moniteur ignore cette étape et poursuit la vérification lors des étapes suivantes :

![Activation de la gestion des erreurs dans le moniteur MSA]([LINK_URL_5])

## Articles liés

Pour vous informer sur la gestion des erreurs dans les moniteurs de transactions, vous pouvez lire l'article de notre base de connaissances intitulé [Ignorer les erreurs pour les étapes et actions facultatives]([LINK_URL_6]).
