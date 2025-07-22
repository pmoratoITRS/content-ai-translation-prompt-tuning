{
"hero": {
"title": "Interactions de page"
},
"title": "Interactions de page",
"summary": "Dans votre moniteur de transactions, vous avez la possibilité d'ajouter quatre types d'actions ou d'interactions, qui sont détaillés dans cet article. ",
"url": "/support/kb/surveillance-synthetique/transactions/interactions-page",
"translationKey": "https://www.uptrends.com/support/kb/transactions/page-interactions"
}

L'une des différences principales entre la surveillance des transactions et les autres types de surveillance est la capacité d'interagir avec les pages. Dans le cas de la surveillance de site web, Uptrends clique sur les éléments de la page, remplit des formulaires, saisit les informations de connexion, télécharge des fichiers et exécute toutes sortes d'actions utilisateur pour tester vos parcours utilisateur.

Avec les transactions en libre-service, vous créez un script qui interagit avec votre page au moyen de quatre types d'actions disponibles. Les quatre principales interactions de page abordées dans cet article sont *[Naviguer](#navigate)*, *[Clic](#click)*, *[Survol](#hover)* et *[Définir](#set)*. L'interaction **Définir** permet également le *[téléchargement de fichiers](#file-uploading-in-transactions)*. Il existe également [d'autres actions]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#what-is-an-action" lang="fr" >}}), comme la vérification du contenu, la prise d'une capture d'écran ou la création d'un rapport en cascade.

## Naviguer {id="navigate"}

La navigation est la toute première action enregistrée ou ajoutée à un script de transaction. Toute transaction commence par accéder à une URL avant de tester les fonctionnalités de votre site. L'action de navigation indique au navigateur d'accéder à l'URL et le moniteur attend que la page se charge complètement (dans un délai raisonnable).

Dans la plupart des cas, une transaction ne contient qu'une seule action de navigation au début. Cependant, une deuxième navigation est parfois nécessaire dans la transaction. Lorsque des actions de navigation supplémentaires sont nécessaires, nous vous recommandons de placer ces actions de navigation chacune dans une étape différente. Le fait de placer chaque action de navigation dans sa propre étape vous aide à mieux surveiller votre transaction, et à comprendre les mesures de timing Uptrends par étape.

Précisons qu'une action de navigation utilise toujours un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}).

### Options de navigation

Les options disponibles pour l'action de navigation comprennent les éléments suivants (voir la figure ci-dessous) :

- **URL** : l'URL utilisée pour la navigation (obligatoire)
- **Description** : une description de l'action, utilisée à des fins de reporting
- **Message d'échec** : le message à inclure dans les rapports d'erreur
- **Résultat** : case à cocher indiquant à Uptrends d'**ignorer le code d'état HTTP renvoyé**
- **Délai d'attente** : spécifiez la durée pendant laquelle Uptrends doit attendre la fin du chargement de la page. La valeur par défaut (et maximale) est de 60 secondes.

L'option **Résultat** se comporte différemment des autres types d'action. Par défaut, une action de navigation garantit que la page a été chargée correctement et que le moniteur a reçu un code d'état HTTP sans erreur (tout code d'état inférieur à 400). Tout code d'état 400 ou supérieur génère une erreur pour l'action de navigation et la transaction cesse de s'exécuter. Si vous avez besoin que la transaction se poursuive malgré la réception d'un code d'état d'erreur, activez l'option **Ignorer le code d'état HTTP renvoyé** pour indiquer à Uptrends de continuer quel que soit le code d'état résultant.

![](/img/content/79ab474d-32d0-4c57-9709-2d86eebebd89.png)

### Compléter les actions Naviguer avec des vérifications de contenu

Pour s'assurer que la transaction se termine sur la bonne page après l'action de navigation, on ajoute une vérification de contenu comme action suivante. Une vérification du contenu vous confirme que votre transaction a atterri sur la bonne page, que la page est entièrement chargée et qu'elle affiche les composants qui permettent au moniteur d'interagir avec la page avant d'exécuter l'action suivante.

### Utiliser des rapports en cascade avec les actions Naviguer

