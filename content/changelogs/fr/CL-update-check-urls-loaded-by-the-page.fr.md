{
"title": "Conditions supplémentaires pour la vérification des URL chargées par la page",
"date": "2025-02-19",
"url": "/changelog/fevrier-2025-nouvelles-conditions-verification-url-chargees-par-page",
"translationKey": "https://www.uptrends.com/changelog/february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition"
}

La condition d'erreur [Vérifier les URL chargées par la page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="fr" >}}) vous permet de vérifier si des éléments spécifiques d'une page sont chargés sur votre site web. Ces éléments de page sont les URL qui s'affichent dans votre [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}). Ils comprennent les images, les fichiers et d'autres ressources de votre site web.

Cette condition d'erreur vous permet désormais d'ajouter de nouveaux critères pour vérifier les métriques de chaque élément de page. En cliquant sur le nouveau bouton {{< AppElement type="editbutton" >}} + Ajouter une condition supplémentaire{{< /AppElement >}}, vous pouvez désormais préciser la taille de la réponse en octets, la durée totale en millisecondes (ms) et le code de statut pour les éléments de la page :

![Nouvelles conditions d'erreur pour la vérification des URL chargées par la page](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

Si vous voulez qu'une erreur se déclenche lorsque le chargement de votre image dure plus de deux secondes ou si un fichier produit un code de statut supérieur à 400, vous pouvez définir un critère correspondant.

La condition d'erreur Vérifier les URL chargées par la page est disponible pour les [moniteurs de navigateur ou Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="fr" >}}) et pour les [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}). Notez que pour les moniteurs de transaction, vous devrez sélectionner l'[option Cascade dans une étape]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="fr" >}}) afin de paramétrer ces conditions supplémentaires.