{
"hero": {
"title": "Accès à l'API d'Uptrends avec cURL"
},
"title": "Accès à l'API d'Uptrends avec cURL",
"summary": "Utilisez cURL pour accéder à l'API d'Uptrends.",
"url": "/support/kb/api/acces-a-l-api-uptrends-avec-curl",
"translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-curl"
}

L'exemple de commande ci-dessous permet d'accéder à l'API d'Uptrends et de récupérer la liste des moniteurs d'Uptrends de votre compte. Pour rappel, l'accès à l'API d'Uptrends nécessite d'obtenir des [identifiants spécifiques à l'API]({{< ref path="/support/kb/api/authentication-v4" lang="fr" >}}), que vous utiliserez ensuite au lieu de vos identifiants Uptrends habituels.

`curl https://api.uptrends.com/v4/Monitor -k --user 9d9f60d1a54ceb34afaf47b3abebde47:1234xxx --header "Accept: application/json"`

{{< callout >}}
**Astuce** : vous n'avez pas le logiciel cURL ? Vous pouvez le télécharger à cette adresse : <https://curl.haxx.se/download.html>.
{{< /callout >}}
