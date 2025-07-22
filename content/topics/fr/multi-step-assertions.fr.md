{
  "hero": {
    "title": "Assertions pour la surveillance multi-étape "
},
"title": "Assertions pour la surveillance multi-étape",
"summary": "Comprendre les assertions dans la surveillance multi-étape.",
  "url": "/support/kb/synthetic-monitoring/surveillance-api/multi-step-assertions",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-assertions"
}

Dans [l'introduction à la surveillance multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}), nous avons expliqué que les assertions vous permettent de contrôler le contenu de vos réponses HTTP, ce qui garantie un comportement correct et le respect des performances de vos API. Cette section décrit en détail comment définir les assertions.

Chaque assertion est définie de la façon suivante :

{{< Code/Symbol type="source" >}}Source{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}propriété{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}comparaison{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}valeur cible{{< /Code/Symbol >}}

par exemple :

{{< Code/Symbol type="source" >}}Corps de résponse en JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products\[0\].Price{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is greater than{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}100{{< /Code/Symbol >}}

- La **source de l'assertion** : ce champ définit l'attribut de la réponse HTTP que vous souhaitez vérifier. [Chaque option disponible est décrite dans cet article]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}}).
- La **propriété de l'assertion** : certaines options de source d'assertion (en particulier la vérification du contenu et les options liées à l'en-tête) nécessitent une précision supplémentaire pour le contenu ou l'en-tête. Ceci est [expliqué plus en détail]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}}) pour chaque type de source concerné.
- La **comparaison de l'assertion** : ce champ exprime le type de vérification que nous devons effectuer. Par défaut, nous ferons une comparaison du type *X égale Y*, mais il existe de nombreuses autres options de comparaison pour le texte et les nombres. [Voir la liste des options de comparaison]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-comparison-operations" lang="fr" >}}).
- La **valeur cible de l'assertion** : pour la plupart des assertions, la comparaison se fera par rapport à une certaine valeur que vous spécifiez. Il s'agit de la valeur cible. En fonction de la source d'assertion et le type de comparaison que vous effectuez, cette valeur peut être une valeur textuelle, une valeur numérique ou même une valeur booléenne (vrai ou faux). Vous pouvez également saisir [une référence à une variable]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}) qui représente l'une de ces valeurs.

## Que se passe-t-il si une condition d'assertion n'est pas remplie ?

Toutes les assertions d'une étape sont exécutées dès que la requête HTTP a été exécutée et que la réponse a été traitée. En règle générale, toutes les assertions pour l'étape sont évaluées, même si une des assertions ne passe pas. Cela signifie qu'il est possible que plusieurs assertions puissent signaler un échec pour une étape.

Si une ou plusieurs assertions échouent, l'exécution du moniteur s'arrête à la fin de l'étape en cours. Les étapes suivantes ne seront pas exécutées et la vérification du moniteur signalera une erreur. Le code d'erreur et la description dépendent du type d'échec. Si plusieurs assertions échouent, le premier qui échoue est considéré comme le plus important.

Parfois, il peut être nécessaire de relancer l'exécution d'une assertion, par exemple parce que vous savez qu'il pourrait y avoir un problème de timing conduisant à un résultat faussement négatif. Évaluer l'assertion à plusieurs reprises est possible ; les détails sont expliqués dans [Réessayer jusqu'à la réussite]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step#msaretry" lang="fr" >}}).
