{
  "hero": {
    "title": "Recevoir des alertes dans Opsgenie"
  },
  "title": "Opsgenie",
  "summary": "Découvrez les étapes à suivre pour configurer l'envoi de notifications d'alerte d'Uptrends vers Opsgenie.",
  "url": "[URL_BASE_TOPICS]alerter/integrations/opsgenie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Opsgenie** est la plateforme de gestion des alertes et des incidents d'Atlassian. Cette plateforme vous permet d'agréger les alertes et les notifications provenant de systèmes externes (tels qu'Uptrends), et de hiérarchiser et d'assigner des actions.  
Intégrer vos alertes Uptrends dans votre environnement Opsgenie, c'est très simple ! La mise en place de l'intégration entre les deux systèmes s'effectue comme suit :

1. Configuration d'une intégration API dans Opsgenie
2. Configuration de l'intégration dans Uptrends
3. Ajout de l'intégration à une définition d'alerte dans Uptrends

Après avoir configuré cette intégration avec les paramètres d'alerte appropriés, vos alertes Uptrends généreront des alertes dans Opsgenie. Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans Opsgenie.

![]([LINK_URL_1])

L'alerte Opsgenie sera générée pour l'équipe pour laquelle vous avez mis en place l'intégration. Si vous souhaitez que les alertes soient envoyées à plusieurs équipes, vous devez créer une intégration pour chacune d'entre elles.

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Configuration de l'intégration dans Opsgenie

1. Dans votre environnement Opsgenie, créez une nouvelle équipe ou utilisez une équipe existante.
2. Dans les options pour cette équipe, allez à *Intégrations*.
3. Repérez l'intégration *API* existante (habituellement nommée *{teamname}\_API*). Si cette intégration n'existe pas encore, créez une nouvelle intégration en cliquant sur le bouton **Ajouter une intégration**, et sélectionnez le type d'intégration "API". Ouvrez cette intégration et notez la clé API dont vous en aurez besoin plus tard.
4. Enregistrez l'intégration.

L'intégration est désormais configurée dans Opsgenie.

## 2. Configuration de l'intégration dans Uptrends

Pour ajouter une nouvelle intégration pour Opsgenie dans Uptrends, suivez ces étapes :

1. Ouvrez [SHORTCODE_3] Alerte > Intégrations [SHORTCODE_4].
2. Cliquez sur [SHORTCODE_5]Ajouter intégration[SHORTCODE_6] en haut à droite.
3. Choisissez Opsgenie comme type d'intégration.
4. Donnez un nom à cette intégration.
5. Collez la clé API Opsgenie (que vous avez copiée précédemment) dans [SHORTCODE_7]Variables prédéfinies > ApiKey[SHORTCODE_8].
6. Cliquez sur [SHORTCODE_9]Enregistrer[SHORTCODE_10] pour enregistrer vos paramètres. La nouvelle intégration Opsgenie apparaîtra sur la page des intégrations.

Par défaut, l'intégration Opsgenie utilisera la version internationale de l'instance Opsgenie, avec l'URL [INLINE_CODE_1] pour les requêtes. Si vous voulez utiliser la version européenne de l'instance Opsgenie, l'URL des requêtes doit être [INLINE_CODE_2]. Pour faire la modification :

1. Dans les paramètres de l'intégration Opsgenie, activez **Personnaliser l'intégration**.
2. Cliquez sur l'onglet [SHORTCODE_11]Personnalisations[SHORTCODE_12] qui apparaît.
3. Sous **Méthode et URL**, remplacez l'URL par défaut par [INLINE_CODE_3] pour utiliser l'instance UE de l'API Opsgenie.
   ![URL de l'instance UE d'Opsgenie ]([LINK_URL_2])
4. Pour vérifier que vous utilisez la bonne instance, envoyez une alerte de test en cliquant sur le bouton [SHORTCODE_13]Envoyer une alerte de test[SHORTCODE_14].
5. Enregistrez l'intégration.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration dans vos définitions d'alerte.

[SHORTCODE_1]
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous souhaitez désactiver temporairement la réception d'alertes.
[SHORTCODE_2]

## 3. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu [SHORTCODE_15] Alerte > Définitions d'alerte [SHORTCODE_16], sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet [SHORTCODE_17]Niveau d'escalade[SHORTCODE_18] contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_3]).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, sélectionnez **l'intégration personnalisée** pour Opsgenie.
4. N'oubliez pas de cliquer sur le bouton [SHORTCODE_19]Enregistrer[SHORTCODE_20] pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration pour Opsgenie.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support]([LINK_URL_4]).
