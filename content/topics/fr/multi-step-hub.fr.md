{
"hero": {
"title": "Hub des moniteurs d'API multi-étapes"
},
"title": "Hub des moniteurs d'API multi-étapes",
"summary": "Le hub des moniteurs d'API multi-étapes est le point de départ pour explorer la surveillance d'API multi-étapes.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/portail-MSA",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-hub",
"tableofcontents": false
}

Le **hub des moniteurs d'API multi-étapes (MSA)** vous fournit une vue d'ensemble générale de vos moniteurs MSA et de la configuration de la surveillance multi-étapes. Pour ouvrir cette page, passez par le menu {{< AppElement type="menuitem" >}} API > {{< /AppElement >}} [Explorer la surveillance des API ](https://app.uptrends.com/Hubs/Api). Dans le menu latéral, vous trouverez des liens vers les articles de notre base de connaissances :

![Hub MSA](/img/content/scr-msa-hub.min.png)

Ces différents blocs vous renseignent sur votre configuration de la surveillance d'API multi-étapes :

- Le bloc **Monitoring d'API** vous montre le nombre de moniteurs configurés. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Voir tous les moniteurs d'API {{< /AppElement >}} pour ouvrir la vue d'ensemble des moniteurs d'API, ou passez par le menu {{< AppElement type="menuitem" >}} Gérer les moniteurs API {{< /AppElement >}}.

- Le bloc **Statut du moniteur d'API** montre le nombre de moniteurs ayant relevé des [erreurs confirmées]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}) et contenant des alertes actives. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher l'état du moniteur {{< /AppElement >}} pour ouvrir la page **Statut moniteurs**. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Afficher les alertes en cours {{< /AppElement >}} pour ouvrir la page **Statut d'alerte actuel**.

- Le bloc des moniteurs actifs montre les moniteurs en [mode Simulation et Production]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}).

- Le bloc Crédits d'API vous indique le nombre de crédits d'API restants. Pour savoir comment acheter de nouveaux crédits, lisez notre article [Ajout de moniteurs et de crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}).

Le hub permet désormais de scanner automatiquement vos moniteurs pour identifier ceux qui peuvent être transformés en [moniteurs d'API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}). Si la fonctionnalité détecte des moniteurs HTTP et HTTPS qui semblent vérifier des points de terminaison API, elle vous propose de créer automatiquement un nouveau moniteur d'API à partir du moniteur original.

Cette fonctionnalité transforme instantanément n'importe quel [moniteur de disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}) en un moniteur d'API entièrement configuré. Le moniteur de disponibilité original n'est ni supprimé ni modifié. Vous pouvez annuler le processus à tout moment si nécessaire. Par ailleurs, vous n'avez pas besoin de tout recréer à partir de zéro. Uptrends se charge de la configuration, en conservant les paramètres des moniteurs d'origine.

Cliquez sur le bouton **Voir les détails** pour ouvrir une fenêtre contextuelle qui vous permet de transformer un moniteur existant en moniteur d'API. Une fois la transformation effectuée, une autre fenêtre contextuelle s'ouvre pour que vous puissiez vérifier la configuration et activer le nouveau moniteur.