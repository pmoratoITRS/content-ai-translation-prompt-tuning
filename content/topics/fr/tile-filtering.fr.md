{
"hero": {
"title": "Filtrage des tuiles et des dashboards"
},
"title": "Filtrage des tuiles et des dashboards",
"summary": "Affichez uniquement certaines données de surveillance en appliquant des filtres dans les dashboards ou les tuiles individuelles.",
"url": "/support/kb/dashboards-et-rapports/dashboards/filtrage-tuile",
"translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/tile-filtering"
}

Il existe deux possibilités pour filtrer les données d'un dashboard : par tuile individuelle (pour pouvoir afficher en côte à côte deux tuiles similaires, mais avec des paramètres distincts) ou en appliquant un filtre sur l'ensemble du dashboard.

## Filtrage de dashboard

Pour filtrer un dashboard dans son ensemble, ouvrez le dashboard puis utilisez les options de filtre dans le menu d'action rapide (en haut à droite du dashboard).

![capture d'écran des filtres de dashboard](/img/content/scr_dashboard-filters.min.png)


Vous verrez une variété d'options de filtrage qui changent en fonction de votre dashboard, parmi lesquelles :

- **Filtrage par moniteur**  
   Ce filtre est très pratique si vous voulez voir les données de seulement certains moniteurs. Vous pouvez sélectionner un ou plusieurs moniteurs ou [groupes de moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="fr" >}}).
- **Filtrage par niveau d'erreur**  
   Ce filtre vous permet d'afficher toutes les erreurs, seulement les [erreurs non confirmées et confirmées]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}), seulement les erreurs confirmées ou seulement les contrôles réussis (soit les résultats de type OK).
- **Filtre de contrôles partiels**  
   Ce filtre spécifique à la [surveillance simultanée]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="fr" >}}) vous permet d'afficher ou de masquer les contrôles partiels.
- **Filtrage par checkpoint**  
   Ce filtre permet d'afficher uniquement les données produites par certains [checkpoints]({{< ref path="#checkpoint-filtering" lang="fr" >}}).
- **Filtrage par date/heure**  
   Définissez un filtre selon une période de votre choix.

## Filtrage par tuile individuelle

Pour filtrer les données par tuile :

1. Accédez au dashboard qui contient la tuile que vous souhaitez filtrer.
2. Une fois la tuile sélectionnée, cliquez sur les points de suspension {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} pour accéder à ses paramètres.
   Une fenêtre pop-up apparaît, avec une série d'onglets et des options de configuration associées à la tuile.

   ![capture d'écran du paramétrage par tuile](/img/content/scr_tile-settings.min.png)

   Les onglets et options disponibles dépendent du [type de tuile]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="fr" >}}). Selon le cas, les onglets suivants peuvent être disponibles :

   **Tuile**  
   Les options contenues dans l'onglet {{< AppElement type="tab" >}}Tuile{{< /AppElement >}} concernent uniquement la façon dont les données sont présentées dans cette tuile.

   **Groupes et moniteurs**  
   L'onglet {{< AppElement type="tab" >}}Groupes et moniteurs{{< /AppElement >}} vous permet d'afficher les données relatives au contexte du dashboard (généralement la valeur par défaut) ou bien de le filtrer pour afficher les données relatives à tout moniteur ou groupe de moniteurs.

   **Checkpoints**  
   Cet onglet permet de filtrer les données selon le ou les checkpoints ayant réalisé la vérification. Vous trouverez ci-dessous les étapes à suivre pour appliquer un [filtrage par checkpoint]({{< ref path="#checkpoint-filtering-tiles" lang="fr" >}}).

   **Période**  
   L'onglet {{< AppElement type="tab" >}}Période{{< /AppElement >}} vous permet de définir la période pour laquelle vous voulez afficher les données, généralement définie par défaut selon le contexte du dashboard.
3. Sélectionnez tous les filtres à appliquer à la tuile.
4. Dans les paramètres de la tuile, cliquez sur le bouton {{< AppElement type="button" >}} Définir {{< /AppElement >}}.
5. Important : vos changements ne sont pas enregistrés automatiquement. Dès que vous apportez des changements à des tuiles (ou à un dashboard), pensez à les enregistrer en cliquant sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} en haut à droite du dashboard.

{{< callout >}} **Remarque** : L'article intitulé [Ajout d'une tuile personnalisée]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="fr" >}}) vous explique comment ajouter des tuiles à un dashboard. {{< /callout >}}

## Filtrage par checkpoint pour les tuiles {id="checkpoint-filtering-tiles"}

Les filtres de checkpoint sont disponibles pour les [types de tuile]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="fr" >}}) suivants :
- Liste ou graphique de données simples
- Liste ou graphique de données de checkpoints
- Liste ou graphique multi checkpoint
- Liste ou graphique de durée des étapes
- Journal moniteurs

Pour appliquer un filtrage par checkpoint à une tuile :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Dashboards {{< /AppElement >}}.
2. Sélectionnez un dashboard.
3. Cliquez sur les points de suspension {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} pour accéder aux paramètres de la tuile.
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}}.

   ![capture d'écran du filtrage des checkpoints d'une tuile](/img/content/scr-cp-selection-tiles.min.png)

5. Sélectionnez le ou les checkpoints dont vous souhaitez afficher les données dans la tuile.  
   Vous pouvez sélectionner des checkpoints un par un, par région ou par pays (dans les régions).
6. Cliquez sur le bouton {{< AppElement type="button" >}} Définir {{< /AppElement >}}.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en haut à droite du dashboard.

**Remarque :** Deux exceptions s'appliquent au filtrage par checkpoint :
- Les métriques supplémentaires de type "FPC et transactions uniquement". Lorsque l'une de ces métriques est sélectionnée dans l'onglet {{< AppElement type="tab" >}}Tuile{{< /AppElement >}} avec un filtre de checkpoint, Uptrends affiche un avertissement.
- Quand le filtre **Groupe de timing** {{< AppElement type="dropdown" >}} Afficher par heure du jour {{< /AppElement >}} est sélectionné dans l'onglet {{< AppElement type="tab" >}} Période {{< /AppElement >}} et qu'un filtre de checkpoint est activé, un avertissement s'affiche.
   ![](/img/content/scr-cp-tile-time-grouping.min.png)