{
  "hero": {
    "title": "Conditions d'erreur liées au contenu de la page"
  },
  "title": "Conditions d'erreur liées au contenu de la page",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/conditions-erreur/correspondance-de-contenu",
  "summary": "La correspondance de contenu permet de vérifier que la page que vous surveillez affiche le bon contenu",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Il arrive parfois que seule la moitié du contenu d'un site web se charge correctement. Le non-chargement de certains blocs de texte, paragraphes et sections complique la navigation pour les utilisateurs. Si vous gérez un site d'e-commerce, cette mauvaise expérience utilisateur peut affecter les performances de votre site et diminuer vos ventes sans que vous vous en rendiez compte.

## Condition d'erreur liée au contenu de la page

La condition d'erreur Contenu de page vous permet de vous assurer que le contenu de votre site web se charge correctement et complètement. Elle vous permet de préciser les blocs de textes, les phrases et les expressions régulières qui doivent apparaître sur votre page, et de vérifier que ces éléments s'affichent.

![Condition d'erreur Contenu de page]([LINK_URL_1])

## Correspondance de contenu

Une correspondance de contenu est une liste de mots que vous fournissez pour que le moniteur vérifie qu'elle figure bien dans le contenu chargé sur le site :

- Si un moniteur vérifiant la page *trouve* le contenu, *aucune erreur* n'est signalée.
- Si un moniteur vérifiant la page *ne trouve pas* le contenu, *une erreur* est signalée.

## Correspondance de contenu spécifique à chaque type de moniteur

Différents types de correspondance de contenu sont disponibles pour les différents moniteurs. La correspondance de contenu varie selon la catégorie du moniteur et les données collectées :

### Moniteurs de disponibilité

Les moniteurs de disponibilité vérifient le contenu de la page en adressant une requête GET à l'URL de votre site web. Si la requête réussit, le moniteur valide le contenu de la réponse GET de votre site web.

Si vous surveillez une URL de site web, comme [URL_1] les vérifications de contenu suivantes peuvent être effectuées :

| Types de correspondance de contenu | Exemples |
|--|--|
| Modèle objet de document (DOM) ou éléments HTML | [SHORTCODE_1]
- [INLINE_CODE_1]
- [INLINE_CODE_2]
- [INLINE_CODE_3]
   [SHORTCODE_2] |
   | [SHORTCODE_3] Textes contenant une [expression régulière]([LINK_URL_2]) [SHORTCODE_4] | [SHORTCODE_5]
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
   [SHORTCODE_6] |
   | [SHORTCODE_7] [Correspondance de contenu avancée]([LINK_URL_3])[SHORTCODE_8] | [SHORTCODE_9]
- [INLINE_CODE_4][SHORTCODE_10] |

### Moniteurs de navigateur

Les moniteurs de navigateur vérifient le contenu de la page en contrôlant son code source. Le code source est la structure brute du site web au format HTML. Il comprend les métadonnées, les scripts et les styles de la page.

Si vous surveillez une URL de site web, comme [URL_2] les vérifications de contenu suivantes peuvent être effectuées :

| Types de correspondance de contenu | Exemples |
|--|--|
| Modèle objet de document (DOM) ou éléments HTML | [SHORTCODE_11]
- [INLINE_CODE_5]
- [INLINE_CODE_6]
- [INLINE_CODE_7]
   [SHORTCODE_12] |
   | [SHORTCODE_13] Textes contenant une [expression régulière]([LINK_URL_4]) [SHORTCODE_14] | [SHORTCODE_15]
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
   [SHORTCODE_16] |
   | [SHORTCODE_17] [Correspondance de contenu avancée]([LINK_URL_5])[SHORTCODE_18] | [SHORTCODE_19]
- [INLINE_CODE_8][SHORTCODE_20] |

[SHORTCODE_21] **Remarque :** Pour ouvrir le code source d'une page, ouvrez votre site web et pressez les touches **Ctrl + U**. Vous pouvez aussi cliquer n'importe où sur la page et sélectionner **Code source de la page**. Notez que tous les éléments du code source ne peuvent pas faire l'objet d'une vérification de contenu.[SHORTCODE_22]

### Moniteurs d'API multi-étapes (MSA)

Les moniteurs MSA vérifient les correspondances de contenu au moyen d'**assertions**. Les assertions vous permettent d'indiquer comment vérifier que la réponse de l'API répond aux conditions attendues. Par exemple, vous pouvez indiquer que la réponse doit contenir le code de statut 200 ou que le corps de réponse au format JSON doit contenir des textes spécifiques. Pour en savoir plus, lisez notre article sur les [assertions pour la surveillance multi-étapes]([LINK_URL_6]).

### Moniteurs de transactions

Les moniteurs de transactions vérifient le contenu de la page en contrôlant que ses éléments s'affichent dans le navigateur. Ils vérifient que des textes, des boutons, des images ou d'autres éléments de l'interface utilisateur sont visibles sur votre site web. Les moniteurs de transactions reposent sur des **vérifications de contenu**. Ces actions configurées à chaque étape vérifient que chaque chargement de page se déroule comme attendu. Par exemple, une vérification peut vérifier que le texte "L'article a été ajouté au panier" s'affiche sur la page. Pour en savoir plus, lisez notre article sur les [vérifications de contenu]([LINK_URL_7]).

## Types de correspondance de contenu

Voici les types de correspondance de contenu disponibles pour certains moniteurs :

### Correspondance de contenu régulière {id = "regular-content-match"}

Vous pouvez définir une correspondance de contenu au moyen d'expressions régulières. Une expression régulière (regex ou regexp) est une chaîne de caractères spéciale utilisée pour décrire un motif de recherche. Pour définir une correspondance de contenu, vous pouvez utiliser les éléments suivants :

- Un mot unique : [INLINE_CODE_9]
- Plusieurs mots ou phrases dans un ordre précis : [INLINE_CODE_10] (dans cet exemple, product ET order doivent apparaître)
- Des symboles correspondant à d'autres éléments :
   - [INLINE_CODE_11] : utilisez un point d'exclamation pour inverser le sens d'un mot. Cette correspondance de contenu signifie que le mot *erreur* ne doit pas apparaître.
   - [INLINE_CODE_12] : la barre verticale indique qu'un mot équivaut à un autre. Cette correspondance de contenu signifie que le texte [INLINE_CODE_13] OU [INLINE_CODE_14] doit apparaître sur votre site web.

Pour en savoir plus, consultez cette ressource (en anglais) sur les expressions régulières : [Regular Expression Language - Quick Reference]([LINK_URL_8]).


### Correspondance de contenu avancée

Vous pouvez utiliser simultanément plusieurs correspondances de contenu en enregistrant les valeurs au format JSON. Pour combiner deux motifs de recherche, sur n'importe quel élément de page ou expression régulière, utilisez le code suivant :

[CODE_BLOCK_1]

Fournissez une correspondance de contenu valide dans le champ [INLINE_CODE_15]. Définissez [INLINE_CODE_16] sur [INLINE_CODE_17] si le motif doit correspondre au contenu de votre site web, ou sur [INLINE_CODE_18] s'il ne doit pas correspondre à un contenu sur le site.

[SHORTCODE_23] **Remarque :** La correspondance de contenu avancée est disponible avec les moniteurs HTTPS, Webservices HTTP et HTTPS, et Full Page Check. [SHORTCODE_24]

Pour vérifier l'horodatage d'un élément de votre site web au moyen d'une correspondance de contenu, utilisez :

[CODE_BLOCK_2]

La valeur JSON, [INLINE_CODE_19], peut contenir des valeurs sous la forme d'une expression régulière, comme \[HTML_TAG_1], \[HTML_TAG_2], \[HTML_TAG_3], \[HTML_TAG_4], \[HTML_TAG_5] et \[HTML_TAG_6]. Toutes ces valeurs peuvent être extraites du contenu du site web et seront fusionnées avec l'heure actuelle du serveur, puis évaluées en horaires UTC.

La valeur [INLINE_CODE_20] est le nombre de minutes à soustraire afin de le comparer à l'heure du serveur en UTC. Si la page web contient un horodatage en UTC\+1, le décalage doit être de 60. Si la page web contient un horodatage en EST (UTC-5), le décalage devrait être de -300.

La valeur [INLINE_CODE_21] est la différence maximale en minutes autorisée entre l'heure de la page web et votre heure locale. Par exemple : s'il est 10h06 et que l'heure de la page web est 10h00, une erreur se produira si la valeur [INLINE_CODE_22] est égale ou inférieure à 5.

## Comment configurer une correspondance de contenu

Pour configurer une correspondance de contenu, vous devez ajouter une condition d'erreur de type **Vérifier le contenu de la page** :

1. Ouvrez le menu [SHORTCODE_25] Surveillance > Configuration du moniteur [SHORTCODE_26].
2. Sélectionnez le moniteur auquel vous souhaitez ajouter une correspondance de contenu.
3. Affichez l'onglet [SHORTCODE_27]Conditions d'erreur[SHORTCODE_28].
4. Saisissez les informations relatives à la correspondance de contenu dans la section **Vérifier le contenu de la page**.
5. Cliquez sur [SHORTCODE_29] Enregistrer [SHORTCODE_30] pour confirmer les changements.

Une fois cela effectué, vous pouvez [créer une définition d'alerte ]([LINK_URL_9]) pour recevoir une notification lorsque la condition d'erreur **Vérifier le contenu de la page** est remplie.
