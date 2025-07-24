{
  "hero": {
    "title": "Recevoir des alertes dans AlertOps"
  },
  "title": "AlertOps",
  "summary": "Découvrez comment intégrer vos alertes Uptrends dans AlertOps",
  "url": "[URL_BASE_TOPICS]alerter/integrations/alertops",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**AlertOps** est un outil d'automatisation des opérations en temps réel. Cet outil vous permet de hiérarchiser vos incidents et d'automatiser vos processus. Les incidents majeurs peuvent être facilement gérés en mobilisant les équipes de garde et en leur fournissant les informations dont elles ont besoin.

1. Configuration de l'intégration entrante dans AlertOps
2. Configuration de l'intégration dans Uptrends
3. Ajout de l'intégration à une définition d'alerte dans Uptrends

Une fois que vous avez configuré cette intégration avec les paramètres d'alerte appropriés, vos alertes Uptrends généreront également des alertes dans AlertOps. Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans AlertOps.![]([LINK_URL_1])

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Configuration de l'intégration entrante dans AlertOps

1. Dans l'interface d'AlertOps, accédez au menu *Inbound Integrations* (sous *Integrations* dans le menu de la barre latérale).
2. Ouvrez l'onglet **API**, puis cliquez sur le bouton *ADD API INTEGRATION*.
3. Dans la fenêtre suivante, cliquez sur *Uptrends* pour sélectionner l'intégration par défaut d'Uptrends.
4. Donnez à l'intégration un nom parlant et sélectionnez le ou les groupes ou utilisateurs destinataires dans les champs **Recipient Group(s)/User(s)**.

   ![]([LINK_URL_2])
5. Cliquez sur le bouton *Save* pour enregistrer.
6. Notez **l'URL de l'API** qui est maintenant répertoriée dans l'interface d'AlertOps. Vous en aurez besoin lors de l'intégration du côté Uptrends.

Vous avez terminé la configuration de l'intégration du côté AlertOps.

[SHORTCODE_1]
**Remarque** : AlertOps propose une intégration prédéfinie pour Uptrends, qui doit normalement être immédiatement utilisable. Cette intégration est largement personnalisable du côté d'AlertOps. À ce stade, nous vous recommandons toutefois de ne modifier aucun des paramètres avancés. Une fois que vous avez vérifié que l'intégration fonctionne, vous pourrez la personnaliser en fonction de vos besoins.
[SHORTCODE_2]

## 2. Configuration de l'intégration dans Uptrends

Pour ajouter une nouvelle intégration pour AlertOps dans Uptrends, procédez comme suit :

1. Ouvrez [SHORTCODE_3] Alerte > Intégrations [SHORTCODE_4].
2. Cliquez sur [SHORTCODE_5]Ajouter intégration[SHORTCODE_6] en haut à droite.
3. Choisissez AlertOps comme type d'intégration.
4. Donnez un nom à cette intégration.
5. Collez **l'URL d'API** d'AlertOps dans le champ correspondant dans les [SHORTCODE_7]variables prédéfinies[SHORTCODE_8].
6. Cliquez sur [SHORTCODE_9]Enregistrer[SHORTCODE_10] pour enregistrer vos paramètres. La nouvelle intégration AlertOps apparaîtra sur la page Intégrations.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration dans vos définitions d'alerte.

## 3. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu [SHORTCODE_11] Alerte > Définitions d'alerte [SHORTCODE_12], sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet [SHORTCODE_13]Niveau d'escalade[SHORTCODE_14] contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_3]).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, il s'agira de **l'intégration personnalisée** pour AlertOps.
4. N'oubliez pas de cliquer sur le bouton [SHORTCODE_15]Enregistrer[SHORTCODE_16] pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration pour AlertOps.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support]([LINK_URL_4]).
