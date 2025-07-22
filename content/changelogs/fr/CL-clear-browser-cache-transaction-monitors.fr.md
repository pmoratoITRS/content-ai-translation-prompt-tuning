{
"title": "Fonction d'effacement du cache du navigateur dans les moniteurs de transactions",
"date": "2025-01-29",
"url": "/changelog/janvier-2025-effacer-cache-navigateur-moniteurs-transactions",
"translationKey": "https://www.uptrends.com/changelog/january-2025-clear-browser-cache-transaction-monitors"
}

Pour vérifier la performance de votre site web, les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}) d'Uptrends ouvrent un navigateur réel afin de simuler les activités de vos utilisateurs. Initialement vide, le cache du navigateur conserve ensuite temporairement les ressources de votre site web afin d'accélérer son chargement.

Effacer le cache du navigateur peut être utile pour comparer le comportement de votre site d'e-commerce selon que les articles du panier d'achats sont ajoutés par des utilisateurs préexistants (avec des données en cache) ou de nouveaux utilisateurs (sans données en cache).

Grâce à la nouvelle action **Effacer le cache du navigateur** proposée dans les étapes des moniteurs de transactions, vous pouvez désormais effacer le cache du navigateur pour recharger les éléments de page directement depuis le serveur, plutôt que depuis le cache. Cette fonctionnalité vous aide à vérifier les performances des premières visites sur votre site web ainsi que le bon chargement des éléments de l'interface (par exemple, images, textes et autres contenus). Cette action d'étape ne coûte aucun crédit de transaction et vous permet de renforcer la surveillance. Pour en savoir plus, lisez notre article sur l'[éditeur d'étapes de transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}).

![GIF Effacer le cache du navigateur](/img/content/gif-transaction-clear-browser-cache.gif)