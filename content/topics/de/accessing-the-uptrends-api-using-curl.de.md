{
  "hero": {
    "title": "Zugriff auf die Uptrends API mit cURL"
  },
  "title": "Zugriff auf die Uptrends API mit cURL",
  "summary": "Verwende cURL, um auf die Uptrends API zuzugreifen.",
  "url": "/support/kb/api/zugriff-auf-die-uptrends-api-mit-curl",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-curl"
}

Das folgende Beispiel greift auf die Uptrends API zu und ruft eine Liste von Uptrends Prüfobjekten deines Accounts ab. Beachte, dass du dich für [API-spezifische Anmeldedaten registrieren musst]({{< ref path="/support/kb/api/authentication-v4" lang="de" >}}), um auf die API zuzugreifen, und stelle sicher, dass du sie verwendest, nicht deine regulären Uptrends Anmeldedaten.

`curl https://api.uptrends.com/v4/Monitor -k --user 9d9f60d1a54ceb34afaf47b3abebde47:1234xxx --header "Accept: application/json"`

{{< callout >}}
**Tipp**: Du hast cURL nicht? Lade es hier herunter: <https://curl.haxx.se/download.html>.
{{< /callout >}}
