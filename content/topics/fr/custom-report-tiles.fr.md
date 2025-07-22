{
"hero": {
"title": "Tuiles personnalisées"
},
"title": "Tuiles personnalisées",
"summary": "Affichez vos données de surveillance sous forme de liste ou de graphique sur des dashboards personnalisés à l'aide de tuiles personnalisées.",
"url": "/support/kb/dashboards-et-rapports/dashboards/tuiles-personnalises",
"translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles"
}

Uptrends propose une large gamme de tuiles de rapport pouvant répondre à tous vos besoins de monitoring. Ces tuiles vous présentent les métriques de vos moniteurs et de vos checkpoints, ainsi que les statuts d'erreur sous forme de diagramme. Plusieurs types de tuiles peuvent être configurés au moyen des [paramètres de vos dashboards]({{< ref path="/support/kb/dashboards-and-reporting/dashboards" lang="fr" >}}). Il peut s'agir de tableaux, de graphiques linéaires, de graphiques à barres et de diagrammes circulaires.

Pour commencer, [ajoutez une tuile]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="fr" >}}) à vos dashboards par défaut ou créez entièrement votre configuration. Une fois la tuile ajoutée, cliquez sur l'icône {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} pour ouvrir et personnaliser ses paramètres.

Cet article de notre base de connaissances vous présente les différents types de tuile et leurs paramètres.

## Liste ou graphique de données simple {id="simple-data-list-chart"}

Ce type de tuile vous permet de sélectionner les moniteurs ou les groupes de moniteurs dont vous souhaitez afficher les métriques correspondant aux options **Général**, **Core Web Vitals** et **Navigation W3C**. Ces métriques peuvent varier selon le type de moniteur et d'autres paramètres de configuration.

Pour activer les métriques **Core Web Vitals** et **Navigation W3C** de vos moniteurs, vérifiez que le [type de navigateur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="fr" >}}) du moniteur est désormais **Chrome avec des métriques supplémentaires**. Pour les moniteurs de transactions, vérifiez aussi que vous avez activé les [métriques de performance]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="fr" >}}) dans les paramètres **Cascade** de vos étapes de transaction.

Sachez toutefois que les données **Core Web Vitals** et **Navigation W3C** ne seront pas disponibles pour la période antérieure à ces activations. Vous pouvez ajuster la période de rapport dans les paramètres de tuile afin de montrer uniquement la période pendant laquelle l'option **Chrome avec des métriques supplémentaires** était activée.

Une fois configurée, la liste de données simple ou le graphique de données simples affiche un graphique reflétant ces métriques. Lisez la légende et survolez le graphique pour en savoir plus sur les étapes. Pour en savoir plus sur les métriques connexes, lisez l'article de notre base de connaissances intitulé [Calcul de la disponibilité et des temps d'arrêt]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="fr" >}}).

![Métriques de la liste ou du graphique de données simple](/img/content/scr-data-metrics.min.png)


### Général

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :

- Temps total, temps de résolution, temps de connexion et temps de téléchargement
- Pourcentage de disponibilité, pourcentage d'indisponibilité (downtime), disponibilité et indisponibilité
- Erreurs confirmées et non confirmées
- Vérifications, alertes et nombre total d'octets
- Pourcentage d'objectif uptime SLA, objectif de temps total SLA, objectif SLA de réponse de l'opérateur et temps de réponse de l'opérateur

![Graphique de données simple présentant des métriques Général](/img/content/scr_simple-data-chart.min.png)

### Core Web Vitals

Les moniteurs FPC et les moniteurs de transactions collectent des données [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) lorsque le type de navigateur est configuré sur [Chrome avec des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="fr" >}}).

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :

- First Contentful Paint
- Largest Contentful Paint
- Time To Interactive
- Total Blocking Time
- Cumulative Layout Shift

![Graphique de données simple présentant des métriques Core Web Vitals](/img/content/scr_simple-data-chart-steps.min.png)


### Navigation W3C

