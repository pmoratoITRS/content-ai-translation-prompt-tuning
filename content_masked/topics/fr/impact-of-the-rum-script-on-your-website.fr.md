{
  "hero": {
    "title": "Impact du script du RUM sur votre site web"
  },
  "title": "Impact of the RUM script on your website",
  "summary": "Le script du Real User Monitoring n'impacte pas le temps de chargement de votre site car il s'effectue de manière asynchrone. Apprenez-en plus ici.",
  "url": "[URL_BASE_TOPICS]rum/impact-du-script-du-rum-sur-votre-site-web",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Vous avez peut-être déjà un certain nombre de scripts sur votre site, et souhaiter collecter des données de RUM signifie qu'il faut ajouter un autre script aux pages de votre site. Cependant, nous avons mis en place un certain nombre de choses pour s'assurer que l'impact d'avoir encore un autre script sur votre site est réduit à pratiquement zéro. Plus important encore, le petit script que vous devez insérer dans vos pages Web effectuera son travail de manière asynchrone. Cela signifie qu'il n'entraînera aucun retard dans le chargement ou le rendu de votre page dans le navigateur : il n'y aura pas d'impact sur le temps de chargement perçu de votre site.

Ensuite, nous nous sommes assurés que le script supplémentaire que nous devons charger provient d'un emplacement très proche de l'endroit où se situent vos utilisateurs finaux. Nous avons plusieurs emplacements sur la plupart des continents, ce qui réduira au minimum la latence. Au fur et à mesure que vos utilisateurs parcourent votre site, le navigateur renverra les données qu'il recueille au même endroit, en veillant à ce que les données soient livrées rapidement en utilisant la même connexion sans provoquer de retards.

Enfin, nous utilisons une connexion HTTPS par défaut pour charger et envoyer les données. Cependant, si votre site est généralement chargé via HTTP et que vous souhaitez éviter les essais supplémentaires de démarrage d'une connexion sécurisée avec nous, il existe une option pour régler sur HTTP par défaut, bien que nous vous recommandons d'utiliser des connexions sécurisées chaque fois que vous le pouvez.
