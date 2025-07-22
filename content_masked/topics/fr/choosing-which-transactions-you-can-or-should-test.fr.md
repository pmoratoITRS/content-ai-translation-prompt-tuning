{
  "hero": {
    "title": "Choisir les transactions que vous pouvez ou devez tester"
  },
  "title": "Choisir les transactions que vous pouvez ou devez tester",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/choisir-les-transactions-a-tester",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lorsqu'il s'agit de mettre en place une bonne stratégie de surveillance des transactions, une des premières étapes est de déterminer quelles transactions tester avec Web Application Monitoring.

## Quelles transactions puis-je surveiller ?

C'est mieux de demander : « Quels types de transactions NE PUIS-JE PAS surveiller avec la surveillance des applications web ». À l'aide de la surveillance des applications web, vous pouvez tester presque toute tâche qu'un utilisateur peut avoir besoin d'effectuer sur votre site ou service web. Cela vous laisse beaucoup d'options de surveillance. Parmi les transactions courantes que vous pouvez vérifier avec ce monitoring il y a :

- Connexion et de déconnexion,
- Fonctions de recherche,
- Effectuer une réservation,
- Opérations de panier : ajouter ou supprimer des produits et sélectionner des options,
- Remplir et envoyer des formulaires, en particulier ceux qui se connectent à d'autres services tels que la vérification d'adresse ou les calculateurs de frais d'expédition, et
- Opérations financières

## Comment choisir les meilleures transactions à surveiller

Votre site a certainement beaucoup de scénarios d'utilisateurs possibles. Il n'est pas possible de tester tous les scénarios, alors comment choisir ? Il faut, bien sur, **tester les transactions essentielles au succès de votre site et qui comptent pour vos utilisateurs** (vous allez en trouver plusieurs dans la liste ci-dessus). Il faudra [analyser vos scénarios utilisateurs]([LINK_URL_1]), les découper en tâches spécifiques telles que la connexion ou l'ajout d'un article à un panier. Créer des moniteurs qui surveillent des parties distinctes de votre système.  La configuration de moniteurs distincts pour vérifier chaque aspect d'un scénario utilisateur permet d'améliorer les rapports et les alertes. Par exemple, pour tester un panier, accédez à la page, ajoutez un article au panier, vérifiez le panier et quittez la transaction. Avec ce moniteur, vous testez la disponibilité des pages, les bases de données associées au produit et à l'utilisateur et la vitesse de transaction. Il faudra tester les transactions qui

- Accèdent aux serveurs pour vérifier la disponibilité du site, l'exactitude de la réponse et les temps de réponse.
- Ont besoin d'accéder aux bases de données et recevoir des réponses. Si votre système utilise plusieurs bases de données, configurez des moniteurs pour les cibler tous.
- Utilisent des services et fonctions externes. Par exemple, si votre transaction utilise des services tiers tels que les services de vérification de localisation et d'adresse, il serait souhaitable de les vérifier tous.

**Remarque** : Les transactions que vous choisissez de surveiller peuvent avoir des effets secondaires inattendus. Ne manquez pas de lire notre article [Mises en garde et astuces sur la surveillance des transactions]([LINK_URL_2]) avant de passer un moniteur en mode simulation ou production.

## Sur le choix des emplacements de test

Comme vous le savez probablement, la localisation de l'utilisateur peut avoir un impact énorme sur les performances et le succès des transactions. Prenez soin de bien choisir les emplacements des points de contrôle. Nous vous déconseillons de choisir l'ensemble des points de contrôle disponibles pour un seul moniteur. Faire des choix larges peut rendre l'identification des problèmes de performances et des erreurs affectant un domaine spécifique plus difficile à détecter. Voici pourquoi.

1. Lorsque vous avez choisi une grande zone de test, une vérification défaillante à un seul point de contrôle peut ne pas générer d'alerte. Si un point de contrôle a détecté une condition d'erreur, Uptrends choisit un autre point de contrôle de manière aléatoire, à partir de vos emplacements de test désignés, pour vérifier l'erreur. Parce que la vérification peut provenir d'une région entièrement différente, Uptrends ne peut pas vérifier l'erreur, donc il n'y a pas d'alerte. Par conséquent, une condition d'erreur pour un emplacement peut persister jusqu'à ce que vous détectiez des anomalies dans vos journaux de surveillance ou que la deuxième vérification a lieu dans la même région qui rencontre le problème.

   **Remarque** : Choisir trop peu de points de contrôle peut également réduire l'efficacité de votre surveillance. Vous devez choisir un minimum de trois points de contrôle pour n'importe quel moniteur, mais nous recommandons d'en choisir plus. Regardez attentivement chaque transaction lorsque vous faites vos choix de points de contrôle.

2. Les performances dépendent en grande partie de l'emplacement de l'utilisateur en raison de la latence et de la qualité du réseau. Certains emplacements peuvent connaître des temps de réponse longs qui passent inaperçus car ils dépassent à peine le temps de réponse minimum. Ou bien, le mauvais temps de réponse n'a pas pu être vérifié, ce qui signifie qu'une alerte ne se déclenche pas. Des contrôles trop espacés font que les temps de réponse longs n'ont pas suffisamment d'impact sur les rapports de performances pour être remarqué facilement.

**Solution** : Dupliquez votre moniteur. Chaque copie peut vérifier des régions spécifiques différentes. Vous obtiendrez des rapports plus fidèles à l'expérience de votre utilisateur dans la région. Avec un nombre de points de contrôle plus petit, Uptrends peut capturer et vous informer des problèmes localisés qui pourraient passer inaperçus avec une zone de points de contrôle plus large.
