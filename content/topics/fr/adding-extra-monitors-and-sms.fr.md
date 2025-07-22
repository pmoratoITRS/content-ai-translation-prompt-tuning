{
"hero": {
"title": "Ajout de moniteurs et de crédits"
},
"title": "Ajout de moniteurs et de crédits de message",
"summary": "Si vous avez besoin d'ajouter des moniteurs, des crédits d'API, des crédits de transaction ou des crédits de message, vous pouvez nous contacter ou les acheter directement depuis votre compte Uptrends.",
"url": "/support/kb/compte/paiements-et-abonnements/ajout-de-moniteurs-et-de-credits-sms-supplementaires",
"translationKey": "https://www.uptrends.com/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms"
}

## Crédits

Uptrends utilise des crédits pour calculer le [prix]({{< ref path="/pricing" lang="fr" >}}) de ses différents services de monitoring. Les crédits sont nécessaires pour créer et configurer des moniteurs, et planifier leur exécution.

Chaque moniteur synthétique, comme les [moniteurs de disponibilité et les moniteurs de base]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}), les [moniteurs de navigateur (Full Page Check ou FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="fr" >}}), les [moniteurs d'API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) et les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}), utilise son propre type de crédit :

- Les moniteurs de disponibilité utilisent des **crédits de disponibilité**.
- Les moniteurs de navigateur utilisent des **crédits de navigateur**.
- Les moniteurs d'API utilisent des **crédits d'API**.
- Les moniteurs de transactions utilisent des **crédits de transaction**.
- **Crédits** : ce système s'applique uniquement aux comptes qui sont abonnés au forfait incluant une seule réserve de crédit.

Le nombre total de crédits dépend du [mode du moniteur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}) et des [paramètres du moniteur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="fr" >}}). Les moniteurs en mode **Simulation** et **Production** utilisent des crédits. Les moniteurs en mode **Développement** sont considérés comme inactifs et n'utilisent pas de crédits.

Si vous manquez de crédits, vous pouvez facilement [acheter des crédits supplémentaires]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms#add-credits" lang="fr" >}}) ou créer et exécuter vos moniteurs en [mode Développement]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode#development-mode" lang="fr" >}}).

## Calcul des crédits

Pour voir l'état des crédits de tous vos moniteurs synthétiques, ouvrez {{< AppElement type="menuitem" >}} Configuration de compte > Abonnement et factures {{< /AppElement >}}. Le graphique circulaire indique vos crédits pour chaque type de moniteur :

![Crédits des moniteurs](/img/content/scr-monitor-credits.min.png)

Dans l'exemple illustré, l'utilisateur a acheté cinq moniteurs ou **crédits de navigateur**. Deux sont actuellement en utilisation, et trois autres moniteurs FPC peuvent encore être créés. De même, pour les **crédits de disponibilité**, l'utilisateur a acheté 10 moniteurs ou crédits de disponibilité. Quatre sont actuellement en utilisation, et six autres moniteurs de base peuvent encore être créés.

Pour les moniteurs de transactions et d'API, le calcul des crédits est légèrement plus complexe. Les crédits ne correspondent pas à des moniteurs, mais à chaque requête ou chargement de page vérifié par le moniteur.

Si vous avez créé un moniteur d'API (API multi-étapes [MSA] ou Postman), chaque requête HTTP correspond à un crédit. Si vous avez créé un moniteur MSA comprenant trois étapes, cela utilise trois crédits. Si vous avez créé deux moniteurs MSA comprenant chacun trois étapes, le nombre total de crédits utilisés correspondra aux trois étapes du premier moniteur MSA et aux trois étapes du deuxième moniteur MSA, soit six crédits d'API au total.

Il en va de même pour les moniteurs de transactions : nous comptons un crédit pour chaque nouvelle requête (chargement de page), [graphique en cascade ou pellicule]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}}). Si un moniteur de transaction parcourt quatre pages (nouveaux chargements de pages) et que le graphique en cascade et la pellicule sont activés pour la première étape, le calcul sera le suivant : quatre crédits pour les chargements de page + un crédit pour le graphique en cascade + un crédit pour la pellicule. Soit six crédits de transaction au total. Pour en savoir plus sur les crédits de transaction, lisez l'article [Comprendre le calcul du nombre de crédits utilisés par les moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="fr" >}}).





## Ajout de crédits

Pour surveiller des sites web, des serveurs, des transactions et des services web supplémentaires, vous pouvez acheter de nouveaux crédits des deux façons suivantes :

1. **Nous contacter**  
   Si vous avez déjà un abonnement et que vous voulez vous assurer d'avoir le bon nombre de nouveaux moniteurs ou crédits de message à un tarif compétitif, contactez directement votre représentant commercial ou [soumettez un ticket](/contact).

2. **Ajouter des crédits depuis l'application web d'Uptrends**
   1. Ouvrez {{< AppElement type="menuitem" >}} Configuration de compte > Acheter des extras {{< /AppElement >}}.
   2. Vous pouvez augmenter le nombre de crédits de disponibilité, de navigateur, d'API, de transaction et de message disponibles pour votre compte.
   3. Cliquez sur {{< AppElement type="buttonPrimary" >}} Suivant {{< /AppElement >}}.
   4. Indiquez vos informations de facturation et choisissez la **méthode de paiement** souhaitée.
   5. Cliquez sur {{< AppElement type="savebutton" >}} Confirmer la commande {{< /AppElement >}}.
