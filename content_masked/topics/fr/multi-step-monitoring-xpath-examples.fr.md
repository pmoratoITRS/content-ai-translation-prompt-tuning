{
  "hero": {
    "title": "Exemples XPath de Monitoring multi-étape"
  },
  "title": "Exemples XPath de Monitoring multi-étape",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/exemples-xpath-de-monitoring-multi-étape",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cet article montre plusieurs exemples d'extraction de contenu à partir de réponses XML à l'aide de XPath. Ces requêtes XPath vous permettent d'inspecter une réponse XML provenant de votre API ou de votre service Web dans le cadre d'un [Moniteur API multi-étapes]([LINK_URL_1]). Une requête XPath définit la partie de la réponse XML qui vous intéresse, généralement une valeur contenue dans l'un des nœuds XML. Vous pouvez alors prendre cette valeur extraite et vérifier si elle [satisfait à certaines conditions]([LINK_URL_2]) (en utilisant des assertions), ou la [stocker dans une variable]([LINK_URL_3]) pour une utilisation ultérieure.

La version de XPath utilisée dans les configurations de moniteurs d'API multi-étapes est XPath 1.0, ce qui signifie que les fonctions introduites dans les versions XPath supérieures ne sont pas prises en compte.

## Exemple 1 : XML simple

Prenons une API ou un service Web pouvant renvoyer des informations sur un inventaire de produit. Lorsque nous envoyons une requête à cette API, elle renvoie des données sur un ou plusieurs produits. Supposons qu'il renvoie ce document XML très basique lorsque nous demandons des informations sur le produit P-12345 :

    [HTML_TAG_1]
      [HTML_TAG_2]
        [HTML_TAG_3]
          [HTML_TAG_4]Product 12345[HTML_TAG_5]
          [HTML_TAG_6]99.90[HTML_TAG_7]
        [HTML_TAG_8]
      [HTML_TAG_9]

Le nœud racine est **Products**, et à l'intérieur il y a un seul nœud **ProductInfo** qui représente le produit que nous avons demandé. A l'intérieur il y a un nœud **Name** et un nœud **Price**, qui ont tous deux un contenu texte à l'intérieur.

Dès la réception de ce document XML de l'API, nous pouvons analyser son contenu afin de vérifier que l'API se comporte correctement. Par exemple, nous pourrions parcourir ce document, jusqu'au nœud **Name**, pour extraire le nom du produit. La requête XPath suivante récupère cette valeur :

[INLINE_CODE_1]

Remarquez comment cet exemple mentionne chaque nœud dans la hiérarchie pour accéder au nœud **Name**, et utilise finalement la fonction pour récupérer le texte à l'intérieur de ce nœud **Name**.

Si nous utilisons cette requête XPath dans une assertion d'API multi-étape, nous pourrons vérifier que la valeur existe bel et bien dans le document XML et qu'elle a la valeur attendue :

![]([LINK_URL_4])

## Exemple 2 : Une enveloppe SOAP avec des préfixes

Si votre API est un service Web SOAP, le code XML renvoyé peut ressembler à ceci :

    [HTML_TAG_10]
      [HTML_TAG_11]
        [HTML_TAG_12]
          [HTML_TAG_13]
            [HTML_TAG_14]
              [HTML_TAG_15]
                [HTML_TAG_16]Product 12345[HTML_TAG_17]
                [HTML_TAG_18]99.90[HTML_TAG_19]
              [HTML_TAG_20]
            [HTML_TAG_21]
          [HTML_TAG_22]
        [HTML_TAG_23]
      [HTML_TAG_24]

Cela nous permet de définir une requête XPath disposant d'un sélecteur de nœuds complet pour chaque nœud du chemin que nous voulons sélectionner. La requête XPath suivante renvoie la valeur 99.90 :

[INLINE_CODE_2]

Notez qu’il faut inclure le bon préfixe pour chaque nœud de notre requête. En cas d'oubli (d'un préfix), la requête XPath échouera parce que XPath 1.0 nécessite une référence de nom complet pour chaque nœud, y compris son préfixe. Néanmoins, nous pouvons simplifier cette requête un peu parce qu'il n'y a qu'un seul produit dans le document, et un seul nœud **Price**. Comme il n'y a pas d'ambiguïté ici, nous pouvons naviguer vers le nœud **Price** directement en utilisant l'opérateur // :

