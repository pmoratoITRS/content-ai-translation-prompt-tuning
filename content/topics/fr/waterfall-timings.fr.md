{
"hero": {
"title": "Timings des cascades"
},
"title": "Timings des cascades",
"url": "/support/kb/surveillance-synthetique/resultats-surveillance/timings-des-cascades",
"translationKey": "https://www.uptrends.com/support/kb/monitoring-results/waterfall-timings",
"tableofcontents": true
}

Pour certains types de moniteurs, les résultats de la vérification du moniteur sont présentés sous forme d'un graphique en cascade. Ce [graphique en cascade]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="fr" >}}) est une présentation graphique du temps qu'il a fallu aux éléments de la page pour se charger.


En survolant le graphique, vous pouvez zoomer sur les timings par élément.

![capture d'écran du popup des mesures de la cascade](/img/content/scr_waterfall_chart-popup-detail.min.png)

## Étapes du processus de chargement

Les timings sont répartis sur un nombre d'étapes nécessaires au chargement de l'élément. Une légende avec les couleurs des étapes est située en haut du graphique en cascade :

![capture d'écran de la légende des timings de la cascade](/img/content/scr_waterfall_chart-timings-legend.min.png)

Tous les timings sont indiqués en millisecondes. Les différentes étapes du processus de chargement sont décrites ci-dessous.

### Début

La valeur *Start* (début) est la seule valeur de cette collection qui n'est pas une durée, mais un moment dans la chronologie. Plus précisément, il s'agit du moment où le chargement de l'élément de page en question a commencé dans la chronologie complète de la page.

### File d'attente

La durée *File d'attente* est la durée pendant laquelle une requête est restée en file d'attente.

Il existe différentes raisons d'être mis en attente :

- Une requête avec une priorité plus élevée existe. Par exemple, les images ont souvent une priorité inférieure à celle des scripts ou des feuilles de style.
- La requête attend la libération d'un socket TCP.
- Il y a déjà 6 connexions TCP ouvertes pour la même origine. Cette raison n'est valable que pour HTTP/1.0 et HTTP/1.1.
- Le navigateur alloue de l'espace dans le cache disque.

### Résolution

Il s'agit du temps pris par le navigateur pour effectuer la recherche DNS de l'élément de page. La recherche DNS est utilisée pour traduire un nom de domaine ou une URL en une adresse IP correspondante.

### Connexion TCP

*Connexion TCP* est le temps qu'il faut pour établir la connexion TCP entre le client et l'adresse IP du serveur web.

### HTTPS handshake

Un handshake (poignée de main) se compose d'un certain nombre de sous-étapes qui sont nécessaires pour initier une communication sécurisée entre le client et le serveur. Cette étape est également appelée "handshake TLS".

### Envoi

Une fois la connexion établie et la communication sécurisée négociée, le client envoie une demande au serveur web.

### En attente

C'est le temps qui s'écoule entre l'envoi d'une requête et la réponse du serveur web.

### Réception

C'est le temps nécessaire pour recevoir la réponse du serveur web.

### Timeout

Ce temps ne s'applique que si la requête a échoué. Dans ce cas, il indique la période pendant laquelle le client n'a pas reçu de réponse. Il y aura seulement un temps de début et un délai d'attente dans ce cas, aucun autre timing.
