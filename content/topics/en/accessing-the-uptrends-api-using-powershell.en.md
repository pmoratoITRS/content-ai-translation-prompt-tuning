{
  "hero": {
    "title": "Accessing the Uptrends API using Powershell"
  },
  "title": "Accessing the Uptrends API using Powershell",
  "summary": "Learn how to setup a PowerShell Uptrends' API connection. ",
  "url": "/support/kb/api/accessing-the-uptrends-api-using-powershell",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-powershell",
   "TableOfContents": false
}

The following example accesses the Uptrends API and fetches the list of Uptrends monitors in your account. Keep in mind that in order to access our API, you'll need to [register for a set of API-specific credentials]({{< ref path="/support/kb/api/authentication-v4" lang="en" >}}), and make sure to use those rather than your regular Uptrends credentials.

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

That final statement puts the result in the \`$result\` variable. You can then continue working with that content. For example, to retrieve the check URL for a specific monitor:

`$result | Where-Object { $_.Name -eq 'Uptime galacticresorts.com' } | Select Url`
