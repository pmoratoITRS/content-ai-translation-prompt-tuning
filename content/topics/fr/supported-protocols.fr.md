{
  "hero": {
    "title": "Protocoles pris en charge"
  },
  "title": "Protocoles pris en charge",
"summary":"Les protocoles pris en charge par Uptrends.",
  "url": "/support/kb/surveillance-synthetique/parametres-moniteurs/protocoles-pris-en-charge",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/supported-protocols"
}

## Protocoles pris en charge

Vous vous demandez peut-être si Uptrends prend en charge les protocoles dont vous avez besoin pour surveiller vos sites, vos serveurs, vos applications web et autres services web ? **Réponse** : Mais bien sûr !

**Uptrends prend en charge** :*HTTP*, *HTTPS*, *SMTP*, *POP3*, IMAP, *Ping*, *DNS*, *FTP*, *Relier*, *SQL*, *MySQL*, et plus.

## HTTP

#### Qu'est-ce que le protocole HTTP ?

Le **protocole HTTP** est utilisé pour visualiser et interagir avec des pages web non sécurisées. C'est le type de moniteur par défaut dans Uptrends et doit être choisi lorsque vous avez besoin de vérifier une page web.

#### Comment fonctionne le protocole HTTP ?

Tout d'abord, vous devez [Ajouter un nouveau moniteur](/support/kb/demarrage) (fourni avec l'URL pour le suivi).

Puis, lorsque le moniteur s'exécute, le service Uptrends contacte l'adresse web. Il vérifie les erreurs de réseau et HTTP les plus courants, et tente de télécharger le contenu de la page web.

{{< callout >}}
**Remarque** : ce type de moniteur téléchargera uniquement le contenu HTML d'une page. Il ne télécharge pas les images, les scripts ou des éléments interactifs qui peuvent faire partie de la page. Si vous voulez vérifier le contenu complet d'une page web, nous vous suggérons d'utiliser le type de moniteur Full Page Check.
{{< /callout >}}

#### Puis-je surveiller davantage avec le protocole HTTP ?

Oui ! En plus des contrôles simples décrits ci-dessus, vous pouvez également vérifier :

**Les temps de chargement** :

Lorsque vous définissez les limites, nous vérifions que le temps total qu'il faut pour charger la page Web est dans ces limites. En d'autres termes : nous pouvons vérifier que votre page web se charge aussi rapidement que vous le souhaitez.

**La taille** :

Nous pouvons tester que la taille du contenu téléchargé est plus grand que le nombre minimal d'octets ou de caractères que vous avez spécifiés. Ceci est utile lorsque vous voulez vous assurer qu'un fichier particulier sur votre serveur web (une image générée, par exemple) n'est pas cassé ou absent.

**Le contenu** :

Uptrends peuvent vérifier qu'un mot ou une phrase est réellement présent dans le contenu de la page. Ceci est un moyen puissant de vérifier que votre page web montre le contenu correct.  
  
Choisissez un mot ou une expression qui est une partie essentielle de votre page; quelque chose qui ne sera pas visible dans le cas où il y a une erreur. Il suffit de remplir votre mot ou une phrase dans le champ de correspondance de contenu de la page.  
  
Dans certains cas, vous voudriez peut-être vérifier l'absence d'un mot. Vous pouvez le faire en précédant le mot par un point d'exclamation. Par exemple, si vous voulez que nous puissions vérifier que le mot "erreur" n'est pas présent dans le contenu, saisissez !erreur.

## HTTPS

#### Qu'est-ce que le protocole HTTPS et comment fonctionne-t-il ?

Le **protocole HTTPS** fonctionne exactement comme le protocole HTTP (voir ci-dessus), sauf qu'il ne peut être utilisé que pour vérifier une page web sécurisée par un certificat SSL.

## SMTP, POP3 et IMAP

#### Que sont les protocoles SMTP, POP3 et IMAP ?

Les **protocoles SMTP, POP3 et IMAP** sont utilisés pour se connecter aux serveurs de messagerie pour gérer le courrier électronique.

#### Comment fonctionnent les protocoles SMTP, POP3 et IMAP ?

Tout d'abord, vous devez Ajouter un nouveau moniteur, en sélectionnant le protocole SMTP, POP3 ou IMAP, et renseigner les informations IP et de port appropriées.

Puis, lorsque le moniteur s'exécute, le service Uptrends essaiera de contacter l'adresse IP. S'il y parvient, un début de disponibilité est enregistré.

{{< callout >}}
**Remarque** : Si vous choisissez d'ajouter un nom d'utilisateur et un mot de passe (les informations de connexion à votre serveur de messagerie, en option), le service Uptrends tente également de se connecter dans le cadre de son test.
{{< /callout >}}

## Ping

#### Qu'est-ce que le protocole Ping ?

**Ping** (ou ICMP) est un moyen très simple pour voir si un serveur est toujours en cours d'exécution et accessible.

