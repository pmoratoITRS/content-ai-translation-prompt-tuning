{
"hero": {
"title": "Aperçu des principes de base"
},
"title": "Aperçu des principes de base",
"summary": "Vous découvrez tout juste Uptrends ? Lisez les articles ci-dessous pour connaître les principes de base de l'application et ses principales fonctionnalités.",
"url": "/support/kb/demarrage/apercu-des-principes-de-base",
"translationKey": "https://www.uptrends.com/support/kb/basics/basics-overview",
"sectionlist": false
}

Uptrends est un outil SaaS (software as a service) de monitoring de l'expérience digitale qui vous fournit des informations détaillées sur la disponibilité et la performance de vos sites et services web, du point de vue de l'utilisateur final. Facile à configurer, Uptrends propose un large éventail de [types de moniteurs]({{< ref path="/support/kb/basics/monitor-types" lang="fr" >}}) pour chaque scénario de surveillance, ainsi qu'une fonctionnalité de monitoring de l'utilisation réelle, le [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="fr" >}}).

## Monitoring synthétique

Avec sa solution de [monitoring synthétique]({{< ref path="/products/synthetics/synthetic-monitoring" lang="fr" >}}) proactif, Uptrends s'appuie sur son [réseau mondial de checkpoints]({{< ref path="/checkpoints" lang="fr" >}}) pour vérifier 24 h/24 et 7 j/7 la disponibilité et la performance de vos sites et processus web, depuis des emplacements en lien avec vos activités. Les types de moniteurs correspondent aux différents cas clients possibles.

{{< Support/storylane url="https://app.storylane.io/demo/tqewkqp0c4ly" >}}

### Surveillance de la disponibilité {id="synthetic-monitoring"}

La [surveillance de la disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring" lang="fr" >}}) vous permet de vérifier très régulièrement la disponibilité de vos sites et services web. Des moniteurs tels que le [moniteur HTTPS]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https" lang="fr" >}}) vérifient la disponibilité et le fonctionnement de votre site. Les vérifications peuvent avoir lieu au moins toutes les minutes, depuis n'importe où dans le monde.

![Journal d'un moniteur de base](/img/content/scr-basics-uptimelog_020224.min.png)

D'autres types de moniteurs de base sont disponibles, comme le [moniteur DNS]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="fr" >}}), qui vérifie votre configuration en envoyant une requête à un serveur DNS, et le moniteur [Certificat SSL]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="fr" >}}) qui vérifie la validité de vos certificats SSL et vous avertit en cas d'erreur ou de risque d'expiration.

### Surveillance dans le navigateur {id="browser-monitoring"}

Contrairement à la surveillance de la disponibilité, la [surveillance dans le navigateur]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) utilise un navigateur réel pour ouvrir vos sites web. Le type de moniteur Full Page Check (FPC) charge complètement la page, exactement comme le feraient vos utilisateurs finaux, et génère un large ensemble de métriques détaillées sur la performance.

Ces métriques incluent un [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) (qui offre une vue détaillée contenant des informations techniques et des métriques de performance sur chaque élément contribuant au chargement de la page), mais aussi des indicateurs essentiels tels que les [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) et les [temps de navigation du W3C]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}), qui peuvent avoir une incidence sur l'expérience client ou le classement dans les moteurs de recherche.

![Exemple de résultat du moniteur Full Page Check](/img/content/scr-fpc-result-basics.min.png)

### Surveillance des transactions/applications web {id="transaction-monitoring"}

Le [moniteur de transaction (ou d'application web)]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="fr" >}}) charge votre page dans un navigateur réel, puis exécute un script qui interagit avec la page en imitant les actions d'un utilisateur réel. Ce type de moniteur permet de tester les parcours d'utilisation de votre site web, et notamment l'étape de connexion, la recherche de produits, l'ajout au panier d'achats, le traitement du paiement, le remplissage de formulaires, etc.

Généralement, le flux d'utilisateurs, c'est-à-dire les étapes du parcours emprunté par les utilisateurs pour effectuer une action spécifique sur votre site web, mobilise plusieurs serveurs web, bases de données, API ou ressources externes. La surveillance des transactions est la meilleure solution pour vérifier le bon fonctionnement de tous les aspects de vos principaux flux d'utilisateurs. Grâce au plugin d'enregistrement de transaction [Transaction recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}) disponible dans Chrome, la configuration est facile et ne nécessite pas d'expérience dans l'utilisation des scripts.

![Éditeur d'étapes de transaction](/img/content/scr-transaction-steps-basics_020224.min.png)

#### Monitoring d'API

Le [moniteur d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring" lang="fr" >}}) est à votre backend et vos API ce que le monitoring de transaction est à votre frontend et vos parcours utilisateur. Les API permettent la communication entre les applications et forment la colonne vertébrale de l'Internet moderne.

Votre organisation repose certainement sur plusieurs API d'une façon ou d'une autre. Cependant, comme la communication et les interactions entre les API se déroulent dans les coulisses, il est parfois difficile d'identifier la source des problèmes. Avec le monitoring d'API multi-étapes, vous pouvez vérifier directement vos API en recréant des requêtes et en vérifiant dans la réponse que les valeurs sont correctes, complètes et à jour.

## Real User Monitoring

En plus du monitoring synthétique, Uptrends propose une solution de [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="fr" >}}). Le RUM intègre un script simple dans le code HTML de votre page afin de collecter en temps réel des données sur les performances réelles de vos utilisateurs finaux. En complément des données issues de la surveillance synthétique, le RUM vous fournit des informations sur l'expérience de vos utilisateurs réels, quel que soit leur emplacement. Il vous fournit également des données sur la configuration de leurs appareils, notamment les navigateurs et les systèmes d'exploitation qu'ils utilisent.

![Exemple de données issues du RUM](/img/content/scr-rum-map-basics_020224.min.png)

## Alertes

Le monitoring d'Uptrends s'accompagne d'[alertes]({{< ref path="/support/kb/alerting" lang="fr" >}}) à la fois polyvalentes et performantes. Grâce aux [définitions d'alerte]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="fr" >}}), vous pouvez indiquer quand les alertes doivent être envoyées, et avec quels messages. Des [intégrations]({{< ref path="/support/kb/alerting/integrations/what-are-integrations" lang="fr" >}}) prêtes à l'emploi permettent d'envoyer les messages par e-mail, par SMS, par téléphone ou au moyen d'une plateforme externe. Vous pouvez aussi créer une [intégration personnalisée]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="fr" >}}) pour relier vos alertes Uptrends à une plateforme externe, y compris si elle ne figure pas sur la page des intégrations.

