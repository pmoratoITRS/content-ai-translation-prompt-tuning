{
  "hero": {
    "title": "Accès à l'API d'Uptrends avec PowerShell"
  },
  "title": "Accès à l'API d'Uptrends avec PowerShell",
  "summary": "Apprenez à configurer une connexion à l'API d'Uptrends avec PowerShell.",
  "url": "/support/kb/api/acces-a-l-api-uptrends-api-avec-powershell",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-powershell",
   "TableOfContents": false
}

L'exemple de commande ci-dessous permet d'accéder à l'API d'Uptrends et de récupérer la liste des moniteurs d'Uptrends de votre compte. Pour rappel, l'accès à l'API d'Uptrends nécessite d'obtenir des [identifiants spécifiques à l'API]({{< ref path="/support/kb/api/authentication-v4" lang="fr" >}}), que vous utiliserez ensuite au lieu de vos identifiants Uptrends habituels.

```powershell
# Indiquez vos identifiants de connexion Uptrends
$user = "9d9f60d1a54ceb34afaf47b3abebde47" $pass= "1234xxx" 
# Indiquez l'URI de la méthode de la commande d'API à exécuter
$uri = "https://api.uptrends.com/v4/Monitor"
# Compilez ces informations de connexion dans une référence d'identification contenant l'authentification de base 
$passwordValue = ConvertTo-SecureString $pass -AsPlainText -Force  $cred = New-Object System.Management.Automation.PSCredential ($user, $passwordValue)  
# Exécutez la demande
$result = Invoke-RestMethod -Uri $uri -Method Get -Credential $cred -Headers @{ Accept = "application/json" }
```

Cette commande finale place le résultat dans la variable \`$ result\`. Vous pouvez ensuite continuer à travailler avec ce contenu. Par exemple, pour récupérer l'URL de vérification d'un moniteur spécifique :

`$result | Where-Object { $_.Name -eq 'Uptime galacticresorts.com' } | Select Url`
