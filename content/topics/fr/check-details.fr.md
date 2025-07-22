{
"hero": {
"title": "Détails de vérification"
},
"title": "Détails de vérification",
"summary": "Les résultats des vérifications effectuées par les moniteurs sont présentés dans une fenêtre intitulée Voir les détails. Les informations disponibles dépendent du type de moniteur.",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/details-verification",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/check-details"
}

Les informations recueillies lors des vérifications effectuées par les moniteurs s'affichent dans une fenêtre intitulée "Voir les détails". Cette fenêtre vous indique si la vérification s'est bien déroulée ou si une erreur a été détectée (d'après vos [conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}})). Elle contient aussi des informations plus détaillées sur la vérification et ses résultats, ce qui peut vous aider à résoudre la cause d'une éventuelle erreur.

## Que contiennent les détails de la vérification ?

Les informations figurant dans les détails de la vérification dépendent fortement du type de moniteur. Pour un moniteur HTTP(S), il peut simplement s'agir d'un code de statut. Les moniteurs plus complexes peuvent aussi fournir des captures d'écran (par exemple, le moniteur Full Page Check) ou les résultats des étapes d'une transaction (par exemple, le moniteur de transaction ou Multi-step API), comme dans les exemples ci-dessous.

Fenêtre Voir les détails (résultat "OK") pour un moniteur HTTPS :

![capture d'écran fenêtre voir les détails moniteur https](/img/content/scr_check-details-https-monitor.min.png)

Fenêtre Voir les détails pour un moniteur de transaction ayant détecté une erreur :

![capture d'écran fenêtre voir les détails moniteur de transaction](/img/content/scr_check-details-transaction-monitor-041024.min.png)

## Où trouver les détails d'une vérification ?

Les détails des vérifications sont accessibles à plusieurs endroits.

Si vous effectuez une vérification au moyen du bouton {{< AppElement type="buttonSecondary" >}} Tester maintenant {{< /AppElement >}}, une fenêtre contextuelle s'affiche avec les détails de la vérification.

Plusieurs dashboards présentent aussi une liste des vérifications. Les détails s'affichent lorsque vous cliquez sur une erreur ou une vérification. Vous pouvez consulter les erreurs ou les vérifications à ces différents endroits :

- Dashboard accessible en cliquant sur {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Vue d'ensemble des erreurs {{< /AppElement >}}
- Dashboard accessible en cliquant sur {{< AppElement type="menuitem" >}} Surveillance > Détails du statut {{< /AppElement >}}
- Dashboard accessible en cliquant sur {{< AppElement type="menuitem" >}} Surveillance > Journal moniteurs {{< /AppElement >}}
- Tuile *Détails dernière vérification* : une [tuile de rapport personnalisée]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#last-check-details" lang="fr" >}}) à ajouter à vos [dashboards personnalisés]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-dashboards" lang="fr" >}})
