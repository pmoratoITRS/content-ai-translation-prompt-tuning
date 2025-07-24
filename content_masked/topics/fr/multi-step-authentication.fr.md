{
  "hero": {
    "title": "Authentification lors de la surveillance multi-étapes"
  },
  "title": "Authentification lors de la surveillance multi-étapes",
  "summary": "Découvrez les options disponibles pour l'authentification lors de l'utilisation de la surveillance API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/authentification-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De nombreuses API exigent que l'appelant spécifie des informations d'authentification pour la vérification de son identité, et parfois de ses droits d'accès. Les informations d'authentification peuvent être transmises via des en-têtes HTTP (authentification basique/NTLM/Digest ), en échangeant des jetons d'accès (OAuth), en demandant au client d'inclure un certificat client dans la requête, ou via une combinaison de ces méthodes.

Cet article décrit deux types d'authentification utilisés dans Uptrends, celui basé sur les en-têtes HTTP et celui basé sur des jetons. Pour configurer les certificats clients, lisez [l'article sur l'authentification par certificat client]([LINK_URL_1]) .

## Types d'authentification par défaut

La section Authentification de l'onglet Étapes d'un moniteur d'API multi-étapes propose plusieurs types d'authentification. Ils utilisent tous une combinaison nom-utilisateur/mot-de-passe, mais la façon dont ces informations d'identification sont traitées et envoyées à l'API est différente pour chaque type :

- **Authentification de base** : le nom d'utilisateur et le mot de passe sont encodés avec le format simple Base-64 et envoyés au serveur API.
- **Authentification  NTLM (Windows)** : lorsque vous spécifiez ce type, plusieurs requêtes sont envoyées à l'API pour déterminer quelle  authentification doit être utilisée, avant que la demande HTTP finale soit envoyée avec l'authentification adéquate. Cette séquence de requêtes compte comme une seule étape. Si un domaine Windows doit être spécifié, incluez-le dans le nom d'utilisateur : VOTREDOMAINE\\Nom d'utilisateur
- **Authentification (méthode digest)** : le nom d'utilisateur et le mot de passe sont hachés au moyen de l'algorithme de hachage MD5, et le hashcode est envoyé au serveur.
- **Aucun** : sélectionnez *Aucun* si vous ne voulez pas appliquer d'authentification pour votre requête HTTP.

### En-têtes HTTP

Les types d'authentification décrits ci-dessus envoient tous plusieurs requêtes (même si toutes comptent comme une même étape). La première requête n'inclut pas d'informations d'identification (hachées/encodées/autres). Le client attend que le serveur envoie un challenge sous la forme d'un code de réponse 401 Unauthorized, et un en-tête **WWW-Authenticate** qui précise la méthode d'authentification requise. Puis le client renvoie la requête, en incluant cette fois l'en-tête d'authentification demandé.

Lorsque vous utilisez l'un de ces types d'authentification, vous n'avez généralement pas besoin de spécifier d'autres en-têtes HTTP contenant une authentification : l'en-tête Authorization est généré automatiquement. Cependant, si le challenge est incomplet (par exemple, si le serveur répond avec un autre code de statut que 401 ou sans l'en-tête WWW-Authenticate), le moniteur renverra une erreur et vous devrez peut-être définir manuellement l'en-tête Authorization demandé.

Par exemple, pour l'authentification de base, le serveur doit répondre avec un challenge après la première requête, avec l'en-tête [INLINE_CODE_1] et le code de statut 401 Unauthorized. Si ce n'est pas le cas, vous pourriez devoir définir manuellement l'en-tête d'authentification de base, pour transmettre les informations d'identification sans passer par le challenge.

Pour le [modèle d'authentification de base]([LINK_URL_2]), les informations d'identification doivent être transmises sous la forme d'une chaîne encodée en Base64, au format suivant : *nom d'utilisateur:mot de passe*. La chaîne d'encodage en Base64 'nom d'utilisateur:mot de passe' génère la valeur [INLINE_CODE_2] qui doit ensuite être incluse via un en-tête Authorization. En ajoutant l'en-tête [INLINE_CODE_3] à l'étape MSA, vous pouvez efficacement contourner la nécessité du challenge.

### Prise en charge des Variables

Les champs nom d'utilisateur et mot de passe acceptent l'utilisation de variables. Vous pouvez créer des variables prédéfinies (par exemple : [SHORTCODE_1]{{username}}[SHORTCODE_2] et [SHORTCODE_3]{{password}}[SHORTCODE_4]) avec les valeurs appropriées, puis utiliser ces noms de variables dans les champs d'authentification. [Plus d'informations sur les variables et les variables prédéfinies ici.]([LINK_URL_3])

