{
"hero": {
"title": "Conditions d'erreur : vérifier les URL chargées par la page"
},
"title": "Conditions d'erreur : vérifier les URL chargées par la page",
"summary": "Comment utiliser la condition d'erreur Vérifier les URL chargées par la page",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-verifier-url",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-url-check",
"tableofcontents": true
}

Les moniteurs basés sur navigateur, comme les [moniteurs Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) et les [moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}), chargent vos pages dans un navigateur réel. Lors du chargement, le navigateur génère un [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) qui liste l'ensemble des éléments et des ressources chargés sur votre page web.

Ces éléments peuvent inclure du contenu interne, comme le document HTML original, des images, des vidéos et d'autres médias hébergés sur le même réseau. Ils peuvent aussi inclure des contenus tiers ou des ressources externes, comme les scripts de surveillance externe ou les données d'analyse. Chacun de ces éléments correspond à une entrée distincte dans le graphique en cascade, avec sa propre URL de requête et ses métriques relatives au temps de chargement.

## Condition d'erreur Vérifier les URL chargées par la page

La [condition d'erreur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}})  **Vérifier les URL chargées par la page** vérifie si des éléments spécifiques d'une page sont chargés sur votre site web. Elle vérifie si l'URL de requête ou ces éléments apparaissent ou non dans le graphique en cascade.

Par exemple, imaginons que vous souhaitiez vérifier si le [Real User Monitoring d'Uptrends]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="fr" >}}) se charge sur une page. En ajoutant la condition d'erreur **Vérifier les URL chargées par la page**, vous ordonnez au moniteur de vérifier si l'URL de requête ou des éléments du graphique en cascade correspondent à `hit.uptrends.com/.*`.

Par ailleurs, cette condition d'erreur vous permet d'indiquer des critères pour vérifier les métriques de chaque URL de requête. Par exemple, si vous voulez détecter des erreurs lorsque le chargement de votre image `uptrends.png` dure plus de deux secondes, ou si un fichier produit un code de statut supérieur à 400, vous pouvez définir un critère correspondant.

## Configurer la condition d'erreur Vérifier les URL chargées par la page

Pour vérifier si un élément spécifique d'une page est visible sur votre site web, vous devez ajouter une condition d'erreur du type **Vérifier les URL chargées par la page** :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Sélectionnez le moniteur au moyen duquel vous voulez vérifier l'URL de requête.
3. Ouvrez l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}}.
4. Dans la condition d'erreur **Vérifier les URL chargées par la page**, cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} + Nouvelle vérification {{< /AppElement >}}.
5. Sélectionnez un type d'erreur pour déterminer si le moniteur doit générer une erreur lorsque l'URL de requête s'affiche ou ne s'affiche pas dans le graphique en cascade.
6. Indiquez l'URL de requête dans le champ de saisie du texte. Vous pouvez utiliser des expressions régulières.
7. (Facultatif) Pour ajouter de nouveaux critères de vérification d'une URL de requête, cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} \+ Ajouter une condition supplémentaire {{< /AppElement >}}. Configurez ensuite vos conditions en utilisant les options disponibles :

- Sélectionnez la **taille de la réponse**, l'opérateur de comparaison approprié et la valeur en octets.
- Sélectionnez le **temps total**, l'opérateur de comparaison approprié et la valeur en millisecondes.
- Sélectionnez le **code de statut**, l'opérateur de comparaison approprié et la valeur.

8. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements apportés.

![Nouvelles conditions d'erreur pour la vérification des URL chargées par la page](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

## Exemples

### Chargement du script RUM d'Uptrends sur le site web

L'exemple ci-dessous montre la condition d'erreur permettant de vérifier si le script RUM d'Uptrends a été correctement configuré. Si l'URL de requête `hit.uptrends.com/.*` n'est pas dans la liste des éléments de page chargés, le moniteur générera [une erreur]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}).

![Vérification d'URL : RUM d'Uptrends](/img/content/scr-error-conditions-url-check.min.png)

### Chargement d'une image sur le site web

L'exemple ci-dessous montre la condition d'erreur permettant de vérifier si l'URL de requête, `stars.png`, s'affiche dans la liste des éléments de page chargés en moins de 1 000 millisecondes. Si le temps de chargement de l'URL dépasse le temps total, le moniteur générera [une erreur]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}).

![Vérification d'URL : Stars.png](/img/content/scr-error-conditions-url-check-image.min.png)