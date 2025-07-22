{
"hero": {
"title": "Recevez vos alertes de surveillance dans Splunk On-Call"
},
"title": "Intégration de Splunk On-Call",
"summary": "Recevez les alertes de monitoring de sites web d’Uptrends dans Splunk On-Call.",
"url": "/support/kb/alerting/integrations/splunk-on-call",
"translationKey": "https://www.uptrends.com/support/kb/integrations/splunk-on-call"
}

**Splunk On-Call** est une plateforme de gestion des incidents qui aide les équipes DevOps à collaborer pour résoudre efficacement les incidents. Elle vous permet de planifier les horaires de service, d’organiser les remontées d’incidents et d’envoyer des notifications à votre équipe dès qu’un problème nécessite une intervention immédiate.

L’intégration entre Splunk On-Call et Uptrends crée automatiquement des incidents qui s’affichent dans votre tableau de bord Splunk On-Call. La mise en place de l'intégration entre les deux systèmes s'effectue comme suit :

## 1. Configurez votre intégration REST dans Splunk On-Call.
1. Connectez-vous à votre compte Splunk On-Call.
2. Dans l’onglet {{< AppElement type="tab" >}}Integrations{{< /AppElement >}}, cliquez sur l’intégration REST qui est déjà activée par défaut. Pour en savoir plus, lisez cet article (en anglais) sur les [intégrations REST](https://help.victorops.com/knowledge-base/rest-endpoint-integration-guide/) dans Splunk On-Call.
3. Copiez le champ *URL to notify* sans la valeur */$routing_key* et gardez-la pour un usage ultérieur.

## 2. Configuration de l'intégration dans Uptrends
1. Dans votre compte Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}}Alerte > Intégrations {{< /AppElement >}}.
2. Dans le coin supérieur droit, cliquez sur le bouton {{< AppElement type="button" >}}Ajouter intégration{{< /AppElement >}}.
3. Dans la fenêtre contextuelle, sélectionnez *Splunk On-Call* comme intégration tierce.
4. Cliquez sur le bouton {{< AppElement type="button" >}}Choisir{{< /AppElement >}}.
5. Vous pouvez désormais affiner la configuration de votre intégration. Donnez un nom à votre nouvelle intégration.
6. Par défaut, le champ {{< AppElement type="menuitem" >}}Personnaliser l'intégration{{< /AppElement >}} est désactivé. Cochez la case pour activer la personnalisation et ajuster les paramètres d’intégration par défaut pour Splunk On-Call. Si cela n’est pas nécessaire, vous pouvez laisser le champ désactivé.

{{< callout >}}
**Remarque :** l’activation de la {{< AppElement type="menuitem" >}}personnalisation{{< /AppElement >}} entraîne l’apparition de l’onglet {{< AppElement type="tab" >}}Personnalisations{{< /AppElement >}}. Vous pouvez préciser quels messages sont envoyés lorsqu’une alerte est générée, y compris la partie tierce ou l’API à contacter, le contenu des messages HTTP, toute authentification requise, etc.

La plupart du temps, une seule étape HTTP suffit. Il est toutefois possible d’ajouter des étapes si vous avez besoin de séparer les étapes d’authentification. Vous pouvez aussi définir des étapes distinctes pour différents types d’alerte. Cette possibilité est pratique si vos messages d’erreur doivent être différents des messages OK correspondant aux alertes résolues. Pour en savoir plus, consultez les [articles de notre base de connaissances sur les intégrations]({{< ref path="support/kb/alerting/integrations" lang="fr" >}}).
{{< /callout >}}


7. Sous la section Variables prédéfinies, vous pouvez voir *SplunkOnCallUrl*. Choisissez la façon dont vous souhaitez spécifier la valeur au moyen du menu déroulant. Par exemple, vous pouvez choisir l’option *Spécifiez la valeur ici*.
8. Cliquez sur les points de suspension à côté du menu déroulant *SplunkOnCallUrl*. Une fenêtre contextuelle vous propose deux options. Vous pouvez coller dans le champ vierge la valeur *URL to notify* que vous avez enregistrée précédemment, ou choisir un nom d'utilisateur ou un mot de passe correspondant à vos [références d'identification dans le coffre-fort]({{< ref path="support/kb/account/vault#credential-set" lang="fr" >}}) (si applicable).
9. Cliquez sur le bouton {{< AppElement type="button" >}}Sélectionnez{{< /AppElement >}}.
10. Spécifiez ensuite la valeur *RoutingKey* que vous souhaitez utiliser. Les [routing keys](https://help.victorops.com/knowledge-base/routing-keys/) se trouvent dans l’onglet {{< AppElement type="tab" >}} Settings {{< /AppElement >}} (Paramètres) dans votre compte Splunk On-Call.
11. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour confirmer vos paramètres d’intégration.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration et l’ajouter à vos [définitions d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}).

**C’est tout.** Vous avez terminé l’intégration de Splunk On-Call.

Vous vous demandez ce que cela donne une fois l'intégration configurée ? Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans le tableau de bord de Splunk On-Call.
![Tableau de bord de Splunk On-Call avec l’intégration d’Uptrends](/img/content/scr_integration-splunk-on-call.min.png)

{{< callout >}}
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous souhaitez désactiver temporairement la réception d'alertes.
{{< /callout >}}

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support](/contact).
