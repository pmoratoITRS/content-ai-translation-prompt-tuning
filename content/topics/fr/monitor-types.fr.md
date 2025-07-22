{
"hero": {
"title": "Types de moniteurs"
},
"title": "Types de moniteurs",
"summary": "Cet article vous fournit une vue d'ensemble des types de moniteurs d'Uptrends, des moniteurs de disponibilité aux moniteurs de transactions.",
"url": "/support/kb/basics/types-moniteur",
"translationKey": "https://www.uptrends.com/support/kb/basics/monitor-types"
}

Uptrends propose une large gamme de moniteurs afin de répondre à vos différents besoins de surveillance. Chaque moniteur synthétique utilise des [crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}) pour calculer le prix des différents services de monitoring.

Pour vous aider à vous lancer, cet article vous explique comment chaque type de moniteur vérifie les performances de votre site web.

{{< callout >}} **Remarque :** Vous pouvez associer plusieurs types de moniteurs au [Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="fr" >}}) pour mesurer les performances de votre site web d'après l'expérience que vos utilisateurs vivent depuis leur propre réseau, leurs navigateurs réels et leurs diverses activités. {{< /callout >}}

## Moniteurs de disponibilité (vérifications de base)

Les moniteurs de disponibilité effectuent des vérifications de base sur vos sites web. Ils vérifient la disponibilité de chaque page, au moyen de la réception d'un code de statut de réponse 200. Ce type de moniteur contrôle uniquement la réponse initiale du site web et ne passe pas en revue les éléments de la page ou d'autres composantes.

Les vérifications du moniteur de disponibilité peuvent se produire toutes les minutes, ce qui vous fournit des informations plus précises sur la disponibilité de la page qu'une vérification effectuée dans le navigateur réel ou par un moniteur Full Page Check.

### Types de moniteurs de disponibilité

Voici les différents types de moniteurs de disponibilité :

- Vérifications de pages web avec les moniteurs **HTTP** et **HTTPS** (à privilégier)
- Contrôles avancés avec les moniteurs **DNS**, **Certificat SSL**, **SFTP** et **FTP**
- Serveurs mails avec les moniteurs **SMTP**, **POP3** et **IMAP**
- Serveurs de bases de données avec les moniteurs **Microsoft SQL Server** et **MySQL**
- Vérifications du réseau avec les moniteurs **Ping** et **Connect**

{{< callout >}}**Remarque :** Le moniteur **HTTP** n'est plus disponible pour les nouveaux utilisateurs. Uptrends a élargi les fonctionnalités des moniteurs **HTTPS** pour prendre en charge et vérifier la disponibilité des sites web HTTP. {{< /callout >}}

Pour en savoir plus sur les différents types de moniteurs de disponibilité, lisez l'article intitulé [Moniteurs de disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}).

## Moniteurs de navigateur (Full Page Check)

Les moniteurs de navigateur, aussi appelés Full Page Check (FPC) ou Real Browser, effectuent une vérification complète des performances de chargement des pages de votre site web, élément après élément. Ce type de moniteur ouvre un navigateur réel pour reproduire ce que les utilisateurs voient lorsqu'ils consultent votre site web.

Il examine comment votre site web se charge du début à la fin, en tenant compte du comportement de chaque élément de la page (par exemple, les scripts, les fichiers CSS, les images et les contenus tiers). De même, les moniteurs de navigateurs fournissent des informations sur les indicateurs [Core Web Vitals]({{< ref path="" lang="fr" >}}) et les [temps de navigation du W3C]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}) de votre site web. Les métriques sont présentées sous forme de [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}).

Les vérifications de ce moniteur peuvent se produire toutes les cinq minutes, ce qui vous donne une idée de la disponibilité de votre site web. Ce moniteur est toutefois moins précis qu'un moniteur de disponibilité. Pour en savoir plus sur la différence entre les vérifications de base et les vérifications dans le navigateur, lisez l'article de notre base de connaissances intitulé [Vérification de base des pages comparé aux Real Browser Checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="fr" >}}). Pour en savoir plus, vous pouvez aussi lire notre article sur la [surveillance par navigateur]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="fr" >}}).

