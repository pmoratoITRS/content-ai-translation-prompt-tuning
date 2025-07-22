{
"hero": {
"title": "Apercu des erreurs"
},
"title": "Apercu des erreurs",
"summary": "Lorsqu'une vérification de moniteur rencontre un problème (préalablement défini dans les conditions d'erreur), une erreur est signalée.",
"url": "/support/kb/alerter/erreurs/apercu-des-erreurs",
"translationKey": "https://www.uptrends.com/support/kb/error-analysis/errors-overview",
"sectionlist": false,
"tableofcontents": false
}

Lorsqu'un problème survient sur votre site web ou dans vos services, la vérification du moniteur produit une erreur. Pour cela, vous devez définir ce qui représente un problème en configurant des [conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}}) dans vos moniteurs.

Il convient de préciser qu'une erreur n'est pas la même chose qu'une alerte. Pour bien comprendre les différences et le rapport entre les erreurs et les alertes, vous pouvez lire l'article [Présentation des alertes]({{< ref path="support/kb/alerting/alerting-overview" lang="fr" >}}).

Afin d'éviter les faux positifs, les erreurs sont toujours vérifiées deux fois. Pour en savoir plus à ce sujet, vous pouvez lire l'article [Erreurs non confirmées et confirmées]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}).

Lorsqu'une erreur se produit, elle apparaît dans le dashboard *Vue d'ensemble des erreurs*. Pour y accéder, passez par le menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Vue d'ensemble des erreurs{{< /AppElement >}}. De plus amples informations figurent dans la fenêtre [Voir les détails]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="fr" >}}) correspondant à la vérification du moniteur ayant signalé l'erreur.

Selon le moniteur et le contexte de l'erreur, une [capture d'écran d'erreur]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="fr" >}}) est parfois fournie pour vous aider à résoudre le problème.

Il existe de nombreux types d'erreurs. Si vous avez besoin d'informations sur une erreur, vous pouvez effectuer une recherche par code d'erreur ou selon d'autres critères sur la page [Types d'erreurs]({{< ref path="support/kb/alerting/errors/error-types" lang="fr" >}}).

Si des erreurs vous semblent incorrectes ou à supprimer de la liste d'erreurs, vous pouvez [supprimer des erreurs]({{< ref path="support/kb/alerting/errors/clearing-errors" lang="fr" >}}).
