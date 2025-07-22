{
  "hero": {
    "title": "Alert Definition API"
  },
  "title": "Alert Definition API",
  "url": "/support/kb/api/alert-definition-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-definition-api"
}

Using the Alert Definition API, you can manage settings for a specific alert definition. An alert definition is used to define how and to whom an alert is sent. For example, you can configure an alert to be generated when an error occurs for more than 5 minutes, and choose which users should be notified by e-mail and SMS.

The Alert Definition API currently only supports enabling and disabling an alert definition with the `Active` setting.

## PUT /AlertDefinition/{alertDefinitionGuid}

Updates the alert definition specified by the Guid. The request body for this request is expected to contain the full list of all alert definition fields, as opposed to a PATCH request where you specifiy a part of the fields. The full list consists of the `AlertDefinitionGuid` and the `IsActive` fields. The following PUT request will set the alert definition to disabled, even if it had already been disabled previously.

`PUT /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Request body:

    {
      "AlertDefinitionGuid": "e06bcd76-b20f-42de-a2d4-5b2a4daad902",
      "IsActive": false
    }

## PATCH /AlertDefinition/{alertDefinitionGuid}

Updates the alert definition specified by the Guid. The request body for this request is expected to contain a partial list of fields you want to update. You'll typically use this request to update just one or a few fields. In the request body, only list the fields you want to update. Including the `AlertDefinitionGuid` field is optional. If you do specify it, it must match the AlertDefinitionGuid you specify in the URL.

The following PATCH request is used to activate an alert definition, by specifying the value `true` for its `IsActive` field.

`PATCH /AlertDefinition/e06bcd76-b20f-42de-a2d4-5b2a4daad902`

Request body:

    {
      "IsActive": true
    }
