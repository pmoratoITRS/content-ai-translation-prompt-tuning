{
"hero": {
"title": "Détermination du sélecteur par l'enregistreur de transactions"
},
"title": "Détermination du sélecteur par l'enregistreur de transactions",
"summary": "Lorsque vous utilisez l'enregistreur de transactions, se pose le problème de décider comment identifier les éléments individuels sur la page en fonction de plusieurs facteurs. ",
"url": "/support/kb/surveillance-synthetique/transactions/enregistreur-de-transactions-comment-determiner-le-selecteur",
"translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-recorder-selector-determination"
}

Pour vos étapes de transactions en libre-service, lorsque vous utilisez l'enregistreur de transactions, celui-ci renvoie une longue liste de sélecteurs possibles utilisés par Uptrends pour identifier un élément de page. Chaque étape ou action n'utilisera qu'un seul de ces sélecteurs dans votre script. Uptrends utilise alors un algorithme pour déterminer le meilleur sélecteur.

## Sélecteurs

Pendant l'enregistrement de votre transaction à l'aide de l'enregistreur de transactions, pendant que vous interagissez avec les différents éléments de la page, l'enregistreur génère une liste de sélecteurs possibles pour identifier chaque élément. La liste des sélecteurs possibles contient divers types, comme texte, ID, CSS et XPath. Pour chaque élément, l'enregistreur de transactions génère une liste des sélecteurs possibles. L'enregistreur lui-même ne contient pas de logique permettant de choisir un sélecteur plutôt qu'un autre, cette décision est prise au niveau des serveurs Uptrends au cours du processus de conversion.

Pour choisir le meilleur sélecteur, Uptrends examine la valeur des sélecteurs et choisit une valeur et un type qui ne soit pas trop vague, ni trop compliqué et qui n'apparaît pas trop souvent sur la page.

{{< callout >}}
**Remarque** : Vous pouvez afficher les autres sélecteurs en cliquant sur les points de suspension {{< AppElement type="button" >}}...{{< /AppElement >}} dans le champ de valeur du sélecteur.
{{< /callout >}}

## Processus de sélection

Le processus de sélection passe par les étapes suivantes :

1. **Normalisation** : Le processus de normalisation élimine tous les sélecteurs qui ont la même valeur et font référence aux mêmes attributs.
2. **La suppression des localisateurs inconnus**  : Le processus supprime tous les sélecteurs que les transactions en libre-service ne prennent pas en charge (sélecteurs de texte).
3. **Priorisation des types** : Le processus donne la priorité aux sélecteurs basés sur le type (par ordre de priorité) : text, ID, name, CSS, XPath (texte), XPath (attributs), XPath (index), XPath (node).
4. **Priorité aux sélecteurs les plus courts** : Uptrends priorise le sélecteur en fonction du nombre de caractères dans la chaîne en donnant la priorité au sélecteur le plus court.
5. **Priorité aux sélecteurs avec le moins de correspondances** : Chaque sélecteur peut correspondre à plusieurs éléments sur la page qui ont la même description, donc ce processus donne la priorité aux sélecteurs qui en ont le moins.
6. **Priorisation des sélecteurs à correspondance unique** : Uptrends donne la priorité la plus élevée aux sélecteurs qui ne correspondent qu'à un seul élément de la page.
7. **Sélection finale** : La liste contient les sélecteurs en ordre de priorité, et Uptrends choisit le premier sélecteur dans la liste pour l'action.
