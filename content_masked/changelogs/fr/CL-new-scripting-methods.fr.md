{
  "title": "Ajout de nouvelles méthodes de script dans les moniteurs API multi-étapes",
  "date": "2025-03-12",
  "url": "[URL_BASE_CHANGELOG]mars-2025-nouvelles-methodes-script",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les méthodes de script suivantes peuvent désormais être utilisées dans les onglets des [scripts de pré-requête et de post-réponse]([LINK_URL_1]) des moniteurs d'API multi-étapes :

- [INLINE_CODE_1] : analyse une liste de révocation de certificats et fournit ses métadonnées.
- [INLINE_CODE_2] : génère un hash MD5 de la valeur précisée.
- [INLINE_CODE_3] : génère un hash SHA-1 de la valeur précisée.
- [INLINE_CODE_4] : génère un hash SHA-256 de la valeur précisée.
- [INLINE_CODE_5] : génère un hash SHA-512 de la valeur précisée.
- [INLINE_CODE_6] : fournit un tableau d'octets contenant le corps de la requête. Les réponses ne peuvent excéder 100 Mo.

Notez que la méthode [INLINE_CODE_7] est uniquement disponible dans l'onglet [SHORTCODE_1] Post-response [SHORTCODE_2] de votre moniteur multi-étapes. Les méthodes de script permettant de générer des hash MD5 et SHA vous permettent de stocker et d'envoyer des valeurs de façon sécurisée, en garantissant la protection des données au moyen du hachage.