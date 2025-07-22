{
  "hero": {
    "title": "Cryptage et sécurité de votre site"
  },
  "title": "Cryptage et sécurité de votre site",
  "summary": "Uptrends utilise les normes de cryptage avancées pour protéger les noms d'utilisateur et les mots de passe de votre site.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/cryptage-et-securite-de-votre-site",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends accorde une attention centrale à la sécurité de votre site. Les noms d'utilisateur et les mots de passe que vous fournissez sont traités avec soin. Nous chiffrons les données sensibles immédiatement, puis nous les stockons dans notre base de données et nous exerçons un contrôle très strict sur l'accès à ces données au sein de notre organisation.

## Comment nous protégeons vos données

Notre système utilise l'algorithme [Rijndael]([LINK_URL_1]), qui applique la norme **Advanced Encryption Standard** (AES - standard de chiffrement avancé) pour crypter les données sensibles. Pour ce faire, nous utilisons [PBKDF2]([LINK_URL_2]) (suivant RFC 2898) pour générer la clé de cryptage nécessaire au chiffrement. Nous utilisons des valeurs aléatoires sécurisées sur 256 bits pour le salage et le vecteur d'initialisation (IV) dont nous avons besoin pour générer la clé de cryptage et effectuer le chiffrement. Enfin, toutes les communications entre les sous-systèmes d'Uptrends se font via des connexions cryptées et authentifiées.

## Ce que vous pouvez faire

En plus du cryptage et des politiques d'accès que nous gérons de notre côté, nous encourageons également nos clients à prendre des mesures de sécurité de leur côté.

### Limiter les droits d'accès

Limitez les droits d'accès que vous nous fournissez à travers les informations de connexion. Idéalement, les comptes de connexion configurés pour les moniteurs de transactions et les autres types de moniteurs doivent avoir des droits d'accès minimaux. Donnez à ces comptes juste assez de privilèges pour effectuer les vérifications nécessaires.

### Utiliser des comptes de connexion distincts

Nous vous conseillons également de créer des comptes de connexion distincts dans votre système, qui auront comme seul but d'effectuer des tâches de surveillance. Il peut être judicieux de mettre ces comptes sur liste blanche en fonction des emplacements géographiques ([adresses IP]([LINK_URL_3]), c'est-à-dire les adresses des serveurs de checkpoints d'Uptrends) que vous autorisez à utiliser ces identifiants.

### Surveiller le comportement des comptes

Si vos systèmes utilisent la journalisation pour suivre le comportement de chaque compte connecté, il est de bonne pratique de surveiller ce comportement. Cette surveillance vous permet d'empêcher tout fonctionnement anormal.

### Mettre à jour les mots de passe

Enfin, pensez à mettre à jour les mots de passe dans vos scripts de configuration et de suivi des transactions (comme indiqué dans l'article consacré aux [valeurs dans les transactions])([SHORTCODE_1])) si votre politique de sécurité force leur expiration sur votre serveur. La mise à jour de vos mots de passe empêche vos moniteurs de signaler des erreurs inutiles.

## Notre collaboration autour de votre sécurité

Grâce à notre engagement continu en matière de sécurité et à votre application active de ces mesures de sécurité, notre collaboration sera des plus efficaces et réduira les vulnérabilités au minimum.
