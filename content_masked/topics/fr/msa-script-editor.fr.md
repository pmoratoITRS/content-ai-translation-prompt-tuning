{
  "hero": {
    "title": "Éditeur de script pour les API multi-étapes"
  },
  "title": "Éditeur de script pour les API multi-étapes",
  "summary": "Une présentation de l'éditeur de script pour les API multi-étapes",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/editeur-de-script-msa",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Comme pour les [moniteurs de transactions]([LINK_URL_1]), le type de moniteur d'API multi-étapes est livré avec un éditeur de script comme alternative à l'éditeur visuel par défaut. L'éditeur de script vous permet d'apporter des modifications aux étapes de votre moniteur, un peu comme l'éditeur visuel, mais dans un script JSON au lieu de l'interface utilisateur.

## Avantages de l'éditeur de script

Il y a plusieurs avantages à utiliser un éditeur de script plutôt que d'apporter des modifications au moniteur via l'interface utilisateur :

- Les utilisateurs expérimentés pourraient préférer effectuer des modifications directement dans un script plutôt que de naviguer dans une interface utilisateur. Certains utilisateurs préfèrent une expérience similaire à l'utilisation d'une ligne de commande.
- Un script permet l'automatisation, par exemple pour s'adapter à votre [processus CI/CD]([LINK_URL_2]). En utilisant l'[API d'Uptrends]([LINK_URL_3]), vous allez pouvoir mettre à jour les étapes du moniteur en même temps que vous mettez à jour l'API qu'il vérifie.
- L'éditeur de script vous permet de faire une copie locale des étapes de votre moniteur, en copiant simplement le script et en le collant dans un fichier local. La conservation d'une copie locale permet le contrôle des versions, les sauvegardes de vos moniteurs API multi-étapes et la réplication facile des configurations complexes.

## Passer à l'éditeur de script

Vous pouvez passer à l'éditeur de script pour n'importe quel moniteur API multi-étapes en cliquant sur le bouton [SHORTCODE_1] BASCULER VERS LE SCRIPT [SHORTCODE_2] en haut à droite de l'onglet [SHORTCODE_3] Étapes [SHORTCODE_4] dans les paramètres du moniteur. Basculer vers et depuis l'éditeur de script déclenchera la validation, assurez-vous donc que le code JSON dans le script reste valide. Le script ressemblera à ceci :

![L'éditeur de scripts]([LINK_URL_4])

## Comprendre le script

Comme vous pouvez le constater, le script est essentiellement un ensemble d'étapes individuelles au format JSON, contenant pour chacun la méthode de requête, l'URL, l'en-tête et le corps de la requête que vous avez configurés, ainsi que les options d'authentification. De plus, chaque étape contient les définitions des variables créées  à partir de la réponse ou des assertions à faire. Toute modification nécessaire peut être apportée directement dans l'éditeur de script.

Une étape individuelle ressemblera à peu près à ceci :

[CODE_BLOCK_1]

Ajouter une étape supplémentaire est très simple, il suffit d'ajouter le bloc de texte d'une étape, en utilisant la définition d'étape complète comme indiqué ci-dessus.

Après les blocs des étapes, le script liste également des informations sur les [variables prédéfinies]([LINK_URL_5]) ou les [fonctions définies par l'utilisateur]([LINK_URL_6]) que vous avez configurés :

[CODE_BLOCK_2]
