{
  "hero": {
    "title": "Points de contrôle non-principaux"
  },
  "title": "Points de contrôle non-principaux",
  "summary": "Découvrez pourquoi Uptrends désigne certains points de contrôle comme non principaux et ce que vous devez savoir avant d’envisager de les utiliser.",
  "url": "/support/kb/surveillance-synthetique/points-de-controle/points-de-controle-non-principaux",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/non-primary-checkpoints"
}

Vous avez peut-être remarqué, lors de la sélection de vos points de contrôle, que nous avons désigné certains points de contrôle *comme non principaux*. Les points de contrôle non principaux sont des points de contrôle ayant à une disponibilité intermittente et éventuellement une bande passante réduite en raison de l'infrastructure Internet locale ou du contrôle gouvernemental.

Par défaut, nous avons choisi d'exclure les points de contrôle non principaux lorsque vous sélectionnez une région qui en contient (voir ci-dessous), mais cela ne signifie pas que vous ne pouvez pas les utiliser. Nous les avons exclus pour que vous sachiez que ces points de contrôle sont soumis à des conditions instables et qu'ils peuvent affecter de manière négative votre temps de disponibilité et vos rapports de performance lorsque vous choisissez de les utiliser. Pour les utiliser, décochez la case **Utiliser uniquement les points de contrôle principaux**.

![](/img/content/0dd34957-9d71-4d9d-b31a-2aba574935e9.png)

## Je teste uniquement dans des zones qui ont des points de contrôle non principaux, mais je vois des tests d'autres points de contrôle. Pourquoi ?

Bien qu'il soit important de tester depuis l'emplacement de votre utilisateur, si cet emplacement devient indisponible pour le test, vous voudriez tout de même connaître le statut de votre site web ou de votre service. Au lieu de laisser votre site ou votre service sans aucun test lors de périodes de connectivité limitée ou inexistante avec des points de contrôle non principaux, Uptrends utilisera d’autres points de contrôle à des fins de test afin que vous puissiez détecter les pannes et les problèmes de performances susceptibles de se produire entre-temps.
