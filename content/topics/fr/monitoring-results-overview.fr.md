{
"hero": {
"title": "Aperçu des résultats de la surveillance"
},
"title": "Aperçu des résultats de la surveillance",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/apercu-des-resultats-de-la-surveillance",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/monitoring-results-overview",
"sectionlist": false
}

Les vérifications effectuées par les moniteurs donnent lieu à différents types de résultats ou de rapports en fonction du type de moniteur et de vos paramètres. Les [détails de vérification]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="fr" >}}) contiennent de nombreux résultats et sont fournis par tous les moniteurs. Cependant, certains de ces résultats peuvent concerner seulement quelques types de moniteurs. Par exemple, le graphique en cascade peut être fourni par les moniteurs Full Page Check et les moniteurs de transactions, mais pas par les autres moniteurs.

## Métriques

Les **Core Web Vitals** et les **durées de navigation du W3C** vous fournissent deux ensembles de métriques basées sur des normes internationales. Ces métriques vous permettent de mieux comprendre les performances de votre site web et de déterminer ce qui doit être amélioré pour obtenir un meilleur score dans les classements des moteurs de recherche.

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}})
- [Durées de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}})

Notez que vous pouvez ajouter ces métriques à un dashboard personnalisé en ajoutant une tuile personnalisée de type [Liste ou graphique simple de données]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}).

## Cascade

Le graphique en cascade présente vos résultats de surveillance dans un graphique à barres, qui montre en détail le chargement successif des éléments de la page ainsi que le temps pris par chacun. C'est un bon outil de dépannage pour découvrir ce qui ralentit le chargement d'une page. Consultez les articles de la base de connaissances sur les cascades :

- [Graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}})
- [Durées des cascades]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="fr" >}})
- [Interprétation des résultats du rapport en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="fr" >}})

## Dépannage

Les résultats de la vérification effectuée par un moniteur sont disponibles dans les détails de la vérification. Ces résultats sont un bon point de départ pour le dépannage.

- [Détails de vérification]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="fr" >}})

Les résultats de la vérification contiennent aussi la source de la page (source HTML) et le journal de la console (du chargement de la page). Ces informations sont disponibles dans les résultats de vérification des moniteurs de transaction et des moniteurs Full Page Check. Vous aurez peut-être à activer cette fonctionnalité : consultez l'article de la base de connaissances ci-dessous pour plus de détails.

- [Source de la page et journal de la console]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="fr" >}})

Le graphique en cascade vous donne un bon aperçu du chargement des éléments de votre page. Cependant, il peut être difficile d'imaginer ce qui s'y passe étape par étape. Les captures d'écran successives vous montrent à quoi ressemble la page à différentes étapes du processus de chargement.

- [Captures d'écran successives]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}})
