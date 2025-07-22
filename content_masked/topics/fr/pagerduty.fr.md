{
  "hero": {
    "title": "Recevoir des alertes de surveillance web dans PagerDuty"
  },
  "title": "PagerDuty",
  "summary": "Recevez les alertes de surveillance de site web d'Uptrends dans PagerDuty. Inscrivez-vous pour essayer Uptrends gratuitement pendant 30 jours.",
  "url": "[URL_BASE_TOPICS]alerter/integrations/pagerduty",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

PagerDuty fournit un système d'alertes, une planification des astreintes, des politiques d'escalade et un suivi des incidents pour alerter votre équipe et agréger des données système. L'option d'intégration d'Uptrends avec **PagerDuty** peut envoyer des messages d'alerte depuis votre **compte Uptrends** vers un **compte PagerDuty**. La configuration de l'intégration se fait en trois étapes :

1. Configuration de l'intégration dans PagerDuty
2. Configuration de l'intégration dans Uptrends
3. Ajout de l'intégration à une définition d'alerte dans Uptrends

Vous vous demandez ce que cela donne une fois l'intégration configurée ? Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans PagerDuty. Dans la suite de cet article, vous trouverez des **instructions détaillées** sur la configuration de l'intégration.

![]([LINK_URL_1])

## 1. Configuration de l'intégration dans PagerDuty

Cette procédure ne s'applique que si vous souhaitez recevoir des alertes dans votre compte PagerDuty. L'intégration entre Uptrends et PagerDuty comprend des alertes qui sont envoyées par Uptrends à un service défini par l'utilisateur dans PagerDuty. Pour qu'Uptrends puisse envoyer des alertes à ce service PagerDuty, vous devez le créer dans votre compte PagerDuty. Le processus est détaillé ci-dessous.

1. Sélectionnez **Services** dans la barre de menu supérieure de l'écran principal de votre compte PagerDuty.
2. Une page nommée *Services* s'ouvrira. Cliquez sur le bouton **\+ New service**.
3. Une page nommée *Create a Service* s'ouvrira. C'est sur cette page que vous allez fournir les informations du service.
4. Saisissez un nom pour le service et éventuellement une description. Choisissez une politique d'escalade existante, ou créez-en une nouvelle, selon les besoins. Si nécessaire, renseignez le paramètre **Alert Grouping** (Groupement d'alertes).
5. Il n'est **pas** nécessaire d'ajouter une intégration à ce stade, car elle sera créée automatiquement. Cliquez sur *Create service without an integration* (Créer le service sans intégration).
6. Vous êtes maintenant dirigé vers la page de votre service nouvellement créée. L'onglet *Integrations* contiendra la **clé d'intégration** de votre service.

La configuration de l'intégration dans PagerDuty est terminée.

## 2. Configuration de l'intégration dans Uptrends

Dans Uptrends, la fonctionnalité des intégrations est accessible à partir du menu principal.

1. Dans le menu latéral, cliquez sur **Alerte**. Ajoutez une nouvelle intégration en cliquant sur l'icône **+** à côté de *Intégrations*. ![Ajout d'une nouvelle intégration]([LINK_URL_2])
2. Sélectionnez *PagerDuty* pour créer une intégration PagerDuty. ![Sélection de PagerDuty]([LINK_URL_3])
3. Cliquez sur le bouton **Alert with PagerDuty** pour lancer le processus de connexion entre Uptrends et PagerDuty. Connectez-vous à l'aide de vos identifiants PagerDuty. ![Portail de connexion à PagerDuty]([LINK_URL_4])
4. Dans la fenêtre suivante, sélectionnez le ou les services PagerDuty que vous souhaitez utiliser avec vos alertes Uptrends.
   ![Sélection du ou des services PagerDuty]([LINK_URL_5])
5. Après avoir cliqué sur *Connect*, vous serez renvoyé à Uptrends.
6. Pour terminer la configuration, saisissez un nom pour cette intégration et cliquez sur le bouton [SHORTCODE_3]Enregistrer[SHORTCODE_4] dans le coin inférieur gauche. Après avoir enregistré, vous reviendrez à la liste des intégrations, qui contient maintenant votre définition d'intégration nouvellement créée.
7. Vous pouvez cliquer sur cette intégration pour l'éditer ou pour envoyer des messages de test.
   ![Intégration PagerDuty]([LINK_URL_6])

[SHORTCODE_1]
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut notamment être utile si vous souhaitez désactiver temporairement la réception d'alertes dans votre service PagerDuty.
[SHORTCODE_2]

## 3. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Vous devez **la relier à un ou plusieurs niveaux d'escalade pour recevoir des alertes** via l'intégration.

1. Pour rattacher une définition d'intégration à un niveau d'escalade, naviguez jusqu'à la définition d'alerte, puis le niveau d'escalade souhaité dans Uptrends.

![Ouverture des définitions d'alerte]([LINK_URL_7])

2. Chaque onglet [SHORTCODE_5]Niveau d'escalade[SHORTCODE_6] contient une section appelée **Alertes par intégrations**. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_8]).
3. Sélectionnez l'intégration que vous souhaitez associer à ce niveau d'escalade. Dans ce cas-ci, sélectionnez **l'intégration personnalisée** pour PagerDuty.
4. N'oubliez pas de cliquer sur le bouton [SHORTCODE_7]Enregistrer[SHORTCODE_8] pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration pour PagerDuty.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support]([LINK_URL_9]).
