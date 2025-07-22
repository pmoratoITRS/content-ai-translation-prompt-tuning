{
  "hero": {
    "title": "Personnalisation des scripts pour les moniteurs d'API multi-étapes"
  },
  "title": "Personnalisation des scripts pour les moniteurs d'API multi-étapes",
  "summary": "Découvrez les options de personnalisation des scripts pour le monitoring d'API multi-étapes",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/personnalisation-script-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le moniteur d'API multi-étapes s'accompagne de puissantes [fonctions intégrées]([LINK_URL_1]) qui fournissent une solution sans code facile à employer pour tester le comportement de vos API.

L'approche sans code est très commode pour configurer des moniteurs, mais il est possible que vous ayez besoin d'un langage de script pour effectuer des tests fonctionnels approfondis et décrire en détail ce que vous attendez de vos API. Par exemple, vous pouvez avoir besoin d'ajouter une logique personnalisée ou de gérer des comportements plus avancés qui ne peuvent pas être traités dans une simple interface.

Le moniteur MSA vous permet d'utiliser à la fois les fonctionnalités sans code et les scripts personnalisés. Vous pouvez associer les fonctions d'interface intégrées et les fonctions de scripts. Ainsi, vous n'avez pas à créer entièrement de nouveaux moniteurs si vous voulez ajouter des scripts personnalisés à des moniteurs d'API existants. Commencez simplement par ajouter quelques scripts à votre configuration.

## Script de pré-requête et de post-réponse

Un moniteur d'API peut exécuter une seule ou plusieurs étapes à la suite. Pour chaque étape du moniteur MSA (à l'exception des étapes d'attente), deux éditeurs de scripts sont disponibles :
[SHORTCODE_1] Pré-Requête [SHORTCODE_2] et [SHORTCODE_3] Post-Réponse [SHORTCODE_4].

- L'éditeur de **script de pré-requête** vous permet d'écrire des scripts pour préparer l'envoi d'une requête HTTP. Cette étape est utile pour préparer et calculer les valeurs à inclure dans la requête, comme les variables d'environnement, les paramètres d'URL, les en-têtes de requête ou le contenu du corps de requête. Le script écrit dans cet éditeur s'exécute *avant* que la requête API soit envoyée au serveur.

- L'éditeur de **script de post-réponse** vous permet d'écrire des scripts pour vérifier et traiter la réponse HTTP fournie par l'API. Cette étape est utile pour définir une logique personnalisée permettant de vérifier les en-têtes de réponse, de valider l'exhaustivité et la cohérence de votre contenu et d'utiliser ces données pour préparer les étapes suivantes. Le script écrit dans l'éditeur s'exécute uniquement *après* que la réponse d'API a été reçue depuis le serveur. Si une erreur de connexion se produit, le script n'est pas exécuté et toute assertion ou variable dans l'onglet [SHORTCODE_5] Réponse [SHORTCODE_6] n'est pas validée.

Ces éditeurs incluent aussi les fonctionnalités suivantes :
![Onglets liés aux scripts personnalisés]([LINK_URL_2])

- Numérotation des lignes : affiche des valeurs numériques qui permettent d'identifier les scripts ou les codes ligne par ligne.
- Mise en surbrillance du code : affiche les codes dans une couleur qui permet de repérer facilement les erreurs de syntaxe et les mots-clés.
- Remplissage du code : suggère automatiquement des combinaisons de code pour faciliter l'écriture.
- Extraits de code : un panneau fournit une liste d'extraits de code utiles que vous pouvez insérer automatiquement dans votre éditeur de code au moyen d'un simple clic.

## Extraits de code

Les éditeurs de scripts **pré-requête** et **post-réponse** vous permettent d'insérer et d'exécuter des scripts écrits en langage Javascript. En plus de toutes les possibilités offertes par Javascript, vous pouvez utiliser les **extraits de code**.

Les **extraits de code** sont des fonctions spéciales qui vous permettent d'accéder aux données des requêtes HTTP (pendant le processus de pré-requête) et des réponses HTTP (pendant le processus de post-réponse). Ils vous permettent aussi d'exécuter des instructions de log, de stocker des données calculées sous forme de [métriques personnalisées]([LINK_URL_3]), et d'exécuter des tests sur les données des étapes. Ces fonctions spéciales sont disponibles via un objet unique appelé [INLINE_CODE_1].

## Objets ut généraux/de base

La liste des objets [INLINE_CODE_2] généraux est fournie dans cette section :

- [INLINE_CODE_3] vous donne accès à l'objet de requête d'API.
- [INLINE_CODE_4] vous donne accès à l'objet de réponse d'API.
- [INLINE_CODE_5] désigne la collection de variables que vous pouvez utiliser dans les étapes d'API. Vous pouvez utiliser cette fonction pour faire passer des valeurs d'une étape à la suivante. Les [variables prédéfinies]([LINK_URL_4]) ou les variables que vous utilisez dans l'onglet [SHORTCODE_7] Réponse [SHORTCODE_8] sont incluses dans la collection d'objets.
- [INLINE_CODE_6] est une fonction helper qui extrait les journaux indiqués dans le journal de la console. Lors de l'exécution des scripts de pré-requête, les logs se trouvent dans le **journal de la console du script de pré-requête**, tandis que les logs des scripts de post-réponse se trouvent dans le **journal de la console des scripts de post-réponse**.
- [INLINE_CODE_7] est la principale fonction de saisie des résultats du test. Le résultat de test que vous définissez à l'intérieur de chaque appel [INLINE_CODE_8] est enregistré et ajouté en tant que résultat d'**assertion**, aux côtés des assertions que vous définissez dans l'onglet [SHORTCODE_9] Réponse [SHORTCODE_10] de chaque étape.
- [INLINE_CODE_9] est une collection de valeurs numériques provenant directement d'une réponse d'API. Vous pouvez définir votre propre variable de métrique personnalisée pour enregistrer ou calculer les valeurs à partir de la réponse d'API. Cette valeur s'affiche pour chaque mesure dans les détails de vérification du moniteur, et peut aussi être listée et présentée sur les dashboards.
- [INLINE_CODE_10] permet de générer des hash MD5 et SHA pour manipuler et transmettre les données en toute sécurité. Cette fonction permet aussi d'analyser les listes de révocation de certificats (CRL).

Vous connaissez désormais les objets [INLINE_CODE_11] de base/généraux. La section ci-dessous détaille les attributs de chaque objet [INLINE_CODE_12].

### Requête

Attributs de [INLINE_CODE_13] :

- [INLINE_CODE_14] : obtient ou définit l'URL de requête.
- [INLINE_CODE_15] : obtient ou définit la méthode HTTP de la requête (par exemple GET et POST).
- [INLINE_CODE_16] : obtient ou définit une version sous forme de texte brut du corps de la requête.

### En-têtes de requête

Fonctions de [INLINE_CODE_17]:

- [INLINE_CODE_18] : indique si l'en-tête existe et présente une valeur spécifique.
- [INLINE_CODE_19] : indique la valeur de l'en-tête ou renvoie une chaîne vide si l'en-tête n'existe pas.
- [INLINE_CODE_20] : crée un nouvel en-tête et sa [INLINE_CODE_21] spécifiée (seulement si l'en-tête n'a pas encore été défini).
- [INLINE_CODE_22] : insère l'en-tête avec la [INLINE_CODE_23] spécifiée (si l'en-tête n'existe pas déjà) ou actualise l'en-tête avec la valeur spécifiée (si l'en-tête existe).
- [INLINE_CODE_24] : retire l'en-tête.

### Réponse

Attributs de [INLINE_CODE_25] :

- [INLINE_CODE_26] : obtient le code de statut numérique de la réponse HTTP (par exemple, 200, 404, 500).
- [INLINE_CODE_27] : obtient la description du statut HTTP (par exemple, OK).
- [INLINE_CODE_28] : obtient la taille de la réponse en octets.
- [INLINE_CODE_29] : fournit un tableau d'octets contenant le corps de la requête. Les réponses ne peuvent excéder 100 Mo.

Fonctions de l'objet [INLINE_CODE_30] :

- [INLINE_CODE_31] : renvoie une version sous forme de texte brut du corps de la réponse.
- [INLINE_CODE_32] : renvoie un objet en analysant le texte de la réponse sous format JSON.

### En-têtes de réponse

Fonctions de [INLINE_CODE_33]:

- [INLINE_CODE_34] : indique si l'en-tête existe.
- [INLINE_CODE_35] : indique la valeur de l'en-tête ou renvoie une chaîne vide si l'en-tête n'existe pas.

### Variables

Fonctions de [INLINE_CODE_36] :

- [INLINE_CODE_37] : indique si la variable existe.
- [INLINE_CODE_38] : indique la valeur de la variable ou renvoie une chaîne vide si la variable n'existe pas.
- [INLINE_CODE_39] :  crée la variable (si elle n'existe pas) et enregistre la [INLINE_CODE_40] spécifiée dans la variable [INLINE_CODE_41].

### Métriques personnalisées

Fonctions de [INLINE_CODE_42] :

- [INLINE_CODE_43] : indique la valeur de la variable de métrique personnalisée ou renvoie une chaîne vide si la métrique personnalisée n'existe pas.
- [INLINE_CODE_44] : enregistre la [INLINE_CODE_45] spécifiée dans la variable [INLINE_CODE_46] de la métrique personnalisée.

Pour en savoir plus, consultez les articles de notre base de connaissances intitulés [Configuration des métriques personnalisées]([LINK_URL_5]) et [Variables de monitoring d'API multi-étapes]([LINK_URL_6]).

### Test ou assertion

Uptrends prend en charge les interfaces Expect et Should de Chai JS. Lisez [Chai - Should]([LINK_URL_7]) et [Chai - Expect]([LINK_URL_8]) pour en savoir plus sur l'expression des tests de valeur et des comparaisons :

- [INLINE_CODE_47] + différentes expressions
- [INLINE_CODE_48] + différentes expressions

Lorsqu'elles sont utilisées seules et que les critères ne sont pas remplis, les expressions [INLINE_CODE_49] et [INLINE_CODE_50] génèrent une erreur qui interrompt l'exécution du moniteur. Toute autre assertion figurant dans le restant du script ne sera pas exécutée.

Utilisez [INLINE_CODE_51] pour exécuter l'ensemble des assertions malgré l'échec possible de l'une d'entre elles :

- [INLINE_CODE_52] : le résultat (succès ou échec) d'une assertion [INLINE_CODE_53] ou [INLINE_CODE_54] définie dans la fonction spécifiée testFunction est présentée dans les résultats des assertions du moniteur. De plus, lorsqu'une assertion échoue, la fonction [INLINE_CODE_55] garantit que l'exécution du script n'est pas interrompue.

## Hachage

Fonctions de [INLINE_CODE_56] :

- [INLINE_CODE_57] : génère un hash MD5 de la valeur précisée.
- [INLINE_CODE_58] : génère un hash SHA-1 de la valeur précisée.
- [INLINE_CODE_59] : génère un hash SHA-256 de la valeur précisée
- [INLINE_CODE_60] : génère un hash SHA-512 de la valeur précisée.

Les méthodes de script permettant de générer des hash MD5 et SHA vous permettent de stocker et d'envoyer des valeurs de façon sécurisée, en garantissant la protection des données au moyen du hachage.

Exemple :

[CODE_BLOCK_1]

- [INLINE_CODE_61] : analyse une liste de révocation de certificats (CRL) et fournit ses métadonnées. Un fichier CRL doit être fourni pour permettre l'exécution de la fonction [INLINE_CODE_62]. Par exemple, si vous voulez lire le champ [INLINE_CODE_63] d'un fichier ou d'une URL CRL, vous pouvez utiliser cette fonction de la façon suivante :

[CODE_BLOCK_2]
