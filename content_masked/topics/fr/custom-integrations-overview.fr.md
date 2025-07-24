{
  "hero": {
    "title": "Aperçu des intégrations personnalisées"
  },
  "title": "Aperçu des intégrations personnalisées",
  "summary": "Aperçu des intégrations personnalisées",
  "url": "[URL_BASE_TOPICS]alerter/integrations/integrations-personnalisees/apercu-des-integrations-personnalisees",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Et si vous pouviez connecter votre compte Uptrends au logiciel de gestion de votre organisation. Intégrer vos données d'alerte d'Uptrends avec vos processus de gestion d'incidents existants permet un fonctionnement transparent dans les procédures quotidiennes que vos équipes utilisent déjà.

 Si votre logiciel DevOps ne se trouve pas dans nos [types d'intégration prédéfinis]([LINK_URL_1]), alors vous pouvez utiliser l'option d'intégration personnalisée pour créer l'intégration vous-même. La clé pour construire une intégration réussie est de connaître le type de message attendu par l'autre système. La documentation de l'API du tiers vous indique quelle URL utiliser et quel contenu y envoyer. Souvent appelées intégrations webhook, elles permettent à Uptrends de se connecter à l'autre système avec des appels directs. Uptrends peut initier un appel à l'intégration dès qu'une alerte pertinente apparaît.

Les articles de cette section traiteront de la construction du bon contenu de message (y compris le formatage correct), de la création de différentes règles pour différents types de messages et de la manière de tester votre intégration personnalisée une fois que vous avez terminé sa mise en place.

## Configuration d'une intégration personnalisée

Pour commencer à utiliser les intégrations personnalisées, suivez ces étapes :

1. Ajoutez un modèle d'intégration personnalisé à votre compte. Pour ce faire, dans le menu *Alertes*, cliquez sur le bouton [SHORTCODE_1]\+[SHORTCODE_2] à côté de *Intégrations*, dans l'application Uptrends.
2. Une fenêtre popup apparaîtra, vous invitant à choisir un type d'intégration. Pour une intégration personnalisée, faites défiler jusqu'au bas de la liste et sélectionnez **Intégration Uptrends**.
3. Dans la section **Variables prédéfinies**, pour la variable *ApiUrl* indiquez l'URL de l'API à laquelle vous vous connectez. Vous trouverez l'URL de ce site dans la documentation ou l'interface utilisateur du système externe auquel Uptrends sera connecté.
4. N'oubliez pas de donner à l'intégration un nom approprié dans le champ **Nom d'intégration**.
5. If necessary, customize your integration by visiting the [SHORTCODE_3]Customizations[SHORTCODE_4] tab. Les autres chapitres de cet article vous guideront tout au long du processus.
6. When you're done setting up, click [SHORTCODE_5]Save[SHORTCODE_6] to store your settings. Vous pouvez à tout moment revenir à l'intégration pour terminer la personnalisation si nécessaire.

## Créer le bon contenu de message

Cette intégration sera un modèle prédéfini : un corps de message (personnalisable) au format JSON contenant toute la gamme des variables d'alerte disponibles. Ce format de message par défaut vous permet de traiter toutes les informations disponibles relatives à chaque alerte ; cependant vous pouvez supprimer les données dont vous n'avez pas besoin, ajouter vos propres données ou modifier le format du message. You can find the predefined message body under the [SHORTCODE_7]Customizations[SHORTCODE_8] tab, along with other options to further customize your integration.

- Pour comprendre comment commencer à configurer le contenu du message souhaité et comment utiliser les variables, nous vous recommandons de lire d'abord notre article sur la [construction du bon contenu de message]([LINK_URL_2]).
- Vous trouverez une description complète des variables d'alerte disponibles dans notre liste de [variables du système d'alerte]([LINK_URL_3]).
- Gardez à l'esprit que votre message sortant doit être formaté correctement. Lisez notre [guide sur le formatage des messages]([LINK_URL_4]) pour éviter des erreurs inutiles dans votre application externe.

## Types de messages

Il y a différents types de messages d'alerte. Uptrends fait la distinction entre les messages **Erreur**, les messages **Rappel** et les messages **Ok**. Par défaut, tous ces types de messages sont créés avec la même configuration. Toutefois, lors de la mise en place d'une intégration personnalisée ou de la personnalisation d'une intégration existante, vous pouvez créer différents ensembles d'actions pour chaque type de message. Consultez notre [article sur les types de messages]([LINK_URL_5]) pour en savoir plus.

## Tester votre intégration personnalisée

Une fois que vous avez créé ou modifié une intégration personnalisée, il est recommandé de la tester avant de l'utiliser en production. Notre [article sur le test de votre intégration personnalisée]([LINK_URL_6]) couvrira les moyens de tester l'intégration nouvellement mise en place.

## Ajout de l'intégration à une définition d'alerte dans Uptrends

Une définition d'intégration seule ne fait rien. Vous devez **l'attacher à un ou plusieurs niveaux d'escalade pour recevoir des alertes** via l'intégration. Pour associer une définition d'intégration à un niveau d'escalade :

1. Allez à la définition d'alerte souhaitée dans Uptrends (*Alertes* > *Définitions d'alerte*).
2. Click to open an existing definition or create a new one using the [SHORTCODE_9]Add alert definition[SHORTCODE_10] button on the top right.
3. Click an [SHORTCODE_11]Escalation level[SHORTCODE_12] tab.
4. Dans la section **Alerte par intégrations**, cochez les cases correspondant à vos définitions d'intégration personnalisées
5. Click [SHORTCODE_13]Save[SHORTCODE_14] when finished.

**Et c'est tout !** Vous avez configuré avec succès une intégration personnalisée.

Comme toujours, si vous avez des questions, n'hésitez pas de [contacter notre équipe de Support]([LINK_URL_7]).
