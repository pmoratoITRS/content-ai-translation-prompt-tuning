{
  "hero": {
    "title": "Configuration d'un moniteur API multi-étapes"
  },
  "title": "Configuration d'un moniteur API multi-étapes",
  "summary": "Instructions pas-à-pas pour configurer un moniteur API multi-étapes",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/multi-step",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Pour surveiller efficacement votre API, vous devez généralement créer une séquence de requêtes HTTP, dans laquelle chaque requête récupère les données d'une requête précédente pour effectuer la suite de tâches suivante. Le **moniteur d'API multi-étapes** vous permet de configurer de multiples requêtes HTTP, de définir des [variables]([LINK_URL_1]), de créer des [fonctions définies par l'utilisateur]([LINK_URL_2]), de configurer des [scripts personnalisés]([LINK_URL_3]), et bien plus encore.

Voici quelques exemples de situations dans lesquelles vous devez exécuter une séquence de requêtes HTTP :

- Votre API repose sur un accès authentifié : le client API doit vérifier ses informations de connexion avant d'accéder aux méthodes HTTP (par exemple, en utilisant l'authentification OAuth).
- Vous voulez tester dans votre API un scénario de fonctionnement qui comprend plusieurs étapes généralement exécutées dans un certain ordre par vos utilisateurs finaux.
- Votre requête HTTP renvoie une redirection vers une URL différente, et vous voulez inspecter le comportement de cette réponse avant d'effectuer la redirection.

## Fonctionnalités du moniteur d'API multi-étapes

Le **moniteur d'API multi-étapes** vous donne le plein contrôle sur le contenu de vos requêtes HTTP. Ses fonctionnalités sont les suivantes :

