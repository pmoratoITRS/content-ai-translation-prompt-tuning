{
  "hero": {
    "title": "Vue d'ensemble des autorisations"
  },
  "title": "Vue d'ensemble des autorisations",
  "url": "[URL_BASE_TOPICS]compte/autorisations/vue-d'ensemble-des-autorisations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

L'application Uptrends s'appuie sur un système d'autorisations pour attribuer des droits d'accès afin que les opérateurs puissent afficher, modifier ou créer les éléments pertinents pour leur rôle.

D'une manière générale, on distingue deux types d'autorisations : les **autorisations sur tout le système** sont attribuées à un opérateur ou groupe d'opérateurs, tandis que les **autorisations contextuelles** permettent à un opérateur ou groupe d'opérateurs d'accéder à un élément donné. Ces deux types d'autorisations sont présentés en détail ci-dessous.

[SHORTCODE_1] Les autorisations sur tout le système sont disponibles pour toutes les formules d'abonnement. En revanche, les autorisations contextuelles sont réservées aux comptes Enterprise. [SHORTCODE_2]


## Qui peut modifier (octroyer ou révoquer) les autorisations ?

Les administrateurs (membres du groupe d'opérateurs **Administrateurs**) peuvent toujours modifier les autorisations.

Dans le cas des autorisations contextuelles, la situation est légèrement différente puisque les non-administrateurs peuvent aussi être habilités à modifier des autorisations. Dans les faits, cela dépend du niveau de l'autorisation contextuelle qui leur a été accordée, en plus de l'autorisation sur tout le système dont ils disposent.
Pour comprendre le fonctionnement, reportez-vous à la section sur les [autorisations contextuelles]([LINK_URL_1]).

## Autorisations sur tout le système

Les autorisations sur tout le système sont présentées en détail dans l'article de la base de connaissances intitulé [Autorisations]([LINK_URL_2]).

Dans la plupart de cas, nous vous recommandons de définir les autorisations au niveau des groupes d'opérateurs plutôt que des opérateurs individuels. Cette approche aide à conserver une vue d'ensemble. Dans la plupart des cas, vous administrerez des équipes (les groupes d'opérateurs) dont tous les membres devront avoir les mêmes autorisations.

## Autorisations contextuelles [ANCHOR_1]

Dans Uptrends, vous pouvez partir des éléments suivants pour attribuer des autorisations à un groupe d'opérateurs (par exemple, *afficher*, *modifier*, *utiliser* et *créer*). Pour connaître la marche à suivre, consultez les articles correspondants tirés de notre base de connaissances :

- [Définitions d'alerte]([LINK_URL_3])
- [Dashboards]([LINK_URL_4])
- [Intégrations]([LINK_URL_5])
- [Moniteurs]([LINK_URL_6])
- [Coffre-fort]([LINK_URL_7])

## Guide d'utilisation

Ce guide présente la procédure détaillée pour attribuer des autorisations à une nouvelle équipe dans votre compte.

- [Configurer une équipe dans votre compte]([LINK_URL_8])