[INLINE_CODE_3]

Notez que nous devons toujours inclure le préfixe

Jusque-là, nous avons extrait le texte interne d'un nœud. Et si on veut plutôt extraire la valeur d'un attribut (comme l'attribut Id avec la valeur "P-12345") ? Vous pouvez simplement utiliser l'opérateur XPath @. Cette requête XPath renvoie la valeur P-12345 :

[INLINE_CODE_4]

## Exemple 3 : Données SOAP avec plusieurs objets

Dans notre exemple précédent, il n'y avait pas d'ambiguïté car tout était préfixé et il n'y avait qu'un seul objet **product:ProductInfo** dans notre document XML. Mais que se passe-t-il si nous avons une méthode SOAP qui retourne une liste d'objets ? Prenons ce document XML, qui répertorie plusieurs produits (seulement deux pour simplifier) :

    [HTML_TAG_25]
      [HTML_TAG_26]
        [HTML_TAG_27]
          [HTML_TAG_28]
            [HTML_TAG_29]
              [HTML_TAG_30]
                [HTML_TAG_31]Product 12345[HTML_TAG_32]
                [HTML_TAG_33]99.90[HTML_TAG_34]
              [HTML_TAG_35]
              [HTML_TAG_36]
                [HTML_TAG_37]Product 24680[HTML_TAG_38]
                [HTML_TAG_39]45.99[HTML_TAG_40]
              [HTML_TAG_41]
            [HTML_TAG_42]
          [HTML_TAG_43]
        [HTML_TAG_44]
      [HTML_TAG_45]

Si nous voulons accéder au tout premier produit et sélectionner son prix, nous pouvons utiliser la requête suivante qui renvoie 99.90. Rappelez-vous que la numérotation des indices des tableaux XPath commencent à 1, donc nous utilisons une valeur d'index de 1 :

[INLINE_CODE_5]

De même, nous pourrions sélectionner le prix du dernier produit, ce qui retournerait 45.99:

[INLINE_CODE_6]

Nous pourrions même choisir un produit basé sur son attribut Product **Id**. Cette requête cherche un produit dont l'Id est égal à P-24680 et sélectionne son prix - retournant 45.99 :

[INLINE_CODE_7]

## Exemple 4: Données XML avec des préfixes vides

Pour cet exemple, nous utiliserons à nouveau les données SOAP, mais l'idée s'applique à tout document XML ayant les mêmes caractéristiques. Dans nos précédents exemples SOAP, chaque nœud avait un préfixe. Mais la réponse XML de votre API peut renvoyer du XML qui n'a pas de préfixe partout.

Dans XPath 1.0, chaque nœud soumis à un espace de nom doit être spécifié avec son préfixe. Cela devient difficile lorsque certains nœuds ont un préfixe vide. Vous ne pouvez pas spécifier un préfixe vide dans une requête XPath, donc la sélection de ces nœuds devient compliquée.

Regardons le XML suivant, qui a des préfixes pour l'enveloppe et le corps SOAP, mais pas pour les nœuds internes. Notez qu'aucun espace de noms supplémentaire n'a été défini pour les nœuds de produit :

    [HTML_TAG_46]
      [HTML_TAG_47]
        [HTML_TAG_48]
          [HTML_TAG_49]
            [HTML_TAG_50]
              [HTML_TAG_51]
                [HTML_TAG_52]Product 12345[HTML_TAG_53]
                [HTML_TAG_54]99.90[HTML_TAG_55]
              [HTML_TAG_56]
            [HTML_TAG_57]
          [HTML_TAG_58]
        [HTML_TAG_59]
      [HTML_TAG_60]

Cela fonctionne toujours comme prévu, car les nœuds sans préfixe ne sont pas soumis à un espace de noms. Cette requête XPath renvoie 99.90 :

[INLINE_CODE_8]

Maintenant, regardons une variante qui elle, a un espace de noms supplémentaire. Remarquez l'attribut xmlns= "[URL_1]  au niveau racine, qui ne spécifie pas de préfixe (c'est-à-dire qu'il a un préfixe vide):

    [HTML_TAG_61]
      [HTML_TAG_62]
        [HTML_TAG_63]
          [HTML_TAG_64]
            [HTML_TAG_65]
              [HTML_TAG_66]
                [HTML_TAG_67]Product 12345[HTML_TAG_68]
                [HTML_TAG_69]99.90[HTML_TAG_70]
              [HTML_TAG_71]
            [HTML_TAG_72]
          [HTML_TAG_73]
        [HTML_TAG_74]
      [HTML_TAG_75]

Dans ce cas, les nœuds internes sont soumis à cet espace de noms, mais nous ne pouvons pas les sélectionner de la manière habituelle, car leur préfixe d'espace de nom est vide. Par conséquent, la requête suivante ne fonctionne pas et renvoie simplement une valeur vide :

[INLINE_CODE_9]

Malheureusement, il n'y a aucun moyen d'inclure un préfixe vide dans une requête XPath. Heureusement, il existe un moyen d'éviter le problème du préfixe vide. Nous pouvons utiliser la fonction XPath **local-name()** qui nous permet de sélectionner un nœud en utilisant son nom, sans avoir à spécifier le préfixe :

[INLINE_CODE_10]

Cette requête est constituée des éléments suivants :

// : opérateur descendant : sélectionne tous les nœuds descendants à partir de la racine  
\* : opérateur générique : n'importe quel nœud, quel que soit son nom  
\[local-name()="Price"\] : sélectionne uniquement les nœuds ayant un nom local (c'est-à-dire excluant tout préfixe) égal à Price  
 : sélectionne le texte interne du ou des nœuds sélectionnés

En reprenant nos exemples précédents qui avaient plusieurs nœuds ProductInfo dans le XML, nous pouvons combiner plusieurs stratégies pour sélectionner les nœuds qui nous intéressent. Cette requête sélectionne le nœud ProductInfo avec Id est égal à P-24680, puis récupère le texte interne de son nœud Price :

[INLINE_CODE_11]

## Exemple 5 : Des fonctions XPath

Les exemples précédents utilisaient des requêtes XPath pour vérifier l'existence d'un ou de plusieurs nœuds dans un document XML et ensuite renvoyer le contenu d'un nœud ou d'un attribut de nœud. En plus de chercher des nœuds et leurs contenus, XPath permet également d'exécuter certaines fonctions.  En gardant à l'esprit que seules les fonctions XPath 1.0 sont disponibles, voici quelques exemples :

| **Fonction**                                                                                                                                                                                                                                                                                                        | **Exemple de requête**                | **Valeur** |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|------------|
| La fonction **count()** compte combien de nœuds sont trouvés en utilisant l'argument que vous spécifiez. Il renvoie une valeur numérique que vous pouvez utiliser dans une assertion. Par exemple, vous pouvez configurer une assertion qui vérifie que le nombre de produits renvoyés est supérieur ou égal à 100. | count(//ProductInfo)                  | 2          |
| La fonction **contains ()** vérifie si la valeur de chaîne sélectionnée contient la sous-chaîne que vous spécifiez. Renvoie Vrai (True) ou Faux (False).                                                                                                                                                            | contains(//ProductInfo/Name, "12345") | True       |
| La fonction **sum()** calcule la somme des valeurs numériques des nœuds sélectionnés.                                                                                                                                                                                                                               | sum(//ProductInfo/Price)              | 145.89     |
