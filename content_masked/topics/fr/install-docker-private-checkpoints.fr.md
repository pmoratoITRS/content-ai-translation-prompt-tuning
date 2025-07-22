{
  "hero": {
    "title": "Installer un checkpoint Docker"
  },
  "title": "Installer un checkpoint Docker",
  "summary": "Mettez en place un hôte Docker et des conteneurs de checkpoint pour assurer le monitoring interne de votre infrastructure réseau.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/installer-checkpoint-en-conteneur-docker",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cet article de notre base de connaissances vous explique comment configurer un serveur Windows 2022 (ou 2019) comme système d'exploitation hôte. Il vous indique aussi comment installer et activer un [checkpoint privé dans un conteneur Docker]([LINK_URL_1]).

Avant de procéder à l'installation, vérifiez que toutes les [exigences]([LINK_URL_2]) sont respectées. Uptrends vous fournira tous les fichiers nécessaires pour commencer.

## Script d'installation

Uptrends fournit un script d'installation que vous pouvez télécharger sous format compressé depuis le menu [SHORTCODE_5] Emplacements privés [SHORTCODE_6] de l'[application Uptrends]([LINK_URL_3]). Ce script est disponible pour chacun de vos [emplacements privés]([LINK_URL_4]) et permet d'exécuter les principales étapes d'installation. Ces étapes incluent l'installation de Docker et Docker Compose, l'extraction des images de conteneurs d'Uptrends, la configuration du démarrage et de l'actualisation, et le démarrage du checkpoint en conteneur.

## Étapes d'installation

**Voici les étapes à suivre pour installer un checkpoint au moyen du script :**

1. Ouvrez le menu [SHORTCODE_7] Emplacements privés [SHORTCODE_8].
2. Si vous n'avez ajouté aucun [emplacement privé]([LINK_URL_5]), cliquez sur le bouton [SHORTCODE_9] Ajouter un emplacement [SHORTCODE_10]. Une fois l'emplacement ajouté, deux checkpoints sont ajoutés par défaut.
3. Cliquez sur le nom du checkpoint de l'emplacement privé.
4. Sélectionnez le système d'exploitation hôte requis dans le menu déroulant **Système d'exploitation hôte**.
5. Cliquez sur le bouton [SHORTCODE_11] Télécharger le fichier zip d'installation [SHORTCODE_12].

[SHORTCODE_1] **Important :** souvenez-vous que le fichier zip téléchargé contient uniquement le checkpoint de l'emplacement privé que vous avez choisi entre les deux checkpoints par défaut. Votre fichier zip contient un nom de fichier UptrendsCheckpoints\[HTML_TAG_1].zip, où \[HTML_TAG_2] est le nom de votre checkpoint. [SHORTCODE_2]

5. Décompressez le fichier téléchargé à l'emplacement où vous souhaitez installer le checkpoint privé.
6. Pour empêcher le téléversement des captures d'écran sur le cloud, vous devez [modifier le fichier docker-compose]([LINK_URL_6]) après avoir téléchargé et extrait les fichiers.

[SHORTCODE_3] **Important :** Selon les politiques en vigueur dans votre entreprise, vous devrez peut-être débloquer tous les fichiers de script Powershell (*.ps1) dans le dossier .zip avant de les exécuter. Pour en savoir plus, consultez ces [instructions]([LINK_URL_7]) sur le déblocage de fichiers. [SHORTCODE_4]

7. Ouvrez une console PowerShell et exécutez-la en tant qu'administrateur. Exécutez le script [INLINE_CODE_1] dans le répertoire (décompressé) Uptrends. Cette opération relance le serveur une fois. Notez que le script configure une tâche qui s'exécute toutes les heures pour vérifier l'existence de mises à jour pour les conteneurs d'Uptrends.

La sélection de checkpoints est désormais accessible dans l'onglet [SHORTCODE_13] Checkpoints [SHORTCODE_14]. Les checkpoints sont aussi visibles dans la boîte de dialogue *Voir les détails* lorsque vous effectuez un test rapide directement depuis le moniteur au moyen du bouton [SHORTCODE_15] Tester maintenant [SHORTCODE_16].

Pour installer des certificats dans des emplacements privés, lisez notre article [Installation de certificats dans des emplacements privés]([LINK_URL_8]).

## Surveillance de votre checkpoint privé

Uptrends apportera des changements à votre compte pour vous aider à surveiller vos checkpoints privés. Assurez-vous que tous les serveurs de checkpoints privés, le pare-feu, la connexion Internet et les autres systèmes nécessaires restent accessibles.

Pendant la configuration de votre checkpoint privé, Uptrends ajoutera des moniteurs et des configurations. Veuillez ne pas supprimer ou modifier ces changements apportés à votre compte.

Pour en savoir plus, consultez l'article de notre base de connaissances intitulé [Comment utiliser les checkpoints des emplacements privés]([LINK_URL_9]).