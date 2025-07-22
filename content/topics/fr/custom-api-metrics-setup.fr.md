{
"hero": {
"title": "Configuration de métriques personnalisées"
},
"title": "Configuration de métriques personnalisées",
"summary": "Cet article vous présente les métriques personnalisées et vous explique comment les configurer dans vos moniteurs d'API multi-étapes.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/configuration-des-metriques-personnalisees",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/custom-api-metrics-setup",
"sectionlist": true
}

Chaque jour, les API jouent un rôle crucial pour votre entreprise, votre plateforme et vos services. C'est pourquoi il est essentiel de vérifier régulièrement leur comportement et de valider leurs données. Cet article vous explique comment utiliser les **métriques personnalisées** pour contrôler la disponibilité des API, extraire les données dans les réponses d'API et créer des tableaux ou des listes en temps réel pour analyser ces données.

Les **métriques personnalisées** sont une fonctionnalité des [moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) qui vous permet de récupérer des données numériques spécifiques auprès d'une API interne ou externe.
Vous pouvez stocker les valeurs de chaque point de données capturé dans une [variable de métrique personnalisée]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="fr" >}}) qui vous permettra de visualiser la progression des données.

## Pourquoi utiliser les métriques personnalisées

Imaginez que votre système d'e-commerce repose sur une API qui fournit des informations en temps réel sur votre catalogue de produits. Ces informations peuvent inclure les prix, les données d'inventaire et d'autres données sur les produits.

Imaginez maintenant que vous souhaitiez surveiller le nombre d'articles par produit. Au lieu d'effectuer manuellement un appel d'API à chaque fois, les métriques personnalisées peuvent récupérer directement ces données auprès de la réponse d'API et enregistrer chaque point de données dans des [variables de métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="fr" >}}) :

![Variable de métriques personnalisées sur les produits](/img/content/scr-custom-metrics-products.min.png)

À chaque exécution du moniteur d'API multi-étapes, les valeurs des variables sont contrôlées. Vous pouvez ensuite créer [une liste ou un tableau de métriques personnalisées]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#custom-metrics-list-or-chart" lang="fr" >}}) pour approfondir l'analyse des données ou des tendances, ou pour surveiller vos opérations et vos performances :

![Variable de métrique personnalisée](/img/content/scr-custom-metrics-product-graph.min.png)

Les métriques personnalisées peuvent aussi être utilisées dans différents contextes :

- DevOps : surveillez aisément la santé de votre système ou de votre application en suivant des métriques telles que le nombre d'erreurs enregistrées, le nombre d'utilisateurs simultanés et la vitesse du réseau.
- Opérations informatiques : surveillez les métriques relatives à l'environnement de votre centre de données, comme la température, l'humidité et la santé du système.
- Support informatique : suivez le nombre de demandes d'appels d'assistance en attente, le nombre de tickets et les performances SLA.

## Configurer des métriques personnalisées

Une fois que vous avez [configuré un moniteur d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}) avec une ou plusieurs étapes, vous pouvez configurer des **métriques personnalisées** de deux façons : [en configurant une variable]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#set-using-a-variable" lang="fr" >}}) ou [en configurant un script]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#set-using-script" lang="fr" >}}).

Lorsque vous créez une nouvelle métrique personnalisée, utilisez un nom qui soit facile à lire et qui indique sa fonction. Les noms des métriques et des moniteurs s'affichent dans la liste des métriques personnalisées disponibles une fois qu'ils ont été ajoutés à votre rapport personnalisé sur les données d'API. Vous pouvez donc utiliser les mêmes noms de métriques personnalisées pour représenter des types de données similaires appartenant à différents groupes. Par exemple, une métrique personnalisée appelée `totalSum` peut être utilisée à la fois dans les API produits et dans les API clients. Bien que le nom soit identique, les données représentées correspondent à différents groupes. Uptrends vous recommande de choisir immédiatement le nom définitif. En effet, renommer une métrique personnalisée revient à créer une nouvelle métrique.

### Configurer au moyen d'une variable

Cette méthode vous permet de suivre et d'enregistrer les données provenant de la réponse de l'API sans devoir écrire du code ou un script. Il vous suffit de définir une expression dans une variable et de définir un nom de métrique personnalisée pour utiliser cette variable comme une métrique personnalisée.

