{
"hero": {
"title": "Recevez vos alertes de suivi de site web dans ServiceNow"
},
"title": "Intégration ServiceNow",
"summary": "Recevez les alertes de suivi de site web d'Uptrends dans ServiceNow.",
"url": "/support/kb/alerting/integrations/service-now",
"translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/service-now"
}

**ServiceNow** est une plateforme cloud qui vous permet de gérer l'ensemble de vos opérations IT au moyen de différentes applications, dont une consacrée à la gestion des incidents.

L'intégration de **ServiceNow** à Uptrends fait automatiquement apparaître les incidents dans votre compte **ServiceNow**. Pour en savoir plus sur ServiceNow, reportez-vous à la [documentation de l'intégration ServiceNow](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/managing-data/concept/integrations.html) et aux [API REST ServiceNow REST](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html).

## Configurer l'intégration

L'ajout d'intégrations pour **ServiceNow** dans Uptrends nécessite que vous ayez un compte ServiceNow. Préparez votre nom d'instance et vos données d'authentification.

Pour configurer l'intégration :

1. Dans l'application web d'Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. En haut à droite, cliquez sur le bouton {{< AppElement type="button" >}} Ajouter intégration {{< /AppElement >}}.
3. Dans le menu contextuel, sélectionnez **ServiceNow** comme type d'intégration tierce.
4. Cliquez sur le bouton {{< AppElement type="button" >}} Choisir {{< /AppElement >}} pour créer une nouvelle intégration.
5. **ServiceNow** est la valeur par défaut du champ **Types d'intégration**. Précisez le nom de votre nouvelle intégration.
6. Dans la section **Variables prédéfinies**, remplissez les champs **Valeur** suivants :

- `InstanceName` : le nom de votre instance de ServiceNow. Vous le trouverez dans l'URL de ServiceNow : `https://<instancename>.service-now.com`.
- `Username` : le nom d'utilisateur de votre compte ServiceNow.
- `Password` : le mot de passe de votre compte ServiceNow.

Vous pouvez choisir de saisir ces valeurs sous forme de **texte brut** ou récupérer les **identifiants de coffre-fort** stockés dans le [coffre-fort]({{< ref path="/support/kb/account/vault" lang="fr" >}}). L'intégration utilisera automatiquement une authentification de base pour accéder à la plateforme **ServiceNow**.

![Intégration ServiceNow](/img/content/scr-service-now-integration.min.png)

7. (Facultatif) Pour personnaliser vos paramètres de connexion et d'intégration, cochez la case **Personnaliser l'intégration**. En activant la personnalisation, vous pouvez :

- Ajouter des **variables prédéfinies** et modifier les variables prédéfinies existantes, en vue de les utiliser pour l'authentification, les niveaux d'escalade et les définitions d'étape.
- Ajouter et définir des étapes pour les différents types d'alerte. La plupart du temps, une seule étape HTTP sera suffisante pour votre configuration. Si vous devez créer des étapes distinctes pour d'autres scénarios, comme l'authentification, cliquez sur le bouton {{< AppElement type="button" >}} Ajouter des étapes {{< /AppElement >}}.
- Personnaliser les [messages d'alerte]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="fr" >}}) pour différents types d'alerte. Ce message précise le service tiers ou l'API à contacter, le contenu des messages HTTP, l'authentification requise et d'autres informations.

![Variables prédéfinies personnalisées](/img/content/scr-service-now-integration-customization.min.png)

![Définition d'étape personnalisée](/img/content/scr-service-now-integration-customization-steps.min.png)

8. (Facultatif) Dans l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}, sélectionnez un opérateur ou un groupe d'opérateurs afin d'ajouter des [autorisations d'intégration]({{< ref path="/support/kb/alerting/integrations/integrations-permissions" lang="fr" >}}).

9. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.

10. Pour vérifier votre configuration, testez votre intégration personnalisée au moyen des [messages test]({{< ref path="/support/kb/alerting/integrations/custom-integrations/testing-your-custom-integration" lang="fr" >}}). Pour en savoir plus, lisez la section d'article de notre base de connaissances intitulée [Envoi d'un message de test à des systèmes tiers]({{< ref path="/support/kb/alerting/testing-alert-configurations#sending-a-test-message-to-third-party-systems" lang="fr" >}}).

À ce stade, vous avez terminé de configurer l'intégration **ServiceNow** dans Uptrends. Vous pouvez utiliser cette intégration et l'ajouter à vos [définitions d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}).

{{< callout >}}
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous voulez désactiver temporairement la réception d'alertes.
{{< /callout >}}

Pour toute question, veuillez [contacter notre équipe de support](/contact).
