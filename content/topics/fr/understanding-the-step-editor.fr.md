{
"hero": {
"title": "Comprendre l'éditeur d'étapes"
},
"title": "Comprendre l'éditeur d'étapes",
"summary": "L'éditeur d'étapes est utilisé pour modifier les étapes et les actions d'un script de transaction.",
"url": "/support/kb/surveillance-synthetique/transactions/comprendre-editeur-etapes",
"translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-the-step-editor"
}

L'éditeur d'étapes est nécessaire pour modifier les étapes et les actions d'un script de transaction. Il est disponible sous forme d'éditeur visuel, dans lequel vous pouvez ajouter et modifier visuellement les étapes, ou sous forme d'éditeur textuel qui vous permet d'éditer du texte brut.

Si vous savez coder votre propre script, vous pouvez passer directement à la section [Écrire le code source de A à Z]({{< ref path="#scripting-source-code-directly" lang="fr" >}}) pour en savoir plus sur l'éditeur de script.

Dans la plupart des cas, vous n'écrirez pas le script directement. Au lieu de cela, vous utiliserez [l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}) pour créer une première ébauche du script que vous modifierez ensuite avec l'éditeur d'étapes.

{{< callout >}}
**Note** : Uptrends utilise des crédits de transaction pour calculer le prix de vos moniteurs de transactions. Le nombre de crédits utilisés pour un moniteur s'affiche après le nom du moniteur dans la vue d'ensemble *Moniteurs* (pour y accéder, ouvrez {{< AppElement type="menuitem" >}} Transactions > Gérer les transactions {{< /AppElement >}}). Pour tout savoir sur les crédits, lisez l'article de notre base de connaissances sur le [calcul du nombre de crédits utilisés par les moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="fr" >}}).
{{< /callout >}}

## Étapes et actions

Le script d'un moniteur de transaction contient les étapes de la transaction à surveiller. Ces étapes se composent d'actions, qui correspondent aux micro-étapes de votre transaction.

Pour modifier les étapes et les actions :

1. Ouvrez {{< AppElement type="menuitem" >}} Transactions > Gérer les transactions {{< /AppElement >}}.
2. Ouvrez l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}.

![Capture d'écran de l'éditeur d'étapes](/img/content/scr_transaction-step-editor-041024.min.png)

Vous pouvez modifier et tester votre script de transaction dans l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}. Cet onglet vous permet aussi d'y écrire directement votre script si vous le souhaitez. Pour cela, utilisez le bouton {{< AppElement type="buttonSecondary" >}} Basculer vers le script {{< /AppElement >}} en haut à droite de l'éditeur.

Si vous avez chargé votre script dans [l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}), la ou les étapes et leurs actions devraient s'afficher. Si vous créez votre script de A à Z, vous coderez chaque étape de votre description dans l'éditeur d'étapes. Nous vous recommandons d'utiliser l'enregistreur de transaction pour disposer d'une bonne base de départ.

Comme indiqué ci-dessus, votre script de transaction comprend des *étapes* et des *actions*. Voyons plus précisément ce que ces deux termes signifient.

## Qu'est-ce qu'une étape ?

Lorsque vous chargez votre script depuis l'enregistreur de transaction, Uptrends définit automatiquement les étapes de la transaction. Mais qu'est-ce qu'une étape ? Une étape est un regroupement arbitraire d'actions dans votre script de transaction. Généralement, une étape regroupe les interactions de l'utilisateur qui se terminent par l'envoi d'une requête à un serveur, par exemple lors de l'envoi d'un formulaire. Regrouper les actions par requêtes adressées à un serveur est utile pour les opérations de dépannage et de rapport sur les performances.

L'étape peut aussi être envisagée comme une transition dans le navigateur, c'est-à-dire toute action qui crée une nouvelle page ou actualise la page avec du nouveau contenu. Cela étant, vous pouvez tout à fait regrouper vos étapes d'une autre façon si cela est pertinent dans votre cas et pour vos besoins de rapports de performances.

### Configuration des étapes {id="step-settings"}

Cliquez sur la flèche **>** à côté du nom de l'étape pour accéder à ses paramètres et aux actions qui la composent.

![Capture d'écran d'une étape de script](/img/content/scr_transaction-single-step-041024.min.png)

Pour chaque étape, plusieurs paramètres sont disponibles :

