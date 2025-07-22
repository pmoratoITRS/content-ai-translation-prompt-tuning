{
  "title": "Automatische Content-Type header in Multi-step API-controleregels",
  "date": "2024-01-17",
  "url": "/changelog/januariy-2024-msa-content-type-header",
  "translationKey": "https://www.uptrends.com/changelog/january-2024-msa-content-type-header"
}

Met ons controleregeltype [Multi-step API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}) kunnen gebruikers rechtstreeks met hun kritieke API's communiceren. Voor sommige monitoringtoepassingen moeten data naar de API worden gestuurd, bijvoorbeeld bij het uitvoeren van POST-requests om een nieuw object te maken, of bij een PUT/PATCH-request om een bestaand object bij te werken. In dergelijke gevallen is het belangrijk om een `Content-Type` header op te nemen om de ontvangende API te informeren over het type data dat binnenkomt (JSON, XML, formuliergegevens, enz.), zodat het weet hoe de request moet worden verwerkt.  Een API retourneert gewoonlijk fouten als het een request body ontvangt zonder een `Content-Type` header.

Tot nu toe moesten dergelijke headers handmatig aan de Multi-step API-controleregelstap(pen) worden toegevoegd. Vanaf deze update detecteren we automatisch het type inhoud en voegen we de juiste 'Content-Type' header toe voor JSON-, XML- of formulierdata-requestbodies. Deze wijziging helpt gebruikers bij het configureren van POST-, PUT- en PATCH-requests in hun Multi-step API-controleregels. 