Puisqu'une action de navigation charge une nouvelle page, il peut vous sembler utile de regarder des mesures spécifiques du chargement en activant l'option de rapport en cascade dans l'étape qui contient l'action de navigation. Chaque graphique en cascade ajouté à une transaction utilise un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="fr" >}}).

## Clic {id="click"}

**L'action Clic** indique au navigateur de cliquer sur un élément spécifique de la page à l'aide d'un sélecteur CSS ou XPath. Il y a plusieurs utilisations possibles pour une action de clic :

- Sélectionner une option
- Ouvrir un sous-menu
- Sélectionner une case à cocher
- Cliquer sur un lien qui amène la transaction à la page suivante

Par conséquent, l'action Clic fait partie intégrante de toute transaction.

De manière générale, une action de clic se divise en deux catégories :

- Celles qui mènent à une nouvelle page (liens ou boutons)
- Celles qui exécutent une action sur la page existante

Un clic peut ou non entraîner l'utilisation d'un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}) .

### Options de l'action Clic

Les options d'action Clic sont les suivantes (voir la figure ci-dessous) :

- **Description** : une description de l'action, utilisée à des fins de reporting
- **Message d'échec** : le message à inclure dans les rapports d'erreur
- **Gestion des erreurs** : cochez la case **Ignorer les erreurs qui se produisent dans cette action** pour indiquer au moniteur de ne pas tenir compte des erreurs que cette action peut rencontrer, comme, par exemple, ne pas trouver l'élément cliquable.
- **Attendre jusqu'à** : avant qu'une action de clic puisse se produire, l'élément sur lequel le moniteur doit cliquer doit être rendu et visible sur la page (en termes CSS, l'élément doit être affiché et visible). Ces *conditions d'attente* sont décrites dans un [article de la base de connaissances qui leur est dédié]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}), dans lequel vous trouverez des informations sur les différentes options.
- **Délai d'attente** : vous pouvez spécifier la durée pendant laquelle le moniteur doit attendre que la condition **Attendre jusqu'à** ci-dessus soit remplie. Le temps d'attente par défaut est de 30 secondes, mais vous pouvez remplacer cette valeur par défaut par une autre valeur, jusqu'à un maximum de 60 secondes.
- **Hôte DOM fantôme** : si l'élément visé par l'interaction se trouve dans un DOM fantôme, la transaction doit être configurée de façon à chercher l'élément dans ce DOM fantôme. Pour en savoir plus, consultez l'article de notre base de connaissances sur [l'intégration d'un DOM fantôme dans une transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}).

![Interactions de page - Clic](/img/content/scr-page-interactions-click.min.png)


{{< callout >}}
**Remarque** : Si vous utilisez la touche [\Entrée\] plutôt que la souris pour activer le bouton d'envoi, l'enregistreur de transaction ne peut pas capter l'interaction. Pour contourner ce problème, vous devez utiliser un [*événement clé*]({{< ref path="#key-event" lang="fr" >}}) pour imiter l'appui sur une touche de clavier. Vous devez d'abord enregistrer votre transaction, puis ajouter l'*événement clé* manuellement dans l'éditeur d'étapes.
{{< /callout >}}


## Définir {id="set"}

**L'action Définir** indique au moniteur qu'il y a des valeurs à saisir. Plusieurs scénarios sont possibles pour cette action :

- **Remplir des champs et des zones de texte** : identifiants et autres chaînes de caractères couramment nécessaires dans les champs de saisie.  
   L'action Définir peut déclencher une fonction de remplissage semi-automatique ; par exemple, lorsque vous entrez un code postal ou un terme de recherche, la page suggère une adresse complète ou des termes fréquemment recherchés. Dans ces cas de remplissage semi-automatique, vous pouvez ajouter une vérification du contenu pour vous assurer que le remplissage a fonctionné correctement, puis ajouter une action de clic pour sélectionner l'option souhaitée.
