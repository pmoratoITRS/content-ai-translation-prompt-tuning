{
  "title": "Prise en charge de certaines versions HTTP dans les étapes des moniteurs d'API multi-étapes",
  "date": "2025-04-03",
  "url": "[URL_BASE_CHANGELOG]avril-2025-versions-http-dans-moniteurs-api-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Vous pouvez désormais préciser une version HTTP pour chaque étape d'un moniteur d'API multi-étapes. Cette option vous permet de contrôler la version HTTP utilisée par les serveurs de checkpoint lors de l'exécution de requêtes :

![Version HTTP]([LINK_URL_1])

Par défaut, l'option **Version HTTP** est décochée, ce qui signifie que le serveur utilisera automatiquement la plus récente version HTTP disponible, et au moins la version HTTP/1.1. Actuellement, la version HTTP/3 est disponible pour certains emplacements de checkpoints, dont la liste sera élargie prochainement.

De façon similaire, la configuration HTTP vous permet de sélectionner uniquement une version, tandis que la configuration TLS prend plusieurs versions en charge. En effet, le protocole TLS inclut une négociation de version lors du processus de connexion, ce qui n'est pas le cas avec le protocole HTTP/3 qui nécessite qu'une version spécifique soit définie.