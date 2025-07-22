{
"hero": {
"title": "Sélecteurs alternatifs"
},
"title": "Trouver des sélecteurs alternatifs",
"summary": "Il arrive parfois que les sélecteurs ne fonctionnent pas, ou pas tout le temps. Dans cet article, nous vous présentons certains des problèmes couramment rencontrés avec les sélecteurs et comment y remédier.",
"url": "/support/kb/surveillance-synthetique/transactions/selecteurs-alternatifs",
"translationKey": "https://www.uptrends.com/support/kb/transactions/selector-alternatives"
}

Lorsque vous devez identifier un élément de page spécifique dans votre script de transaction, vous utilisez un sélecteur XPath ou CSS. Il existe souvent plusieurs choix de sélecteurs possibles pour spécifier un élément type, mais certains sélecteurs peuvent occasionner des problèmes. Trouver le bon sélecteur nécessite donc parfois une utilisation astucieuse des sélecteurs XPath ou CSS.

Lorsque vous utilisez l'enregistreur de transaction pour capturer un parcours de clics, [l'enregistreur applique des algorithmes]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="fr" >}}) pour choisir ce qui lui semble être le meilleur choix de sélecteur. Cependant, comme l'enregistreur de transaction n'obtient qu'un aperçu de la structure de votre page, le sélecteur qu'il choisit peut ne pas être le meilleur choix pour vous. Dans cet article, nous abordons quelques cas de figure et les solutions à envisager pour changer de sélecteur.

## Causes courantes d'une incompatibilité de sélecteur

De nombreux facteurs peuvent faire que votre sélecteur ne fonctionne pas comme vous l'attendez. Par exemple, vos tests peuvent donner lieu à des erreurs telles que "Element not found". Un mauvais choix de sélecteur peut en être la cause. Examinons quelques-unes des raisons qui peuvent expliquer les erreurs de script.

### ID dynamiques

Certains éléments obtiennent un nouvel ID chaque fois que le serveur envoie la page. Si votre sélecteur fait référence à l'ancien ID, votre script ne trouvera pas l'élément. Il existe différentes manières de résoudre ce problème.

Dans les exemples suivants, nous utiliserons un élément de saisie pour sélectionner la quantité d'articles dans le snippet HTML.

    <div class="quantity"> 
      <input type="number" id="quantity_5e5653081acc7" class="input-text qty text"
      step="1" min="1" max="" name="quantity" value="1" title="Qty" size="4" 
      pattern="[0-9]*"inputmode="numeric"
      aria-labelledby="Suraya Bay T-Shirt quantity"> 
    </div>

L'identifiant de la saisie est en partie fixe et en partie généré, ce qui entraîne des erreurs lors de la référence à l'identifiant par l'enregistreur de transaction. L'enregistreur de transaction propose :  
XPath : `//input[@id="quantity_5e5653081acc7"])[1] ` Sélecteur CSS : `input#quantity_5e5653081acc7`  
Les deux ID échouent lorsqu'ils sont utilisés dans la transaction. Vous avez plusieurs options pour résoudre ce problème.

- **Utiliser un attribut d'élément qui ne change pas**. En utilisant un attribut d'élément différent tel qu'un nom d'élément, vous aurez un sélecteur stable.  
   `//input[@name="quantity"]`
- **Utiliser un chemin relatif pour naviguer dans le DOM**. Le nœud HTML ci-dessus est imbriqué dans un nœud parent `<div>`. On peut faire référence à l'élément à l'intérieur du parent en utilisant XPath. Le code ci-dessous localise le parent suivi de l'élément enfant.  
   //div\[@class="quantity"\]/input
- **Utiliser un XPath relatif avec** `contains` ou `starts with`. Si l'ID est en partie fixe et en partie dynamique, comme `id="quantity_5e5653081acc7"`, où la partie numérique "`5e5653081acc7`" change mais la partie "`quantity_`" est fixe, vous pouvez faire référence à la partie qui ne change pas. Par exemple,  
   `//select[starts with (@id, "quantity_")]`  
   ou  
   `//select[contains(@id, "quantity")]`
- **Ajouter des attributs d'élément pour vos tests de transaction**. Demandez à vos développeurs de vous aider en ajoutant des attributs d'éléments spéciaux qui ne changent pas pour les tests. Par exemple, disons que vous avez un élément avec un ID dynamique tel que  
   `<button id=”i2fe4owf” class=”btn”>`  
   Dans ce cas vous n'avez rien, comme un nom d'attribut, pour identifier l'élément. Si vous ajoutez un autre attribut avec une valeur statique tel que "data-test-id", vous pourrez toujours trouver l'élément. Un attribut ajouté peut prendre cette forme  
   `<button id=”i2fe4owf” class=”btn” data-test-id =”shoppingcart-test-step2”>`
- **Identifier les éléments en utilisant plusieurs attributs d'élément**. Si vos options d'identification `contains` ou `starts with` ne fonctionnent pas car d'autres éléments de la page utilisent le même préfixe ou suffixe avec la partie dynamique, vous pouvez parfois utiliser une combinaison d'attributs pour identifier l'élément à l'aide de XPath.  
   `//select[starts-with(@id, "quantity_" and contains(@class, "qty text")]```

### Sites multilingues

Lorsque vous avez un site web multilingue, la page change de langue en fonction de l'emplacement de l'utilisateur. Si le checkpoint que vous avez sélectionné se trouve dans une région qui déclenche un changement de langue, votre moniteur de transaction peut échouer selon la façon dont vous avez identifié l'élément. Pour vos sélecteurs, il est préférable d'utiliser d'autres options que les valeurs des étiquettes ou des mots spécifiques trouvés sur la page si la langue affecte votre contenu.

### Contenu dynamique