Les moniteurs FPC et les moniteurs de transactions collectent des données [Navigation W3C]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}) et [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) lorsque le type de navigateur est configuré sur [Chrome avec des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring#chrome-extra-metrics" lang="fr" >}}).

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :
- Début de la requête
- Durée jusqu'au premier octet
- DOM interactive
- DOM terminé
- Load event

![Métriques de navigation W3C de la liste de données simple](/img/content/scr_simple-data-list.min.png)


## Liste ou graphique de données de moniteurs

Sélectionnez les moniteurs ou les groupes de moniteurs et la période, puis les métriques à afficher parmi les options suivantes :

- Objectif uptime SLA et Uptime SLA
- Objectif de temps total SLA, Temps total objectif SLA, Indisponibilité SLA
- Temps SLA de réponse opérateur, Objectif SLA de réponse opérateur
- Temps total, Vérifications, Erreurs confirmées, Erreurs non confirmées
- Pourcentage de disponibilité, Pourcentage downtime (indisponibilité)
- Options Trier par et Montrer les lignes

![Capture d'écran de la tuile Graphique données moniteur](/img/content/scr_monitor-data-chart.min.png)

![Capture d'écran de la tuile Liste de données de moniteurs](/img/content/scr_monitor-data-list.min.png)

## Liste ou graphique de types d'erreurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs, et la période.

![Capture d'écran des tuiles Liste et graphique de types d'erreurs](/img/content/scr_error-type-list-chart.min.png)

## Liste ou graphique de données de checkpoints

Sélectionnez les moniteurs ou les groupes de moniteurs et la période, puis les métriques à afficher parmi les options suivantes :

- Temps total, Temps de résolution
- Temps de connexion, Temps de téléchargement
- Vérifications, Erreurs confirmées et option Trier par

![Capture d'écran de la tuile Graphique de données de checkpoints](/img/content/scr_checkpoint-data-chart.min.png)

![Capture d'écran de la tuile Liste de données de checkpoints](/img/content/scr_checkpoint-data-list.min.png)

## Liste ou graphique multi checkpoint

Sélectionnez les moniteurs ou groupes de moniteurs et la période, puis choisissez la métrique à afficher dans la liste ou le graphique.


![Capture d'écran de la tuile Graphique multi checkpoint](/img/content/scr_multi-checkpoint-chart-tile.min.png)

![Capture d'écran de la tuile Liste multi checkpoint](/img/content/scr_multi-checkpoint-list-tile.min.png)

## Liste ou graphique multi moniteurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs et la période, puis sélectionnez la métrique à afficher dans la liste ou le graphique.

![Capture d'écran de la tuile Graphique multi moniteurs](/img/content/scr_multi-monitor-chart-tile.min.png)

![Capture d'écran de la tuile Liste multi moniteurs](/img/content/scr_multi-monitor-list-tile.min.png)

## Détails dernière vérification {id="last-check-details"}

Cette tuile indique quand un ou plusieurs moniteurs ou groupes de moniteurs ont été vérifiés pour la dernière fois, et permet de sélectionner la période pour laquelle il faut afficher les données.  
![Capture d'écran de la tuile personnalisée sur les détails de vérification du moniteur ](/img/content/scr_custom-report-tiles-lastcheck.min.png)

## Journal moniteurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs et la période, puis indiquez comment filtrer les erreurs et précisez si vous souhaitez afficher le rapport dans un fichier exporté.

![Capture d'écran de la tuile Journal moniteurs](/img/content/scr_monitor-log-tile.min.png)

## Historique des alertes

Cette tuile affiche l'historique des notifications d'alerte par moniteur ou groupe de moniteurs, et permet de filtrer les données par période.

![Capture d'écran de la tuile Historique des alertes](/img/content/scr_alert-history-tile.min.png)

## Liste ou graphique de durée des étapes

Cette tuile est disponible pour les moniteurs de transactions et moniteurs d'API multi-étapes, un moniteur à la fois. Elle présente la durée des étapes dans le temps.

![Capture d'écran de la tuile Graphique de durée des étapes](/img/content/scr_step-duration-chart-tile.min.png)

## Liste ou graphique de la durée moyenne des étapes

Cette tuile est disponible pour les moniteurs de transactions et moniteurs d'API multi-étapes, un moniteur à la fois. Elle présente la durée moyenne des étapes.

![Capture d'écran de la tuile Graphique de la durée moyenne des étapes](/img/content/scr_average-step-duration-chart-tile.min.png)
