{
"hero": {
"title": "Affichez vos données de surveillance dans Grafana"
  },
"title": "Intégration pour Grafana",
"summary": "Découvrez comment afficher vos données de surveillance dans Grafana.",
  "url": "/support/kb/dashboards-et-rapports/grafana",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/grafana"
}

La source de données Uptrends pour Grafana permet d'afficher dans un environnement Grafana les informations relatives aux statuts et statistiques relevées par les moniteurs et les groupes de moniteurs d'Uptrends. Cette extension utilise l'API Uptrends pour récupérer des données statistiques ou des données sur le statut de vos moniteurs et groupes de moniteurs.

Cet article vous explique comment configurer une instance Grafana de base pour récupérer des données depuis Uptrends et les afficher dans votre environnement Grafana. Pour tout problème, question ou commentaire, veuillez nous écrire depuis notre [page de contact]({{< ref path="/contact" lang="fr" >}}).

## Prérequis
- Un compte Uptrends actif
- Des identifiants APIv4 pour Uptrends : voir plus bas pour savoir comment les générer
- Une instance Grafana avec un accès à la configuration du serveur

## Préconfiguration

### Créer un compte Uptrends APIv4

{{< callout >}} **Remarque** : Si vous disposez déjà d'identifiants APIv4, vous pouvez les utiliser et ignorer cette étape.  {{< /callout >}}

Grafana communique avec Uptrends via notre API (version 4, consultez [la documentation de l'API]({{< ref path="/support/kb/api" lang="fr" >}}) pour en savoir plus) pour obtenir les informations recherchées et les afficher dans vos dashboards Grafana. Pour effectuer ces requêtes, Grafana doit avoir accès à un compte API enregistré. Pour créer un compte API, suivez les instructions figurant dans notre article [Gestion des comptes API d'un opérateur]({{< ref path="/support/kb/account/users/operators/operator-API-management" lang="fr" >}}).

Les étapes décrites dans cet article vous permettent d'obtenir un nom d'utilisateur et un mot de passe. Notez-les soigneusement, car vous devrez les ajouter ultérieurement à la source de données dans Grafana.

Chaque compte API est associé à un opérateur dans Uptrends. Vérifiez que l'opérateur possède au moins l'autorisation [*Afficher les données du moniteur dans le groupe*]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}}) pour chacun des moniteurs ou groupes de moniteurs que vous souhaitez afficher dans Grafana.

## Installation de l'extension

1. **Téléchargez l'extension :** l'extension Uptrends pour Grafana la plus récente est la [version 0.9.274](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana.0.9.274.zip). Vous pouvez télécharger le fichier compressé depuis ce [lien](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana_latest.zip).
2. **Extrayez le fichier .zip et copiez son contenu dans le répertoire d'extensions de Grafana :** son emplacement par défaut est `/var/lib/grafana/plugins`. Pour plus d'informations, consultez la documentation de Grafana.
3. **Activez l'extension :** l'extension est actuellement non signée, ce qui signifie qu’elle doit être activée dans la configuration de Grafana. Pour activer l’extension, suivez ces étapes :

   - Sur le serveur qui héberge votre instance Grafana, trouvez le fichier *grafana.ini* (qui se trouve par défaut à l'emplacement `/etc/grafana/grafana.ini`) et ouvrez-le avec votre éditeur de fichiers habituel.
   - Dans `[plugins]` (faites défiler ou utilisez la fonction de recherche si nécessaire), trouvez la clé `allow_loading_unsigned_plugins`.
   - Ajoutez la valeur `uptrends-uptrends-plugin` à la commande `allow_loading_unsigned_plugins`.

![Activer une extension non signée](/img/content/scr-grafana-allow-unsigned-plugins.min.png)

4. **Redémarrez Grafana.** L'extension devrait désormais être disponible dans l'interface.

## Créer la source de données
1. Dans votre interface Grafana, ouvrez le menu _Configuration_ (l'icône engrenage dans le menu à gauche) -> _Data sources_ (Sources de données).
2. Cliquez sur _Add data source_ (Ajouter une source de données).
3. Trouvez l'option _Uptrends_ et cliquez sur l'extension correspondante (qui devrait s'appeler `uptrends-plugin`).
4. Saisissez le nom d'utilisateur et le mot de passe APIv4 que vous avez obtenus à l'étape 1, ou utilisez les identifiants dont vous disposiez déjà.
5. Cliquez sur _Save & test_ (Enregistrer et tester).

![Création de la source de données](/img/content/scr-grafana-plugin-config.min.png)

### Créer un dashboard

Maintenant que la source de données a été configurée, elle peut commencer à extraire des données d'Uptrends pour les afficher dans des dashboards de Grafana.

1. Ouvrez *Dashboards > + New dashboard* (+ Nouveau dashboard), ou modifiez un dashboard existant.
2. Cliquez sur *Add a new panel* (Ajouter un nouveau panneau).

![Modifier un panneau](/img/content/scr-grafana-edit-panel.min.png)

3. Vérifiez que la bonne source de données (intitulée `uptrends-plugin`) est sélectionnée comme **Data source** (Source de données) du panneau.
4. Choisissez un type de panneau dans l'angle supérieur droit, et remplissez les autres options demandées dans le menu à droite.
5. Choisissez les données à afficher.

   \- Vous pouvez choisir les données sur les statuts des moniteurs (qui indiquent si vos moniteurs affichent une erreur ou un statut OK) ou les statistiques des moniteurs (qui concernent l'évolution des performances des moniteurs).

   \- Vous pouvez filtrer un moniteur ou un groupe de moniteurs par requête. Les listes de moniteurs et de groupes de moniteurs doivent se remplir automatiquement.

![Sélectionner les données d'Uptrends à afficher dans le panneau](/img/content/scr-grafana-populating-panel.min.png)

6. Cliquez sur *Apply* (Appliquer) dans l'angle supérieur droit.

Cet article propose une description très sommaire de l'affichage des données d'Uptrends dans Grafana. L'outil Grafana offre de nombreuses options supplémentaires.
