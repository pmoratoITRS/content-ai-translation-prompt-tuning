{
  "hero": {
    "title": "Variables automatiques"
  },
  "title": "Variables automatiques",
  "summary": "Liste des variables automatiques à utiliser dans les moniteurs de transactions et Multi-step API",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/variables-automatiques",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les types de moniteurs [Transaction]([LINK_URL_1]) et [Multi-Step API]([LINK_URL_2]) d'Uptrends vous permettent de suivre un parcours composé de plusieurs étapes, soit sur une page web, soit en interagissant directement avec une API. Dans certains cas, vous aurez peut-être à soumettre des données. Par exemple, un formulaire dans l'une de vos transactions peut nécessiter un horodatage, ou vous devrez peut-être générer un identifiant unique à utiliser dans l'une des requêtes API. Uprends vous fournit un certain nombre de **variables automatiques**. La plupart d'entre elles sont en fait des fonctions qui génèrent une valeur que vous pouvez utiliser dans vos requêtes HTTP, insérer dans des champs textuels ou ajouter aux sélecteurs dans vos moniteurs de transactions.

## Variables automatiques génériques

Les variables automatiques suivantes sont disponibles pour les types de moniteurs **Transaction** et **API multi-étapes** :

### Date et heure

[SHORTCODE_1][SYSTEM_VAR_1][SHORTCODE_2] : Cette variable génère des valeurs dynamiques de date et heure, selon le format que vous spécifiez et avec un décalage (offset) facultatif. La date/heure (sans un décalage) est toujours l'heure actuelle exprimée en UTC (coordinated universal time).

Pour formatter la date/heure selon vos besoins, définissez le paramètre [INLINE_CODE_1] sur :

- une valeur compatible avec le formatage de date .NET, par exemple [INLINE_CODE_2] ou alors [INLINE_CODE_3]
- [INLINE_CODE_4], pour le format ISO 8601
- [INLINE_CODE_5], pour l'époque Unix

L'option [INLINE_CODE_6] peut être utilisée pour recalculer la date/heure en fonction d'une différence donnée (en secondes) ou d'une fonction date/heure. Si le paramètre de décalage est absent, aucun décalage n'est appliqué. Pour recalculer la date et l'heure, utilisez les options suivantes :

- Donnez au paramètre de décalage une valeur en secondes, positive ou négative. Le nombre de secondes spécifié est ajouté ou soustrait de la valeur de date/heure actuelle. Un cas d'utilisation typique est de calculer la date et l'heure dans un fuseau horaire différent ou de passer à un jour différent avant ou après la date/heure actuelle.

   Le tableau ci-dessous présente quelques exemples.

- Utilisez une fonction de date/heure pour calculer le dernier ou le premier jour du mois en cours, du mois précédent ou du mois suivant, par rapport à la valeur de date/heure donnée. Les valeurs possibles pour le décalage sont :
   - [INLINE_CODE_7]
   - [INLINE_CODE_8]
   - [INLINE_CODE_9]
   - [INLINE_CODE_10]
   - [INLINE_CODE_11]
   - [INLINE_CODE_12]

Le tableau ci-dessous montre quelques exemples pour une date/heure de 24 février 2018 à 22h30 UTC.
| Expression                                  | Valeur                        | Description                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| [INLINE_CODE_13]           | 24-02-2018 22:30             | Maintenant, au format dd-MM-yyyy HH:mm               |
| [INLINE_CODE_14]    | 24-02-2018 17:30             | Maintenant, au fuseau horaire EST (côte Est américaine)  (UTC-5)         |
| [INLINE_CODE_15]                        | 2018-02-24T22:30:00.0000000Z | Maintenant, au format ISO 8601                        |
| [INLINE_CODE_16]                       | 1519511400                   | Maintenant, au format Unix epoch                       |
| [INLINE_CODE_17]          | 02/23/2018                   | Hier, au format MM/dd/yyyy               |
| [INLINE_CODE_18]           | 02/25/2018                   | Demain, au format MM/dd/yyyy                |
| [INLINE_CODE_19] | 02/01/2018                   | Premier jour du mois, au format MM/dd/yyyy |
| [INLINE_CODE_20]  | 02/28/2018                   | Dernier jour du mois, au format MM/dd/yyyy  |

### Identifiant unique aléatoire

[SHORTCODE_3][SYSTEM_VAR_10][SHORTCODE_4] : Cette variable produit une valeur aléatoire sous la forme [INLINE_CODE_21]. Vous pouvez utiliser cette variable si vous devez inclure une valeur aléatoire dans votre URL, vos données POST ou votre en-tête HTTP. Si vous utilisez la variable [SHORTCODE_5]@RandomGuid[SHORTCODE_6] dans plusieurs étapes, chaque étape aura une valeur aléatoire différente. À chaque exécution du moniteur, vous obtiendrez de nouvelles valeurs aléatoires.
### Identifiant unique aléatoire récurrent
[SHORTCODE_7][SYSTEM_VAR_11][SHORTCODE_8] : Cette variable unique et aléatoire peut être réutilisée plusieurs fois tout au long de la transaction. À la différence de la variable [SHORTCODE_9]@RandomGuid[SHORTCODE_10] présentée ci-dessus, qui crée une nouvelle valeur à chaque fois, vous pouvez utiliser cette variable pour inclure une valeur récurrente dans votre URL, vos données POST ou votre en-tête HTTP.
Par exemple, cela peut vous être utile pour créer le script d'un processus d'inscription, dans lequel l'adresse e-mail générée et l'adresse e-mail confirmée doivent être identiques.
### Entier aléatoire

[SHORTCODE_11][SYSTEM_VAR_12][SHORTCODE_12] : Cette variable produit un nombre entier aléatoire, entre les valeurs minimum et maximum que vous spécifiez (minimum et maximum incluses). Par exemple, si vous spécifiez [INLINE_CODE_22], cette variable produit un nombre compris entre 0 et 100.
### Lettres aléatoires en majuscules

[SHORTCODE_13][SYSTEM_VAR_14][SHORTCODE_14] : Cette variable automatique vous permet de générer une série aléatoire de caractères alphabétiques dans une longueur donnée. Tous les caractères seront en majuscules. Par exemple, [INLINE_CODE_23] produit une valeur aléatoire sous la forme [INLINE_CODE_24].
### Identifiants aléatoires pour les bénéficiaires Medicare (aux États-Unis)
[SHORTCODE_15][SYSTEM_VAR_16][SHORTCODE_16] : Cette variable automatique vous permet de générer des identifiants pour les bénéficiaires du programme Medicare aux États-Unis. Ces identifiants, connus sous l'acronyme MBI (Medicare Beneficiary Identifier), sont composés d'une série de 11 caractères alphanumériques. Par exemple, [INLINE_CODE_25]. Veuillez noter que le code est généré sans tiret. Les codes MBI peuvent être utilisés par les entreprises du secteur de la santé aux États-Unis.

## Variables (héritées) spécifiques à la transaction

L'ensemble suivant de variables automatiques est plus ancien, mais peut toujours être utilisé. Ces variables ne sont disponibles que pour les moniteurs **Transaction**.

### Horodatages

[SHORTCODE_17]{timespan 0}{now dd-MM-yyyy}[SHORTCODE_18] : Pour **appliquer un horodatage** (date actuelle) dans un champ de texte sur votre page.

[SHORTCODE_19]{timespan 1:0:0:0}{now dd-MM-yyyy}[SHORTCODE_20] : Pour **décaler d'un jour** (demain).

[SHORTCODE_21]{timespan 0:1:0:0}{now dd-MM-yyyy}[SHORTCODE_22] : comme ci-dessus, mais pour un **décalage de 1 heure**.

[SHORTCODE_23]{timespan 0:0:1:0}{now dd-MM-yyyy}[SHORTCODE_24] et [SHORTCODE_25]{timespan 0:0:0:1}{now dd-MM-yyyy}[SHORTCODE_26] : Décaler l'heure actuelle d'une minute ou d'une seconde, respectivement.

### Valeur aléatoire à partir d'un tableau

[SHORTCODE_27]{random 1 2 3 4 5}[SHORTCODE_28] : Définir une variable aléatoire à partir d'un tableau. Cette fonction définit de manière aléatoire une des valeurs de un à cinq.

[SHORTCODE_29]{random pomme banane orange}[SHORTCODE_30] : Cette fonction définit de manière aléatoire une des chaînes du tableau, soit [INLINE_CODE_26], [INLINE_CODE_27], ou [INLINE_CODE_28].

## Variables spécifiques à l'API multi-étapes

Les variables et informations suivantes ne s'appliquent qu'aux moniteurs de type **API multi-étapes**.

### Identification du serveur (ID)

[SHORTCODE_31][SYSTEM_VAR_17][SHORTCODE_32] : Lors de l'exécution d'un moniteur d'API multi-étapes, cette variable génère une valeur numérique qui identifie l'emplacement du point de contrôle Uptrends qui exécute cette vérification. Par exemple, si la vérification est en cours d'exécution sur le point de contrôle d'Uptrends à Sydney, en Australie, la variable affichera la valeur [INLINE_CODE_29]. La liste des serveurs de checkpoints et des **identifiants de serveur** correspondants est disponible via [l'API d'Uptrends]([LINK_URL_3]) au [endpoint Checkpoint]([LINK_URL_4]).

### URL de redirection

[SHORTCODE_33][SYSTEM_VAR_18][SHORTCODE_34] : Si l'une des étapes de votre moniteur doit renvoyer un code de redirection et que vous souhaitez le capturer et tester plutôt que de le suivre automatiquement, cette variable automatique contiendra l'URL à laquelle la redirection fait référence. Cela ne se produit que si vous choisissez de ne pas suivre automatiquement les redirections, et que vous configurez une assertion qui vérifie le code de redirection approprié. Pour en savoir plus, lisez l'article [Multi-step monitoring - Gestion des redirections]([LINK_URL_5]).

### Flottant aléatoire

[SHORTCODE_35][SYSTEM_VAR_19][SHORTCODE_36] : Utilisez cette fonction pour générer un nombre en virgule flottante compris dans l'intervalle (min/max) indiqué. La précision (nombre de décimales après la virgule) du flottant généré est dérivée de la plus haute précision des valeurs [INLINE_CODE_30] et [INLINE_CODE_31].

Par exemple, la variable [INLINE_CODE_32] générera un flottant aléatoire compris entre -1,2 et 3,0, avec une précision de 5, comme 2,12345.

## Comment utiliser une valeur générée automatiquement plusieurs fois de suite

Certaines de ces fonctions variables (en particulier celles produisant des valeurs aléatoires ou des valeurs date/heure) sont réévaluées chaque fois que vous les utilisez, et généreront donc une nouvelle valeur à chaque fois. Si vous souhaitez générer une valeur particulière et l'utiliser plusieurs fois tout au long de votre scénario multi-étapes, vous pouvez utiliser une variable prédéfinie (comme expliqué dans l'article sur les [variables de surveillance multi-étapes]([LINK_URL_6])) et lui assigner comme valeur une variable automatique.

### Exemples de variables prédéfinies utilisant des variables automatiques

| Nom | Valeur | Utilisation |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_33] | [INLINE_CODE_34] | Une valeur de date à utiliser comme entrée pour une requête de recherche. |
| [INLINE_CODE_35] | [INLINE_CODE_36] | Une valeur guid aléatoire combinée avec du texte fixe pour générer une adresse e-mail qui est différente à chaque fois. |
| [INLINE_CODE_37] | [INLINE_CODE_38] | Un nombre aléatoire compris entre 1 et 10 à utiliser comme nombre de produits à commander. Lors d'un appel ultérieur, vous pouvez réutiliser cette variable pour vérifier le contenu d'un panier et voir s'il contient effectivement ce nombre d'articles. |
