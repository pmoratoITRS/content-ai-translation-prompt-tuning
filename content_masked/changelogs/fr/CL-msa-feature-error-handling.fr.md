{
  "title": "Nouvelle fonctionnalité dans les moniteurs d'API multi-étapes : la gestion des erreurs",
  "date": "2024-12-18",
  "url": "[URL_BASE_CHANGELOG]decembre-2024-fonctionnalite-gestion-erreurs-moniteurs-api-multi-etapes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Une section consacrée à la [INLINE_CODE_1] a été ajoutée dans l'interface de l'éditeur visuel d'étapes des moniteurs d'API multi-étapes. Cette fonctionnalité vous apporte plus de flexibilité pour gérer les erreurs dans les étapes du monitoring d'API multi-étapes, ce qui renforce votre contrôle et votre capacité d'adaptation face aux comportements des serveurs web dynamiques.

![Case à cocher Gestion des erreurs dans le moniteur d'API multi-étapes]([LINK_URL_1])

Cocher la case **Continuer l'exécution après une erreur** permet d'ignorer les erreurs survenues lors d'une étape du moniteur d'API multi-étapes. Autrement dit, si une étape présente des erreurs (par exemple, une requête erronée, un retard de réponse ou une assertion ayant échoué), le moniteur poursuit la vérification des étapes suivantes. Les erreurs seront visibles uniquement dans les **résultats d'étapes**, avec la mention [INLINE_CODE_2]. Elles n'apparaîtront pas dans les dashboards ou les rapports de **vue d'ensemble des erreurs**.  

Cette fonctionnalité de gestion des erreurs est similaire à celle applicable aux moniteurs de transactions. Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Ignorer les erreurs pour les étapes et actions facultatives]([LINK_URL_2]).

