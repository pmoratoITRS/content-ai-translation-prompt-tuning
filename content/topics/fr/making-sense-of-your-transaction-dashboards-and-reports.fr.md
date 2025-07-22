{
"hero": {
"title": "Comprendre les données relatives à vos transactions"
},
"title": "Comprendre les données relatives à vos transactions",
"summary": "Une fois que votre moniteur de transaction est opérationnel, vous commencez à obtenir des rapports détaillés et vos dashboards se remplissent avec des données. Cet exercice vous aidera à comprendre à quoi ces données correspondent.",
"url": "/support/kb/surveillance-synthetique/transactions/tutorial-record-user-journey-in-shop/comprendre-dashboards-et-rapports-sur-transactions",
"translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/making-sense-of-your-transaction-dashboards-and-reports"
}

Les données collectées lors du monitoring peuvent être consultées depuis le [dashboard] *Vue d'ensemble de transaction*({{< ref path="support/kb/dashboards-and-reporting/dashboards"  lang="fr" >}}). Comme son nom l'indique, ce dashboard est une vue d'ensemble et peut donc contenir des informations sur plusieurs moniteurs de transactions. Si vous souhaitez afficher uniquement les informations d'un moniteur de transaction spécifique, ouvrez l'onglet [Voir les détails]({{< ref path="#tutorial-check-details" lang="fr" >}}) de ce moniteur.

## Dashboard Vue d'ensemble de transaction

Votre dashboard *Vue d'ensemble de transaction* contient des tuiles qui indiquent le statut actuel de vos transactions, le relevé des dernières vérifications, ainsi que des informations et un diagramme sur la disponibilité et les performances de vos transactions.
Il existe deux [types de tuiles de dashboard]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="fr" >}}) : les graphiques et les listes. Les listes présentent les données de monitoring sous forme de tableau, tandis que les graphiques en fournissent une représentation visuelle.

Veuillez noter que le dashboard *Vue d'ensemble de transaction* ne contient pas d'informations sur les moniteurs de transactions en [développement]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}).

Pour ouvrir le dashboard *Vue d'ensemble de transaction*, ouvrez le menu {{< AppElement type="menuitem" >}} Transactions > Vue d'ensemble de transaction {{< /AppElement >}}.

![Capture d'écran du dashboard vue d'ensemble de transaction](/img/content/scr_transaction-tutorial-transaction-overview.min.png)

### Statut de compte

La tuile *Statut de compte* vous indique le statut de vos moniteurs de transactions en mode simulation et production. Depuis ce tableau, vous pouvez rapidement activer et désactiver vos moniteurs, ainsi que les alertes de vos transactions en mode production.

