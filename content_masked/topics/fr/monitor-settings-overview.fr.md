{
  "hero": {
    "title": "Vue d'ensemble des réglages du moniteur"
  },
  "title": "Vue d'ensemble des réglages du moniteur",
  "summary": "Chaque moniteur s'accompagne de paramètres généraux et spécifiques. Découvrez quels paramètres sont disponibles.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/vue-densemble-des-reglages-du-moniteur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

## Emplacement des paramètres des moniteurs

Pour gérer les paramètres de vos moniteurs :

1. Ouvrez le menu [SHORTCODE_1] Surveillance > Configuration du moniteur [SHORTCODE_2].
2. Trouvez le nom du moniteur qui vous intéresse et cliquez sur le lien correspondant dans la colonne *Nom de moniteur*. Vous pouvez aussi filtrer les résultats en saisissant la totalité ou le début du nom, du type, du groupe ou de l'URL dans le champ de recherche.
   La page de configuration du moniteur se compose de plusieurs onglets contenant les différents paramètres. Les catégories de paramètres sont détaillées dans la suite de cet article.
3. Apportez les changements nécessaires dans les onglets.
4. Cliquez sur le bouton [SHORTCODE_3] Enregistrer [SHORTCODE_4] pour conserver tous les changements apportés au moniteur.

## Catégories de paramètres de moniteurs

Chaque type de moniteur correspond à des objectifs de surveillance distincts. Tous les moniteurs n'ont donc pas les mêmes paramètres. Découvrez quels paramètres sont applicables à votre moniteur :
- Principaux paramètres
   - [Intervalle de vérification]([LINK_URL_1])
   - [Valeurs dynamiques dans les URL et les requêtes POST]([LINK_URL_2])
   - [Mode du moniteur]([LINK_URL_3])
   - [Notes des moniteurs]([LINK_URL_4])
   - [Modèles de moniteur]([LINK_URL_5])
- [Étapes (moniteurs de transactions)]([LINK_URL_6])
- [Étapes (moniteurs multi-étapes)]([LINK_URL_7])
- [Conditions d'erreur]([LINK_URL_8])
- Paramètres avancés
   - [Types de navigateurs]([LINK_URL_9])
   - [Blocage de Google Analytics]([LINK_URL_10])
   - [Limitation de bande passante]([LINK_URL_11])
   - [Contournement DNS]([LINK_URL_12])
- [Checkpoints]([LINK_URL_13])
- [Périodes de maintenance]([LINK_URL_14])
- [Membre de (Groupes de moniteurs)]([LINK_URL_15])
- [Autorisations]([LINK_URL_16])

## Dashboard Configuration du moniteur

Comme l'application Web d'Uptrends peut contenir de nombreux moniteurs, le **dashboard Configuration du moniteur** vous fournit un tableau récapitulatif qui vous permet de consulter tous vos moniteurs et leurs paramètres depuis un même emplacement. Depuis ce dashboard, vous pouvez consulter, filtrer et exporter les paramètres de moniteur configurés dans votre compte.

![Vue d'ensemble du dashboard Configuration du moniteur]([LINK_URL_17])

### Consulter les paramètres des moniteurs
Depuis ce dashboard, vous pouvez facilement consulter les paramètres de vos moniteurs, soit les informations suivantes :

- **Nom du moniteur** : cette colonne précise le nom du moniteur configuré et le nombre de [crédits]([LINK_URL_18]) de moniteur utilisés. La présence d'une icône en forme de fiole indique que votre moniteur est en [mode]([LINK_URL_19]) *Simulation*, tandis que l'icône en forme de clé à molette correspond au mode *Développement*.
- **Dashboard du moniteur** : cette colonne contient un lien *Aller au dashboard du moniteur* qui vous redirige directement vers le dashboard spécifique au moniteur.
- **Type de moniteur** : cette colonne précise le [type de moniteur]([LINK_URL_20]) configuré (par exemple, un moniteur de transactions et un moniteur d'API multi-étapes).
- **Intervalle de vérification (en minutes)** : cette colonne indique à quelle fréquence votre moniteur fait l'objet d'une vérification.
- **URL / Adresse réseau** : cette colonne précise l'adresse de navigateur ou l'adresse IP du site Web que vous surveillez.
- **Actif** : cette colonne indique si votre moniteur est activé ou désactivé. Si le moniteur est activé, elle affiche *Oui*. S'il est désactivé, elle affiche *Non*. Pour les moniteurs activés et désactivés, le [mode]([LINK_URL_21]) actuel du moniteur est aussi précisé entre parenthèses, soit *Simulation* ou *Développement*.
- **Créé le** : cette colonne indique la date et l'heure de création du moniteur.
- **Modifié le** : cette colonne indique la date et l'heure de la dernière modification ou du dernier enregistrement de changements apportés au moniteur.
- **Membre des groupes** : cette colonne précise le ou les groupes de moniteurs auxquels le moniteur appartient.

### Filtrer les paramètres des moniteurs

Pour cibler facilement des moniteurs, ouvrez le champ textuel de filtre et filtrez les résultats d'après le nom, le type, le groupe et l'URL du moniteur. Vous pouvez aussi filtrer les résultats par mode de moniteur en cochant simplement les cases *Développement, Simulation ou Production*.

### Exporter les paramètres des moniteurs

Les paramètres de vos moniteurs peuvent être consultés et regroupés dans le **dashboard Configuration du moniteur**, mais vous pouvez aussi exporter ces données pour affiner les informations dont vous disposez et y revenir ultérieurement. Lisez cet [article de notre base de connaissances]([LINK_URL_22]) pour connaître la procédure à suivre pour exporter vos dashboards.

Une fois vos données exportées dans l'un des formats disponibles, vous pourrez consulter les détails des paramètres de vos moniteurs comme indiqué dans la section ci-dessus [Dashboard Configuration du moniteur]([LINK_URL_23]). L'export vous fournira aussi d'autres informations :

- **Alerte sur les limites de temps** : cette colonne fournit des informations sur les paramètres relatifs aux [temps de chargement et de fonctionnement]([LINK_URL_24]). Elle indique si la condition d'erreur est définie sur le statut *Code couleur uniquement* ou *Générer une erreur*.
- **Limites de temps** : cette colonne affiche les [seuils de temps (en millisecondes)]([LINK_URL_25]) correspondants de votre moniteur (ce paramètre est lié à l'alerte sur les limites de temps).
- **Notes** : cette colonne montre la description du champ *Notes*.