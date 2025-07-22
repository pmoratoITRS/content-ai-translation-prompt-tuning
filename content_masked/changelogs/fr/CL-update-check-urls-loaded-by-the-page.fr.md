{
  "title": "Conditions supplémentaires pour la vérification des URL chargées par la page",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]fevrier-2025-nouvelles-conditions-verification-url-chargees-par-page",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

La condition d'erreur [Vérifier les URL chargées par la page]([LINK_URL_1]) vous permet de vérifier si des éléments spécifiques d'une page sont chargés sur votre site web. Ces éléments de page sont les URL qui s'affichent dans votre [graphique en cascade]([LINK_URL_2]). Ils comprennent les images, les fichiers et d'autres ressources de votre site web.

Cette condition d'erreur vous permet désormais d'ajouter de nouveaux critères pour vérifier les métriques de chaque élément de page. En cliquant sur le nouveau bouton [SHORTCODE_1] + Ajouter une condition supplémentaire[SHORTCODE_2], vous pouvez désormais préciser la taille de la réponse en octets, la durée totale en millisecondes (ms) et le code de statut pour les éléments de la page :

![Nouvelles conditions d'erreur pour la vérification des URL chargées par la page]([LINK_URL_3])

Si vous voulez qu'une erreur se déclenche lorsque le chargement de votre image dure plus de deux secondes ou si un fichier produit un code de statut supérieur à 400, vous pouvez définir un critère correspondant.

La condition d'erreur Vérifier les URL chargées par la page est disponible pour les [moniteurs de navigateur ou Full Page Check]([LINK_URL_4]) et pour les [moniteurs de transactions]([LINK_URL_5]). Notez que pour les moniteurs de transaction, vous devrez sélectionner l'[option Cascade dans une étape]([LINK_URL_6]) afin de paramétrer ces conditions supplémentaires.