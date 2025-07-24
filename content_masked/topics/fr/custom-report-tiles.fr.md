{
  "hero": {
    "title": "Tuiles personnalisées"
  },
  "title": "Tuiles personnalisées",
  "summary": "Affichez vos données de surveillance sous forme de liste ou de graphique sur des dashboards personnalisés à l'aide de tuiles personnalisées.",
  "url": "[URL_BASE_TOPICS]dashboards-et-rapports/dashboards/tuiles-personnalises",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends propose une large gamme de tuiles de rapport pouvant répondre à tous vos besoins de monitoring. Ces tuiles vous présentent les métriques de vos moniteurs et de vos checkpoints, ainsi que les statuts d'erreur sous forme de diagramme. Plusieurs types de tuiles peuvent être configurés au moyen des [paramètres de vos dashboards]([LINK_URL_1]). Il peut s'agir de tableaux, de graphiques linéaires, de graphiques à barres et de diagrammes circulaires.

Pour commencer, [ajoutez une tuile]([LINK_URL_2]) à vos dashboards par défaut ou créez entièrement votre configuration. Une fois la tuile ajoutée, cliquez sur l'icône [SHORTCODE_1] [SHORTCODE_2] pour ouvrir et personnaliser ses paramètres.

Cet article de notre base de connaissances vous présente les différents types de tuile et leurs paramètres.

## Liste ou graphique de données simple [ANCHOR_1]

Ce type de tuile vous permet de sélectionner les moniteurs ou les groupes de moniteurs dont vous souhaitez afficher les métriques correspondant aux options **Général**, **Core Web Vitals** et **Navigation W3C**. Ces métriques peuvent varier selon le type de moniteur et d'autres paramètres de configuration.

Pour activer les métriques **Core Web Vitals** et **Navigation W3C** de vos moniteurs, vérifiez que le [type de navigateur]([LINK_URL_3]) du moniteur est désormais **Chrome avec des métriques supplémentaires**. Pour les moniteurs de transactions, vérifiez aussi que vous avez activé les [métriques de performance]([LINK_URL_4]) dans les paramètres **Cascade** de vos étapes de transaction.

Sachez toutefois que les données **Core Web Vitals** et **Navigation W3C** ne seront pas disponibles pour la période antérieure à ces activations. Vous pouvez ajuster la période de rapport dans les paramètres de tuile afin de montrer uniquement la période pendant laquelle l'option **Chrome avec des métriques supplémentaires** était activée.

Une fois configurée, la liste de données simple ou le graphique de données simples affiche un graphique reflétant ces métriques. Lisez la légende et survolez le graphique pour en savoir plus sur les étapes. Pour en savoir plus sur les métriques connexes, lisez l'article de notre base de connaissances intitulé [Calcul de la disponibilité et des temps d'arrêt]([LINK_URL_5]).

![Métriques de la liste ou du graphique de données simple]([LINK_URL_6])


### Général

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :

- Temps total, temps de résolution, temps de connexion et temps de téléchargement
- Pourcentage de disponibilité, pourcentage d'indisponibilité (downtime), disponibilité et indisponibilité
- Erreurs confirmées et non confirmées
- Vérifications, alertes et nombre total d'octets
- Pourcentage d'objectif uptime SLA, objectif de temps total SLA, objectif SLA de réponse de l'opérateur et temps de réponse de l'opérateur

![Graphique de données simple présentant des métriques Général]([LINK_URL_7])

### Core Web Vitals

Les moniteurs FPC et les moniteurs de transactions collectent des données [Core Web Vitals]([LINK_URL_8]) lorsque le type de navigateur est configuré sur [Chrome avec des métriques supplémentaires]([LINK_URL_9]).

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :

- First Contentful Paint
- Largest Contentful Paint
- Time To Interactive
- Total Blocking Time
- Cumulative Layout Shift

![Graphique de données simple présentant des métriques Core Web Vitals]([LINK_URL_10])


### Navigation W3C

