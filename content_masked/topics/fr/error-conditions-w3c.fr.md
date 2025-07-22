{
  "hero": {
    "title": "Conditions d'erreur liées aux métriques du W3C"
  },
  "title": "Conditions d'erreur liées aux métriques du W3C",
  "summary": "Cet article vous explique comment définir les seuils de déclenchement des erreurs liées aux métriques du W3C.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-w3c",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le World Wide Web Consortium (ou W3C) est une organisation internationale qui travaille au développement de standards pour le World Wide Web. À ce titre, le W3C a défini une norme pour les navigateurs et les applications web, qui permet de générer et d'afficher des informations sur les durées de chargement des pages web.

Les types de moniteurs qui utilisent un [navigateur avec des métriques supplémentaires]([LINK_URL_1]) mesurent les [métriques correspondant aux durées de navigation du W3C]([LINK_URL_2]). Ces métriques figurent dans les détails de vérification du moniteur et peuvent servir à définir des conditions d'erreur. Les conditions liées aux métriques du W3C font partie des [conditions d'erreur]([LINK_URL_3]).

Chaque type de moniteur s'accompagne de conditions d'erreur différentes. Consultez le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]([LINK_URL_4]) pour connaître les options associées à chaque type de moniteur.

## Définition des conditions d'erreur d'après les métriques du W3C

Pour définir les conditions d'erreur d'après les durées de navigation du W3C :

1. Ouvrez le menu [SHORTCODE_1] Surveillance > Configuration du moniteur [SHORTCODE_2].
2. Cliquez sur le nom du moniteur pour le modifier.
3. Ouvrez l'onglet [SHORTCODE_3] Conditions d'erreur [SHORTCODE_4].
4. Affichez la catégorie *Vérifier les métriques W3C* en cliquant sur la flèche qui la précède.

   ![capture d'écran des conditions d'erreur liées aux métriques W3C]([LINK_URL_5])

5. Activez les conditions d'erreur en cochant la case correspondante et en précisant la valeur applicable. Laissez les métriques décochées si vous ne souhaitez pas appliquer cette condition d'erreur.
6. Cliquez sur le bouton [SHORTCODE_5]Enregistrer[SHORTCODE_6].

## Métriques du W3C [ANCHOR_1]

Les métriques du W3C mesurées par les moniteurs utilisant un [navigateur avec des métriques supplémentaires]([LINK_URL_6]) sont décrites dans notre article intitulé [Mesures des durées de navigation du W3C]([LINK_URL_7]). Ces métriques correspondent aux conditions d'erreur sélectionnées dans la catégorie *Vérifier les métriques W3C*. La seule métrique qui n'est pas présente dans cette liste de conditions d'erreur est "load event". Pour savoir comment configurer une condition d'erreur basée sur cette métrique, reportez-vous à la section [Condition d'erreur liée au load event]([LINK_URL_8]) ci-dessous.

## Condition d'erreur liée au load event [ANCHOR_2]

La métrique load event du W3C ne se trouve pas dans la catégorie *Vérifier les métriques W3C*. Si vous souhaitez créer une condition d'erreur d'après cette métrique, vous pouvez le faire avec les moniteurs [Full Page Check]([LINK_URL_9]). Suivez les étapes suivantes :

1. Ouvrez les paramètres du moniteur.
2. Dans l'onglet [SHORTCODE_7] Principal [SHORTCODE_8], choisissez le **type de navigateur** *Chrome avec des métriques supplémentaires*.
3. Dans l'onglet [SHORTCODE_9] Avancé [SHORTCODE_10], vous trouverez la section *Mesure*. Pour l'option **Baser le temps de chargement sur**, cochez la case *W3C load event*.
4. Dans l'onglet [SHORTCODE_11] Conditions d'erreur [SHORTCODE_12], définissez les seuils dans la section **Vérifier le temps de chargement de la page**.

L'article de la base de connaissances intitulé [Conditions d'erreur liées à la disponibilité des pages]([LINK_URL_10]) contient de plus amples informations sur la définition des limites applicables aux temps de chargement.
