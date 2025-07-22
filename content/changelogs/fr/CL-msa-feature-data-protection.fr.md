{
"title": "Nouvelle fonctionnalité dans les moniteurs d'API multi-étapes : la protection des données",
"date": "2024-12-18",
"url": "/changelog/decembre-2024-fonctionnalite-protection-donnees-moniteurs-api-multi-etapes",
"translationKey": "https://www.uptrends.com/changelog/december-2024-msa-data-protection-feature"
}

Uptrends collecte tous les résultats de vos moniteurs d'API multi-étapes auprès du serveur de checkpoint, puis les stocke et les rend accessibles directement sur sa plateforme.

Grâce à la fonctionnalité de **protection des données**, vous pouvez désormais empêcher que certaines informations issues du monitoring soient collectées et stockées sur la plateforme d'Uptrends. Cette nouvelle fonction fournit une couche de sécurité supplémentaire, en vous garantissant que les informations sensibles restent à l'intérieur de votre réseau et ne sont pas transmises en externe.

![Case à cocher Protection des données dans le moniteur d'API multi-étapes](/img/content/scr-data-protection-checkbox.min.png)

Par défaut, les cases suivantes sont cochées pour permettre à Uptrends de stocker et d'afficher des informations dans les résultats de votre monitoring d'API multi-étapes :

- Collecter les headers HTTP : Uptrends collecte les en-têtes de requête et de réponse HTTP de votre site web.
- Collecter le contenu de la réponse : Uptrends collecte le contenu des réponses HTTP de votre site web.
- Collecter les adresses IP résolues : Uptrends collecte les détails de connexion relatifs à la résolution des adresses IP de votre site web.

Décocher l'une de ces cases empêche que les informations correspondantes soient envoyées à la plateforme d'Uptrends. À la place, c'est un texte informatif qui s'affiche.

La fonction de **protection des données** est déjà disponible avec les [emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}). Nous élargissons sa mise en œuvre à notre réseau de checkpoints publics, qui inclut le monitoring d'API multi-étapes.

