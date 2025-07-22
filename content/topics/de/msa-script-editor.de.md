{
  "hero": {
    "title": "Der Multi-step API-Skript-Editor"
  },
  "title": "Der Multi-step API-Skript-Editor",
  "summary":"Ein Überblick über den Skript-Editor des Multi-step API-Prüfobjekts",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/msa-skript-editor",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/msa-script-editor"
}

Wie das [Transaktionsprüfobjekt]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) verfügt auch der Prüfobjekttyp Multi-step API über eine Editorversion für die Skript-Ansicht als eine Alternative zum visuellen Standardeditor. Der Skript-Editor ermöglicht genauso wie der visuelle Editor Änderungen an den Schritten des Prüfobjekts, aber im JSON-Skript statt über die Benutzeroberfläche.

## Vorteile des Skript-Editors

Es gibt mehrere Vorteile beim Einsatz eines Skript-Editors gegenüber den Prüfobjektsänderungen über die Benutzeroberfläche:

- Power-User empfinden das direkte Bearbeiten eines Skripts einfacher als das Navigieren durch eine Benutzeroberfläche. Einige Nutzer ziehen eine Arbeitsweise ähnlich dem Einsatz einer Befehlszeile vor.
- Wenn ein Skript verfügbar ist, ist eine Automatisierung möglich, beispielsweise um deine [CI/CD-Prozesse](https://blog.uptrends.com/technology/uptrends-and-your-ci-cd-processes/) einzubauen. Mit der [Uptrends API]({{< ref path="/support/kb/api" lang="de" >}}) kannst du die Schritte des Prüfobjekts im selben Moment aktualisieren, wie du die API aktualisierst, die damit geprüft wird.
- Über den Skript-Editor kannst du eine lokale Kopie der Schritte deines Prüfobjekts erstellen, indem du das Skript einfach kopierst und es in eine lokale Datei einfügst. Eine lokale Kopie bietet eine Versionskontrolle, Sicherungen des Multi-step API-Prüfobjekts und ein einfaches Reproduzieren komplizierter Einrichtungen:

## Wechsel zum Skript-Editor

Rufe den Skript-Editor für ein beliebiges Multi-step API-Prüfobjekt auf, indem du zu den Prüfobjekten wechselst, die Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}} aufrufst und auf die Schaltfläche {{< AppElement type="buttonSecondary" >}} WECHSLE ZUM SKRIPT {{< /AppElement >}} oben rechts klickst. Der Wechsel in und aus dem Skript-Editor löst eine Validierung aus, mit der sichergestellt wird, dass das JSON im Skript korrekt bleibt. Das Skript sieht folgendermaßen aus:

![Der Skript-Editor](/img/content/scr-msa-script-editor.min.png)

## Das Skript verstehen

Wie zu sehen, ist das Skript im Grunde eine JSON-formatierte Reihe einzelner Schritte, die die konfigurierte Request-Methode, URL, Header und Request Body sowie die Authentifizierungsoptionen enthalten. Darüber hinaus enthält jeder Schritt-Eintrag die Definitionen für jegliche Variablen, die aus der Antwort erzeugt wurden, sowie Assertions die zu ihr erstellt wurden. Alle notwendigen Änderungen können direkt im Skript-Editor vorgenommen werden.

Ein einzelner Schritt wird in etwa folgendermaßen aussehen:

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

Das Hinzufügen weiterer Schritte ist genauso einfach wie das Einfügen weiterer Einträge in das Array – mit der vollständigen oben dargestellten Schrittdefinition.

Nach dem Array mit den Schritten, enthält die Schrittdefinition auch Informationen zu [vordefinierten Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined-variables" lang="de" >}}) oder [benutzerdefinierten Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#user-defined-functions" lang="de" >}}), die du eingerichtet hast:

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
