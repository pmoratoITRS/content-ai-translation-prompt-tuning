{
"hero": {
"title": "Tester et modifier votre script de transaction"
},
"title": "Tester et modifier votre script de transaction",
"summary": "Cet article vous explique comment tester et modifier vous-même votre moniteur une fois votre transaction enregistrée.",
"url": "/support/kb/surveillance-synthetique/transactions/tutorial-record-user-journey-in-shop/tester-votre-transaction",
"translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction"
}

Cet exercice vous présente les étapes à suivre pour modifier et tester une transaction simple, ainsi que quelques-unes des principales opérations de dépannage.

L'exemple utilisé provient d'un exercice antérieur, que vous trouverez ici : [Enregistrer un parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}). Si vous n'avez pas encore réalisé cet exercice, vous pouvez le faire maintenant ou alors [copier et coller ce script]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/test-script" lang="fr" >}}) dans l'éditeur d'étapes.

## Réaliser un test manuel en mode développement

Trois options sont disponibles pour vos moniteurs : les modes développement, simulation et production. Testez toujours vos scripts en mode développement avant de passer au mode simulation ou production. Cet article sur les [modes des moniteurs]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}) vous apportera de plus amples informations à ce sujet.

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Transactions > Gérer les transactions {{< /AppElement >}}.
2. Ouvrez le moniteur de transaction qui a été chargé par l'enregistreur de transaction.
3. Assurez-vous d'ouvrir l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}.
4. Dans la section *Statut*, choisissez le *mode* "Développement".
5. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}}.

{{< callout >}}
**Astuce :** Maintenez la touche \[Ctrl\] enfoncée tout en cliquant sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour garder ouverte la fenêtre du moniteur. Autrement, l'enregistrement des modifications vous ramène à la vue d'ensemble des *moniteurs*.
{{< /callout >}}

## Commencer le test avec "Tester maintenant"

Que ce soit pour utiliser un script tiré de l'enregistreur de transaction, pour modifier un script existant ou pour corriger des erreurs dans un script en production, vous utiliserez le bouton {{< AppElement type="savebutton" >}} Tester maintenant {{< /AppElement >}}. Ce bouton vous permet de réaliser rapidement un test pour vérifier si le script contient des erreurs.

1. Ouvrez le moniteur de transaction créé pour ce tutoriel.
2. Cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} Tester maintenant {{< /AppElement >}} au bas de la page. La fenêtre contextuelle *Tester depuis :* s'affiche.
3. Choisissez le checkpoint depuis lequel effectuer le test.
4. Cliquez sur {{< AppElement type="button" >}} Tester maintenant {{< /AppElement >}}.

{{< callout >}}
**Important** : La réussite d'un test en mode développement n'indique pas que le script de transaction est stabilisé. Suivez toutes les recommandations relatives aux tests avant de faire passer un script de transaction en mode production.
{{< /callout >}}

Une fois le test lancé, l'éditeur revient automatiquement en haut de la page et le checkpoint ajoute votre moniteur à la file d'attente. Vous pouvez alors suivre la progression du checkpoint dans les étapes du script. La réussite de votre test est une première bonne étape, mais d'autres tests doivent aussi être effectués.

Si vous utilisez le modèle de script, vous remarquerez que l'*Étape 1* (navigation) et l'*Étape 2* (clic sur un élément) réussissent, mais que l'*Étape 3* échoue au point 3.3.

![Capture d'écran de l'échec du test](/img/content/scr_transaction-tutorial-failedTest.min.png)

{{< callout >}}
**Remarque :** Si vous réalisez un test manuel avec le bouton {{< AppElement type="savebutton" >}} Tester maintenant {{< /AppElement >}}, les résultats du test incluent des graphiques en cascade et des captures d'écran utiles pour le débogage. Cliquez sur le bouton {{< AppElement type="button" >}}Résultats de test disponibles{{< /AppElement >}} pour les afficher. Lors du passage au mode simulation ou production, seuls les utilisateurs possédant un compte Business ou Enterprise peuvent choisir d'ajouter les graphiques en cascade et les captures d'écran aux étapes.
{{< /callout >}}

## Corriger le script

En mode développement, une transaction peut échouer pour de nombreuses raisons telles qu'un contenu manquant ou le choix d'un sélecteur inadapté pour les éléments, les onglets et les cadres. Les problèmes de délais et les interactions manquantes peuvent aussi causer des erreurs. Les astuces suivantes vous indiquent comment résoudre les problèmes les plus fréquents.

