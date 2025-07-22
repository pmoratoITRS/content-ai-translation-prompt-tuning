{
"hero": {
"title": "Tester les messages d'alerte"
},
"title": "Tester les messages d'alerte",
"summary": "Les alertes sont un moyen très utile de rester au courant de l'état et des performances de vos sites web. Pensez à les tester.",
"url": "/support/kb/alerter/tester-configurations-alertes",
"translationKey": "https://www.uptrends.com/support/kb/alerting/testing-alert-configurations"
}

Les messages d'alerte sont un moyen très utile de rester au courant de l'état et des performances de vos sites web, serveurs et services web.

Lorsqu'une alerte est déclenchée par la surveillance Uptrends, des messages d'alerte peuvent être envoyés aux opérateurs ou aux applications tierces. Le message peut être un message vocal (reçu par téléphone), un e-mail, un SMS ou un message (personnalisé) envoyé à une application. Les intégrations définissent la manière dont ces messages doivent être envoyés. L'envoi des messages se configure dans les définitions d'alerte. Pour en savoir plus, veuillez consulter l'article sur les [alertes]({{< ref path="support/kb/alerting" lang="fr" >}}).

Puisqu'il est essentiel que les messages parviennent à l'opérateur ou à l'application, il est aussi nécessaire de tester leur bon fonctionnement. L'envoi d'un message de test fonctionne différemment pour les différents types d'intégrations. Les étapes pour chaque type d'intégration sont expliquées ci-dessous.

## Envoi d'un message test par e-mail ou SMS

{{< callout >}}
**Remarque** : Il faut disposer de droits d'administrateur pour accéder aux informations de compte des opérateurs.
{{< /callout >}}

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Opérateurs, groupes et sous-comptes {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Voir tous les opérateurs {{< /AppElement >}}.
3. Dans la liste des opérateurs, sélectionnez celui pour lequel vous souhaitez tester les messages.
4. Assurez-vous que l'adresse e-mail principal et le numéro de téléphone portable sont renseignés dans l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}}.
5. Cliquez sur {{< AppElement type="button" >}}Envoyer un e-mail de test{{< /AppElement >}} ou {{< AppElement type="button" >}}Envoyer un SMS de test{{< /AppElement >}} pour envoyer respectivement un e-mail ou un SMS.

Vous devriez recevoir un message de test.

Si vous n'êtes pas administrateur, vous pouvez quand même tester les messages pour votre propre compte.

1. Accédez au menu de l'utilisateur en bas du menu principal et sélectionnez {{< AppElement type="menuitem" >}} Paramètres utilisateur {{< /AppElement >}}.
2. Vous verrez vos informations de compte.
3. Assurez-vous que l'adresse e-mail principal et le numéro de téléphone portable sont renseignés. Utilisez ensuite le bouton {{< AppElement type="button" >}}Envoyer un e-mail de test{{< /AppElement >}} ou {{< AppElement type="button" >}}Envoyer un SMS de test{{< /AppElement >}} pour démarrer votre test.

## Envoi d'un message de test à des systèmes tiers

Plusieurs applications tierces peuvent recevoir des messages d'alerte en provenance de l'application Uptrends. Il existe des [intégrations](/integrations) prêtes à l'emploi pour de nombreux systèmes tiers, qui ont des fonctionnalités de test. Pour pouvoir envoyer des messages de test, vous devez ajouter ces intégrations, puis les configurer.

Si le test réussit, un message est reçu dans l'application tierce. Le traitement par le système et l'apparence du message pour l'utilisateur dépendent du système que vous utilisez. Par exemple, si vous envoyez un message de test à Slack, vous devriez voir un message de test apparaître dans le canal que vous avez spécifié.

### Slack et PagerDuty

Pour Slack et PagerDuty, une fonction de test standard existe dans l'intégration :

1. Passez par le menu {{< AppElement type="menuitem" >}}Alerte > Intégrations{{< /AppElement >}}.
2. Dans la liste des intégrations, cliquez sur celle que vous souhaitez tester.
3. Assurez-vous que toutes les informations sont renseignées.
4. Cliquez sur le bouton {{< AppElement type="button" >}}Envoyer un message test{{< /AppElement >}}.

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Si vous souhaitez faire un test simple et rapide, utilisez le bouton {{< AppElement type="savebutton" >}}Envoyer une alerte de test{{< /AppElement >}} en bas de la page de l'intégration.

![Capture d'écran du test de l'intégration pour Microsoft Teams](/img/content/scr_test-message-to-microsoft-teams.min.png)

Si vous avez personnalisé l'intégration, un onglet supplémentaire {{< AppElement type="tab" >}}Personnalisations{{< /AppElement >}} a été rajouté à votre intégration. Vous pouvez ensuite utiliser cette fonction de message de test de l'intégration personnalisée comme décrit ci-dessous. Les personnalisations que vous avez ajoutées seront prises en compte.

## Envoi d'un message de test pour les intégrations personnalisées

Une autre option consiste à définir une intégration personnalisée, où vous pouvez envoyer un message à une application tierce pour laquelle Uptrends n'a pas d'intégration standard. Vous définissez l'intégration à l'aide de l'API du tiers. Ces intégrations peuvent également être testées pour savoir si elles envoient un message comme prévu.

1. Passez par le menu {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Dans la liste des intégrations, cliquez sur l'intégration personnalisée que vous souhaitez tester.
3. Assurez-vous que toutes les informations sont renseignées.
4. Si vous souhaitez faire un test simple et rapide, utilisez le bouton {{< AppElement type="savebutton" >}}Envoyer une alerte de test{{< /AppElement >}} en bas de la page de l'intégration.
5. Si vous souhaitez tester des messages qui tiennent compte de vos paramètres spécifiques (personnalisations), ouvrez l'onglet {{< AppElement type="tab" >}}Personnalisations{{< /AppElement >}}. Normalement vous avez dû définir les étapes HTTP lors de la configuration de l'intégration. Vous pouvez définir des étapes pour les différents types d'alertes : Erreur, OK et Rappel. Si vous avez décidé d'avoir des étapes HTTP distinctes pour les différents types d'alerte ou combinaisons de types d'alerte, plusieurs définitions d'étape existent.  
   ![Capture d'écran des étapes des alertes d'une intégration personnalisée](/img/content/scr_custom-integration-steps-for-alerts.min.png)

6. Pour chaque définition d'étape HTTP, cliquez sur le bouton {{< AppElement type="button" >}}Envoyer une alerte de test{{< /AppElement >}}.

L'article [Configuration d'une intégration personnalisée]({{< ref path="support/kb/alerting/integrations/custom-integrations" lang="fr" >}}) contient plus d'informations sur les tests des messages avec les intégrations personnalisées.

## Dépannage

Si vos messages ne sont pas reçus comme prévu, vous pouvez consulter les principaux conseils de dépannage ici : [Alertes - Dépanner]({{< ref path="support/kb/alerting#troubleshooting" lang="fr" >}}).
