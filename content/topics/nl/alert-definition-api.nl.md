{
  "hero": {
    "title": "Alert Definition API"
  },
  "title": "Alert Definition API",
  "url": "/support/kb/api/alert-definition-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-definition-api"
}

Met de Alert Definition API kunt u instellingen voor een specifieke alertdefinitie beheren. Een alertdefinitie wordt gebruikt om te definiëren hoe en naar wie een alert wordt verstuurd. U kunt bijvoorbeeld configureren dat een alert moet worden gegenereerd wanneer er meer dan 5 minuten een fout optreedt en kiezen welke gebruikers per e-mail en SMS op de hoogte moeten worden gesteld.

De Alert Definition API ondersteunt momenteel alleen het in- en uitschakelen van een alertdefinitie met de instelling `Active`.

## PUT /AlertDefinition/{alertDefinitionGuid}

Werkt de alertdefinitie bij die is gespecificeerd door de Guid. De request body voor deze request bevat naar verwachting de volledige lijst van alle alertdefinitievelden, in tegenstelling tot een PATCH-request waarbij u een deel van de velden specificeert. De volledige lijst bestaat uit de velden `AlertDefinitionGuid` en `IsActive`. De volgende PUT-request zet de alertdefinitie op uitgeschakeld, ook als deze eerder al was uitgeschakeld.

`PUT /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Request body:

    {
      "AlertDefinitionGuid": "e06bcd76-b20f-42de-a2d4-5b2a4daad902",
      "IsActive": false
    }

## PATCH /AlertDefinition/{alertDefinitionGuid}

Werkt de alertdefinitie bij die is gespecificeerd door de Guid. De request body voor deze request bevat naar verwachting een gedeeltelijke lijst met velden die u wilt bijwerken. U gebruikt deze request meestal om slechts een of enkele velden bij te werken. Vermeld in de request body alleen de velden die u wilt bijwerken. Het opnemen van het veld `AlertDefinitionGuid` is optioneel. Als u het specificeert, moet het overeenstemmen met de `AlertDefinitionGuid` die u specificeert in de URL.

De volgende PATCH request wordt gebruikt om een alertdefinitie te activeren door de waarde `true` op te geven voor zijn veld `IsActive`.

`PATCH /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Request body:

    {
      "IsActive": true
    }
