{
  "hero": {
    "title": "Types de message"
  },
  "title": "Types de message",
  "summary": "Intégration personnalisée - déscriptions des types de message ",
  "url": "[URL_BASE_TOPICS]alerter/integrations/integrations-personnalisees/types-de-message",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Il y a différents types de messages d'alerte. Uptrends fait la distinction entre les messages **Erreur**, les messages **Rappel** et les messages **Ok**. Par défaut, tous ces types de messages sont créés avec la même configuration. Toutefois, lors de la mise en place d'une intégration personnalisée ou de la personnalisation d'une intégration existante, vous pouvez créer différents ensembles d'actions pour chaque type de message.

## Messages d'erreur, messages OK et rappels

Lorsque vous créez une définition de message dans l'onglet [SHORTCODE_1]Personnalisations[SHORTCODE_2], Uptrends utilise cette définition de message pour tous les types d'erreur : une alerte d'erreur lorsque la vérification a généré l'alerte pour la première fois, une alerte OK lorsque la vérification résout l'alerte, et des alertes de rappel (selon vos paramètres de niveau d'escalade) entre les deux.

Le contenu du message est pratiquement le même pour tous les types d'alerte, à l'exception des valeurs d'horodatage et de la variable [SYSTEM_VAR_1], à l'origine du type d'alerte.

Même si ça convient dans de nombreuses situations, l'utilisation du même contenu de message n'est pas suffisante si vous avez besoin d'un contenu différent pour différents types d'alerte, ou si vous devez créer un nouvel incident dans votre système (basé sur une alerte d'erreur) nécessitant une URL différente de celle qui a résolu le même incident (basé sur une alerte OK).

### Des messages séparés pour différents types d'alerte

Pour créer des définitions de message distinctes pour les différents types d'alerte, cliquez sur le bouton "Ajouter des étapes" en bas de l'onglet [SHORTCODE_3]Personnalisations[SHORTCODE_4]. Le bouton "Ajouter des étapes" crée une définition de message supplémentaire que vous pouvez utiliser, par exemple, pour seulement les alertes OK. Pour chaque type d'alerte, vous pouvez désormais spécifier la méthode HTTP appropriée (GET / POST / PUT / PATCH / DELETE), l'URL, les en-têtes et le corps de la requête.

Cochez les cases *Alerte d'erreur*, *Alerte d'OK* ou *Rappel d'alerte* en haut de chaque définition d'étape pour créer la configuration souhaitée. Les cases cochées s'appliquent à toutes les étapes ; les alertes OK et les alertes de rappel sont facultatives. Si vous ne souhaitez pas envoyer d'alertes OK ou d'alertes de rappels, laissez simplement ces cases décochées.

### Les alertes d'erreur et les alertes OK vont de pair

Que vous utilisiez ou non des messages distincts pour les alertes d'erreur et OK, il est utile pour le système externe de savoir quelles alertes vont ensemble. Après tout, chaque incident commence par une alerte d'erreur et se termine par une alerte OK. Pour que le système externe le comprenne, vous pouvez utiliser la variable [SYSTEM_VAR_2] dans vos messages. Les alertes d'erreur et OK partagent la même clé d'incident, mais chaque nouvel incident a une clé différente et unique. Dans certains systèmes, la clé d'incident est appelée clé de déduplication ou ID d'incident.
