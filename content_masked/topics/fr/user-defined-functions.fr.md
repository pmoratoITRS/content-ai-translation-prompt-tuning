{
  "hero": {
    "title": "Fonctions définies par l'utilisateur"
  },
  "title": "Fonctions définies par l'utilisateur",
  "summary": "Cet article présente les fonctions définies par l'utilisateur et leur utilisation",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/fonctions-definies-utilisateur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

La [surveillance d'API multi-étapes]([LINK_URL_1]) d'Uptrends vous permet d'exécuter plusieurs requêtes HTTP séquentielles sur votre API. De cette façon, les données entrantes sont analysées, enregistrées dans des variables ou vérifiées afin de contrôler la présence de contenu spécifique. Dans certains cas, cependant, les données entrantes doivent être transformées ou converties pour en extraire plus facilement un sens. Il s'agit par exemple des fonctions d'encodage et de décodage XML et JSON décrites dans notre article sur le [format des messages pour les intégrations personnalisées]([LINK_URL_2]). En plus de ces fonctions prédéfinies, Uptrends vous permet aussi de définir vous-même des fonctions. On parle alors de **fonctions définies par l’utilisateur**. Ces fonctions peuvent être utilisées pour convertir des [valeurs de variables]([LINK_URL_3]) (acquises lors d'une étape précédente, ou à partir d'une [variable système fournie par Uptrends]([LINK_URL_4])) vers une nouvelle valeur.

## Types de fonctions définies par l’utilisateur

Nous proposons ces types de fonctions définies par l’utilisateur :

- **Expression régulière** : ce type de fonction vous permet d'appliquer une expression régulière (RegEx) à vos variables précédemment créées. Cette fonction sert à extraire des sections spécifiques des données de réponse (comme un code d'authentification à partir d'un en-tête de redirection *Location*).
- **Conversion** : ce type de fonction vous permet de remplacer automatiquement certaines valeurs de la réponse par d'autres valeurs spécifiques. Par exemple, si un endpoint utilise les termes *erreur* ou *ok* (comme c'est le cas pour l'[API d'Uptrends]([LINK_URL_5]) tandis que le suivant avec lequel vous interagissez utilise plutôt les termes *incident* ou *sain*, vous pouvez utiliser une fonction de conversion pour adapter automatiquement ces valeurs aux équivalents corrects.
- **Hachage** : le hachage est un processus unilatéral par lequel un algorithme transforme un message de n'importe quelle longueur en une valeur d'une longueur fixe. Une même entrée doit toujours donner lieu au même résultat. Les fonctions de hachage sont donc très utiles pour comparer en toute sécurité des données sensibles comme les mots de passe, les jetons d'accès ou les signatures numériques, sans devoir se les échanger à proprement parler. Pour en savoir plus sur les fonctions de hachage et les moniteurs d'API Multi-step, vous pouvez lire notre article intitulé [Hachage et encodage]([LINK_URL_6]).

## Créer des fonctions définies par l’utilisateur

Vous pouvez créer une fonction définie par l'utilisateur dans l'onglet [SHORTCODE_3]Étapes[SHORTCODE_4] de vos moniteurs d'API multi-étapes ou dans l'onglet [SHORTCODE_5]Personnalisations[SHORTCODE_6] de vos intégrations (personnalisées).

[SHORTCODE_1]
**Remarque :** Une fonction définie par l'utilisateur est propre au moniteur d'API multi-étapes ou à l'intégration personnalisée pour lequel vous l'avez créée, et ne peut s'appliquer à d'autres moniteurs ou intégrations.
[SHORTCODE_2]

1. Dans l'onglet [SHORTCODE_7]Étapes[SHORTCODE_8] de l'un de vos moniteurs d'API multi-étapes ou dans l'onglet [SHORTCODE_9]Personnalisations[SHORTCODE_10] de vos intégrations (personnalisées), vous trouverez la section **Fonctions définies par l'utilisateur** près du bas de la page.

2. Cliquez sur le bouton [SHORTCODE_11]Ajouter une fonction[SHORTCODE_12] pour commencer à définir une nouvelle fonction.

3. Sélectionnez le type de fonction souhaitée : **Conversion**, **Expression régulière** ou **Hachage**, et donnez à la fonction un nom approprié. Nous vous recommandons d'utiliser un nom simple et sans espaces, car vous devrez vous y référer plus tard.

4. Remplissez les autres informations demandées :
- Dans le cas d'une fonction de conversion, ajoutez les correspondances individuelles dont vous avez besoin. La fonction de conversion traduira les valeurs "De" en valeurs "À" correspondantes.
- Pour une fonction de type expression régulière, spécifiez l'expression régulière dont vous avez besoin. La regex est comparée au texte entrant et peut être utilisée pour en extraire une partie spécifique.
- Pour une fonction de hachage utilisant un algorithme HMAC, indiquez la valeur de la clé secrète.

Vous pouvez ajouter des fonctions supplémentaires en répétant ces étapes, si nécessaire.

![Exemple de fonctions définies par l'utilisateur]([LINK_URL_7])

## Utiliser vos fonctions [ANCHOR_1]

Pour utiliser votre ou vos nouvelles **fonctions définies par l'utilisateur**, il faudra envelopper de cette façon la ou les variables sur lesquelles la fonction doit agir : [INLINE_CODE_1]. À titre d'exemple, examinons une fonction de conversion dont le but est de remplacer, dans les données de réponse entrantes, le texte 'Erreur' par 'Incident', 'Avertissement' par 'Anormal' et 'Ok' par 'Sain', de sorte que l'endpoint à l'étape suivante reçoive les termes qu'il comprend. Par exemple :

- Dans l'image ci-dessus, une fonction définie par l'utilisateur a été créée sous le nom [INLINE_CODE_2].
- L'endpoint renvoie une réponse JSON contenant un champ 'Status', qui a une valeur 'Erreur', 'Avertissement' ou 'Ok'.
- À l'étape suivante, nous voulons transmettre ces données d'état à une autre API. Cette nouvelle API ne comprend cependant pas les termes utilisés et requiert plutôt les valeurs 'Incident', 'Anormal' ou 'Sain'.

Pour utiliser la fonction [INLINE_CODE_3] de façon à remplacer automatiquement les valeurs d'état par les termes corrects, il faudra :

1. Extraire la valeur du champ 'Status' à partir des données de réponse, comme vous le feriez normalement (voir notre [article sur les variables de surveillance multi-étapes]([LINK_URL_8]). Dans cet exemple, la nouvelle variable est nommée statusRaw. Comme décrit ci-dessus, cette variable contiendra 'Erreur', 'Avertissement' ou 'Ok'.
2. Pour appliquer la fonction définie par l'utilisateur, cliquer d'abord sur le bouton [SHORTCODE_13]Ajouter une variable[SHORTCODE_14].
3. Définir la source de la variable (dans la liste déroulante à gauche) pour activer l'option [SHORTCODE_15]Exécuter la fonction[SHORTCODE_16].
4. Pour l'**expression de la fonction**, encapsuler la référence de la variable dans la fonction comme décrit ci-dessus : [SHORTCODE_17]{{errorMapping({{statusRaw}})}}[SHORTCODE_18]
5. La valeur résultante sera 'Incident', 'Anormal' ou 'Sain', en fonction de la valeur de statutRaw. Dans le champ **Nom de variable**, spécifiez un nom pour la valeur de sortie.

![Utilisation d'une fonction définie par l'utilisateur]([LINK_URL_9])

Nous avons maintenant créé une nouvelle variable, *status*, dont la valeur est 'Incident', 'Anormal' ou 'Sain'. Dans les étapes suivantes, nous pouvons faire référence à cette variable de la façon habituelle (par exemple en utilisant la notation [INLINE_CODE_4]. Dans cet exemple, nous avons utilisé une fonction de **conversion**, mais pour une fonction **RegEx** les étapes sont identiques.
