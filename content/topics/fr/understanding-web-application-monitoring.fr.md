{
"hero": {
"title": "Comprendre la surveillance des transactions"
},
"title": "Comprendre la surveillance des transactions",
"summary": "Cet article vous explique en quoi consiste la surveillance des applications (aussi appelée surveillance des applications web), comment elle fonctionne et quels types de transactions vous pouvez surveiller. ",
"url": "/support/kb/surveillance-synthetique/transactions/comprendre-surveillance-applications-web",
"translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-web-application-monitoring"
}

Qu'est-ce que la surveillance des transactions (aussi appelée surveillance des applications web) ? Notre article complet sur la [surveillance des applications web]({{< ref path="what-is/web-application-monitoring" lang="fr" >}}) contient des informations détaillées à ce sujet. En voici un très bref résumé :

*La surveillance des applications web désigne l'utilisation d'un moniteur (ou robot) synthétique pour effectuer des actions utilisateur sur un site web ou une application web à des intervalles réguliers. Le moniteur utilise un navigateur web (tout comme le font vos utilisateurs) pour vérifier le bon fonctionnement et les performances de votre site ou de votre application.*

Autrement dit, toute transaction qu'un utilisateur effectue sur votre site à l'aide d'un navigateur peut aussi être réalisée à intervalles réguliers par un moniteur de transaction. La surveillance de transactions vérifie votre site 24 h/24. Si la transaction échoue ou prend trop de temps, le système d'alertes d'Uptrends vous avertit.

## Pourquoi surveiller vos applications web ? {id="why-monitor-your-web-applications"}

Après tout, pourquoi surveiller vos transactions puisque les erreurs ne passent jamais inaperçues ? Bien sûr, vous finirez par les remarquer. Mais il ne faut pas oublier que la confiance et la réputation s'érodent rapidement.

### La lenteur et les défaillances peuvent coûter cher

Si votre site web ou votre service web ne fonctionne pas correctement, vos utilisateurs risquent de se tourner vers la concurrence.  Et la plupart ne reviendront jamais vers vous.

Les échecs des applications web sont coûteux sur le long terme. Mettez-vous à la place des utilisateurs : confieriez-vous des informations personnelles à une marque dont l'application présente des bugs et des lenteurs ?

Grâce à la surveillance des transactions, vous savez immédiatement quand un problème survient. Vous pouvez réagir sur le champ, avant que cela touche vos utilisateurs.

### Les conséquences peuvent s'avérer très coûteuses

Certaines organisations vérifient leurs transactions de temps en temps dans la journée. Mais que se passe-t-il quand les équipes rentrent chez elles ? L'application doit continuer de fonctionner même après les heures d'affluence. Votre site doit être opérationnel 24 h/24. Si vous ne le surveillez pas continuellement, bien des aspects peuvent dérailler sans que vous vous en aperceviez. Vérifier vos transactions 24 h/24 vous permet de repérer plusieurs types de problèmes, comme :

- La lenteur de chargement des pages et des transactions lors des actualisations d'inventaire matinales et d'autres opérations au niveau du backend. Vous espérez que ces opérations n'affectent pas vos utilisateurs, mais c'est inévitable.
- Les dépendances externes qui peuvent ne pas fonctionner correctement :
   - **Processus liés aux activités commerciales** : actualisation des stocks, calcul des prix et traitement des commandes
   - **Intégrations de systèmes** : prestataires de paiement tiers, services de localisation, intégrations de SharePoint/Office365, et modules de calcul externes
   - **E-commerce et web analytics** : suivi des comportements d'utilisation, Google Analytics et systèmes de publicité

   Bien que ces dépendances tierces semblent parallèles, les temps d'arrêt, les défaillances ou les erreurs des systèmes externes peuvent affecter votre performance globale, voire l'affichage et le comportement de vos pages.

## Quels types de transactions les moniteurs peuvent-ils surveiller ?

Ou plutôt : "quels types de transactions les moniteurs ne peuvent-ils pas surveiller ?". Voici quelques exemples de transactions dont vous pourriez vouloir surveiller les performances et le fonctionnement.

