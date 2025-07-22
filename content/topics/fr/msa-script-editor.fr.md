{
"hero": {
"title": "Éditeur de script pour les API multi-étapes"
},
"title": "Éditeur de script pour les API multi-étapes",
"summary":"Une présentation de l'éditeur de script pour les API multi-étapes",
"url": "/support/kb/synthetic-monitoring/surveillance-api/editeur-de-script-msa",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/msa-script-editor"
}

Comme pour les [moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}), le type de moniteur d'API multi-étapes est livré avec un éditeur de script comme alternative à l'éditeur visuel par défaut. L'éditeur de script vous permet d'apporter des modifications aux étapes de votre moniteur, un peu comme l'éditeur visuel, mais dans un script JSON au lieu de l'interface utilisateur.

## Avantages de l'éditeur de script

Il y a plusieurs avantages à utiliser un éditeur de script plutôt que d'apporter des modifications au moniteur via l'interface utilisateur :

- Les utilisateurs expérimentés pourraient préférer effectuer des modifications directement dans un script plutôt que de naviguer dans une interface utilisateur. Certains utilisateurs préfèrent une expérience similaire à l'utilisation d'une ligne de commande.
- Un script permet l'automatisation, par exemple pour s'adapter à votre [processus CI/CD](https://blog.uptrends.com/technology/uptrends-and-your-ci-cd-processes/). En utilisant l'[API d'Uptrends]({{< ref path="/support/kb/api" lang="fr" >}}), vous allez pouvoir mettre à jour les étapes du moniteur en même temps que vous mettez à jour l'API qu'il vérifie.
- L'éditeur de script vous permet de faire une copie locale des étapes de votre moniteur, en copiant simplement le script et en le collant dans un fichier local. La conservation d'une copie locale permet le contrôle des versions, les sauvegardes de vos moniteurs API multi-étapes et la réplication facile des configurations complexes.

## Passer à l'éditeur de script

Vous pouvez passer à l'éditeur de script pour n'importe quel moniteur API multi-étapes en cliquant sur le bouton {{< AppElement type="buttonSecondary" >}} BASCULER VERS LE SCRIPT {{< /AppElement >}} en haut à droite de l'onglet {{< AppElement type="tab" >}} Étapes {{< /AppElement >}} dans les paramètres du moniteur. Basculer vers et depuis l'éditeur de script déclenchera la validation, assurez-vous donc que le code JSON dans le script reste valide. Le script ressemblera à ceci :

![L'éditeur de scripts](/img/content/scr-msa-script-editor.min.png)

## Comprendre le script

Comme vous pouvez le constater, le script est essentiellement un ensemble d'étapes individuelles au format JSON, contenant pour chacun la méthode de requête, l'URL, l'en-tête et le corps de la requête que vous avez configurés, ainsi que les options d'authentification. De plus, chaque étape contient les définitions des variables créées  à partir de la réponse ou des assertions à faire. Toute modification nécessaire peut être apportée directement dans l'éditeur de script.

Une étape individuelle ressemblera à peu près à ceci :

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

Ajouter une étape supplémentaire est très simple, il suffit d'ajouter le bloc de texte d'une étape, en utilisant la définition d'étape complète comme indiqué ci-dessus.

Après les blocs des étapes, le script liste également des informations sur les [variables prédéfinies]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined-variables" lang="fr" >}}) ou les [fonctions définies par l'utilisateur]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#user-defined-functions" lang="fr" >}}) que vous avez configurés :

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
