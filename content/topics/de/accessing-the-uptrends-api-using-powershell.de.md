{
  "hero": {
    "title": "Zugriff auf die Uptrends API mit Powershell"
  },
  "title": "Zugriff auf die Uptrends API mit Powershell",
  "summary": "Erfahre, wie du eine PowerShell Uptrends API-Verbindung einrichtest. ",
  "url": "/support/kb/api/zugriff-auf-die-uptrends-api-mit-powershell",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-powershell",
   "TableOfContents": false
}

Das folgende Beispiel greift auf die Uptrends API zu und ruft eine Liste von Uptrends Prüfobjekten deines Accounts ab. Beachte, dass du dich für [API-spezifische Anmeldedaten registrieren musst]({{< ref path="/support/kb/api/authentication-v4" lang="de" >}}), um auf die API zuzugreifen, und stelle sicher, dass du sie verwendest, nicht deine regulären Uptrends Anmeldedaten.

```powershell
# Specify your Uptrends login info here 
$user = "9d9f60d1a54ceb34afaf47b3abebde47" $pass= "1234xxx" 
# URI to the API method you want to execute 
$uri = "https://api.uptrends.com/v4/Monitor"  
# Compile the login info into credentials containing basic authentication 
$passwordValue = ConvertTo-SecureString $pass -AsPlainText -Force  $cred = New-Object System.Management.Automation.PSCredential ($user, $passwordValue)  
# Execute the request 
$result = Invoke-RestMethod -Uri $uri -Method Get -Credential $cred -Headers @{ Accept = "application/json" }
```

Diese letzte Anweisung liefert das Ergebnis in der Variablen '$result'. Du kannst dann mit diesen Inhalten weiterarbeiten. Um beispielsweise die Prüfungs-URL für ein bestimmtes Prüfobjekt abzurufen:

`$result | Where-Object { $_.Name -eq 'Uptime galacticresorts.com' } | Select Url`
