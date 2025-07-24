{
  "hero": {
    "title": "Notes des moniteurs"
  },
  "title": "Notes des moniteurs",
  "summary": "Ajouter des notes à un moniteur, les modifier et les utiliser pour faciliter la communication.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/notes-moniteurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans l'application Uptrends, les notes des moniteurs peuvent faciliter la communication entre les opérateurs. Il s'agit d'une méthode simple et directe pour échanger des informations sur les moniteurs et leur configuration. Le dashboard **Statut moniteurs** vous indique quels moniteurs sont accompagnés d'une note. Vous pouvez aussi y lire facilement les notes, sans devoir changer de fenêtre. Les opérateurs peuvent ainsi accéder rapidement aux informations internes laissées par un autre opérateur, par exemple concernant :

- le statut du moniteur ;
- les erreurs fréquentes et les instructions pour les résoudre ;
- le nom de la personne responsable, pour que les autres membres de l'équipe puissent se concentrer sur d'autres tâches.

Prenons l'exemple d'un moniteur _Certificat SSL_. Lorsque ce moniteur vous avertit de l'expiration prochaine de votre certificat, un opérateur intervient pour renouveler le certificat, et enregistre ses actions dans la note du moniteur. Une fois le certificat renouvelé, le texte dans le champ **Notes** peut être effacé.

## Comment ajouter des notes à un moniteur
Chaque écran de modification d'un moniteur contient un champ de texte libre intitulé **Notes**.
Pour accéder aux paramètres des moniteurs :
1. Ouvrez le menu [SHORTCODE_1] Moniteurs > Configuration du moniteur [SHORTCODE_2].
2. Cliquez sur [SHORTCODE_3] Configuration du moniteur [SHORTCODE_4].
3. Cherchez le nom du moniteur que vous souhaitez modifier. Cliquez sur le lien correspondant dans la colonne **Nom de moniteur**. Vous pouvez aussi filtrer les résultats en saisissant le début ou la totalité du nom, du type, du groupe ou de l'URL du moniteur dans le champ de recherche, puis en pressant la touche Entrée.
4. L'écran de configuration du moniteur s'ouvre avec l'onglet [SHORTCODE_5] Principal [SHORTCODE_6].
   ![Saisir une note dans le champ de texte libre]([LINK_URL_1])
5. Saisissez vos notes dans le champ **Notes** de la rubrique **Métadonnées**.
6. Si vous avez saisi des notes que vous souhaitez conserver, n'oubliez pas de cliquer sur le bouton [SHORTCODE_7] Enregistrer [SHORTCODE_8].

## Où les notes s'affichent-elles ?
Les notes s'affichent dans le dashboard **Statut moniteurs**. (Ouvrez le menu [SHORTCODE_9] Surveillance > Détails du statut [SHORTCODE_10]). La deuxième colonne du dashboard montre quels moniteurs sont assortis d'une note. Si une note existe, l'icône s'affiche en noir. S'il n'y a pas de note, l'icône est grisée. L'opérateur peut lire la note en survolant l'icône.

![Notes dans le dashboard Statut moniteurs]([LINK_URL_2])

Les notes sont aussi visibles dans le panneau d'information rapide du moniteur :

![Notes dans le panneau d'information rapide du dashboard statut moniteurs]([LINK_URL_3])
## Qui peut consulter les notes des moniteurs ?
Ouvrez le menu [SHORTCODE_11] Configuration de compte > Paramètres de compte [SHORTCODE_12]. La configuration des droits d'accès aux notes pour les opérateurs s'effectue dans l'onglet [SHORTCODE_13] Paramètres [SHORTCODE_14], dans la section Accès aux notes de moniteur.
![Accès aux notes de moniteur]([LINK_URL_4])
Remarque : Les paramètres d'accessibilité sont réservés aux comptes Enterprise.