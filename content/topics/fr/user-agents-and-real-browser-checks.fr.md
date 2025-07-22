{
"hero": {
"title": "Agents utilisateurs et Real Browser Checks"
},
"title": "Agents utilisateurs et Real Browser Checks",
"summary": "Les agents utilisateurs sont un excellent moyen d'effectuer des tests synthétiques sur des environnements utilisateurs spécifiques tels que les dispositifs mobiles. Cet article vous explique comment les Real Browser Checks et les agents utilisateurs peuvent vous aider.",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/agents-utilisateurs-et-real-browser-checks",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/user-agents-and-real-browser-checks"
}

Si vous avez des difficultés avec les notions d'agent utilisateur et de Real Browser Monitoring, ne vous inquiétez pas. Les agents utilisateurs et leur application au Real Browser Monitoring sont l'un des sujets les plus fréquemment traités par notre équipe de support. Voici une première réponse rapide :

Les Real Browser Checks (utilisés par les moniteurs Full Page Check et les moniteurs de transactions) utilisent un navigateur réel (tout comme les visiteurs de votre site) pour obtenir et charger le contenu de votre site web. Le navigateur génère un agent utilisateur qui informe vos serveurs sur l'environnement de votre utilisateur. L'agent utilisateur permet au serveur de renvoyer un contenu optimisé pour l'environnement défini par l'agent utilisateur. Vous pouvez manipuler l'agent utilisateur sur vos moniteurs pour tester le contenu destiné à d'autres navigateurs, systèmes d'exploitation et périphériques tels que les téléphones mobiles et les tablettes.

Si cette première réponse vous convient, c'est tant mieux. Pour aller plus loin, vous pouvez aussi poursuivre la lecture de cet article. Voyons d'abord les trois principaux composants des communications HTTP.

## Les acteurs

La communication est un chemin à double sens entre deux parties ; l'une demandant des informations et l'autre donnant des informations. C'est le langage qui permet ce transfert d'informations. Pour que les deux parties se comprennent, elles doivent utiliser le même langage. Voici les différents acteurs :

- **Client** : Le client demande quelque chose à une ressource. Le client peut être un navigateur Internet ou un autre type d'application logicielle comme un robot d'indexation web.
- **HTTP** : Le langage commun. Le protocole de transfert hypertexte définit clairement la sémantique de la communication.
- **Serveur** : Le serveur renvoie les informations au client en les personnalisant d'après l'agent utilisateur.

Un client utilise une requête HTTP pour demander des informations au serveur et le serveur renvoie les informations sous la forme d'une réponse HTTP. Alors, quel est le rapport avec les Real Browser Checks et les agents utilisateurs ? Commençons par l'agent utilisateur.

## Qu'est-ce qu'un agent utilisateur ?

Un agent utilisateur est un champ spécifique de la requête HTTP qui contient des informations sur le client. Le serveur recherche des mots spécifiques dans le texte et ignore tout le reste. Il construit le contenu optimisé pour le client selon ce qu'il trouve ou ne trouve pas dans le texte de l'agent utilisateur. L'agent utilisateur comprend les éléments suivants :

- Type de navigateur et version
- Système d'exploitation et version
- Moteur de rendu

Pour compliquer les choses, vous verrez que les agents utilisateurs incluent des informations comme, par exemple, le texte "Mozilla/5.0" (présent dans la plupart des agents utilisateurs des navigateurs) qui signale simplement au serveur que ce client est compatible avec ce navigateur.

