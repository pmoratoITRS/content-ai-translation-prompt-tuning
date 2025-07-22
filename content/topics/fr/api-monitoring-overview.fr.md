{
"hero": {
"title": "Vue d'ensemble de la surveillance des API"
},
"title": "Vue d'ensemble de la surveillance des API",
"summary": "Qu'est-ce que le monitoring d'API et comment l'utiliser ?",
"url": "/support/kb/synthetic-monitoring/surveillance-api/vue-densemble-de-la-surveillance-des-api",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/api-monitoring-overview",
"sectionlist": false
}

Une API (Application Programming Interface ou « interface de programmation d'application ») est un logiciel qui permet à plusieurs applications de communiquer entre elles. Vous pouvez utiliser vos propres API ou des API tierces. Dans les deux cas, les API doivent être surveillées, car elles sont indispensables au bon fonctionnement de votre site web et de vos services.

La fonction de monitoring d'API vérifie si les API que vous utilisez sont disponibles, en bon état de fonctionnement et performantes. Pour en savoir plus, vous pouvez lire l'article [Qu'est-ce que le monitoring d'API ?]({{< ref path="/what-is/api-monitoring" lang="fr" >}}).

Le monitoring d'API d'Uptrends vous permet de surveiller vos API au moyen de différents types de moniteurs. Votre choix dépendra du nombre d'étapes à traiter. En cas d'étape unique, vous utiliserez le moniteur Webservice HTTP ou HTTPS. Pour surveiller une série d'étapes, vous utiliserez le moniteur Multi-step API (aussi parfois désigné sous l'acronyme MSA).

Dans l'application Uptrends, le [portail pour les moniteurs API multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="fr" >}}) contient toutes les informations concernant ces moniteurs et leur statut actuel.

## Configurer les moniteurs d'API

La méthode de configuration des différents types de moniteurs est décrite dans ces articles :

- [Configurer un monitoring Webservice]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="fr" >}})
- [Configurer un monitoring Webservice (SOAP)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/setting-up-a-soap-web-service-probe" lang="fr" >}})
- [Configurer un monitoring d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}})
- [Configurer une surveillance d'API avec Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="fr" >}})

## Définir les étapes du moniteur Multi-step API

Lors de la configuration d'un moniteur Multi-step API, vous définissez une étape pour chaque requête HTTP faisant partie du scénario que vous souhaitez surveiller. Chaque étape est abordée en deux parties. Tout d'abord, vous précisez les détails de la requête, en définissant ce qui doit être exécuté et envoyé à votre API. Ensuite, vous précisez la réponse, en définissant ce qui doit être vérifié dans la réponse de notre API.

Pour chaque étape, la requête et la réponse peuvent être enrichies avec des [scripts personnalisés]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}}) écrits en langage Javascript. Les scripts personnalisés peuvent être utilisés pour configurer l'authentification et pour effectuer des calculs et appliquer une logique personnalisée dans le but de vérifier le bon fonctionnement et le contenu de vos étapes d'API.

Vous pouvez aussi configurer les [fonctions définies par l'utilisateur]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="fr" >}}), les [variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}) et les [métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="fr" >}}). Cette configuration s'applique à toutes les étapes. Pour en savoir plus sur la configuration des étapes HTTP, lisez les articles dans les sections ci-dessous.

### Requête

Pour configurer la requête étapes HTTP, vous devez préciser une méthode, une URL et le corps de la requête (requête body), puis d'autres détails comme l'authentification. La définition de la requête peut aussi être modifiée au moyen de la personnalisation de script. Pour en savoir plus, référez-vous aux articles ci-dessous.

- [Authentification]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="fr" >}})
- [Certificats clients]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="fr" >}})
- [Certificats clients d'Uptrends]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="fr" >}})
- [Téléchargements de fichiers pour les moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step#configuring-file-uploads" lang="fr" >}})
- [Personnalisation des scripts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}})

### Réponse

Dans la réponse de l'étape, vous devez définir des assertions. Les assertions sont des vérifications qui permettent de passer à l'étape suivante si la requête produit une réponse. L'assertion vérifie également si la réponse est valide et si elle est reçue dans les délais impartis. Pour chaque étape, vous pouvez définir plusieurs assertions. En plus de définir des assertions dans l'onglet Réponse, vous pouvez complètement personnaliser les vérifications et la logique au moyen de la fonctionnalité de personnalisation de script. Pour en savoir plus sur les assertions, référez-vous à ces articles :

- [Introduction sur les assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="fr" >}})
- [Sources des assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}})
- [Opérateurs de comparaison des assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-comparison-operations" lang="fr" >}})
- [Exemples d'assertions utilisant XPath]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="fr" >}})
- [Variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}})
- [Gestion des redirections]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="fr" >}})
- [Personnalisation des scripts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}})

### Définitions générales

Certaines de vos définitions peuvent s'appliquer à toutes les étapes, requête et réponse incluses. Cette possibilité s'avère très utile si vous souhaitez réutiliser une certaine valeur ou fonction pour différentes étapes. Pour en savoir plus, consultez les articles suivants :

- [Variables prédéfinies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined" lang="fr" >}})
- [Fonctions définies par l'utilisateur]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="fr" >}})
- [Métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="fr" >}})
- [Hachage et encodage]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/hashing-and-encoding" lang="fr" >}})

### Éditeur de script

Vous pouvez aussi modifier les définitions des étapes du moniteur Multi-step API directement dans *l'éditeur de scripts*. Ce script contient l'intégralité de la définition de votre moniteur Multi-step API, que vous pouvez copier et coller ailleurs. Lisez notre article sur [l'éditeur de script du moniteur Multi-step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/msa-script-editor" lang="fr" >}}) pour en savoir plus.

Notez que l'*éditeur de scripts* est à différencier de la fonction de [personnalisation des scripts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}}) qui permet d'ajouter une logique personnalisé à vos scripts.

## Crédits

Créer des moniteurs d'API et planifier leur exécution utilisent des crédits d'API. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}).