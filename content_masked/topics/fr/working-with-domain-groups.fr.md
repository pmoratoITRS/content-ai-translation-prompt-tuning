{
  "hero": {
    "title": "Travailler avec les groupes de domaine"
  },
  "title": "Travailler avec les groupes de domaine",
  "summary": "Comprendre vos groupes de domaine et comment les configurer pour le Full Page Check Plus.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/browser-monitoring/travailler-avec-les-groupes-de-domaine",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le  Full Page Check \+ (FPC\+) vous permet d'identifier la source des éléments de la page rapidement. Une page typique comporte de nombreux éléments qui proviennent de fournisseurs différents; par exemple, vous pouvez avoir du contenu provenant d'un CDN, des annonces provenant de Google, et les derniers messages/posts apportés par les plugins de médias sociaux. Avec les groupes de domaine, vous verrez que vous pouvez identifier rapidement les sources des problèmes. Une excellente façon de comprendre la gestion des groupes de domaine est de regarder l'Ensemble par défaut (**Default set**).

[SHORTCODE_1]
**Remarque** : Vous trouverez les informations sur l'affichage des éléments de la page au moyen des groupes de domaine, dans la base de connaissances : [Interpréter les résultats du graphique en cascade]([LINK_URL_1]).
[SHORTCODE_2]

## L'Ensemble par défaut (Default Set) 

Uptrends a créé un ensemble de domaines par défaut. Ont été inclus les domaines les plus courants, donc il se peut que vous n'ayez rien de plus à faire. Bien sûr, nous ne vivons pas dans un monde uniforme, et cet ensemble par défaut peut ne pas répondre à vos besoins. Uptrends vous offre plusieurs options; vous pouvez

-   Modifier l'ensemble par défaut directement (pas recommandé),
-   Copiez l'ensemble par défaut, puis le modifier, ou
-   Créer un nouveau groupe de domaine à partir de zéro.

Avant de commencer à modifier les paramètres du groupe de domaine, prenez un moment pour bien comprendre les parties qui définissent un groupe de domaine.

[SHORTCODE_3]
**Remarque** : Après avoir ouvert l'ensemble par défaut (dans l'étape suivante), vous verrez le bouton [SHORTCODE_5]Ajouter groupe de domaines[SHORTCODE_6] en haut à droite de la page. Nous vous recommandons d'utiliser ce bouton pour dupliquer l’Ensemble par défaut plutôt que de le modifier directement.
[SHORTCODE_4]

### Opening Domain Groups and the Default Set

Lorsque vous ouvrez la page [SHORTCODE_7]Groupes de Domaines[SHORTCODE_8] pour la première fois, vous aurez un groupe de domaine dans la liste appelé Ensemble par défaut (**Default Set**).

Pour accéder à la page [SHORTCODE_9]Groupes de Domaine :[SHORTCODE_10] 

1.  Placer la souris au-dessus de **Compte** du menu [SHORTCODE_11]Principal[SHORTCODE_12] 
2.  Dans les sous-menus cliquez sur **Groupes de Domaines**
3.  Cliquez sur Ensemble par défaut (**Default Set**) pour ouvrir l'éditeur

![]([LINK_URL_2])

### Les groupes prédéfinis

Une fois que vous avez ouvert le Default Set, vous verrez cinq groupes de domaines définis dans la section **Groupes** de la page. Pour chaque groupe, vous pouvez ajouter des domaines supplémentaires en utilisant le bouton [SHORTCODE_13]Ajouter une règle[SHORTCODE_14]. Vous pouvez également exclure une règle en sélectionnant **Exclure** dans la définition des règles ou supprimer une règle en cliquant sur le bouton à droite de la règle à supprimer.

#### 1st party (Votre contenu)

Lorsque vous développez le groupe (cliquez sur le triangle à côté du N**om**), vous remarquerez que, par défaut, les développeurs ont choisi de cocher les cases **Automatiquement inclure tous les types de contenu en provenance de l'URL surveillée** et **Ceci est le contenu interne**. La sélection de ces cases à cocher indique au système d'inclure tout le contenu qui vient de l'URL fourni pour le moniteur. Ce groupe concerne votre contenu. Vous pouvez également avoir d'autres domaines que vous contrôlez qui contribuent au contenu de la page. N’oubliez pas de les ajouter en utilisant le bouton [SHORTCODE_15]Ajouter une règle[SHORTCODE_16].

#### Statistics (Statistiques)

Le contenu analytique fonctionne à l'arrière-plan et les services analytiques contribuent souvent à une mauvaise performance des pages. Vous pouvez ajouter les URL des outils analytiques que vous utilisez. Si vous voulez surveiller Google Analytics, assurez-vous de ne pas sélectionner la case à cocher **Bloquer Google Analytics** sur la page de définition du moniteur.

#### CDN

Parfois, les réseaux de diffusion de contenu (CDN) ne fonctionnent pas ou pas bien. En définissant les URL et les règles pour vos CDN, vous pouvez surveiller leurs performances.

#### Social

Les plugins de médias sociaux ont l'air assez inoffensif, mais fréquemment le contenu des médias sociaux et les boutons d'action peuvent être à l'origine de performances web dégradées. Rajoutez les URL de vos éléments de médias sociaux ici. Uptrends a déjà inclus les cinq URL de médias sociaux les plus fréquemment utilisés.

#### Ads

Nous avons tous vu des sites de pub alléchants vous invitant à cliquer dessus, avec tellement de publicité sur la page que vous renoncez tout simplement à attendre l'affichage des cinq meilleures recettes de cassoulet sur Internet. Ne laissez pas vos fournisseurs d'annonces ralentir votre page; surveiller vos fournisseurs d'annonces en incluant les URL dans la section **Ads**.

#### Ajoutez les vôtres

Bien sûr, vous pouvez ajouter des règles aux groupes prédéfinis, mais l'Ensemble par défaut vous laisse la possibilité d'ajouter jusqu'à trois autres groupes au bas de la page. N'oubliez pas de cliquer sur le bouton [SHORTCODE_17]Enregistrer[SHORTCODE_18] avant de quitter la page.