- **Sélection d'options dans une liste déroulante** : généralement, les types d'éléments *select* ont plusieurs éléments *<option>* prédéfinis ayant chacun leurs valeurs propres. À l'aide d'un sélecteur CSS ou XPath, pointez le script sur l'élément select. Pour chaque élément option, vous pouvez choisir de définir un attribut *id*, un attribut *valeur* ou du texte.
- **Téléchargement de fichiers depuis le coffre-fort** : dans certains cas, un téléchargement de fichier (vers l'amont) peut être nécessaire pour tester correctement votre flux. Par exemple, si vous remplissez un formulaire de réclamation qui nécessite une capture d'écran obligatoire, ou si vous testez la capacité de téléchargement d'un référentiel en ligne. Il est possible de faire télécharger un fichier par la transaction, depuis le [coffre-fort de votre compte]({{< ref path="support/kb/account/vault" lang="fr" >}}). Vous trouverez des explications sur la configuration des téléchargements de fichiers [plus bas sur cette page](#file-uploading-in-transactions).

[L'ajout d'une action *Définir*]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-action" lang="fr" >}}) à une étape se déroule dans l'encadré suivant :

![Interactions de page - Définir](/img/content/scr-page-interactions-set.min.png)

Les *paramètres* sont expliqués dans la rubrique [Options de l'action Définir]({{< ref path="#setaction-options" lang="fr" >}}).

Vous devez d'abord décider quel élément vous souhaitez définir et sur quelle valeur. Indiquez le [sélecteur CSS ou la requête XPath]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}) pour l'élément pour lequel vous souhaitez définir une valeur (ou un chargement de fichier).

Cliquez ensuite sur les points de suspension pour ouvrir la fenêtre contextuelle **Sélectionnez une valeur**.

![capture d'écran de la sélection de valeur dans l'action définir](/img/content/scr_transaction-selection-value-picker.min.png)

Les options sont [Texte (brut) ou variable]({{< ref path="#variables" lang="fr" >}}), [Identifiants de coffre-fort]({{< ref path="support/kb/account/vault#credential-set" lang="fr" >}}), [Mot de passe à usage unique]({{< ref path="support/kb/account/vault#one-time-password" lang="fr" >}}) et [Téléchargement de fichier de coffre-fort]({{< ref path="#file-uploading-in-transactions" lang="fr" >}}).

### Texte (brut) ou variable {id="variables"}

Vous pouvez utiliser un texte simple, une variable ou une combinaison des deux pour définir la valeur d'un élément. Les variables peuvent être automatiques ou définies par l'utilisateur.
#### Variables automatiques

Vous pouvez utiliser l'action Définir pour renseigner des données générées dynamiquement, telles que des horodatages ou des chaînes sélectionnées aléatoirement depuis un tableau. Ces variables automatiques doivent être saisies comme suit : {{< Code/Symbol type="variable" >}}{{@variableGoesHere(option1,option2)}}{{< /Code/Symbol >}}

![Exemple de variable DateTime](/img/content/scr-page-interactions-datetime.min.png)

Si vous souhaitez utiliser des variables automatiques dans votre transaction, consultez la [liste complète des variables automatiques disponibles]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="fr" >}}).

#### Variables définies par l'utilisateur

Pour en savoir plus sur les variables définies par l'utilisateur, consultez l'article de notre base de connaissances sur [l'utilisation des variables dans les transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="fr" >}}).

### Téléchargement de fichiers dans les transactions {id="file-uploading-in-transactions"}

Si vous désirez configurer votre transaction pour télécharger des fichiers (vers le serveur), vous devez d'abord ajouter le ou les fichiers au coffre-fort. Pour savoir comment ajouter des fichiers à votre coffre-fort, consultez notre [article sur le coffre-fort]({{< ref path="support/kb/account/vault" lang="fr" >}}).

Lorsque vous avez ajouté le fichier à votre coffre-fort, vous êtes prêt à configurer la transaction pour le téléchargement. Le téléchargement de fichiers se fait avec l'action **Définir**. Il faut ajouter cette action à la transaction, puis la configurer pour télécharger le fichier :

1. Accédez à l'éditeur d'étape de la transaction appropriée via les options du moniteur, puis à l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}.

2. Ajouter une action **Définir** à l'étape où vous voulez effectuer le téléchargement.