### Problème : Élément non trouvé en raison d'un ID dynamique

Avec l'exemple de script de test, vous pouvez voir dans les résultats de test que le moniteur n'a pas trouvé l'élément spécifié dans le sélecteur CSS. L'action indique au checkpoint de changer la quantité, mais elle échoue car le moniteur ne trouve pas l'élément en question. L'article [Sélecteurs alternatifs]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}) contient plus d'informations sur les sélecteurs.

![Capture d'écran de l'action échouée](/img/content/scr_transaction-tutorial-failedstep.min.png)

Le sélecteur CSS complet indique :

`#quantity_6346b8b92ac97`

Le moniteur cherche donc sur la page un élément dont l'ID est "quantity\_6346b8b92ac97" pour définir la valeur de l'élément sur "2". Toutefois, l'élément avec l'ID "quantity\_6346b8b92ac97" n'apparaît jamais. Pourquoi ? Le sélecteur cherche un ID spécifique, mais le serveur génère l'ID d'élément de façon dynamique. À chaque chargement de la page, le serveur donne un autre ID à l'élément. Pour corriger cela, l'élément peut être identifié autrement qu'avec son ID.

### Solution : Utiliser un autre sélecteur

Pour contourner le problème lié à l'ID dynamique, il faut choisir un autre sélecteur. Pour consulter la liste des sélecteurs disponibles, cliquez sur le bouton {{< AppElement type="button" >}}…{{< /AppElement >}} dans la zone de sélection du sélecteur.

![Capture d'écran montrant les détails de l'échec](/img/content/scr_transaction-tutorial-failedstep-detail.min.png)

Une fenêtre contextuelle montrant les [autres sélecteurs disponibles]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}) s'ouvre :

![Sélecteurs alternatifs](/img/content/scr_transaction-tutorial-alternativeselectors.min.png)

Dans le cas présent, vous remarquerez que plusieurs des sélecteurs utilisent la valeur créée dynamiquement. Vous pouvez donc écarter ces choix-là. Deux options n'incluent pas l'ID dynamique : *name* et *xpath:idRelative*. L'enregistreur choisit automatiquement les sélecteurs d'après ce qui lui semble la meilleure option. Dans ce cas, la deuxième recommandation (“name”) pourrait être plus indiquée pour identifier l'élément. Le nom est un attribut de l'élément. Si cette valeur est propre à cette page, le sélecteur "name" sera probablement le meilleur choix.

Ici, il s'avère que l'option *xpath:idRelative* fonctionnerait aussi. Uptrends vous propose deux choix qui fonctionneront en mode développement, mais il vous faudra aussi les tester en mode simulation. Mais nous n'en sommes pas encore là.

### Problème : Élément non trouvé en raison de l'absence d'une interaction de l'utilisateur

Tout comme les ID dynamiques, le contenu dynamique qui nécessite une interaction de l'utilisateur pour afficher un élément peut aussi poser problème. Il n'est pas toujours facile de trouver ces problèmes, et nous vous conseillons de bien examiner les détails des interactions.

### Solution : Ajouter une action de survol

Certains éléments de page ne se chargent pas ou ne s'affichent pas tant que l'utilisateur ne survole pas l'élément avec le curseur. Par exemple, si un utilisateur doit survoler un menu pour rendre les sous-menus visibles et accessibles, le script doit aussi réaliser cette action de survol. Toutefois, l'enregistreur de transaction ne peut pas enregistrer les survols et, si un élément n'est pas visible sur la page, le script ne peut pas interagir avec cet élément. Vous devez donc ajouter une action de survol avant l'interaction concernée. Notre article sur les [actions de survol]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="fr" >}}) et leur configuration contient plus d'informations à ce sujet.

### Problème : Erreur due à une expiration de délai

Lors de son exécution, le script surveille et attend constamment que les éléments se chargent. Le temps d'attente par défaut est de 30 secondes, et suffit généralement largement. Toutefois, si ce délai ne suffit pas, il est parfois utile de pouvoir ajouter du temps d'attente à une action. Pour en savoir plus sur les conditions d'attente, lisez notre article [Comment utiliser les conditions d’attente]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}).

### Causes et solutions (possibles) pour les problèmes de délais

Les problèmes de délais peuvent présenter plusieurs causes et plusieurs solutions.

- **L'élément n'est pas encore interactif** : prolongez le temps d'attente.
- **Le délai de la transaction a expiré** : la transaction est assortie d'un délai d'exécution maximal. [Contactez le support]({{< ref path="contact" lang="fr" >}}) qui examinera votre script pour trouver le problème.

