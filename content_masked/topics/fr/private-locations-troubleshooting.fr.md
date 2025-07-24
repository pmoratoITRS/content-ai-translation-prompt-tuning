{
  "hero": {
    "title": "Résolution des problèmes liés aux emplacements privés"
  },
  "title": "Résolution des problèmes liés aux emplacements privés",
  "summary": "Indications et exemples relatifs à la résolution des problèmes liés aux emplacements privés",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/depannage-problemes-emplacements-prives",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

L'installation d'un emplacement privé est entièrement automatisée. Une fois qu'elle est effectuée, vous disposez d'un checkpoint en conteneurs actif, qui s'actualise automatiquement et effectue des mesures pour les moniteurs. Le présent article décrit les étapes à suivre pour [vérifier l'installation de votre emplacement privé]([LINK_URL_1]), [réaliser un test de fumée de votre configuration]([LINK_URL_2]) et [résoudre]([LINK_URL_3]) les problèmes qui peuvent survenir pendant ou après l'installation.

## Vérifier l'installation de l'emplacement privé

La première étape consiste à vérifier si votre emplacement privé est correctement [installé et configuré]([LINK_URL_4]). Le package d'installation automatisé est préconfiguré et se compose de trois étapes.

- Installation des prérequis (pouvant nécessiter un redémarrage)
- Extraction des images de conteneurs d'Uptrends depuis Azure
- Installation des tâches d'exécution et d'actualisation automatiques


### Installation des prérequis
Pour exécuter les images de conteneurs d'Uptrends, trois prérequis doivent être installés : la fonctionnalité Windows "Containers", Docker Engine et Docker Compose. L'installation de la fonctionnalité Windows "Containers" peut nécessiter un redémarrage. Un message s'affichera le cas échéant. L'installation continuera automatiquement après ce redémarrage (au moyen d'une tâche planifiée).

Si vous souhaitez vérifier que ces trois éléments sont installés correctement, vous pouvez exécuter les commandes suivantes.

Tout d'abord, affichez la liste des fonctionnalités Windows et vérifiez que cette liste contient l'entrée "Containers".
1. Ouvrez une console PowerShell en mode admin.
2. Ouvrez le dossier où se trouve le fichier docker-compose.yml file et exécutez la commande suivante : `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4][INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7][INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10][INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13][INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16][INLINE_CODE_17][INLINE_CODE_18][INLINE_CODE_19][INLINE_CODE_20][INLINE_CODE_21][INLINE_CODE_22][INLINE_CODE_23][INLINE_CODE_24][INLINE_CODE_25][INLINE_CODE_26]docker-compose up -d[INLINE_CODE_27]docker-compose down[INLINE_CODE_28]docker-compose restart[INLINE_CODE_29][INLINE_CODE_30][INLINE_CODE_31][INLINE_CODE_32][INLINE_CODE_33][INLINE_CODE_34][INLINE_CODE_35][INLINE_CODE_36][INLINE_CODE_37][INLINE_CODE_38][INLINE_CODE_39]Docker-compose logs -t -n 5000[INLINE_CODE_40][INLINE_CODE_41][INLINE_CODE_42][INLINE_CODE_43][INLINE_CODE_44][INLINE_CODE_45][INLINE_CODE_46][INLINE_CODE_47][INLINE_CODE_48][INLINE_CODE_49][INLINE_CODE_50][INLINE_CODE_51][INLINE_CODE_52][INLINE_CODE_53][INLINE_CODE_54][INLINE_CODE_55][INLINE_CODE_56][INLINE_CODE_57][INLINE_CODE_58][INLINE_CODE_59][INLINE_CODE_60][INLINE_CODE_61][INLINE_CODE_62][INLINE_CODE_63]`. Si cela fonctionne correctement quand vous n'utilisez pas l'adresse IP du DNS public, mais que vous rencontrez des problèmes en son absence, il peut y avoir un problème au niveau de la résolution DNS. Notez que l'utilisation de 8.8.8.8 comme serveur DNS en production n'est pas souhaitable car cela ne permet pas de résoudre les applications internes.

Spécifiez un ou des serveurs DNS spécifiques dans le fichier compose, comme indiqué dans le code ci-dessous. Souvenez-vous de répéter la manœuvre pour les deux conteneurs dans le fichier yaml.

[CODE_BLOCK_4]

Indiquez les adresses IP des serveurs DNS que vous souhaitez utiliser. Vous pouvez les tester avec la commande probemaster1.uptrends.com, ainsi que le nom d'hôte au moyen de nslookup. Souvenez-vous de faire cette manœuvre depuis l'intérieur du conteneur.

Vous pouvez avoir besoin d'autoriser les requêtes DNS qui proviennent des conteneurs Docker, si vos serveurs DNS utilisent une liste d'autorisation. Si vous exécutez des checkpoints en conteneur sur une plateforme cloud comme Google Cloud, AWS ou Azure, une configuration plus avancée peut être nécessaire pour assurer la connectivité depuis les conteneurs Docker.

## Cela ne fonctionne toujours pas ?

À toute étape du processus de dépannage, si vous avez un doute ou une question, n'hésitez pas à solliciter Uptrends en ouvrant un [ticket de support]([LINK_URL_14]). Nous vous recontacterons rapidement.