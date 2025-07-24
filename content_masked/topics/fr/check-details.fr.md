{
  "hero": {
    "title": "Détails de vérification"
  },
  "title": "Détails de vérification",
  "summary": "Les résultats des vérifications effectuées par les moniteurs sont présentés dans une fenêtre intitulée Voir les détails. Les informations disponibles dépendent du type de moniteur.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/resultats-surveillance/details-verification",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les informations recueillies lors des vérifications effectuées par les moniteurs s'affichent dans une fenêtre intitulée "Voir les détails". Cette fenêtre vous indique si la vérification s'est bien déroulée ou si une erreur a été détectée (d'après vos [conditions d'erreur]([LINK_URL_1])). Elle contient aussi des informations plus détaillées sur la vérification et ses résultats, ce qui peut vous aider à résoudre la cause d'une éventuelle erreur.

## Que contiennent les détails de la vérification ?

Les informations figurant dans les détails de la vérification dépendent fortement du type de moniteur. Pour un moniteur HTTP(S), il peut simplement s'agir d'un code de statut. Les moniteurs plus complexes peuvent aussi fournir des captures d'écran (par exemple, le moniteur Full Page Check) ou les résultats des étapes d'une transaction (par exemple, le moniteur de transaction ou Multi-step API), comme dans les exemples ci-dessous.

Fenêtre Voir les détails (résultat "OK") pour un moniteur HTTPS :

![capture d'écran fenêtre voir les détails moniteur https]([LINK_URL_2])

Fenêtre Voir les détails pour un moniteur de transaction ayant détecté une erreur :

![capture d'écran fenêtre voir les détails moniteur de transaction]([LINK_URL_3])

## Où trouver les détails d'une vérification ?

Les détails des vérifications sont accessibles à plusieurs endroits.

Si vous effectuez une vérification au moyen du bouton [SHORTCODE_1] Tester maintenant [SHORTCODE_2], une fenêtre contextuelle s'affiche avec les détails de la vérification.

Plusieurs dashboards présentent aussi une liste des vérifications. Les détails s'affichent lorsque vous cliquez sur une erreur ou une vérification. Vous pouvez consulter les erreurs ou les vérifications à ces différents endroits :

- Dashboard accessible en cliquant sur [SHORTCODE_3] Dashboards > Synthetics > Vue d'ensemble des erreurs [SHORTCODE_4]
- Dashboard accessible en cliquant sur [SHORTCODE_5] Surveillance > Détails du statut [SHORTCODE_6]
- Dashboard accessible en cliquant sur [SHORTCODE_7] Surveillance > Journal moniteurs [SHORTCODE_8]
- Tuile *Détails dernière vérification* : une [tuile de rapport personnalisée]([LINK_URL_4]) à ajouter à vos [dashboards personnalisés]([LINK_URL_5])
