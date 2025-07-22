{
  "hero": {
    "title": "Afficher les statuts de vos API et de votre site dans StatusHub"
  },
  "title": "Intégration StatusHub",
  "summary": "Profitez de cette intégration pour combiner la puissance des capacités d'alerte de StatusHub avec vos paramètres Uptrends.",
  "url": "[URL_BASE_TOPICS]alerter/integrations/statushub",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Intégrer votre compte [StatusHub]([LINK_URL_1]) à Uptrends vous permet de mettre automatiquement à jour les informations sur le statut de vos services dans votre page de statut StatusHub. La mise en place de l'intégration entre les deux systèmes consiste en 3 étapes :

1. Configuration des intégrations de webhook dans StatusHub
2. Création d'une intégration et spécification des webhooks dans Uptrends
3. Création des liens de service dans Uptrends pour lier les moniteurs Uptrends aux services StatusHub

Vous trouverez ci-dessous une description détaillée des étapes nécessaires pour intégrer Uptrends à vos pages de statut StatusHub.

## 1. Configuration des intégrations de webhook dans StatusHub

1. D'abord, nous allons tout préparer du côté de StatusHub. Connectez-vous à votre compte StatusHub et cliquez sur l'icône en forme de crayon pour modifier votre site de statut.

2. Cliquez sur "Service & integrations" (Services et intégrations) dans le menu à gauche. Ensuite, vous allez modifier chaque service que vous voulez contrôler avec Uptrends.

3. Dans la fenêtre d'édition d'un service, recherchez la section "Enable/disable integrations" (Activer ou désactiver les intégrations). Cliquez sur le bouton Uptrends et assurez-vous qu'il est en surbrillance.

4. Au bas de la fenêtre contextuelle, cliquez sur "Update Service" (Actualiser le service). De retour dans la vue d'ensemble des services, vous verrez que le service affiche maintenant une URL de ce type :

   [INLINE_CODE_1]

   Nous utiliserons cette URL plus tard pour lier Uptrends à ce service StatusHub.

5. Répétez cette procédure pour chaque service que vous souhaitez contrôler avec Uptrends.

L'intégration est désormais configurée dans StatusHub.

[SHORTCODE_1]
**Astuce :** Dans Uptrends, il n'y a pas de limite au nombre de services de StatusHub que vous pouvez contrôler. Vous pouvez créer autant de liens de service que vous le souhaitez, ou commencer par un seul.
[SHORTCODE_2]

## 2. Configuration de l'intégration dans Uptrends

1. Dans votre compte Uptrends, sélectionnez [SHORTCODE_5] Alerte > Intégrations [SHORTCODE_6] dans le menu latéral.
2. Pour configurer une nouvelle intégration StatusHub, cliquez sur **Ajouter intégration** en haut à droite.
3. Choisissez StatusHub comme type d'intégration. Spécifiez un nom pour cette intégration (*StatusHub* fera l'affaire).
4. Enregistrez l'intégration.
5. Dans la fenêtre suivante (qui présente la vue d'ensemble des intégrations), sélectionnez l'intégration que vous venez d'enregistrer.
6. De retour dans la page d'intégration de StatusHub, donnez-nous quelques informations sur vos services StatusHub. Cliquez sur le bouton [SHORTCODE_7] Ajouter un service [SHORTCODE_8] en haut à droite.
7. Indiquez le nom du service et l'URL du service pour chaque service StatusHub. L'URL du service est l'URL du webhook que vous venez de créer en activant la fonction Uptrends dans StatusHub.
8. Enfin, cliquez sur [SHORTCODE_9]Enregistrer[SHORTCODE_10] pour enregistrer vos paramètres. La nouvelle intégration de StatusHub apparaîtra sur la page Intégrations.

## 3. Utilisation de l'intégration de StatusHub dans les définitions d'alerte

Pour réellement commencer à utiliser l'intégration, nous devons l'attacher à au moins une définition d'alerte et mettre en place des liens de service. Un lien de service est un lien entre un moniteur Uptrends et un service StatusHub. Les alertes pour ce moniteur seront envoyées au service que vous liez.

1. Accédez à l'une de vos définitions d'alerte ou créez-en une nouvelle ([SHORTCODE_11] Alerte > Définitions d'alerte [SHORTCODE_12]).
2. Sélectionnez le niveau d'escalade auquel vous voulez ajouter StatusHub.
3. Dans la section **Alertes par intégrations**, localisez l'intégration de StatusHub et sélectionnez-la. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_2]).
4. L'intégration n'est pas encore active ; cliquez sur la case à cocher pour l'activer dans ce niveau d'escalade.
5. Un bouton [SHORTCODE_13]Ajouter un lien de service[SHORTCODE_14] apparaît. Cliquez dessus pour créer un lien entre un moniteur Uptrends sur la gauche et un service StatusHub sur la droite. En utilisant ces paramètres, vous pouvez définir précisément quel moniteur Uptrends surveille quel service dans StatusHub. Vous pouvez ajouter autant de liens de service à ce niveau d'escalade que nécessaire.
6. Cliquez sur le bouton [SHORTCODE_15]Enregistrer[SHORTCODE_16] en bas à gauche pour enregistrer cette définition d'alerte.

[SHORTCODE_3]
**Astuce :** La plupart des configurations utilisent des liens de service de un à un entre les moniteurs et les services. Cependant, vous pouvez également créer des configurations plus avancées. Par exemple, il est possible de créer plusieurs liens de service qui utilisent un seul moniteur pour mettre à jour plusieurs services dans StatusHub.
[SHORTCODE_4]

## À quoi vous attendre lorsque votre intégration est terminée

Les conditions normales de définition d'alerte s'appliquent. Lorsque Uptrends détecte une erreur pour l'un de vos moniteurs, nous générons une alerte en fonction des paramètres de vos niveaux d'escalade. Lorsqu'un niveau d'escalade déclenche une nouvelle alerte, nous générons un nouvel incident dans StatusHub pour le ou les services concernés. Le statut du service est défini sur **Service disruption** (Perturbation de service) et le nouvel incident obtient le statut **Investigating** (En cours d'étude). Votre page d'état StatusHub devrait se mettre à jour immédiatement pour refléter ces changements.

Cette situation reste inchangée tant que la situation d'erreur continue dans Uptrends. En attendant, vous pouvez mettre à jour vos services StatusHub comme bon vous semble. Dès qu'Uptrends détectera que l'erreur a été résolue, nous mettrons à jour votre service sur **Service is operating normally** (Fonctionnement normal du service), et l'incident sur **Monitoring** (Sous surveillance). Lorsque vous êtes sûr que le problème a été résolu, vous pouvez réinitialiser l'incident sur **Resolved** (Résolu) dans StatusHub. De cette façon, vous pouvez toujours contrôler ce qui est affiché sur votre page de statut.

Vous avez des questions sur la configuration à adopter ? Veuillez [contacter notre équipe de support]([LINK_URL_3]).
