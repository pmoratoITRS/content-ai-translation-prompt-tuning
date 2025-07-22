{
  "title": "Présentation des nouvelles variables d'alerte",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]fevrier-2025-nouvelles-variables-alerte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les variables d'alerte suivantes sont désormais disponibles :

- **@alert.numberOfConsecutiveErrors** : cette variable contient le nombre total d'erreurs (confirmées) consécutives de l'alerte. Elle indique [INLINE_CODE_1] lorsque la réponse de l'API est [INLINE_CODE_2].
- **@alert.checkpointName** : cette variable contient le nom ou l'emplacement du checkpoint où l'alerte a été vérifiée en dernier. Elle indique [INLINE_CODE_3] lorsque la réponse de l'API est [INLINE_CODE_4].
- **@‌alert.responseHeaders** : cette variable contient les en-têtes de réponse de l'alerte sous forme de paires clé-valeur. Par exemple, elle indique la valeur [INLINE_CODE_5] issue de l'en-tête de réponse de l'API, de la même façon que les valeurs sont renvoyées par la variable [INLINE_CODE_6].

Notez que la valeur de la variable [INLINE_CODE_7] peut être vide si la [protection des données des emplacements privés]([LINK_URL_1]) est activée sur le checkpoint privé vérifiant l'alerte. Pour en savoir plus, lisez notre article sur les [variables système d'alerte]([LINK_URL_2]).