{
  "hero": {
    "title": "Checkpoints gérés par l'utilisateur (avec les conteneurs Docker)"
  },
  "title": "Checkpoints gérés par l'utilisateur (avec les conteneurs Docker)",
  "summary": "Découvrez ce qu'est un checkpoint géré par l'utilisateur et comment le monitoring d'Uptrends peut s'effectuer derrière le pare-feu de votre entreprise avec les conteneurs Docker.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/points-de-controle/emplacements-prives/checkpoints-prives-docker",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends fournit un conteneur Docker qui permet d'exécuter un checkpoint Uptrends sur votre réseau (derrière votre pare-feu). Ce checkpoint privé vous donne accès à toutes les fonctionnalités d'Uptrends, et peut effectuer des tests sur votre infrastructure privée. Grâce à l'application Uptrends, c'est vous qui choisissez où les moniteurs doivent effectuer leurs tests : en interne via votre checkpoint privé et/ou en externe via le [réseau mondial de checkpoints]([LINK_URL_1]) d'Uptrends.

![]([LINK_URL_2])

Les tests sont effectués sur votre réseau, mais toutes les autres activités comme la planification, les alertes et les rapports se produisent dans l'application cloud d'Uptrends. Uptrends conserve vos définitions de moniteurs et les données de vos tests dans ses centres de données.

Votre checkpoint privé est propre à votre compte Uptrends et ne peut être utilisé que par vous. Vous pouvez exécuter les moniteurs en interne pour vérifier vos infrastructures non reliées à Internet, comme :

- l'intranet
- les applications métier web internes
- les services web (API)
- les environnements de pré-production, par ex. l'environnement de test d'acceptation
- la disponibilité des infrastructures de base pour les serveurs de base de données, les serveurs de messagerie et les serveurs SFTP

## Comment fonctionne un checkpoint privé ?

Le checkpoint privé d'Uptrends est empaqueté dans des conteneurs Docker. Ces conteneurs sont hébergés sur votre propre réseau au moyen d'une plateforme de conteneurs. La plateforme peut être un ordinateur hôte ou une machine virtuelle. D'autres options comme Azure sont aussi disponibles. Les instructions présentées dans la rubrique [Installer un checkpoint privé Docker]([LINK_URL_3]) portent sur la création d'une machine virtuelle.

Un checkpoint privé utilise au moins deux instances de conteneurs Windows Docker qui s'exécutent sur la plateforme de conteneurs connectée à votre réseau. Ces instances ont seulement accès aux infrastructures qui doivent être surveillées, et vous devez isoler les applications Docker du reste de votre réseau. Uptrends fournit le logiciel pour utiliser ces checkpoints en conteneurs, et votre entreprise veille au bon fonctionnement du matériel et de l'infrastructure.

Le système de monitoring d'Uptrends utilise une plateforme cloud comme système centralisé de commande et de contrôle. Cette plateforme cloud conserve vos définitions de moniteurs, et décide où et quand la prochaine vérification de moniteur doit être effectuée d'après le checkpoint sélectionné. Quand vous configurez un moniteur pour utiliser un checkpoint privé, Uptrends sélectionne l'une des instances de conteneurs pour effectuer la vérification avec le moniteur. L'instance de conteneurs effectue les tests et renvoie les résultats à Uptrends. Uptrends traite et enregistre les résultats du test effectué sur votre checkpoint privé. Si Uptrends détecte une erreur, le test est immédiatement recommencé dans l'autre instance Docker. Si le moniteur détecte une erreur la deuxième fois, Uptrends envoie une alerte depuis le cloud (voir l'architecture des checkpoints privés ci-dessous).

Si votre checkpoint devient complètement indisponible, Uptrends envoie une erreur pour vous avertir. Voici deux des causes pouvant expliquer cette indisponibilité :

- Le checkpoint privé perd sa connexion à Internet.
- Toutes vos instances de conteneurs utilisent la même plateforme hôte, et cette dernière est en panne.

![]([LINK_URL_4])

1. Connectivité HTTPS sortante (avec des websockets) à la plateforme cloud de commande et de contrôle d'Uptrends, pour récupérer les définitions de moniteurs et renvoyer les résultats. La connexion sortante des websockets est utilisée pour recevoir des commandes et reste ouverte pendant une longue période. Une liste blanche est établie pour quatre emplacements d'Uptrends.
2. Connectivité HTTPS sortante pour récupérer les mises à jour des conteneurs avec les mises à jour des checkpoints et des navigateurs
3. Connectivité Internet sortante pour valider la révocation des certificats expirés
4. Connectivité provenant du checkpoint privé d'Uptrends vers l'infrastructure surveillée, avec un blocage vers tout le reste de la plateforme

## Comment acquérir un checkpoint privé ?

Pour surveiller votre infrastructure interne avec un checkpoint privé Docker, vous devez préparer l'infrastructure. Pour cela, vous devez installer des hôtes basés sur Windows Server (de préférence deux) comme expliqué dans l'article [Installer un checkpoint privé Docker]([LINK_URL_5]).

Si vous avez des questions, n'hésitez pas à nous les transmettre en ouvrant un [ticket de support]([LINK_URL_6]). Nos échanges et les décisions qui seront prises sont enregistrés dans notre système de tickets. Vous pouvez relire les discussions, ajouter des commentaires et poser des questions directement à l'ingénieur du support en charge de votre ticket.

## Précisions relatives à la sécurité

Bien qu'Uptrends applique les meilleures pratiques du secteur et prenne les mesures raisonnables pour garantir la sécurité, c'est vous qui êtes responsable des conséquences que le checkpoint privé peut avoir sur votre réseau. Nous présentons ci-dessous le partage de responsabilités entre vous et Uptrends.

### Responsabilités d'Uptrends

- Fournir des conteneurs de checkpoints privés avec un logiciel à jour
- Veiller à tenir à jour les composants logiciels utilisés dans les conteneurs (à savoir l'image et les navigateurs web)
- Chiffrer tout le trafic vers et depuis votre plateforme
- Fournir des informations pour la constitution de listes blanches

### Responsabilités de l'utilisateur

- Appliquer des règles de pare-feu pour restreindre l'accès à l'infrastructure qui doit être surveillée
- Utiliser des comptes de monitoring avec un accès limité à la plateforme (le cas échéant)
- Effectuer les contrôles antivirus nécessaires
- Appliquer les autres mesures nécessaires (p. ex. quand une transaction effectue un transfert d'argent récurrent)
- Mettre à jour l'hôte et les conteneurs Docker de préférence tous les jours, mais au moins toutes les deux semaines pour s'assurer que les versions les plus récentes des navigateurs sont utilisées et que les derniers correctifs de sécurité sont appliqués
- Veiller à tenir à jour le système d'exploitation hôte
- Au besoin, [désactiver les captures d'écran et les captures d'écran chronologiques]([LINK_URL_7]) dans les moniteurs de base et les moniteurs de navigateur.

[SHORTCODE_1] Si vous avez d'autres questions, vous pouvez consulter la [FAQ sur les checkpoints privés]([LINK_URL_8]). [SHORTCODE_2]
