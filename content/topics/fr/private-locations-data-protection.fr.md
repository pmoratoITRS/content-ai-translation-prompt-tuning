{
"hero": {
"title": "Protection des données dans les emplacements privés"
},
"title": "Protection des données dans les emplacements privés",
"summary": "Comment sont protégées les données dans les emplacements privés ?",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/protection-donnees-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-data-protection"
}

Cet article de notre base de connaissances vous explique comment protéger les données situées dans vos emplacements privés. L'une des mesures de protection liées aux emplacements privés d'Uptrends consiste à empêcher le chargement des captures d'écran sur le cloud. Vous pouvez aussi désactiver le contenu des pages, et masquer les en-têtes de requête et de réponse ainsi que les adresses IP résolues dans les résultats des vérifications.

## Modification du fichier Docker Compose

Si vous ne l'avez pas déjà fait, commencez par installer votre checkpoint en suivant les étapes présentées dans l'article [Installer un checkpoint Docker]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="fr" >}}).

1. Effectuez une copie de sauvegarde de l'extraction du fichier Docker Compose. Tout changement apporté au fichier Compose est effectué à vos propres risques. En cas de doute, contactez le [support]({{< ref path="/contact" lang="fr" >}}).
2. Ouvrez le fichier docker-compose.yml et retirez la balise de commentaire ``#`` avant la ou les variables de protection de données dans le service Checkpoint que vous voulez activer. En supprimant la balise, la protection des données s'applique à l'élément de la liste d'environnement sélectionnée.


```
Checkpoint:
   container_name: Checkpoint
   image: uptrends.azurecr.io/win2022/checkpoint
   depends_on:
     - TransactionProcessor
   deploy:
     restart_policy:
       condition: always
   volumes:
     - .\Certificates:C:\Uptrends\Certificates:ro
   logging:
     driver: "json-file"
     options:
       max-size: 10m
       max-file: "3"
   environment:
    - ServerId=
    - Password=
    - HasIpv6Support=false
#    - AllowScreenshotsInResults=false
#    - AllowPageContentInResults=false
#    - AllowHttpHeadersInResults=false
#    - AllowResolvedIpAddressesInResults=false
 
```
3. Enregistrez votre fichier.
4. Redémarrez le conteneur manuellement en exécutant la commande ```docker-compose down```, puis en exécutant ```docker-compose up``` dans la ligne de commande du dossier où se trouve le fichier Compose modifié. Dans l'application Uptrends, vérifiez les paramètres modifiés dans la section [Paramètres de protection des données](#data-protection-settings-status) de l'onglet {{< AppElement type="tab" >}} Santé du point de contrôle {{< /AppElement >}}.

### Empêcher le chargement des captures d'écran des erreurs et des captures d'écran chronologiques sur le cloud
Une fois le paramètre activé, les **détails de vérification** d'Uptrends affichent un message vous confirmant que les captures d'écran ne sont pas collectées, conformément à la politique de protection des données de votre entreprise.

Ce réglage s'applique à toutes les captures d'écran, y compris les [captures d'écran chronologiques]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}) (aussi appelées pellicules) et les [captures d'écran des erreurs]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="fr" >}}) pour les moniteurs HTTP(S).

Pour désactiver les captures d'écran dans les résultats, retirez la balise ``#`` avant `- AllowScreenshotsInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.

{{< callout >}} **Important** : Cette méthode repose sur la désactivation des captures d'écran. Aucune capture d'écran n'est effectuée. En cas d'erreur, les informations de [dépannage]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#further-troubleshooting" lang="fr" >}}) ne contiennent donc pas de captures d'écran.
{{< /callout >}}

### Désactiver le contenu des pages
Ce paramètre permet de s'assurer qu'aucun contenu ne s'affiche dans [la source de la page et le journal de la console]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="fr">}}). Les URL de données ne fournissent jamais les données dans les résultats.

Pour désactiver le contenu de page dans les résultats, retirez la balise ``#`` avant `- AllowScreenshotsInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.

### Masquer les en-têtes de requête et de réponse HTTP
Une fois le paramètre activé, le graphique en cascade des détails de vérification n'affiche aucun en-tête de requête ou de réponse HTTP.

Pour masquer les en-têtes de requête et de réponse HTTP, ajoutez la balise  ``#`` avant `- AllowHttpHeadersInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.
![Protection des données : masquage des en-têtes de requête et de réponse HTTP dans le graphique en cascade](/img/content/scr-data-protection-waterfall-headers.min.png)

### Désactiver les adresses IP résolues pour les en-têtes de réponse et de requête
Ce paramètre vous permet de vous assurer que les en-têtes du rapport de la vérification n'affichent aucune adresse IP résolue. Notez toutefois que cela ne fonctionne pas si le champ d'URL du ou des moniteurs contient une adresse IP littérale au lieu d'une valeur de domaine.

Pour masquer les adresses IP résolues, ajoutez la balise ``#`` avant `- AllowResolvedIpAddressesInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.

### Désactiver les adresses IP résolues dans les détails de vérification
Ce paramètre vous permet de vous assurer qu'aucune adresse IP résolue ne s'affiche dans le champ **Adresse IP résolue**.

Pour masquer les adresses IP résolues, ajoutez la balise ``#`` avant `- AllowResolvedIpAddressesInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.

Si cette valeur est définie comme "false", l'exécution des moniteurs DNS sera bloquée sur les serveurs de checkpoints de votre emplacement privé.

{{< callout >}} **Remarque** : Tous les paramètres ne sont pas disponibles pour tous les moniteurs. Par exemple, pour les moniteurs HTTP(S) de base, seules les captures d'écran des erreurs fonctionnent, et le paramétrage des adresses IP résolues n'est pas disponible pour ce type de moniteur.
{{< /callout >}}

## État des paramètres de protection des données

Dans l'application Uptrends, l'onglet [Santé du point de contrôle]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="fr" >}}) montre l'état des paramètres de protection des données. La présence d'une croix rouge signifie que les données ne s'affichent pas, et donc que la protection des données est activée. Notez que l'affichage est en lecture seule, et que les paramètres ne peuvent être ajustés que dans le fichier Docker.

![Paramètres de protection des données dans l'onglet Santé du point de contrôle](/img/content/scr_private-location-checkpoint-health-data-protected.min.png)