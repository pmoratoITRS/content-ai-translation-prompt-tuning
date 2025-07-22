{
"hero": {
"title": "Résolution des problèmes liés aux emplacements privés"
},
"title": "Résolution des problèmes liés aux emplacements privés",
"summary": "Indications et exemples relatifs à la résolution des problèmes liés aux emplacements privés",
"url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/depannage-problemes-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting"
}

L'installation d'un emplacement privé est entièrement automatisée. Une fois qu'elle est effectuée, vous disposez d'un checkpoint en conteneurs actif, qui s'actualise automatiquement et effectue des mesures pour les moniteurs. Le présent article décrit les étapes à suivre pour [vérifier l'installation de votre emplacement privé](#verify-private-location-installation), [réaliser un test de fumée de votre configuration](#smoke-test-your-setup) et [résoudre](#how-to-troubleshoot) les problèmes qui peuvent survenir pendant ou après l'installation.

## Vérifier l'installation de l'emplacement privé

La première étape consiste à vérifier si votre emplacement privé est correctement [installé et configuré]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="fr" >}}). Le package d'installation automatisé est préconfiguré et se compose de trois étapes.

- Installation des prérequis (pouvant nécessiter un redémarrage)
- Extraction des images de conteneurs d'Uptrends depuis Azure
- Installation des tâches d'exécution et d'actualisation automatiques


