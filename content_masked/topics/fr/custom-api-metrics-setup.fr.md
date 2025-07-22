{
  "hero": {
    "title": "Configuration de métriques personnalisées"
  },
  "title": "Configuration de métriques personnalisées",
  "summary": "Cet article vous présente les métriques personnalisées et vous explique comment les configurer dans vos moniteurs d'API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/configuration-des-metriques-personnalisees",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Chaque jour, les API jouent un rôle crucial pour votre entreprise, votre plateforme et vos services. C'est pourquoi il est essentiel de vérifier régulièrement leur comportement et de valider leurs données. Cet article vous explique comment utiliser les **métriques personnalisées** pour contrôler la disponibilité des API, extraire les données dans les réponses d'API et créer des tableaux ou des listes en temps réel pour analyser ces données.

Les **métriques personnalisées** sont une fonctionnalité des [moniteurs d'API multi-étapes]([LINK_URL_1]) qui vous permet de récupérer des données numériques spécifiques auprès d'une API interne ou externe.
Vous pouvez stocker les valeurs de chaque point de données capturé dans une [variable de métrique personnalisée]([LINK_URL_2]) qui vous permettra de visualiser la progression des données.

## Pourquoi utiliser les métriques personnalisées

Imaginez que votre système d'e-commerce repose sur une API qui fournit des informations en temps réel sur votre catalogue de produits. Ces informations peuvent inclure les prix, les données d'inventaire et d'autres données sur les produits.

Imaginez maintenant que vous souhaitiez surveiller le nombre d'articles par produit. Au lieu d'effectuer manuellement un appel d'API à chaque fois, les métriques personnalisées peuvent récupérer directement ces données auprès de la réponse d'API et enregistrer chaque point de données dans des [variables de métriques personnalisées]([LINK_URL_3]) :

![Variable de métriques personnalisées sur les produits]([LINK_URL_4])

À chaque exécution du moniteur d'API multi-étapes, les valeurs des variables sont contrôlées. Vous pouvez ensuite créer [une liste ou un tableau de métriques personnalisées]([LINK_URL_5]) pour approfondir l'analyse des données ou des tendances, ou pour surveiller vos opérations et vos performances :

![Variable de métrique personnalisée]([LINK_URL_6])

Les métriques personnalisées peuvent aussi être utilisées dans différents contextes :

- DevOps : surveillez aisément la santé de votre système ou de votre application en suivant des métriques telles que le nombre d'erreurs enregistrées, le nombre d'utilisateurs simultanés et la vitesse du réseau.
- Opérations informatiques : surveillez les métriques relatives à l'environnement de votre centre de données, comme la température, l'humidité et la santé du système.
- Support informatique : suivez le nombre de demandes d'appels d'assistance en attente, le nombre de tickets et les performances SLA.

## Configurer des métriques personnalisées

Une fois que vous avez [configuré un moniteur d'API multi-étapes]([LINK_URL_7]) avec une ou plusieurs étapes, vous pouvez configurer des **métriques personnalisées** de deux façons : [en configurant une variable]([LINK_URL_8]) ou [en configurant un script]([LINK_URL_9]).

Lorsque vous créez une nouvelle métrique personnalisée, utilisez un nom qui soit facile à lire et qui indique sa fonction. Les noms des métriques et des moniteurs s'affichent dans la liste des métriques personnalisées disponibles une fois qu'ils ont été ajoutés à votre rapport personnalisé sur les données d'API. Vous pouvez donc utiliser les mêmes noms de métriques personnalisées pour représenter des types de données similaires appartenant à différents groupes. Par exemple, une métrique personnalisée appelée [INLINE_CODE_1] peut être utilisée à la fois dans les API produits et dans les API clients. Bien que le nom soit identique, les données représentées correspondent à différents groupes. Uptrends vous recommande de choisir immédiatement le nom définitif. En effet, renommer une métrique personnalisée revient à créer une nouvelle métrique.

### Configurer au moyen d'une variable

Cette méthode vous permet de suivre et d'enregistrer les données provenant de la réponse de l'API sans devoir écrire du code ou un script. Il vous suffit de définir une expression dans une variable et de définir un nom de métrique personnalisée pour utiliser cette variable comme une métrique personnalisée.

Par exemple, voici comment configurer des **métriques personnalisées** pour l'[API Carbon Intensity]([LINK_URL_10]). Les données sur l'intensité ([INLINE_CODE_2]) peuvent être surveillées au moyen de la méthode de variable suivante :

{{[HTML_TAG_1]}}

### Configurer au moyen d'un script

Cette méthode vous permet de rédiger vos propres [scripts]([LINK_URL_11]) pour contrôler entièrement l'extraction et le traitement des données provenant des réponses d'API.

Pensez à utiliser des [extraits de code pour vos métriques personnalisées]([LINK_URL_12]) et à définir un nom de métrique personnalisée pour utiliser ces données comme une métrique personnalisée.

Par exemple, voici comment configurer des **métriques personnalisées** pour l'[API Carbon Intensity]([LINK_URL_13]). Les données sur l'intensité ([INLINE_CODE_3]) peuvent être surveillées au moyen de la méthode de script suivante :

{{[HTML_TAG_2]}}

Pour en savoir plus sur les extraits de code et les scripts, lisez l'article [Personnalisation des scripts pour les moniteurs d'API multi-étapes]([LINK_URL_14]).

[SHORTCODE_1] **Remarque :** Dans un moniteur d'API multi-étapes, vous pouvez déclarer au maximum cinq [variables de métriques personnalisées]([LINK_URL_15]). Pour en ajouter d'autres, veuillez contacter notre [équipe de support]([LINK_URL_16]). [SHORTCODE_2]

## Inspecter les données des métriques personnalisées

Une fois votre métrique personnalisée, inspectez les données pour vérifier que le moniteur les récupère et les suit correctement.

Pour inspecter les données de métriques personnalisées que vous suivez :

1. Ouvrez [SHORTCODE_3] API > Gérer les moniteurs API [SHORTCODE_4].
2. Cliquez sur le lien **Accéder au dashboard** pour le moniteur où vous avez créé la **métrique personnalisée**.
3. Dans la tuile **Journal moniteurs**, cliquez n'importe où sur une ligne pour ouvrir la fenêtre contextuelle **Voir les détails**.

Dans la fenêtre contextuelle, vous pouvez voir les données des métriques personnalisées récupérées lors de la vérification du moniteur. La valeur [INLINE_CODE_4] est de 85 :

![Données CarbonIntensity dans les métriques personnalisées]([LINK_URL_17])

Vous avez directement accès aux valeurs de métriques personnalisées telles qu'elles ont été récupérées par le moniteur d'API multi-étapes.

### Dépannage

Si aucune valeur de métrique personnalisée ne s'affiche, vérifiez ce qui suit :

- Avez-vous ouvert par erreur les résultats d'une vérification effectuée avant la création de la nouvelle métrique personnalisée ?

- Votre métrique personnalisée capture-t-elle des nombres entiers ? Si les données contiennent du texte ou des nombres décimaux (comme [INLINE_CODE_5] ou [INLINE_CODE_6]), ces données ne sont pas capturées. Actuellement, seuls les nombres entiers sont pris en charge.

- Si un problème s'est produit pendant l'exécution du moniteur d'API multi-étapes, la variable attribuée à votre métrique personnalisée n'a peut-être pas être créée. Vérifiez l'absence d'erreurs dans le nom de la métrique personnalisée ou les variables.

## Afficher les métriques personnalisées dans des dashboards

Pour aller plus loin et utiliser les données sous-jacentes pour détecter avec précision des hausses soudaines de valeurs, vous pouvez afficher les données des métriques personnalisées dans votre dashboard en utilisant le format **Liste ou tableau de métriques personnalisées** :

![Tableau de métriques personnalisées]([LINK_URL_18])

Vous pouvez ainsi suivre la tendance de la variable de métrique au fil du temps, en affichant les valeurs minimales, moyennes et maximales. Pour en savoir plus, lisez ces indications (en anglais) : [Custom metrics list or chart]([LINK_URL_19]).

Vous pouvez aussi exporter les données du tableau ou de la liste de métriques personnalisées dans un autre format grâce à la fonctionnalité [Exporter les données d'un dashboard]([LINK_URL_20]).
