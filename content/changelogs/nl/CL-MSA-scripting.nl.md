{
  "title": "Pre-request en post-response scripting in Multi-step API-controleregels",
  "date": "2024-07-03",
  "url": "/changelog/juli-2024-msa-scripting",
  "translationKey": "https://www.uptrends.com/changelog/july-2024-msa-scripting"
}

We hebben [aangepaste pre-request en post-response scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}}) ingeschakeld voor stappen in [Multi-step API-controleregels]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}). Het controleregeltype Multi-step API ondersteunt veel ingebouwde opties om requests te configureren en de response af te handelen, maar voor sommige gebruiksscenario's kan extra flexibiliteit of functionaliteit nodig zijn. Met de nieuwe scriptingtabbladen kunnen gebruikers JavaScript-code toepassen en uitvoeren op de request en response voor elke stap, inclusief speciale functies voor interactie met de rest van de controleregelinstellingen.

![Voorbeeld MSA pre-request script](/img/content/scr-msa-prerequest-script.min.png)

Met wat scripting zorgt dit voor maximale flexibiliteit om de request- of response-afhandeling precies zo te configureren als u nodig heeft.