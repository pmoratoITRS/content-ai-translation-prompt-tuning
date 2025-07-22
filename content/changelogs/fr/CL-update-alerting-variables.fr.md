{
"title": "Présentation des nouvelles variables d'alerte",
"date": "2025-02-19",
"url": "/changelog/fevrier-2025-nouvelles-variables-alerte",
"translationKey": "https://www.uptrends.com/changelog/february-2025-alert-variable-updates"
}

Les variables d'alerte suivantes sont désormais disponibles :

- **@alert.numberOfConsecutiveErrors** : cette variable contient le nombre total d'erreurs (confirmées) consécutives de l'alerte. Elle indique `2` lorsque la réponse de l'API est `{"numberOfConsecutiveErrors": "2"}`.
- **@alert.checkpointName** : cette variable contient le nom ou l'emplacement du checkpoint où l'alerte a été vérifiée en dernier. Elle indique `Ghent, Belgium` lorsque la réponse de l'API est `{"checkpointName": "Ghent, Belgium"}`.
- **@‌alert.responseHeaders** : cette variable contient les en-têtes de réponse de l'alerte sous forme de paires clé-valeur. Par exemple, elle indique la valeur `{"Content-Type": "text/html"}` issue de l'en-tête de réponse de l'API, de la même façon que les valeurs sont renvoyées par la variable `@alert.responseBody`.

Notez que la valeur de la variable `@‌alert.responseHeaders` peut être vide si la [protection des données des emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}) est activée sur le checkpoint privé vérifiant l'alerte. Pour en savoir plus, lisez notre article sur les [variables système d'alerte]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="fr" >}}).