{
  "hero": {
    "title": "Toegang tot de Uptrends API met Powershell"
  },
  "title": "Toegang tot de Uptrends API met Powershell",
  "summary": "Leer hoe u een PowerShell Uptrends' API-verbinding instelt. ",
  "url": "/support/kb/api/toegang-tot-de-uptrends-api-met-powershell",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-powershell",
   "TableOfContents": false
}

Het volgende voorbeeld benadert de Uptrends API en haalt de lijst met Uptrends-controleregels in uw account op. Houd er rekening mee dat u zich moet [registreren voor een set API-specifieke inloggegevens]({{< ref path="/support/kb/api/authentication-v4" lang="nl" >}}) om toegang te krijgen tot onze API, en zorg ervoor dat u die gebruikt in plaats van uw reguliere Uptrends-inloggegevens.

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

Dit laatste statement zet het resultaat in de \`$result\` variabele. U kunt dan verder werken met deze content. Bijvoorbeeld om de check URL voor een specifieke controleregel op te halen:

`$result | Where-Object { $_.Name -eq 'Uptime galacticresorts.com' } | Select Url`
