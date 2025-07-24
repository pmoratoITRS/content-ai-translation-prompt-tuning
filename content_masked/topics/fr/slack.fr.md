{
  "hero": {
    "title": "Recevoir vos alertes de surveillance de site web dans Slack"
  },
  "title": "Slack",
  "summary": "Recevez les alertes de surveillance de site web d'Uptrends dans Slack. Inscrivez-vous pour essayer gratuitement Uptrends pendant 30 jours.",
  "url": "[URL_BASE_TOPICS]alerter/integrations/slack",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

En intégrant **Slack** à Uptrends, vous pouvez envoyer des messages d'alerte dans vos **canaux Slack**. Chaque intégration que vous définissez pour Slack peut envoyer des alertes à un canal différent et vous pouvez affecter plusieurs intégrations pour Slack à un niveau d'escalade donné. La configuration de l'intégration se fait en deux étapes :

1. Configuration de l'intégration dans Uptrends
2. Ajout de l'intégration à une définition d'alerte dans Uptrends

Vous vous demandez ce que cela donne une fois l'intégration configurée ? Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans un canal Slack. Dans la suite de cet article, vous trouverez des **instructions détaillées** sur la configuration des **intégrations pour Slack**.

![]([LINK_URL_1])

## 1. Configuration de l'intégration dans Uptrends

L'ajout d'intégrations pour Slack dans Uptrends nécessite que vous ayez un compte Slack. Vous devrez vous connecter à ce compte avant ou pendant l'installation. Voici les étapes à suivre pour configurer une intégration :

1. Accédez à la page des intégrations en passant par le menu [SHORTCODE_3]Alertes > Intégrations[SHORTCODE_4]. Cette page contient les intégrations que vous avez définies dans Uptrends. À la première ouverture, ce panneau est vide.
2. Cliquez sur le bouton [SHORTCODE_5]Ajouter intégration[SHORTCODE_6] dans le coin supérieur droit pour ouvrir la page [SHORTCODE_7]Nouvelle intégration[SHORTCODE_8].
3. Sélectionnez **Slack** comme **type d'intégration**.
4. Cliquez sur le bouton **Add to Slack** (Ajouter à Slack) et choisissez l'équipe et le canal Slack qui vous intéressent.
5. Cliquez sur [SHORTCODE_9]Authorize[SHORTCODE_10] (Autoriser) pour revenir à la page de configuration des intégrations.
6. Saisissez un nom pour l'intégration dans la boîte de dialogue **Nom d'intégration**.
7. Cliquez sur le bouton [SHORTCODE_11]Enregistrer[SHORTCODE_12] dans le coin inférieur gauche. Après l'enregistrement, vous verrez votre nouvelle intégration pour Slack s'afficher sur la page *Intégration*.
8. Si vous devez envoyer des messages à plusieurs canaux Slack, continuez à ajouter de nouvelles intégrations.

[SHORTCODE_1]
**Astuce :** Désactiver une définition d’intégration signifie que l’intégration ne sera plus utilisée pour vous alerter. Ceci peut notamment être utile si vous souhaitez temporairement ne plus recevoir d’alertes dans votre canal Slack.
[SHORTCODE_2]

## 2. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Vous devez **la relier à un ou plusieurs niveaux d'escalade pour recevoir des alertes** via l'intégration. Suivez les étapes suivantes pour associer une définition d'intégration à un niveau d'escalade :

1. Accédez à la définition d'alerte souhaitée dans Uptrends (*Alertes* > *Définitions d'alerte*).
2. Cliquez pour ouvrir une définition existante ou pour créer une nouvelle définition en utilisant le bouton [SHORTCODE_13]Ajouter une définition d'alerte[SHORTCODE_14] en haut à droite.
3. Cliquez sur un onglet [SHORTCODE_15]Niveau d'escalade[SHORTCODE_16]. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_2]).
4. Cochez les cases de vos définitions d'intégration dans la section **Alertes par intégrations**.
5. Cliquez sur [SHORTCODE_17]Enregistrer[SHORTCODE_18] lorsque vous avez terminé.

**Et voilà, c'est fait !** Vous avez terminé de paramétrer l’intégration pour Slack.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support]([LINK_URL_3]).
