{
  "hero": {
    "title": "Core Web Vitals"
  },
  "title": "Core Web Vitals",
  "summary": "Description des métriques Core Web Vitals figurant dans les graphiques en cascade des moniteurs Full Page Check et de transactions",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/resultats-surveillance/core-web-vitals",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Conformément à une initiative prise par Google pour simplifier l'optimisation des sites web, les **Core Web Vitals** sont un ensemble de métriques clés qui permettent de mesurer les performances des sites web. Ces métriques reflètent différents aspects de l'expérience utilisateur lors de la visite d'un site, comme la vitesse de chargement et la stabilité visuelle. De mauvais scores sur ces métriques peuvent affecter directement votre classement dans les moteurs de recherche. C'est pourquoi il est important de garder un œil sur ces chiffres clés pour vous assurer que votre page reste constamment optimisée.



Les moniteurs [Full Page Check (FPC)]([LINK_URL_1]) et les moniteurs de [transaction]([LINK_URL_2]) d'Uptrends peuvent vous fournir l'ensemble des Core Web Vitals (ainsi que des informations supplémentaires). Cet article vous présente les métriques fournies et ce qu'elles signifient.

## Métriques

Uptrends fournit les Core Web Vitals suivants (et les métriques correspondantes) :

![Core Web Vitals dans Uptrends]([LINK_URL_3])

- **First contentful paint (FCP) :** le FCP mesure le temps qu'il a fallu au navigateur pour afficher le premier contenu de la page.
- **Largest contentful paint (LCP) :** le LCP indique le moment où le plus grand élément unique (image ou bloc de texte) s'est affiché sur la page. Il marque dans la chronologie de chargement de la page le moment où le contenu principal (ou le plus grand) de la page a commencé à se charger. Le LCP et le FCP peuvent être identiques lorsque le plus grand élément de page est le premier qui se charge.
- **Time to interactive (TTI) :** le TTI indique le délai entre le début du chargement et le moment où la page peut répondre de manière fiable aux actions de l'utilisateur. C'est donc un bon indicateur du temps que l'utilisateur doit attendre pour que la page se charge. La mesure du TTI permet de calculer le temps de blocage total.
- **Total Blocking Time (TBT) :** le TBT mesure la durée pendant laquelle le thread principal du navigateur est bloqué. Il prend en compte le temps durant lequel le navigateur consacre plus de 50 millisecondes (ms) à traiter une tâche, ce qui entraîne un ralentissement de la page et bloque les interactions avec l'utilisateur. Pour chaque tâche longue, seule la partie du temps dépassant les 50 ms initiales est comptabilisée dans le TBT. Les tâches qui durent 50 ms ou moins ne sont pas incluses dans cette métrique.
- **Cumulative layout shift (CLS) :** le CLS est la dernière métrique mesurée après que la page a fini de se charger. Elle mesure les déplacements des éléments de la page (lorsque des éléments visibles se déplacent d'un endroit à l'autre) après que la page soit devenue interactive, et renseigne ainsi sur sa stabilité visuelle.
- **Interaction to next paint (INP) :** l'INP indique la réactivité globale d'une page aux interactions de l'utilisateur. Cet indicateur mesure le temps écoulé entre un clic ou une interaction clavier sur la page et le retour visuel associé. Comme il mesure les interactions après le chargement initial de la page, l'INP est *uniquement disponible pour les moniteurs de transactions*.

## Rapports de performance

Vous pouvez afficher toutes les métriques dans un dashboard personnalisé. Ajoutez simplement une tuile personnalisée du type [Liste ou graphique de données simple]([LINK_URL_4]). Cliquez ensuite sur le bouton des paramètres [SHORTCODE_1] [SHORTCODE_2] de la tuile et choisissez les valeurs que vous souhaitez afficher en cochant leurs cases.

Vous pouvez afficher les Core Web Vitals pour chaque étape des transactions. Pour chaque étape que vous souhaitez afficher dans le graphique, vous devez activer les options *Cascade* et *Métriques de performance*. Pour en savoir plus, consultez les informations relatives à la [configuration des étapes]([LINK_URL_5]).

![capture d'écran des paramètres de la tuile]([LINK_URL_6])

## Core Web Vitals dans les moniteurs de transactions

Les [graphiques en cascade]([LINK_URL_7]) des [moniteurs de transactions]([LINK_URL_8]) affichent les Core Web Vitals et les [durées de navigation du W3C]([LINK_URL_9]). Uptrends fournit les métriques pour chacune des actions de navigation d'une étape.

![capture d'écran montrant plusieurs actions de navigation dans une étape de transaction]([LINK_URL_10])