Comme vous pouvez le voir dans l'exemple ci-dessous, l'agent utilisateur Chrome indique au serveur qu'il s'agit d'un navigateur Mozilla/5.0, d'un navigateur Safari et d'un navigateur Chrome.

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36`

## Qu'est-ce qu'un Real Browser Check ?

Comme décrit ci-dessus, un client peut être n'importe quelle application logicielle capable de communiquer sur Internet, et un navigateur Internet n'est qu'un des types de clients. Les applications logicielles pourraient se contenter de communiquer sous un format brut, mais vos utilisateurs finaux ne seraient pas ravis. Au lieu de cela, pour les utilisateurs finaux, le navigateur prend tout le contenu renvoyé, l'analyse et l'affiche visuellement à l'écran.

Vous pouvez tester votre site en utilisant un [moniteur de base ou un Real Browser Check]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="fr" >}}). Nos points de contrôle peuvent utiliser un navigateur ou s'en passer selon le type de moniteur que vous avez sélectionné. Les moniteurs HTTP et HTTPS de base génèrent une requête et l'envoient au serveur (aucun navigateur n'est utilisé). Lorsque l'ordinateur du point de contrôle reçoit la réponse, il recherche un code de résultat, parfois un contenu spécifique, et quelques autres éléments de base. La réponse n'est jamais traitée, les images ne sont jamais téléchargées et les fichiers de script ne sont jamais exécutés. Ce processus vous indique si votre site est disponible ou pas.

Lorsque vous choisissez d'effectuer la surveillance avec un véritable navigateur, nos ordinateurs de point de contrôle ouvrent une fenêtre de navigateur et envoient une requête à votre serveur, tout comme les visiteurs de votre site qui utilisent un navigateur. La réponse est reçue et traitée, les images téléchargées, les fichiers script exécutés, les fichiers CSS appliqués et la page apparaît dans la fenêtre du navigateur. Le Real Browser Check, tel qu'exécuté par le moniteur [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="fr" >}}), peut vous donner les temps de connexion et de chargement pour chaque élément de la page ainsi que tout contenu défaillant. Il effectue même une capture d'écran lorsqu'une erreur se produit sur la page.

## Alors, quelle est la différence entre les agents utilisateurs et le Real Browser Monitoring ?

Vous pouvez modifier l'agent utilisateur pour les moniteurs basés sur navigateur ou non basés sur navigateur. Vous pouvez modifier l'agent utilisateur pour les moniteurs de base si vous voulez juste vérifier un contenu spécifique dans certains environnements utilisateurs. Vous verrez que l'utilisation d'un vrai navigateur est plus puissante. En modifiant l'agent utilisateur, vous pouvez tester les performances et le contenu de la page pour presque tous les environnements utilisateurs. Regardons quelques exemples :

### Tester les versions mobiles

Le smartphone est en train de dépasser l'ordinateur de bureau en tant qu'outil préféré des utilisateurs, et il est donc extrêmement important de savoir si vos serveurs répondent rapidement et correctement avec un contenu adapté. Les tests manuels semblent souvent la seule solution pour tester les versions mobiles des sites web. Pourtant, il n'en est rien. Utiliser un agent utilisateur avec le Real Browser Check permet d'émuler n'importe quel périphérique, taille d'écran et navigateur sur mobile. Vos serveurs répondront avec le contenu pour mobile, et nos Real Browser Checks chargeront le contenu. Vous trouverez ci-dessous des agents utilisateurs pour les appareils, les systèmes d'exploitation et les navigateurs les plus répandus.

**Android Chrome**

`Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36`

**iPhone Safari**

`Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25`

**Amazon Fire**

`Mozilla/5.0 (Linux; U; Android 5.1; locale; device Build/build) AppleWebKit/webkit (KHTML, like Gecko) Version/4.0 Chrome/chrome Safari/safari`

### Tester les navigateurs non pris en charge

Actuellement, des tests natifs sont possibles avec Chrome et d'autres seront ajoutés bientôt. L'utilisation de la dernière version du navigateur natif est idéale lorsque les utilisateurs mettent régulièrement leurs navigateurs à jour, mais beaucoup d'utilisateurs ne le font pas. Alors, même si votre site fonctionne correctement avec le dernier navigateur Chrome, comment fonctionne-t-il avec les versions précédentes ? En modifiant l'agent utilisateur, vous pouvez tester n'importe quelle version du navigateur.

### Tester d'autres systèmes d'exploitation

Un navigateur Chrome s'exécutant sous Mac OSX peut fonctionner de manière très différente que le même navigateur Chrome fonctionnant sous Windows 10. La seule façon de vérifier cela correctement consiste à modifier votre agent utilisateur pour spécifier d'autres systèmes d'exploitation et d'autres versions. Si le point de contrôle emploie le navigateur natif, l'agent utilisateur utilise par défaut le système d'exploitation et la version de navigateur du point de contrôle.
