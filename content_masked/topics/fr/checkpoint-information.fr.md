{
  "hero": {
    "title": "Informations sur les checkpoints"
  },
  "title": "Informations sur les checkpoints",
  "summary": "Qu'est-ce qu'un checkpoint et comment faire son choix parmi toutes les options proposées par Uptrends ?",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/points-de-controle/informations-sur-les-checkpoints",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends dispose d'un vaste réseau comptant plus de {{% Features/Variable variable="CheckpointCount" %}} checkpoints de surveillance à travers le monde. Ces checkpoints peuvent être configurés pour surveiller vos sites web, serveurs et services web, et déterminer l'origine des problèmes.

## Qu'est-ce qu'un checkpoint ?

Un checkpoint ou point de contrôle est un emplacement géographique qui permet de vérifier régulièrement la disponibilité et la performance de vos moniteurs. Pour effectuer les tests, chaque checkpoint est lié à un ou plusieurs serveurs situés dans des data centers. Afin de garantir l'exactitude des mesures et des résultats, ces checkpoints utilisent principalement les serveurs DNS des fournisseurs d'accès Internet locaux, lorsqu'ils sont disponibles.

## Liste des adresses IP des checkpoints d'Uptrends

Consultez la [liste complète et actualisée des checkpoints de surveillance mondiaux d'Uptrends]([LINK_URL_1]). Cette liste contient à la fois les adresses IPv4 et IPv6.

Les listes des [adresses IPv4]([LINK_URL_2]) et des [adresses IPv6]([LINK_URL_3]) sont également à votre disposition. Pour télécharger les adresses IP au format JSON ou XML, lisez l'article de notre base de connaissances intitulé [Obtenir des données de checkpoints au format JSON ou XML]([LINK_URL_4]).

## Gamme de checkpoints

Compte tenu du grand nombre de checkpoints disponibles avec Uptrends, vous pouvez librement choisir différents emplacements où effectuer vos tests et vérifier le comportement des résultats de surveillance.

Les checkpoints sont aussi très utiles pour :

- Tester le réseau de diffusion de contenu (CDN) au moyen de nombreux endpoints.
- Tester le réseau DNS mondial. Bon nombre des checkpoints d'Uptrends utilisent un DNS local, ce qui vous permet de vérifier que vos changements de DNS se propagent à travers le monde d'une manière correcte.
- Tester si la latence se trouve dans la limite acceptable quand le point de contrôle est loin ou dépend des fournisseurs d'un réseau dorsal.

## Choisir le bon ensemble de checkpoints

La sélection de plusieurs checkpoints est incluse dans votre abonnement et n'entraîne aucun coût supplémentaire. Uptrends vous recommande de sélectionner autant de checkpoints que possible. En effet, cela vous permettra de mieux évaluer la performance de votre moniteur et d'utiliser d'autres emplacements pendant la maintenance et les temps d'arrêt des checkpoints.

Par défaut, Uptrends sélectionne des emplacements de checkpoint dans le monde entier, y compris en Europe, en Amérique du Nord, en Afrique, en Asie, en Australie, en Amérique du Sud et au Moyen-Orient. Votre sélection de checkpoints sera plus efficace si elle vise une région particulière.

Vous devez sélectionner au moins trois checkpoints. Si, pour une raison ou pour une autre, l'un des checkpoints est en maintenance, au moins deux autres checkpoints pourront effectuer les vérifications et vérifier les erreurs.

Depuis l'onglet [SHORTCODE_5]Checkpoints[SHORTCODE_6] d'un moniteur, vous pouvez activer des checkpoints individuels, mais aussi des pays et des continents entiers. Si vous sélectionnez un pays ou un continent, vous bénéficierez immédiatement des nouveaux checkpoints lorsque nous ajouterons des emplacements supplémentaires pour cette région. Votre couverture augmente automatiquement chaque fois que notre réseau grandit ! Si vous souhaitez omettre certains checkpoints, vous pouvez tout de même bénéficier automatiquement de l'élargissement de notre réseau. Plutôt que de sélectionner tous les checkpoints d'un pays sauf un, utilisez la fonction d'[exclusion de checkpoints]([LINK_URL_5]) pour contrôler précisément vos ensembles de checkpoints.

[SHORTCODE_1]
**Remarque :** Les options dont vous disposez diffèrent selon le type de compte. Les utilisateurs des versions Starter, Premium ou Professional peuvent sélectionner des ensembles de points de contrôle prédéfinis. Les utilisateurs des versions Business ou Enterprise peuvent sélectionner chaque checkpoint disponible de manière individuelle.
[SHORTCODE_2]

## Temps d'arrêt des checkpoints

En cas de maintenance ou de problème de réseau local, les emplacements de checkpoints peuvent être temporairement hors service. Si tous vos checkpoints sont indisponibles, Uptrends s'assure que les vérifications soient effectuées depuis un emplacement de secours qui ne fait pas partie de votre sélection. Si seulement quelques-uns de vos checkpoints sont indisponibles, Uptrends effectue les vérifications depuis les autres checkpoints sélectionnés.

L'emplacement de secours est activé par défaut dans le menu [SHORTCODE_7] Paramètres de compte [SHORTCODE_8] > **Checkpoints de secours**. Les tests sont ainsi effectués depuis d'autres emplacements et ne risquent pas d'être compromis. Une fois que les checkpoints redeviennent disponibles, Uptrends réactive automatiquement les paramètres de checkpoint de votre moniteur.

Il existe quelques situations où l'emplacement de secours n'est pas une solution idéale. Par exemple, si vous utilisez une liste blanche où seules certaines [adresses IP d'Uptrends]([LINK_URL_6]) sont listées. Dans ce cas, suivez les étapes suivantes pour résoudre le problème :

- Augmentez le nombre de checkpoints sélectionnés pour réduire le risque que la surveillance soit effectuée depuis un emplacement de checkpoint indisponible.

- Ouvrez le menu [SHORTCODE_9] Paramètres de compte [SHORTCODE_10] et décochez l'option **Checkpoints de secours**. La désactivation de l'option **Checkpoints de secours** signifie qu'aucun autre emplacement ne sera disponible pour vérifier votre moniteur. Si votre moniteur commence à effectuer un test et détecte un checkpoint indisponible, il passera automatiquement cette vérification. Ensuite, le moniteur commencera une autre vérification lors du prochain [intervalle]([LINK_URL_7]) de vérification. La désactivation de cette option peut causer des écarts dans vos résultats de surveillance.

## Vous rencontrez des difficultés avec les checkpoints ?

Un point de contrôle vous pose problème ? [Contactez-nous]([LINK_URL_8]) !

[SHORTCODE_3]
**Remarque :** Certains outils de localisation géographique sur Internet ne montrent pas correctement l'emplacement physique de nos centres de données. [En savoir plus]([LINK_URL_9]).
[SHORTCODE_4]
