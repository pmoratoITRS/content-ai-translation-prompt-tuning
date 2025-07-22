{
  "hero": {
    "title": "Vérification de base des pages comparé aux Real Browser Checks"
  },
  "title": "Vérification de base des pages web comparé aux Real Browser Checks",
  "summary": "Découvrez la différence entre une vérification de base d’une page web et celle qui utilise un navigateur réel.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/verification-de-base-des-pages-compare-aux-real-browser-checks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

En ce qui concerne le [Monitoring Synthétique]([LINK_URL_1]), vous avez deux choix pour surveiller votre page web : les vérifications de base et les vérifications qui utilisent un vrai navigateur. Alors, quelle est la différence entre ces deux types de moniteurs ? La principale différence est la façon dont Uptrends gère la réponse.

#### La réponse rapide

Les vérifications de base ne regardent que la réponse initiale ; des éléments de la page comme les scripts, fichiers CSS et les images ne sont jamais récupérés ou exécutés. Le Real browser check (vérification par un vrai navigateur) charge le contenu de la page entière (scripts, fichiers CSS, images et contenu tiers) dans une fenêtre de navigateur réel.

## La vérification de base

Lorsqu'un point de contrôle effectue une vérification de base (HTTP/HTTPS), le point de contrôle envoie une requête pour la page. Le point de contrôle reçoit la réponse et examine quelques composants clés. En fonction des paramètres de votre moniteur, une vérification de base peut examiner :

-   le code de résultat
-   le temps de réponse
-   la longueur de la page en octets
-   des correspondances de contenu (chaînes de caractères)

Le moniteur ne charge jamais le contenu de la réponse dans un navigateur, donc les éléments de la page comme les fichiers CSS, les fichiers script, le contenu tiers et les images ne sont jamais téléchargés, analysés et chargés. Avec une vérification de base, vous ne saurez pas si des erreurs ou problèmes de performance peuvent survenir lors de la récupération et du chargement du contenu complet. Ce que vous savez, c'est que le site est disponible, qu'il renvoie des codes acceptables, qu'il a une taille minimale et qu'il inclut le contenu spécifié. Une vérification de base peut avoir lieu aussi souvent qu'une fois par minute, ce qui donne une idée assez précise de la disponibilité de la page.

## Real browser checks

Lorsqu'un point de contrôle effectue un Real browser check ([Full Page Check]([LINK_URL_2]), [Transaction Monitor]([LINK_URL_3])), le point de contrôle demande la page et charge la réponse dans un vrai navigateur. Le point de contrôle charge le contenu entier de la page (CSS, fichiers de script, fichiers HTML supplémentaires, contenu tiers et images). Chaque requête et réponse est vérifiée pour mesurer performances et détecter les erreurs. Ces vérifications par navigateur réels sont planifiées aussi souvent qu'une fois toutes les cinq minutes, ce qui simule assez bien l'expérience réel d'un utilisateur avec votre page. Une telle vérification par navigateur réel peut vous donner une idée de la disponibilité de la page, mais avec moins de précision qu'une vérification de base.
