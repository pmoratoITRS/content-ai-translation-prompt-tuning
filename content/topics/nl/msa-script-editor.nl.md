{
  "hero": {
    "title": "Multi-step API-scripteditor"
  },
  "title": "Multi-step API-scripteditor",
  "summary":"Een overzicht van de scripteditor voor Multi-step API-controleregels",
  "url": "support/kb/synthetic-monitoring/api-monitoring/msa-scripteditor",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/msa-script-editor"
}

Net als [transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}}) bevat het controleregeltype Multi-step API een scriptweergave-editor als een alternatief voor de standaard visuele editor. Met de scripteditor kunt u wijzigingen aanbrengen in de stappen van uw controleregel, net zoals met de visuele editor, maar in een JSON-script in plaats van in de gebruikersinterface. 

## Voordelen van de scripteditor

Het gebruik van een scripteditor heeft verschillende voordelen vergeleken met het aanbrengen van wijzigingen in de controleregel via de gebruikersinterface:

- Ervaren gebruikers vinden het misschien gemakkelijker om wijzigingen rechtstreeks in een script aan te brengen dan door een gebruikersinterface te navigeren. Sommige gebruikers geven de voorkeur aan een ervaring die lijkt op het gebruik van een command line. 
- Het beschikbaar hebben van een script maakt automatisering mogelijk, bijvoorbeeld om uw [CI/CD-proces](https://blog.uptrends.com/technology/uptrends-and-your-ci-cd-processes/) te accomoderen. Met behulp van de [Uptrends API]({{< ref path="/support/kb/api" lang="nl" >}}) kunt u de stappen van de controleregel bijwerken op hetzelfde moment dat u de API bijwerkt die het controleert. 
- Met de scripteditor kunt u een lokale kopie van de stappen in uw controleregel maken door het script eenvoudigweg te kopiëren en in een lokaal bestand te plakken. Het bewaren van een lokale kopie maakt versiebeheer, back-ups van uw multi-step API-controleregels en eenvoudige replicatie van gecompliceerde set-ups mogelijk.

## Omschakelen naar de scripteditor

U kunt bij elke Multi-step API-controleregel omschakelen naar de scripteditor door naar de controleregelopties te gaan, naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}} te gaan en rechtsboven te klikken op de knop {{< AppElement type="buttonSecondary" >}} NAAR SCRIPT SCHAKELEN {{< /AppElement >}}. Omschakelen van en naar de scripteditor activeert validatie, dus zorg ervoor dat de JSON in de scriptweergave geldig blijft. Het script zal er als volgt uitzien:

![De scripteditor](/img/content/scr-msa-script-editor.min.png)

## Het script begrijpen

Zoals u kunt zien, is het script in wezen een JSON-geformatteerde reeks van afzonderlijke stappen, met hun request method, URL, alle headers en request body die u heeft geconfigureerd, en de authenticatie-opties. Bovendien bevat elke stap-entry de definities voor alle variabelen die zijn gemaakt van of assertions over de response. Alle noodzakelijke veranderingen kunnen direct in de scripteditor worden aangebracht.

Een individuele stap ziet er ongeveer zo uit:

```json
{
      "StepType": "HttpRequest",
      "Url": "http://galacticresorts.com/api/Destinations",
      "Method": "GET",
      "BodyType": "Raw",
      "RequestHeaders": [
        {
          "Key": "accept",
          "Value": "application/json"
        }
      ],
      "Variables": [
        {
          "Source": "ResponseBodyJson",
          "Property": "[0].ProductId",
          "Name": "ProductId",
          "Arguments": []
        }
      ],
      "Assertions": [
        {
          "Source": "ResponseBodyJson",
          "Property": "[0].ProductId",
          "Comparison": "DoesNotEqual",
          "TargetValue": "100"
        }
      ],
      "Name": "Get destinations",
      "UseFixedClientCertificate": false,
      "Authentication": {
        "Id": "5ef65980-8577-4d8c-b359-91551feef03d",
        "AuthenticationType": "None",
        "PasswordSpecified": false
      },
      "IgnoreCertificateErrors": false,
      "Encoding": "Utf8",
      "RetryUntilSuccessful": false,
      "MaxAttempts": 0,
      "discriminator": "HttpRequestStepV2"
    }
```

Het toevoegen van extra stappen is net zo eenvoudig als het toevoegen van extra entries aan de array, met behulp van de volledige stapdefinitie zoals hierboven beschreven. 

Na de array met de stappen, bevat de stapdefinitie ook informatie over eventuele [voorgedefinieerde variabelen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined-variables" lang="nl" >}}) of [door de gebruiker gedefinieerde functies]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#user-defined-functions" lang="nl" >}}) die u heeft ingesteld:

```json
"PredefinedVariables": [
    {
      "Key": "examplePredefinedVariable",
      "Value": "example value"
    }
  ],
  "UserDefinedFunctions": [
    {
      "Mapping": {
        "Error": "Red",
        "Ok": "Green"
      },
      "Name": "exampleMapping",
      "discriminator": "UserDefinedFunctionMapping"
    }
  ]
```