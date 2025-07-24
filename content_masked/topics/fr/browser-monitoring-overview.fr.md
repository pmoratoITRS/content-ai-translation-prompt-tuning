{
  "hero": {
    "title": "Surveillance par navigateur"
  },
  "title": "Surveillance par navigateur",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/browser-monitoring/aperçu-de-la-surveillance-des-navigateurs",
  "summary": "Le Full Page Check est le type de moniteur le plus complet. Chaque élément est téléchargé, puis importé dans un navigateur. Le rapport affiche vos résultats dans un graphique en cascade détaillé.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Les moniteurs de navigateur, aussi appelés Full Page Check (FPC), font partie des différents [types de moniteur]([LINK_URL_1]) proposés par Uptrends. Ces moniteurs fournissent des données de performance détaillées sur vos pages web, élément par élément. Le moniteur FPC charge votre page dans un navigateur réel, en incluant les scripts, les styles CSS, les images, les éléments tiers et les autres composantes de votre site web. Ce chargement complet de la page dans un navigateur réel permet de mesurer précisément les performances du site web, telles qu'elles sont vécues par vos utilisateurs finaux.

Le FPC fournit des informations sur la surveillance dans les détails de la vérification du moniteur, notamment sous la forme d'un [graphique en cascade]([LINK_URL_2]). Selon le [type de navigateur]([LINK_URL_3]) choisi pour le moniteur, diverses informations supplémentaires peuvent aussi être obtenues (voir l'article sur les [métriques et fonctionnalités supplémentaires]([LINK_URL_4])).

Pour surveiller du contenu tiers sur votre site web, vous pouvez utiliser l'option [Full Page Check amélioré]([LINK_URL_5]).

## Configurer un moniteur FPC [ANCHOR_1]

Pour configurer un moniteur FPC, commencez par créer un moniteur puis choisissez le type de navigateur et l'intervalle de vérification, puis définissez les conditions d'erreur, sélectionnez les checkpoints et configurez d'autres options comme les périodes de maintenance.

Pour connaître les bases, vous pouvez lire l'article d'Uptrends sur les types de moniteurs, et plus précisément les [moniteurs de performance de site web]([LINK_URL_6]).

## Moniteurs de navigateur (Full Page Check ou FPC)

Vous avez le choix entre plusieurs types de moniteurs de navigateur :

- [Full Page Check (FPC)]([LINK_URL_7]) : ce type de moniteur vérifie tous les éléments lors du chargement de la page, puis affiche l'ensemble des données dans un [graphique en cascade]([LINK_URL_8]).

- [Full Page Check amélioré ou Full Page Check \+ (FPC+)]([LINK_URL_9]) : cette option du moniteur FPC vous permet d'ajouter le contenu tiers aux éléments vérifiés sur la page lors du chargement. Ce moniteur affiche aussi toutes les données dans un [graphique en cascade]([LINK_URL_10]).

Vous trouverez dans la section [Full Page Check]([LINK_URL_11]) toutes les informations nécessaires pour ajouter ce type de moniteur et gérer les paramètres.

Les paramètres des moniteurs sont présentés dans plusieurs articles de notre base de connaissances, dont voici la liste.

### Principaux paramètres

Les options disponibles dans l'onglet [SHORTCODE_1] Principal [SHORTCODE_2] servent à définir les principaux paramètres du moniteur.


- [Intervalle de vérification]([LINK_URL_12])
- [Surveillance simultanée]([LINK_URL_13])
- [Mode du moniteur]([LINK_URL_14])
- [Type de navigateur]([LINK_URL_15])
- [Notes des moniteurs (facultatif)]([LINK_URL_16])

### Conditions d'erreur

Par défaut, le moniteur FCP vérifie la disponibilité d'une URL de serveur donnée. Les autres vérifications doivent être définies dans l'onglet [SHORTCODE_3] Conditions d'erreur [SHORTCODE_4] du moniteur.

Pour savoir comment configurer les conditions d'erreur, lisez l'article de notre base de connaissances intitulé [Conditions d'erreur]([LINK_URL_17]).

Dans cet article, le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]([LINK_URL_18]) indique quelles conditions d'erreur sont compatibles avec le moniteur Full Page Check.

### Autorisations de moniteurs

Le système d'[autorisations]([LINK_URL_19]) d'Uptrends permet de définir quelles équipes ou quels membres du personnel ont accès aux différents éléments. Des autorisations diverses sont nécessaires pour créer/supprimer, afficher et modifier les activités.

- [Permissions de moniteur]([LINK_URL_20])

### Autres paramètres des moniteurs

Les paramètres suivants sont facultatifs, ce qui signifie que le moniteur peut fonctionner sans eux. Toutefois, pour tirer pleinement profit de la surveillance et pour adapter les réglages à votre situation, il est recommandé de configurer les paramètres suivants.

- [Checkpoints]([LINK_URL_21])
- [Périodes de maintenance]([LINK_URL_22])
- [Groupes de moniteurs]([LINK_URL_23])


## Données et rapports des moniteurs

Une fois que votre moniteur est configuré et opérationnel, vous allez commencer à collecter des données sur les performances. Plusieurs métriques sont collectées et stockées par chaque moniteur. Ces données s'affichent dans les détails de la vérification. Pour y accéder, sélectionnez [SHORTCODE_5] Surveillance > Journal moniteurs [SHORTCODE_6] et cliquez sur l'une des entrées.

### Détails de vérification du moniteur

Les détails de la vérification contiennent les [métriques de base sur les temps de chargement]([LINK_URL_24]) (*temps de résolution*, *temps de connexion*, *temps de chargement* et *temps total*). Les résultats du FPC fournissent également un [graphique en cascade]([LINK_URL_25]) détaillé.

Le graphique en cascade est une représentation visuelle du chargement de la page, pour chaque élément chargé. Il comprend des informations comme l'adresse IP source de l'élément, les en-têtes de requête et de réponse, la taille de l'élément et un aperçu détaillé des [temps de chargement de chaque élément]([LINK_URL_26]).

### Métriques et fonctionnalités supplémentaires [ANCHOR_2]

Avec les [types de navigateurs incluant des métriques supplémentaires]([LINK_URL_27]), vous pouvez obtenir encore d'autres informations, comme les [durées de navigation du W3C]([LINK_URL_28]), les [Core Web Vitals]([LINK_URL_29]) et les [captures d'écran successives]([LINK_URL_30]). Ces types de navigateurs vous permettent aussi de configurer un [contournement DNS]([LINK_URL_31]).

La liste complète des données et fonctionnalités supplémentaires figure dans l'article de la base de connaissances sur les [métriques et fonctionnalités supplémentaires]([LINK_URL_32]).

## Crédits

Créer des moniteurs de navigateur et planifier leur exécution utilisent des crédits de navigateur. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]([LINK_URL_33]).