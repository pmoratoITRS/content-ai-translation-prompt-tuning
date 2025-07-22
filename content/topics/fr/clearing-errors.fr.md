{
"hero": {
"title": "Supprimer des erreurs"
},
"title": "Supprimer des erreurs",
"summary": "Découvrez comment effacer les erreurs incorrectes ou indésirables dans l'historique d'erreurs",
  "url": "/support/kb/alerter/erreurs/supprimer-des-erreurs",
"translationKey": "https://www.uptrends.com/support/kb/error-analysis/clearing-errors"
}

Vous avez la possibilité d'effacer des erreurs ou des groupes d'erreurs (non confirmées et confirmées) que vous jugez incorrectes ou indésirables. Les erreurs individuelles ou peu nombreuses peuvent être effacées par vos soins. Si vous avez de nombreuses erreurs à effacer, Uptrends est là pour vous aider. Pour savoir comment faire, consultez la section [Supprimer des lots d'erreurs]({{< ref path="#bulk-error-clearance" lang="fr" >}}).

Sachez que la suppression d'erreurs n'est pas suivie automatiquement d'une actualisation du calcul des métriques basées sur les erreurs, comme les statistiques des accords de niveau de service ([SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="fr" >}})) ou les données chiffrées des [pages de statut publiques]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="fr" >}}). Lisez la section [Incidence sur les données des SLA et des pages de statut publiques]({{< ref path="#effect-sla-psp-data" lang="fr" >}}) pour savoir comment recalculer les statistiques, selon que les erreurs ont été effacées par vous-même ou par le Support.

{{< callout >}}
**Remarque** : Malheureusement, il est impossible de recalculer les données des SLA supérieures à 90 jours, car ces données ne sont pas conservées au-delà de cette période.
{{< /callout >}}

## Comment effacer des erreurs individuelles {id="clear-individual-errors"}

Pour effacer une erreur dans votre compte :
1. Ouvrez le menu {{< AppElement type="menuitem" >}}Surveillance > Journal moniteurs{{< /AppElement >}}.
2. Cliquez sur l'erreur que vous souhaitez effacer. La fenêtre contextuelle *Voir les détails* relative à cette erreur s'affiche.
3. En bas de la fenêtre, cliquez sur le bouton {{< AppElement type="button" >}}Effacer erreur{{< /AppElement >}}.
4. Confirmez l'action avec le bouton {{< AppElement type="editbutton" >}} Effacer {{< /AppElement >}}.

L'erreur se transforme en un résultat "OK", qui devient immédiatement visible dans le dashboard *Journal moniteurs*.

Les données relatives au pourcentage de disponibilité sont aussi modifiées. Pour des raisons de mise en cache, les changements peuvent ne pas être visibles immédiatement.

## Supprimer des lots d'erreurs {id="bulk-error-clearance"}

Dans certaines situations, vous pouvez avoir besoin de supprimer des erreurs pour une plage de temps spécifique (par exemple, plusieurs journées d'indisponibilité). Plutôt que d'effacer chaque erreur individuellement, nous vous recommandons de procéder comme suit :

1. Si une fenêtre contextuelle *Voir les détails* est ouverte, cliquez sur le bouton {{< AppElement type="editbutton" >}} Effacer les erreurs multiples {{< /AppElement >}} en bas de cette fenêtre. Le formulaire *Demande de suppression des erreurs* s'affiche.
2. Vous pouvez aussi passer par le menu {{< AppElement type="menuitem" >}} Support {{< /AppElement >}} et cliquer sur l'option {{< AppElement type="buttonPrimary" >}} Demande pour effacer les erreurs {{< /AppElement >}}. Le formulaire *Demande de suppression des erreurs* s'affiche.
3. Indiquez les informations obligatoires, à savoir le moniteur ou les groupes de moniteurs concernés, et la plage de dates. Ajoutez toute information facultative en lien avec votre requête, comme le code de statut.
4. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Envoi {{< /AppElement >}}.

Lorsque vous envoyez une requête, un ticket est automatiquement créé pour que votre demande soit traitée. Le traitement de votre demande peut prendre un certain temps, mais le système de ticket vous enverra une notification lorsque la suppression des erreurs et l'actualisation des données SLA auront été effectuées.

## Incidence sur les données des SLA et des pages de statut publiques {id="effect-sla-psp-data"}

La suppression d'erreurs n'est pas suivie automatiquement d'une modification des données relatives aux accords de niveau de service existants [SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="fr" >}}), ni des données des [pages de statut publiques]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="fr" >}}), qui sont aussi liées aux SLA.

Il est toutefois possible de les recalculer. Lorsque vous demandez à l'équipe de support de [supprimer plusieurs erreurs]({{< ref path="#bulk-error-clearance" lang="fr" >}}), un nouveau calcul des données est effectué automatiquement. Il n'est pas nécessaire d'en faire la demande.

En revanche, la situation est différente si vous supprimez vous-même les erreurs. Dans ce cas, veuillez contacter le support au moyen d'un [ticket]({{< ref path="contact" lang="fr" >}}) dans lequel vous indiquerez votre besoin.