{{< callout >}}
**Important :** Nous ne pouvons qu'insister sur l'importance des vérifications de contenu pour la réussite de votre monitoring de transactions. Pensez à ajouter une vérification de contenu après chaque action de navigation ou d'actualisation du contenu. Utilisez-les avant chaque interaction. Les [vérifications de contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}) sont gratuites, et renforcent votre monitoring.
{{< /callout >}}

### Problème : Erreurs dans les actions Définir

Tout clic manquant avant une [action Définir]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="fr" >}}) peut causer des erreurs. Évitez les erreurs en intégrant toujours une [action de clic]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="fr" >}}) à chaque interaction de type Définir.

### Solution : Ajouter des actions de clic

**N'utilisez pas la touche Entrée** : Lors de l'enregistrement de votre transaction, vous avez peut-être utilisé la touche Entrée au lieu de cliquer sur le bouton d'envoi. Par exemple, quand vous utilisez une fonction de recherche, il est probable que vous pressiez naturellement la touche Entrée plutôt que de cliquer sur le bouton de recherche. L'enregistreur ne peut pas capter l'utilisation de la touche Entrée. Si vous avez pressé la touche Entrée pendant l'enregistrement, ajoutez une action de clic. Si vous n'avez pas d'option de bouton à cliquer, [contactez le support]({{< ref path="contact" lang="fr" >}}) qui vous aidera à trouver une solution.

**Clics manquants** : Ne retirez pas les clics qui ont lieu avant la saisie de valeurs dans les champs. Les clics activent des actions de saisie ainsi que d'autres événements dans le navigateur. Dans certains cas, deux clics doivent être ajoutés avant la saisie d'une valeur.

Pour en savoir plus, lisez notre article sur les [actions de clic]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="fr" >}}).

## Checklist pour les tests de script

Avant de faire passer votre moniteur de transaction en mode simulation, il y a plusieurs points à vérifier.

- **Intégration des [vérifications de contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}).** Assurez-vous qu'une vérification de contenu figure après chaque transition de page pour vérifier que la page charge le contenu attendu.
- **Consultez les [captures d'écran et les graphiques en cascade]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}}).** En mode développement, chaque étape génère une capture d'écran de la fenêtre du navigateur et un graphique en cascade. Assurez-vous de consulter les graphiques en cascade et les captures d'écran pour vérifier le parcours, le contenu et l'adéquation des produits ou articles.
- **Lisez nos [mises en garde sur le monitoring transactionnel]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="fr" >}}).** Assurez-vous que votre monitoring n'aura pas de conséquences négatives pour votre entreprise ou organisation.
- **Vérifiez que des [actions de clic]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#click" lang="fr" >}})** ont été ajoutées avant la saisie de valeurs dans les zones textuelles.

## Passer au mode simulation

Une fois votre code ajusté et testé en mode développement, l'étape suivante consiste à passer au mode simulation. Pour en savoir plus, lisez notre article sur les [modes des moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}})).

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Transactions > Gérer les transactions {{< /AppElement >}}.
2. Ouvrez le moniteur de transaction créé pour ce tutoriel.
3. Assurez-vous d'ouvrir l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}.
4. Définissez le **mode** sur "Simulation".
5. Définissez le moniteur comme **Activé** en cliquant sur la case à cocher.
6. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}}.

Il est conseillé d'exécuter votre nouveau moniteur de transaction en mode simulation pendant quelques semaines afin de tester sa stabilité, particulièrement après les actualisations du site. Ouvrir les tests au réseau de checkpoints élargi peut aussi occasionner des problèmes de localisation.

Les tests en mode simulation ne génèrent pas d'alerte, mais vous pouvez consulter les journaux des moniteurs et le dashboard des **transactions** pour vérifier si votre moniteur a rencontré des erreurs. Dans le *Journal moniteurs* (et d'autres dashboards), une icône représentant une fiole s'affiche à côté des moniteurs en mode simulation.

![Capture d'écran du journal de moniteurs](/img/content/scr_transaction-tutorial-stagingmode.min.png)


Vous pouvez cliquer sur l'horodatage de l'erreur pour ouvrir le rapport [Voir les détails]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/making-sense-of-your-transaction-dashboards-and-reports#tutorial-check-details" lang="fr" >}}) et obtenir des informations sur le déroulement de la transaction jusqu'à l'apparition de l'erreur.