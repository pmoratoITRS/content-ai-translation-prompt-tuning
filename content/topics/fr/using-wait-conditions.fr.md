{
"hero": {
"title": "Comment utiliser les conditions d'attente"
},
"title": "Comment utiliser les conditions d'attente",
"summary": "Lors de l'édition de scripts pour vos transactions, vous devez parfois indiquer au moniteur qu'il doit attendre un élément spécifique à charger avant de continuer. La surveillance des transactions prend en charge trois types de conditions d'attente",
"url": "/support/kb/surveillance-synthetique/transactions/les-conditions-d-attente",
"translationKey": "https://www.uptrends.com/support/kb/transactions/using-wait-conditions"
}

Le chargement d'une page prend du temps. De la même manière que lorsque c'est vous qui devez attendre le chargement d'une page, le script de transaction doit parfois également attendre la fin du chargement de la page avant de pouvoir continuer avec l'action suivante.

Le chargement d'une page est un peu chaotique car le navigateur divise le processus en phases avec certains éléments se chargeant simultanément tandis que d'autres éléments attendent leur tour. Par conséquent, il peut être difficile pour un script de savoir quand il faut effectuer une action. Le script doit attendre que le navigateur charge les éléments de la page et que ces éléments deviennent interactifs avant qu'il ne puisse passer à l'action suivante.

En raison du processus de chargement chaotique, les moniteurs de transactions d'Uptrends ont une option **Attendre l'élément**, disponible pour toutes les actions qui interagissent avec un élément spécifique. Avec cette option **Attendre l'élément**, vous pouvez définir une condition que doit remplir l'élément indiqué avant que la transaction n'exécute une action.

Actuellement, vous avez le choix entre trois conditions pour **Attendre l'élément**.

![](/img/content/37df779f-b4a7-4e0e-bf9f-8bc1ca996396.png)

## L'élément existe

L'option **L'élément existe** vérifie si l'élément indiqué existe dans le DOM de la page. Le simple fait qu'un élément existe ne signifie pas nécessairement que vous pouvez interagir avec l'élément, ni que l'élément est visible sur la page. Très souvent, le DOM d'une page contient des éléments que le navigateur ne rend pas pour différentes raisons. L'option **L'élément existe** permet à la transaction de tenter de se poursuivre dès qu'elle trouve l'élément indiqué dans le DOM.

## L'élément est visible

L'option **L'élément est visible** vérifie si l'élément existe dans le document et qu'il est visible sur la page. Par exemple, un menu déroulant (avec différents liens) qui ne devient visible que lorsque vous passez le curseur sur un élément de page spécifique. Ces liens existent dans le DOM avant que l'action de survol ne soit disponible, mais vous devez indiquer au moniteur de transactions d'attendre que le navigateur affiche les liens avant de pouvoir interagir avec eux.

## L'élément est à la fois visible et activé

L'option **L'élément est à la fois visible et activé** se comporte de la même manière que l'option **L'élément est visible**, avec une différence importante : non seulement l'élément doit être visible sur la page, mais l'élément doit également être activé. Par exemple, le navigateur désactive certains boutons (en les grisant) sur certaines pages jusqu'à ce que la page réponde à une exigence spécifique. La condition peut être que l'utilisateur remplisse un formulaire avant d'utiliser le bouton. Donc, l'élément est visible sur la page, mais vous devez également indiquer au moniteur de transactions d'attendre que le bouton soit activé avant de tenter une interaction.

## Qu'est-ce qu'une durée d'attente raisonnable ?

Le temps d'attente que vous définissez est la durée maximale pendant laquelle votre moniteur attend un élément. Les temps d'attente par défaut, sauf indication contraire, sont de 60 secondes pour la navigation et de 30 secondes pour tous les autres types d'action. Ces valeurs par défaut sont en général largement suffisantes, donc sauf besoin particulier, il n'est pas nécessaire de modifier la valeur par défaut. Mais si vous en avez le besoin, vous pouvez les modifier à l'aide du champ **Délai d'attente**. La valeur de timeout maximale pour tout type d'action est de 60 secondes. Points à considérer avec les délais d'attente :

- Pas de délais d'attente trop courts. Des délais d'attente trop courts peuvent provoquer la génération d'erreurs par votre moniteur. Nous vous recommandons de laisser les valeurs par défaut pour éviter les erreurs indésirables.
- Le temps d'exécution maximal autorisé par Uptrends pour un moniteur de transactions est de quatre minutes. Après quatre minutes, la transaction s'arrête. Le cumul de plusieurs délais d'attentes trop longs peuvent entraîner une erreur de votre moniteur en raison de cette limite de durée d'exécution maximale de quatre minutes.

{{< callout >}}
**Remarque** : En règle générale, il n'est pas nécessaire de modifier les valeurs par défaut des conditions d'attente. Si vous pensez devoir changer les conditions d'attente, [contactez le support](/contact) pour vous aider à les optimiser.
{{< /callout >}}
