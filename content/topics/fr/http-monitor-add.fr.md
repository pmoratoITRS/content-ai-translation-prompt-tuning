{
"hero": {
"title": "Ajouter un moniteur HTTP(S) ou Webservice HTTP(S)"
},
"title": "Ajouter un moniteur HTTP(S) ou Webservice HTTP(S)",
"summary": "Cet article vous explique comment ajouter un moniteur HTTP(S) ou Webservice HTTP(S).",
"url": "/support/kb/surveillance-synthetique/uptime-monitoring/http-et-https/ajouter-moniteur-http",
"translationKey": "https://www.uptrends.com/support/kb/http-and-https/http-monitor-add",
"tableofcontents": false
}

Pour créer un moniteur HTTP ou HTTPS :

1. Dans le menu, ouvrez {{< AppElement type="menuitem" >}} Disponibilité > Gérer les moniteurs de disponibilité {{< AppElement type="iconAdd" >}} {{< /AppElement >}} {{< /AppElement >}}.
2. Sélectionnez le type de moniteur **HTTP** ou **HTTPS**.
3. Cliquez sur le bouton {{< AppElement type="button" >}} Choisir {{< /AppElement >}}.
4. Dans l'éditeur de moniteur, précisez le nom du moniteur dans le champ **Nom**.
5. Configurez les [paramètres du moniteur]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview#monitor-settings" lang="fr" >}}) selon vos besoins.
6. Saisissez l'**URL** du site web que vous voulez surveiller dans le champ **URL**. Vérifiez que les préfixes, `http://` pour le moniteur HTTP et `https://` pour le moniteur HTTPS, sont correctement précisés.
7. Pour personnaliser davantage votre monitoring, vous pouvez configurer des [paramètres avancés]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-and-https-overview#advanced-http-settings" lang="fr" >}}).
8. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.