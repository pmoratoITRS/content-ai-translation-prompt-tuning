{
"hero": {
"title": "Conditions d'erreur liées au temps de chargement ou de fonctionnement"
},
"title": "Conditions d'erreur liées au temps de chargement ou de fonctionnement",
"summary": "Cet article présente les limites applicables aux temps de chargement ou de fonctionnement, et leurs conséquences sur les alertes",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/configuration-limites-temps-chargement-alertes-avertissements",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/load-time-limit-settings-alerts-and-warnings"
}

Lorsque vous définissez des conditions d'erreur pour vos moniteurs, vous avez la possibilité de définir des limites de temps de chargement ou de fonctionnement. Vous pouvez définir deux limites pour les temps de chargement ou de fonctionnement : une limite inférieure qui correspond à un problème mineur et une limite supérieure qui correspond à un problème majeur.

La limite de temps de fonctionnement est utilisée pour les moniteurs de transactions et les moniteurs qui ne sont pas basées sur HTTP(S) ou sur un navigateur, comme les moniteurs DNS, Ping ou serveurs mails.

Le temps de chargement est utilisé pour les moniteurs HTTP(S), Webservice HTTP(S) et Full Page Check. Il correspond au temps écoulé entre le début de la requête initiale et la fin de la vérification.

{{< callout >}}
**Remarque** : Uptrends calcule le temps de chargement comme le temps écoulé entre le début de la requête initiale et la fin de la vérification. Ce temps est différent en fonction du type de moniteur. Le temps de chargement pour une vérification de base est très différent du temps de chargement d'un Real Browser Check pour la même URL. En savoir plus sur la [différence entre les vérifications de base et les Real Browser Checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="fr" >}}).
{{< /callout >}}

À la différence des autres [conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}}) qui génèrent toujours une erreur quand la condition est remplie, le temps de chargement de page peut générer une erreur ou simplement un avertissement au moyen d'un code couleur s'affichant dans le dashboard *Statut moniteurs*. Sachez toutefois que la fonction d'[alerte]({{< ref path="support/kb/alerting" lang="fr" >}}) nécessite que cette condition soit paramétrée de façon à générer une alerte.

## Ajout d'une vérification pour le temps de fonctionnement total

Suivez les étapes suivantes pour ajouter une vérification des temps de fonctionnement :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Cliquez sur le nom du moniteur pour le modifier.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Conditions d'erreur {{< /AppElement >}} et affichez la section **Vérifier le temps de fonctionnement total**.
   ![capture d'écran de la condition d'erreur pour les temps de fonctionnement](/img/content/scr_errorconditions-running-times.min.png)
4. Indiquez si vous souhaitez utiliser le code couleur (dans le dashboard *Statut moniteurs*) ou générer une erreur.
5. Indiquez les valeurs (en millisecondes) des limites de temps de fonctionnement inférieures (problème mineur) et supérieures (problème majeur).
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

Avec un moniteur de transaction, le temps de fonctionnement total correspond au temps nécessaire à la transaction dans son intégralité.

## Ajouter une vérification des temps de chargement

Suivez les étapes suivantes pour ajouter une vérification des temps de chargement :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Cliquez sur le nom du moniteur pour le modifier.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Conditions d'erreur {{< /AppElement >}} et affichez la section **Vérifier le temps de chargement de page**.
   ![Capture d'écran de la condition d'erreur liée au temps de chargement de page](/img/content/scr_errorconditions-load-times.min.png)
4. Indiquez si vous souhaitez utiliser le code couleur (dans le dashboard *Statut moniteurs*) ou générer une erreur.
5. Indiquez les valeurs (en millisecondes) des limites de temps de chargement inférieures (problème mineur) et supérieures (problème majeur).
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran.

## Code couleur uniquement

Si vous choisissez l'option *Code couleur uniquement* pour une limite ou les deux, le dashboard *Statut moniteurs* indiquera le dépassement de ces limites. Si la limite inférieure (qui correspond à un seuil mineur) est dépassée, la valeur s'affiche avec un fond jaune dans la colonne **Temps total**. Si la limite supérieure (qui correspond à un problème majeur) est dépassée, la valeur s'affiche avec un fond rouge. Pour ouvrir le dashboard *Statut moniteurs*, passez par le menu {{< AppElement type="menuitem" >}} Surveillance > Détails du statut {{< /AppElement >}}.

![Capture d'écran du dashboard Statut moniteurs avec les codes couleur](/img/content/scr_errorconditions-colorcode-loadtime.min.png)

Dans cet exemple du dashboard *Statut moniteurs*, vous remarquez que deux des moniteurs indiquent un temps total sur fond jaune et rouge. Malgré cela, l'indicateur d'erreur sur la gauche reste vert et donc inactif. C'est ce qui se produit lorsque vous choisissez l'option *Code couleur uniquement*.

## Générer une erreur {id="generate-error"}

Pour générer des alertes d'après les temps de chargement ou le temps de fonctionnement d'une page, vous devez utiliser I'option **Générer une erreur** dans la condition d'erreur. C'est seulement lorsque des erreurs sont générées que des alertes peuvent aussi l'être. L'article de la base de connaissances intitulé [Présentation des alertes]({{< ref path="support/kb/alerting/alerting-overview" lang="fr" >}}) explique en détail comment fonctionne la séquence des vérifications jusqu'aux alertes.

Avec l'option *Générer une erreur*, le code couleur correspondant aux temps de chargement ou de fonctionnement s'affiche tout de même dans le dashboard *Statut moniteurs*.
