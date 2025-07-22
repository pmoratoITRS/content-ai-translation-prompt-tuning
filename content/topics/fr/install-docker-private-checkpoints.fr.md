{
"hero": {
"title": "Installer un checkpoint Docker"
},
"title": "Installer un checkpoint Docker",
"summary": "Mettez en place un hôte Docker et des conteneurs de checkpoint pour assurer le monitoring interne de votre infrastructure réseau.",
"url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/installer-checkpoint-en-conteneur-docker",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-docker-private-checkpoints"
}

Cet article de notre base de connaissances vous explique comment configurer un serveur Windows 2022 (ou 2019) comme système d'exploitation hôte. Il vous indique aussi comment installer et activer un [checkpoint privé dans un conteneur Docker]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker#how-do-i-get-a-private-checkpoint" lang="fr" >}}).

Avant de procéder à l'installation, vérifiez que toutes les [exigences]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="fr" >}}) sont respectées. Uptrends vous fournira tous les fichiers nécessaires pour commencer.

## Script d'installation

Uptrends fournit un script d'installation que vous pouvez télécharger sous format compressé depuis le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}} de l'[application Uptrends](https://app.uptrends.com/PrivateLocations). Ce script est disponible pour chacun de vos [emplacements privés]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}) et permet d'exécuter les principales étapes d'installation. Ces étapes incluent l'installation de Docker et Docker Compose, l'extraction des images de conteneurs d'Uptrends, la configuration du démarrage et de l'actualisation, et le démarrage du checkpoint en conteneur.

## Étapes d'installation

**Voici les étapes à suivre pour installer un checkpoint au moyen du script :**

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Si vous n'avez ajouté aucun [emplacement privé]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}), cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter un emplacement {{< /AppElement >}}. Une fois l'emplacement ajouté, deux checkpoints sont ajoutés par défaut.
3. Cliquez sur le nom du checkpoint de l'emplacement privé.
4. Sélectionnez le système d'exploitation hôte requis dans le menu déroulant **Système d'exploitation hôte**.
5. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Télécharger le fichier zip d'installation {{< /AppElement >}}.

{{< callout >}} **Important :** souvenez-vous que le fichier zip téléchargé contient uniquement le checkpoint de l'emplacement privé que vous avez choisi entre les deux checkpoints par défaut. Votre fichier zip contient un nom de fichier UptrendsCheckpoints\<checkpoint-name\>.zip, où \<checkpoint-name\> est le nom de votre checkpoint. {{< /callout >}}

5. Décompressez le fichier téléchargé à l'emplacement où vous souhaitez installer le checkpoint privé.
6. Pour empêcher le téléversement des captures d'écran sur le cloud, vous devez [modifier le fichier docker-compose]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection#disable-screenshots-in-docker-compose-file" lang="fr" >}}) après avoir téléchargé et extrait les fichiers.

{{< callout >}} **Important :** Selon les politiques en vigueur dans votre entreprise, vous devrez peut-être débloquer tous les fichiers de script Powershell (*.ps1) dans le dossier .zip avant de les exécuter. Pour en savoir plus, consultez ces [instructions](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-5.1) sur le déblocage de fichiers. {{< /callout >}}

7. Ouvrez une console PowerShell et exécutez-la en tant qu'administrateur. Exécutez le script `./install-checkpoint.ps1` dans le répertoire (décompressé) Uptrends. Cette opération relance le serveur une fois. Notez que le script configure une tâche qui s'exécute toutes les heures pour vérifier l'existence de mises à jour pour les conteneurs d'Uptrends.

La sélection de checkpoints est désormais accessible dans l'onglet {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}}. Les checkpoints sont aussi visibles dans la boîte de dialogue *Voir les détails* lorsque vous effectuez un test rapide directement depuis le moniteur au moyen du bouton {{< AppElement type="buttonSecondary" >}} Tester maintenant {{< /AppElement >}}.

Pour installer des certificats dans des emplacements privés, lisez notre article [Installation de certificats dans des emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-certificates-private-locations" lang="fr" >}}).

## Surveillance de votre checkpoint privé

Uptrends apportera des changements à votre compte pour vous aider à surveiller vos checkpoints privés. Assurez-vous que tous les serveurs de checkpoints privés, le pare-feu, la connexion Internet et les autres systèmes nécessaires restent accessibles.

Pendant la configuration de votre checkpoint privé, Uptrends ajoutera des moniteurs et des configurations. Veuillez ne pas supprimer ou modifier ces changements apportés à votre compte.

Pour en savoir plus, consultez l'article de notre base de connaissances intitulé [Comment utiliser les checkpoints des emplacements privés]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="fr" >}}).