3. Indiquez le [sélecteur CSS ou la requête XPath]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}) pour sélectionner l'élément de téléchargement d'un fichier.

   {{< callout >}}**Remarque** : Le plus souvent, l'élément de téléchargement de fichier avec lequel il faut interagir sur la page est `input type="file"`. Dans certains cas, ces éléments peuvent être « cachés » sur la page, alors l'utilisateur clique plutôt sur un bouton ou un lien. L'action **Définir** devrait s'appliquer à l'élément de téléchargement de fichier de la page. Étant donné que ces éléments ne sont pas toujours visibles, il est généralement judicieux de définir l'option **Attendre jusqu'à** dans l'action **Définir** sur *L'élément existe*, plutôt que de laisser la valeur par défaut *L'élément est à la fois visible et activé*.{{< /callout >}}

4. Cliquez sur le bouton points de suspension à droite du champ de saisie **Nouvelle valeur** pour ouvrir la boîte de dialogue qui vous permet de spécifier la valeur de l'élément.

5. Cliquez sur **Téléchargement de fichiers de coffre-fort** et sélectionnez le fichier correct. Si vous avez plusieurs fichiers dans votre coffre-fort, ils doivent être répertoriés par section de coffre-fort.

   ![capture d'écran de la sélection de valeur dans l'action définir](/img/content/scr-page-interactions-fileupload-vault.min.png)

La configuration de transaction pour télécharger un fichier est terminée. Vous pouvez maintenant continuer à créer la transaction comme vous le feriez normalement.

![Téléchargement de fichiers](/img/content/scr-page-interactions-fileupload.min.png)

### Options de l'action Définir {id="setaction-options"}

Pour l'action Définir, plusieurs options s'offrent à vous.

- **Description** : une description de l'action, utilisée à des fins de reporting.
- **Message d'échec** : le message à inclure dans les rapports d'erreur.
- **Gestion des erreurs** : cochez la case **Ignorer les erreurs qui se produisent dans cette action** pour indiquer au moniteur de ne pas tenir compte des erreurs que cette action peut rencontrer, comme, par exemple, ne pas trouver l'élément cliquable.
- **Attendre jusqu'à** : avant qu'une action de clic puisse se produire, l'élément sur lequel le moniteur doit cliquer doit être reproduit et visible sur la page (en termes CSS, l'élément doit être affiché et visible). Ces *conditions d'attente* sont décrites dans un [article de la base de connaissances qui leur est dédié]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}), dans lequel vous trouverez des informations sur les différentes options.
- **Délai d'attente** : vous pouvez spécifier la durée pendant laquelle le moniteur doit attendre que la condition Attendre jusqu'à ci-dessus soit remplie. Le temps d'attente par défaut est de 30 secondes, mais vous pouvez remplacer cette valeur par défaut par une autre valeur, jusqu'à un maximum de 60 secondes.
- **Affecter une variable** : Saisissez un nom de variable au format `{{name}}`. Cette variable contient la valeur définie dans cette action. Vous pouvez utiliser cette variable dans une action ou étape ultérieure.
- **Hôte DOM fantôme** : si l'élément visé par l'interaction se trouve dans un DOM fantôme, la transaction doit être configurée de façon à chercher l'élément dans ce DOM fantôme. Pour en savoir plus, consultez l'article de notre base de connaissances sur [l'intégration d'un DOM fantôme dans une transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}).

## Survol {id="hover"}

Lorsqu'une page contient des éléments qui nécessitent que l'utilisateur passe le curseur dessus pour effectuer une action, telle que la sélection d'un sous-menu ou la sélection dans une liste déroulante, il faut ajouter une **action de survol**. Avant que l'utilisateur ou le moniteur ne puisse interagir avec un élément tel qu'un lien dans un menu déroulant, l'élément doit être visible sur la page.

Étant donné que le curseur est toujours sur la page pendant l'enregistrement de la transaction, l'enregistreur pourrait enregistrer constamment les événements de survol qu'il faudrait supprimer après coup. Au lieu de supprimer éventuellement des centaines d'événements de survol inutiles, l'enregistreur n'enregistre aucune action de survol. Par conséquent, vous devez ajouter toutes les actions de survol requises après coup.

Dans l'exemple ci-dessous, pour accéder au menu de sélection des options de paiement, vous devez d'abord survoler le panier.

![Exemple de survol](/img/content/78c2d8f8-3fb0-44ed-a056-bb9231334f6c.gif)

### Options de l'action Survol

