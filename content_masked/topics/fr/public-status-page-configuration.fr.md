{
  "hero": {
    "title": "Configuration d'une page de statut publique"
  },
  "title": "Configuration d'une page de statut publique",
  "summary": "Cet article vous explique comment créer et configurer une nouvelle page de statut publique.",
  "url": "[URL_BASE_TOPICS]dashboards-et-rapports/pages-statut/configuration-page-statut-publique",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Création d'une page de statut publique

1. Ouvrez [SHORTCODE_3] Configuration de compte > Pages de statut publiques [SHORTCODE_4].
2. La page affiche la liste de vos pages de statut publiques. Par défaut, votre compte comprend une page de statut préconfigurée.
3. Cliquez sur le bouton [SHORTCODE_5]Ajouter une page de statut publique[SHORTCODE_6] en haut à droite.
4. Saisissez un *nom* descriptif pour votre page de statut publique.
5. L'*URL* sera créée et accessible dès que vous aurez enregistré la page de statut. Cette URL est nécessaire pour [intégrer la page de statut]([LINK_URL_1]) dans une page web.
6. Cochez l'option *Publier* pour rendre votre page de statut publique disponible depuis l'adresse indiquée dans le champ *URL*. Ainsi, la page peut être consultée sans aucun identifiant de connexion à Uptrends.
7. Ensuite, ouvrez l'onglet [SHORTCODE_7]Données[SHORTCODE_8].
8. Configurez la **période** dont vous souhaitez récupérer et afficher les données.
9. Définissez aussi le **SLA** ([accord de niveau de service]([LINK_URL_2])). Les données qui s'affichent sur votre page de statut publique dépendent du SLA sélectionné.
10. Ajoutez les moniteurs ou groupes de moniteurs dont vous souhaitez afficher les données sur la page de statut.
11. Cliquez sur le bouton [SHORTCODE_9]Enregistrer[SHORTCODE_10] en bas de l'écran.

Vous avez désormais configuré votre page de statut publique, et vous revenez à la liste principale, où vous pouvez voir votre nouvelle page de statut publique. Pour prévisualiser les pages publiées, cliquez sur les liens qui s'affichent.

Si vous avez besoin d'aide, n'hésitez pas à [soumettre un ticket de support]([LINK_URL_3]).

## Intégration d'une page de statut publique dans une page web [ANCHOR_1]

Intégrer une page de statut publique dans une page web est facile.
1. Ouvrez l'onglet [SHORTCODE_11]Personnalisation[SHORTCODE_12] de la page de statut publique.
2. Copiez la valeur du *Code d'intégration*, qui ressemble à cela : [INLINE_CODE_1].
3. Collez le *code d'intégration* dans la source de votre page web.
4. Enregistrez et actualisez la page pour afficher le résultat.

## Personnalisation d'une page de statut publique [ANCHOR_2]

Il existe plusieurs possibilités pour personnaliser l'apparence de votre page de statut publique.
Dans l'onglet [SHORTCODE_13] Personnalisation [SHORTCODE_14], vous pouvez modifier des paramètres tels que la couleur, le logo, le titre, les commentaires, l'ordre de tri, etc.

![Capture d'écran de l'onglet Personnalisation d'une page de statut publique]([LINK_URL_4])

### Utilisation de commentaires [ANCHOR_3]

Si vous souhaitez utiliser vos pages de statut publiques pour informer vos clients d'incidents en cours, vous pouvez ajouter un rapport ou un message dans les champs de commentaires.

Les champs **Titre du commentaire** et **Texte de commentaire** se trouvent dans l'onglet [SHORTCODE_15] Personnalisation [SHORTCODE_16].

Une fois que vous avez saisi le titre et le texte, ces derniers s'afficheront entre la barre de titre et le contenu de votre page de statut publique.

![]([LINK_URL_5])

[SHORTCODE_1]**Astuce :** Si vous souhaitez attirer l'attention sur ce message, ajoutez une émoticône avec un panneau d'avertissement, un point d'exclamation ou un signal d'alerte dans le champ de texte de commentaire.[SHORTCODE_2]

### Actualisation automatique de la page

Pour que la page s'actualise automatiquement, activez l'option **Actualisation automatique** dans l'onglet [SHORTCODE_17] Personnalisation [SHORTCODE_18] de votre page de statut publique. La page s'actualisera toutes les 30 secondes. L'actualisation automatique est désactivée par défaut.

### Modification du logo

Pour modifier le logo de votre page, vous devez tout d'abord ouvrir un [ticket de support]([LINK_URL_6]) où vous inclurez un fichier image PNG ou JPG de 210 x 40 pixels. Les images plus grandes seront redimensionnées. L'équipe Support ajoutera ce fichier à votre compte, pour que vous puissiez remplacer le logo d'Uptrends sur votre page.

### Définition d'un nom de moniteur alternatif [ANCHOR_4]

Les noms de moniteurs que vous utilisez dans votre entreprise peuvent manquer de sens pour les personnes extérieures à votre entreprise. Peut-être aussi ne souhaitez-vous tout simplement pas partager les noms de moniteurs utilisés en interne. Dans ces deux cas, vous pouvez utiliser un nom de moniteur alternatif. Celui-ci est défini à l'aide d'un champ personnalisé qui aura le même nom dans les paramètres de la page de statut publique et des moniteurs.

Définir un nom de moniteur alternatif :

1. Ouvrez [SHORTCODE_19] Configuration de compte > Pages de statut publiques [SHORTCODE_20].
2. Ouvrez la page de statut publique pour laquelle vous souhaitez définir un nom de moniteur alternatif.
3. Ouvrez l'onglet [SHORTCODE_21]Personnalisation[SHORTCODE_22] de la page de statut publique.
4. Saisissez un *nom de champ personnalisé*, par exemple [INLINE_CODE_2].
5. Cliquez sur le bouton [SHORTCODE_23]Enregistrer[SHORTCODE_24] en bas de l'écran.
6. Ouvrez le menu [SHORTCODE_25] Surveillance > Configuration du moniteur [SHORTCODE_26].
7. Cliquez sur l'onglet [SHORTCODE_27] Principal [SHORTCODE_28].
8. Dans la section **Métadonnées**, ajoutez un champ personnalisé contenant le même nom que celui utilisé dans la page de statut publique, par exemple [INLINE_CODE_3] et ajoutez une valeur. Cette valeur est le nom de moniteur alternatif qui s'affichera sur la page de statut publique.
9. Cliquez sur le bouton [SHORTCODE_29]Enregistrer[SHORTCODE_30].
10. Reproduisez les étapes 6 à 9 pour tous les moniteurs qui doivent présenter des noms alternatifs sur la page de statut publique.

Si vous souhaitez afficher des noms alternatifs dans plusieurs pages de statut publiques, reproduisez les étapes 1 à 5 pour chaque page. 
