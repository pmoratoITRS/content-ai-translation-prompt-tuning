{
  "hero": {
    "title": "FTP et SFTP"
  },
  "title": "FTP et SFTP",
  "summary": "Toutes les infos sur le paramétrage de la surveilance et la supervision des protocoles FTP et SFTP avec le monitoring d'Uptrends.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/uptime-monitoring/ftp-et-sftp",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Vos clients comptent sur la disponibilité de vos services FTP (protocole de transfert de fichiers) et SFTP (protocole de transfert de fichiers sécurisé) pour télécharger des fichiers à partir de votre serveur sur leur ordinateur. Les types de moniteurs FTP et SFTP vérifient la disponibilité de vos serveurs et signalent tout temps d'arrêt. Vos options dépendent de votre choix de moniteur FTP ou SFTP.

## Quelles actions puis-je effectuer avec un moniteur FTP ?

Le moniteur FTP de base vérifie :

-   **Disponibilité et vitesse**  
    En cochant les cases **Limites de performance** sur l'onglet [SHORTCODE_3]Conditions d'erreur[SHORTCODE_4] vous serez en mesure de vérifier que votre serveur FTP répond rapidement aux demandes des utilisateurs.
-   **Authentification basique du serveur**  
    Vérifiez que votre processus d'authentification de base fonctionne correctement en fournissant un **Nom d'utilisateur** et un **Mot de passe** sur l'onglet [SHORTCODE_5]Avancé[SHORTCODE_6].

## Quelles actions puis-je effectuer avec un moniteur SFTP ?

Le moniteur SFTP utilise une connexion cryptée pour effectuer le transfert de fichiers. Le moniteur SFTP propose une gamme d'options de test plus large que celle du moniteur FTP. Le moniteur SFTP peut effectuer différentes actions. Avec l'onglet Avancé, choisissez parmi :

-   **Se connecter à un serveur SFTP avec un nom d'utilisateur et un mot de passe.**   
    Le moniteur se connecte au serveur SFTP avec le nom d'utilisateur et le mot de passe que vous spécifiez. Le moniteur signalera une erreur si le serveur n'est pas disponible ou si une erreur se produit lors de la connexion.
-   **Tester si un fichier existe sur le serveur SFTP.**   
    Dans ce mode, le moniteur va d'abord se connecter au serveur SFTP puis vérifier si un fichier spécifique existe sur le serveur.
-   **Tester si un fichier n'existe pas sur le serveur SFTP.**   
    Parfois il est nécessaire de savoir si un fichier spécifique n'existe pas sur le serveur SFTP. Vous pouvez choisir cette action dans les propriétés du moniteur SFTP.
-   **Télécharger un fichier à partir du serveur SFTP.**  
    Dans ce mode, le moniteur va d'abord se connecter au serveur SFTP, vérifier si un fichier spécifique existe sur le serveur, puis télécharger le fichier. La taille maximale du fichier à télécharger est 1Mo.

## Comment configurer un moniteur (S)FTP ?

Le protocole SFTP (Secure File Transfer Protocol) est le protocole standard pour le transfert de fichiers. Ce protocole est utilisé pour transférer des fichiers entre deux ordinateurs en toute sécurité. Uptrends vous permet de surveiller votre serveur SFTP pour vérifier son état de sécurité et son bon fonctionnement.

Pour créer un moniteur (S)FTP :

1. Cliquez sur le bouton + dans le menu [SHORTCODE_7] Surveillance > Configuration du moniteur [SHORTCODE_8].
2. Dans la fenêtre contextuelle *Sélectionnez un type de moniteur*, cliquez tout d'abord sur le type de moniteur *FTP* ou *SFTP*, puis cliquez sur le bouton [SHORTCODE_9] Choisir [SHORTCODE_10].  
   Le nouveau moniteur est créé et la page de configuration s'affiche.
3. Donnez un **Nom** à votre moniteur.
4. Choisissez l'**intervalle de vérification**. [L'intervalle de vérification]([LINK_URL_1]) correspond au temps écoulé entre la fin d'une vérification et le début de la suivante.
5. Entrez le nom de domaine ou l'adresse IP de votre serveur FTP dans le champ *Adresse réseau*.
6. Si le numéro de port de votre serveur FTP est différent de la valeur par défaut affichée, remplacez-le par la valeur correcte.
7. Ouvrez l'onglet [SHORTCODE_11] Avancé [SHORTCODE_12].
8. Choisissez une option dans la boîte de dialogue **Action** (pour en savoir plus sur les actions disponibles, consultez la page de [vue d'ensemble]([LINK_URL_2])).
9. Si vous choisissez de télécharger ou de vérifier un fichier, indiquez le nom du fichier ou son chemin dans la case **Chemin du fichier**.
10. Si vous appliquez une authentification, précisez le **nom d'utilisateur** et le **mot de passe**.
11. Une fois que vous avez terminé la configuration de votre nouveau moniteur, cliquez sur le bouton [SHORTCODE_13]Enregistrer[SHORTCODE_14].

[SHORTCODE_1]**Remarque** : D'autres [paramètres de moniteurs]([LINK_URL_3]) peuvent être définis dans les autres onglets de la page de configuration.[SHORTCODE_2]