Vous disposez des options suivantes pour l'action de survol (voir la figure ci-dessous) :

- **Description** : une description de l'action, utilisée à des fins de reporting
- **Message d'échec** : le message à inclure dans les rapports d'erreur
- **Gestion des erreurs** : cochez la case **Ignorer les erreurs qui se produisent dans cette action** pour indiquer au moniteur de ne pas tenir compte des erreurs que cette action peut rencontrer, comme, par exemple, ne pas trouver l'élément cliquable.
- **Attendre jusqu'à** : avant qu'une action puisse se produire, le navigateur doit rendre l'élément pour qu'il soit visible sur la page. Ces *conditions d'attente* sont décrites dans un [article de la base de connaissances qui leur est dédié]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}), dans lequel vous trouverez des informations sur les différentes options.
- **Délai d'attente** : vous pouvez spécifier la durée pendant laquelle le moniteur doit attendre que la condition Attendre jusqu'à ci-dessus soit remplie. Le temps d'attente par défaut est de 30 secondes, mais vous pouvez remplacer cette valeur par défaut par une autre valeur, jusqu'à un maximum de 60 secondes.
- **Hôte DOM fantôme** : si l'élément visé par l'interaction se trouve dans un DOM fantôme, la transaction doit être configurée de façon à chercher l'élément dans ce DOM fantôme. Pour en savoir plus, consultez l'article de notre base de connaissances sur [l'intégration d'un DOM fantôme dans une transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}).

![Interactions de page - Survol](/img/content/scr-page-interactions-hover.min.png)

### Utiliser les vérifications de contenu après les actions de survol

Pour vérifier si une action de survol a réussi (si le sous-menu s'est chargé correctement), pensez à ajouter une action de vérification de contenu directement après le survol pour vérifier que le moniteur peut interagir avec le menu avant de continuer.


## Évènement clé {id="key-event"}

L'action *Évènement clé* vous permet d'ajouter une pression de touche à une étape de transaction. Cette action peut vous être utile lorsque la page web affiche un élément contenant lui-même un élément non cliquable (ou bouton). Par exemple, c'est parfois le cas lorsque vous cherchez un terme de recherche et qu'aucun bouton n'est utilisé pour lancer la recherche.

Dans une étape de transaction, ajoutez une nouvelle action et choisissez l'action *Évènement clé* dans la liste des interactions de page. Dans la nouvelle action, vous devez choisir un caractère dans une liste. Veuillez saisir un [sélecteur CSS ou XPath]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="fr" >}}) pour identifier l'élément pour lequel vous souhaitez configurer la touche.

### Options de l'action Évènement clé

Les options suivantes sont disponibles pour utiliser l'action *Évènement clé* dans une étape :

- **Description** : une description de l'action, utilisée à des fins de reporting.
- **Message d'échec** : le message à inclure dans les rapports d'erreur.
- **Gestion des erreurs** : cochez la case **Ignorer les erreurs qui se produisent dans cette action** pour indiquer au moniteur de ne pas tenir compte des erreurs que cette action peut rencontrer, comme, par exemple, ne pas trouver l'élément cliquable.
- **Attendre jusqu'à** : avant qu'une action puisse se produire, l'élément avec lequel le moniteur doit interagir doit être reproduit et visible sur la page (en termes CSS, l'élément doit être affiché et visible). Ces *conditions d'attente* sont décrites dans un [article de la base de connaissances qui leur est dédié]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}), dans lequel vous trouverez des informations sur les différentes options.
- **Délai d'attente** : vous pouvez spécifier la durée pendant laquelle le moniteur doit attendre que la condition Attendre jusqu'à ci-dessus soit remplie. Le temps d'attente par défaut est de 30 secondes, mais vous pouvez remplacer cette valeur par défaut par une autre valeur, jusqu'à un maximum de 60 secondes.
- **Hôte DOM fantôme** : si l'élément visé par l'interaction se trouve dans un DOM fantôme, la transaction doit être configurée de façon à chercher l'élément dans ce DOM fantôme. Pour en savoir plus, consultez l'article de notre base de connaissances sur [l'intégration d'un DOM fantôme dans une transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}).

![Exemple d'événement clé](/img/content/scr-page-interactions-keyevent.min.png)
