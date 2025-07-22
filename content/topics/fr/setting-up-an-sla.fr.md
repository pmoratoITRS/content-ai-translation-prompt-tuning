{
"hero": {
"title": "Mettre en place un SLA"
},
"title": "Mettre en place un SLA",
"summary": "Surveillez la conformité de vos accords de niveau de service (SLA) avec Uptrends.",
"url": "/support/kb/dashboards-et-rapports/sla/mettre-en-place-un-sla",
"translationKey": "https://www.uptrends.com/support/kb/sla/setting-up-an-sla"
}



## Définitions de SLA

En créant une définition de SLA, vous pouvez configurer les mêmes exigences minimales que celles définies par votre fournisseur et les contrôler à l'aide du dashboard **Vue d'ensemble SLA** que vous trouverez dans le menu {{< AppElement type="menuitem" >}}Dashboards > Synthetics > Vue d'ensemble SLA {{< /AppElement >}}. Si le site ou le service ne satisfait pas aux exigences minimales, cela apparaît en rouge dans la vue d'ensemble SLA. Pour en savoir plus sur le dashboard Vue d'ensemble SLA, lisez notre article [Travailler avec les données et rapports SLA]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-sla-data-and-reports" lang="fr" >}}).

{{< callout >}}
**Remarque :** Si vous voyez des tirets et des zéros à la place des données dans votre rapport Vue d'ensemble SLA, c'est parce que le paramétrage de votre tuile/dashboard a entraîné un conflit dans les données et produit des données non valides. Pour en savoir plus sur les causes possibles, lisez l'article de notre base de connaissances intitulé [Données absentes dans Vue d’ensemble SLA]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="fr" >}}).
{{< /callout >}}

### Seuils SLA

Les **seuils SLA** désignent les éléments suivants. Votre définition SLA peut porter uniquement sur la disponibilité, mais aussi d'autres seuils SLA.

- **Erreur de pourcentage uptime** : les résultats de disponibilité inférieurs à ce seuil ne satisfont pas l'objectif du SLA et entraînent une erreur rouge dans les rapports SLA. Les valeurs supérieures à ce seuil (mais inférieures au pourcentage de disponibilité souhaité) entraînent des avertissements dans les rapports SLA.
- **Pourcentage de disponibilité souhaité** : les résultats de disponibilité avec cette valeur (ou plus) sont bons, car satisfont l'objectif du SLA. Les valeurs comprises entre ce seuil et le pourcentage de disponibilité minimum entraîneront un avertissement jaune dans les rapports des SLA.
- **Temps de chargement de page** : le temps de chargement maximum de la page tel que convenu dans le SLA.
- **Temps de réponse opérateur** : le laps de temps entre une alerte Uptrends et le moment où un opérateur se connecte à Uptrends et confirme l'alerte dans le dashboard d'état d'alerte pour indiquer qu'il s'occupe du problème. Le dashboard **Statut d'alerte actuel** ({{< AppElement type="menuitem" >}} Alerte > Statut d'alerte actuel {{< /AppElement >}}) permet de confirmer une alerte.

Pour en savoir plus sur le calcul du pourcentage de disponibilité, consultez l'article de la base de connaissances intitulé [Calcul de la disponibilité et des temps d’arrêt]({{< ref path="support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="fr" >}}).

### Planning SLA {id="sla-schedule"}

Si votre SLA ne s'applique pas 24 heures sur 24 et 7 jours sur 7 (par exemple, s'il ne couvre que les heures de bureau normales ou si vous avez une maintenance programmée), vous pouvez ajouter un planning SLA. Les plannings SLA vous permettent de définir les horaires auxquels votre SLA est actif. Tout temps d'arrêt, temps de chargement trop long ou erreur survenant en dehors de ces horaires ne sera pas pris en compte dans le rapport SLA. Vous pouvez configurer votre planning SLA dans l'onglet {{< AppElement type="tab" >}}Planning{{< /AppElement >}}, où vous trouverez une grille horaire et l'option permettant d'exclure des jours pour des raisons de maintenance.

Lors de la configuration du planning SLA, Uptrends utilise l'heure et la date de votre compte principal. La date et l'heure de l'ordinateur local (sur lequel vous modifiez le planning SLA) ne sont pas prises en compte. Ce fonctionnement simplifie la collaboration entre les opérateurs situés sur différents fuseaux horaires, car les plannings SLA dépendent d'un seul système de date et d'heure, à savoir celui du compte Uptrends.

- **Grille horaire** : précisez le SLA s'applique ou non pour chaque heure de chaque jour de la semaine.

- **Exclure des jours** : si vous avez prévu des temps d'arrêt inhabituels, vous pouvez exclure ces périodes en précisant des jours et des heures.

## Configurer une définition de SLA

Pour définir un SLA :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Définitions SLA {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="button" >}}Ajouter définition SLA {{< /AppElement >}} en haut à droite.
3. Donnez à votre définition un nom parlant.
4. Pour le champ **Disponibilité**, définissez le pourcentage de disponibilité d'erreur (la disponibilité minimum exigée) dans le rectangle jaune. Les résultats de disponibilité inférieurs à cette valeur seront marqués en rouge sur les rapports de la Vue d'ensemble SLA.
5. Dans le même champ **Disponibilité**, dans le rectangle vert, définissez le pourcentage au-dessous duquel la disponibilité devient un point de préoccupation pour le respect des SLA. Les résultats de disponibilité entre ce dernier et le pourcentage de temps de disponibilité des erreurs seront marqués en jaune sur les rapports de la Vue d'ensemble SLA.
6. (Facultatif) Si votre SLA le requiert, réglez aussi le **Temps de chargement de page** et le **Temps de réponse opérateur**.
7. (Facultatif) Si votre SLA ne s'applique pas continuellement, définissez un planning. Dans la grille horaire figurant dans l'onglet {{< AppElement type="tab" >}}Planning{{< /AppElement >}}, les carrés bleus indiquent que le SLA s'applique à ces horaires, tandis que les carrés blancs indiquent le contraire. Cliquez sur un carré pour définir un horaire actif ou inactif. Pour désactiver des journées entières ou la même heure chaque jour, cliquez sur la colonne ou la ligne plutôt que sur les carrés individuels.
8. (Facultatif) Pour les temps d'arrêt planifiés (en dehors du planning), ajoutez des jours d'exclusion dans l'onglet {{< AppElement type="tab" >}}Planning{{< /AppElement >}} :

   1. Cliquez sur le bouton {{< AppElement type="button" >}}Ajouter une nouvelle période d'exclusion{{< /AppElement >}}.
   2. Donnez à la période d'exclusion un nom parlant.
   3. Précisez les jours et heures de début et de fin dans les champs **Du** et **Jusqu'au**.
   4. Cliquez sur {{< AppElement type="button" >}}Définir{{< /AppElement >}}.

9. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas à gauche.