- **Cascade** : si vous le souhaitez, vous pouvez ajouter un [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}}) à votre étape afin de connaître la performance du chargement de la page, les **Core Web Vitals** et les **métriques du W3C**. Chaque graphique en cascade utilise un [crédit d'étape de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="fr" >}}). Pour activer ce paramètre, cochez la case **Cascade** et ajustez les options selon vos besoins.

   1. **Nom** : donnez un nom descriptif à chaque étape. Par exemple, *Ajout au panier*, *Connexion* ou *Demande de rendez-vous*.

   2. **Gestion des erreurs** : pour continuer d'exécuter vos étapes ou scripts de transcription contenant des erreurs, cochez l'option **Ignorer toutes les erreurs qui se produisent dans cette étape**. Uptrends passe alors à l'étape suivante quel que soit le résultat de l'étape. Le rapport présentant les **détails de vérification** montre l'erreur, mais le moniteur de transaction continue ses vérifications. Pour en savoir plus, lisez l'article [Ignorer les erreurs pour les étapes et actions facultatives]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="fr" >}}).

   3. **Métriques de performance** : cochez cette option pour **stocker les Core Web Vitals et les scores W3C comme métriques séparées** dans vos moniteurs de transactions. Cette option vous permet d'afficher ces [métriques]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/monitoring-results-overview" lang="fr" >}}) dans vos [tuiles personnalisées sous forme de liste ou graphique de données simple]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}) en cliquant sur l'icône {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}}.


- **Filmstrip** : vous pouvez ajouter des [captures d'écran successives]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}) (aussi appelées pellicules) pour une ou plusieurs étapes. Chaque pellicule utilise un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}), sauf si l'étape contient déjà une capture d'écran. Dans ce cas, la pellicule n'utilise aucun crédit.

- **Capture d'écran** : si vous le souhaitez, vous pouvez obtenir une [capture d'écran]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}}) pour savoir ce qui s'affiche pour votre utilisateur à la fin de chaque étape. Vous pouvez créer une capture d'écran au moyen de [l'action](#adding-an-action) de type *Contrôle* **Capture d'écran**. Une capture d'écran utilise un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}).

- **Source de la page** : choisissez cette option pour obtenir des informations sur la source de la page et les données du journal de la console généré pendant l'exécution de l'étape. À noter que la source de la page est accessible uniquement en association avec le graphique en cascade.


### Ajouter des étapes

Pour ajouter une étape à votre script :

1. Faites défiler la page jusqu'au bas de l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}}Ajouter une étape{{< /AppElement >}}.
3. Nommez cette étape, qui est actuellement vide.
4. (Facultatif) La poignée de déplacement (symbolisée par le rectangle en pointillé situé en haut à gauche de l'étape) vous permet de déplacer l'étape à l'emplacement souhaité dans la séquence du script.
5. Ajoutez les actions. Vous trouverez plus d'informations sur les actions au prochain paragraphe.
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour enregistrer vos changements.

## Qu'est-ce qu'une action ?

Les actions désignent les interactions des utilisateurs, les vérifications de contenu et les interactions effectuées dans le navigateur à chaque étape. Ces actions se partagent en trois catégories présentées ci-dessous : Interaction, Test et Control.

#### Interaction

Les actions du type *Interaction* sont les suivantes :

- **Naviguer** : naviguer jusqu'à une URL.
- **Clic** : trouver un élément de page comme un bouton radio ou une case à cocher, et cliquer dessus.
- **Définir** : trouver et remplir un champ de texte, une zone de texte, un champ de mot de passe, etc.
- **Survol** : trouver un élément et le survoler pour afficher un autre élément masqué.
- **Évènement clé** : effectuer une pression de touche, par exemple lorsqu'un élément ne contient pas de bouton cliquable

Ces types d'actions sont décrits en détail dans l'article de la base de connaissances intitulé [Interactions de page]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="fr" >}}).


#### Test

Les actions de type *Test* correspondent à des vérifications de contenu ou à une action d'attente.

- **Tester le contenu de l'élément (ou Contenu de l'élément de test)** : vérifier qu'un élément contient le contenu attendu.
- **Tester le contenu du document** : vérifier que le contenu attendu est présent sur la page.
- **Attendre l'élément** : chercher et attendre un élément sur la page.
- **Attendre un temps défini** : ajouter un temps d'attente personnalisé

