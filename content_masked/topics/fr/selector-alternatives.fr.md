{
  "hero": {
    "title": "Sélecteurs alternatifs"
  },
  "title": "Trouver des sélecteurs alternatifs",
  "summary": "Il arrive parfois que les sélecteurs ne fonctionnent pas, ou pas tout le temps. Dans cet article, nous vous présentons certains des problèmes couramment rencontrés avec les sélecteurs et comment y remédier.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/selecteurs-alternatifs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lorsque vous devez identifier un élément de page spécifique dans votre script de transaction, vous utilisez un sélecteur XPath ou CSS. Il existe souvent plusieurs choix de sélecteurs possibles pour spécifier un élément type, mais certains sélecteurs peuvent occasionner des problèmes. Trouver le bon sélecteur nécessite donc parfois une utilisation astucieuse des sélecteurs XPath ou CSS.

Lorsque vous utilisez l'enregistreur de transaction pour capturer un parcours de clics, [l'enregistreur applique des algorithmes]([LINK_URL_1]) pour choisir ce qui lui semble être le meilleur choix de sélecteur. Cependant, comme l'enregistreur de transaction n'obtient qu'un aperçu de la structure de votre page, le sélecteur qu'il choisit peut ne pas être le meilleur choix pour vous. Dans cet article, nous abordons quelques cas de figure et les solutions à envisager pour changer de sélecteur.

## Causes courantes d'une incompatibilité de sélecteur

De nombreux facteurs peuvent faire que votre sélecteur ne fonctionne pas comme vous l'attendez. Par exemple, vos tests peuvent donner lieu à des erreurs telles que "Element not found". Un mauvais choix de sélecteur peut en être la cause. Examinons quelques-unes des raisons qui peuvent expliquer les erreurs de script.

### ID dynamiques

Certains éléments obtiennent un nouvel ID chaque fois que le serveur envoie la page. Si votre sélecteur fait référence à l'ancien ID, votre script ne trouvera pas l'élément. Il existe différentes manières de résoudre ce problème.

Dans les exemples suivants, nous utiliserons un élément de saisie pour sélectionner la quantité d'articles dans le snippet HTML.

    [HTML_TAG_1] 
      [HTML_TAG_2] 
    [HTML_TAG_3]

L'identifiant de la saisie est en partie fixe et en partie généré, ce qui entraîne des erreurs lors de la référence à l'identifiant par l'enregistreur de transaction. L'enregistreur de transaction propose :  
XPath : [INLINE_CODE_1] Sélecteur CSS : [INLINE_CODE_2]  
Les deux ID échouent lorsqu'ils sont utilisés dans la transaction. Vous avez plusieurs options pour résoudre ce problème.

- **Utiliser un attribut d'élément qui ne change pas**. En utilisant un attribut d'élément différent tel qu'un nom d'élément, vous aurez un sélecteur stable.  
   [INLINE_CODE_3]
- **Utiliser un chemin relatif pour naviguer dans le DOM**. Le nœud HTML ci-dessus est imbriqué dans un nœud parent [INLINE_CODE_4]. On peut faire référence à l'élément à l'intérieur du parent en utilisant XPath. Le code ci-dessous localise le parent suivi de l'élément enfant.  
   //div\[@class="quantity"\]/input
- **Utiliser un XPath relatif avec** [INLINE_CODE_5] ou [INLINE_CODE_6]. Si l'ID est en partie fixe et en partie dynamique, comme [INLINE_CODE_7], où la partie numérique "[INLINE_CODE_8]" change mais la partie "[INLINE_CODE_9]" est fixe, vous pouvez faire référence à la partie qui ne change pas. Par exemple,  
   [INLINE_CODE_10]  
   ou  
   [INLINE_CODE_11]
- **Ajouter des attributs d'élément pour vos tests de transaction**. Demandez à vos développeurs de vous aider en ajoutant des attributs d'éléments spéciaux qui ne changent pas pour les tests. Par exemple, disons que vous avez un élément avec un ID dynamique tel que  
   [INLINE_CODE_12]  
   Dans ce cas vous n'avez rien, comme un nom d'attribut, pour identifier l'élément. Si vous ajoutez un autre attribut avec une valeur statique tel que "data-test-id", vous pourrez toujours trouver l'élément. Un attribut ajouté peut prendre cette forme  
   [INLINE_CODE_13]
- **Identifier les éléments en utilisant plusieurs attributs d'élément**. Si vos options d'identification [INLINE_CODE_14] ou [INLINE_CODE_15] ne fonctionnent pas car d'autres éléments de la page utilisent le même préfixe ou suffixe avec la partie dynamique, vous pouvez parfois utiliser une combinaison d'attributs pour identifier l'élément à l'aide de XPath.  
   [INLINE_CODE_16]`[INLINE_CODE_17][SYSTEM_VAR_1]`.

### Demander de l'aide au support

Même si vous avez choisi l'option de transactions en libre-service, vous n'êtes pas livré à vous-même. Notre équipe de support est là pour vous. Nos spécialistes des transactions ont déjà tout vu ou presque, et sauront vous aider à modifier vos sélecteurs. Il vous suffit de créer un [ticket de support]([LINK_URL_8]) et de leur expliquer vos difficultés.
