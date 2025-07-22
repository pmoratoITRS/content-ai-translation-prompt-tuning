{
"hero": {
"title": "Types de navigateurs"
},
"title": "Types de navigateurs",
"summary": "Quels types de navigateurs sont disponibles avec le moniteur Full Page Check ?",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/types-navigateurs",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/browser-types",
"tableofcontents": false
}

Vous pouvez configurer le moniteur Full Page Check (FPC) de façon à utiliser l'un des différents navigateurs disponibles. Le choix du **type de navigateur** se fait soit dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}, soit dans l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} des paramètres du moniteur. Les navigateurs suivants sont disponibles :

- Chrome avec des métriques supplémentaires
- Microsoft Edge

Uptrends actualise les navigateurs utilisés par les [checkpoints]({{< ref path="/checkpoints" lang="fr" >}}) pour que votre vérification s'exécute toujours dans la dernière version disponible du navigateur sélectionné.

{{< callout >}}
**Remarque :** Pour surveiller le comportement de votre site web sur un appareil mobile, vous devez modifier l'[agent utilisateur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="fr"  >}}) dans l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} du moniteur.
{{< /callout >}}

## Chrome avec des métriques supplémentaires {id="chrome-extra-metrics"}

En plus des mesures habituelles, Uptrends peut fournir des informations supplémentaires, comme les [durées de navigation définies par le W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}), les indicateurs [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}), les [captures d'écran successives]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}), et des informations plus détaillées au niveau de l'élément, y compris la version du protocole et les informations TLS. Pour en savoir plus, consultez l'article sur les [métriques et fonctionnalités supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr"  >}}) dans notre base de connaissances.

Les métriques supplémentaires sont disponibles pour les types de navigateurs suivants :

- Chrome avec des métriques supplémentaires
- Microsoft Edge