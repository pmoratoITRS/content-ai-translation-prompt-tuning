{
"title": "De l'interface utilisateur classique à la nouvelle interface",
"summary": "Comment la nouvelle interface utilisateur se compare-t-elle à l'interface classique ?",
"url": "/support/kb/demarrage/interface-utilisateur/de-classique-nouvelle-ui",
"translationKey": "https://www.uptrends.com/support/kb/user-interface/from-classic-to-new-ui",
"draft": false
}

{{< callout >}} **Remarque :** Le nouveau menu est le seul disponible depuis le 10 mai 2023, et tous les comptes l'utilisent. Vous ne pouvez plus revenir au menu classique. {{< /callout >}}

L'interface utilisateur (UI) de l'application Uptrends existe depuis plusieurs années et il était temps de la changer.

L'un des objectifs de la nouvelle interface utilisateur est d'intégrer les produits Synthetics, RUM et Infra d'Uptrends dans la même application Uptrends. Ceci est visible dans le nouveau menu latéral et le nouveau dashboard "Vue d'ensemble à 360 degrés", qui affiche des informations sur les différents produits. De plus, l'interface utilisateur a été rafraîchie et des hubs ont été ajoutés pour présenter les informations connexes en un seul endroit.

Cet article vous aidera à naviguer dans la nouvelle interface utilisateur de l'application Uptrends. Beaucoup de choses ont changé, sans forcément affecter votre façon de travailler. Par exemple, les dashboards ont un nouveau look. L'aspect est différent, mais vous trouverez toujours ce dont vous avez besoin dans les endroits bien connus.

