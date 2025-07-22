{
"title": "Métriques de performance pour chaque étape de transaction",
"date": "2024-02-07",
"url": "/changelog/fevrier-2024-metriques-performance-etapes-transaction",
"translationKey": "https://www.uptrends.com/changelog/february-2024-performance-metrics-transaction-steps"
}

Aimeriez-vous pouvoir consulter les métriques de performance [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) et les [temps de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}) pour chaque étape dans votre dashboard ? C'est désormais possible en activant l'enregistrement des données dans l'étape de transaction. Ouvrez la transaction et déroulez l'étape qui vous intéresse, puis activez l'option "Métriques de performance" dans la partie supérieure des paramètres de l'étape. À noter que le paramètre "Cascade" doit être activé pour que cette option fonctionne.

Une fois l'activation effectuée, les indicateurs de performance Core Web Vitals et les temps de navigation du W3C sont disponibles et peuvent être consultés sur un dashboard au moyen de la tuile personnalisée [Simple graphique de données]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}). La légende de la tuile indique quel graphique correspond à quelle étape. Par exemple, *First contentful paint (étape 1)*. Vous pouvez aussi survoler le graphique pour obtenir des données plus détaillées.
