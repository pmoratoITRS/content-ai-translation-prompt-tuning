{
  "hero": {
    "title": "Obtenir des données de checkpoints au format JSON ou XML"
  },
  "title": "Obtenir des données de checkpoints au format JSON ou XML",
  "summary": "Avec l'API Uptrends, vous pouvez obtenir des informations sur les checkpoints sous plusieurs formats.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/points-de-controle/donnees-checkpoints-formats-json-csv-et-xml",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le téléchargement de données relatives aux checkpoints sous format JSON ou XML est disponible via notre API. La documentation complète de l'API se trouve sur [cette page]([LINK_URL_1]).

Vous pouvez utiliser notre API pour récupérer les listes d'adresses IPv4 ou IPv6 de tous les checkpoints d'Uptrends, y compris les adresses à venir des checkpoints nouvellement créés ou modifiés. Les réponses sont disponibles sous format JSON ou XML, selon votre en-tête [INLINE_CODE_1].

Vous pouvez aussi télécharger des listes simples contenant les adresses [IPv4]([LINK_URL_2]) et [IPv6]([LINK_URL_3]) de nos checkpoints.

Toutes les méthodes et tous les liens présentés dans cette page génèrent une liste d'adresses IP de checkpoints, qui inclut les **adresses à venir** (comme annoncé dans notre newsletter mensuelle sur les checkpoints).

#### Pour obtenir une liste des adresses IPv4 :
Envoyez une requête GET à [INLINE_CODE_2] avec l'en-tête [INLINE_CODE_3]. Aucune authentification n'est nécessaire.

Si vous utilisez *curl*, voici un exemple de requête :
[CODE_BLOCK_1]

Pour obtenir une réponse au format XML, remplacez *application/json* par *application/xml*.

#### Pour obtenir une liste des adresses IPv6 :
La procédure est la même que pour les adresses IPv4, sauf que la requête devra être envoyée à [INLINE_CODE_4].


[SHORTCODE_1]
**Remarque :** À la place de *curl*, vous pouvez utiliser un powershell Invoke-Webrequest.
[SHORTCODE_2]