#### Comment fonctionne le protocole Ping ?

Le protocole ping fonctionne en envoyant des requêtes appelées ICMP Echo et mesure combien de temps il faut pour atteindre le serveur. Vous pouvez choisir cette option si vous ne disposez pas d'autres services en cours d'exécution sur le serveur et accessibles par Internet (web, base de données ou courrier).

{{< callout >}}
**Remarque** : Vos paramètres réseau ou serveur doivent autoriser explicitement les requêtes ICMP.
{{< /callout >}}

## DNS

#### Qu'est-ce que le protocole DNS ?

Le **protocole DNS** permet de surveiller l'état de disponibilité de l'infrastructure qui fournit à vos utilisateurs un moyen simple d'atteindre l'adresse de votre site web. (Par exemple : www.uptrends.com plutôt qu'une adresse IP)
  
Uptrends est capable de surveiller les DNS de type local, principal et spécifique.

#### Comment fonctionne le protocole DNS ?

Tout d'abord, connectez-vous, ajoutez un moniteur (DNS), et configurez-le en utilisant l'adresse du serveur DNS (nom de domaine ou IP), le numéro de port, type de requête DNS, la valeur de test et le résultat attendu.

La vérification la plus courante consiste à savoir si votre nom de domaine (www\.yourcompany.com) pointe toujours à l'adresse IP de votre serveur web. Si ce n'est pas le cas, les utilisateurs seront probablement pas en mesure de trouver votre site Web. En surveillant cette requête DNS directement, le service Uptrends détecte les problèmes de DNS avant même que votre site devient inaccessible aux utilisateurs.

Le moniteur DNS Uptrends vous permet de faire de nombreuses contrôles de bon fonctionnement de DNS : vérifiez vos noms de domaine (enregistrements A et CNAME), les noms de domaine des serveurs de messagerie (enregistrements MX), délégués de zone DNS (enregistrements NS), des informations faisant autorité sur les zones DNS (enregistrements SOA) et d'autres informations DNS contenues dans des enregistrements au format TXT (y compris les informations SPF pour l'authentification par e-mail).

## FTP

#### Qu'est-ce que le protocole FTP ?

Le **protocole FTP** vous permet de surveiller la disponibilité de votre serveur FTP via le port de votre choix.

#### Comment fonctionne le protocole FTP ?

Pour que le protocole FTP fonctionne, vous devez d'abord vous connecter et ajouter un moniteur (FTP) en renseignant les informations appropriées.  
  
Le service Uptrends contactera ensuite régulièrement le serveur FTP via le port approprié surveillant son statut pour assurer qu'il est opérationnel.

{{< callout >}}
**Remarque** : Il est possible d'ajouter des informations de connexion au moniteur afin de pouvoir savoir que les connexions FTP fonctionnent. Cependant, vous ne pouvez pas actuellement récupérer des fichiers à partir dudit serveur avec le service Uptrends.
{{< /callout >}}

## Connect

Si aucun autre protocole n'est adapté à votre situation, vous pouvez utiliser le **protocole Connect** pour faire un test très simple. Si vous spécifiez un nom de domaine ou une adresse IP de votre serveur ou pare-feu, ainsi qu'un numéro de port, nous tenterons d'établir une simple connexion à cette combinaison d'adresse et de port.

## SQL

#### Qu'est-ce que le protocole SQL ?

Le **protocole SQL** vous permet de surveiller la disponibilité de votre base de données Microsoft SQL.

{{< callout >}}
**Remarque :** les serveurs SQL ne peuvent être surveillées que si elles sont directement (et régulièrement) accessibles par Internet.
{{< /callout >}}

#### Comment fonctionne le protocole SQL ?

Afin de faire exécuter un moniteur de surveillance SQL, vous devez d'abord vous connecter et ajouter un moniteur SQL à votre compte. Au minimum, vous devez spécifier l'adresse IP du serveur et un numéro de port (par défaut 1433).  
  
Le service Uptrends tentera alors de communiquer avec le serveur en question, rendant un rapport positif si tout est OK, sinon déclenchant une erreur non confirmée (et sera peut-être confirmé plus tard) s'il est inaccessible.

{{< callout >}}
**Remarque** : Vous pouvez spécifier un nom d'utilisateur et un mot de passe pour tester votre connexion, ainsi qu'un nom de base de données afin que nous puissions vérifier si la base de données est accessible.
{{< /callout >}}

## MySQL

#### Qu'est-ce que le protocole MySQL ?

Le **protocole MySQL** permet à l'application Uptrends de surveiller la disponibilité des bases de données MySQL.

#### Comment fonctionne le protocole MySQL ?

Le protocole MySQL fonctionne de la même manière que le protocole SQL, mais avec des bases de données MySQL ! (Le numéro de port par défaut pour la connexion à des bases de données MySQL est 3306.)
