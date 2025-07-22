{
"title": "Nouvelle fonctionnalité dans les moniteurs d'API multi-étapes : la gestion des erreurs",
"date": "2024-12-18",
"url": "/changelog/decembre-2024-fonctionnalite-gestion-erreurs-moniteurs-api-multi-etapes",
"translationKey": "https://www.uptrends.com/changelog/december-2024-msa-error-handling-feature"
}

Une section consacrée à la `gestion des erreurs` a été ajoutée dans l'interface de l'éditeur visuel d'étapes des moniteurs d'API multi-étapes. Cette fonctionnalité vous apporte plus de flexibilité pour gérer les erreurs dans les étapes du monitoring d'API multi-étapes, ce qui renforce votre contrôle et votre capacité d'adaptation face aux comportements des serveurs web dynamiques.

![Case à cocher Gestion des erreurs dans le moniteur d'API multi-étapes](/img/content/scr-error-handling-checkbox.min.png)

Cocher la case **Continuer l'exécution après une erreur** permet d'ignorer les erreurs survenues lors d'une étape du moniteur d'API multi-étapes. Autrement dit, si une étape présente des erreurs (par exemple, une requête erronée, un retard de réponse ou une assertion ayant échoué), le moniteur poursuit la vérification des étapes suivantes. Les erreurs seront visibles uniquement dans les **résultats d'étapes**, avec la mention `Une erreur est survenue lors de cette étape`. Elles n'apparaîtront pas dans les dashboards ou les rapports de **vue d'ensemble des erreurs**.  

Cette fonctionnalité de gestion des erreurs est similaire à celle applicable aux moniteurs de transactions. Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Ignorer les erreurs pour les étapes et actions facultatives]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="fr" >}}).

