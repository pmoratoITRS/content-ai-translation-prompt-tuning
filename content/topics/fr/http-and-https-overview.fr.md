{
"hero": {
"title": "Vue d'ensemble des moniteurs HTTP et HTTPS"
},
"title": "Vue d'ensemble des moniteurs HTTP et HTTPS",
"summary": "Découvrez comment fonctionne la surveillance de la disponibilité avec les moniteurs HTTP et HTTPS, ainsi que les options de surveillance HTTP avancées.",
"url": "/support/kb/surveillance-synthetique/uptime-monitoring/http-et-https/vue-densemble-de-http-et-https",
"translationKey": "https://www.uptrends.com/support/kb/http-and-https/http-and-https-overview",
"sectionlist": false
}

{{< callout >}}**Remarque :** Le moniteur **HTTP** n'est plus disponible pour les nouveaux utilisateurs. Uptrends a élargi les fonctionnalités des moniteurs **HTTPS** pour prendre en charge et vérifier la disponibilité des sites web HTTP. {{< /callout >}}

Les moniteurs de disponibilité HTTP (Hypertext Transfer Protocol) et HTTPS (Hypertext Transfer Protocol Secure) sont des [moniteurs]({{< ref path="support/kb/basics/monitor-types" lang="fr" >}}) qui peuvent être configurés de façon très rapide et très simple. Ces moniteurs fonctionnent de façon similaire, ce qui vous permet de vérifier la disponibilité de sites web basés sur des requêtes HTTP et HTTPS.

Ces moniteurs exécutent des vérifications de base sur vos sites web `http://` et `https://` depuis des [checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="fr" >}}) spécialement dédiés situés dans le monde entier. Ces vérifications de base vous permettent de surveiller les codes de réponse du site web, le temps de chargement des pages et le chargement du contenu. Dans les faits, les moniteurs HTTP et HTTPS récupèrent simplement les ressources demandées auprès du site web. Leur principal objectif est de vérifier qu'une réponse sans erreur est reçue du serveur web et de confirmer que votre page est opérationnelle. Pour en savoir plus, lisez l'article [Le fonctionnement d'un moniteur HTTP]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/how-an-http-monitor-works" lang="fr" >}}).

Si vous voulez configurer des vérifications approfondies pour mesurer précisément la performance et la disponibilité de votre site web, Uptrends vous recommande d'utiliser un moniteur [Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}). Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Vérification de base des pages comparé aux Real Browser Checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="fr" >}}).

## Configuration d'un moniteur HTTP ou HTTPS

La différence de configuration entre un moniteur HTTP ou un moniteur HTTPS est minime. Plus complet et sécurisé que le moniteur HTTP, le moniteur HTTPS contient une vérification supplémentaire concernant les certificats SSL. Pour configurer ce paramètre, ouvrez l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} dans votre éditeur de moniteur et cochez l'option **Vérifier les erreurs de certif. SSL**.

Cette option permet à votre moniteur HTTPS de confirmer que le certificat SSL ne génère pas d'erreurs. Décochez-la uniquement si vous souhaitez ignorer les erreurs générées par votre certificat SSL. Si vous souhaitez effectuer une surveillance approfondie de vos certificats SSL, vous trouverez des informations sur les autres vérifications possibles dans l'article [Moniteurs de certificat SSL]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="fr" >}}).

Pour créer votre propre moniteur HTTP ou HTTPS, lisez l'article de notre base de connaissances intitulé [Ajouter un moniteur HTTP(S) ou Webservice HTTP(S)]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="fr" >}}).

## Paramètres HTTP avancés

Pour personnaliser davantage votre moniteur, ouvrez l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} dans votre moniteur HTTP ou HTTPS et configurez les options suivantes :

- [Agent utilisateur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks#what-is-a-user-agent" lang="fr" >}})
- Authentification : si la ressource HTTP que vous surveillez nécessite une authentification dans la requête HTTP, choisissez le type d'authentification approprié (Aucun, Authentification de base, Authentification NTLM (Windows) ou Méthode Digest). Saisissez vos informations d'identification dans les champs **Nom d'utilisateur** et **Mot de passe**. Sachez qu'Uptrends applique toujours un [chiffrement]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="fr" >}}) pour protéger vos données.
- Champs de requête HTTP personnalisés : configurez les options **Méthode HTTP** (GET/POST), **HTTP request headers**, **Vérifier les erreurs de certif. SSL** et **Version(s) TLS**. Pour en savoir plus à ce sujet, lisez cet [article de notre base de connaissances]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/monitoring-websites-other-than-the-production-server" lang="fr" >}}).
