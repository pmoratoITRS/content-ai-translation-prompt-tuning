{
"hero": {
"title": "Mises en garde et astuces"
},
"title": "Mises en garde et astuces",
"summary": "Lorsque vous configurez des moniteurs de transactions, vous devez prêter attention à un certain nombre de choses.",
  "url": "/support/kb/surveillance-synthetique/transactions/mises-en-garde-et-astuces-pour-le-monitoring-transactionnel",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-monitoring-caveats-tips-and-tricks"
}

La surveillance des transactions (ou monitoring des applications web) peut préserver la réputation de votre marque et entraîner des économies de coûts grâce à l'identification des problèmes touchant vos transactions. Il s'agit d'une approche de surveillance synthétique qui consiste à faire exécuter un script par les checkpoints d'Uptrends pour simuler les parcours réels des utilisateurs. Lors de la configuration des tests de parcours utilisateur, il est important de réfléchir aux conséquences à court et à long terme de vos tests. Vous pouvez éviter de nombreux problèmes en élaborant soigneusement votre transaction avant l'enregistrement. Même si chaque cas client est différent, nous avons répertorié quelques problèmes courants sur lesquels nous souhaitons attirer votre attention en vue de la configuration de la surveillance de vos transactions.

## Évitez les pénuries de stock

Le test des paniers d'achats et des transactions de paiement peut entraîner des problèmes avec votre inventaire et induire des pénuries. Le test synthétique génère jusqu'à 288 commandes par jour. S'il n'est pas géré correctement, il peut donc réduire artificiellement votre stock et rendre l'article indisponible pour vos utilisateurs. Nous avons même observé des situations où l'entrepôt a traité et préparé les commandes d'expédition.  Voici plusieurs solutions pour éviter les problèmes d'inventaire.

**Configurer la base de données**

Bien que certaines entreprises choisissent de supprimer manuellement les achats et les paniers d'achats dus aux tests dans la base de données, la mise en place d'une procédure stockée ou d'un processus automatisé semble plus fiable. Par exemple, votre système de traitement des commandes peut ignorer les commandes passées par l'utilisateur test ou les commandes passées depuis les [adresses IP des checkpoints]({{< ref path="checkpoints" lang="fr" >}}) d'Uptrends.

**Utiliser des articles de test (virtuels)**

Il peut être intéressant de créer un article d'inventaire qui sera utilisé strictement à des fins de test. L'utilisation d'un article de test permet de préserver la précision et la disponibilité de votre inventaire réel. Les articles de test peuvent également vous aider à identifier les transactions de test lorsque vous purgez vos bases de données, et éviter l'envoi accidentel d'articles réels.

**Vider le panier**

Lors du test d'une transaction de panier, prévoyez la suppression des articles dans les étapes de la transaction. Ajoutez un article, puis supprimez l'article avant de fermer la transaction.

{{< callout >}}
**Remarque** : La suppression d'articles du panier préservera la disponibilité de vos produits pour votre clientèle. Cependant, lorsque la transaction échoue avant que le script ne supprime l'article du panier, des articles peuvent s'y accumuler. Il vous faudra donc surveiller fréquemment le panier pour effacer les articles au moyen de l'utilisateur test.
{{< /callout >}}

**Choisissez un article disponible en grandes quantités**

Si vous utilisez un article réel, choisissez un article à tester qui existe dans une telle quantité qu'une pénurie de stock devient presque impossible.

## Gardez un œil sur les systèmes de réapprovisionnement

Le logiciel de gestion des stocks intègre souvent un processus qui réapprovisionne automatiquement les articles les plus vendus ou les articles qui viennent à manquer. Pour éviter toute surabondance d'un article dans votre inventaire, consultez les administrateurs système pour déterminer la meilleure méthode. Par exemple, vous pouvez décider d'utiliser un article de test ou de désactiver le réapprovisionnement automatique d'un article donné.

## Évitez tout engorgement de votre agenda

Si votre moniteur de transaction teste un planificateur de rendez-vous médicaux, de chambres d'hôtel, de vols ou de réservations au restaurant, tous vos créneaux horaires peuvent être rapidement pris ou indisponibles. Il est donc crucial d'identifier et de supprimer les rendez-vous créés par les tests.

## Souvenez-vous que votre moniteur de transaction envoie des e-mails

