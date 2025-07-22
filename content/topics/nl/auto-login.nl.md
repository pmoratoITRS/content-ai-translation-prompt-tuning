{
  "hero": {
    "title": "Automatisch inloggen"
  },
  "title": "Automatisch inloggen",
  "summary": "Bekijk welke URLs u kunt bookmarken om automatisch in te loggen in Uptrends.",
  "url": "/support/kb/basisprincipes/automatisch-inloggen",
  "translationKey": "https://www.uptrends.com/support/kb/basics/auto-login"
}

## Direct inloggen/automatisch inloggen (met gebruikersnaam/wachtwoord in een bookmarked URL)

U kunt de volgende URL gebruiken om direct in te loggen op uw Uptrends-account:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>`

U hebt ook de mogelijkheid de URL van een dashboard te specificeren om **meteen naar dat dashboard te gaan** nadat u hebt ingelogd. Om bijvoorbeeld het dashboard Operations te laden, gebruikt u:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>&returnurl=/Report/Operations`

## Encodering van speciale tekens

Als uw gebruikersnaam of wachtwoord speciale tekens bevat, moet u deze encoderen in de URL. De gebruikersnaam 'Maël' bijvoorbeeld, moet gewijzigd worden in `Ma%C3%ABl`en het wachtwoord '123@GZ!98' in `123%40GZ%2198`. Bij het eerste voorbeeld hierboven zou de URL er als volgt uitzien met deze gebruikersnaam en wachtwoord:

`https://app.uptrends.com/Account/DirectLogin?username=Ma%C3%ABl&password=123%40GZ%2198`

{{< callout >}}
**Opmerking:** Meer informatie over tekenencodering en een volledige lijst met tekens kunt u vinden op de website van w3schools [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).
{{< /callout >}}
