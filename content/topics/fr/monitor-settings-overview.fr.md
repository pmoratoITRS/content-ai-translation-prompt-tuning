{
"hero": {
"title": "Vue d'ensemble des réglages du moniteur"
},
"title": "Vue d'ensemble des réglages du moniteur",
"summary": "Chaque moniteur s'accompagne de paramètres généraux et spécifiques. Découvrez quels paramètres sont disponibles.",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/vue-densemble-des-reglages-du-moniteur",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-settings-overview",
"sectionlist": false
}

## Emplacement des paramètres des moniteurs

Pour gérer les paramètres de vos moniteurs :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Trouvez le nom du moniteur qui vous intéresse et cliquez sur le lien correspondant dans la colonne *Nom de moniteur*. Vous pouvez aussi filtrer les résultats en saisissant la totalité ou le début du nom, du type, du groupe ou de l'URL dans le champ de recherche.
   La page de configuration du moniteur se compose de plusieurs onglets contenant les différents paramètres. Les catégories de paramètres sont détaillées dans la suite de cet article.
3. Apportez les changements nécessaires dans les onglets.
4. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour conserver tous les changements apportés au moniteur.

## Catégories de paramètres de moniteurs

Chaque type de moniteur correspond à des objectifs de surveillance distincts. Tous les moniteurs n'ont donc pas les mêmes paramètres. Découvrez quels paramètres sont applicables à votre moniteur :
- Principaux paramètres
   - [Intervalle de vérification]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="fr" >}})
   - [Valeurs dynamiques dans les URL et les requêtes POST]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dynamic-date-notation-in-url-and-post-content" lang="fr" >}})
   - [Mode du moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}})
   - [Notes des moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="fr" >}})
   - [Modèles de moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="fr" >}})
- [Étapes (moniteurs de transactions)]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}})
- [Étapes (moniteurs multi-étapes)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}})
- [Conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}})
- Paramètres avancés
   - [Types de navigateurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="fr" >}})
   - [Blocage de Google Analytics]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="fr" >}})
   - [Limitation de bande passante]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling" lang="fr" >}})
   - [Contournement DNS]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="fr" >}})
- [Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="fr" >}})
- [Périodes de maintenance]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="fr" >}})
- [Membre de (Groupes de moniteurs)]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="fr" >}})
- [Autorisations]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}})

## Dashboard Configuration du moniteur

Comme l'application Web d'Uptrends peut contenir de nombreux moniteurs, le **dashboard Configuration du moniteur** vous fournit un tableau récapitulatif qui vous permet de consulter tous vos moniteurs et leurs paramètres depuis un même emplacement. Depuis ce dashboard, vous pouvez consulter, filtrer et exporter les paramètres de moniteur configurés dans votre compte.

![Vue d'ensemble du dashboard Configuration du moniteur](/img/content/src_monitor-setup-dashboard-overview.min.png)

### Consulter les paramètres des moniteurs
Depuis ce dashboard, vous pouvez facilement consulter les paramètres de vos moniteurs, soit les informations suivantes :

- **Nom du moniteur** : cette colonne précise le nom du moniteur configuré et le nombre de [crédits]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}) de moniteur utilisés. La présence d'une icône en forme de fiole indique que votre moniteur est en [mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}) *Simulation*, tandis que l'icône en forme de clé à molette correspond au mode *Développement*.
- **Dashboard du moniteur** : cette colonne contient un lien *Aller au dashboard du moniteur* qui vous redirige directement vers le dashboard spécifique au moniteur.
- **Type de moniteur** : cette colonne précise le [type de moniteur]({{< ref path="/support/kb/basics/monitor-types" lang="fr" >}}) configuré (par exemple, un moniteur de transactions et un moniteur d'API multi-étapes).
- **Intervalle de vérification (en minutes)** : cette colonne indique à quelle fréquence votre moniteur fait l'objet d'une vérification.
- **URL / Adresse réseau** : cette colonne précise l'adresse de navigateur ou l'adresse IP du site Web que vous surveillez.
- **Actif** : cette colonne indique si votre moniteur est activé ou désactivé. Si le moniteur est activé, elle affiche *Oui*. S'il est désactivé, elle affiche *Non*. Pour les moniteurs activés et désactivés, le [mode]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="fr" >}}) actuel du moniteur est aussi précisé entre parenthèses, soit *Simulation* ou *Développement*.
- **Créé le** : cette colonne indique la date et l'heure de création du moniteur.
- **Modifié le** : cette colonne indique la date et l'heure de la dernière modification ou du dernier enregistrement de changements apportés au moniteur.
- **Membre des groupes** : cette colonne précise le ou les groupes de moniteurs auxquels le moniteur appartient.

### Filtrer les paramètres des moniteurs

Pour cibler facilement des moniteurs, ouvrez le champ textuel de filtre et filtrez les résultats d'après le nom, le type, le groupe et l'URL du moniteur. Vous pouvez aussi filtrer les résultats par mode de moniteur en cochant simplement les cases *Développement, Simulation ou Production*.

### Exporter les paramètres des moniteurs

Les paramètres de vos moniteurs peuvent être consultés et regroupés dans le **dashboard Configuration du moniteur**, mais vous pouvez aussi exporter ces données pour affiner les informations dont vous disposez et y revenir ultérieurement. Lisez cet [article de notre base de connaissances]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="fr" >}}) pour connaître la procédure à suivre pour exporter vos dashboards.

Une fois vos données exportées dans l'un des formats disponibles, vous pourrez consulter les détails des paramètres de vos moniteurs comme indiqué dans la section ci-dessus [Dashboard Configuration du moniteur]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-setup" lang="en" >}}). L'export vous fournira aussi d'autres informations :

- **Alerte sur les limites de temps** : cette colonne fournit des informations sur les paramètres relatifs aux [temps de chargement et de fonctionnement]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}}). Elle indique si la condition d'erreur est définie sur le statut *Code couleur uniquement* ou *Générer une erreur*.
- **Limites de temps** : cette colonne affiche les [seuils de temps (en millisecondes)]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}}) correspondants de votre moniteur (ce paramètre est lié à l'alerte sur les limites de temps).
- **Notes** : cette colonne montre la description du champ *Notes*.