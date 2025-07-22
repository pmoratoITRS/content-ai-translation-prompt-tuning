{
"hero": {
"title": "Comment associer Uptrends et Cloudflare pour encore plus de sécurité"
},
"title": "Comment associer Uptrends et Cloudflare pour encore plus de sécurité",
"summary": "Cet article explique comment Cloudflare et Uptrends fonctionnent, et ce que vous devez prendre en compte pour les associer. ",
"url": "/support/kb/surveillance-synthetique/points-de-controle/cloudflare",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/cloudflare"
}

Vous utilisez peut-être déjà les services de Cloudflare pour sécuriser et protéger vos sites web et vos API. Si tel est le cas, vous savez déjà que Cloudflare bloque le trafic provenant d'utilisateurs malveillants qui utilisent des outils automatisés ou des bots (voire des réseaux de bots) pour accéder à des ressources sur vos sites et vos API.

Pour vérifier la légitimité des utilisateurs et bloquer les bots automatisés, Cloudflare s'appuie sur différentes technologies telles que la limitation du taux, le blocage d'adresses IP et de pays, les solutions anti-DDoS et les CAPTCHA.

Cloudflare propose aussi un service de bots vérifiés qui vous permet de préciser quels bots doivent pouvoir accéder à vos sites web et à vos API. Ainsi, vous avez l'assurance que les requêtes de ces bots sont vérifiées et autorisées, tandis que tous les autres bots sont bloqués de façon à renforcer la sécurité de vos sites.

## Uptrends est un bot vérifié

Le monitoring de disponibilité et de performance effectué par Uptrends sur vos pages web, vos parcours utilisateur et vos API est exécuté par des bots. C'est cette automatisation des processus qui nous permet d'accéder continuellement à vos serveurs web.

Uptrends est l'un des partenaires de bots vérifiés de Cloudflare. Cloudflare connaît les emplacements des checkpoints publics d'Uptrends et actualise régulièrement la liste d'adresses IP (IPv4 et IPv6) utilisées pour surveiller vos sites web.

En combinant Cloudflare et Uptrends, vous protégez les ressources sur vos sites web et vos API contre les bots malveillants, tout en permettant à Uptrends de surveiller le trafic sans être bloqué par le pare-feu de Cloudflare.

## Liste des bots vérifiés

Le service Cloudflare Radar publie la liste des [bots vérifiés](https://radar.cloudflare.com/traffic/verified-bots) par Cloudflare. Tous les services légitimes peuvent demander à figurer sur la liste de bots validés par Cloudflare.

Uptrends a suivi cette procédure et obtenu le statut de bot vérifié par Cloudflare. Toutefois, Cloudflare ne publie qu'une partie des bots vérifiés sur cette liste, et Uptrends n'y figure pas malgré l'obtention de ce statut.

## Dépannage

Même si Cloudflare a confirmé que les bots d'Uptrends disposent du statut vérifié et que les adresses IP des serveurs de checkpoints sont autorisées chez Cloudflare, il arrive que des utilisateurs d'Uptrends nous signalent des problèmes.

Si Cloudflare bloque le trafic entrant d'un des emplacements de checkpoints, votre site est présenté comme indisponible dans les résultats du monitoring.

Si vous remarquez un dysfonctionnement qui semble causé par le blocage du trafic entrant d'Uptrends par Cloudflare, veuillez suivre ces étapes :

- Reportez-vous à la documentation de Cloudflare sur la [gestion des bons bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/). Cet article explique comment fonctionnent les listes vertes et les listes de blocage, ainsi que la configuration de règles pour les bots qui accèdent au site web ou à l'application.

- Relevez les emplacements de checkpoints qui rencontrent des difficultés pour accéder à votre site ou à votre API, et ceux pour lesquels cela fonctionne. Envoyez ensuite ces informations en soumettant un ticket au [support d'Uptrends]({{< ref path="contact" lang="fr" >}}). Nous pourrons ainsi déterminer si le problème est lié aux listes d'autorisation de Cloudfare ou à une autre cause.

- Contactez l'[assistance de Cloudflare](https://dash.cloudflare.com/support) si vous avez besoin de modifier la configuration des règles de pare-feu de Cloudfare. Assurez-vous aussi de lire la documentation de Cloudflare sur les [actions liées aux règles de pare-feu](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/).

Nous collaborons activement avec Cloudflare pour résoudre ces problèmes et vos informations nous sont précieuses pour mieux comprendre la cause profonde.