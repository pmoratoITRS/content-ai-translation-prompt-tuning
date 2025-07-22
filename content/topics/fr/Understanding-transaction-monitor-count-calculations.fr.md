{
"hero": {
"title": "Comprendre le calcul du nombre de crédits utilisés par les moniteurs de transactions"
},
"title": "Comprendre le calcul du nombre de crédits utilisés par les moniteurs de transactions",
"summary": "Cet article vous explique comment nous calculons le nombre de crédits utilisés pour votre transaction.",
"url": "/support/kb/surveillance-synthetique/transactions/comprendre-calcul-nombre-moniteurs-transactions",
"translationKey": "https://www.uptrends.com/support/kb/transactions/Understanding-transaction-monitor-count-calculations"
}

Si vous vous demandez comment Uptrends détermine le coût d’un moniteur de transaction, vous êtes au bon endroit. Avant d’aborder le calcul du nombre de crédits utilisés, passons en revue certains termes fréquemment utilisés au sujet des moniteurs de transactions.

**Transaction** : la transaction correspond au parcours de navigation emprunté par un utilisateur pour effectuer une tâche sur votre site web. Les transactions comprennent des tâches telles que se connecter, effectuer un achat, envoyer un formulaire, demander un document, configurer un compte, demander une réinitialisation du mot de passe, etc. Chaque transaction se compose de deux étapes ou plus.

**Crédit de transaction** : vous pouvez envisager le crédit de transaction comme de l’argent. Selon votre abonnement, vous disposez d’un certain nombre de crédits de transaction (qui peut toujours être complété). Chaque moniteur de transaction a un "coût" qui correspond à un certain nombre de crédits, en fonction de différents facteurs présentés dans cet article. Tant que votre moniteur est en mode développement, aucun crédit n’est utilisé ou nécessaire. Les crédits sont utilisés lorsque le moniteur est en mode simulation ou production (pour en savoir plus, vous pouvez lire notre article sur les [modes des moniteurs]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}).).



Vous trouverez le nombre de crédits disponibles dans les paramètres de votre compte.

**Action utilisateur** : ce terme désigne une interaction de l’utilisateur avec la page. Par exemple, il peut s'agir des clics, de la saisie de texte, des actions de survol et des vérifications de contenu.

**Étape** : une étape est un regroupement arbitraire d’actions utilisateur. Vous pouvez regrouper vos actions en formant des étapes qui vous semblent pertinentes et qui vous aideront à résoudre les problèmes et à générer des rapports. Pour vous guider dans la configuration des étapes, sachez qu'Uptrends fournit la durée de chaque étape. Nous vous recommandons de terminer chaque étape par une action qui déclenche le chargement d’une nouvelle page et une vérification de contenu.

## Comment Uptrends détermine-t-il le nombre de crédits utilisés par un moniteur de transaction ?

Nous calculons le nombre de crédits de transaction utilisés par transaction en fonction de deux facteurs :

**Le nombre d’actions utilisateur qui déclenchent une requête serveur** : chaque action utilisateur (voir la définition ci-dessus) qui est configurée dans un moniteur de transaction et qui aboutit à une requête serveur utilise un crédit de transaction. Ainsi, les actions de navigation, les téléchargements de fichiers et les clics qui chargent de nouvelles pages dans le navigateur utilisent tous un crédit. La saisie de texte, les actions de survol et les vérifications de contenu sont gratuites.

**Cascades de transaction, pellicules et captures d’écran** : chaque cascade de transaction ou capture d’écran utilisée dans votre transaction utilise un crédit de transaction. Les pellicules coûtent un crédit de transaction, à moins que l'étape contienne déjà une capture d'écran, auquel cas la pellicule n'utilise pas de crédit de transaction. Deux captures d'écran et une pellicule coûtent deux crédits de transaction.

## Mode de calcul du nombre de crédits utilisés par les moniteurs de transaction

Voici une formule pour calculer le nombre de crédits requis pour une seule transaction :

**Nombre d’actions avec requêtes serveur** + **nombre de graphiques en cascade** + **nombre de captures d’écran** = **nombre total de crédits de transaction utilisés**

**Remarque** : dans la liste des moniteurs, lorsque vous ajoutez un nouveau moniteur ou que vous modifiez un moniteur, le nombre de crédits s’affiche, suivi de l’indication "en calcul" ou "calculé". Le système a besoin de quelques instants pour analyser les étapes de votre transaction afin de déterminer le coût exact. Dans certains cas, notre équipe d’assistance examine le nouveau moniteur, ou le moniteur qui a été modifié, pour vérifier que le nombre de crédits appliqué au moniteur est juste.

## Conclusion

Si vous avez un doute sur la façon dont nous avons calculé les crédits utilisés pour une transaction, [contactez le support](/contact). Notre équipe d’assistance examinera la transaction avec vous pour que tout soit clair.
