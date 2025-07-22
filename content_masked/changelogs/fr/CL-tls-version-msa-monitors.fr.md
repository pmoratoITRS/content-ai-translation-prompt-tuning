{
  "title": "Nouvelle option de sélection des versions TLS dans les moniteurs d'API multi-étapes",
  "date": "2024-11-06",
  "url": "[URL_BASE_CHANGELOG]novembre-2024-nouvelle-option-selection-versions-tls-moniteurs-api-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Nous avons ajouté une option à cocher *Version(s) TLS* dans l’éditeur visuel du moniteur d’API multi-étapes.

En cochant la case *Autoriser uniquement certaines versions de TLS*, vous pouvez désormais préciser les versions TLS à appliquer lors de la négociation TLS pour la connexion HTTPS dans les moniteurs d’API multi-étapes. Vous pouvez aussi décocher la case si aucune restriction n’est nécessaire.

Tous les [checkpoints d’Uptrends]([LINK_URL_1]) prennent en charge les protocoles TLS 1.1 et TLS 1.2. Si vous cochez l’option TLS 1.3, cela limite votre sélection aux checkpoints prenant en charge le protocole TLS 1.3. Ce choix est déconseillé tant que le protocole TLS 1.1 est pris en charge.

![Case à cocher Version(s) TLS dans les moniteurs d’API multi-étapes]([LINK_URL_2])