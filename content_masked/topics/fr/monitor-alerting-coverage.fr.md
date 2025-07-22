{
  "hero": {
    "title": "Couverture d'alerte des moniteurs"
  },
  "title": "Couverture d'alerte des moniteurs",
  "summary": "Vue d'ensemble de tous les moniteurs indiquant pour chacun si les alertes sont couvertes ou non",
  "url": "[URL_BASE_TOPICS]alerter/couverture-alertes-des-moniteurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

La vue d'ensemble [Couverture d'alerte des moniteurs]([LINK_URL_1]) est une liste qui indique si vos moniteurs sont couverts par des définitions d'alertes et vous donne des informations détaillées sur les raisons pour lesquelles ce n'est peut-être pas le cas.

[SHORTCODE_1] **Remarque** : la vue d'ensemble **Couverture d'alerte des moniteurs** tient compte de vos autorisations pour créer une vue personnalisée. Elle vous montre uniquement les définitions d'alerte que vous avez le droit de modifier. Pour le compte Uptrends dans son ensemble, cela signifie qu'un moniteur couvert par une définition d'alerte et lançant des alertes peut néanmoins apparaître comme non couvert dans la vue d'ensemble si vous ne disposez pas des droits d'accès à la définition d'alerte. [SHORTCODE_2]

Si vous avez des moniteurs qui devraient générer des alertes mais qui ne le font pas, ou qu'ils le font alors qu'ils ne le devraient pas, voici comment résoudre le problème.

Pour ouvrir la vue d'ensemble, sélectionnez [SHORTCODE_3]Alerte > Explorer les alertes[SHORTCODE_4], puis cliquez sur la statistique "Moniteurs de production couverts par les alertes".

![Capture d'écran de la statistique sur la couverture d'alerte des moniteurs ]([LINK_URL_2])

La vue d'ensemble *Couverture d'alerte des moniteurs* apparaît avec, en haut de la liste sur fond rouge, les moniteurs qui ne sont pas couverts par une alerte.

![Capture d'écran de la vue d'ensemble sur la couverture d'alerte des moniteurs ]([LINK_URL_3])

Pourquoi ces moniteurs ne sont-ils pas couverts ?
Plusieurs raisons peuvent conditionner la couverture d'une alerte :

- Le moniteur lui-même doit être actif.
- Les alertes pour le moniteur doivent être activées.
- Au moins une définition d'alerte active doit être attachée au moniteur (directement ou via un groupe de moniteurs).
- Dans la définition d'alerte active, au moins un niveau d'escalade doit être actif.

Vérifiez la liste pour savoir quelle condition n'est pas remplie.
