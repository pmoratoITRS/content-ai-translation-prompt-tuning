{
"hero": {
"title": "Conditions d'erreur liées aux ressources"
},
"title": "Conditions d'erreur liées aux ressources",
"summary": "Présentation des conditions d'erreur disponibles dans la catégorie *Ressources*. Les ressources sont les éléments qui doivent être chargés pour que votre page web soit visible et fonctionnelle.",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-ressources",
"tableofcontents": true,
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-resources"
}

Chaque moniteur réalise des vérifications standard qui lui sont spécifiques.
 Si vous le souhaitez, vous pouvez aussi utiliser les conditions d'erreur du moniteur pour définir des vérifications personnalisées qui vous permettront de générer des alertes dans certaines situations. L'article de la base de connaissances intitulé [Conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}}) vous expliquent à quoi servent les conditions d'erreur et comment les utiliser.

Cet article-ci vous décrit le fonctionnement des conditions d'erreur liées aux *ressources*. Dans la configuration du moniteur, ces conditions d'erreur sont disponibles dans l'onglet {{< AppElement type="tab" >}} Conditions d'erreur {{< /AppElement >}} de la section *Vérifier les ressources*. Remarque : Toutes les conditions d'erreur ne sont pas disponibles avec tous les moniteurs. Consultez le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="fr" >}}) pour connaître les options associées à chaque type de moniteur.

## Qu'est-ce qu'une vérification de ressource ?

Votre site web repose sur plusieurs ressources (images, feuilles de style, scripts, etc.) qui doivent être chargées. Ces ressources sont donc les éléments chargeables de votre site web. La vérification effectuée par le moniteur renvoie des informations sur la taille (en kilooctets) de la réponse du serveur. La taille de la page (de même que la correspondance de contenu) peut vous indiquer si la page s'est chargée complètement ou non.

Les valeurs de taille inattendues (qu'elles soient faibles ou élevées) peuvent aussi vous indiquer une utilisation frauduleuse de la page. Les moniteurs Full Page Check et les moniteurs de transactions créent un [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) qui représente le processus de chargement des éléments. Le graphique présente les métriques et certaines informations tirées de la vérification du monitoring.

Les conditions d'erreur disponibles dans la section **Vérifier les ressources** vous permettent de définir une limite quant à la taille totale ou au pourcentage des ressources individuelles dont le chargement peut échouer sans donner lieu à une erreur.

## Vérification de la taille du contenu (avec les moniteurs HTTP(S) et Webservice HTTP(S))

Pour les moniteurs HTTP(S) ou Webservice HTTP(S), vous pouvez définir une condition d'erreur qui vérifie la taille minimum du contenu.

![capture d'écran de la vérification de ressources avec les moniteurs HTTPS(S) ou Webservice](/img/content/scr_errorconditions-resources-https.min.png)

## Vérification de la somme de toutes les ressources (avec le moniteur Full Page Check)

Vous pouvez définir une taille maximum et minimum (en ko) acceptable dans la réponse du serveur. Choisissez l'option ** Vérifier la somme de toutes les ressources** dans la section *Vérifier les ressources*.

![capture d'écran de la condition d'erreur somme de toutes les ressources](/img/content/scr_errorconditions-resources-all.min.png)

Définissez une taille minimum en sélectionnant *L'ensemble des ressources a une taille supérieure à*, puis en remplissant la limite inférieure (en ko). Si la taille de tous les éléments de la page est inférieure à ce nombre, cela peut indiquer que votre page manque de contenu et ne fonctionne pas correctement.

Définissez une taille maximum en sélectionnant *L'ensemble des ressources a une taille inférieure à*, puis en remplissant la limite supérieure (en ko). Si la taille de tous les éléments de la page est supérieure à ce nombre, cela indique une quantité excessive de contenu. Cela peut indiquer une erreur au niveau du contenu, ou que du contenu a été ajouté à votre site web sans que vous le sachiez.

Vous pouvez combiner des conditions d'erreur minimum et maximum. Ajoutez une nouvelle condition d'erreur en cliquant sur le bouton {{< AppElement type="buttonSecondary" >}} Nouvelle vérification {{< /AppElement >}}.

## Vérification de chaque ressource (avec le moniteur Full Page Check)

En plus de vérifier la somme de toutes les ressources, vous pouvez aussi vérifier les éléments de façon individuelle. Choisissez l'option **Vérifiez chaque ressource individuellement**, puis précisez si la vérification doit évaluer si un pourcentage de ressources échoue à charger ou s'il dépasse une limite maximale.

Notez que le descriptif de la vérification est dynamique et qu'il reflète les options et les limites définies.

Pour vérifier si un pourcentage de ressources échoue à charger, choisissez l'option **Vérifier que les ressources ne se chargent pas** et indiquer le pourcentage (limite supérieure) de ressources dont le chargement peut échouer. Une erreur est alors générée lorsque le seuil est dépassé.

![capture d'écran de la condition d'erreur échec de chargement de la ressource](/img/content/scr_errorconditions-resources-individual-fail.min.png)

Pour vérifier si une partie (un pourcentage) ou la totalité de toutes les ressources dépasse une certaine taille, choisissez l'option **La taille de la ressource est supérieure à** et indiquez le pourcentage, le cas échéant. Si le pourcentage est réglé à 0 %, le système vérifiera si une ressource dépasse la limite. Si le pourcentage est réglé à 100 %, le système vérifiera si toutes les ressources dépassent ensemble la limite.

![capture d'écran de la condition d'erreur limite atteinte par les ressources](/img/content/scr_errorconditions-resources-individual-percentage.min.png)

