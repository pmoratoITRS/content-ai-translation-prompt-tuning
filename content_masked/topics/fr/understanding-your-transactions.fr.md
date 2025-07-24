{
  "hero": {
    "title": "Maîtriser vos transactions"
  },
  "title": "Maîtriser vos transactions",
  "summary": "Bien comprendre vos transactions, les parcours possibles et les pièges à éviter vous sera utile pour améliorer votre surveillance et vos résultats. ",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/maitriser-vos-transactions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Avant de vous lancer dans l'enregistrement ou l'écriture de votre script de transaction, vous devez planifier et bien comprendre vos transactions. Votre plan vous guidera dans l'enregistrement et le test de vos transactions, et vous prémunira contre différents problèmes.

## Répertorier et cartographier vos transactions

Toutes les transactions ne sont pas conçues de la même façon. Pour bien les comprendre, nous vous recommandons de les cartographier. Voici comment faire :

- Énumérez les principales tâches que vos utilisateurs effectuent sur votre site web ou votre application.
- Créez des diagrammes pour les principales tâches. Envisagez les différents parcours que les utilisateurs peuvent emprunter pour atteindre leur but sur votre site (différents parcours peuvent mener au même but).
- Assurez-vous de cartographier les parcours réussis (où tout se passe comme prévu) mais aussi les parcours chaotiques (où l'utilisateur rencontre des erreurs et des défauts). Par exemple, un parcours chaotique peut présenter des difficultés comme un échec d'authentification utilisateur, une rupture de stock, un problème de carte de crédit invalide, l'échec des systèmes de support comme les services de paiement ou des erreurs de base de données. Il peut être judicieux de tester ces différents aspects pour vous assurer que votre système réagit comme attendu.

Le diagramme ci-dessous vous présente les principales fonctionnalités et parcours de navigation sur un site d'e-commerce assez simple. L'image présente plusieurs parcours de navigation réussis. Certaines tâches dépendent de la bonne exécution d'autres tâches, et pourraient être découpées autrement.

![]([LINK_URL_1])

Pour simplifier, concentrons-nous sur la fonctionnalité du panier d'achats. Cette fonctionnalité inclut la sélection d'un article, son ajout au panier et sa modification.

Il peut être tentant d'élargir cette fonctionnalité pour y inclure les étapes de recherche ou de paiement. Toutefois, nous vous recommandons de cloisonner la fonctionnalité du panier d'achats pour ne tester qu'une tâche à la fois.

![]([LINK_URL_2])

## Autres éléments à prendre en compte

Avant de commencer à enregistrer vos transactions, prenez le temps de lire ces recommandations :

- Notre article [Choisir les transactions que vous pouvez ou devez tester]([LINK_URL_3]) vous aide à envisager les types de transactions que vous pouvez et devez surveiller avec la surveillance des transactions. Cet article vous explique aussi comment sélectionner les checkpoints qui serviront à surveiller vos transactions.
- La surveillance des transactions peut aussi avoir des conséquences négatives pour une entreprise, par exemple si elle réduit l'inventaire disponible ou entraîne des frais de la part des services de paiement. Veuillez lire nos [mises en garde et astuces]([LINK_URL_4]) avant de faire passer votre moniteur en mode [simulation ou production]([LINK_URL_5]).

Si tout cela vous semble compliqué, n'oubliez pas que notre [équipe de support]([LINK_URL_6]) est là pour vous accompagner.
