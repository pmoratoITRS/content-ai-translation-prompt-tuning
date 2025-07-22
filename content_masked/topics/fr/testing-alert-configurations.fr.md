{
  "hero": {
    "title": "Tester les messages d'alerte"
  },
  "title": "Tester les messages d'alerte",
  "summary": "Les alertes sont un moyen très utile de rester au courant de l'état et des performances de vos sites web. Pensez à les tester.",
  "url": "[URL_BASE_TOPICS]alerter/tester-configurations-alertes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les messages d'alerte sont un moyen très utile de rester au courant de l'état et des performances de vos sites web, serveurs et services web.

Lorsqu'une alerte est déclenchée par la surveillance Uptrends, des messages d'alerte peuvent être envoyés aux opérateurs ou aux applications tierces. Le message peut être un message vocal (reçu par téléphone), un e-mail, un SMS ou un message (personnalisé) envoyé à une application. Les intégrations définissent la manière dont ces messages doivent être envoyés. L'envoi des messages se configure dans les définitions d'alerte. Pour en savoir plus, veuillez consulter l'article sur les [alertes]([LINK_URL_1]).

Puisqu'il est essentiel que les messages parviennent à l'opérateur ou à l'application, il est aussi nécessaire de tester leur bon fonctionnement. L'envoi d'un message de test fonctionne différemment pour les différents types d'intégrations. Les étapes pour chaque type d'intégration sont expliquées ci-dessous.

## Envoi d'un message test par e-mail ou SMS

[SHORTCODE_1]
**Remarque** : Il faut disposer de droits d'administrateur pour accéder aux informations de compte des opérateurs.
[SHORTCODE_2]

1. Ouvrez le menu [SHORTCODE_3] Configuration de compte > Opérateurs, groupes et sous-comptes [SHORTCODE_4].
2. Cliquez sur le bouton [SHORTCODE_5] Voir tous les opérateurs [SHORTCODE_6].
3. Dans la liste des opérateurs, sélectionnez celui pour lequel vous souhaitez tester les messages.
4. Assurez-vous que l'adresse e-mail principal et le numéro de téléphone portable sont renseignés dans l'onglet [SHORTCODE_7]Principal[SHORTCODE_8].
5. Cliquez sur [SHORTCODE_9]Envoyer un e-mail de test[SHORTCODE_10] ou [SHORTCODE_11]Envoyer un SMS de test[SHORTCODE_12] pour envoyer respectivement un e-mail ou un SMS.

Vous devriez recevoir un message de test.

Si vous n'êtes pas administrateur, vous pouvez quand même tester les messages pour votre propre compte.

1. Accédez au menu de l'utilisateur en bas du menu principal et sélectionnez [SHORTCODE_13] Paramètres utilisateur [SHORTCODE_14].
2. Vous verrez vos informations de compte.
3. Assurez-vous que l'adresse e-mail principal et le numéro de téléphone portable sont renseignés. Utilisez ensuite le bouton [SHORTCODE_15]Envoyer un e-mail de test[SHORTCODE_16] ou [SHORTCODE_17]Envoyer un SMS de test[SHORTCODE_18] pour démarrer votre test.

## Envoi d'un message de test à des systèmes tiers

Plusieurs applications tierces peuvent recevoir des messages d'alerte en provenance de l'application Uptrends. Il existe des [intégrations]([LINK_URL_2]) prêtes à l'emploi pour de nombreux systèmes tiers, qui ont des fonctionnalités de test. Pour pouvoir envoyer des messages de test, vous devez ajouter ces intégrations, puis les configurer.

Si le test réussit, un message est reçu dans l'application tierce. Le traitement par le système et l'apparence du message pour l'utilisateur dépendent du système que vous utilisez. Par exemple, si vous envoyez un message de test à Slack, vous devriez voir un message de test apparaître dans le canal que vous avez spécifié.

### Slack et PagerDuty

Pour Slack et PagerDuty, une fonction de test standard existe dans l'intégration :

1. Passez par le menu [SHORTCODE_19]Alerte > Intégrations[SHORTCODE_20].
2. Dans la liste des intégrations, cliquez sur celle que vous souhaitez tester.
3. Assurez-vous que toutes les informations sont renseignées.
4. Cliquez sur le bouton [SHORTCODE_21]Envoyer un message test[SHORTCODE_22].

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Si vous souhaitez faire un test simple et rapide, utilisez le bouton [SHORTCODE_23]Envoyer une alerte de test[SHORTCODE_24] en bas de la page de l'intégration.

![Capture d'écran du test de l'intégration pour Microsoft Teams]([LINK_URL_3])

Si vous avez personnalisé l'intégration, un onglet supplémentaire [SHORTCODE_25]Personnalisations[SHORTCODE_26] a été rajouté à votre intégration. Vous pouvez ensuite utiliser cette fonction de message de test de l'intégration personnalisée comme décrit ci-dessous. Les personnalisations que vous avez ajoutées seront prises en compte.

## Envoi d'un message de test pour les intégrations personnalisées

Une autre option consiste à définir une intégration personnalisée, où vous pouvez envoyer un message à une application tierce pour laquelle Uptrends n'a pas d'intégration standard. Vous définissez l'intégration à l'aide de l'API du tiers. Ces intégrations peuvent également être testées pour savoir si elles envoient un message comme prévu.

1. Passez par le menu [SHORTCODE_27] Alerte > Intégrations [SHORTCODE_28].
2. Dans la liste des intégrations, cliquez sur l'intégration personnalisée que vous souhaitez tester.
3. Assurez-vous que toutes les informations sont renseignées.
4. Si vous souhaitez faire un test simple et rapide, utilisez le bouton [SHORTCODE_29]Envoyer une alerte de test[SHORTCODE_30] en bas de la page de l'intégration.
5. Si vous souhaitez tester des messages qui tiennent compte de vos paramètres spécifiques (personnalisations), ouvrez l'onglet [SHORTCODE_31]Personnalisations[SHORTCODE_32]. Normalement vous avez dû définir les étapes HTTP lors de la configuration de l'intégration. Vous pouvez définir des étapes pour les différents types d'alertes : Erreur, OK et Rappel. Si vous avez décidé d'avoir des étapes HTTP distinctes pour les différents types d'alerte ou combinaisons de types d'alerte, plusieurs définitions d'étape existent.  
   ![Capture d'écran des étapes des alertes d'une intégration personnalisée]([LINK_URL_4])

6. Pour chaque définition d'étape HTTP, cliquez sur le bouton [SHORTCODE_33]Envoyer une alerte de test[SHORTCODE_34].

L'article [Configuration d'une intégration personnalisée]([LINK_URL_5]) contient plus d'informations sur les tests des messages avec les intégrations personnalisées.

## Dépannage

Si vos messages ne sont pas reçus comme prévu, vous pouvez consulter les principaux conseils de dépannage ici : [Alertes - Dépanner]([LINK_URL_6]).
