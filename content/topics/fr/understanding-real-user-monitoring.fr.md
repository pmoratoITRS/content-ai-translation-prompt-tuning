{
"hero": {
"title": "Comprendre le Real User Monitoring"
},
"title": "Comprendre le Real User Monitoring",
"summary": "Cet article vous présente les grands principes du RUM et son fonctionnement. ",
"url": "/support/kb/rum/comprendre-real-user-monitoring",
"translationKey": "https://www.uptrends.com/support/kb/rum/understanding-real-user-monitoring"
}

Cert article vous présente les principes essentiels liés au RUM et à sa configuration.

## Qu'est-ce que le Real User Monitoring ?

Pour mesurer les performances ressenties par les utilisateurs réels de votre site, il n'y a pas mieux que le Real User Monitoring (RUM). Le RUM enregistre les performances des pages pour lesquelles il a été configuré, agrège les données, puis les affiche dans des dashboards interactifs où vous pouvez comparer les performances en fonction de plusieurs critères. Parmi ces critères figurent la page consultée, le périphérique, le navigateur et sa version, le système d'exploitation et sa version et l'emplacement géographique de l'utilisateur.

Le RUM est une approche passive de la surveillance, car il génère des données lorsque vos utilisateurs accèdent à votre site. Si votre site tombe en panne, vos utilisateurs ne peuvent pas y accéder et aucune donnée n'est générée. C'est là qu'intervient le monitoring synthétique ou actif. Vos [moniteurs synthétiques]({{< ref path="what-is/synthetic-monitoring" lang="fr" >}}) tels que les moniteurs de disponibilité, les moniteurs de performances, les moniteurs d'API et les moniteurs de transactions vérifient régulièrement votre site. En cas de problème, nous vous informons immédiatement en utilisant vos [paramètres d'alerte]({{< ref path="support/kb/alerting" lang="fr" >}}).

## Comment fonctionne le Real User Monitoring ?

Le fonctionnement du RUM est le suivant : vous placez un petit [script non invasif]({{< ref path="support/kb/rum/impact-of-the-rum-script-on-your-website" lang="fr" >}}) dans la section `head` des pages que vous souhaitez surveiller avec le RUM. Lorsque vos utilisateurs accèdent à une page configurée par le RUM, le script enregistre les performances de la page. Une fois le chargement de la page terminé, le script regroupe les données de performance avec des informations sur l'environnement et l'emplacement de l'utilisateur et les envoie au cloud. Uptrends récupère les données [quasiment en temps réel]({{< ref path="support/kb/rum/real-time-data" lang="fr" >}}) et les affiche dans vos dashboards RUM. Le résultat est une image complète des performances réelles de votre site telles que vécues par vos utilisateurs. Si la confidentialité vous préoccupe, veuillez lire notre article sur [le RUM et la confidentialité des utilisateurs]({{< ref path="/support/kb/rum/rum-and-user-privacy" lang="fr" >}}).

## À quoi ressemble un script de RUM ?

Nos ingénieurs ont conçu le script RUM pour qu'il soit aussi peu invasif que possible. Ce petit script se charge rapidement sans pratiquement aucun impact sur les performances de la page. Le script s’exécute en arrière-plan pendant le chargement de la page, et une fois le chargement de la page terminé, il se termine en envoyant les données utilisateur et les données de performance au cloud. Votre script ressemblera au script ci-dessous.
```js
script
var _urconfig = { sid: "9acad2af-b1f5-4438-8de6-5047a02a7ecf", aip: 0, usePageProtocol: false };
(function (d, s) {
    var js = d.createElement(s),
    sc = d.getElementsByTagName(s)[0];
    js.src = "https://hit.uptrendsdata.com/rum.min.js";
    js.async = "async";
    sc.parentNode.insertBefore(js, sc);
}(document, "script"));
/script
```
