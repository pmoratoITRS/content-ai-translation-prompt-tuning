{
"hero": {
"title": "Surveillance par navigateur"
},
"title": "Surveillance par navigateur",
"url": "/support/kb/surveillance-synthetique/browser-monitoring/aperçu-de-la-surveillance-des-navigateurs",
"summary": "Le Full Page Check est le type de moniteur le plus complet. Chaque élément est téléchargé, puis importé dans un navigateur. Le rapport affiche vos résultats dans un graphique en cascade détaillé.",
"translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
"sectionlist": true
}

Les moniteurs de navigateur, aussi appelés Full Page Check (FPC), font partie des différents [types de moniteur]({{< ref path="support/kb/basics/monitor-types" lang="fr" >}}) proposés par Uptrends. Ces moniteurs fournissent des données de performance détaillées sur vos pages web, élément par élément. Le moniteur FPC charge votre page dans un navigateur réel, en incluant les scripts, les styles CSS, les images, les éléments tiers et les autres composantes de votre site web. Ce chargement complet de la page dans un navigateur réel permet de mesurer précisément les performances du site web, telles qu'elles sont vécues par vos utilisateurs finaux.

Le FPC fournit des informations sur la surveillance dans les détails de la vérification du moniteur, notamment sous la forme d'un [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}). Selon le [type de navigateur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="fr" >}}) choisi pour le moniteur, diverses informations supplémentaires peuvent aussi être obtenues (voir l'article sur les [métriques et fonctionnalités supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}})).

Pour surveiller du contenu tiers sur votre site web, vous pouvez utiliser l'option [Full Page Check amélioré]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="fr" >}}).

## Configurer un moniteur FPC {id="set-up-fpc"}

Pour configurer un moniteur FPC, commencez par créer un moniteur puis choisissez le type de navigateur et l'intervalle de vérification, puis définissez les conditions d'erreur, sélectionnez les checkpoints et configurez d'autres options comme les périodes de maintenance.

Pour connaître les bases, vous pouvez lire l'article d'Uptrends sur les types de moniteurs, et plus précisément les [moniteurs de performance de site web]({{< ref path="support/kb/basics/monitor-types#browser-monitors" lang="fr" >}}).

## Moniteurs de navigateur (Full Page Check ou FPC)

Vous avez le choix entre plusieurs types de moniteurs de navigateur :

- [Full Page Check (FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) : ce type de moniteur vérifie tous les éléments lors du chargement de la page, puis affiche l'ensemble des données dans un [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}).

- [Full Page Check amélioré ou Full Page Check \+ (FPC+)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="fr" >}}) : cette option du moniteur FPC vous permet d'ajouter le contenu tiers aux éléments vérifiés sur la page lors du chargement. Ce moniteur affiche aussi toutes les données dans un [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}).

Vous trouverez dans la section [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}) toutes les informations nécessaires pour ajouter ce type de moniteur et gérer les paramètres.

Les paramètres des moniteurs sont présentés dans plusieurs articles de notre base de connaissances, dont voici la liste.

### Principaux paramètres

Les options disponibles dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}} servent à définir les principaux paramètres du moniteur.


- [Intervalle de vérification]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="fr" >}})
- [Surveillance simultanée]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="fr" >}})
- [Mode du moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}})
- [Type de navigateur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="fr" >}})
- [Notes des moniteurs (facultatif)]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="fr" >}})

### Conditions d'erreur

Par défaut, le moniteur FCP vérifie la disponibilité d'une URL de serveur donnée. Les autres vérifications doivent être définies dans l'onglet {{< AppElement type="tab" >}} Conditions d'erreur {{< /AppElement >}} du moniteur.

Pour savoir comment configurer les conditions d'erreur, lisez l'article de notre base de connaissances intitulé [Conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr">}}).

Dans cet article, le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="fr" >}}) indique quelles conditions d'erreur sont compatibles avec le moniteur Full Page Check.

### Autorisations de moniteurs

Le système d'[autorisations]({{< ref path="support/kb/account/permissions" lang="fr" >}}) d'Uptrends permet de définir quelles équipes ou quels membres du personnel ont accès aux différents éléments. Des autorisations diverses sont nécessaires pour créer/supprimer, afficher et modifier les activités.

- [Permissions de moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}})

### Autres paramètres des moniteurs

Les paramètres suivants sont facultatifs, ce qui signifie que le moniteur peut fonctionner sans eux. Toutefois, pour tirer pleinement profit de la surveillance et pour adapter les réglages à votre situation, il est recommandé de configurer les paramètres suivants.

- [Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/checkpoint-information" lang="fr" >}})
- [Périodes de maintenance]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="fr" >}})
- [Groupes de moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="fr" >}})


## Données et rapports des moniteurs

Une fois que votre moniteur est configuré et opérationnel, vous allez commencer à collecter des données sur les performances. Plusieurs métriques sont collectées et stockées par chaque moniteur. Ces données s'affichent dans les détails de la vérification. Pour y accéder, sélectionnez {{< AppElement type="menuitem" >}} Surveillance > Journal moniteurs {{< /AppElement >}} et cliquez sur l'une des entrées.

### Détails de vérification du moniteur

Les détails de la vérification contiennent les [métriques de base sur les temps de chargement]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="fr" >}}) (*temps de résolution*, *temps de connexion*, *temps de chargement* et *temps total*). Les résultats du FPC fournissent également un [graphique en cascade]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) détaillé.

Le graphique en cascade est une représentation visuelle du chargement de la page, pour chaque élément chargé. Il comprend des informations comme l'adresse IP source de l'élément, les en-têtes de requête et de réponse, la taille de l'élément et un aperçu détaillé des [temps de chargement de chaque élément]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="fr" >}}).

### Métriques et fonctionnalités supplémentaires {id="chrome-extra-metrics"}

Avec les [types de navigateurs incluant des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types#chrome-extra-metrics" lang="fr" >}}), vous pouvez obtenir encore d'autres informations, comme les [durées de navigation du W3C]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}), les [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) et les [captures d'écran successives]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}). Ces types de navigateurs vous permettent aussi de configurer un [contournement DNS]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="fr" >}}).

La liste complète des données et fonctionnalités supplémentaires figure dans l'article de la base de connaissances sur les [métriques et fonctionnalités supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}}).

## Crédits

Créer des moniteurs de navigateur et planifier leur exécution utilisent des crédits de navigateur. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}).