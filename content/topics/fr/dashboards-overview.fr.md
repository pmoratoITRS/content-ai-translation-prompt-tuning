{
"hero": {
"title": "Vue d'ensemble des dashboards"
},
"title": "Vue d'ensemble des dashboards",
"summary": "Les dashboards affichent toutes vos données de surveillance de façon organisée. Découvrez comment les utiliser et créer vos propres dashboards avec des tuiles personnalisées.",
"url": "/support/kb/dashboards-et-rapports/dashboards/apercu-des-tableaux-de-bord",
"translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/dashboards-overview",
"sectionlist": false
}

Les dashboards servent à présenter toutes vos données de surveillance de manière organisée. Les dashboards peuvent contenir des tuiles qui montrent vos données sous forme de listes ou de graphiques, ou afficher les derniers résultats d'une vérification. L'application Uptrends fournit plusieurs dashboards prédéfinis, mais vous pouvez aussi créer des dashboards personnalisés.

Tous les dashboards sont accessibles depuis le menu {{< AppElement type="menuitem" >}} Dashboard {{< /AppElement >}}. De plus, certains dashboards peuvent être ouverts depuis le menu principal correspondant. Par exemple, la vue d'ensemble des moniteurs de navigateur est accessible depuis le menu {{< AppElement type="menuitem" >}} Navigateur > Présentation de moniteurs de navigateur {{< /AppElement >}}.

![capture d'écran du dashboard de vue d'ensemble des moniteurs](/img/content/scr_dashboard-browser-overview.min.png)

## Dashboards prédéfinis

Plusieurs dashboards prédéfinis sont à votre disposition. Pour en savoir plus sur ces dashboards prêts à l'emploi, vous pouvez lire l'article [Dashboards prédéfinis]({{< ref path="support/kb/dashboards-and-reporting/dashboards/predefined-dashboards" lang="fr" >}}).

## Dashboards personnalisés et tuiles personnalisées

En plus des dashboards prédéfinis, vous pouvez créer des [dashboards personnalisés]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-dashboards" lang="fr" >}}) et les remplir avec des [tuiles personnalisées]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="fr" >}}).

Les dashboards peuvent être personnalisés en modifiant leur nom ou celui des tuiles, en indiquant quelles métriques doivent être affichées dans les tuiles et en définissant les filtres applicables aux dashboards ou aux tuiles.

## Filtrer les données des dashboards

Pour savoir comment appliquer des filtres à vos dashboards ou à vos tuiles, vous pouvez lire notre article sur le [filtrage des données de dashboard]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/tile-filtering" lang="fr" >}}).

## Dépannage

Quelque chose ne fonctionne pas comme prévu ? Voici quelques-unes des solutions possibles :

- Données manquantes dans les nouveaux moniteurs ou les moniteurs modifiés
   - Pour les nouveaux moniteurs ou les moniteurs modifiés, la tuile de dashboard reflète les données du moniteur dans un délai de deux secondes. Une fois que les données initiales s'affichent sur la tuile ou après un délai de cinq minutes, la tuile s'actualise et récupère les données toutes les 30 secondes, conformément au temps de chargement standard.
- [Données manquantes dans les tuiles multi-checkpoint]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/missing-data-in-multi-checkpoint-dashboard-tiles" lang="fr" >}})
- [Données manquantes dans les tuiles contenant les métriques des moniteurs Full Page Check]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}})
