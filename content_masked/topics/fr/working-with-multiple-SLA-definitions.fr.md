{
  "hero": {
    "title": "Travailler avec plusieurs définitions de SLA"
  },
  "title": "Travailler avec plusieurs définitions de SLA",
  "summary": "Vous pouvez surveiller plusieurs SLA à l'aide des définitions SLA et des dashboards personnalisés.",
  "url": "[URL_BASE_TOPICS]dashboards-et-rapports/sla/travailler-avec-plusieurs-definitions-de-sla",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Une seule définition SLA suffit pour la plupart des utilisateurs d'Uptrends. Toutefois, certaines sociétés doivent assurer ou surveiller plusieurs SLA avec différents minimums de pourcentage, de temps de chargement de page ou de temps de réponse opérateur. Pour savoir comment configurer de nouvelles définitions SLA ou modifier la définition de SLA par défaut, lisez l'article [Mettre en place un SLA]([LINK_URL_1]). Si votre SLA est déjà paramétré et que vous souhaitez apprendre comment gérer plusieurs définitions de SLA dans votre compte Uptrends, alors vous êtes au bon endroit.

Uptrends calcule les données chiffrées et la conformité à chaque définition SLA pour chaque moniteur dans votre compte. Il n'est pas nécessaire de lier certains moniteurs à certaines définitions SLA, car vous pouvez voir les données de tous les moniteurs ou groupes de moniteurs selon une définition de SLA. Depuis le dashboard Vue d'ensemble SLA par défaut, vous pouvez changer les définitions et les moniteurs ou groupes de moniteurs. Vous pouvez aussi créer un dashboard personnalisé Vue d'ensemble SLA pour des moniteurs ou groupes de moniteurs concernés par des définitions SLA spécifiques.

[SHORTCODE_1]
**Remarque :** Si vous voyez des tirets et des zéros à la place des données dans votre rapport Vue d'ensemble SLA, c'est parce que le paramétrage de votre tuile/dashboard a entraîné un conflit dans les données et produit des données non valides. Pour en savoir plus sur les causes possibles, lisez l'article de notre base de connaissances intitulé [Données absentes dans Vue d’ensemble SLA]([LINK_URL_2]).
[SHORTCODE_2]

## Changer les définitions de SLA dans le dashboard Vue d'ensemble SLA

Une fois que vous avez créé une définition de SLA supplémentaire, vous pouvez choisir laquelle afficher dans votre dashboard **Vue d'ensemble SLA**. Pour cela, suivez les étapes suivantes :

1. Ouvrez le menu [SHORTCODE_3] Dashboards > Synthetics : Vue d'ensemble SLA [SHORTCODE_4].
2. Cliquez sur les points de suspension [SHORTCODE_5] [SHORTCODE_6] pour ouvrir les paramètres de la tuile.
3. Choisissez une définition SLA dans la liste **SLA basé sur**.
5. Cliquez sur [SHORTCODE_7]Définir[SHORTCODE_8].

Votre tuile se rafraîchit et change le SLA d'après la nouvelle définition. Si la définition de SLA est nouvelle, il est probable que vous voyiez des tirets (-) au lieu de données. Uptrends calcule et stocke les données de SLA en temps réel dès la création de la définition. Vu que la définition est nouvelle, le système ne dispose pas d'une base de données suffisante d'après cette nouvelle définition et les paramètres de date/heure, de sorte que le rapport affiche un tiret plutôt que d'afficher des pourcentages basés sur un ensemble de données incomplet. Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Données absentes dans Vue d’ensemble SLA]([LINK_URL_3]).

## Dashboards personnalisés Vue d'ensemble SLA [ANCHOR_1]

Lorsque vous travaillez avec plusieurs définitions SLA, vous pouvez créer des tuiles distinctes basées sur différentes combinaisons de définitions et de moniteurs SLA dans un dashboard personnalisé. Vous pouvez aussi créer plusieurs dashboards personnalisés d'après différentes combinaisons de définitions SLA et de moniteurs ou groupes de moniteurs.

Pour créer un dashboard SLA personnalisé, vous devez commencer par créer un dashboard personnalisé ou enregistrer une copie du dashboard **Vue d'ensemble SLA** pour ensuite le personnaliser.

### Créer un dashboard personnalisé Vue d'ensemble SLA

1. Ouvrez le menu [SHORTCODE_9] Dashboards > Synthetics : Vue d'ensemble SLA [SHORTCODE_10].
2. Cliquez sur les points de suspension [SHORTCODE_11] [SHORTCODE_12] pour ouvrir les paramètres de la tuile.
3. (Facultatif) Si vous utilisez plusieurs définitions, modifiez la définition SLA dans **SLA basé sur**.
4. Cliquez sur l'onglet [SHORTCODE_13]Groupes et moniteurs[SHORTCODE_14].
5. Décochez ** Utiliser le contexte du dashboard** si la case était cochée, et sélectionnez le ou les moniteurs ou groupes de moniteurs à inclure dans le dashboard personnalisé.
6. Cliquez sur [SHORTCODE_15]Définir[SHORTCODE_16].
7. Cliquez sur l'icône hamburger [SHORTCODE_17][SHORTCODE_18].
8. Cliquez sur [SHORTCODE_19]Enregistrer sous[SHORTCODE_20].
9. Donnez au nouveau dashboard un nom descriptif.
10. Cliquez sur [SHORTCODE_21]Enregistrer[SHORTCODE_22].

Vous avez maintenant un dashboard personnalisé auquel vous pouvez accéder à partir du menu [SHORTCODE_23]Dashboards > Dashboards personnalisés[SHORTCODE_24].

### Créer des tuiles SLA supplémentaires

Au lieu de créer plusieurs dashboards, vous pouvez également créer un dashboard à vues multiples avec des tuiles basées sur différentes combinaisons de définitions de SLA, de moniteurs ou de groupes de moniteurs. Commencez par créer une copie du dashboard SLA défaut en vue de le personnaliser (voir les instructions ci-dessus à partir de l'étape 7). Pour ajouter des tuiles :

1. Ouvrez votre dashboard personnalisé en ouvrant le menu [SHORTCODE_25]Dashboards > Dashboards personnalisés [SHORTCODE_26].
2. Cliquez sur l'icône hamburger [SHORTCODE_27][SHORTCODE_28].
3. Sélectionnez *Ajouter une tuile*.
4. Sélectionnez **Liste de données de moniteurs** dans les types de tuile.
5. Cliquez sur [SHORTCODE_29]Suivant[SHORTCODE_30].
6. Sélectionnez le ou les moniteurs ou groupes de moniteurs que vous souhaitez utiliser pour cette tuile.
7. Cliquez sur [SHORTCODE_31]Terminer[SHORTCODE_32] et la nouvelle tuile est créée.
8. Cliquez sur les points de suspension [SHORTCODE_33] [SHORTCODE_34] pour ouvrir les paramètres de la tuile.
9. Choisissez une définition SLA dans la liste **SLA basé sur**.
10. Cochez les cases correspondant aux champs que vous souhaitez afficher.
11. Ajustez les autres paramètres que vous souhaitez.
12. Cliquez sur [SHORTCODE_35]Définir[SHORTCODE_36].
13. Cliquez sur [SHORTCODE_37]Enregistrer[SHORTCODE_38] dans le menu d'*accès rapide* en haut à droite.

Ajoutez toutes les tuiles nécessaires.