![Capture d'écran de la tuile statut de compte](/img/content/scr_transaction-tutorial-account-status.min.png)

### Dernière vérification

Le tableau *Dernière vérification* présente un relevé chronologique des dernières vérifications. Depuis la tuile *Dernière vérification*, vous pouvez cliquer sur une vérification spécifique (cliquez sur la date) pour afficher le rapport [*Voir les détails*]({{< ref path="#tutorial-check-details" lang="fr" >}}). L'icône appareil photo dans la colonne **Statut** indique que le rapport *Voir les détails* inclut une ou plusieurs captures d'écran.

![Capture d'écran de la tuile dernière vérification](/img/content/scr_transaction-tutorial-last-checks.min.png)

### Temps total, disponibilité et erreurs confirmées

Cette liste indique le temps total moyen, le pourcentage de disponibilité et le nombre d'erreurs confirmées pour la période couverte par le rapport. Bien sûr, vous pouvez ajouter d'autres métriques en cliquant sur les points de suspension {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} qui vous donnent accès aux paramètres de la tuile.

![Capture d'écran de la tuile sur la disponibilité et les erreurs](/img/content/scr_transaction-dashboard-tile-total-uptime-errors.min.png)

{{< callout >}}**Remarque :** La disponibilité des transactions en mode simulation n'est pas relevée et celles-ci sont considérées comme toujours disponibles. {{< /callout >}}

### Disponibilité et erreurs confirmées

La tuile *Disponibilité et erreurs confirmées* fournit une représentation visuelle du temps de disponibilité moyen et des erreurs survenues pendant la période de rapport pour tous les moniteurs de transactions en mode production.

![Capture d'écran de la tuile disponibilité et erreurs confirmées](/img/content/scr_transaction-tutorial-uptime-confirmed-errors.min.png)

### Rapport détaillé sur une transaction {id="monitor-own-dashboard"}

Le dashboard *Vue d'ensemble de transaction* contient des données sur tous les moniteurs de transactions définis par défaut ou sur les moniteurs définis pour ce dashboard. Pour consulter les informations détaillées sur un seul moniteur, voici comment procéder :

À certains endroits des tuiles de dashboards, les noms des moniteurs sont soulignés par un trait en pointillé. Survolez le nom du moniteur qui vous intéresse. Une fenêtre d'information s'affiche :

![Capture d'écran de la fenêtre d'information sur le moniteur](/img/content/scr_transaction-tutorial-monitor-quick-access.min.png)

Cliquez sur le lien **Dashboard** dans cette fenêtre pour afficher un autre dashboard spécifique au moniteur. Ce dashboard présente toutes les informations que vous pouvez obtenir sur un moniteur.

![Capture d'écran du dashboard du moniteur de transaction](/img/content/scr_transaction-tutorial-drilldown.min.png)
### Listes et graphiques sur la durée des étapes des transactions

La durée de chaque action est aussi importante que le temps de chargement de la page à l'ouverture du site. Tout temps d'attente important entre deux actions affecte la confiance que les utilisateurs accordent à votre produit et à votre marque. Les listes et les graphiques *Timing étape de transaction* vous aident à identifier les problèmes et les tendances.

Voici le graphique *Timing étape de transaction*. Cette tuile de dashboard montre la durée de chaque étape de la transaction, telle que mesurée lors de chaque vérification de moniteur.

![Capture d'écran de la tuile timing étape de transaction](/img/content/scr_transaction-tutorial-step-timing.min.png)

Pour connaître les performances d'une transaction, vous pouvez aussi vérifier la durée moyenne nécessaire à chaque étape. En vous appuyant sur la durée attendue d'une étape, vous pouvez observer les durées moyennes des étapes pour repérer d'éventuels problèmes de performance.

![Capture d'écran de la tuile Temps moyen d'étape de transaction](/img/content/scr_transaction-tutorial-average-steptime.min.png)

La liste *Timing étape de transaction* vous montre les données chiffres des durées relevées pour chaque test.

![Capture d'écran de la tuile timing étape de transaction](/img/content/scr_transaction-tutorial-step-timing-drilldown.min.png)

### Liste et graphique sur les types d'erreurs

La liste et le graphique sur les *types d'erreurs* vous donnent une vue d'ensemble des erreurs confirmées que votre moniteur a décelées pour la période de rapport.

![Capture d'écran sur les tuiles présentant les types d'erreurs](/img/content/scr_transaction-tutorial-error-types.min.png)

## Voir les détails {id="tutorial-check-details"}

Pour consulter les résultats d'une vérification spécifique, cliquez sur la ligne correspondante dans la tuile *Dernière vérification* de votre dashboard *Vue d'ensemble de transaction*. Vous pouvez aussi cliquer sur la tuile *Journal moniteurs* dans le [dashboard du moniteur]({{< ref path="#monitor-own-dashboard" lang="fr" >}}). Vous obtenez ainsi toutes les informations disponibles : la date et l'heure, le résultat, le checkpoint, le temps de chargement, le type de navigateur et sa version, le système d'exploitation et les résultats par étape.

![screenshot transaction check details](/img/content/scr_transaction-check-details.min.png)

Habituellement, le **temps de chargement** (visible dans le rapport ci-dessus) désigne le temps nécessaire pour demander et charger une page dans un navigateur. Dans le contexte des transactions, le temps de chargement désigne le temps total nécessaire à la réalisation de la transaction, de la première requête à la dernière action (soit la somme de toutes les durées de chaque étape).

### Résultat par étape

La section **Résultat par étape** doit vous sembler familière. En effet, elle correspond à votre script ventilé par étape, et vous fournit le résultat de chaque action. Vous obtenez la durée par étape et le résultat de chaque action. Si une action échoue, le test s'interrompt et l'étape s'affiche en rouge dans le rapport. Si vous avez un compte Business ou Enterprise, le rapport *Voir les détails* vous donne aussi accès aux graphiques en cascade et aux captures d'écran. Par exemple, si vous cliquez sur l'icône du graphique en cascade {{< AppElement type="iconWaterfall" >}} {{< /AppElement >}} (à côté du nom de l'étape), cela ouvre le graphique correspondant.

![](/img/content/77be77be-5520-4eab-9bf5-1d423f1acd6b.png)
