{
"hero": {
"title": "Captures d'écran successives"
},
"title": "Captures d'écran successives",
"summary": "Description des captures d'écran chronologiques dans les résultats de la cascade",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/captures-ecran-successives",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/timeline-screenshots",
"TableOfContents": false
}

Le chargement d'une page dans un navigateur s'effectue en plusieurs étapes. Au fur et à mesure que les éléments de la page sont chargés, le navigateur commence à afficher le contenu et à construire sa mise en page, jusqu'à ce que le chargement soit terminé et que votre moniteur renvoie (avec un peu de chance) un résultat Ok. Un [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) est une bonne représentation de ce qui se passe pendant le chargement de la page, mais comme de nombreux éléments se chargent simultanément, il peut être difficile de se faire une idée de ce qui se passe réellement dans le navigateur.

Pour vous aider, notre type de moniteur [Full Page Check (FPC)]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}), lorsqu'il est configuré pour utiliser **Chrome avec métriques supplémentaires** comme type de navigateur, inclut des **captures d'écran successives** (également appelées des **filmstrip**). Il s'agit d'une série de captures d'écran du navigateur, montrant exactement à quoi ressemblait la page à différents moments de son chargement.

![Captures d'écran successives](/img/content/scr-timeline-screenshots.min.png)

Si votre graphique en cascade indique des soucis, comme des images qui ne se chargent pas ou des scripts qui bloquent le reste de la page, vous pouvez comparer la chronologie de la cascade avec la capture d'écran correspondante pour voir à quoi ressemblait la page à ce moment-là.

## Quand ces captures d'écran successives sont-elles prises ?

Les captures d'écran présentées dans Uptrends proviennent directement de Chrome. Faisant partie de ses fonctionnalités par défaut, Chrome collecte ses propres captures d'écran lorsqu'un enregistrement de performance est effectué via son interface Dev tools. À partir de cet ensemble capturé par Chrome, nous tentons d'afficher les plus pertinentes :

- Celles qui suivent directement certains jalons (première/dernière capture d'écran, premier affichage de contenu (contentful paint), plus grande peinture de contenu, temps avant interaction).
- En fonction de la durée totale du moniteur, nous déciderons du nombre de captures d'écran à présenter, mais avec un minimum de six.