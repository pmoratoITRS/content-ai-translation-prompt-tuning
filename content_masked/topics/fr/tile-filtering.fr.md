{
  "hero": {
    "title": "Filtrage des tuiles et des dashboards"
  },
  "title": "Filtrage des tuiles et des dashboards",
  "summary": "Affichez uniquement certaines données de surveillance en appliquant des filtres dans les dashboards ou les tuiles individuelles.",
  "url": "[URL_BASE_TOPICS]dashboards-et-rapports/dashboards/filtrage-tuile",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Il existe deux possibilités pour filtrer les données d'un dashboard : par tuile individuelle (pour pouvoir afficher en côte à côte deux tuiles similaires, mais avec des paramètres distincts) ou en appliquant un filtre sur l'ensemble du dashboard.

## Filtrage de dashboard

Pour filtrer un dashboard dans son ensemble, ouvrez le dashboard puis utilisez les options de filtre dans le menu d'action rapide (en haut à droite du dashboard).

![capture d'écran des filtres de dashboard]([LINK_URL_1])


Vous verrez une variété d'options de filtrage qui changent en fonction de votre dashboard, parmi lesquelles :

- **Filtrage par moniteur**  
   Ce filtre est très pratique si vous voulez voir les données de seulement certains moniteurs. Vous pouvez sélectionner un ou plusieurs moniteurs ou [groupes de moniteurs]([LINK_URL_2]).
- **Filtrage par niveau d'erreur**  
   Ce filtre vous permet d'afficher toutes les erreurs, seulement les [erreurs non confirmées et confirmées]([LINK_URL_3]), seulement les erreurs confirmées ou seulement les contrôles réussis (soit les résultats de type OK).
- **Filtre de contrôles partiels**  
   Ce filtre spécifique à la [surveillance simultanée]([LINK_URL_4]) vous permet d'afficher ou de masquer les contrôles partiels.
- **Filtrage par checkpoint**  
   Ce filtre permet d'afficher uniquement les données produites par certains [checkpoints]([LINK_URL_5]).
- **Filtrage par date/heure**  
   Définissez un filtre selon une période de votre choix.

## Filtrage par tuile individuelle

Pour filtrer les données par tuile :

1. Accédez au dashboard qui contient la tuile que vous souhaitez filtrer.
2. Une fois la tuile sélectionnée, cliquez sur les points de suspension [SHORTCODE_3][SHORTCODE_4] pour accéder à ses paramètres.
   Une fenêtre pop-up apparaît, avec une série d'onglets et des options de configuration associées à la tuile.

   ![capture d'écran du paramétrage par tuile]([LINK_URL_6])

   Les onglets et options disponibles dépendent du [type de tuile]([LINK_URL_7]). Selon le cas, les onglets suivants peuvent être disponibles :

   **Tuile**  
   Les options contenues dans l'onglet [SHORTCODE_5]Tuile[SHORTCODE_6] concernent uniquement la façon dont les données sont présentées dans cette tuile.

   **Groupes et moniteurs**  
   L'onglet [SHORTCODE_7]Groupes et moniteurs[SHORTCODE_8] vous permet d'afficher les données relatives au contexte du dashboard (généralement la valeur par défaut) ou bien de le filtrer pour afficher les données relatives à tout moniteur ou groupe de moniteurs.

   **Checkpoints**  
   Cet onglet permet de filtrer les données selon le ou les checkpoints ayant réalisé la vérification. Vous trouverez ci-dessous les étapes à suivre pour appliquer un [filtrage par checkpoint]([LINK_URL_8]).

   **Période**  
   L'onglet [SHORTCODE_9]Période[SHORTCODE_10] vous permet de définir la période pour laquelle vous voulez afficher les données, généralement définie par défaut selon le contexte du dashboard.
3. Sélectionnez tous les filtres à appliquer à la tuile.
4. Dans les paramètres de la tuile, cliquez sur le bouton [SHORTCODE_11] Définir [SHORTCODE_12].
5. Important : vos changements ne sont pas enregistrés automatiquement. Dès que vous apportez des changements à des tuiles (ou à un dashboard), pensez à les enregistrer en cliquant sur le bouton [SHORTCODE_13]Enregistrer[SHORTCODE_14] en haut à droite du dashboard.

[SHORTCODE_1] **Remarque** : L'article intitulé [Ajout d'une tuile personnalisée]([LINK_URL_9]) vous explique comment ajouter des tuiles à un dashboard. [SHORTCODE_2]

## Filtrage par checkpoint pour les tuiles [ANCHOR_1]

Les filtres de checkpoint sont disponibles pour les [types de tuile]([LINK_URL_10]) suivants :
- Liste ou graphique de données simples
- Liste ou graphique de données de checkpoints
- Liste ou graphique multi checkpoint
- Liste ou graphique de durée des étapes
- Journal moniteurs

Pour appliquer un filtrage par checkpoint à une tuile :

1. Ouvrez le menu [SHORTCODE_15] Dashboards [SHORTCODE_16].
2. Sélectionnez un dashboard.
3. Cliquez sur les points de suspension [SHORTCODE_17] [SHORTCODE_18] pour accéder aux paramètres de la tuile.
4. Ouvrez l'onglet [SHORTCODE_19] Checkpoints [SHORTCODE_20].

   ![capture d'écran du filtrage des checkpoints d'une tuile]([LINK_URL_11])

5. Sélectionnez le ou les checkpoints dont vous souhaitez afficher les données dans la tuile.  
   Vous pouvez sélectionner des checkpoints un par un, par région ou par pays (dans les régions).
6. Cliquez sur le bouton [SHORTCODE_21] Définir [SHORTCODE_22].
7. Cliquez sur le bouton [SHORTCODE_23] Enregistrer [SHORTCODE_24] en haut à droite du dashboard.

**Remarque :** Deux exceptions s'appliquent au filtrage par checkpoint :
- Les métriques supplémentaires de type "FPC et transactions uniquement". Lorsque l'une de ces métriques est sélectionnée dans l'onglet [SHORTCODE_25]Tuile[SHORTCODE_26] avec un filtre de checkpoint, Uptrends affiche un avertissement.
- Quand le filtre **Groupe de timing** [SHORTCODE_27] Afficher par heure du jour [SHORTCODE_28] est sélectionné dans l'onglet [SHORTCODE_29] Période [SHORTCODE_30] et qu'un filtre de checkpoint est activé, un avertissement s'affiche.
   ![]([LINK_URL_12])