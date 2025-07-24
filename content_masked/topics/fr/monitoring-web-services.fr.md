{
  "hero": {
    "title": "Surveillance de services web"
  },
  "title": "Surveillance de services web",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/surveillance-de-service-web",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]**Remarque :** les moniteurs **Webservice HTTP et Webservice HTTPS** utilisés pour la surveillance d'API ne sont plus disponibles pour les nouveaux utilisateurs. À la place, Uptrends recommande d'utiliser le [moniteur d'API multi-étapes]([LINK_URL_1]) pour vérifier les comportements de vos API. [SHORTCODE_2]

Les moniteurs Webservice HTTP et Webservice HTTPS font partie des différents [types de moniteurs]([LINK_URL_2]) proposés par Uptrends.

## Quels types de services web sont pris en charge ?

Uptrends prend en charge *REST* et *SOAP*, ainsi que tout service web accessible au moyen des protocoles *HTTP* et *HTTPS.*

## Comment ces services web fonctionnent-ils avec Uptrends ?

- Nous surveillons que le service web renvoie une réponse HTTP 200 OK et nous mesurons le temps de résolution, le temps de connexion, le temps de téléchargement, et le temps total, tout comme avec les moniteurs HTTP(S).
- Le monitoring des services web inclut l'authentification de base, la vérification de contenu, etc.
- La plupart des moniteurs de services web utilisent la méthode POST HTTP pour envoyer des données au serveur lors de l'appel du service web.
- Généralement, les services SOAP requièrent un document XML (enveloppe SOAP) en tant que données POST dans le corps de requête, ainsi qu'un en-tête HTTP appelé SOAPAction.
- Certains services web nécessitent de configurer des en-têtes HTTP pour définir le type de contenu.

**Par exemple** :

- \[INLINE_CODE_1] si les données POST sont des données JSON.
- \[INLINE_CODE_2] ou application/xml si les données POST sont au format XML (ce qui est le format par défaut pour les moniteurs de services web, à la différence des moniteurs HTTP(S) habituels).
