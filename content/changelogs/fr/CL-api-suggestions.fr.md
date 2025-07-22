{
"title": "Transformez facilement vos moniteurs de disponibilité en moniteurs d'API dans le Centre d'API",
"date": "2025-04-24",
"url": "/changelog/avril-2025-suggestions-api",
"translationKey": "https://www.uptrends.com/changelog/april-2025-api-suggestions"
}

Le [Centre d'API](https://app.uptrends.com/Hubs/Api) comprend désormais une fonctionnalité qui scanne automatiquement vos moniteurs pour identifier ceux qui peuvent être transformés en [moniteurs d'API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}). Si la fonctionnalité détecte des moniteurs HTTP et HTTPS qui semblent vérifier des points de terminaison API, elle vous propose de créer automatiquement un nouveau moniteur d'API à partir du moniteur original.

Cette fonctionnalité transforme instantanément n'importe quel [moniteur de disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}) en un moniteur d'API entièrement configuré. Le moniteur de disponibilité original n'est ni supprimé ni modifié. Vous pouvez annuler le processus à tout moment si nécessaire. Par ailleurs, vous n'avez pas besoin de tout recréer à partir de zéro. Uptrends se charge de la configuration, en conservant les paramètres des moniteurs d'origine.

Une fois la transformation effectuée, vous pouvez vérifier la configuration et activer le moniteur. Pour en savoir plus, lisez l'article de la base de connaissances intitulé [Hub des moniteurs d’API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="fr" >}}).

![Tuile présentant des suggestions d'API](/img/content/scr-api-suggestions.min.png)