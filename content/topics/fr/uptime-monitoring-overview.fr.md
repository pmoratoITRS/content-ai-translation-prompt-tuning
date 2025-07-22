{
"hero": {
"title": "Vue d'ensemble des moniteurs de disponibilité"
},
"title": "Vue d'ensemble des moniteurs de disponibilité",

"summary": "Cet article vous présente les différents moniteurs de disponibilité d'Uptrends et vous explique comment les configurer.",
"url": "/support/kb/synthetic-monitoring/uptime-monitoring/apercu-de-la-surveillance-de-la-disponibilite",
"translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview",
"tableofcontents": true,
"sectionlist": true
}

Les **moniteurs de disponibilité** font partie des différents [types de moniteurs]({{< ref path="support/kb/basics/monitor-types" lang="fr" >}}) proposés par Uptrends. Ces moniteurs effectuent des vérifications de base, par exemple sur la disponibilité du site web, le contenu des pages et les temps de chargement.

En tâche de fond, ces moniteurs obtiennent l'URL de votre site web et envoient une requête à cette URL. La réponse doit leur permettre de récupérer toutes les sources des pages de votre site web (sous forme de document HTML) ainsi que le code de statut de réponse 200. Une fois ces exigences satisfaites, les moniteurs considèrent que votre site web est atteignable et fonctionne comme attendu.

## Types de moniteurs de disponibilité

Vous avez le choix entre plusieurs types de moniteurs de disponibilité :

### Moniteurs HTTP et HTTPS

Le moniteur **HTTP** permet de vérifier la disponibilité d'un site web HTTP, tandis que le moniteur **HTTPS** permet de vérifier la disponibilité des sites web HTTP et HTTPS (qui sont sécurisés par un certificat SSL).

Depuis peu, le type de moniteur **HTTP** n'est plus disponible pour les nouveaux utilisateurs. Uptrends a complété les fonctionnalités des moniteurs **HTTPS** pour prendre en charge et vérifier la disponibilité des sites web HTTP. Pour en savoir plus, lisez l'article [Vue d'ensemble des moniteurs HTTP et HTTPS]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-and-https-overview" lang="fr" >}}).

### Moniteurs de vérification de réseau {id="network-server-monitors"}

Vous avez le choix entre plusieurs types de moniteurs de vérification de réseau :

- **Ping** : ce moniteur vérifie la disponibilité d'une adresse IP, à condition qu'elle ne se trouve pas derrière un pare-feu.
- **Connect** : ce moniteur vérifie la disponibilité de votre réseau en effectuant un TCP Connect de bas niveau sur un port spécifique.

Pour en savoir plus, vous pouvez lire les articles sur la [vérification de réseau]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="fr" >}}) et [la configuration d'un moniteur de vérification du réseau]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="fr" >}}).

### Moniteurs de serveurs de bases de données

Uptrends fournit deux types de moniteurs permettant de vérifier la disponibilité de bases de données : **Microsoft SQL** et **MySQL**. Pour en savoir plus, lisez notre article sur les [moniteurs de base de données]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/database-server-monitors" lang="fr" >}}).

### Moniteurs de serveurs mails

Vous avez le choix entre trois principaux types de moniteurs de serveur mail :

- Simple Mail Transfer Protocol (SMTP)
- Post Office Protocol (POP3)
- Internet Message Access Protocol (IMAP)

Pour en savoir plus, vous pouvez lire l'article sur les [moniteurs de serveur mail]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/mail-server-monitors" lang="fr" >}}).

### Moniteurs de disponibilité avancés

Uptrends propose des moniteurs de disponibilité plus avancés qui peuvent être utilisés pour les transferts de données :

- File Transfer Protocol (FTP) et Secure File Transfer Protocol (SFTP) : ces moniteurs vérifient la disponibilité de vos [moniteurs FTP et SFTP]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ftp-and-sftp" lang="fr" >}}).
- Domain Name System (DNS) : ce moniteur vérifie si la configuration DNS est disponible et fonctionne comme attendu.
- Certificat Secure Sockets Layer (SSL) : ce moniteur vérifie si vos certificats SSL sont encore valides et n'ont pas expiré.

## Crédits

Créer des moniteurs de disponibilité et planifier leur exécution utilisent des crédits de disponibilité. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="fr" >}}).