- Réussite des connexions
- Utilisation de la fonction de recherche de votre site
- Utilisation du calendrier dans un système de réservation
- Fonctions du panier d'achats : ajout, suppression et sélection des options des produits
- Remplissage de formulaires (p. ex, de commande) avec des liens avec d'autres services tels que la vérification d'adresse et le calcul des coûts d'expédition.
- Réussite des transactions financières : connexion aux services de paiement, validation des saisies des utilisateurs et réception de réponses de serveurs valides.

## Comment sélectionner les transactions à surveiller ?

Votre site présente probablement de très nombreux scénarios d'utilisation. Vous ne pouvez pas tous les tester, alors comment choisir ? Le plus judicieux est de tester les transactions cruciales pour votre site et celles sur lesquelles comptent vos utilisateurs (la plupart figurent dans la liste ci-dessus). Vous pouvez aussi sélectionner les transactions qui nécessitent différents systèmes et services pour fonctionner correctement. Sélectionnez les transactions qui mobilisent différents aspects de vos systèmes pour vérifier :

- La disponibilité et les délais de réponse du serveur de support
- L'accès et les réponses de la base de données : s'il existe plusieurs bases de données, choisissez les transactions qui les mobilisent toutes. Il peut s'agir des bases de données concernant vos utilisateurs, vos produits, vos commandes, les données de vos utilisateurs ou toute autre base de données sur laquelle s'appuie votre système.
- La disponibilité et le fonctionnement des services externes : par exemple, la vérification des lieux et des adresses, la recherche de codes postaux, les systèmes de gestion des stocks, les services logistiques, les services de paiement ou les systèmes de gestion des relations clientèle.

## Quelles données dois-je utiliser pour effectuer les tests ?

Lorsque vous choisissez les données à utiliser pour vos tests, il est préférable d'utiliser des données spécialement réservées à cette fin. Par exemple, pour un site d'e-commerce, utilisez plutôt des ID de produit qui ne sont pas liés à des produits réels de l'inventaire, afin d'éviter toute conséquence fâcheuse. Nous avons recensé tous les pièges à éviter lors de la surveillance de votre site ou service, et certains de ces problèmes découlent directement des données choisies pour les tests. Pour connaître ces risques et leurs solutions, vous pouvez lire notre article intitulé [Mises en garde et astuces]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="fr" >}}). Nous vous présentons ci-dessous quelques problèmes spécifiques aux données qu'il est important d'envisager.

### E-commerce
Lorsque vous choisissez des produits pour vos tests, souvenez-vous que le moniteur renvoie une erreur si votre inventaire s'épuise.

- Votre moniteur peut générer des commandes qui réduisent vos stocks disponibles. Ces commandes réalisées aux fins de test peuvent empêcher vos utilisateurs d'acheter des produits qui paraîtront indisponibles.
- Les commandes générées pour les tests peuvent entraîner un réapprovisionnement automatique.
- La génération de bons de préparation et de bordereaux d'expédition peut amener le service d'expédition à conditionner voire à envoyer des articles de test.
- Les e-mails de confirmation d'achat risquent de remplir une messagerie, qui peut être la vôtre.
- Les tests des systèmes de paiement peuvent modifier les soldes et engendrer des frais pour les services de paiement.

### Systèmes de réservation
Les systèmes de réservation et outils similaires posent des questions spécifiques.

- Votre moniteur peut remplir vos créneaux disponibles et empêcher les utilisateurs réels de faire des réservations.
- Les e-mails de confirmation peuvent inonder des messageries.
- Les réservations peuvent générer des frais de banque et de service.

### Identifiants de connexion

Les informations de connexion doivent être sécurisées, et la fonctionnalité de création automatique doit générer des identifiants uniques. Suivez les recommandations suivantes :

- Choisissez soigneusement les identifiants de connexion.
- Limitez les [autorisations]({{< ref path="support/kb/account/permissions" lang="fr" >}}) de l'utilisateur test et surveillez étroitement le compte afin de détecter toute activité anormale.
- Protégez les identifiants grâce au [coffre-fort]({{< ref path="support/kb/account/vault" lang="fr" >}}) d'Uptrends.
- Assurez-vous de déconnecter l'utilisateur à la fin de la transaction pour prévenir les conflits de connexion lors du prochain test.

### Analytics et Real User Monitoring

Votre surveillance a un impact sur les données d'analytics et de Real User Monitoring. Heureusement, ce problème peut être évité grâce au [blocage d'URL et de Google Analytics]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="fr" >}}).

## Le moniteur de transaction est-il toujours le meilleur choix ? {id="transaction-best-choice"}

