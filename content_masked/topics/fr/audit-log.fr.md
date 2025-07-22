{
  "hero": {
    "title": "Journal d'audit"
  },
  "title": "Journal d'audit",
  "summary": "Cet article contient des indications sur les journaux d'audit.",
  "url": "[URL_BASE_TOPICS]account/journal-audit",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De nombreux changements et activités ont lieu dans l'application web d'Uptrends, et il est difficile de suivre manuellement tout ce qui a été modifié, où, quand et par qui. Dans ces situations, il est intéressant de tenir un journal d'historique. Entre autres situations, ce journal peut vous aider à corriger rapidement un changement injustifié, à trouver la cause profonde d'un problème, à évaluer les autorisations attribuées, etc.

Le **journal d'audit** d'Uptrends est un outil qui répond à tous vos besoins. Il enregistre toutes les activités effectuées dans votre application Uptrends, et vous fournit des informations détaillées sur les changements apportés dans votre compte, leur auteur, leur date et leur emplacement.

![Vue d'ensemble du dashboard Journal d'audit]([LINK_URL_1])

[SHORTCODE_1]
Le **journal d'audit** est disponible avec tous les abonnements. Il vous suffit de passer par le menu [SHORTCODE_3] Configuration de compte > Journal d'audit [SHORTCODE_4] pour visualiser les changements effectués dans votre application.
[SHORTCODE_2]

## Fonctionnalités du journal d'audit

Le dashboard Journal d'audit vous permet de consulter, de filtrer et d'exporter les journaux enregistrés dans votre compte.

### Afficher les journaux d'audit

Par défaut, le dashboard Journal d'audit présente un tableau listant les changements du plus récent au plus ancien, en détaillant les colonnes suivantes :

- **Jour/heure** : indique la date et l'heure du changement.
- **Type d'événement** : précise le type de changement apporté par l'utilisateur, par exemple *Action de connexion, Élément mis à jour et Changement d'appartenance*.
- **Opérateur** : fournit le nom de l'opérateur ayant effectué le changement.
- **Message** : fournit la description des éléments créés, mis à jour ou supprimés. Par exemple, si vous créez un opérateur, le message indique : *L'opérateur "ABC" a été créé*.
- **Source** : précise la source du changement. Si des changements ont été apportés via l'application web d'Uptrends, la source indique *Application Web*. Si les changements ont été apportés via l'API, la source indique *API*.

### Filtrer les journaux d'audit

Pour cibler facilement des activités spécifiques effectuées dans votre application, le journal d'audit vous permet de filtrer les entrées par *Type d'événement* et *Type d'élément*.

En cliquant sur le menu déroulant [SHORTCODE_5] Type d'événement [SHORTCODE_6], vous pouvez filtrer aisément les changements apportés à votre compte. Vous avez le choix entre plusieurs catégories, dont *Action de connexion, Changement d'appartenance, Changement d'autorisation et Élément créé*.

De même, le menu déroulant [SHORTCODE_7] Type d'élément [SHORTCODE_8] vous permet de filtrer les changements apportés aux *moniteurs, groupes de moniteurs, opérateurs, groupes d'opérateurs*, entre autres éléments.

### Exporter les journaux d'audit

Tout comme n'importe quel dashboard d'Uptrends, le journal d'audit peut aussi être exporté sous format PDF, Excel ou HTML. Lisez cet [article de notre base de connaissances]([LINK_URL_2]) pour connaître la marche à suivre pour exporter les données de votre dashboard Journal d'audit.

L'export de vos données contient les mêmes détails que ceux présentés dans le tableau récapitulatif de votre dashboard Journal d'audit. Seule la colonne *Source* est supprimée pour simplifier la consultation.

## Détails du journal d'audit

Tandis que le tableau du journal d'audit fournit une vue d'ensemble de l'historique des changements apportés dans votre compte, les **Détails du journal d'audit** contiennent des informations plus précises sur les changements effectués.

Il vous suffit de cliquer sur chaque entrée du journal d'audit pour afficher la vue contextuelle **Détails du journal d'audit** :

![Vue d'ensemble des détails du journal d'audit]([LINK_URL_3])

La plupart du temps, cette fenêtre contextuelle affiche des informations similaires à celles qui sont présentées dans le tableau récapitulatif fourni dans le dashboard Journal d'audit. D'autres informations s'affichent aussi, telles que l'identifiant du journal d'audit (un identifiant unique pour chaque entrée du journal d'audit), le nom du type d'élément (par exemple, moniteur, opérateur, définition d'alerte, etc.) et des informations spécifiques sur les éléments créés, mis à jour et supprimés.

Comme le montre l'image ci-dessus, lorsqu'un élément est créé, la fenêtre **Détails du journal d'audit** contient une section *Créé avec les valeurs :*, qui apporte des précisions sur l'élément créé et ses paramètres. De la même façon, lorsque vous actualisez un élément, les détails du journal d'audit affichent une section *Mis à jour avec les nouvelles valeurs :*, qui précise les anciennes et les nouvelles valeurs. Notez que les informations affichées dans les détails du journal d'audit varient selon les modifications apportées et les éléments mis à jour.

## Détails du journal d'audit pour chaque type d'élément

Cette section présente l'historique des changements enregistrés par le journal d'audit pour chaque *type d'élément*.