Si une partie de votre transaction inclut un champ de courrier électronique et que votre transaction inclut l'envoi d'e-mails de confirmation pour différentes raisons (factures, réinitialisation de mots de passe ou rappel d'identifiants), sachez que votre moniteur de transactions enverra ces e-mails. Pour éviter que votre boîte aux lettres se remplisse de ces e‑mails indésirables, utilisez une adresse e-mail comme noreply@mysite.com pour votre moniteur de transaction.

## Évitez des frais imprévus

Si vous utilisez une carte de crédit réelle lors des tests de paiement, vous risquez de payer des frais et des commissions, de bloquer des fonds disponibles et de déclencher des alertes pour fraude en raison de la fréquence des transactions. Pour éviter cela, pensez à utiliser des comptes de test de carte de crédit. La plupart des prestataires de services de paiement proposent des numéros de compte de test qui vous permettent de tester le paiement sans générer des frais ou bloquer un compte réel.

## Contournez les problèmes liés à la création d'un nouveau compte

Lorsque vous testez une nouvelle configuration de compte, vous ne pouvez le faire qu'une seule fois avec le même nom d'utilisateur. La deuxième fois que le script s'exécute, la transaction génère une erreur liée au compte en double. Nous avons répertorié différentes solutions pour tester la configuration du compte.

### Ne validez pas les données

Bien que cette option ne fournisse pas un test complet de la configuration complète du compte, certains utilisateurs d'Uptrends ont choisi d'arrêter la transaction avant la validation finale. Le moniteur teste tous les aspects du processus de création de compte, à l'exception de l'envoi final.

### Configurez votre base de données

Vous pouvez envisager d'utiliser un déclencheur depuis une base de données pour vérifier l'ID de compte de test après un événement CREATE qui purge le compte de test de la base de données avant le début du test suivant.

### Générez de nouvelles connexions uniques

Vous pouvez également générer de nouvelles connexions uniques en utilisant par exemple l'horodatage. N'oubliez pas de les purger régulièrement. [Contactez le support]({{< ref path="contact" lang="fr" >}}) pour en savoir plus.

## Évitez les problèmes liés à un compte déjà connecté

Si vous utilisez les mêmes informations de connexion pour plusieurs moniteurs ou si vous ne vous déconnectez pas après un test, vous risquez de générer des erreurs. Une bonne pratique consiste à configurer un compte d'utilisateur de test différent pour chaque moniteur et à vous déconnecter à la fin du processus de test pour éviter les alertes inutiles.

## Protégez les informations sensibles

Si un utilisateur doit se connecter pour réaliser une tâche, il en va de même pour le moniteur. Étudiez le processus d'authentification et protégez les identifiants de connexion et les mots de passe. Vous pouvez protéger vos informations d'authentification dans notre [coffre-fort]({{< ref path="support/kb/account/vault" lang="fr" >}}), et les masquer dans les résultats de test.

Par ailleurs, prenez garde aux autorisations que vous accordez à l'utilisateur test, et gardez un œil sur cet utilisateur pour repérer toute activité anormale.

## Utilisez les vérifications de contenu

Les [vérifications de contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}) sont gratuites. Vous pouvez en ajouter une à chaque étape de votre transaction. Ces contrôles sont un excellent moyen de s'assurer que la page est chargée complètement et que le navigateur a reçu le bon contenu. Il existe trois façons d’ajouter une vérification de contenu. Vous pouvez utiliser le bouton *Ajouter une vérification de contenu* ou le menu contextuel. Les vérifications de contenu peuvent aussi être ajoutées ultérieurement au moyen de l’éditeur d’étape du moniteur disponible dans votre compte. Reportez-vous au [tutoriel sur le parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}) pour apprendre à utiliser les vérifications de contenu dans des situations réelles.

## Utilisez les actions de clavier
L’enregistreur de transaction vous permet d’enregistrer les actions de clavier de l’utilisateur. Vous avez le choix entre différents caractères, dont les touches de contrôle, les touches spéciales. les touches numériques, les touches du pavé numériques, les touches majuscules et les touches minuscules. Indiquez si la sélection de cette touche doit s’appliquer tout le temps ou seulement sur l’élément qui vous intéresse ou le dernier élément cliqué.

Cette fonctionnalité est pratique lorsqu’un site Web propose des instructions telles que *Appuyez sur n’importe quelle touche pour continuer* ou *Appuyez sur Entrée pour confirmer*. Cependant, contrairement aux actions reposant sur un clic de souris (qui sont automatiquement enregistrées comme un mouvement), vous devez ajouter manuellement l’action de clavier pour qu’elle soit enregistrée comme une activité réelle. Reportez-vous au [tutoriel sur le parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}) pour en savoir plus sur les actions de clavier.

## Utilisez les actions Survol et Attendre que l'élément soit visible

Vous pouvez aussi enregistrer les actions de survol de souris et vérifier si un élément est visible en effectuant un clic droit sur un élément de la page, puis en choisissant l’option adéquate dans le menu contextuel *ITRS Uptrends Transaction Recorder*. Cette fonctionnalité vous sera utile pour vérifier si un élément déclenche certaines actions lors d’un survol avec la souris, comme l’affichage d’un message, d’un élément ou de sous-menus. Reportez-vous au [tutoriel sur le parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}) pour consulter des exemples réels.

{{< callout >}}
**Remarque :** Chaque cas client est différent, alors n'hésitez pas à contacter nos spécialistes de script pour vous aider à trouver des solutions adaptées à votre situation. Vous pouvez utiliser le [système de tickets]({{< ref path="contact" lang="fr" >}}) ou ajouter un commentaire à votre enregistrement de transaction pour informer notre équipe de votre besoin.
{{< /callout >}}