## Authentification personnalisée (et pour OAuth)

Si votre API utilise OAuth comme protocole d'authentification, vous aurez besoin d'une configuration plus élaborée. En fonction de votre API, vous pourrez avoir besoin de quelque chose de spécifique à votre situation. En particulier, OAuth 2.0 utilise au moins une requête spéciale juste pour le processus d'authentification. Cette requête demande l'accès à l'API (en utilisant soit l'un des types d'authentification par défaut, soit en spécifiant les informations de connexion dans l'URL, ou même en effectuant une connexion à une page web). Une fois l'authentification réussie, le jeton d'accès OAuth est capturé et stocké dans une variable pour être utilisé dans les requêtes suivantes.

Si vous n'utilisez pas OAuth mais un protocole différent, le fonctionnement pourrait être similaire : vous devez d'abord spécifier les informations de connexion qui "prouvent" votre identité à l'API. Le serveur API répondra en vous donnant un jeton de connexion valide pendant un certain temps. En capturant ce jeton et en le stockant dans une variable, vous pourrez exécuter une séquence de requêtes utilisant ce jeton d'accès pour vous connecter.

### Configuration de l'authentification OAuth 2.0 [ANCHOR_1]

Dans l'exemple qui suit, nous allons mettre en place une forme simple d'authentification OAuth 2.0. Notre objectif est d'acquérir un jeton d'accès à partir de l'API, que nous pouvons ensuite utiliser dans des requêtes ultérieures.

Pour ce faire, nous enverrons d'abord une requête contenant les champs OAuth appropriés. Dans ce cas, nous demandons un accès basé sur un code d'autorisation, un identifiant client et un secret client. L'identifiant client et le secret client auront des valeurs fixes que nous pouvons définir en tant que variables prédéfinies. Dans notre configuration simple, le code d'autorisation aura également une valeur fixe, mais dans votre configuration, il pourrait être nécessaire de récupérer ce code d'autorisation en utilisant une étape distincte.

Nous allons d'abord ajouter ces valeurs aux variables prédéfinies :

![Predefined variables]([LINK_URL_4])

Avec ces variables définies, nous pouvons maintenant configurer une requête à notre API en rajoutant des références à ces variables et d'autres paramètres attendus par l'API. Dans la première étape de notre configuration multi-étapes, ajoutez cette URL :

[INLINE_CODE_4]

Nous nous attendons à ce que l'API renvoie une structure de données contenant le jeton d'accès dont nous avons besoin, mais comment cette structure de données sera-t-elle formattée ? Pour nous assurer que nous aurons des données formatées JSON, nous devons dire au serveur que nous n'accepterons que le format application/json en le spécifiant dans un en-tête HTTP :

![MSA accept header]([LINK_URL_5])

Ceci fait, nous pouvons maintenant nous attendre à ce que la réponse ressemble à ceci :

[INLINE_CODE_5]

Tout ce qui reste faire maintenant, c'est capturer le champ access\_token  dans la réponse JSON. Pour ce faire, nous allons créer une nouvelle variable dans l'onglet Réponse de notre étape :

- La réponse devrait contenir JSON, alors il faut choisir Response body as JSON comme la source de notre variable.
- Puisque l'attribut **access\_token** est situé au plus haut niveau dans notre structure de données, notre expression JSON est simplement [SHORTCODE_5]access\_token[SHORTCODE_6].
- Nous allons choisir [SHORTCODE_7]accesstoken[SHORTCODE_8] comme notre nom de variable. C'est le nom que nous utiliserons dans les étapes suivantes.

![Access token variable]([LINK_URL_6])

Même si l'objectif principal de cette première étape est de capturer le jeton d'accès, elle effectue également de la surveillance : si l'API renvoie une erreur à ce stade, ou si la réponse ne contient pas de jeton d'accès, une erreur sera signalée.

Maintenant que nous avons un jeton d'accès valide, nous pouvons enfin accéder à la méthode API que nous voulons vérifier (par exemple, pour récupérer une liste de produits). Créez une nouvelle étape pour définir cet appel d'API. Après avoir spécifié la méthode et l'URL pour cette nouvelle requête, nous pouvons transmettre le jeton d'accès que nous venons de capturer. Les API basées sur OAuth 2.0 attendent un en-tête HTTP appelé **Authorization**, avec une valeur [INLINE_CODE_6]

![Access token header]([LINK_URL_7])

Nous pouvons faire pareil pour chaque étape supplémentaire qui nécessite le même jeton d'accès.
