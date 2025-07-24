{
  "hero": {
    "title": "Comprendre l'éditeur d'étapes"
  },
  "title": "Comprendre l'éditeur d'étapes",
  "summary": "L'éditeur d'étapes est utilisé pour modifier les étapes et les actions d'un script de transaction.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/comprendre-editeur-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

L'éditeur d'étapes est nécessaire pour modifier les étapes et les actions d'un script de transaction. Il est disponible sous forme d'éditeur visuel, dans lequel vous pouvez ajouter et modifier visuellement les étapes, ou sous forme d'éditeur textuel qui vous permet d'éditer du texte brut.

Si vous savez coder votre propre script, vous pouvez passer directement à la section [Écrire le code source de A à Z]([LINK_URL_1]) pour en savoir plus sur l'éditeur de script.

Dans la plupart des cas, vous n'écrirez pas le script directement. Au lieu de cela, vous utiliserez [l'enregistreur de transaction]([LINK_URL_2]) pour créer une première ébauche du script que vous modifierez ensuite avec l'éditeur d'étapes.

[SHORTCODE_1]
**Note** : Uptrends utilise des crédits de transaction pour calculer le prix de vos moniteurs de transactions. Le nombre de crédits utilisés pour un moniteur s'affiche après le nom du moniteur dans la vue d'ensemble *Moniteurs* (pour y accéder, ouvrez [SHORTCODE_3] Transactions > Gérer les transactions [SHORTCODE_4]). Pour tout savoir sur les crédits, lisez l'article de notre base de connaissances sur le [calcul du nombre de crédits utilisés par les moniteurs de transactions]([LINK_URL_3]).
[SHORTCODE_2]

## Étapes et actions

Le script d'un moniteur de transaction contient les étapes de la transaction à surveiller. Ces étapes se composent d'actions, qui correspondent aux micro-étapes de votre transaction.

Pour modifier les étapes et les actions :

1. Ouvrez [SHORTCODE_5] Transactions > Gérer les transactions [SHORTCODE_6].
2. Ouvrez l'onglet [SHORTCODE_7]Étapes[SHORTCODE_8].