### Installation des prérequis
Pour exécuter les images de conteneurs d'Uptrends, trois prérequis doivent être installés : la fonctionnalité Windows "Containers", Docker Engine et Docker Compose. L'installation de la fonctionnalité Windows "Containers" peut nécessiter un redémarrage. Un message s'affichera le cas échéant. L'installation continuera automatiquement après ce redémarrage (au moyen d'une tâche planifiée).

Si vous souhaitez vérifier que ces trois éléments sont installés correctement, vous pouvez exécuter les commandes suivantes.

Tout d'abord, affichez la liste des fonctionnalités Windows et vérifiez que cette liste contient l'entrée "Containers".
1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez la commande suivante : ``Get-WindowsFeature | Where-Object {$_. installstate -eq "installed"}``.
3. Vérifiez si cette liste contient l'entrée "Containers".

Ensuite, vérifiez la sortie concernant la version de Docker.
1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez la commande suivante ``Docker -v``.
3. Le résultat doit indiquer "Docker version 23.0.3, build 3e7cbfd".

Pour terminer, vérifiez la sortie concernant la version de Docker Compose.
1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez la commande suivante ``Docker-compose -v``.
3. Le résultat doit indiquer "Docker Compose version v2.17.2".

Si quelque chose vous semble anormal, vous pouvez vous référer au script d'installation, install-checkpoint.ps1, et exécuter manuellement les parties correspondant aux composants ci-dessus, puis examiner la sortie.

### Images de conteneurs
Si les trois prérequis ci-dessus sont en place, le [script d'installation]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="fr" >}}) lancera l'extraction des images de conteneurs d'Uptrends depuis Azure. Ces images sont volumineuses car chacune comprend une installation compressée de Windows Server. Selon le débit du réseau, le téléchargement peut prendre au moins quelques minutes (et dure couramment 20 minutes). Les téléchargements sont plus rapides lors des actualisations ultérieures car des parties des images sont réutilisées. Une fois le téléchargement effectué, vous pouvez procéder à une vérification en [exécutant](#managing-running-containers) : ``docker images``. Trois entrées doivent s'afficher.

L'extraction des images sollicite le fonctionnement interne de Docker. Il s'agit d'un processus robuste qui peut entraîner des défaillances dans les connexions. Si le téléchargement échoue complètement, la cause la plus probable est qu'un pare-feu (local) empêche Docker d'accéder au référentiel de conteneurs Azure via le site azurecr.io, hébergé par Microsoft.

Pour réaliser l'authentification lors de l'extraction des images, le script d'installation enregistrera les identifiants via la connexion Docker. En cas de problèmes d'authentification, vous pouvez naviguer jusqu'au répertoire d'installation (le dossier qui contient le script install-checkpoint.ps1) et exécuter ces commandes dans PowerShell pour :

Effacer les identifiants existants :
``Docker logout``

Réexécuter registry-login.ps1 et examiner la sortie de la commande :
``.\registry-login.ps1``

### Auto-exécution et auto-actualisation
Pour assurer le fonctionnement continu des checkpoints en conteneurs, une tâche planifiée est créée afin d'exécuter le script start-containers.ps1 après le lancement du serveur. Pour [actualiser]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-update-containers" lang="fr" >}}) les images Docker de conteneurs d'Uptrends, une seconde tâche planifiée est créée afin de vérifier régulièrement si des images doivent être actualisées. Reportez-vous à la sortie de la commande PowerShell ``Get-ScheduledTask`` pour vérifier si ces tâches existent. Ces tâches sont nommées "Start Checkpoint Containers" et "Update Checkpoint Images".

Vous pouvez utiliser l'interface utilisateur du Planificateur de tâches de Windows pour examiner les tâches, parcourir l'historique et les défaillances ou activer manuellement la tâche pour résoudre le problème. Comme précédemment, en cas de problème, utilisez le script d'installation (install-checkpoint.ps1) pour réexécuter manuellement cette partie de l'installation.

### Configuration
Toute la configuration relative aux serveurs se trouve dans le fichier de configuration Docker-compose.yml. Ce fichier répertorie les trois images de conteneurs et leurs paramètres individuels. Lors du téléchargement, il est prérempli avec tous les paramètres nécessaires. Une information particulièrement importante : la combinaison ``ServerId/Password`` doit être configurée pour les trois images de conteneurs répertoriées dans le fichier (la même combinaison d'identifiants est répétée trois fois dans le fichier yml, avec les mêmes valeurs).

{{< callout >}} Les valeurs *ServerId* et *Password* sont spécifiques à chaque checkpoint en conteneurs. Les différents serveurs de checkpoints en conteneurs ne peuvent jamais avoir le même *ServerId*.
{{< /callout >}}

Le fichier Docker Compose peut être utilisé pour configurer des politiques de [protection de données]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}) spécifiques à un checkpoint, et des [règles DNS propres à l'environnement](#dns-issues).

### État actuel
Les conteneurs des trois images se lancent après l'installation et doivent fonctionner de façon continue. Vous pouvez consulter leur état avec la commande ``docker ps`` et vérifier dans la colonne la plus à droite si les conteneurs fonctionnent bien. En cas de problème, utilisez les commandes ci-dessous pour affiner le diagnostic au moyen des fichiers journaux :


- Obtenir l'état actuel de tous les conteneurs
   ``Docker ps``

- Obtenir les fichiers journaux pour le conteneur de l'agent de checkpoints et les enregistrer dans un fichier texte
   ``Docker logs Checkpoint | Out-File Docker_CS.txt``

- Obtenir les fichiers journaux pour le conteneur de traitement des transactions et les enregistrer dans un fichier texte
   ``Docker logs Checkpoint | Out-File Docker_CS.txt``

- Obtenir les fichiers journaux combinés pour tous les conteneurs
   ``Docker-compose logs -t -n 5000 | Out-File Docker.txt``

## Réaliser un test de fumée de votre configuration

Une fois que les checkpoints en conteneurs sont installés, ils sont immédiatement disponibles pour effectuer des mesures. Les processus internes d'Uptrends modifient automatiquement l'état de maintenance d'un checkpoint en conteneurs, selon son état. Un checkpoint en bon état de fonctionnement est marqué comme actif, tandis qu'un checkpoint présentant un problème est marqué comme étant en maintenance.

L'état des checkpoints est actualisé toutes les minutes. Vous pouvez aussi activer ou [désactiver]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use#disable-a-private-checkpoint" lang="fr" >}}) des checkpoints (par exemple, lors d'une opération de maintenance ou d'un test de configuration) depuis l'interface des emplacements privés dans l'application web d'Uptrends. Par défaut, leur état est "activé".

Pour réaliser un test de fumée sur un checkpoint en conteneurs, la méthode la plus pratique consiste à utiliser le bouton {{< AppElement type="buttonSecondary" >}} Tester maintenant {{< /AppElement >}}. Idéalement, le test doit être effectué pour chaque type de moniteur que vous souhaitez exécuter au moyen de ce checkpoint.

Vous pouvez utiliser l'onglet [Santé du point de contrôle]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="fr" >}}) des emplacements privés pour établir un diagnostic sur les checkpoints présentant un problème.

À noter que toutes les mesures sont effectuées "à l'intérieur" du conteneur. Aucun navigateur n'est lancé sur la machine hôte lorsque vous utilisez le bouton {{< AppElement type="buttonSecondary" >}} Tester maintenant {{< /AppElement >}} pour un moniteur FPC ou un moniteur de transaction.

Notez également que lorsque vous ajoutez un checkpoint à un emplacement privé existant faisant partie de la sélection de checkpoints des moniteurs actifs, le nouveau checkpoint commence à effectuer les mesures une fois l'installation terminée. Si ce n'est pas souhaité (par exemple, si vous préférez le tester d'abord), vous devez désactiver le checkpoint dans la section des emplacements privés d'Uptrends.


## Résoudre les problèmes

### Interrompre, démarrer ou redémarrer un ensemble de conteneurs
Redémarrez les conteneurs associés au fichier Docker-compose.yaml dans le répertoire actuel. Il s'agit souvent du dossier C:\uptrends\ :

1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez une ou plusieurs des commandes suivantes.
- Pour démarrer le contenu, saisissez `docker-compose up -d` dans la ligne de commande.
- Pour interrompre un conteneur, saisissez `docker-compose down` dans la ligne de commande.
- Pour redémarrer un conteneur, saisissez `docker-compose restart` dans la ligne de commande.


{{< callout >}} **Astuce :** utilisez l'aide de Docker. Vous pouvez en savoir plus sur chaque commande au moyen de la commande *docker - -help*. Cette commande affiche toutes les commandes assorties d'une aide générale. Pour obtenir de l'aide sur une commande spécifique, vous pouvez aussi saisir *docker image - -help*.{{< /callout >}}


### Gérer les conteneurs en fonctionnement
Pour obtenir une liste de tous les conteneurs en fonctionnement, exécutez la commande ``docker ps``. Vous y trouverez un identifiant "containerId" qui pourra être utilisé dans d'autres commandes liées à ce conteneur.

Pour obtenir une liste de toutes les images locales, exécutez la commande ``docker images``

Les images peuvent devenir assez volumineuses. Pour libérer de l'espace, vous pouvez utiliser la commande ``docker image prune``, qui supprime les images qui ne sont plus utilisées par des conteneurs actifs. Vous pouvez aussi utiliser la commande ``docker image rm <containerid>`` pour retirer un conteneur spécifique.

### Retirer des objets Docker inutilisés

Le [script d'installation d'Uptrends pour les emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="fr" >}}) ne prévoit pas de nettoyage automatique des objets Docker inutilisés. Pour retirer des objets Docker non utilisés, reportez-vous à la documentation sur le [nettoyage des objets Docker inutilisés](https://docs.docker.com/engine/manage-resources/pruning). Si vous utilisez d'autres plateformes, comme Kubernetes, veuillez vous reporter à leur documentation officielle.

### Obtenir l'accès commande/shell à l'intérieur du conteneur
Exécutez cette commande pour démarrer un processus PowerShell ou un processus de commande depuis l'intérieur du conteneur. Cela vous permet d'accéder rapidement au système de fichiers depuis les conteneurs. Utilisez les commandes ```Docker exec -i checkpoint powershell``` ou ```Docker exec -i checkpoint cmd```.

Vous ne savez pas si vous êtes à l'intérieur ou à l'extérieur d'un conteneur ? Saisissez ``winver`` dans l'invite de commande de Windows. Si vous êtes à l'intérieur du conteneur, vous verrez ceci :

```winver : The term 'winver' is not recognized```

Si vous êtes sur l'hôte, la fenêtre contextuelle **About Windows** s'affichera.
Pour sortir du PowerShell ou de la session de commandes depuis le conteneur et revenir à l'hôte, utilisez la commande Ctrl+C.

### Lire la sortie du fichier journal

1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez l'une des commandes suivantes.
- Pour consulter la sortie du journal, saisissez `Docker-compose logs -t -n 5000` dans la ligne de commande.
- Pour envoyer cette sortie dans un fichier containerlogs.log, saisissez ``Docker-compose logs -t -n 5000 > containerlogs.log``

### Réseau
Au démarrage, Docker crée un réseau virtuel sur l'hôte auquel les conteneurs sont associés, et obtient une adresse IP.
Vous pouvez afficher les réseaux existants dans PowerShell avec la commande ``docker network ls`` et un réseau spécifique avec la commande ``docker network inspect <<network name>>``. Pour trouver le réseau associé à un conteneur, utilisez la commande ``docker inspect <<container name>>`` (et ``docker ps`` pour trouver les noms des conteneurs).

Les trois conteneurs Docker d'Uptrends (Checkpoint, CheckpointRelay et TransactionProcessor) doivent pouvoir se connecter à Uptrends via les commandes probemaster1.uptrends.com et probemaster2.uptrends.com. Les conteneurs Checkpoint et CheckpointRelay doivent pouvoir se connecter aux applications clients testées.

### Problèmes liés au DNS

Les problèmes de connectivité sont souvent liés à la résolution DNS. Pour les résoudre, vous pouvez suivre ces étapes :

1. Sur l'hôte, ``nslookup probemaster1.uptrends.com`` doit renvoyer 95.211.70.204. Si ce n'est pas le cas, les conteneurs ne pourront pas se connecter à Uptrends.

2. Après avoir vérifié que les conteneurs fonctionnent (au moyen de la commande ``docker ps``), ouvrez une session PowerShell dans un conteneur : ``docker exec -i Checkpoint powershell.exe``.

3. Une fois dans le conteneur, ``nslookup probemaster1.uptrends.com`` doit à nouveau renvoyer 95.211.70.204. Si c'est le cas, le conteneur doit pouvoir se connecter à la plateforme cloud d'Uptrends.

4. Essayez la même manœuvre pour un nom d'hôte d'une application interne, comme ``nslookup <<name application>>``, et vérifiez l'adresse IP renvoyée. Une fois le délai atteint, l'application n'est plus atteignable depuis le conteneur (et ne peut donc pas être surveillée).

Si l'une de ces étapes échoue, vous pouvez essayer l'action suivante :

- Comparez ipconfig depuis l'hôte et depuis l'intérieur d'un conteneur (``docker exec -i Checkpoint powershell.exe`` pour obtenir une session PowerShell dans le conteneur de checkpoints) et vérifiez le ou les serveurs DNS configurés.

Essayez de spécifier un DNS public comme 8.8.8.8 (Google) lors de l'exécution de la commande nslookup comme ceci : ``nslookup probemaster1.uptrends.com 8.8.8.8``. Si cela fonctionne correctement quand vous n'utilisez pas l'adresse IP du DNS public, mais que vous rencontrez des problèmes en son absence, il peut y avoir un problème au niveau de la résolution DNS. Notez que l'utilisation de 8.8.8.8 comme serveur DNS en production n'est pas souhaitable car cela ne permet pas de résoudre les applications internes.

Spécifiez un ou des serveurs DNS spécifiques dans le fichier compose, comme indiqué dans le code ci-dessous. Souvenez-vous de répéter la manœuvre pour les deux conteneurs dans le fichier yaml.

```yaml
TransactionProcessor:
    container_name: TransactionProcessor
    image: uptrends.azurecr.io/win2022/transaction-processor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: local
    environment:
      - ServerId=
      - Password=
    dns:
      - 1.2.3.4
      - 2.3.4.5
```

Indiquez les adresses IP des serveurs DNS que vous souhaitez utiliser. Vous pouvez les tester avec la commande probemaster1.uptrends.com, ainsi que le nom d'hôte au moyen de nslookup. Souvenez-vous de faire cette manœuvre depuis l'intérieur du conteneur.

Vous pouvez avoir besoin d'autoriser les requêtes DNS qui proviennent des conteneurs Docker, si vos serveurs DNS utilisent une liste d'autorisation. Si vous exécutez des checkpoints en conteneur sur une plateforme cloud comme Google Cloud, AWS ou Azure, une configuration plus avancée peut être nécessaire pour assurer la connectivité depuis les conteneurs Docker.

## Cela ne fonctionne toujours pas ?

À toute étape du processus de dépannage, si vous avez un doute ou une question, n'hésitez pas à solliciter Uptrends en ouvrant un [ticket de support]({{< ref path="contact" lang="fr" >}}). Nous vous recontacterons rapidement.