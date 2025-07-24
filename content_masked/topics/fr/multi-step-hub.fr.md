{
  "hero": {
    "title": "Hub des moniteurs d'API multi-étapes"
  },
  "title": "Hub des moniteurs d'API multi-étapes",
  "summary": "Le hub des moniteurs d'API multi-étapes est le point de départ pour explorer la surveillance d'API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/portail-MSA",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Le **hub des moniteurs d'API multi-étapes (MSA)** vous fournit une vue d'ensemble générale de vos moniteurs MSA et de la configuration de la surveillance multi-étapes. Pour ouvrir cette page, passez par le menu [SHORTCODE_1] API > [SHORTCODE_2] [Explorer la surveillance des API ]([LINK_URL_1]). Dans le menu latéral, vous trouverez des liens vers les articles de notre base de connaissances :

![Hub MSA]([LINK_URL_2])

Ces différents blocs vous renseignent sur votre configuration de la surveillance d'API multi-étapes :

- Le bloc **Monitoring d'API** vous montre le nombre de moniteurs configurés. Cliquez sur le bouton [SHORTCODE_3] Voir tous les moniteurs d'API [SHORTCODE_4] pour ouvrir la vue d'ensemble des moniteurs d'API, ou passez par le menu [SHORTCODE_5] Gérer les moniteurs API [SHORTCODE_6].

- Le bloc **Statut du moniteur d'API** montre le nombre de moniteurs ayant relevé des [erreurs confirmées]([LINK_URL_3]) et contenant des alertes actives. Cliquez sur le bouton [SHORTCODE_7] Afficher l'état du moniteur [SHORTCODE_8] pour ouvrir la page **Statut moniteurs**. Cliquez sur le bouton [SHORTCODE_9] Afficher les alertes en cours [SHORTCODE_10] pour ouvrir la page **Statut d'alerte actuel**.

- Le bloc des moniteurs actifs montre les moniteurs en [mode Simulation et Production]([LINK_URL_4]).

- Le bloc Crédits d'API vous indique le nombre de crédits d'API restants. Pour savoir comment acheter de nouveaux crédits, lisez notre article [Ajout de moniteurs et de crédits]([LINK_URL_5]).

Le hub permet désormais de scanner automatiquement vos moniteurs pour identifier ceux qui peuvent être transformés en [moniteurs d'API]([LINK_URL_6]). Si la fonctionnalité détecte des moniteurs HTTP et HTTPS qui semblent vérifier des points de terminaison API, elle vous propose de créer automatiquement un nouveau moniteur d'API à partir du moniteur original.

Cette fonctionnalité transforme instantanément n'importe quel [moniteur de disponibilité]([LINK_URL_7]) en un moniteur d'API entièrement configuré. Le moniteur de disponibilité original n'est ni supprimé ni modifié. Vous pouvez annuler le processus à tout moment si nécessaire. Par ailleurs, vous n'avez pas besoin de tout recréer à partir de zéro. Uptrends se charge de la configuration, en conservant les paramètres des moniteurs d'origine.

Cliquez sur le bouton **Voir les détails** pour ouvrir une fenêtre contextuelle qui vous permet de transformer un moniteur existant en moniteur d'API. Une fois la transformation effectuée, une autre fenêtre contextuelle s'ouvre pour que vous puissiez vérifier la configuration et activer le nouveau moniteur.