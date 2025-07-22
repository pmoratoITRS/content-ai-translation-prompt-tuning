{
"hero": {
"title": "Vue d'ensemble de la surveillance des transactions"
},
"title": "Vue d'ensemble de la surveillance des transactions",
"url": "/support/kb/surveillance-synthetique/transactions/apercu-du-suivi-des-transactions",
"translationKey": "https://www.uptrends.com/support/kb/transactions/transactions-overview",
"sectionlist": false
}

La surveillance des transactions, également connue sous le nom de surveillance des applications web, est utilisée pour vérifier le bon fonctionnement des interactions des utilisateurs de votre site web. L'interaction peut être une simple connexion ou toutes les actions nécessaires à l'achat d'un produit dans votre boutique en ligne.

Pour surveiller ces interactions d'utilisateurs, il faut les placer dans un script qui peut être exécuté à plusieurs reprises pour vérifier si tout fonctionne toujours comme prévu. Uptrends fournit un enregistreur de transaction (en tant qu'extension Chrome) pour construire un script de manière simple. Une fois que vous avez enregistré le script, vous pouvez l'affiner vous-même (transactions en libre-service) ou demander au support Uptrends de l'affiner (transactions en service complet). Si vous savez écrire les scripts, vous pouvez décider d'omettre l'enregistrement et placer directement votre propre script dans un moniteur de transaction.

Lorsque vous chargez l'enregistrement d'une transaction vers votre compte Uptrends, un moniteur de transaction est créé avec quelques informations de base. Il vous faut ensuite ajuster certains paramètres en fonction de vos besoins.

Une fois que vous avez testé votre moniteur de transaction et que son fonctionnement vous convient, mettez en place des [alertes]({{< ref path="support/kb/alerting" lang="fr" >}}) pour ce moniteur. Après tout, c'est de cela qu'il s'agit : recevoir des alertes lorsque quelque chose ne fonctionne pas comme prévu.

{{< callout >}}
Notre tutoriel [Parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop" lang="fr" >}}) vous guide pas à pas dans la mise en place de la surveillance des transactions et la vérification des données de surveillance.
{{< /callout >}}

## 1. Introduction

Si vous débutez dans la surveillance des applications/transactions web, les articles suivants vous donneront de bonnes bases :

- Apprenez le B.A.BA en lisant l'article [Qu'est-ce que la surveillance de site web ?]({{< ref path="what-is/web-application-monitoring" lang="fr" >}})
- Découvrez [pourquoi vous avez intérêt à utiliser la surveillance d'applications web]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#why-monitor-your-web-applications" lang="fr" >}}).
- Vérifiez si la surveillance des applications web est [la bonne solution]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#transaction-best-choice" lang="fr" >}}) pour vous.

## 2. Planifier la surveillance de vos transactions

Comprendre la mécanique de vos transactions, les fonctionnalités à tester et l'impact de la surveillance sur vos systèmes est une part cruciale de la planification de vos transactions. Il sera peut-être également nécessaire d'impliquer d'autres équipes de votre entreprise dans la mise en place d'une surveillance des transactions.

- [Cartographiez les différents chemins de transaction possibles]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="fr" >}}).
- Déterminez [ce que vous allez tester]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="fr" >}}).
- Lisez nos [mises en garde et astuces]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="fr" >}}) qui recensent les éléments à prendre en compte et à surveiller lors de la mise en place de votre surveillance.
- Sachez [dans quels cas]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#programming-skills" lang="fr" >}}) vous pourriez avoir besoin de l'aide d'autres équipes de votre entreprise.

## 3. Enregistrer vos transactions

Une utilisation correcte de l'[enregistreur de transaction]({{< ref path="features/transaction-recorder" lang="fr" >}}) donne des enregistrements plus propres et une configuration du moniteur plus efficace.

- [Téléchargez et utilisez l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}})
- Apprenez à utiliser l'enregistreur de transaction en suivant le [tutoriel sur le parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}).
- Choisissez les [transactions en libre-service ou en service complet]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="fr" >}}).

