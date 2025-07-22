{
"title": "Nouvelle métrique des Core Web Vitals : Interaction to Next Paint (INP)",
"date": "2024-06-12",
"url": "/changelog/juin-2024-nouveau-cwv-inp",
"translationKey": "https://www.uptrends.com/changelog/june-2024-new-cwv-inp"
}

Certains types de moniteurs, tels que les [moniteurs Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) et les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="fr" >}}), peuvent inclure les [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) parmi les métriques de chargement de page pour l'URL que vous vérifiez. Les Core Web Vitals sont l'ensemble standard de métriques utilisé par Google pour mesurer l'expérience utilisateur.

L'ensemble de Core Web Vitals inclus dans les résultats des moniteurs inclut désormais la métrique "Interaction to Next Paint" (INP). Cette métrique permet d'évaluer la réactivité de la page face aux interactions des utilisateurs, en mesurant le temps écoulé entre l'action de l'utilisateur et l'affichage de la réponse sur la page.