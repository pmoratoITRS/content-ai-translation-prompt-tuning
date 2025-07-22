{
"hero": {
"title": "Opérateurs de comparaison pour la surveillance multi-étapes"
},
"title": "Opérateurs de comparaison pour la surveillance multi-étapes",
"summary": "Découvrez les opérateurs de comparaison disponibles pour la configuration d'un moniteur multi-étapes.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/operations-comparaison-multi-etapes",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-comparison-operations",
"TableOfContents": false
}

Lorsque vous créez une assertion pour l’une des étapes de [configuration d'un moniteur multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}), vous devez définir quel type d’opération de vérification doit être effectué. Vous avez le choix entre les options décrites ci-dessous. Dans la description de chaque option, la *source* fait référence à la valeur de l’attribut de réponse HTTP que vous souhaitez inspecter. La *valeur cible* est la valeur fixe utilisée pour la comparaison.

- **Est égal à** : la source doit être égale à la valeur cible. Notez que la comparaison ne tient pas compte de la casse.

- **N'est pas égal à** : la source ne doit PAS être égale à la valeur cible. Notez que la comparaison ne tient pas compte de la casse.

- **Contient** : la source doit contenir la valeur cible. Les valeurs source et cible sont interprétées comme du texte (même si elles contiennent seulement une valeur numérique), et la valeur cible doit apparaître quelque part dans le texte de la valeur source.

- **Ne contient pas** : la source ne doit PAS contenir la valeur cible.

- **Est inférieur à** : la valeur source et la valeur cible doivent toutes deux être des nombres, et la condition “source < cible” doit être vraie.

- **Est inférieur ou égal à** : la source et la valeur cible doivent toutes deux être des nombres, et la condition “source <= cible” doit être vraie.

- **Est supérieur à** : la valeur source et la valeur cible doivent toutes deux être des nombres, et la condition “source > cible” doit être vraie.

- **Est supérieur ou égal à** : la valeur source et la valeur cible doivent toutes deux être des nombres, et la condition “source >= cible” doit être vraie.

- **Est vide** : la source doit être vide (par exemple, `"source": ""`).

- **N'est pas vide** : la source doit contenir des caractères alphabétiques ou numériques.

- **Est nul** : la source doit contenir la valeur `null` (par exemple, `"source": null`).

- **N'est pas nul** : la source ne doit PAS contenir la valeur `null`.

- **Existe** : la source doit exister dans la réponse.

- **N'existe pas** : la source ne doit PAS exister dans la réponse.

- **Doit être ignoré** : cette option indique qu’aucune vérification automatique ne doit être effectuée sur la valeur source. Elle peut être utilisée pour annuler les assertions automatiques sur les champs Code de statut et Réponse complétée. (voir [Types et propriétés des sources]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}})))
