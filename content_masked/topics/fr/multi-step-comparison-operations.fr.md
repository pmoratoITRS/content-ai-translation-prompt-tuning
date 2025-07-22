{
  "hero": {
    "title": "Opérateurs de comparaison pour la surveillance multi-étapes"
  },
  "title": "Opérateurs de comparaison pour la surveillance multi-étapes",
  "summary": "Découvrez les opérateurs de comparaison disponibles pour la configuration d'un moniteur multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/operations-comparaison-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

Lorsque vous créez une assertion pour l’une des étapes de [configuration d'un moniteur multi-étapes]([LINK_URL_1]), vous devez définir quel type d’opération de vérification doit être effectué. Vous avez le choix entre les options décrites ci-dessous. Dans la description de chaque option, la *source* fait référence à la valeur de l’attribut de réponse HTTP que vous souhaitez inspecter. La *valeur cible* est la valeur fixe utilisée pour la comparaison.

- **Est égal à** : la source doit être égale à la valeur cible. Notez que la comparaison ne tient pas compte de la casse.

- **N'est pas égal à** : la source ne doit PAS être égale à la valeur cible. Notez que la comparaison ne tient pas compte de la casse.

- **Contient** : la source doit contenir la valeur cible. Les valeurs source et cible sont interprétées comme du texte (même si elles contiennent seulement une valeur numérique), et la valeur cible doit apparaître quelque part dans le texte de la valeur source.

- **Ne contient pas** : la source ne doit PAS contenir la valeur cible.

- **Est inférieur à** : la valeur source et la valeur cible doivent toutes deux être des nombres, et la condition “source [HTML_TAG_1] cible” doit être vraie.

- **Est supérieur ou égal à** : la valeur source et la valeur cible doivent toutes deux être des nombres, et la condition “source >= cible” doit être vraie.

- **Est vide** : la source doit être vide (par exemple, [INLINE_CODE_1]).

- **N'est pas vide** : la source doit contenir des caractères alphabétiques ou numériques.

- **Est nul** : la source doit contenir la valeur [INLINE_CODE_2] (par exemple, [INLINE_CODE_3]).

- **N'est pas nul** : la source ne doit PAS contenir la valeur [INLINE_CODE_4].

- **Existe** : la source doit exister dans la réponse.

- **N'existe pas** : la source ne doit PAS exister dans la réponse.

- **Doit être ignoré** : cette option indique qu’aucune vérification automatique ne doit être effectuée sur la valeur source. Elle peut être utilisée pour annuler les assertions automatiques sur les champs Code de statut et Réponse complétée. (voir [Types et propriétés des sources]([LINK_URL_2])))
