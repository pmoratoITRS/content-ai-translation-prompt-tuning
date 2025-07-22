{
  "hero": {
    "title": "Format des messages"
  },
  "title": "Format des messages",
  "summary": "Intégration personnalisée : comment formater correctement votre message",
  "url": "[URL_BASE_TOPICS]alerter/integrations/integrations-personnalisees/format-des-messages",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans la mesure où les messages d'alerte sortants sont le plus souvent formatés en JSON, nous devons respecter ces règles de formatage. Pour ce faire, certains caractères (tels que les sauts de ligne ou les guillemets) doivent être encodés avant de pouvoir être insérés dans le message d'alerte sortant au format JSON. Autrement, ils invalideront la structure JSON du message sortant, ce qui pourrait amener l'endpoint de réception à générer une erreur et à ne pas gérer correctement l'alerte entrante. Cet article passe en revue les fonctions intégrées de formatage automatique des messages.

## Appliquer le formatage automatique [ANCHOR_1]

Par exemple, si un champ "Notes" du moniteur (que vous pouvez ajouter au message d'alerte à l'aide de la variable système @monitor.notes) contient ce type de caractères (tels que des sauts de ligne ou des guillemets), cela brisera la structure JSON du message sortant.

Par exemple :  
[INLINE_CODE_1]  

Deviendrait :
[CODE_BLOCK_1]

La rupture de la structure JSON risque d'entraîner une gestion incorrecte de l'alerte du côté récepteur. Pour résoudre ce problème, il est possible d'encoder (ou de décoder) des bouts de texte pour que le format du message JSON ou XML soit respecté. Lors de l'utilisation de cette fonction, tous les caractères qui doivent être évités pour préserver la validité du format JSON seront automatiquement encodés.

Pour utiliser cette fonction, encapsulez la variable système ou le texte souhaité avec la syntaxe suivante :  
[INLINE_CODE_2]

Par exemple, la variable système monitor.notes précédemment mentionnée doit être encapsulée comme suit :  
[INLINE_CODE_3]

Avec la fonction [INLINE_CODE_4], le texte JSON mentionné précédemment et contenant la référence aux notes du moniteur est maintenant résolu comme suit :  
[INLINE_CODE_5]

Comme vous pouvez le voir, les notes du moniteur sont désormais encodées de manière à ne pas casser la structure JSON.

Si vous utilisez XML au lieu de JSON, ne vous inquiétez pas : nous avons une fonction similaire pour l'encodage XML. Vous pouvez utiliser cette fonction pour encapsuler les variables système de votre choix avec [INLINE_CODE_6].