![Capture d'écran de l'éditeur d'étapes]([LINK_URL_4])

Vous pouvez modifier et tester votre script de transaction dans l'onglet [SHORTCODE_9]Étapes[SHORTCODE_10]. Cet onglet vous permet aussi d'y écrire directement votre script si vous le souhaitez. Pour cela, utilisez le bouton [SHORTCODE_11] Basculer vers le script [SHORTCODE_12] en haut à droite de l'éditeur.

Si vous avez chargé votre script dans [l'enregistreur de transaction]([LINK_URL_5]), la ou les étapes et leurs actions devraient s'afficher. Si vous créez votre script de A à Z, vous coderez chaque étape de votre description dans l'éditeur d'étapes. Nous vous recommandons d'utiliser l'enregistreur de transaction pour disposer d'une bonne base de départ.

Comme indiqué ci-dessus, votre script de transaction comprend des *étapes* et des *actions*. Voyons plus précisément ce que ces deux termes signifient.

## Qu'est-ce qu'une étape ?

Lorsque vous chargez votre script depuis l'enregistreur de transaction, Uptrends définit automatiquement les étapes de la transaction. Mais qu'est-ce qu'une étape ? Une étape est un regroupement arbitraire d'actions dans votre script de transaction. Généralement, une étape regroupe les interactions de l'utilisateur qui se terminent par l'envoi d'une requête à un serveur, par exemple lors de l'envoi d'un formulaire. Regrouper les actions par requêtes adressées à un serveur est utile pour les opérations de dépannage et de rapport sur les performances.

L'étape peut aussi être envisagée comme une transition dans le navigateur, c'est-à-dire toute action qui crée une nouvelle page ou actualise la page avec du nouveau contenu. Cela étant, vous pouvez tout à fait regrouper vos étapes d'une autre façon si cela est pertinent dans votre cas et pour vos besoins de rapports de performances.

### Configuration des étapes [ANCHOR_1]

Cliquez sur la flèche **>** à côté du nom de l'étape pour accéder à ses paramètres et aux actions qui la composent.

![Capture d'écran d'une étape de script]([LINK_URL_6])

Pour chaque étape, plusieurs paramètres sont disponibles :

- **Cascade** : si vous le souhaitez, vous pouvez ajouter un [graphique en cascade]([LINK_URL_7]) à votre étape afin de connaître la performance du chargement de la page, les **Core Web Vitals** et les **métriques du W3C**. Chaque graphique en cascade utilise un [crédit d'étape de transaction]([LINK_URL_8]). Pour activer ce paramètre, cochez la case **Cascade** et ajustez les options selon vos besoins.

   1. **Nom** : donnez un nom descriptif à chaque étape. Par exemple, *Ajout au panier*, *Connexion* ou *Demande de rendez-vous*.

   2. **Gestion des erreurs** : pour continuer d'exécuter vos étapes ou scripts de transcription contenant des erreurs, cochez l'option **Ignorer toutes les erreurs qui se produisent dans cette étape**. Uptrends passe alors à l'étape suivante quel que soit le résultat de l'étape. Le rapport présentant les **détails de vérification** montre l'erreur, mais le moniteur de transaction continue ses vérifications. Pour en savoir plus, lisez l'article [Ignorer les erreurs pour les étapes et actions facultatives]([LINK_URL_9]).

   3. **Métriques de performance** : cochez cette option pour **stocker les Core Web Vitals et les scores W3C comme métriques séparées** dans vos moniteurs de transactions. Cette option vous permet d'afficher ces [métriques]([LINK_URL_10]) dans vos [tuiles personnalisées sous forme de liste ou graphique de données simple]([LINK_URL_11]) en cliquant sur l'icône [SHORTCODE_13] [SHORTCODE_14].


- **Filmstrip** : vous pouvez ajouter des [captures d'écran successives]([LINK_URL_12]) (aussi appelées pellicules) pour une ou plusieurs étapes. Chaque pellicule utilise un [crédit de transaction]([LINK_URL_13]), sauf si l'étape contient déjà une capture d'écran. Dans ce cas, la pellicule n'utilise aucun crédit.

- **Capture d'écran** : si vous le souhaitez, vous pouvez obtenir une [capture d'écran]([LINK_URL_14]) pour savoir ce qui s'affiche pour votre utilisateur à la fin de chaque étape. Vous pouvez créer une capture d'écran au moyen de [l'action]([LINK_URL_15]) de type *Contrôle* **Capture d'écran**. Une capture d'écran utilise un [crédit de transaction]([LINK_URL_16]).

- **Source de la page** : choisissez cette option pour obtenir des informations sur la source de la page et les données du journal de la console généré pendant l'exécution de l'étape. À noter que la source de la page est accessible uniquement en association avec le graphique en cascade.


### Ajouter des étapes

Pour ajouter une étape à votre script :

1. Faites défiler la page jusqu'au bas de l'onglet [SHORTCODE_15]Étapes[SHORTCODE_16].
2. Cliquez sur le bouton [SHORTCODE_17]Ajouter une étape[SHORTCODE_18].
3. Nommez cette étape, qui est actuellement vide.
4. (Facultatif) La poignée de déplacement (symbolisée par le rectangle en pointillé situé en haut à gauche de l'étape) vous permet de déplacer l'étape à l'emplacement souhaité dans la séquence du script.
5. Ajoutez les actions. Vous trouverez plus d'informations sur les actions au prochain paragraphe.
6. Cliquez sur le bouton [SHORTCODE_19] Enregistrer [SHORTCODE_20] pour enregistrer vos changements.

## Qu'est-ce qu'une action ?

Les actions désignent les interactions des utilisateurs, les vérifications de contenu et les interactions effectuées dans le navigateur à chaque étape. Ces actions se partagent en trois catégories présentées ci-dessous : Interaction, Test et Control.

#### Interaction

Les actions du type *Interaction* sont les suivantes :

- **Naviguer** : naviguer jusqu'à une URL.
- **Clic** : trouver un élément de page comme un bouton radio ou une case à cocher, et cliquer dessus.
- **Définir** : trouver et remplir un champ de texte, une zone de texte, un champ de mot de passe, etc.
- **Survol** : trouver un élément et le survoler pour afficher un autre élément masqué.
- **Évènement clé** : effectuer une pression de touche, par exemple lorsqu'un élément ne contient pas de bouton cliquable

Ces types d'actions sont décrits en détail dans l'article de la base de connaissances intitulé [Interactions de page]([LINK_URL_17]).


#### Test

Les actions de type *Test* correspondent à des vérifications de contenu ou à une action d'attente.

- **Tester le contenu de l'élément (ou Contenu de l'élément de test)** : vérifier qu'un élément contient le contenu attendu.
- **Tester le contenu du document** : vérifier que le contenu attendu est présent sur la page.
- **Attendre l'élément** : chercher et attendre un élément sur la page.
- **Attendre un temps défini** : ajouter un temps d'attente personnalisé

Reportez-vous aux articles de la base de connaissances sur les [vérifications de contenu]([LINK_URL_18]) et les [conditions d'attente]([LINK_URL_19]) pour comprendre leur utilité dans le cadre de la surveillance des transactions.

#### Contrôle

Les actions de la catégorie *Contrôle* sont les suivantes :

- **Capture d'écran** : prendre une capture d'écran de l'écran affiché.
- **Changer d'onglet de navigateur** : basculer vers une nouvelle fenêtre ou un nouvel onglet si votre page a ouvert une autre fenêtre de navigateur.
- **Basculer vers un nouveau cadre (ou Cadre de commutation)** : cette option vous permet de [passer d'un cadre intégré (iframe) à l'autre]([LINK_URL_20]) sur votre page.
- **Faire défiler** : trouver un élément de page et faire défiler jusqu'à son emplacement sur la page (cette option est particulièrement utile si vous utilisez des captures d'écran).
- **Ajuster le contenu de la variable** : modifier une variable existante grâce à l'action [Ajuster le contenu de la variable]([LINK_URL_21]).
- **Effacer le cache du navigateur** : [effacer le cache du navigateur]([LINK_URL_22]) pour recharger directement les éléments de la page depuis le serveur plutôt que depuis le cache.

### Ajouter une action [ANCHOR_2]

Pour ajouter une nouvelle action à l'une des étapes de votre moniteur de transaction :

1. Ouvrez l'étape à laquelle vous voulez ajouter une action.
2. Cliquez sur le bouton [SHORTCODE_21]Ajouter une action[SHORTCODE_22].
   La fenêtre contextuelle *Ajouter une action* s'affiche :
   ![Capture d'écran de la fenêtre contextuelle d'ajout d'action]([LINK_URL_23])
   Survolez les noms des actions pour en savoir plus sur leurs fonctions.
3. Cliquez sur l'action à ajouter à votre étape.
4. (Facultatif) Réorganisez les actions si nécessaire. Pour ce faire, cliquez sur la poignée de déplacement (symbolisée par le rectangle en pointillé situé en haut à gauche de l'étape) et déplacez l'étape à l'emplacement souhaité dans la séquence d'actions. Vous pouvez aussi déplacer l'action vers une autre étape.
5. Cliquez sur le bouton [SHORTCODE_23] Enregistrer [SHORTCODE_24] pour enregistrer vos changements.

### Sélecteurs CSS et requêtes Xpath [ANCHOR_3]

Vous avez peut-être remarqué que certaines des actions s'appuient sur des sélecteurs CSS ou des requêtes Xpath. Le moniteur de transaction sait ainsi exactement avec quel élément d'écran il doit interagir pour réaliser l'action. Si vous utilisez l'enregistreur de transaction, celui-ci décide de la méthode qu'il juge la meilleure pour localiser un élément sur votre page. Le processus de sélection est expliqué dans notre article intitulé [Détermination du sélecteur par l'enregistreur de transaction]([LINK_URL_24]).

Toutefois, l'algorithme ne choisit pas toujours la meilleure option. Vous pouvez trouver les autres options possibles en cliquant sur le bouton [SHORTCODE_25]\[...\][SHORTCODE_26] dans le champ du sélecteur.

Vous pouvez aussi coder votre propre sélecteur ou votre propre requête. Pour en savoir plus, lisez nos articles sur les [sélecteurs CSS]([LINK_URL_25]) ou les [requêtes XPath]([LINK_URL_26]). Si vous définissez les sélecteurs manuellement, vous pouvez utiliser des [variables automatiques]([LINK_URL_27]). Vous avez ainsi encore plus de flexibilité dans le choix du sélecteur.

Si vous ne maîtrisez pas bien les sélecteurs CSS et les requêtes Xpath, nous vous suggérons de contacter le [support d'Uptrends]([LINK_URL_28]) pour demander à notre équipe d'apporter les changements nécessaires.

### Configurer les actions

Les paramètres de vos actions diffèrent selon leur type. Veuillez consulter la page [Interactions de page]([LINK_URL_29]) pour connaître les paramètres de chaque action.


## Écrire le code source de A à Z [ANCHOR_4]

Vous pouvez tout à fait écrire vos scripts dans un autre éditeur ou environnement, et copier et coller le script dans notre éditeur textuel. Vous pouvez aussi écrire directement le code dans notre éditeur. Utilisez le bouton [SHORTCODE_27]Basculer vers le script[SHORTCODE_28] en haut de l'onglet [SHORTCODE_29]Étapes[SHORTCODE_30] pour ouvrir l'éditeur de texte. Une fois dans l'éditeur de texte, cliquez sur [SHORTCODE_31]Basculer vers l'éditeur visuel [SHORTCODE_32] pour revenir. Le script est validé à chaque passage d'un mode à l'autre.

![Capture d'écran des éditeurs textuel et visuel]([LINK_URL_30])

## Utiliser l'API

Vous pouvez aussi utiliser l'API d'Uptrends pour créer des moniteurs, charger et modifier des scripts et vérifier le statut de votre moniteur. Pour en savoir plus sur les méthodes disponibles, veuillez vous reporter à la documentation de [l'API]([LINK_URL_31]).
