{
"hero": {
"title": "Types de navigateurs avec des métriques supplémentaires"
},
"title": "Types de navigateurs avec des métriques supplémentaires",
"summary": "Certains types de navigateurs fournissent plus d'informations et des fonctionnalités plus avancées que les autres. Lisez cet article pour en savoir plus sur ces informations et fonctionnalités supplémentaires.",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/metriques-et-fonctionnalites-supplementaires",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/extra-metrics-and-features",
"tableofcontents": true
}

Plusieurs métriques et fonctionnalités supplémentaires sont fournies lorsqu'un moniteur Full Page Check ou de transaction utilise les [types de navigateurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="fr" >}}) suivants :

- Chrome avec des métriques supplémentaires
- Microsoft Edge

Le navigateur Chrome avec des métriques supplémentaires relève les Core Web Vitals et les durées de navigation du W3C lors de la surveillance des transactions.

## Caractéristiques

### Vérifications directes

Avec ces types de navigateurs, le moniteur FPC mesure les performances directement dans le navigateur. Ceci permet au navigateur de fonctionner de manière aussi naturelle que possible.

### Prise en charge et en-têtes des protocoles HTTP2, HTTP3 et QUIC

En plus du protocole HTTP, les protocoles HTTP2, HTTP3 et QUIC sont pris en charge.

Les requêtes effectuées par les protocoles HTTP2, HTTP3 et QUIC ont des en-têtes distincts du protocole HTTP. Il n'y a pas d'en-têtes X-Uptrends, tels que X-Uptrends-PortInfo et X-Blocked-By-Uptrends.

### Correspondance de contenu

Seul le résultat final est pris en compte pour une correspondance du contenu. Le contenu affiché lors d'une redirection ne déclenche pas de correspondance de contenu.

### Blocage d'URL

La navigation vers un site aboutit dans tous les cas, même si l'URL de ce site figure dans la liste des URL bloquées. S'il est configuré avec un navigateur proposant des métriques supplémentaires, le FPC ne bloque pas la navigation. En revanche, les autres éléments auxquels le site fait référence, comme les images, sont bloqués.

### Éléments mis en cache

Comme Uptrends extrait les informations de performance à partir du navigateur, les éléments en cache peuvent être affichés. Il est possible de les filtrer si on le souhaite.

### Contournement DNS

Vous pouvez ajouter un contournement DNS. Le Full Page Check charge votre page au moyen d'un navigateur réel, télécharge chaque élément et affiche un graphique en cascade pour permettre l'inspection de ces éléments. Le [contournement DNS]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="fr" >}}) permet de s'assurer que la résolution de la page web se fait dans un nom de domaine ou une adresse IP spécifique. Le contournement DNS est aussi disponible pour les transactions.

## Métriques

### Techniques de mesure

Les résultats (durées et nombre total d'octets) qui s'affichent dans un type de navigateur avec métriques supplémentaires ne sont pas les mêmes qu'avec les autres types de navigateurs.

Le FPC (configuré avec un navigateur offrant des métriques supplémentaires) prend en charge de nouveaux protocoles tels que HTTP2 et HTTP3. Il est aussi étroitement intégré au navigateur. Par conséquent, le graphique en cascade généré peut être différent de celui d'un moniteur FPC utilisant un autre type de navigateur. Vous allez certainement voir plus de requêtes simultanées, qui se transfèrent plus rapidement. Comme la mesure peut être plus rapide ou plus lente, le nombre total d'octets peut également différer, car Uptrends ne capture pas les mêmes activités en arrière-plan une fois la page chargée (par exemple, une vidéo qui se charge, ou un service worker JavaScript qui effectue des tâches en arrière-plan).

### Core Web Vitals

Les Core Web Vitals (signaux web essentiels) sont des mesures faites par Google qui aident à comprendre la performance de votre site web. Uptrends mesure et rapporte maintenant ces métriques dans les résultats de vérification. Vous pouvez rapporter toutes les métriques dans un tableau de bord personnalisé. Pour cela, utilisez une tuile de type [Liste ou graphique de données simple] ({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}) et choisissez les valeurs dans la liste de données des Core Web Vitals.

Les résultats de ces mesures peuvent être différents de ceux effectués avec l'outil Lighthouse.
L'outil Lighthouse fourni par Google utilise une technique de mesure différente de celle d'Uptrends. Nous utilisons un navigateur qui visite un site web comme le ferait un utilisateur normal. L'outil Lighthouse effectue d'abord une mise en route, puis visite le site plusieurs fois pour déterminer une moyenne. L'outil Lighthouse ne déclenche pas non plus certains contrôles d'entrée de l'utilisateur, contrairement à notre technique de mesure et aux utilisateurs normaux. Il simule également une connexion plus lente au moyen d'une limitation de la bande passante. C'est pourquoi les indicateurs Core Web Vitals rapportés par Lighthouse peuvent différer des mesures Uptrends.

Pour tout savoir sur les nouvelles métriques, consultez l'article sur les [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}).

### Métriques du W3C

Le World Wide Web Consortium (W3C) a défini un ensemble de timings de navigation qui sont essentiels au chargement d'une page web. Uptrends a adopté plusieurs de ces timings pour les mesurer et les présenter dans des rapports. Vous pouvez rapporter toutes les métriques dans un tableau de bord personnalisé. Pour cela, utilisez une tuile de type [Liste ou graphique de données simple]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="fr" >}}) et choisissez les valeurs dans la liste de données du W3C relatives aux durées de navigation.

Consultez l'article de la base de connaissances [Mesures des durées de navigation du W3C]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="fr" >}}) pour en savoir plus sur les durées de navigation mises en œuvre.

Les [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}) et les durées de navigation du W3C sont aussi disponibles pour vos [transactions]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}). Pour appliquer ces métriques à votre monitoring de transaction, il vous suffit de sélectionner **Chrome avec des métriques supplémentaires** dans le menu déroulant *Type de navigateur* dans l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} des paramètres de moniteur. Vous trouverez les métriques supplémentaires dans le [graphique en cascade de la transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="fr" >}}), à chaque étape pour laquelle un graphique en cascade a été configuré. (Disponible pour les [comptes Business et Enterprise]({{< ref path="/pricing" lang="fr" >}}) uniquement.)

