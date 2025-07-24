{
  "hero": {
    "title": "Conditions d'erreur liées au contenu de la console"
  },
  "title": "Conditions d'erreur liées au contenu de la console",
  "summary": "Vous pouvez baser les vérifications du moniteur et les erreurs sur le contenu du journal de la console de votre navigateur.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-contenu-console",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Chaque moniteur réalise des vérifications standard qui lui sont spécifiques.
 Si vous le souhaitez, vous pouvez aussi utiliser les conditions d'erreur du moniteur pour définir des vérifications personnalisées qui vous permettront de générer des alertes dans certaines situations. L'article de la base de connaissances intitulé [Conditions d'erreur]([LINK_URL_1]) vous expliquent à quoi servent les conditions d'erreur et comment les utiliser.

Cet article explique le fonctionnement des conditions d'erreur de la catégorie *Contenu de la console*. Dans la configuration du moniteur, ces conditions d'erreur sont disponibles dans l'onglet [SHORTCODE_1] Conditions d'erreur [SHORTCODE_2] de la section *Vérifier le contenu de la console*. Remarque : Toutes les conditions d'erreur ne sont pas disponibles avec tous les moniteurs. Consultez le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]([LINK_URL_2]) pour connaître les options associées à chaque type de moniteur.

## Journal de la console du navigateur

Lorsque vous chargez une page web dans un navigateur, le journal de la console du navigateur enregistre tous les messages de la console. Vous pouvez consulter ces messages. Par exemple, dans Chrome, il faut presser la touche "F12" pour ouvrir les outils DevTools, puis ouvrir l'onglet *Console*. Le journal enregistre des messages d'information, d'avertissement ou d'erreur (p. ex. échec de chargement d'un élément, erreur JavaScript, etc.). Les messages de journal peuvent être utilisés par l'équipe de développement web.

Vos conditions d'erreur peuvent être basées sur la présence de messages enregistrés dans le journal de console, et facultativement de leur contenu. Grâce à ces conditions d'erreur, vous pouvez vérifier si une entrée du journal de type information, avertissement ou erreur est présente, et si elle contient ou non un texte donné. Une erreur est générée si la condition d'erreur est remplie.

Veuillez noter que cette condition d'erreur est différente de la condition d'erreur basée sur le [contenu de la page]([LINK_URL_3]), qui permet de contrôler le contenu de la page elle-même.

## Présence d'un message dans le journal de la console [ANCHOR_1]

Vous pouvez vérifier si le journal de la console contient un message. Si vous le souhaitez, vous pouvez aussi vérifier si ce message contient un contenu donné.

Pour définir cette condition d'erreur :

1. Ouvrez le menu [SHORTCODE_3] Surveillance > Configuration du moniteur [SHORTCODE_4].
2. Cliquez sur le nom du moniteur pour le modifier.
3. Ouvrez l'onglet [SHORTCODE_5] Conditions d'erreur [SHORTCODE_6].
4. Dans la section *Vérifier le contenu de la console*, cliquez sur le bouton [SHORTCODE_7] \+ Nouvelle vérification [SHORTCODE_8] pour ajouter une nouvelle vérification.

   ![capture d'écran de la section vérifier le contenu de la console]([LINK_URL_4])

5. Sélectionnez l'option **Erreur lorsque la console contient certains contenus**.
6. Choisissez le niveau du message (information, avertissement ou erreur).
7. Le champ **Texte du message** fonctionne de la façon suivante : si vous le laissez vide, le moniteur vérifie uniquement si le journal contient un message du niveau que vous avez indiqué, quel que soit son contenu. Si vous souhaitez vérifier la présence d'un contenu donné dans les messages du journal, vous devez saisir le texte recherché dans le champ **Texte du message**. Il peut s'agir d'un mot, d'une suite de mots ou d'une expression régulière.
8. Vous pouvez ajouter d'autres vérifications si vous le souhaitez.
9. Cliquez sur le bouton [SHORTCODE_9] Enregistrer [SHORTCODE_10] en bas de l'écran.

## Absence d'un message dans le journal de la console

Plutôt que de vérifier la présence d'un message (voire d'un contenu de message) dans le journal de la console, vous pouvez aussi vous assurer de l'absence d'un message dans le journal de la console. À nouveau, votre recherche peut porter sur un contenu spécifique.

Suivez les étapes décrites dans la section [Présence d'un message dans le journal de la console]([LINK_URL_5]) ci-dessus, mais sélectionnez l'option **Erreur lorsque la console ne contient pas certains contenus**.

Choisissez ensuite le niveau de message (information, avertissement ou erreur) à vérifier. Si vous laissez vide le champ **Texte du message**, une erreur sera générée si le journal ne contient aucun message de ce type. Si vous remplissez le champ **Texte du message**, une erreur sera générée si le journal ne contient aucun message de ce type avec le texte indiqué.

## Résultats de la vérification du contenu de la console

Le moniteur effectue la vérification en tenant compte du paramétrage de cette condition d'erreur. Les résultats sont accessibles dans la fenêtre [Voir les détails]([LINK_URL_6]). Si la vérification donne lieu à une erreur au lieu d'un résultat "OK", cette fenêtre vous aide à comprendre quelle condition d'erreur a causé une erreur et comment aborder le dépannage.

