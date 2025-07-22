{
"title": "Amélioration apportée à la suppression de lots d'erreurs",
"date": "2024-01-04",
"url": "/changelog/janvier-2024-amelioration-suppression-lots-erreurs",
"translationKey": "https://www.uptrends.com/changelog/january-2024-clearing-errors-in-bulk-improved"
}

Si vous rencontrez des [erreurs]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}}) qui vous semblent incorrectes, vous avez la possibilité de [les supprimer]({{< ref path="support/kb/alerting/errors/clearing-errors" lang="fr" >}}), puis de recalculer les données de l'[accord de niveau de service (SLA)]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="fr" >}}).

Jusqu'à présent, vous deviez créer un ticket de support (standard) et fournir certaines informations pour demander la suppression d'une erreur.
Nous avons simplifié la procédure en ajoutant un bouton {{< AppElement type="buttonSecondary" >}} Effacer les erreurs multiples {{< /AppElement >}} en bas de la boîte de dialogue *Voir les détails* du moniteur.

Ce bouton permet d'ouvrir un ticket spécifique à cette suppression d'erreur. Dans le ticket, vous devez inclure les données nécessaires pour que l'équipe de support puisse traiter votre demande.
Ces données sont le moniteur ou les groupes de moniteurs concernés, et la plage de dates. Vous pouvez aussi préciser les checkpoints et le code d'erreur.