{
  "hero": {
    "title": "Vue d'ensemble de la surveillance des API"
  },
  "title": "Vue d'ensemble de la surveillance des API",
  "summary": "Qu'est-ce que le monitoring d'API et comment l'utiliser ?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/vue-densemble-de-la-surveillance-des-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Une API (Application Programming Interface ou « interface de programmation d'application ») est un logiciel qui permet à plusieurs applications de communiquer entre elles. Vous pouvez utiliser vos propres API ou des API tierces. Dans les deux cas, les API doivent être surveillées, car elles sont indispensables au bon fonctionnement de votre site web et de vos services.

La fonction de monitoring d'API vérifie si les API que vous utilisez sont disponibles, en bon état de fonctionnement et performantes. Pour en savoir plus, vous pouvez lire l'article [Qu'est-ce que le monitoring d'API ?]([LINK_URL_1]).

Le monitoring d'API d'Uptrends vous permet de surveiller vos API au moyen de différents types de moniteurs. Votre choix dépendra du nombre d'étapes à traiter. En cas d'étape unique, vous utiliserez le moniteur Webservice HTTP ou HTTPS. Pour surveiller une série d'étapes, vous utiliserez le moniteur Multi-step API (aussi parfois désigné sous l'acronyme MSA).

Dans l'application Uptrends, le [portail pour les moniteurs API multi-étapes]([LINK_URL_2]) contient toutes les informations concernant ces moniteurs et leur statut actuel.

## Configurer les moniteurs d'API

La méthode de configuration des différents types de moniteurs est décrite dans ces articles :

- [Configurer un monitoring Webservice]([LINK_URL_3])
- [Configurer un monitoring Webservice (SOAP)]([LINK_URL_4])
- [Configurer un monitoring d'API multi-étapes]([LINK_URL_5])
- [Configurer une surveillance d'API avec Postman]([LINK_URL_6])

## Définir les étapes du moniteur Multi-step API

Lors de la configuration d'un moniteur Multi-step API, vous définissez une étape pour chaque requête HTTP faisant partie du scénario que vous souhaitez surveiller. Chaque étape est abordée en deux parties. Tout d'abord, vous précisez les détails de la requête, en définissant ce qui doit être exécuté et envoyé à votre API. Ensuite, vous précisez la réponse, en définissant ce qui doit être vérifié dans la réponse de notre API.

Pour chaque étape, la requête et la réponse peuvent être enrichies avec des [scripts personnalisés]([LINK_URL_7]) écrits en langage Javascript. Les scripts personnalisés peuvent être utilisés pour configurer l'authentification et pour effectuer des calculs et appliquer une logique personnalisée dans le but de vérifier le bon fonctionnement et le contenu de vos étapes d'API.

Vous pouvez aussi configurer les [fonctions définies par l'utilisateur]([LINK_URL_8]), les [variables]([LINK_URL_9]) et les [métriques personnalisées]([LINK_URL_10]). Cette configuration s'applique à toutes les étapes. Pour en savoir plus sur la configuration des étapes HTTP, lisez les articles dans les sections ci-dessous.

### Requête

Pour configurer la requête étapes HTTP, vous devez préciser une méthode, une URL et le corps de la requête (requête body), puis d'autres détails comme l'authentification. La définition de la requête peut aussi être modifiée au moyen de la personnalisation de script. Pour en savoir plus, référez-vous aux articles ci-dessous.

- [Authentification]([LINK_URL_11])
- [Certificats clients]([LINK_URL_12])
- [Certificats clients d'Uptrends]([LINK_URL_13])
- [Téléchargements de fichiers pour les moniteurs d'API multi-étapes]([LINK_URL_14])
- [Personnalisation des scripts]([LINK_URL_15])

### Réponse

Dans la réponse de l'étape, vous devez définir des assertions. Les assertions sont des vérifications qui permettent de passer à l'étape suivante si la requête produit une réponse. L'assertion vérifie également si la réponse est valide et si elle est reçue dans les délais impartis. Pour chaque étape, vous pouvez définir plusieurs assertions. En plus de définir des assertions dans l'onglet Réponse, vous pouvez complètement personnaliser les vérifications et la logique au moyen de la fonctionnalité de personnalisation de script. Pour en savoir plus sur les assertions, référez-vous à ces articles :

- [Introduction sur les assertions]([LINK_URL_16])
- [Sources des assertions]([LINK_URL_17])
- [Opérateurs de comparaison des assertions]([LINK_URL_18])
- [Exemples d'assertions utilisant XPath]([LINK_URL_19])
- [Variables]([LINK_URL_20])
- [Gestion des redirections]([LINK_URL_21])
- [Personnalisation des scripts]([LINK_URL_22])

### Définitions générales

Certaines de vos définitions peuvent s'appliquer à toutes les étapes, requête et réponse incluses. Cette possibilité s'avère très utile si vous souhaitez réutiliser une certaine valeur ou fonction pour différentes étapes. Pour en savoir plus, consultez les articles suivants :

- [Variables prédéfinies]([LINK_URL_23])
- [Fonctions définies par l'utilisateur]([LINK_URL_24])
- [Métriques personnalisées]([LINK_URL_25])
- [Hachage et encodage]([LINK_URL_26])

### Éditeur de script

Vous pouvez aussi modifier les définitions des étapes du moniteur Multi-step API directement dans *l'éditeur de scripts*. Ce script contient l'intégralité de la définition de votre moniteur Multi-step API, que vous pouvez copier et coller ailleurs. Lisez notre article sur [l'éditeur de script du moniteur Multi-step API]([LINK_URL_27]) pour en savoir plus.

Notez que l'*éditeur de scripts* est à différencier de la fonction de [personnalisation des scripts]([LINK_URL_28]) qui permet d'ajouter une logique personnalisé à vos scripts.

## Crédits

Créer des moniteurs d'API et planifier leur exécution utilisent des crédits d'API. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]([LINK_URL_29]).