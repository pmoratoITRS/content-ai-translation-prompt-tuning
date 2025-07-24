{
  "hero": {
    "title": "Protection des données dans les moniteurs d'API multi-étapes"
  },
  "title": "Protection des données dans les moniteurs d'API multi-étapes",
  "summary": "Cet article vous explique comment vos informations sont protégées dans les moniteurs d'API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/protection-donnees-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false,
  "sectionlist": "true"
}

Lorsque vous utilisez un moniteur synthétique dans Uptrends, le serveur de l'emplacement de checkpoint effectue des tests de monitoring. Uptrends récupère tous les résultats de surveillance au niveau du serveur du checkpoint, puis les enregistre directement sur sa plateforme.

La plupart des entreprises appliquent une réglementation stricte concernant la confidentialité des données et interdisent de récupérer ou d'envoyer des données sensibles, quelle que soit leur forme. Grâce à la fonction de **protection des données**, vous pouvez empêcher que certains détails de la vérification soient collectés et enregistrés par Uptrends. Cette fonctionnalité fournit une couche de sécurité supplémentaire, en vous garantissant que les informations sensibles ne sont pas transmises en externe (ou sortent du serveur du checkpoint).

![Cases à cocher pour la protection des données dans le moniteur d'API multi-étapes]([LINK_URL_1])

Par défaut, les informations suivantes sont récupérées et affichées dans les résultats de votre monitoring d'API multi-étapes :

- En-têtes de requête et de réponse HTTP de votre site web
- Contenu de la réponse HTTP de votre site web
- Détails de connexion relatifs à la résolution des adresses IP de votre site web

Décocher l'une de ces cases empêche que les informations correspondantes soient envoyées à la plateforme d'Uptrends. À la place, un message s'affiche pour indiquer que ces données ne sont pas collectées en vertu de la politique de protection des données de votre entreprise.

![Collecte désactivée grâce à la protection des données dans les moniteurs MSA]([LINK_URL_2])

## Articles liés

Pour en savoir sur la protection des données dans les emplacements privés, lisez [cet article de notre base de connaissances]([LINK_URL_3]).
