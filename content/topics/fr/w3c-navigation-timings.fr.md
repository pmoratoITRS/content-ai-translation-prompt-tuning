{
"hero": {
"title": "Mesures des durées de navigation du W3C"
},
"title": "Mesures des durées de navigation du W3C",
"summary": "Description des mesures des durées de navigation du W3C fournies dans les graphiques en cascade des moniteurs Full Page Check et de transactions",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/metriques-duree-navigation-w3c",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/w3c-navigation-timings"
}


Le **World Wide Web Consortium** (ou W3C) est une organisation internationale qui travaille au développement de standards pour le World Wide Web. À ce titre, le W3C a défini une norme pour les navigateurs et les applications web, qui permet de générer et d'afficher des informations sur les durées de chargement des pages web. La spécification complète de la norme peut être consultée sur le [site web du W3C (Copyright © 2012, World Wide Web Consortium)](https://www.w3.org/TR/navigation-timing/).

Les [moniteurs Full Page Check (FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) et [les moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="fr" >}}) d'Uptrends permettent d'afficher un sous-ensemble des métriques de durées de navigation du W3C (ainsi que quelques informations supplémentaires telles que les [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}})). Cet article vous présente les métriques fournies et ce qu'elles signifient.

Par exemple, l'image suivante montre tous les éléments de navigation définis par le W3C sur une frise chronologique.

![métriques de navigation du w3c](/img/content/img-w3c-nav-timings.min.png)
(Copyright © 2012, [World Wide Web Consortium](https://www.w3.org))

## Métriques

Voici une vue d'ensemble des métriques des durées de navigation du W3C que vous pouvez trouver dans les rapports du moniteur Full Page Check d'Uptrends.

![Durées de navigation du W3C dans Uptrends](/img/content/scr-new-w3c-timings.png)

- **Début de la requête** : équivaut au `requestStart` tel que défini par le W3C. Cet horodatage indique le moment où le navigateur commence à demander la ressource au serveur web après la consultation du DNS et la connexion TCP.
- **Durée jusqu'au premier octet** (Time to first byte) : équivaut à la différence entre `navigationStart` et `responseStart` tels que définis par le W3C. En bref, c'est le temps entre le moment où la première requête a été envoyée du navigateur au serveur et le moment où le premier octet de la réponse suivante a été reçu par le navigateur (qui peut comprendre des redirections et des connexions SSL/TCP).
- **DOM interactif** : équivaut au `domInteractive` tel que défini par le W3C. Il s'agit du moment où le document est devenu "interactif", ce qui indique que le navigateur a cessé d'analyser la page et que l'utilisateur peut commencer à interagir avec elle. Des ressources telles que les scripts, les images, les feuilles de style ou les cadres peuvent encore être en cours de chargement.
- **DOM terminé** : équivaut au `domComplete` tel que défini par le W3C. Il s'agit du moment où le document principal a été analysé, où le DOM a été entièrement chargé et où l'état de préparation de la page est devenu "terminé".
- **Load event** : équivaut à `loadEventEnd` tel que défini par le W3C. Il s'agit du moment où le chargement du document actuel est terminé, y compris pour toutes les ressources dépendantes telles que les feuilles de style et les images.

## Rapports de performance

Vous pouvez afficher toutes les métriques dans un dashboard personnalisé. Ajoutez simplement une tuile personnalisée du type [Liste ou graphique de données simple]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}). Cliquez ensuite sur le bouton des paramètres {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} de la tuile et choisissez les valeurs que vous souhaitez afficher en cochant leurs cases.

Vous pouvez afficher les métriques de navigation du W3C pour chaque étape d'un moniteur de transaction. Pour chaque étape que vous souhaitez afficher dans le graphique, vous devez activer les options *Cascade* et *Métriques de performance*. Pour en savoir plus, consultez les informations relatives à la [configuration des étapes]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="fr" >}}).

![capture d'écran des paramètres de la tuile](/img/content/scr_simple-data-metrics.min.png)