Certains sites utilisent un contenu dynamique basé sur les promotions saisonnières, les vacances, la connexion de l'utilisateur, les cookies, les données de localisation ou encore d'autres facteurs. Les changements dans les données produits par les variations du contenu dynamique peuvent provoquer l'échec des moniteurs de transactions. Le contenu dynamique génère les mêmes problèmes que les identifiants dynamiques, mais ce sont les éléments de la page entière qui changent à chaque requête du serveur (pensez aux pages d'Amazon avec les recommandations de produits qui changent constamment). Bien que les détails changent, la structure reste fixe. Vous obtiendrez de meilleurs résultats en référençant les éléments par leur emplacement dans le DOM plutôt que par leurs attributs.

Prenons l'exemple d'un site d'e-commerce qui affiche des articles sur la page en fonction de leur popularité. Les articles apparaissent et disparaissent à tour de rôle presque à chaque chargement de la page. Plutôt que d'utiliser un sélecteur qui identifie un article par son nom ou par un autre attribut spécifique, il est probablement préférable d'utiliser un sélecteur de chemin relatif qui choisit le premier article d'une liste, quel que soit l'article affiché.

### Éléments cachés

Les erreurs dues à des éléments cachés ne sont pas nécessairement le résultat d'un mauvais sélecteur. Votre sélecteur peut aussi échouer parce qu'une action fait défaut. Dès lors, si vous obtenez des erreurs indiquant que le script a trouvé l'élément, mais que celui-ci n'est pas visible, votre script peut nécessiter une action supplémentaire avant de tenter l'interaction.  Tout comme vos utilisateurs, le script ne peut pas interagir avec des éléments invisibles.

**Action de survol manquante** :

Une action de survol manquante provoque des erreurs. Un élément de menu peut ne pas devenir visible tant que l'utilisateur n'a pas placé le curseur au-dessus pour afficher le menu déroulant. L'ajout de l'action de survol rend l'élément visible et disponible pour l'interaction.

**Action de défilement manquante** :

Souvent, les pages ne chargent les éléments que lorsque l'utilisateur en a besoin, afin de donner l'impression d'une meilleure performance et de réduire la transmission des données. Lorsque l'utilisateur fait défiler la page, le contenu se charge au fur et à mesure. Sans l'action de défilement, les éléments ne sont pas restitués et mis à disposition pour l'interaction du script. L'ajout d'une action de défilement résout le problème. L'action de défilement ne rend pas visibles tous les éléments. Vous aurez peut-être à ajouter plusieurs actions de défilement avant que l'élément cible ne soit visible sur la page.

{{< callout >}}
**Remarque** : L'enregistreur ne capture pas les actions de défilement et [de survol]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="fr" >}}), vous devez donc les ajouter dans votre script manuellement.
{{< /callout >}}

**Caché dans le DOM mais visible à l'écran** :

Vous pouvez également obtenir des erreurs dues à des éléments que vous pouvez clairement voir sur la page, mais qui sont cachés dans le DOM. Les causes courantes de ce problème sont les boutons radio ou les cases à cocher. L'enregistreur capture l'action du clic sur le bouton radio ou la case à cocher, mais ces éléments ne sont pas visibles dans le DOM ; leurs étiquettes le sont. Pour résoudre le problème, déplacez l'action du clic sur l'étiquette couvrant l'élément.

## Changement de sélecteur

Si vous avez rencontré des problèmes avec vos sélecteurs, vous pouvez prendre plusieurs mesures pour résoudre le problème.

### Utiliser un autre sélecteur

Lors de la conversion de votre enregistrement en script, Uptrends décide du sélecteur à utiliser sur la base d'un algorithme. Si l'enregistreur a fait un mauvais choix, vous devez intervenir. Uptrends vous facilite la tâche en mettant à votre disposition tous les sélecteurs possibles. Pour accéder aux autres sélecteurs,

1. Cliquez sur le carré gris (avec trois points) pour ouvrir la boîte de dialogue du sélecteur.
   ![Bouton de sélection du sélecteur](/img/content/ed5d9588-d944-402f-9899-5ba46a574c2b.png)

2. Choisissez un autre sélecteur dans la liste.
   ![Fenêtre de sélection du sélecteur](/img/content/c8a2a635-1e85-4c3b-b84b-2b1edbe4dd15.png)

Vous pouvez choisir et tester n'importe lequel des sélecteurs de la liste. Si aucun d'entre eux ne fonctionne bien pour vous et que vous n'êtes pas à l'aise pour écrire le vôtre, notre [équipe de support](/contact) se fera un plaisir de vous aider à trouver une solution.

{{< callout >}}
**Remarque** : Si vous travaillez avec un ancien script, les sélecteurs proposés sont probablement obsolètes. Vous devez alors soit écrire le nouveau sélecteur vous-même, soit demander au [support](/contact) de vous aider.
{{< /callout >}}

### Écrire le sélecteur vous-même

Si les sélecteurs ne vous font pas peur ou que vous disposez d'un personnel de développement pour vous aider, vous pouvez écrire vos propres sélecteurs CSS ou XPath. Peu importe qui écrit vos sélecteurs, il faut les tester de manière exhaustive.

Vous pouvez utiliser des [variables automatiques]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="fr" >}}) dans le sélecteur. Par exemple, vous pouvez ajouter un nombre aléatoire au chemin du sélecteur en utilisant la variable automatique `{{@RandomInt(min,max)}}`.

### Demander de l'aide au support

Même si vous avez choisi l'option de transactions en libre-service, vous n'êtes pas livré à vous-même. Notre équipe de support est là pour vous. Nos spécialistes des transactions ont déjà tout vu ou presque, et sauront vous aider à modifier vos sélecteurs. Il vous suffit de créer un [ticket de support](/contact) et de leur expliquer vos difficultés.