Le menu est une autre histoire. Il a été totalement retravaillé, et les positions des menus et même certains noms ont changé. Uptrends vous recommande de consulter le tableau [Comparaison des deux menus](#classic-vs-new-menu), ainsi que la section sur les [changements dans le menu](#menu) pour en savoir plus sur ces modifications.

## Comparaison entre les deux menus {id="classic-vs-new-menu"}

Le tableau ci-dessous montre comment la correspondance entre les éléments des deux menus.

{{< callout >}}**Astuce :** Si vous ne savez pas où trouver quelque chose dans le nouveau menu, mais que vous connaissez son nom dans le menu classique, vous pouvez toujours utiliser la fonction de recherche dans le menu latéral pour essayer de trouver le nouvel emplacement.{{< /callout >}}

| Menu classique | Nouveau menu latéral |
|--------------------------------------------------|--------------------------------------------------------------------------------|
| Moniteurs > Journal des moniteurs | Surveillance > Journal moniteurs |
| Moniteurs > Statut moniteurs | Surveillance > Détails du statut |
| Moniteurs > Moniteurs | Surveillance > Configuration du moniteur |
| Moniteurs > Groupes de moniteurs | Configuration de compte > Groupes de moniteurs |
| Moniteurs > Sites web RUM | RUM > Véritables utilisateurs > Sites web en RUM |
| Moniteurs > Modèles de moniteur | Configuration de compte > Modèles de moniteur |
| Moniteurs > Périodes de maintenance | Configuration de compte > Périodes de maintenance |
| Tableaux de bord, divers tableaux de bord | Dashboards > Parcourir tout |
| Dashboards > Ajouter dashboard | Dashboards > Ajouter un nouveau dashboard OU Dashboards > Parcourir tout > Ajouter un nouveau dashboard |
| Dashboards > Gérer les dashboards | Dashboards > Parcourir tout |
| Dashboards > Gérer les rapports planifiés | Configuration de compte > Rapports planifiés |
| Dashboards > Gérer les pages de statut public | Configuration de compte > Pages de statut public |
| Alertes > Statut d'alerte actuel | Alerte > Statut d'alerte actuel |
| Alertes > Historique des alertes | Alerte > Historique des alertes |
| Alerte > Définitions d'alerte | Alerte > Définitions d'alerte |
| Alerte > Intégrations | Alertes > Intégrations |
| SLA > Vue d'ensemble SLA | Dashboards > Synthetics > Vue d'ensemble SLA |
| SLA > Définitions SLA | Configuration de compte > Définitions SLA |
| Compte > tous les menus | Configuration de compte |
| Applications et extras > Outils | Outils et applications > Outils de diagnostic |
| Applications et extras > Enregistreur de transaction | Outils et applications > Télécharger l'enregistreur de transaction OU Synthetics > Transactions > Télécharger l'enregistreur de transaction |
| Applications et extras > Applications mobiles | Outils et applications > Applications mobiles |
| Support > tous les menus | Support |
| Compteur d'erreurs non confirmées / confirmées (en haut à droite) | Badges (jaune ou rouge avec un nombre), à droite des sections Synthetics, RUM et Infra dans le menu |
| Compte utilisateur (nom), en haut à droite du menu classique | Compte utilisateur (nom), au bas du menu latéral |

## Changements dans l'interface utilisateur

Les améliorations suivantes font partie de la nouvelle interface utilisateur :

- Le menu latéral, consultez la section [Menu](#menu) pour les détails
- Des hubs, une nouvelle façon de vous présenter des informations succinctes sur la situation actuelle de surveillance, des informations générales et des liens vers des lectures complémentaires.
- La vue d'ensemble des dashboards ({{< AppElement type="menuitem" >}} Dashboards > Tous les dashboards {{< /AppElement >}}), y compris les vues miniatures, qui vous permet de parcourir et de rechercher dans tous les dashboards Synthetics, Infra, RUM et 360.
- La possibilité de marquer des dashboards comme favoris en cliquant sur le bouton en forme d'étoile {{< AppElement type="menuitem" >}}Favoris{{< /AppElement >}}, en haut à droite du dashboard lorsque ce dernier est ouvert.
- La section Favoris dans le menu Dashboards, qui vous permet d'accéder rapidement aux dashboards que vous avez marqués comme favoris.
- Une option de recherche pour retrouver les options du menu, ainsi que bien d'autres éléments d'Uptrends.
- Des sections dédiées dans le menu Synthetics pour les moniteurs de transactions, de navigateur, d'API et de disponibilité.
- L'icône engrenage {{< AppElement type="iconProperties" >}}{{< /AppElement >}} des tuiles de dashboards a été remplacée par un menu indiqué par des points de suspension {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}}.
- Une option pour les retours (dans la partie Support du menu) pour nous donner votre avis rapidement.

La page [Interface utilisateur]({{< ref path="support/kb/basics/user-interface" lang="fr" >}}) donne une description détaillée des différentes sections de l'interface utilisateur.

## Changements dans le menu {id="menu"}

Les modifications suivantes ont été apportées au nouveau menu :

- Le nouveau menu est situé sur le côté alors que le menu classique était situé en haut.
- Les trois principaux produits [Uptrends Synthetics]({{< ref path="products/synthetics/website-monitoring" lang="fr" >}}), [Uptrends Real User Monitoring]({{< ref path="products/real-user-monitoring" lang="fr" >}}) et [Uptrends Infra]({{< ref path="products/infra/server-monitoring" lang="fr" >}}) sont accessibles depuis un même menu.
- Dans Synthetics, il existe des sections dédiées pour les principaux types de moniteurs : moniteurs de transactions, moniteurs basés sur un navigateur (Full Page Check), moniteurs d'API et moniteurs de disponibilité (HTTP(S), SSL, DNS, SMTP, Ping, etc.).
- Vous pouvez réduire ou développer le menu, ce qui donne plus (ou moins) d'espace aux dashboards. Il est aussi possible d'épingler le menu.
- Les dashboards favoris s'affichent sous forme de liens rapides dans le menu {{< AppElement type="menuitem" >}}Dashboards{{< /AppElement >}}.
- Une [fonction de recherche]({{< ref path="support/kb/basics/user-interface/search" lang="fr" >}}) des options de menu et de nombreux autres éléments d'Uptrends est disponible en haut du menu latéral.
- Le regroupement des éléments de menu et leurs noms de menu a changé. Veuillez consulter le tableau [Comparaison entre les deux menus](#classic-vs-new-menu).

