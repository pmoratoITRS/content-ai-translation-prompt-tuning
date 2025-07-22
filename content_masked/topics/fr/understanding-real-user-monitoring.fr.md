{
  "hero": {
    "title": "Comprendre le Real User Monitoring"
  },
  "title": "Comprendre le Real User Monitoring",
  "summary": "Cet article vous présente les grands principes du RUM et son fonctionnement. ",
  "url": "[URL_BASE_TOPICS]rum/comprendre-real-user-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cert article vous présente les principes essentiels liés au RUM et à sa configuration.

## Qu'est-ce que le Real User Monitoring ?

Pour mesurer les performances ressenties par les utilisateurs réels de votre site, il n'y a pas mieux que le Real User Monitoring (RUM). Le RUM enregistre les performances des pages pour lesquelles il a été configuré, agrège les données, puis les affiche dans des dashboards interactifs où vous pouvez comparer les performances en fonction de plusieurs critères. Parmi ces critères figurent la page consultée, le périphérique, le navigateur et sa version, le système d'exploitation et sa version et l'emplacement géographique de l'utilisateur.

Le RUM est une approche passive de la surveillance, car il génère des données lorsque vos utilisateurs accèdent à votre site. Si votre site tombe en panne, vos utilisateurs ne peuvent pas y accéder et aucune donnée n'est générée. C'est là qu'intervient le monitoring synthétique ou actif. Vos [moniteurs synthétiques]([LINK_URL_1]) tels que les moniteurs de disponibilité, les moniteurs de performances, les moniteurs d'API et les moniteurs de transactions vérifient régulièrement votre site. En cas de problème, nous vous informons immédiatement en utilisant vos [paramètres d'alerte]([LINK_URL_2]).

## Comment fonctionne le Real User Monitoring ?

Le fonctionnement du RUM est le suivant : vous placez un petit [script non invasif]([LINK_URL_3]) dans la section [INLINE_CODE_1] des pages que vous souhaitez surveiller avec le RUM. Lorsque vos utilisateurs accèdent à une page configurée par le RUM, le script enregistre les performances de la page. Une fois le chargement de la page terminé, le script regroupe les données de performance avec des informations sur l'environnement et l'emplacement de l'utilisateur et les envoie au cloud. Uptrends récupère les données [quasiment en temps réel]([LINK_URL_4]) et les affiche dans vos dashboards RUM. Le résultat est une image complète des performances réelles de votre site telles que vécues par vos utilisateurs. Si la confidentialité vous préoccupe, veuillez lire notre article sur [le RUM et la confidentialité des utilisateurs]([LINK_URL_5]).

## À quoi ressemble un script de RUM ?

Nos ingénieurs ont conçu le script RUM pour qu'il soit aussi peu invasif que possible. Ce petit script se charge rapidement sans pratiquement aucun impact sur les performances de la page. Le script s’exécute en arrière-plan pendant le chargement de la page, et une fois le chargement de la page terminé, il se termine en envoyant les données utilisateur et les données de performance au cloud. Votre script ressemblera au script ci-dessous.
[CODE_BLOCK_1]