Par exemple, voici comment configurer des **métriques personnalisées** pour l'[API Carbon Intensity](https://api.carbonintensity.org.uk/intensity). Les données sur l'intensité (`intensity`) peuvent être surveillées au moyen de la méthode de variable suivante :

{{< Support/storylane url="https://app.storylane.io/demo/1eztu52puc8s" >}}

### Configurer au moyen d'un script

Cette méthode vous permet de rédiger vos propres [scripts]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="fr" >}}) pour contrôler entièrement l'extraction et le traitement des données provenant des réponses d'API.

Pensez à utiliser des [extraits de code pour vos métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#custom-metrics" lang="fr" >}}) et à définir un nom de métrique personnalisée pour utiliser ces données comme une métrique personnalisée.

Par exemple, voici comment configurer des **métriques personnalisées** pour l'[API Carbon Intensity](https://api.carbonintensity.org.uk/intensity). Les données sur l'intensité (`intensity`) peuvent être surveillées au moyen de la méthode de script suivante :

{{< Support/storylane url="https://app.storylane.io/demo/wwoetpfkky65" >}}

Pour en savoir plus sur les extraits de code et les scripts, lisez l'article [Personnalisation des scripts pour les moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="fr" >}}).

{{< callout >}} **Remarque :** Dans un moniteur d'API multi-étapes, vous pouvez déclarer au maximum cinq [variables de métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="fr" >}}). Pour en ajouter d'autres, veuillez contacter notre [équipe de support](/contact). {{< /callout >}}

## Inspecter les données des métriques personnalisées

Une fois votre métrique personnalisée, inspectez les données pour vérifier que le moniteur les récupère et les suit correctement.

Pour inspecter les données de métriques personnalisées que vous suivez :

1. Ouvrez {{< AppElement type="menuitem" >}} API > Gérer les moniteurs API {{< /AppElement >}}.
2. Cliquez sur le lien **Accéder au dashboard** pour le moniteur où vous avez créé la **métrique personnalisée**.
3. Dans la tuile **Journal moniteurs**, cliquez n'importe où sur une ligne pour ouvrir la fenêtre contextuelle **Voir les détails**.

Dans la fenêtre contextuelle, vous pouvez voir les données des métriques personnalisées récupérées lors de la vérification du moniteur. La valeur `CarbonIntensity` est de 85 :

![Données CarbonIntensity dans les métriques personnalisées](/img/content/scr-check-details-popup-carbon-intensity.min.png)

Vous avez directement accès aux valeurs de métriques personnalisées telles qu'elles ont été récupérées par le moniteur d'API multi-étapes.

### Dépannage

Si aucune valeur de métrique personnalisée ne s'affiche, vérifiez ce qui suit :

- Avez-vous ouvert par erreur les résultats d'une vérification effectuée avant la création de la nouvelle métrique personnalisée ?

- Votre métrique personnalisée capture-t-elle des nombres entiers ? Si les données contiennent du texte ou des nombres décimaux (comme `99,9 %` ou `3,1415`), ces données ne sont pas capturées. Actuellement, seuls les nombres entiers sont pris en charge.

- Si un problème s'est produit pendant l'exécution du moniteur d'API multi-étapes, la variable attribuée à votre métrique personnalisée n'a peut-être pas être créée. Vérifiez l'absence d'erreurs dans le nom de la métrique personnalisée ou les variables.

## Afficher les métriques personnalisées dans des dashboards

Pour aller plus loin et utiliser les données sous-jacentes pour détecter avec précision des hausses soudaines de valeurs, vous pouvez afficher les données des métriques personnalisées dans votre dashboard en utilisant le format **Liste ou tableau de métriques personnalisées** :

![Tableau de métriques personnalisées](/img/content/scr-custom-metric-min-max-values.min.png)

Vous pouvez ainsi suivre la tendance de la variable de métrique au fil du temps, en affichant les valeurs minimales, moyennes et maximales. Pour en savoir plus, lisez ces indications (en anglais) : [Custom metrics list or chart]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#custom-metrics-list-or-chart" lang="fr" >}}).

Vous pouvez aussi exporter les données du tableau ou de la liste de métriques personnalisées dans un autre format grâce à la fonctionnalité [Exporter les données d'un dashboard]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="fr" >}}).