## 4. Tester et modifier vos scripts de transaction

Une fois votre transaction enregistrée et le moyen de tester le script choisi (par vous-même ou par notre équipe de support), vous devez résoudre les problèmes dans le script, configurer les vérifications de contenu si ce n'est pas déjà fait, et définir les autorisations du coffre-fort sur les éléments nouvellement créés. Enfin, vous devez suivre de près le moniteur en mode "simulation" avant de le déplacer vers la production.

- Pour en savoir plus sur l'éditeur, les étapes et les actions, lisez l'article [Comprendre l'éditeur d'étapes]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}})

- Les actions sont au cœur des transactions. Apprenez-en plus à leur sujet dans les articles suivants :
   - [Interactions de page : naviguer, cliquer, définir, etc.]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="fr" >}})
   - [Actions de test : vérifications de contenu et délais d'attente]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}})
   - [Actions de contrôle : changement de cadre (intégré) ou d'onglet]({{< ref path="support/kb/synthetic-monitoring/transactions/Switching-between-iframes-browser-tabs" lang="fr" >}})
   - [Actions de contrôle : ajustement du contenu d'une variable]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="fr" >}})
   - [Ignorer les erreurs pour les étapes et actions facultatives]({{< ref path="support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="fr" >}})
   - [Utilisation des sélecteurs]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="fr" >}}) et des [sélecteurs alternatifs]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}})
   - [Utilisation de variables dans les transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="fr" >}}) et [ajustement des variables de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="fr" >}})

- Dans l'exercice [Tester et modifier votre script de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="fr" >}}), vous pouvez expérimenter la fonction *Tester maintenant* et apprendre à gérer les erreurs liées aux ID dynamiques et à l'expiration des temps d'attente. Cet exercice contient également une [checklist pour le test]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction#script-testing-checklist" lang="fr" >}}).

- En fonction de votre configuration et de vos transactions, vous aurez peut-être à gérer également :
   - [Les valeurs sensibles]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="fr" >}}) qui ont été automatiquement ajoutées au coffre-fort lors de l'enregistrement
   - [Les autorisations du coffre-fort (sections créées automatiquement)]({{< ref path="support/kb/synthetic-monitoring/transactions/managing-authorizations-for-automatically-created-vault-sections" lang="fr" >}})
   - La surveillance des transactions pour les [appareils mobiles]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup" lang="fr" >}})
   - L'utilisation d'un [DOM fantôme]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}) pour votre transaction
   - L'utilisation de la [double authentification par SMS]({{< ref path="/support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="fr" >}}) ou de la [double authentification basée sur un mot de passe à usage unique]({{< ref path="/support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="fr" >}}) pour votre transaction

   - L'ajout de [métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}}) telles que les [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) et les [durées de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}) aux résultats relatifs à vos transactions

   - Le contournement ou le remplacement du système DNS classique par l'application d'un [contournement DNS]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="fr" >}}) à votre transaction

## 5. Résultats de la surveillance des transactions

Une fois vos transactions surveillées, vous recevrez des retours. En cas de problème, plusieurs ressources peuvent vous aider à comprendre ce qui ne va pas.

- [Les captures d'écran]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-screenshots" lang="fr" >}})

- [Les graphiques en cascade]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}})

- [Les durées de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}})

- [Les Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}})

- [L'analyse des erreurs]({{< ref path="support/kb/synthetic-monitoring/transactions/analyzing-transaction-errors" lang="fr" >}})

## 6. Dépannage

Lorsque la surveillance des transactions ne fonctionne pas comme prévu, voici quelques points à vérifier :

- [Excluez les tests A/B]({{< ref path="support/kb/synthetic-monitoring/transactions/exclude-a-b-tests-from-transaction-requests" lang="fr" >}})

- [Utilisez le mode de navigation privée]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-incognito-mode" lang="fr" >}})

- [Lisez nos mises en garde et astuces]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="fr" >}})

## Crédits

Créer des moniteurs de transactions et planifier leur exécution utilisent des crédits de transaction. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}).
