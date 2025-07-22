{
  "hero": {
    "title": "Modèles de moniteur"
  },
  "title": "Modèles de moniteur",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/gestion-moniteurs/modeles-moniteurs",
  "summary": "Le modèle de moniteur vous permet d'appliquer des paramètres à plusieurs moniteurs en une seule fois.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Avec Uptrends, surveiller la disponibilité et la performance d'un site web, d'un serveur ou d'un service web est plus facile que jamais. Mais comment faire pour surveiller une série de services, et les configurer rapidement ? Le mieux est d'utiliser des **modèles de moniteur**.

Un modèle de moniteur est un outil qui permet d'ajouter certains paramètres, comme des *conditions d'erreur*, des *checkpoints* et des *périodes de maintenance* à des groupes de moniteurs. Il faut le considérer comme un moyen très rapide de dupliquer des configurations de moniteur.

## Pourquoi les modèles de moniteur sont-ils utiles ?

Créer manuellement une série de moniteurs qui ont les mêmes règles de conditions d'erreur, les mêmes checkpoints pour la surveillance ou les mêmes périodes de maintenance peut être long et fastidieux. En utilisant un modèle de moniteur, vous pouvez réduire le temps et l'effort nécessaires pour ajouter des règles aux moniteurs, et ainsi vous occuper de choses plus utiles.

[SHORTCODE_1] **Remarque** : vous devez être un administrateur ou disposer de [l'autorisation Gérer les modèles de moniteur]([LINK_URL_1]) pour pouvoir créer, modifier et exécuter des modèles de moniteur. [SHORTCODE_2]

## Comment créer un modèle de moniteur ?

1. Cliquez sur [SHORTCODE_5]Configuration de compte > Modèles de moniteur[SHORTCODE_6].
2. Dans l'angle supérieur droit de l'écran, cliquez sur le bouton [SHORTCODE_7]Ajouter un modèle de moniteur[SHORTCODE_8].
3. Vous pouvez désormais personnaliser vos paramètres de moniteur :
- Définissez un nom pour votre modèle de moniteur.
- Dans les paramètres du moniteur, vous pouvez définir des [limites de temps de chargement]([LINK_URL_2]) de façon à générer une erreur lorsque la réponse du serveur est plus lente que la limite indiquée.
   Vous pouvez aussi sélectionner un [agent utilisateur]([LINK_URL_3]) afin d'identifier le type de navigateur et le système d'exploitation de l'utilisateur, dont la valeur sera envoyée au serveur lors des requêtes HTTPS. Par défaut, l'agent utilisateur est défini sur *Garder inchangé*.
- Dans l'onglet [Checkpoints]([LINK_URL_4]), utilisez les cases à cocher pour déterminer les emplacements depuis lesquels vous souhaitez effectuer la surveillance.
- Vous pouvez aussi ajouter des [périodes de maintenance]([LINK_URL_5]) et préciser leur récurrence.

[SHORTCODE_3] **Remarque** : Lors de l'application d'un modèle de moniteur, nous appliquons uniquement les paramètres que vous avez modifiés lors de la création du modèle. Par exemple, si vous souhaitez créer un modèle pour appliquer uniquement une période de maintenance, souvenez-vous de modifier uniquement ce paramètre lorsque vous créez le modèle de moniteur. Il en va de même pour une sélection de checkpoints et une condition d'erreur. [SHORTCODE_4]

4. Cliquez ensuite sur le bouton [SHORTCODE_9]Enregistrer[SHORTCODE_10].

Vous pouvez désormais appliquer vos modèles de moniteur à tout moniteur existant, selon deux options. La première consiste à actualiser le moniteur individuellement ou à modifier plusieurs moniteurs simultanément via le menu [SHORTCODE_11]Modèles de moniteur[SHORTCODE_12]. La deuxième vous permet d'appliquer directement un modèle depuis le moniteur ouvert via [SHORTCODE_13]l'éditeur de moniteur [SHORTCODE_14]. Lisez les instructions détaillées ci-dessous pour en savoir plus sur l'application des modèles de moniteur.

## Appliquer un modèle de moniteur
Pour appliquer un modèle à un moniteur individuel ou modifier plusieurs moniteurs simultanément :

1. Cliquez sur [SHORTCODE_15]Configuration de compte > Modèles de moniteur[SHORTCODE_16].
2. Trouvez le modèle de moniteur qui vous intéresse dans la liste, et cliquez sur **Valider**.
3. Sélectionnez le ou les moniteurs ou groupes de moniteurs auxquels vous souhaitez appliquer le modèle.
4. Cliquez sur le bouton [SHORTCODE_17] Valider [SHORTCODE_18].

Les réglages précisés seront appliqués aux moniteurs ou groupes de moniteurs sélectionnés.

## Pour appliquer un modèle de moniteur depuis l'éditeur de moniteur :
Pour appliquer un modèle directement depuis le moniteur ouvert :

1. Ouvrez le menu [SHORTCODE_19] Surveillance > Configuration du moniteur [SHORTCODE_20].
2. Cliquez sur le nom du moniteur auquel vous voulez appliquer le modèle.
3. En bas de la page de l'éditeur de moniteur, cliquez sur le bouton [SHORTCODE_21] Appliquer le modèle [SHORTCODE_22].
4. Dans la boîte de dialogue Appliquer le modèle, sélectionnez le modèle à appliquer dans le menu déroulant. Toutes les sections disponibles dans votre modèle s'affichent. Cochez ou décochez les cases selon vos préférences. Si les options sont grisées, cela signifie que le modèle ne contient pas de paramètres pour cette section.

![Capture d'écran montrant la fenêtre contextuelle d'application d'un modèle de moniteur dans la fenêtre de l'éditeur de moniteur]([LINK_URL_6])

5. Cliquez sur le bouton [SHORTCODE_23] Appliquer [SHORTCODE_24] pour confirmer les changements appliqués à votre moniteur.
