{
  "hero": {
    "title": "Aperçu des principes de base"
  },
  "title": "Aperçu des principes de base",
  "summary": "Vous découvrez tout juste Uptrends ? Lisez les articles ci-dessous pour connaître les principes de base de l'application et ses principales fonctionnalités.",
  "url": "[URL_BASE_TOPICS]demarrage/apercu-des-principes-de-base",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Uptrends est un outil SaaS (software as a service) de monitoring de l'expérience digitale qui vous fournit des informations détaillées sur la disponibilité et la performance de vos sites et services web, du point de vue de l'utilisateur final. Facile à configurer, Uptrends propose un large éventail de [types de moniteurs]([LINK_URL_1]) pour chaque scénario de surveillance, ainsi qu'une fonctionnalité de monitoring de l'utilisation réelle, le [Real User Monitoring (RUM)]([LINK_URL_2]).

## Monitoring synthétique

Avec sa solution de [monitoring synthétique]([LINK_URL_3]) proactif, Uptrends s'appuie sur son [réseau mondial de checkpoints]([LINK_URL_4]) pour vérifier 24 h/24 et 7 j/7 la disponibilité et la performance de vos sites et processus web, depuis des emplacements en lien avec vos activités. Les types de moniteurs correspondent aux différents cas clients possibles.

{{[HTML_TAG_1]}}

### Surveillance de la disponibilité [ANCHOR_1]

La [surveillance de la disponibilité]([LINK_URL_5]) vous permet de vérifier très régulièrement la disponibilité de vos sites et services web. Des moniteurs tels que le [moniteur HTTPS]([LINK_URL_6]) vérifient la disponibilité et le fonctionnement de votre site. Les vérifications peuvent avoir lieu au moins toutes les minutes, depuis n'importe où dans le monde.

![Journal d'un moniteur de base]([LINK_URL_7])

D'autres types de moniteurs de base sont disponibles, comme le [moniteur DNS]([LINK_URL_8]), qui vérifie votre configuration en envoyant une requête à un serveur DNS, et le moniteur [Certificat SSL]([LINK_URL_9]) qui vérifie la validité de vos certificats SSL et vous avertit en cas d'erreur ou de risque d'expiration.

### Surveillance dans le navigateur [ANCHOR_2]

Contrairement à la surveillance de la disponibilité, la [surveillance dans le navigateur]([LINK_URL_10]) utilise un navigateur réel pour ouvrir vos sites web. Le type de moniteur Full Page Check (FPC) charge complètement la page, exactement comme le feraient vos utilisateurs finaux, et génère un large ensemble de métriques détaillées sur la performance.

Ces métriques incluent un [graphique en cascade]([LINK_URL_11]) (qui offre une vue détaillée contenant des informations techniques et des métriques de performance sur chaque élément contribuant au chargement de la page), mais aussi des indicateurs essentiels tels que les [Core Web Vitals]([LINK_URL_12]) et les [temps de navigation du W3C]([LINK_URL_13]), qui peuvent avoir une incidence sur l'expérience client ou le classement dans les moteurs de recherche.

![Exemple de résultat du moniteur Full Page Check]([LINK_URL_14])

### Surveillance des transactions/applications web [ANCHOR_3]

Le [moniteur de transaction (ou d'application web)]([LINK_URL_15]) charge votre page dans un navigateur réel, puis exécute un script qui interagit avec la page en imitant les actions d'un utilisateur réel. Ce type de moniteur permet de tester les parcours d'utilisation de votre site web, et notamment l'étape de connexion, la recherche de produits, l'ajout au panier d'achats, le traitement du paiement, le remplissage de formulaires, etc.

Généralement, le flux d'utilisateurs, c'est-à-dire les étapes du parcours emprunté par les utilisateurs pour effectuer une action spécifique sur votre site web, mobilise plusieurs serveurs web, bases de données, API ou ressources externes. La surveillance des transactions est la meilleure solution pour vérifier le bon fonctionnement de tous les aspects de vos principaux flux d'utilisateurs. Grâce au plugin d'enregistrement de transaction [Transaction recorder]([LINK_URL_16]) disponible dans Chrome, la configuration est facile et ne nécessite pas d'expérience dans l'utilisation des scripts.

![Éditeur d'étapes de transaction]([LINK_URL_17])

#### Monitoring d'API

Le [moniteur d'API multi-étapes]([LINK_URL_18]) est à votre backend et vos API ce que le monitoring de transaction est à votre frontend et vos parcours utilisateur. Les API permettent la communication entre les applications et forment la colonne vertébrale de l'Internet moderne.

Votre organisation repose certainement sur plusieurs API d'une façon ou d'une autre. Cependant, comme la communication et les interactions entre les API se déroulent dans les coulisses, il est parfois difficile d'identifier la source des problèmes. Avec le monitoring d'API multi-étapes, vous pouvez vérifier directement vos API en recréant des requêtes et en vérifiant dans la réponse que les valeurs sont correctes, complètes et à jour.

## Real User Monitoring

En plus du monitoring synthétique, Uptrends propose une solution de [Real User Monitoring (RUM)]([LINK_URL_19]). Le RUM intègre un script simple dans le code HTML de votre page afin de collecter en temps réel des données sur les performances réelles de vos utilisateurs finaux. En complément des données issues de la surveillance synthétique, le RUM vous fournit des informations sur l'expérience de vos utilisateurs réels, quel que soit leur emplacement. Il vous fournit également des données sur la configuration de leurs appareils, notamment les navigateurs et les systèmes d'exploitation qu'ils utilisent.

![Exemple de données issues du RUM]([LINK_URL_20])

## Alertes

Le monitoring d'Uptrends s'accompagne d'[alertes]([LINK_URL_21]) à la fois polyvalentes et performantes. Grâce aux [définitions d'alerte]([LINK_URL_22]), vous pouvez indiquer quand les alertes doivent être envoyées, et avec quels messages. Des [intégrations]([LINK_URL_23]) prêtes à l'emploi permettent d'envoyer les messages par e-mail, par SMS, par téléphone ou au moyen d'une plateforme externe. Vous pouvez aussi créer une [intégration personnalisée]([LINK_URL_24]) pour relier vos alertes Uptrends à une plateforme externe, y compris si elle ne figure pas sur la page des intégrations.