## Moniteurs d'API

Les moniteurs d'API sont des outils puissants pour effectuer des vérifications au moyen d'un simple appel d'API en une étape ou d'appels d'API plus complexes en plusieurs étapes. Ce moniteur propose une solution sans code (via une interface) et une fonction de [personnalisation des scripts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}}) pour tester facilement les requêtes et les réponses HTTP selon vos besoins de surveillance.

Vous pouvez aussi ajouter une logique personnalisée ou des [fonctions définies par l'utilisateur]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="fr" >}}), définir des [variables personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}), utiliser des [assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="fr" >}}) et d'autres fonctionnalités permises par les API.

### Types de moniteurs d'API

Voici les différents types de moniteurs d'API :

- [Moniteur d'API multi-étapes (MSA)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) : il s'agit du principal type de moniteur d'API. Ce type de moniteur propose des fonctionnalités plus avancées et puissantes que les moniteurs Webservice HTTP et HTTPS.
- [Moniteur API Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="fr" >}}) : ce moniteur vous permet d'optimiser les vérifications d'API en exécutant une collection d'un espace de travail Postman sur le réseau de checkpoints d'Uprends.
- [Moniteurs Webservice HTTP et HTTPS]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/monitoring-web-services" lang="fr" >}}) : ce type de moniteur HTTP classique effectue seulement des vérifications de base concernant la disponibilité de l'API.

{{< callout >}}**Remarque :** les moniteurs **Webservice HTTP et Webservice HTTPS** utilisés pour la surveillance d'API ne sont plus disponibles pour les nouveaux utilisateurs. Uptrends recommande d'utiliser le moniteur d'API multi-étapes pour vérifier les comportements de vos API. {{< /callout >}}

Pour en savoir plus sur les moniteurs d'API, lisez notre article sur la [surveillance des API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}).

## Moniteurs de transaction

Les moniteurs de transactions, aussi appelés moniteurs d'application web ou de surveillance du parcours utilisateur, simulent les activités des utilisateurs au moyen d'un navigateur réel qui permet de vérifier les performances de votre site web.

Imaginez un utilisateur réel en train d'interagir avec votre site web depuis son navigateur. Il remplit des formulaires, clique sur des boutons et sélectionne des éléments sur votre site. Les moniteurs de transactions vous permettent de remplacer cet utilisateur par un robot effectuant exactement les mêmes actions. Ce robot est un checkpoint d'Uptrends qui ouvre un navigateur Chrome et utilise un script pour naviguer sur votre site et le tester. Ces scripts sont programmés pour effectuer les interactions que vos utilisateurs effectuent au quotidien.

Pour vous aider à automatiser vos transactions, les moniteurs de transactions travaillent de pair avec l'[enregistreur de transaction d'Uptrends/ITRS]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}). Cette extension Chrome enregistre votre progression dans les parcours de clics propres à vos transactions. Une fois vos transactions enregistrées, vous pouvez les enregistrer en tant que moniteur pour générer des scripts correspondant à l'enregistrement.

Pour configurer un moniteur de transaction, vous pouvez exécuter l'une des actions suivantes :

- Créez un moniteur de transaction au moyen de l'[éditeur d'étapes de transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}).
- [Téléchargez et utilisez l'enregistreur de transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}) pour créer des scripts que vous pourrez ensuite modifier et administrer.
- Demandez à l'équipe de support d'Uptrends d'utiliser votre enregistrement pour écrire et tester votre script.

Pour en savoir plus sur les moniteurs de transactions, vous pouvez lire les articles suivants :

- [Aperçu du suivi des transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}})
- [Comprendre la surveillance des transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="fr" >}})
- [Comment utiliser l'enregistreur de transactions d'Uptrends : tutoriel sur le parcours d'utilisation du panier d'achats]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/tutorial-introduction" lang="fr" >}}) : ce guide pas à pas vous explique comment utiliser l'enregistreur de transaction