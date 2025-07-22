{
"title": "Enregistrement dans le journal d'audit des modifications apportées via l'API",
"date": "2024-04-10",
"url": "/changelog/avril-2024-api-journal-audit",
"translationKey": "https://www.uptrends.com/changelog/april-2024-api-audit-logging"
}

Le **journal d'audit** de votre compte fournit désormais des informations supplémentaires concernant la source des modifications. Plus précisément, il indique si une modification a été apportée via l'interface web d'Uptrends ou via l'API. Lorsque la modification provient de l'API, le journal indique quel est [l'utilisateur de l'API]({{< ref path="/support/kb/api/authentication-v4" lang="fr" >}}), en plus de l'opérateur initial.

![Exemple de journal d'audit indiquant l'API comme une source](/img/content/scr-auditlog-api-source.min.png)