Les moniteurs FPC et les moniteurs de transactions collectent des données [Navigation W3C]([LINK_URL_11]) et [Core Web Vitals]([LINK_URL_12]) lorsque le type de navigateur est configuré sur [Chrome avec des métriques supplémentaires]([LINK_URL_13]).

Sélectionnez une ou plusieurs des métriques suivantes pour qu'elles s'affichent dans la tuile :
- Début de la requête
- Durée jusqu'au premier octet
- DOM interactive
- DOM terminé
- Load event

![Métriques de navigation W3C de la liste de données simple]([LINK_URL_14])


## Liste ou graphique de données de moniteurs

Sélectionnez les moniteurs ou les groupes de moniteurs et la période, puis les métriques à afficher parmi les options suivantes :

- Objectif uptime SLA et Uptime SLA
- Objectif de temps total SLA, Temps total objectif SLA, Indisponibilité SLA
- Temps SLA de réponse opérateur, Objectif SLA de réponse opérateur
- Temps total, Vérifications, Erreurs confirmées, Erreurs non confirmées
- Pourcentage de disponibilité, Pourcentage downtime (indisponibilité)
- Options Trier par et Montrer les lignes

![Capture d'écran de la tuile Graphique données moniteur]([LINK_URL_15])

![Capture d'écran de la tuile Liste de données de moniteurs]([LINK_URL_16])

## Liste ou graphique de types d'erreurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs, et la période.

![Capture d'écran des tuiles Liste et graphique de types d'erreurs]([LINK_URL_17])

## Liste ou graphique de données de checkpoints

Sélectionnez les moniteurs ou les groupes de moniteurs et la période, puis les métriques à afficher parmi les options suivantes :

- Temps total, Temps de résolution
- Temps de connexion, Temps de téléchargement
- Vérifications, Erreurs confirmées et option Trier par

![Capture d'écran de la tuile Graphique de données de checkpoints]([LINK_URL_18])

![Capture d'écran de la tuile Liste de données de checkpoints]([LINK_URL_19])

## Liste ou graphique multi checkpoint

Sélectionnez les moniteurs ou groupes de moniteurs et la période, puis choisissez la métrique à afficher dans la liste ou le graphique.


![Capture d'écran de la tuile Graphique multi checkpoint]([LINK_URL_20])

![Capture d'écran de la tuile Liste multi checkpoint]([LINK_URL_21])

## Liste ou graphique multi moniteurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs et la période, puis sélectionnez la métrique à afficher dans la liste ou le graphique.

![Capture d'écran de la tuile Graphique multi moniteurs]([LINK_URL_22])

![Capture d'écran de la tuile Liste multi moniteurs]([LINK_URL_23])

## Détails dernière vérification [ANCHOR_2]

Cette tuile indique quand un ou plusieurs moniteurs ou groupes de moniteurs ont été vérifiés pour la dernière fois, et permet de sélectionner la période pour laquelle il faut afficher les données.  
![Capture d'écran de la tuile personnalisée sur les détails de vérification du moniteur ]([LINK_URL_24])

## Journal moniteurs

Sélectionnez le ou les moniteurs ou groupes de moniteurs et la période, puis indiquez comment filtrer les erreurs et précisez si vous souhaitez afficher le rapport dans un fichier exporté.

![Capture d'écran de la tuile Journal moniteurs]([LINK_URL_25])

## Historique des alertes

Cette tuile affiche l'historique des notifications d'alerte par moniteur ou groupe de moniteurs, et permet de filtrer les données par période.

![Capture d'écran de la tuile Historique des alertes]([LINK_URL_26])

## Liste ou graphique de durée des étapes

Cette tuile est disponible pour les moniteurs de transactions et moniteurs d'API multi-étapes, un moniteur à la fois. Elle présente la durée des étapes dans le temps.

![Capture d'écran de la tuile Graphique de durée des étapes]([LINK_URL_27])

## Liste ou graphique de la durée moyenne des étapes

Cette tuile est disponible pour les moniteurs de transactions et moniteurs d'API multi-étapes, un moniteur à la fois. Elle présente la durée moyenne des étapes.

![Capture d'écran de la tuile Graphique de la durée moyenne des étapes]([LINK_URL_28])
