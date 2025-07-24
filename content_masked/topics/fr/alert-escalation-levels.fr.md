{
  "hero": {
    "title": "Niveaux d'escalade des alertes"
  },
  "title": "Niveaux d'escalade des alertes",
  "summary": "Grâce aux définitions et aux niveaux d'escalade des alertes, vous pouvez configurer des alertes pour des destinataires ou des intégrations spécifiques, en fonction de la politique de gestion des interruptions en vigueur dans votre entreprise ou organisation.",
  "url": "[URL_BASE_TOPICS]alerter/niveaux-des-escalades-des-alertes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Que sont les niveaux d'escalade ?

Le système d'alerte d'Uptrends a été conçu pour répondre aux besoins des équipes. Les niveaux d'escalade personnalisables vous permettent d'alerter les bonnes personnes au bon moment, en fonction du problème.

Chaque niveau d'escalade contient plusieurs paramètres pour configurer l'alerte : nombre de rappels, méthode de notification et destinataires. Ces options peuvent être ajustées dans la définition d'alerte.

Vous pouvez configurer jusqu'à trois niveaux d'escalade et générer des alertes selon vos propres règles :

- Générez une alerte lorsque des erreurs se produisent durant une période donnée ou lorsqu'un nombre spécifique d'erreurs est atteint.
- Définissez combien de rappels doivent être envoyés et à quel intervalle.
- Mettez en place des méthodes d'alerte au moyen des [intégrations]([LINK_URL_1]).
- Ajoutez un message personnalisé (pour les notifications Slack, PagerDuty et par e-mail).
- Insérez un journal traceroute dans les e-mails.
- Ajoutez une adresse e-mail supplémentaire pour alerter d'autres personnes.
- Sélectionnez les opérateurs ou les groupes d'opérateurs qui reçoivent l'alerte.
- Décidez si vous souhaitez envoyer des alertes OK et des rappels (pour chaque intégration).

## Configuration d'une escalade d'alerte

Pour chaque définition d'alerte, vous avez jusqu'à trois niveaux d'escalade. Pour configurer vos niveaux d'escalade :

1. Ouvrez [SHORTCODE_1] Alertes > Définitions d'alerte [SHORTCODE_2] et sélectionnez la définition d'alerte à modifier. Vous pouvez aussi chercher une définition précise depuis la [barre de recherche du menu Uptrends]([LINK_URL_2]). Si vous devez créer une nouvelle définition d'alerte, lisez l'article [Créer des définitions d’alerte]([LINK_URL_3]).
2. Ouvrez l'onglet [SHORTCODE_3] Niveau d'escalade 1 [SHORTCODE_4].
3. Cochez la case **Actif** si elle n'est pas cochée.
4. Définissez les règles pour ce **niveau d'escalade** en remplissant les paramètres dans la partie *Générer une alerte quand*.
5. Définissez la fréquence des rappels. Pour en savoir plus, lisez l'article de la base de connaissances intitulé [Rappels d'alerte]([LINK_URL_4]).
6. Choisissez une ou plusieurs options dans la partie **Alertes par intégrations**. Vous pouvez sélectionner les **alertes par e-mail**, les **alertes par SMS** (les messages et les SMS consomment des crédits de message) et les **alertes par téléphone**.
7. Si vous avez défini d'autres intégrations, vous pouvez les sélectionner à cet endroit. Pour en savoir plus, lisez l'article de la base de connaissances sur les [intégrations]([LINK_URL_5]).
8. Pour la plupart des intégrations, vous pouvez indiquer si vous souhaitez recevoir des alertes OK et des rappels. Déroulez l'intégration en cliquant sur la flèche qui la précède. Vous pouvez ainsi activer les options correspondantes.

   ![Capture d'écran des options liées aux alertes]([LINK_URL_6])

   Les [intégrations personnalisées]([LINK_URL_7]) utilisent des [types de messages]([LINK_URL_8]) distincts pour traiter les différentes alertes (erreur, rappel et OK). Les ajustements apportés aux types de messages sont visibles dans la définition d'alerte, mais vous ne pouvez pas les modifier. Les modifications se font directement depuis l'intégration personnalisée.
9. Vous pouvez ajouter un message personnalisé (cette option est facultative et ne s'applique pas à toutes les intégrations).
10. Cochez la case **Traceroute** pour inclure un enregistrement traceroute dans les e-mails.
11. Renseignez la section **Groupes et opérateurs** pour sélectionner les opérateurs concernés par le niveau d'escalade. Souvenez-vous que les alertes ne sont envoyées que lorsque l'opérateur désigné est actif et en service. L'état *Actif* est l'un des principaux paramètres des opérateurs. L'état "En service" dépend des [horaires de repos]([LINK_URL_9]) de l'opérateur.
12. Configurez les niveaux d'escalade 2 et 3 si votre organisation les prévoit.
13. Cliquez sur le bouton [SHORTCODE_5]Enregistrer[SHORTCODE_6] lorsque vous avez terminé de configurer vos niveaux.

## Alertes par intégrations

L'article de la base de connaissances sur les [intégrations]([LINK_URL_10]) contient de plus amples informations sur les différents types d'intégrations, notamment le téléphone (qui utilise des crédits de message) et les intégrations comme [PagerDuty]([LINK_URL_11]), [Microsoft Teams]([LINK_URL_12]), [Slack]([LINK_URL_13]) et [StatusHub]([LINK_URL_14]).

## Tests des configurations d'alerte

Après avoir configuré vos niveaux d'escalade et ajouté les intégrations que vous souhaitez utiliser, vous pouvez effectuer des tests pour vérifier que tout fonctionne correctement. Consultez l'article de la base de connaissances intitulé [Tester les messages d’alerte]([LINK_URL_15]) pour connaître les méthodes disponibles pour chaque intégration.