### Temps de chargement : temps total du W3C ou temps d'activité réseau

Les moniteurs Full Page Check et les moniteurs de transactions utilisant un type de navigateur offrant des *métriques supplémentaires* permettent de mesurer le temps de chargement total d'après le *load event du W3C* ou d'après le *temps d'activité réseau*.

#### Temps total du W3C

Si vous sélectionnez le temps total du W3C, la métrique correspondant à la fin de l'événement de chargement (load event) W3C sera utilisée. Le W3C load event est décrit plus en détail ici (article en anglais) : https://www.w3.org/TR/navigation-timing/#dom-performancetiming-loadend.

Cette métrique n'est pas calculée dans l'application Uptrends mais provient directement du navigateur, et plus précisément des outils de développement.

Les résultats de la mesure sont accessibles dans les détails de vérification du moniteur. Reportez-vous à la section *Charger l'événement* (Load Event) dans les métriques *Calendrier de navigation W3C* (Temps de navigation W3C).

![capture d'écran montrant la section load event dans la rubrique des temps de navigation w3c](/img/content/scr_w3c-navigation-timing-load-event.min.png)

#### Temps d'activité réseau

Le temps d'activité réseau est mesuré jusqu'à la survenue d'une période d'inactivité sur le réseau.

#### Configuration des paramètres de temps de chargement pour un moniteur

Pour faire votre choix, allez dans l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} des paramètres du moniteur. Dans la section *Mesure*, sélectionnez l'une des options disponibles pour le champ *Baser le temps de chargement sur* :

![capture d'écran de la mesure du temps total](/img/content/scr-fpc-choose-load-time-v2.min.png)

#### Différences entre les métriques et recommandations pour le paramétrage

La différence peut être importante selon que vous choisissez de mesurer le temps total d'après le temps de chargement W3C ou le temps d'activité réseau.
Les résultats (et les différences) dépendent fortement de ce que vous surveillez. Par exemple, pour une transaction qui utilise le load event du W3C, un changement de méthode modifie les temps de chargement pour chaque étape, et donc le temps total.

Dans le cas du moniteur Full Page Check, plusieurs actions de navigation peuvent s'afficher, par exemple si des redirections sont paramétrées. Les métriques sont enregistrées par action de navigation et résumées pour la métrique complète du *W3C load event*.

Dans le cas des moniteurs de transactions, plusieurs actions de navigation peuvent être paramétrées par étape. Vous pouvez donc avoir plusieurs actions de navigation ou une action de navigation qui entraîne d'autres actions de navigation. Les temps de chargement sont résumés par étape, puis à nouveau résumés pour la transaction dans son ensemble au moyen de la métrique *temps total*.
Une exception s'applique : si l'étape ne comprend pas d'action de navigation mais, par exemple, une vérification de contenu, la durée de cette étape est 0 (sauf si vous utilisez le *temps d'activité réseau*). Dans ce cas, le temps d'activité réseau ne correspond pas à la période d'inactivité du réseau, mais dépend du délai d'exécution des étapes.

Voici quelques recommandations pour vous aider à choisir la meilleure méthode pour les transactions :

- Si vous souhaitez connaître le temps de chargement de votre page, c'est-à-dire si vous vous intéressez seulement au chargement, nous vous recommandons de sélectionner l'option du temps de chargement du W3C.
- Si vous souhaitez analyser l'expérience de l'utilisateur final, par exemple pour savoir combien de temps il faut pour réaliser une transaction, nous vous recommandons d'utiliser le temps basé sur le réseau. En effet, cette option prend tout en compte, y compris les étapes qui ne sont pas des actions de navigation mais qui influencent néanmoins le temps dont l'utilisateur a besoin pour réaliser une transaction.

### Captures d'écran successives

Les [captures d'écran successives (ou pellicule)]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}) consistent en plusieurs captures d'écran prises pendant le chargement de la page web surveillée. La chronologie est présentée au-dessus de la cascade dans la fenêtre des détails de la vérification :

![capture d'écran de la pellicule dans les détails de la vérification](/img/content/scr-filmstrip.min.png)

### URL de données dans la cascade

Les éléments qui sont intégrés dans le document HTML, tels que les URL de données, ou qui proviennent de JavaScript, tels que les URL Blob, sont également affichés dans la cascade. Vous pouvez appliquer un filtre si nécessaire.

### Informations TLS

Dans la cascade fournie avec les détails de vérification du moniteur, vous pouvez trouver des informations TLS pour chaque élément.fi
Vous les verrez en cliquant sur le signe plus à côté de l'élément :

![capture d'écran des informations TLS dans la cascade](/img/content/scr-TLS-info.min.png)


