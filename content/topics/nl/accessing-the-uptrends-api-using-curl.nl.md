{
  "hero": {
    "title": "Toegang tot de Uptrends API met cURL"
  },
  "title": "Toegang tot de Uptrends API met cURL",
  "summary": "cURL gebruiken voor toegang tot de Uptrends API.",
  "url": "/support/kb/api/toegang-tot-de-uptrends-api-met-curl",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-curl"
}

Het volgende voorbeeld benadert de Uptrends API en haalt de lijst met Uptrends-controleregels in uw account op. Houd er rekening mee dat u zich moet [registreren voor een set API-specifieke inloggegevens]({{< ref path="/support/kb/api/authentication-v4" lang="nl" >}}) om toegang te krijgen tot onze API, en zorg ervoor dat u die gebruikt in plaats van uw reguliere Uptrends-inloggegevens.

`curl https://api.uptrends.com/v4/Monitor -k --user 9d9f60d1a54ceb34afaf47b3abebde47:1234xxx --header "Accept: application/json"`

{{< callout >}}
**Tip**: Heeft u geen cURL? Download deze dan van: <https://curl.haxx.se/download.html>.
{{< /callout >}}
