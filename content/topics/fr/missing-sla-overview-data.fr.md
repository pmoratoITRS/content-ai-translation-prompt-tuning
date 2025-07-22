{
  "hero": {
    "title": "Données absentes dans Vue d’ensemble SLA"
  },
  "title": "Données absentes dans Vue d’ensemble SLA",
"summary": "La vue d'ensemble SLA n'affiche pas de données si la période définie comprend une date antérieure à la création du moniteur.",
  "url": "/support/kb/dashboards-et-rapports/sla/donnees-absentes-dans-vue-densemble-sla",
  "translationKey": "https://www.uptrends.com/support/kb/sla/missing-sla-overview-data"
}

Vous avez pris la peine de mettre en place un moniteur de SLA (Service Level Agreement - accord sur le niveau de service) ou vous avez choisi d'utiliser le moniteur de SLA par défaut créé lors de l'ouverture votre compte, mais quand vous regardez la vue d’ensemble du SLA, vous ne voyez qu'une série de tirets (par exemple, "-") ou de zéros. Pourquoi ? Parce que vos options de rapport ont généré des données non valides. À la place des ensembles de données incomplètes ou non valides, Uptrends affiche des zéros et des tirets.

## Scénarios possibles

Pour ce problème, nous rencontrons fréquemment deux scénarios : soit votre période commence avant la date et l'heure de définition du SLA ou de création du moniteur, ou vous avez choisi l'option **Groupes de moniteurs** pour **Montrer les lignes pour** dans le menu de la tuile.

### Votre période commence avant la date et l'heure de définition du SLA ou de création du moniteur

Quand vous sélectionnez une période de rapport, gardez à l'esprit que si la définition SLA ou le moniteur a été créé après la date et l'heure de la période de rapport, même si la différence se compte en secondes, vos résultats pour ce moniteur s'afficheront sous la forme de tirets (pour une définition SLA plus récente) ou de zéros (pour un moniteur plus récent). Même si vous avez créé votre définition SLA le 1er janvier 2016, et qu’aujourd’hui nous sommes le 31 décembre 2016, si vous sélectionnez « Cette année » pour votre période de rapports, vous ne recevrez pas de données. Vous ne recevrez pas de données parce que le système ne dispose pas de données pour le 1er janvier, et donc le rapport affiche un “-”. Pour obtenir un rapport valide, utilisez l’outil de date personnalisée et choisissez une période qui commence le jour après la création du compte ou la définition SLA, par exemple, du 02/01/2016 au 31/12/2016.

### Vous avez sélectionné « Groupes de moniteurs » pour « Montrer les lignes pour » dans le menu de la tuile.

Quand vous cliquez sur les points de suspension {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} pour ouvrir les paramètres de la tuile, de nombreuses options s'affichent pour les données figurant dans cette tuile. Si vous sélectionnez **Groupes de moniteurs** dans la boîte de sélection **Montrer les lignes pour**, vous n'obtiendrez pas de données sur le SLA. La tuile montrera d'autres champs comme le temps total, les vérifications, les erreurs confirmées, le pourcentage de disponibilité et le downtime pour les groupes de moniteurs, mais vous n'aurez pas de valeurs dans les champs SLA car les données sur le SLA ne peuvent pas être agrégées entre les moniteurs. Vous pouvez afficher des données pour des moniteurs spécifiques ou des groupes de moniteurs en les sélectionnant dans le menu d'accès rapide ou dans les paramètres de la tuile, mais vos données s'afficheront toujours dans les lignes correspondant aux moniteurs individuels dans ces groupes.
