{
  "hero": {
    "title": "Recevez vos alertes de suivi de site web dans ServiceNow"
  },
  "title": "Intégration ServiceNow",
  "summary": "Recevez les alertes de suivi de site web d'Uptrends dans ServiceNow.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/service-now",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**ServiceNow** est une plateforme cloud qui vous permet de gérer l'ensemble de vos opérations IT au moyen de différentes applications, dont une consacrée à la gestion des incidents.

L'intégration de **ServiceNow** à Uptrends fait automatiquement apparaître les incidents dans votre compte **ServiceNow**. Pour en savoir plus sur ServiceNow, reportez-vous à la [documentation de l'intégration ServiceNow]([LINK_URL_1]) et aux [API REST ServiceNow REST]([LINK_URL_2]).

## Configurer l'intégration

L'ajout d'intégrations pour **ServiceNow** dans Uptrends nécessite que vous ayez un compte ServiceNow. Préparez votre nom d'instance et vos données d'authentification.

Pour configurer l'intégration :

1. Dans l'application web d'Uptrends, ouvrez le menu [SHORTCODE_3] Alerte > Intégrations [SHORTCODE_4].
2. En haut à droite, cliquez sur le bouton [SHORTCODE_5] Ajouter intégration [SHORTCODE_6].
3. Dans le menu contextuel, sélectionnez **ServiceNow** comme type d'intégration tierce.
4. Cliquez sur le bouton [SHORTCODE_7] Choisir [SHORTCODE_8] pour créer une nouvelle intégration.
5. **ServiceNow** est la valeur par défaut du champ **Types d'intégration**. Précisez le nom de votre nouvelle intégration.
6. Dans la section **Variables prédéfinies**, remplissez les champs **Valeur** suivants :

- [INLINE_CODE_1] : le nom de votre instance de ServiceNow. Vous le trouverez dans l'URL de ServiceNow : [INLINE_CODE_2].
- [INLINE_CODE_3] : le nom d'utilisateur de votre compte ServiceNow.
- [INLINE_CODE_4] : le mot de passe de votre compte ServiceNow.

Vous pouvez choisir de saisir ces valeurs sous forme de **texte brut** ou récupérer les **identifiants de coffre-fort** stockés dans le [coffre-fort]([LINK_URL_3]). L'intégration utilisera automatiquement une authentification de base pour accéder à la plateforme **ServiceNow**.

![Intégration ServiceNow]([LINK_URL_4])

7. (Facultatif) Pour personnaliser vos paramètres de connexion et d'intégration, cochez la case **Personnaliser l'intégration**. En activant la personnalisation, vous pouvez :

- Ajouter des **variables prédéfinies** et modifier les variables prédéfinies existantes, en vue de les utiliser pour l'authentification, les niveaux d'escalade et les définitions d'étape.
- Ajouter et définir des étapes pour les différents types d'alerte. La plupart du temps, une seule étape HTTP sera suffisante pour votre configuration. Si vous devez créer des étapes distinctes pour d'autres scénarios, comme l'authentification, cliquez sur le bouton [SHORTCODE_9] Ajouter des étapes [SHORTCODE_10].
- Personnaliser les [messages d'alerte]([LINK_URL_5]) pour différents types d'alerte. Ce message précise le service tiers ou l'API à contacter, le contenu des messages HTTP, l'authentification requise et d'autres informations.

![Variables prédéfinies personnalisées]([LINK_URL_6])

![Définition d'étape personnalisée]([LINK_URL_7])

8. (Facultatif) Dans l'onglet [SHORTCODE_11] Autorisations [SHORTCODE_12], sélectionnez un opérateur ou un groupe d'opérateurs afin d'ajouter des [autorisations d'intégration]([LINK_URL_8]).

9. Cliquez sur [SHORTCODE_13] Enregistrer [SHORTCODE_14] pour confirmer les changements.

10. Pour vérifier votre configuration, testez votre intégration personnalisée au moyen des [messages test]([LINK_URL_9]). Pour en savoir plus, lisez la section d'article de notre base de connaissances intitulée [Envoi d'un message de test à des systèmes tiers]([LINK_URL_10]).

À ce stade, vous avez terminé de configurer l'intégration **ServiceNow** dans Uptrends. Vous pouvez utiliser cette intégration et l'ajouter à vos [définitions d'alerte]([LINK_URL_11]).

[SHORTCODE_1]
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous voulez désactiver temporairement la réception d'alertes.
[SHORTCODE_2]

Pour toute question, veuillez [contacter notre équipe de support]([LINK_URL_12]).
