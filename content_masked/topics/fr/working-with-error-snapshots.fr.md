{
  "hero": {
    "title": "Utiliser les captures d'écran d'erreurs"
  },
  "title": "Utiliser les captures d'écran d'erreurs",
  "summary": "Les captures d'écran d'erreurs peuvent vous aider à résoudre les problèmes. Cet article vous indique où les trouver.",
  "url": "[URL_BASE_TOPICS]alerter/erreurs/travailler-avec-des-instantanes-derreur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Votre site web est en panne, mais vous ne savez pas pourquoi. En vous connectant à votre compte de surveillance de site web Uptrends, vous pouvez voir si vos utilisateurs rencontrent des problèmes de connexion. Où exactement ? Dans les détails des erreurs signalées par vos moniteurs, et dans les captures d'écran d'erreurs.

## Qu'est-ce qu'une capture d'écran d'erreur ?

Une capture d'écran d'erreur est une capture d'écran prise par le service d'Uptrends pour vous montrer ce qui se produit dans le navigateur lorsque vos utilisateurs rencontrent un problème.

![capture d'écran d'une fenêtre Voir les détails incluant une capture d'écran d'erreur]([LINK_URL_1])

## Comment fonctionnent les captures d'écran d'erreurs ?

Uptrends prend des captures d'écran d'erreurs dans certaines situations.

- Cette fonctionnalité est disponible uniquement avec les moniteurs **HTTP(S)**, les moniteurs **Web Service (HTTP(S))** et les **moniteurs de transactions**.
- Uptrends prend des captures d'écran pour certains types d'erreurs seulement (par exemple, c'est le cas des erreurs de correspondance, mais pas des erreurs de limites de performance). Si l'erreur est liée à l'infrastructure, comme une erreur de connexion TCP, il n'y a pas de contenu à afficher.
- Le service Uptrends crée des captures d'écran uniquement pour les erreurs confirmées, mais seulement **la première fois** qu'elles se produisent. Les erreurs suivantes ne font pas l'objet d'une capture d'écran. [SHORTCODE_1]**Remarque** : Les captures d'écran peuvent mettre quelques minutes à s'afficher après que l'erreur est survenue. Selon le contenu reçu par Uptrends, la capture d'erreur est parfois indisponible.[SHORTCODE_2]
