{
  "hero": {
    "title": "Que sont les intégrations ?"
  },
  "title": "Que sont les intégrations ?",
  "summary": "Les intégrations sont des connexions au monde extérieur qui se chargent d'envoyer des messages d'alerte générés par la surveillance Uptrends.",
  "url": "/support/kb/alerter/integrations/que-sont-les-integrations",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/what-are-integrations"
}

Les intégrations sont des connexions au monde extérieur qui se chargent d'envoyer des messages d'alerte générés par la surveillance Uptrends. Chaque fois qu'une vérification déclenche une alerte, selon les paramètres des définitions d'alerte que vous configurez, Uptrends envoie les messages appropriés en utilisant les intégrations que vous avez activées dans vos définitions d'alerte. L'intégration la plus simple est l'intégration des e-mails ; elle crée un e-mail et l'envoie aux destinataires que vous spécifiez. Un autre exemple simple est l'intégration SMS ; elle envoie des SMS aux téléphones portables de vos opérateurs.

## Connexion à des systèmes externes

Outre l'envoi de messages d'alerte à des individus, il est probable que vous voudrez envoyer des informations d'alerte d'Uptrends à d'autres systèmes pour un traitement automatisé. L'envoi des informations d'alerte à des processus automatisés permet de se connecter directement à un système de suivi et de gestion des incidents (par exemple, PagerDuty, Splunk On-Call ou ServiceNow) ou simplement de partager des informations d'alerte dans l'outil de communication de votre équipe (par exemple, dans Slack) ou avec le grand public (par exemple, StatusHub).

Certaines des intégrations disponibles utilisent un format de message texte fixe (e-mail, SMS, téléphone, Slack) tandis que d'autres utilisent le format de message attendu par le système tiers, afin que ce système puisse afficher et traiter les données, provenant d'Uptrends, de la meilleure manière possible (PagerDuty, StatusHub, Splunk On-Call, ServiceNow). Nous avons des notices explicatives disponibles pour tous les systèmes d'intégration tiers pris en charge. Pour trouver la bonne notice, pensez à consulter notre [page principale sur les Intégrations](/integrations).

## Création d'une intégration de webhook personnalisée

Même si Uptrends a une liste croissante d'intégrations prédéfinies, il est possible que vous cherchiez à vous connecter à un système qui n'est pas encore répertorié. La connexion à des systèmes autres que ceux proposés par Uptrends est toujours possible en utilisant la fonction d'intégration personnalisée pour configurer une intégration avec tout système prenant en charge les webhooks, c'est-à-dire s'il dispose d'une API capable de traiter les messages entrants.

Si vous vous connectez à un système tiers, ce système tiers s'attend à ce que le webhook entrant (c'est-à-dire les données envoyées par Uptrends à ce système) utilise un format de message particulier afin de pouvoir le traiter. La documentation du système explique le contenu requis du message, y compris la signification de chaque champ et l'URL à laquelle envoyer le message. L'éditeur d'intégration d'Uptrends vous permet de configurer toutes les données nécessaires.

Vous pouvez également vous connecter à un système qui n'a pas de format de message requis ou préféré. Dans ce cas, utilisez plutôt l'intégration personnalisée intitulée **Intégration Uptrends**. Il a un message préconfiguré qui contient toutes les variables d'alerte disponibles dans Uptrends. Il vous suffit de fournir l'URL de l'API à laquelle vous souhaitez vous connecter.

Pour plus d'informations, lisez cet article qui explique [comment créer une intégration personnalisée](/support/kb/alerter/integrations/integrations-personnalisees), et qui est également utile pour modifier une intégration personnalisable.