- Configurer la méthode HTTP, l'URL, l'en-tête et le corps pour chaque requête
- [Ajouter une authentification (Basic/NTLM/Digest/OAuth)]([LINK_URL_4]) ou [inclure les certificats clients]([LINK_URL_5]) pour accéder aux API protégées.
- [Définir des assertions (vérifications) pour chaque réponse]([LINK_URL_6]) pour vérifier le code de statut HTTP, le contenu (d'après le texte brut ou un contenu JSON ou XML), la durée de la requête et d'autres données.
- Extraire du contenu du corps de la réponse, des en-têtes de réponse, des cookies et [le stocker dans des variables]([LINK_URL_7]). Ces variables peuvent être utilisées ultérieurement pour créer d'autres URL, en-têtes de requêtes, etc.
- Utiliser des définitions générales comme les [variables prédéfinies]([LINK_URL_8]), les [fonctions définies par l'utilisateur]([LINK_URL_9]), les [métriques d'API personnalisées]([LINK_URL_10]) et [le hachage et l'encodage]([LINK_URL_11]).

Grâce à ces fonctions, vous pouvez vous assurer que votre API se comporte correctement et s'exécute dans les limites que vous avez définies. Les instructions détaillées vous permettent de configurer des scénarios très puissants sans ajouter de complexité. Si vous savez comment votre API doit se comporter, vous n'avez pas besoin de compétences en programmation pour démarrer la surveillance d'API.

## Création d'un moniteur API multi-étapes

Pour ajouter un moniteur API multi-étapes :

1. Dans le menu, cliquez sur [SHORTCODE_7] API > Gérer les moniteurs API [SHORTCODE_8], puis sur le bouton [SHORTCODE_9][SHORTCODE_10].
2. Dans la fenêtre contextuelle *Sélectionnez un type de moniteur*, cliquez sur *Multi-step API*, puis sur le bouton [SHORTCODE_11] Choisir [SHORTCODE_12].
3. Une fois le moniteur créé, donnez-lui un *nom*.
4. Choisissez l'*intervalle de vérification*. [L'intervalle de vérification]([LINK_URL_12]) correspond au temps écoulé entre la fin d'une vérification et le début de la suivante.
5. Ouvrez l'onglet [SHORTCODE_13]Étapes[SHORTCODE_14] pour saisir les détails de chaque étape.

Votre nouveau moniteur contient déjà une étape (vide). Vous pouvez effectuer toutes les actions suivantes :
- Cliquez sur [SHORTCODE_15] Ajouter une étape de requête [SHORTCODE_16] pour ajouter d'autres étapes.
- Cliquez sur l'icône **>** à côté de chaque étape pour afficher et modifier les détails de l'étape.
- Cliquez sur l'icône **Copier** pour dupliquer une étape existante.
- Cliquez sur l'icône **X** pour supprimer une étape.
- Utilisez les boutons *Déplacer l'étape vers le haut* et *Déplacer l'étape vers le bas* pour déplacer la position des étapes.

![Exemple d'étapes du moniteur MSA]([LINK_URL_13])

## Configuration d'une étape de requête

Dans l'éditeur visuel d'étapes, repérer l'onglet [SHORTCODE_17] Requête [SHORTCODE_18]. Dans le cadre du monitoring d'API multi-étapes, une étape désigne un appel aller-retour à l'API (par exemple, une requête et une réponse). Pour chaque étape, vous pouvez définir votre requête et indiquer à Uptrends comment gérer la réponse. Chaque scénario Multi-step API commence par une étape vide.

### Requête

![Détails de l'onglet Requête]([LINK_URL_14])

L'onglet **Requête** contient toutes les données nécessaires à cette étape pour effectuer la requête HTTP. Au minimum :

1. Choisissez la méthode HTTP appropriée, soit **GET**, **POST**, **PUT**, **PATCH**, **DELETE**, **HEAD** ou **OPTIONS**. Si vous avez besoin d'une méthode différente, [contactez-nous]([LINK_URL_15]).
2. Renseignez l'URL pour la requête. Utilisez une URL complète, comprenant le protocole ("[URL_1] ou "[URL_2]), le nom de domaine et le chemin d'accès à votre API, ainsi que tout paramètre de chaîne de requête que vous souhaitez inclure.

#### Requête body

Lorsque vous configurez une demande POST, PUT, PATCH, HEAD, OPTIONS ou DELETE, le champ **Requête body** (Corps de la requête) vous permet d'envoyer des données spécifiques (la charge utile) dans la définition de requête. Par exemple, cela permet d'envoyer un nom d'utilisateur et un mot de passe spécifiques pour créer un nouveau compte utilisateur.

Voici les formats de données d'en-tête de requête à votre disposition :

- Texte brut : vous permet d'envoyer du texte brut sans mise en forme.
- Télécharger un fichier (en tant que données de formulaire) : vous permet d'envoyer un fichier (comme des images et des documents provenant du [coffre-fort]([LINK_URL_16])) sous format form-data.
- Télécharger un fichier (en tant que données de formulaire) : vous permet d'envoyer un fichier (comme des images et des documents provenant du [coffre-fort]([LINK_URL_17])) sous format de données binaires brutes.
- Multi-part form : vous permet d'envoyer en même temps plusieurs types de contenu dans différents formats (comme des entrées sous forme de texte brut ou des fichiers provenant du [coffre-fort]([LINK_URL_18])).

La plupart du temps et selon le format de données choisi, la valeur correcte de l'en-tête de requête [INLINE_CODE_1] est définie automatiquement (par exemple, sous la forme [INLINE_CODE_2]) pour que le serveur puisse identifier, lire et traiter vos données correctement. Vous pouvez aussi préciser l'en-tête de requête [INLINE_CODE_3], dont il est question ci-dessous.

#### En-têtes de requête [ANCHOR_1]

Une requête HTTP contient généralement des en-têtes de requête (ou request headers) pour spécifier le format des données envoyées ou pour décrire plus en détail le type de réponse attendu. Lorsque vous configurez une étape de requête, vous remarquerez que certains en-têtes sont ajoutés automatiquement. Ces en-têtes sont constitués d'un ensemble d'en-têtes par défaut, en fonction du type de requête que vous effectuez (les demandes GET auront un ensemble d'en-têtes différent de celui des demandes POST, par exemple). Pour remplacer un en-tête par défaut, il suffit d'ajouter un nouvel en-tête et un nom portant exactement le même nom que l'en-tête existant, mais avec une valeur différente.

[SHORTCODE_1] **Remarque :**Dans un objectif d'optimisation, **Connection: Keep-Alive** a été retiré de la liste des en-têtes de requête par défaut. L'en-tête de requête correspond déjà au comportement par défaut pour le protocole HTTP/1.1 et n'est plus en charge pour les protocoles HTTP/2 et HTTP/3. [SHORTCODE_2]

Vous pouvez aussi ajouter de nouveaux en-têtes en suivant ces étapes :

1. Cliquez sur le bouton [SHORTCODE_19]Ajouter un request header[SHORTCODE_20] pour ajouter une clé et une valeur d'en-tête de requête.
2. Saisissez Content-Type dans le champ Nom.
3. La valeur d'en-tête appropriée dépend des données que vous envoyez. Les types de contenu les plus courants sont [INLINE_CODE_4] pour les données JSON, [INLINE_CODE_5] pour les données XML, et [INLINE_CODE_6] pour les données de formulaires web.

De même, si votre API exige une authentification, ajoutez un en-tête [INLINE_CODE_7] avec les données appropriées dans le champ Valeur.

![Exemples d'en-têtes de requête]([LINK_URL_19])

L'image ci-dessus montre un exemple d'étape de requête. Vous remarquerez ce qui suit :

- Il s'agit d'une requête POST vers [INLINE_CODE_8].
- Les en-têtes par défaut définis pour cette requête sont les suivants :
   - [INLINE_CODE_9]
   - [INLINE_CODE_10]
- Les valeurs de l'en-tête [INLINE_CODE_11] seront déterminées lors de l'envoi de la requête.
- Des en-têtes manuels [INLINE_CODE_12] et [INLINE_CODE_13] ont été ajoutés pour spécifier le format des données et fournir les informations d'identification nécessaires.
- L'en-tête par défaut [INLINE_CODE_14] a été remplacé.
- Le corps de la requête contient du contenu [INLINE_CODE_15], qui fait référence à certaines [variables]([LINK_URL_20]).

#### Authentification

De nombreuses API sont protégées et ne sont accessibles qu'en fournissant des informations de connexion. Si votre API utilise l'authentification au niveau du protocole HTTP, choisissez votre type d'authentification (Basic, NTLM ou Digest) et renseignez le nom d'utilisateur et le mot de passe correspondants. Vous pouvez également configurer l'authentification basée sur OAuth en utilisant des étapes distinctes. [Cliquez ici pour en savoir plus sur la configuration de l'authentification intégrée ou personnalisée]([LINK_URL_21]).

#### Utilisation d'un jeu d'identification de coffre-fort

Il est possible d'utiliser le [jeu d'identification de coffre-fort]([LINK_URL_22]) à tout moment dans le corps de la requête, dans les en-têtes de requête ou en tant que valeur pour votre nom d'utilisateur/mot de passe dans la partie *Authentification*. Pour faire référence à un élément de coffre-fort, utilisez l'une des deux syntaxes suivantes : [INLINE_CODE_16] ou [INLINE_CODE_17], selon la valeur requise. Pour trouver le [INLINE_CODE_18], accédez à l'élément du coffre-fort avec vos informations d'identification, puis copiez la dernière partie de l'URL dans la barre d'URL de votre navigateur.

![Exemples de références aux éléments du coffre-fort]([LINK_URL_23])

#### Configuration des versions TLS

Transport Layer Security (TLS) est un protocole de sécurité qui authentifie, chiffre et protège les connexions entre les sites web et les serveurs. En cochant la case *Autoriser uniquement certaines versions de TLS*, vous pouvez préciser les versions TLS à appliquer lors de la négociation TLS pour la connexion HTTPS dans les moniteurs d'API multi-étapes. Vous pouvez aussi décocher la case si aucune restriction n'est nécessaire.

Tous les [checkpoints d'Uptrends]([LINK_URL_24]) prennent en charge les protocoles TLS 1.1 et TLS 1.2. Si vous cochez l'option TLS 1.3, cela limite votre sélection aux checkpoints prenant en charge le protocole TLS 1.3. Ce choix est déconseillé tant que le protocole TLS 1.1 est pris en charge.

![Case à cocher Version(s) TLS dans les moniteurs d'API multi-étapes]([LINK_URL_25])

#### Configuration de la version HTTP

L'option **Version HTTP** vous permet de contrôler la version HTTP utilisée par les serveurs de checkpoint lors de l'exécution de requêtes. Utilisez-la pour vous assurer que les serveurs communiquent avec l'API d'une façon qui assure la compatibilité, la performance et la sécurité.

![Version HTTP]([LINK_URL_26])

Par défaut, l'option **Version HTTP** est décochée, ce qui signifie que le serveur utilisera automatiquement la plus récente version HTTP disponible, et au moins la version HTTP/1.1.

Actuellement, la version HTTP/3 est disponible pour certains emplacements de checkpoints, dont la liste sera élargie prochainement.

[SHORTCODE_3] **Remarque :** La version HTTP vous permet de sélectionner uniquement une version, tandis que **la ou les versions TLS** prennent plusieurs versions en charge.
[SHORTCODE_4]

### Importation de requêtes cURL [ANCHOR_2]

Vous pouvez aussi importer directement des requêtes cURL pour créer vos étapes sans devoir les recréer manuellement. Voici comment faire :

1. Dans **l'éditeur visuel d'étapes** (accessible depuis l'onglet [SHORTCODE_21]Étapes[SHORTCODE_22] dans les paramètres du moniteur) du moniteur d'API multi-étapes dans lequel vous souhaitez importer une étape basée sur une commande cURL, cliquez sur le bouton [SHORTCODE_23]Importation cURL[SHORTCODE_24] pour ouvrir l'assistant d'importation.
2. Cliquez sur le bouton [SHORTCODE_25]Suivant[SHORTCODE_26].
3. Copiez la ou les instructions de votre ligne de commande cURL. Par exemple, imaginons que vous vouliez créer une étape basée sur cette instruction cURL :

[CODE_BLOCK_1]

Cette requête permet de créer une réservation sur notre site fictif de réservation de séjours galactiques [GalacticResorts.com]([LINK_URL_27]).

Vous pouvez ajouter plusieurs fonctions d'un coup, en copiant plusieurs commandes cURL.

4. Si nécessaire, précisez le format de la commande. Dans la plupart des cas, l'option Détection automatique devrait suffire.
5. Cliquez sur le bouton [SHORTCODE_27]Suivant[SHORTCODE_28].
6. Dans la dernière étape de l'assistant, cliquez sur le bouton [SHORTCODE_29]Générer des étapes[SHORTCODE_30].

Le résultat de la commande cURL présentée dans cet exemple serait le suivant :

![Résultat de l'importation cURL]([LINK_URL_28])

Le moniteur Multi-step API ne prend pas en charge toutes les options incluses dans la ligne de commande cURL. Les options non prises en charge sont automatiquement ignorées. Assurez-vous donc d'essayer l'étape pour vérifier que tout fonctionne comme attendu.

### Réponse

L'onglet Réponse contient toutes les options permettant d'effectuer des vérifications sur les données de réponse (à l'aide d'assertions) et de traiter ces données en préparation de l'étape suivante (à l'aide de variables).

![Onglet Réponse]([LINK_URL_29])

#### Assertions

Définir vos étapes et les configurer avec les données correctes est la base d'une bonne configuration. Cependant, il est également important de regarder les résultats de chaque étape. Appeler une série d'URL ne sert à rien si elles ne renvoient pas les bons résultats. Les assertions vous aident à réaliser ces vérifications.

Les assertions sont des vérifications que vous pouvez exécuter pour vérifier que la réponse à une étape particulière se comporte comme prévu, par exemple, en vérifiant son contenu ou en vérifiant qu'elle a été récupérée dans un certain laps de temps. Comme pour les variables, vous spécifiez la source pour la vérification, par exemple, une propriété JSON du corps de réponse JSON, une requête XPath sur le corps de réponse XML, ou même simplement le code d'état de la réponse, sa durée ou la longueur du contenu.

**Pour d'autres exemples d'assertions**, lisez notre [article complet sur la définition des assertions]([LINK_URL_30]).

#### Variables

Lorsque vous configurez des scénarios multi-étapes, il est probable qu'au moins une de ces étapes dépendra de certaines données récupérées lors d'une étape précédente. En capturant cette donnée, en la stockant temporairement et en la transmettant aux étapes suivantes, vous créez une progression naturelle d'étapes interconnectées, sans avoir besoin d'écrire de code.

C'est justement pour cela que nous avons prévu les variables. Chaque étape peut créer de nouvelles variables et accéder aux variables créées par d'autres étapes, ce qui permet de réutiliser les données précédemment capturées dans le scénario.

Vous pouvez définir l'origine d'une variable, qui sera probablement une valeur particulière issue de données JSON ou XML, mais la capture d'en-têtes de réponse ou même de données à partir d'une redirection est également possible. Une fois qu'une variable a été définie, vous pouvez l'utiliser n'importe où dans votre configuration multi-étapes simplement en utilisant son nom : [SHORTCODE_37]{{my-variable}}[SHORTCODE_38].

**Pour plus d'exemples de variables**, lisez l'article sur [la définition et l'utilisation de variables]([LINK_URL_31]).

#### Nombre maximum de tentatives [ANCHOR_3]

Dans certains cas, il se peut que votre API ait besoin d'un certain temps pour traiter une requête entrante avant de pouvoir confirmer la réussite de l'opération. Par exemple, imaginons que vous téléchargiez un fichier en vue de son traitement dans votre API. Pendant son traitement, l'API répond aux requêtes concernant le statut avec [INLINE_CODE_19] dans un corps JSON. Une fois le traitement terminé, l'API répond avec [INLINE_CODE_20]. Dans ces cas, vous pouvez configurer le moniteur pour qu'il continue à interroger l'API jusqu'à ce qu'elle confirme une réussite, en utilisant le paramètre **Nombre maximal de tentatives**.

Cette fonction configurera le moniteur pour qu'il réessaie l'étape si une ou plusieurs des assertions suivantes de l'étape rencontrent un échec : [SHORTCODE_39]Response body as JSON[SHORTCODE_40] [SHORTCODE_41]result[SHORTCODE_42] [SHORTCODE_43]Is equal to[SHORTCODE_44] [SHORTCODE_45]success[SHORTCODE_46] pour l'exemple mentionné ci-dessus. Vous pouvez définir le nombre de tentatives que le moniteur doit effectuer, à hauteur d'un maximum de 50 tentatives. Le nombre minimum de tentatives est fixé à deux, et la requête initiale compte comme première tentative.

En plus du nombre de tentatives, vous pouvez définir le temps d'attente entre ces tentatives. Ce temps d'attente doit être compris entre 500 et 3 000 ms. La valeur par défaut est fixée à 1 000 ms.

Pour chaque étape, vous pouvez configurer un nombre maximum de tentatives ainsi qu'un temps d'attente minimum entre chacune.

Le moniteur continuera à réessayer l'étape jusqu'à ce que le nombre maximal de tentatives soit atteint ou que toutes les assertions réussissent. À ce moment-là, le moniteur continue normalement, en exécutant le reste des étapes dans l'ordre. Si le nombre maximal de tentatives est atteint et qu'au moins une assertion a échoué, le moniteur signale une erreur dans le journal du moniteur.

Le coût du moniteur MSA reste le même, quel que soit le nombre de tentatives.

## Configuration des téléchargements de fichiers

Les moniteurs d'API multi-étapes vous permettent de télécharger des fichiers depuis [votre coffre-fort]([LINK_URL_32]) dans le cadre de l'une de vos étapes de requête. Toute étape HTTP configurée dans le moniteur d'API multi-étapes qui contient un corps de requête peut correspondre à un téléchargement de fichier de données de formulaire (form-data) ou binaires, ou à une simple requête de texte brut. Les fichiers seront envoyés comme du contenu [INLINE_CODE_21] ou binaire. Pour ajouter un fichier form-data, procédez comme suit :

1. [Téléchargez le fichier en question]([LINK_URL_33]) dans votre coffre-fort. La taille maximale du fichier est 2 Mo.
2. Dans les paramètres de votre moniteur API multi-étapes, ajoutez une étape de requête ou utilisez une étape existante pour exécuter le téléchargement du fichier.
3. Dans l'onglet **Requête** de l'étape qui doit exécuter le téléchargement du fichier, définissez la méthode de requête sur *POST*, *PUT* ou *PATCH* (en fonction de votre cas) et renseignez l'URL de la requête.
4. Dans **Requête body**, sélectionnez l'option *Télécharger un fichier (en tant que données de formulaire)*.
5. Cliquez sur le bouton [SHORTCODE_31]Ajouter un fichier à partir du coffre-fort[SHORTCODE_32] qui s'affiche.
6. Choisissez un fichier dans la liste de téléchargement de fichiers du coffre-fort, puis cliquez sur le bouton [SHORTCODE_33]Sélectionner[SHORTCODE_34].
   ![Sélection de fichiers à télécharger]([LINK_URL_34])
7. Il n'est pas nécessaire d'ajouter des en-têtes de requête spécifiques. Nous rajouterons automatiquement un en-tête de requête pour [INLINE_CODE_22] et nous définirons [INLINE_CODE_23] avec la valeur correcte.
   ![Exemples d'en-têtes pour le téléchargement de fichiers]([LINK_URL_35])

Si vous souhaitez télécharger un fichier sans qu'Uptrends ajoute de métadonnées [INLINE_CODE_24] au corps de requête, sélectionnez l'option *Télécharger un fichier (en tant que binaire)* dans la partie **Requête body** à l'étape 4 ci-dessus. Nous produirons automatiquement les en-têtes répertoriés dans **Request headers**, sans ajouter ces métadonnées. Cela vous permettra de tester votre API même si celle-ci nécessite un fichier de données binaires brutes.

Il faut savoir que votre API peut s'attendre à une valeur spécifique pour le nom de fichier. La requête inclura un en-tête construit automatiquement **Content-Disposition**, avec des métadonnées. La valeur de cet en-tête contient un paramètre *name*. Par défaut, nous utiliserons le nom de fichier que vous avez spécifié dans le coffre-fort. Assurez-vous que le nom de fichier que vous spécifiez lors de l'ajout du fichier au coffre-fort correspond à la valeur attendue par votre API. Par exemple, si votre API s'attend à ce que le fichier téléchargé s'appelle "image", assurez-vous de spécifier "image" (sans extension de fichier) comme nom de fichier dans l'élément de coffre-fort approprié.

## Configuration d'une étape d'attente

Lorsque vous avez une séquence d'étapes de requête dans votre moniteur, chaque étape est exécutée dès que l'étape précédente est terminée, sans aucun délai. Cependant, cette exécution immédiate peut être un peu trop rapide pour certains scénarios.

Imaginons qu'une méthode API demande la génération d'un fichier de rapport. L'API lance un processus de backend pour générer le fichier et demande à l'appelant d'envoyer une deuxième requête afin de télécharger le nouveau fichier. La génération du fichier pouvant prendre une seconde ou deux, l'appelant doit attendre quelques secondes avant d'envoyer la deuxième requête. Si la deuxième requête est envoyée trop tôt, elle échouera car le fichier généré n'est pas encore prêt.

Pour ce scénario, il est important d'attendre avant que la deuxième requête ne soit exécutée. Pour ce faire, vous pouvez insérer une étape d'attente distincte. Ce type d'étape vous permet de spécifier le nombre de millisecondes à attendre. Par exemple, pour attendre 3 secondes, spécifiez 3 000 millisecondes comme temps d'attente. Ce temps d'attente sera inclus dans le temps total pour ce moniteur.

Pour ajouter une étape d'attente, cliquez simplement sur le bouton [SHORTCODE_35] Ajouter une étape d'attente [SHORTCODE_36] et spécifiez le nombre de millisecondes à appliquer. Si nécessaire, vous pouvez déplacer l'étape d'attente au bon endroit de votre scénario à l'aide des boutons Déplacer l'étape vers le haut/bas.

Le temps d'attente pour une étape d'attente est limité à 60 secondes : une étape d'attente n'est pas destinée à surveiller une tâche de longue durée prenant plusieurs minutes ou heures. Si le moniteur dépasse le temps total maximal d'exécution, la vérification s'arrête et un échec est signalé.

Ajouter une étape d'attente à votre moniteur ne vous coûte rien. Le coût d'un moniteur API multi-étapes est uniquement basé sur le nombre d'étapes de requêtes.

[SHORTCODE_5] **Remarque** : La durée d'exécution de toutes les étapes de votre moniteur ne doit pas dépasser 4 minutes au total. Si le moniteur prend plus de 4 minutes pour l'exécution du début à la fin, le résultat de la vérification du moniteur sera une erreur. Dans de tels cas, il faut envisager de répartir vos requêtes sur plusieurs moniteurs, si possible. [SHORTCODE_6]

## Résultats, erreurs et alertes du monitoring multi-étapes

Les moniteurs API multi-étapes se comportent de la même manière que tous les autres moniteurs. Chaque vérification apparaît dans le journal du moniteur et fournit des informations détaillées pour chaque étape. Pour chaque étape, cette information comprend les éléments suivants :

- **la durée totale** de l'étape (en millisecondes) ;
- **l'URL** qui a été interrogée au cours de cette étape ;
- **le code d'état HTTP** qui a été renvoyé ;
- le résultat pour chaque **assertion** (réussite ou échec) ;
- **les en-têtes et le contenu des requêtes** que nous avons envoyés ;
- **les en-têtes et le contenu de la réponse** que nous avons reçus.

Si un problème se produit au cours de l'une des étapes ou si l'une des assertions que vous avez définies ne réussit pas, le moniteur échouera et signalera une erreur. Comme toujours, ces erreurs peuvent générer des alertes en fonction de vos définitions d'alertes.