{
  "hero": {
    "title": "API de définition d'alerte"
  },
  "title": "API de définition d'alerte",
  "url": "/support/kb/api/api-de-definition-d-alerte",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-definition-api"
}

À l'aide de l'API de définition d'alerte, vous pouvez gérer les paramètres d'une définition d'alerte spécifique. Une définition d'alerte est utilisée pour définir comment et à qui envoyer une alerte. Par exemple, vous pouvez définir une alerte qui est générée lorsqu'une erreur se produit pendant plus de 5 minutes, et choisir les utilisateurs à notifier par e-mail et SMS.

L'API de définition d'alerte ne prend actuellement en charge que l'activation et la désactivation d'une définition d'alerte.

## PUT /AlertDefinition/{alertDefinitionGuid}

Met à jour la définition d'alerte spécifiée par le Guid. Le corps de cette requête devrait contenir la liste complète de tous les champs de définition d'alerte, par opposition à une demande PATCH où vous spécifiez seulement un sous-ensemble des champs. La liste complète comprend les champs `AlertDefinitionGuid` et `IsActive`. La requête PUT suivante désactivera l'alerte, même si elle avait déjà été désactivée auparavant.

`PUT /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Corps de la requête :

    {
      "AlertDefinitionGuid": "e06bcd76-b20f-42de-a2d4-5b2a4daad902",
      "IsActive": false
    }

## PATCH /AlertDefinition/{alertDefinitionGuid}

Met à jour la définition d'alerte spécifiée par le Guid. Le corps de la requête peut contenir une liste partielle des champs que vous souhaitez mettre à jour. Vous utiliserez généralement cette requête pour mettre à jour un ou plusieurs champs. Dans le corps de la requête, mettez uniquement les champs que vous souhaitez mettre à jour. Inclure le champ `AlertDefinitionGuid` est facultative. Si vous le spécifiez, il doit correspondre au même AlertDefinitionGuid que vous spécifiez dans l'URL.

La requête PATCH suivante va activer une définition d'alerte, en spécifiant la valeur `true` pour son champ `IsActive`.

`PATCH /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Corps de la requête :

    {
      "IsActive": true
    }
