{
  "hero": {
    "title": "Authentification (version 4)"
  },
  "title": "Authentification (version 4)",
  "summary": "Comment enregistrer votre compte API et vous authentifier",
  "url": "[URL_BASE_TOPICS]api/authentification-v4",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Chaque méthode API nécessite une authentification via un compte API, que vous devez d'abord créer. Ce compte API est basé sur votre compte Uptrends, mais ce n’est pas le même compte. Séparer ces deux comptes vous permet d'utiliser les identifiants de l’API dans des scripts (par exemple) sans avoir à divulguer vos identifiants de compte Uptrends.

## Gérer les comptes API dans les paramètres des opérateurs

Les comptes API sont gérés directement dans les paramètres de l'opérateur auquel les comptes sont liés. Pour savoir comment ajouter ou supprimer des comptes API, consultez l'article sur la [gestion des comptes API des opérateurs]([LINK_URL_1]). Dans la plupart des cas, cette méthode est la plus simple pour enregistrer un compte API et connaître les comptes associés à chaque opérateur (en effet, plusieurs comptes peuvent être enregistrés pour un même opérateur).

## Enregistrer un compte API en utilisant les appels d'API [ANCHOR_1]

Le compte API peut aussi être créé à l'aide de l'API d'Uptrends. Cette méthode est moins pratique et plus ancienne. Vous pouvez toutefois toujours l'utiliser, et le compte créé apparaîtra aussi dans l'onglet [SHORTCODE_5] Gestion des API [SHORTCODE_6] de l'opérateur.

La méthode **POST** de l'endpoint **/Register** vous permet aussi de créer un nouveau compte API. Dans la description des étapes, nous utiliserons l’environnement Swagger pour accéder directement à l’API. Le compte API que nous allons créer n’expirera pas, vous n’aurez donc besoin de suivre cette procédure qu’une seule fois.

1. Ouvrez la [page Swagger]([LINK_URL_2]) et cliquez sur la méthode [POST /Register]([LINK_URL_3]).

2. Cliquez sur le bouton *Try it out* pour démarrer la création d’un compte API.

3. Cliquez ensuite sur le bouton *Execute*.

4. Votre navigateur vous demande maintenant les identifiants de connexion Uptrends de l'opérateur. Renseignez l’adresse e-mail et le mot de passe que vous utilisez normalement pour accéder à Uptrends et cliquez sur OK.

5. Une fois les informations de connexion de votre compte Uptrends vérifiées, vous recevrez une réponse dont le corps contient des valeurs pour UserName et Password.

[CODE_BLOCK_1]
                      
Il s'agit des informations d’identification de votre nouveau compte API.

6. Cliquez sur le bouton *Download* dans le corps de la réponse pour enregistrer ces informations d’identification, puis conservez-les en lieu sûr. Utilisez-les comme authentification pour tous les autres appels d’API.

[SHORTCODE_1]
**Remarque :** Le compte API n’expirera pas. Cependant, si vous perdez vos identifiants, vous ne pouvez pas les récupérer. Vous devez alors recréer un compte API.
[SHORTCODE_2]

## Utiliser votre compte API [ANCHOR_2]

Maintenant que vous avez un compte API, vous pouvez commencer à l’utiliser. Si vous utilisez Swagger, vous fournissez les informations d’identification dans une boîte de dialogue. Avec des logiciels comme cURL ou Postman, vous les fournissez comme en-têtes et l’encodage se fait automatiquement. Si vous utilisez vos propres scripts, vous devez d’abord encoder vos identifiants ; lisez la section ci-dessous [Authentification de base]([LINK_URL_4]).

[SHORTCODE_3]
**Remarque :** Souvenez-vous que ce compte API est lié à votre compte d'opérateur sur Uptrends, et qu'il possède donc les mêmes privilèges que ce dernier.
[SHORTCODE_4]

### Environnement Swagger

Si vous exécutez des méthodes API dans l’environnement Swagger, une fenêtre contextuelle [SHORTCODE_7]Sign in[SHORTCODE_8] (à api.uptrends.com) apparaît et vous devez entrer votre nom d’utilisateur et votre mot de passe de compte API.

### Authentification de base

Les identifiants du compte doivent toujours être encodés à l’aide du schéma d’authentification de base et fournis à l’API en tant qu’en-tête particulier.

Des logiciels comme Postman, cURL, etc. se chargent d’encoder ces identifiants et de les fournir correctement. Si vous écrivez votre propre script, vous devez fournir cet en-tête à l’appel API :

[INLINE_CODE_1]

L’encodage doit être fait en base64. Pour créer l’en-tête, procédez comme suit :

1. Définissez une chaîne avec la syntaxe [INLINE_CODE_2], en remplaçant [INLINE_CODE_3] et [INLINE_CODE_4] par vos informations d'identification. N'ajoutez aucune espace.

2. La chaîne [INLINE_CODE_5] doit être encodée en base64. La fonction d’encodage existe peut-être dans votre logiciel ou langage de script. Autrement, vous pouvez utiliser un outil tel que [URL_1]

3. Une fois la chaîne encodée, créez et utilisez un en-tête [INLINE_CODE_6], où la valeur [INLINE_CODE_7] correspond à la chaîne encodée en base64 issue de l'étape précédente.
