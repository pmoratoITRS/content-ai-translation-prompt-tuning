{
"hero": {
"title": "Hachage et encodage"
},
"title": "Valeurs de hachage et d'encodage",
"url": "/support/kb/synthetic-monitoring/surveillance-api/hachage-et-encodage",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/hashing-and-encoding"
}

Dans certains cas d'usage de la [surveillance des API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="fr" >}}), il peut être nécessaire de hacher ou d'encoder des variables ou des valeurs. Par exemple, la configuration des autorisations peut nécessiter un encodage en base64 ou un hachage avec la fonction HMAC-SHA-256 pour pouvoir travailler efficacement. Vous pouvez aussi avoir besoin d'inclure du contenu encodé au format JSON dans votre corps de requête. C'est pour cette raison qu'Uptrends propose plusieurs options d'encodage et de hachage, que nous vous présentons dans cet article.

## Encodage et décodage

L'encodage vise à s'assurer que les données peuvent être envoyées de façon fiable sous un format donné. Une chaîne de caractères ou un fichier peut être codé de façon à s'assurer que le destinataire comprend son format et peut le décoder.

### Base64
Base64 est un schéma d'encodage que l'on utilise habituellement pour convertir des données binaires en texte. Ce schéma est couramment utilisé dans les protocoles de type [Authentification de base](https://www.rfc-editor.org/rfc/rfc7617). Pour appliquer l'encodage en base64 à un moniteur API multi-étapes, utilisez la fonction `{{@Base64Encode(yourContentHere)}}`.

La fonction Base64Encode accepte aussi les [variables (prédéfinies)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}). Il suffit d'ajouter la variable de référence (entourée d'accolades) dans la fonction : `{{@Base64Encode({{yourVariableName}})}}`.

Le décodage est aussi possible avec la fonction `{{@Base64Decode()}}`.

Les fonctions Base64Encode et Base64Decode peuvent être utilisées à toutes les étapes de la configuration des moniteurs API multi-étapes. Vous pouvez donc l'inclure directement dans votre en-tête de requête ou dans votre corps de requête, par exemple.

![Fonction Base64Encode utilisée dans un en-tête d'authentification](/img/content/scr-msa-base64-encode-auth-header.min.png)

### JSON et XML

JSON et XML sont deux formats d'échange de données. Tous deux doivent respecter un format strict pour être valides. Dans certains cas, le contenu JSON ou XML doit être encodé pour pouvoir être envoyé. Par exemple, un contenu JSON ne peut pas être intégré dans un autre contenu JSON. Un encodage est nécessaire pour éviter de briser la structure JSON. Autre exemple : si un contenu en texte brut contient des guillemets, ceux-ci ne peuvent pas être inclus dans un message au format JSON, car ils ont une signification propre dans ce format.

Tout comme les fonctions Base64Encoding et Base64Decoding décrites ci-dessous, Uptrends permet d'utiliser les fonctions JsonEncode(), JsonDecode(), XmlEncode() et XmlDecode(). Pour en savoir plus, reportez-vous à notre documentation sur [l'application du formatage automatique dans une intégration personnalisée ]({{< ref path="support/kb/alerting/integrations/custom-integrations/message-formatting#applying-automatic-formatting" lang="fr" >}}).

## Hachage {id="hashing"}

À la différence de l'encodage qui peut être décodé, le hachage est un processus unilatéral pour lequel un algorithme utilise une fonction mathématique pour transformer un message de n'importe quelle longueur en une valeur d'une longueur fixe. Il est pratiquement impossible d'inverser le hachage. Par ailleurs, une même entrée doit toujours donner lieu au même résultat. Le hachage est couramment utilisé dans le cadre de l'authentification, car il s'agit d'une méthode sécurisée pour échanger et comparer des informations confidentielles, comme des mots de passe ou des signatures.

Uptrends prend en charge les algorithmes de hachage suivants :

- MD5
- SHA1
- SHA256
- SHA512
- HMAC-SHA1
- HMAC-SHA256
- HMAC-SHA512

Le hachage est pris en charge par le système de [fonctions définies par l’utilisateur]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="fr" >}}). L'application d'une fonction de hachage suit les étapes présentées dans cet article. Vous pouvez appliquer une fonction de hachage à toute chaîne de texte brut, à toute [variable]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}) créée par une étape de votre moniteur ou encore à toute [variable prédéfinie]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined-variables" lang="fr" >}}).

Les fonctions de hachage HMAC nécessitent de fournir un **code secret**. Cette donnée statique sera combinée avec le message pour générer une valeur de sortie sécurisée et fiable. Il peut aussi s'agir d'une valeur tirée d'un jeu d'identification de [coffre-fort]({{< ref path="/support/kb/account/vault" lang="fr" >}}).

![Exemple de fonction de hachage](/img/content/scr-msa-hashing-function.min.png)


### Encodage au format base64 pour les données hachées

Certaines méthodes d'authentification nécessitent une valeur hachée, qui doit être encodée au format base64. La fonction `Base64Encode()` mentionnée ci-dessus permet d'encoder les données d'une *chaîne de caractères*. Cependant, cette fonction de hachage produit des données *hexadécimales*. L'encodage de ces données au moyen de la fonction base64 par défaut peut causer des résultats erronés, car il s'agit de types de données différents.

Pour encoder correctement la valeur *hexadécimale* générée par une fonction de hachage, utilisez la fonction `{{@HexToBase64()}}` plutôt que la fonction standard `{{@Base64Encode()}}`.