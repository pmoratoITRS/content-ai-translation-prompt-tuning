{
  "hero": {
    "title": "Utilisation de variables dans les transactions"
  },
  "title": "Utilisation de variables dans les transactions",
  "summary": "Découvrez comment utiliser les variables dans les transactions.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/variables-transactions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Il est possible que vous ayez parfois besoin d'enregistrer et de réutiliser une valeur rencontrée par votre moniteur de transaction pendant l'exécution du script. Dans ce cas, vous pouvez configurer votre transaction de façon à enregistrer la valeur comme une **variable**, pour la réutiliser à une étape ultérieure du script. Par exemple, imaginons que votre transaction passe par une étape du tunnel de vente qui génère un numéro de commande. Vous pouvez configurer la transaction pour qu'elle enregistre ce numéro sous forme de variable, puis vérifie qu'il correspond au bon de commande figurant ensuite sur la page de confirmation. Cette opération vous permet de confirmer que le système de backend fonctionne correctement.

## Créer une variable

Pour créer une variable, utilisez l'action [Tester le contenu de l’élément]([LINK_URL_1]). Les variables sont créées d'après le contenu complet d'un élément de la page. Pour préciser l'élément à enregistrer, vous devez utiliser [un sélecteur CSS ou une requête XPath]([LINK_URL_2]).

1. [Ajoutez une action "Tester le contenu de l’élément"]([LINK_URL_3]) à l'endroit opportun dans le script de transaction. Le contenu de l'élément à enregistrer sous forme de variable doit être présent sur la page à cette étape de la transaction.
2. Pointez la vérification de contenu sur le bon élément de la page en utilisant [le sélecteur CSS ou la requête XPath]([LINK_URL_4]). Si vous avez besoin d'aide, vous pouvez [contacter l'équipe de support]([LINK_URL_5]).
3. La [vérification de contenu]([LINK_URL_6]) testera la présence de l'élément enregistré, et vérifiera que son contenu correspond à la valeur précisée (au moyen d'expressions régulières si besoin).
4. Dans l'option **Affecter une variable**, indiquez le nom de la variable entouré de doubles accolades : [INLINE_CODE_1]

Dans l'exemple ci-dessous, la deuxième étape d'une transaction passe une commande (en cliquant sur l'élément [INLINE_CODE_2] à l'étape 2.1) et vérifie que l'élément [INLINE_CODE_3] est présent et que son contenu correspond à l'expression régulière (à l'étape 2.2). Pour finir, la transaction enregistre la variable [INLINE_CODE_4] au moyen de l'option **Affecter une variable**. La variable contient la valeur complète de l'élément (dans le cas présent : *"Votre numéro de commande est le 1234"*).

![Création d'une variable de transaction]([LINK_URL_7])

## Ajuster une variable

Dans les situations telles que celle décrite ci-dessus, le contenu enregistré dans la variable peut contenir du texte superflu. Dans cet exemple, seul le numéro de commande serait intéressant dans la variable. Le contenu de la variable peut être ajusté au moyen d'une expression régulière, pour conserver ou retirer une partie du contenu. Pour en savoir plus, consultez l'article de notre base de connaissances concernant [l'action "Ajuster le contenu de la variable"]([LINK_URL_8]).

1. Une fois que la variable a été créée dans le script de transaction, ajoutez une action **Ajuster le contenu de la variable**.
2. Ajoutez le nom de la variable défini précédemment ([INLINE_CODE_5] dans l'exemple ci-dessus).
3. Indiquez s'il faut **conserver** ou **supprimer** le contenu qui correspond au modèle d'expression régulière.
4. Ajouter l'expression régulière

![Modification d'une variable]([LINK_URL_9])

Le résultat de l'action décrite dans l'exemple ci-dessus serait *1234*. Gardez à l'esprit que cela remplacera la variable existante.

## Utiliser les variables

Une fois définie et ajustée si nécessaire, la variable peut être utilisée à un autre endroit de la transaction. Une fois nommées, les variables peuvent être utilisées à n'importe quelle étape. Par exemple, le numéro de commande isolé dans l'exemple ci-dessus peut être réutilisé sous forme de valeur dans une action **Définir** et saisi dans la zone de recherche pour vérifier que la commande a bien été créée. Il suffit d'utiliser le nom de la variable ([INLINE_CODE_6] dans cet exemple).


![Utilisation d'une variable de transaction]([LINK_URL_10])