### Dashboards
Le journal d'audit enregistre les changements relatifs aux **dashboards**, qui surviennent lorsque vous :
- accordez et révoquez des autorisations de *partage* pour les dashboards.

### Définition d'alerte
Le journal d'audit enregistre les changements relatifs aux **définitions d'alerte**, qui surviennent lorsque vous :

- créez une définition d'alerte ;
- renommez et supprimez une définition d'alerte ;
- activez et désactivez le statut d'une définition d'alerte ;
- ajoutez, modifiez et supprimez des paramètres en lien avec les moniteurs, groupes de moniteurs et niveaux d'escalade concernés par la définition d'alerte ;
- accordez et révoquez des autorisations pour les définitions d'alerte.

### Intégrations
Le journal d'audit enregistre les changements relatifs aux **intégrations**, qui surviennent lorsque vous :

- créez une intégration ;
- renommez et supprimez une intégration ;
- activez et désactivez le statut de l'intégration ;
- ajoutez, modifiez et supprimez des variables prédéfinies, ainsi que des paramètres généraux de l'intégration ;
- accordez et révoquez des autorisations pour les intégrations.

### Moniteurs
Le journal d'audit enregistre les changements relatifs aux **moniteurs**, qui surviennent lorsque vous :

- créez un moniteur ;
- renommez et supprimez un moniteur ;
- activez et désactivez le statut d'un moniteur ;
- ajoutez, actualisez et supprimez les paramètres de moniteur configurés dans les onglets [SHORTCODE_9] Principal [SHORTCODE_10], [SHORTCODE_11] Étapes [SHORTCODE_12], [SHORTCODE_13] Conditions d'erreur [SHORTCODE_14], [SHORTCODE_15] Avancé [SHORTCODE_16], [SHORTCODE_17] Checkpoints [SHORTCODE_18], [SHORTCODE_19] Périodes de maintenance [SHORTCODE_20] et [SHORTCODE_21] Membre de [SHORTCODE_22] ;
- mettez en place et désactivez des moniteurs et des alertes de moniteurs ;
- accordez et révoquez des autorisations pour les moniteurs.

### Groupes de moniteurs
Le journal d'audit enregistre les changements relatifs aux **groupes de moniteurs**, qui surviennent lorsque vous :

- créez un groupe de moniteurs ;
- renommez et supprimez un groupe de moniteurs ;
- ajoutez, modifiez et supprimez des informations sur les groupes de moniteurs ainsi que les moniteurs compris dans le groupe de moniteurs ;
- accordez et révoquez des autorisations pour les groupes de moniteurs.

### Modèles de moniteur
Le journal d'audit enregistre les changements relatifs aux **modèles de moniteur**, qui surviennent lorsque vous :

- créez un modèle de moniteur ;
- renommez et supprimez un modèle de moniteur ;
- ajoutez, actualisez et supprimez des éléments dans les paramètres généraux, et les onglets [SHORTCODE_23] Checkpoints [SHORTCODE_24] et [SHORTCODE_25] Périodes de maintenance [SHORTCODE_26] du modèle de moniteur.

### Opérateurs
Le journal d'audit enregistre les changements relatifs aux **opérateurs**, qui surviennent lorsque vous :

- créez un opérateur ;
- renommez et supprimez un opérateur ;
- ajoutez, actualisez et supprimez des éléments dans les paramètres généraux, et les onglets [SHORTCODE_27] Horaires de repos [SHORTCODE_28] et [SHORTCODE_29] Membre de [SHORTCODE_30] spécifiques aux opérateurs ;
- actualisez les paramètres des fuseaux horaires ;
- envoyez une invitation à un opérateur ou qu'une invitation est acceptée par l'opérateur ;
- accordez et révoquez des autorisations pour les opérateurs.

Le journal d'audit enregistre aussi les éléments liés aux opérateurs par *type d'événement*, par exemple *Action de connexion et Tentative de connexion échouée*.

### Groupe d'opérateurs

Le journal d'audit enregistre les changements relatifs aux **groupes d'opérateurs**, qui surviennent lorsque vous :

- créez un groupe d'opérateurs ;
- ajoutez ou excluez des membres d'un groupe d'opérateurs ;
- modifiez le nom d'un groupe d'opérateurs ;
- supprimez un groupe d'opérateurs ;
- accordez et révoquez des autorisations pour les groupes d'opérateurs.

### Emplacements privés

Le journal d'audit enregistre les changements relatifs aux **emplacements privés**, qui surviennent lorsque vous :

- créez un emplacement privé ;
- renommez et supprimez un emplacement privé ;
- activez et désactivez les checkpoints ;
- ajoutez, actualisez et supprimez les paramètres d'un emplacement privé.

### Définitions de SLA

Le journal d'audit enregistre les changements relatifs aux **définitions SLA**, qui surviennent lorsque vous :

- créez une définition SLA ;
- renommez et supprimez une définition SLA ;
- ajoutez, actualisez et supprimez les paramètres liés aux plannings et aux périodes d'exclusion des SLA.

### Coffre-fort

Le journal d'audit enregistre les changements relatifs aux **coffres-forts**, qui surviennent lorsque vous :

- créez, actualisez et supprimez un élément de coffre-fort ;
- créez, actualisez et supprimez une section de coffre-fort ;
- ajoutez, actualisez et supprimez des éléments de coffre-fort dans une section de coffre-fort ;
- accordez et révoquez des autorisations pour les sections de coffre-fort.