Le moniteur de transaction est idéal pour vous assurer que votre système vous permet d'obtenir le résultat escompté. Toutefois, les autres types de moniteur peuvent aussi vous renseigner sur les performances et la disponibilité globale de votre site web ou de votre service.

### Disponibilité du site web

Les vérifications des moniteurs de transactions ont lieu toutes les cinq minutes au minimum, soit un intervalle qui peut laisser place à plusieurs temps d'arrêt. Avec les moniteurs de disponibilité, vous pouvez vérifier la disponibilité des pages web ou des services web à des intervalles beaucoup plus réguliers. Vous pouvez aussi configurer des [moniteurs de disponibilité avancés]({{< ref path="/products/synthetics/advanced-availability-monitoring" lang="fr" >}}) pour surveiller les bases de données, les serveurs de messagerie, les serveurs FTP/SFTP, les certificats SSL et les réponses DNS.

### Performance du site web

La surveillance des transactions mesure les temps de chargement des pages. Des données plus précises sont aussi possibles grâce à l'ajout de graphiques en cascade. Cependant, la surveillance de performance porte davantage sur la réactivité des serveurs face aux interactions de vos utilisateurs, telles que les envois. [La surveillance des performances web]({{< ref path="products/synthetics/web-performance-monitoring" lang="fr" >}}) vous apporte des données plus détaillées sur la performance d'une page web, de la première requête au chargement complet. Les moniteurs de type [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) vous fournissent des informations détaillées sur le temps de chargement de chaque page. Vous pouvez voir la progression et la performance du chargement pour toute la page et pour chacun de ses éléments. Chaque vérification inclut plus de données, et Uptrends a aussi optimisé les dashboards de performance pour pouvoir comparer rapidement les temps de chargement de chaque page.

### Monitoring d'API

Votre transaction nécessite probablement plusieurs appels d'API. Certains appels sont composés d'une seule requête, tandis que d'autres en nécessitent plusieurs pour mener à bien une transaction. En surveillant les API séparément de vos transactions grâce au [monitoring d'API]({{< ref path="products/synthetics/api-monitoring" lang="fr" >}}), vous repérez plus tôt les problèmes d'API et vous obtenez plus de données d'analyse en cas d'erreur.

Pour surveiller la disponibilité de vos services web, appuyez-vous sur les types de moniteur Webservice HTTP ou Webservice HTTPS qui vous permettent de vérifier la disponibilité des API chaque minute. Cette solution est plus adaptée que la surveillance de transactions pour suivre les accords de niveau de service associés à l'API et réagir rapidement aux problèmes de disponibilité.

Pour surveiller une séquence d'étapes, tournez-vous vers le [moniteur d'API multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}) (ou moniteur MSA, pour Multi-step API). Ce moniteur vérifie les réponses et les performances à chaque étape du fonctionnement de votre API (qu'elle nécessite une ou plusieurs réponses). Vous obtenez des informations détaillées sur les réponses à valider.

La surveillance des applications web contrôle l'ensemble de l'interaction entre un utilisateur et une application, tandis que le monitoring d'API multi-étapes s'intéresse à l'interaction avec l'API au-delà de l'application web. Par exemple, vous pouvez choisir d'utiliser un moniteur d'API multi-étapes pour tester la communication entre le système de sécurité et le prestataire de service, ou pour surveiller les transactions avec votre prestataire de traitement des opérations par carte de crédit.

## Dois-je m'y connaître en développement pour créer des moniteurs de transactions ?{id="programming-skills"}

Une maîtrise des technologies de développement vous sera certainement utile, mais votre connaissance de vos applications et de vos services vous permettra déjà d'en faire beaucoup. Lisez l'article [Options pour les scripts de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="fr" >}}) pour en savoir plus sur les transactions en service complet, en libre-service ou en autonomie complète. Votre équipe de développement ou DevOps peut vous aider à :

- Répliquer et adapter les scripts pour des sites miroirs en d'autres langues, ou des workflows et fonctionnalités similaires.
- Adapter les scripts en vue du déploiement des prochaines mises à jour de votre site, en phase avec le calendrier de mise à jour défini par votre système d'intégration et de déploiement en continu (CI/CD).
- Utiliser l'API d'Uptrends pour configurer vos moniteurs de façon à appuyer votre système d'assurance qualité.
