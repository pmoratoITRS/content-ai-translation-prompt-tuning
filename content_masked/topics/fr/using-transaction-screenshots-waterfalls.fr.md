{
  "hero": {
    "title": "Utilisation des captures d'écran et des cascades dans les transactions"
  },
  "title": "Utilisation des captures d'écran et des cascades dans les transactions",
  "summary": "Pour tester rigoureusement vos scripts de transaction et résoudre les éventuels problèmes, vous devez examiner les rapports en cascade et les captures d'écran. Ces ressources vous permettent de connaître la source des erreurs et de vérifier le bon fonctionnement de vos scripts de surveillance des transactions. ",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/utilisation-captures-ecran-cascades-transactions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les [moniteurs de transactions]([LINK_URL_1]) d'Uptrends incluent plusieurs options d'analyse et de débogage. Les captures d'écran et les rapports en cascade figurent parmi ces options. Ces outils sont essentiels pour surveiller les transactions, mais aussi pour analyser les causes profondes et les performances.

[SHORTCODE_1]
**Remarque** : Les captures d'écran et les rapports en cascade sont disponibles pour tous les utilisateurs qui utilisent le bouton [SHORTCODE_5] Tester maintenant [SHORTCODE_6]. Toutefois, seuls les abonnés **Enterprise** et **Business** peuvent les ajouter pour les utiliser en mode simulation et production.
[SHORTCODE_2]

## Activer les rapports en cascade et les captures d'écran

1. Ouvrez les paramètres du moniteur de transaction pour lequel vous souhaitez activer les graphiques en cascade ou les captures d'écran (par exemple, cliquez sur [SHORTCODE_7] Surveillance > Configuration du moniteur [SHORTCODE_8] dans la barre latérale).
2. Dans l'onglet [SHORTCODE_9]Étapes[SHORTCODE_10], sélectionnez l'étape pour laquelle vous souhaitez activer le graphique en cascade ou la capture d'écran.
3. Cochez la case correspondante pour cette étape.

- Sachez que vous pouvez aussi ajouter des captures d'écran pendant une étape grâce à [l'ajout d'action]([LINK_URL_2]).

- L'option cascade doit être activée pour voir les [données de la source de la page et du journal de la console]([LINK_URL_3]).

Pour rappel, chaque ajout de cascade ou de capture d'écran coûte un [crédit de moniteur de transaction]([LINK_URL_4]).

[SHORTCODE_3]
**Remarque** : Vous pouvez configurer les graphiques en cascade relatifs à vos transactions de façon à afficher des métriques supplémentaires comme navigateur dans l'onglet [SHORTCODE_11]Avancé[SHORTCODE_12] des paramètres du moniteur.
[SHORTCODE_4]


Uptrends génère un graphique en cascade ou une capture d'écran dans les situations suivantes :

- **En cas d'erreur :** quand une erreur confirmée survient pendant une transaction, une capture d'écran (mais **pas** de graphique en cascade) est générée. Aucun réglage de votre part n'est nécessaire, la capture d'écran est générée automatiquement dès la première erreur confirmée.
- **Avec chaque résultat d'une vérification effectuée par un moniteur :** à l'issue d'une étape pour laquelle vous avez configuré un graphique en cascade ou une capture d'écran.

## Trouver les rapports en cascade et les captures d'écran

Les captures d'écran et les graphiques en cascade sont indispensables pour le dépannage et le débogage des erreurs de transaction. Elles sont générées automatiquement quand vous cliquez sur le bouton [SHORTCODE_13] Tester maintenant [SHORTCODE_14]. Par ailleurs, les abonnés Enterprise et Business obtiennent une capture d'écran pour la première erreur confirmée.

### Où se trouvent mes captures d'écran et graphiques en cascade lors du débogage ?

Quand vous testez votre transaction en mode développement, il est normal que vous cliquiez régulièrement sur le bouton Tester maintenant. Les rapports en cascade et captures d'écran jouent un rôle important dans les résultats des vérifications suscitées par le bouton Tester maintenant. Pour les consulter, cliquez sur le bouton **Résultats de test disponibles** qui se trouve en haut de chaque étape après l'exécution d'un test manuel.

![]([LINK_URL_5])

Après avoir cliqué sur le bouton **Résultats de test disponibles**, faites défiler la page jusqu'aux **informations de débogage**. Pour les tests manuels, le rapport inclut automatiquement les détails du débogage.

Cliquez sur le graphique pour afficher la capture d'écran ou le graphique en cascade.

![Capture d'écran et graphique en cascade après l'option Tester maintenant]([LINK_URL_6])

### Où se trouvent les captures d'écran et les graphiques en cascade dans mes rapports ?

Pour les abonnés Enterprise et Business, les captures d'écran obtenues en mode simulation et production se trouvent dans les rapports détaillés. Cliquez sur [SHORTCODE_15]Surveillance > Journal moniteurs [SHORTCODE_16] dans le menu Uptrends pour afficher votre journal de moniteurs.

**Captures d'écran** : si vous voyez une icône d'appareil photo dans le journal du moniteur, c'est que le rapport détaillé contient une capture d'écran.

**Graphiques en cascade** : si vous avez ajouté des graphiques en cascade à vos scripts de transaction, des graphiques sont disponibles pour chaque semaine. Le journal des moniteurs ne contient pas de confirmation visuelle.

![]([LINK_URL_7])

Pour afficher la capture d'écran ou les graphiques en cascade :

1. Cliquez pour voir le rapport détaillé.
2. Affichez la section **Voir les détails**
3. Cliquez sur l'icône de l'appareil photo ou de la cascade dans les résultats de votre étape.

![]([LINK_URL_8])

## Utiliser les captures d'écran pour le débogage

Afin de voir le résultat d'une étape à l'écran, votre test génère une capture d'écran. La capture d'écran vous montre à quoi ressemblait la fenêtre active après une étape réussie ou une erreur de page. Si l'action se produit plus bas dans la page, vous pouvez ajouter une action de défilement avant l'événement de clic.

La capture d'écran vous permet de vérifier les éléments suivants :

- **Le contenu attendu a été chargé.** Vérifiez que le bon contenu s'affiche lors de la navigation sur une page.
- **Le contenu dynamique a bien été généré après une saisie de l'utilisateur**. Vérifiez que l'élément s'est correctement rempli, par exemple si la sélection d'un élément nécessite que l'utilisateur sélectionne une couleur avant que les options de taille ne soient disponibles.
- **Les champs masqués fonctionnent comme prévu**. Le caractère a-t-il le bon format ?
- **Design auto-adaptatif**. Si votre site utilise un design auto-adaptatif (aussi connu sous le nom de responsive design), vous aurez peut-être à ajuster la résolution du navigateur dans les paramètres de votre moniteur. En ajustant la résolution de votre navigateur, vous vous assurez que vous obtenez la bonne mise en page. Par exemple, si votre menu se réduit à une icône de hamburger lorsque la fenêtre du navigateur devient plus petite, il faudrait peut-être ajouter des actions de clic ou de survol. Vérifiez l'onglet [SHORTCODE_17]Avancé[SHORTCODE_18] du moniteur pour régler la résolution de votre navigateur.

## Utiliser les graphiques en cascade pour le débogage

Le graphique en cascade vous donne des informations détaillées sur le temps de chargement de la page initiale. Vous voyez exactement combien de temps il a fallu pour récupérer et traiter chaque élément de page ainsi que les en-têtes de requête et de réponse. Votre cascade vous aidera à rapidement identifier les problèmes sur la page. Lisez l'article de la base de connaissances sur les [graphiques en cascade]([LINK_URL_9]) pour en savoir plus à ce sujet.

![]([LINK_URL_10])


