{
  "hero": {
    "title": "DOM fantôme"
  },
  "title": "Utiliser un DOM fantôme",
  "summary": "Apprenez à configurer vos moniteurs de transactions pour surveiller les interactions dans un DOM fantôme.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/dom-fantome",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans cet article, nous allons passer en revue les étapes à suivre pour configurer un moniteur de transaction afin de surveiller un DOM fantôme sur votre page.

## Modèle objet de document (DOM)

Le **modèle objet de document (DOM)** représente chacun des éléments d'un document markup (par exemple, un document HTML pour les pages web). Quand vous chargez une page web, votre navigateur construit un DOM basé sur le document HTML, où chaque élément trouve sa place dans une arborescence. Vous pouvez afficher le DOM d'une page depuis l'onglet Éléments dans les *outils de développement* de votre navigateur (généralement accessibles au moyen de la touche F12).

Le DOM constitue une représentation instantanée du document (tout changement apporté au DOM est répercuté sur la page web affichée dans la fenêtre du navigateur). Ainsi, des modifications temporaires peuvent être apportées à la page alors même qu'elle est affichée dans le navigateur, par exemple en utilisant JavaScript.

## DOM fantôme

Des technologies comme JavaScript et CSS s'appliquent à chaque nœud dans le DOM. Toutefois, cela peut parfois causer des problèmes. Par exemple, si votre page contient des composants web (des éléments réutilisables, comme des tableaux ou des modules de paiement présents sur différentes pages), cela peut créer des conflits au niveau du balisage ou du style du reste de la page. Pour éviter cela, il est recommandé d'encapsuler ces composants web. En leur permettant d'exister séparément du document principal, vous prévenez les conflits et vous simplifiez le code.

Parmi les méthodes d'encapsulation se trouve le **DOM fantôme**. Un DOM fantôme est un arbre DOM séparé et caché qui peut être associé à des éléments spécifiques dans l'arbre DOM principal. Le DOM fantôme est structuré de la même façon qu'un DOM standard, mais associé à un **hôte fantôme**, qui est un nœud dans le DOM principal. Comme un DOM fantôme est un « arbre dans l'arbre », aucune partie de son code ne s'applique aux nœuds du DOM principal, et vice-versa.

## Configurer un DOM fantôme pour les transactions

Les interactions dans un script de transaction s'appuient sur les nœuds dans le DOM de la page. Comme le DOM fantôme est séparé, le moniteur de transaction doit être configuré de façon à explorer le DOM fantôme au lieu du DOM principal. Prenons un exemple, et imaginons que le DOM de votre page web contient ce qui suit :

[CODE_BLOCK_1]

Cette section du DOM contient un DOM fantôme, indiqué par le nœud **#shadow-root (open)**. Le DOM fantôme contient trois éléments : un lien (avec la classe 'linkClass'), une chaîne de texte (l'élément [INLINE_CODE_1] contenant "Texte d'exemple") et un élément [INLINE_CODE_2] correspondant à un champ de saisie de texte (avec l'ID 'exampleTextfield').

Comme souvent avec le DOM fantôme, celui-ci est attaché à un élément dans le DOM principal. Dans le cas présent, cet élément (que l'on appelle **hôte fantôme**) est [INLINE_CODE_3] et possède ses propres ID et classe.

Si la transaction doit inclure une étape de saisie d'une valeur dans le champ textuel, nous devons lui ordonner clairement qu'elle doit inclure le contenu du DOM fantôme. La marche à suivre est la suivante :

1. Ajouter [une action]([LINK_URL_1]) du bon type. Dans cet exemple, nous allons saisir du texte. Nous utiliserons donc l'action **Définir**. Les étapes seront les mêmes pour tous les types d'interactions.
2. Dans le paramétrage de l'action, cliquez sur le bouton [SHORTCODE_1] Spécifiez un hôte DOM fantôme [SHORTCODE_2].
3. Saisissez l'identifiant pour l'élément de l'hôte fantôme. Ici, nous pouvons désigner l'élément de la racine fantôme par son ID *exampleId*. Au moment de préciser un hôte fantôme, vous pouvez utiliser un sélecteur CSS ([INLINE_CODE_4]) ou XPath ([INLINE_CODE_5]).
4. Maintenant que nous avons précisé que la transaction devait porter sur ce DOM fantôme, nous pouvons reprendre la procédure habituelle et préciser l'élément sur lequel l'action Définir doit porter. Ici, nous utiliserons l'ID du champ textuel *exampleTextfield*. Pour préciser les éléments dans le DOM fantôme, vous pouvez **seulement utiliser les sélecteurs CSS**.
5. Pour terminer, saisissez le texte qui doit se trouver dans le champ textuel, et configurez d'autres options si nécessaire.

![Exemple de DOM fantôme]([LINK_URL_2])

Si vous utilisez l'[éditeur de script de transaction]([LINK_URL_3]) (en cliquant sur *Basculer vers le script* en haut à droite de l'éditeur), la même action aura l'apparence suivante :

[CODE_BLOCK_2]

### DOM fantômes imbriqués

Dans certains cas, un DOM fantôme peut être imbriqué dans un autre DOM fantôme. Vous pouvez alors configurer votre transaction en ajoutant un autre hôte DOM fantôme imbriqué, puis en saisissant les sélecteurs des DOM fantômes dans leur ordre d'apparition.

![DOM fantôme imbriqué]([LINK_URL_4])

Dans l'éditeur de script de transaction, ajoutez simplement des valeurs au tableau shadowRoots :

[CODE_BLOCK_3]