Reportez-vous aux articles de la base de connaissances sur les [vérifications de contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}) et les [conditions d'attente]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}) pour comprendre leur utilité dans le cadre de la surveillance des transactions.

#### Contrôle

Les actions de la catégorie *Contrôle* sont les suivantes :

- **Capture d'écran** : prendre une capture d'écran de l'écran affiché.
- **Changer d'onglet de navigateur** : basculer vers une nouvelle fenêtre ou un nouvel onglet si votre page a ouvert une autre fenêtre de navigateur.
- **Basculer vers un nouveau cadre (ou Cadre de commutation)** : cette option vous permet de [passer d'un cadre intégré (iframe) à l'autre]({{< ref path="support/kb/synthetic-monitoring/transactions/switching-between-iframes-browser-tabs" lang="fr" >}}) sur votre page.
- **Faire défiler** : trouver un élément de page et faire défiler jusqu'à son emplacement sur la page (cette option est particulièrement utile si vous utilisez des captures d'écran).
- **Ajuster le contenu de la variable** : modifier une variable existante grâce à l'action [Ajuster le contenu de la variable]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="fr" >}}).
- **Effacer le cache du navigateur** : [effacer le cache du navigateur]({{< ref path="/support/kb/synthetic-monitoring/transactions/clear-browser-cache" lang="fr" >}}) pour recharger directement les éléments de la page depuis le serveur plutôt que depuis le cache.

### Ajouter une action {id="adding-action"}

Pour ajouter une nouvelle action à l'une des étapes de votre moniteur de transaction :

1. Ouvrez l'étape à laquelle vous voulez ajouter une action.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}}Ajouter une action{{< /AppElement >}}.
   La fenêtre contextuelle *Ajouter une action* s'affiche :
   ![Capture d'écran de la fenêtre contextuelle d'ajout d'action](/img/content/scr_add-action-popup.min.png)
   Survolez les noms des actions pour en savoir plus sur leurs fonctions.
3. Cliquez sur l'action à ajouter à votre étape.
4. (Facultatif) Réorganisez les actions si nécessaire. Pour ce faire, cliquez sur la poignée de déplacement (symbolisée par le rectangle en pointillé situé en haut à gauche de l'étape) et déplacez l'étape à l'emplacement souhaité dans la séquence d'actions. Vous pouvez aussi déplacer l'action vers une autre étape.
5. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour enregistrer vos changements.

### Sélecteurs CSS et requêtes Xpath {id="css-selectors-and-xpath-queries"}

Vous avez peut-être remarqué que certaines des actions s'appuient sur des sélecteurs CSS ou des requêtes Xpath. Le moniteur de transaction sait ainsi exactement avec quel élément d'écran il doit interagir pour réaliser l'action. Si vous utilisez l'enregistreur de transaction, celui-ci décide de la méthode qu'il juge la meilleure pour localiser un élément sur votre page. Le processus de sélection est expliqué dans notre article intitulé [Détermination du sélecteur par l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="fr" >}}).

Toutefois, l'algorithme ne choisit pas toujours la meilleure option. Vous pouvez trouver les autres options possibles en cliquant sur le bouton {{< AppElement type="button" >}}\[...\]{{< /AppElement >}} dans le champ du sélecteur.

Vous pouvez aussi coder votre propre sélecteur ou votre propre requête. Pour en savoir plus, lisez nos articles sur les [sélecteurs CSS](https://www.w3schools.com/cssref/css_selectors.asp) ou les [requêtes XPath](https://www.w3schools.com/xml/xpath_intro.asp). Si vous définissez les sélecteurs manuellement, vous pouvez utiliser des [variables automatiques]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="fr" >}}). Vous avez ainsi encore plus de flexibilité dans le choix du sélecteur.

Si vous ne maîtrisez pas bien les sélecteurs CSS et les requêtes Xpath, nous vous suggérons de contacter le [support d'Uptrends]({{< ref path="contact" lang="fr" >}}) pour demander à notre équipe d'apporter les changements nécessaires.

### Configurer les actions

Les paramètres de vos actions diffèrent selon leur type. Veuillez consulter la page [Interactions de page]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="fr" >}}) pour connaître les paramètres de chaque action.


## Écrire le code source de A à Z {id="scripting-source-code-directly"}

Vous pouvez tout à fait écrire vos scripts dans un autre éditeur ou environnement, et copier et coller le script dans notre éditeur textuel. Vous pouvez aussi écrire directement le code dans notre éditeur. Utilisez le bouton {{< AppElement type="buttonSecondary" >}}Basculer vers le script{{< /AppElement >}} en haut de l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}} pour ouvrir l'éditeur de texte. Une fois dans l'éditeur de texte, cliquez sur {{< AppElement type="buttonSecondary" >}}Basculer vers l'éditeur visuel {{< /AppElement >}} pour revenir. Le script est validé à chaque passage d'un mode à l'autre.

![Capture d'écran des éditeurs textuel et visuel](/img/content/scr_transaction-visual-script-editor-041024.min.png)

## Utiliser l'API

Vous pouvez aussi utiliser l'API d'Uptrends pour créer des moniteurs, charger et modifier des scripts et vérifier le statut de votre moniteur. Pour en savoir plus sur les méthodes disponibles, veuillez vous reporter à la documentation de [l'API]({{< ref path="support/kb/api" lang="fr" >}}).
