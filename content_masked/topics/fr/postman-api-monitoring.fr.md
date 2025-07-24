{
  "hero": {
    "title": "Configuration de la surveillance d'API avec Postman"
  },
  "title": "Configuration de la surveillance d'API avec Postman",
  "summary": "Instructions détaillées pour configurer une surveillance d'API avec Postman.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/surveillance-api-postman",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Avec le moniteur API Postman d'Uptrends, vous pouvez exécuter automatiquement les collections de vos espaces de travail Postman sur le réseau de checkpoints d'Uptrends. Ce moniteur vous permet de planifier et de tester facilement des scripts Postman et de tester la performance de vos API. Il se configure comme tous les autres moniteurs.

Employé par des millions d'utilisateurs, Postman est un outil informatique standard dont les développeurs se servent pour coder, documenter et exécuter des tests API. Grâce à cet outil, vous pouvez tester des méthodes HTTP (GET, POST, PUT, DELETE, PATCH), et ajouter des en-têtes, des paramètres, des variables et bien plus encore. Vous pouvez aussi regrouper et organiser plusieurs requêtes, désignées comme des collections Postman, et les communiquer à d'autres personnes ou les conserver pour un usage ultérieur. Dès que vous avez besoin de tester vos API, il vous suffit d'ouvrir l'interface de Postman pour exécuter vos scripts d'API d'un simple clic.

Avec Uptrends, vous n'avez pas à ouvrir Postman pour tester manuellement vos scripts : votre moniteur API Postman le fait pour vous. Ce moniteur récupère votre collection Postman de scripts d'API, y compris les scripts de pré-requête et de post-requête, les importe au moyen d'une URL d'API ou d'un fichier JSON, puis lance leur exécution à travers le monde comme tous les autres types de moniteur.

## Avantages du moniteur API Postman

Si votre organisation utilise déjà Postman, ce moniteur pourra vous apporter les avantages suivants :

- **Exécution automatique de vos scripts** : vous pouvez exécuter automatiquement vos scripts Postman toutes les minutes, toutes les 5 minutes et toutes les heures, et dans le monde entier. Nous possédons plus de 200 [checkpoints]([LINK_URL_1]) de surveillance que vous pouvez sélectionner pour exécuter vos tests.

- **Aucun délai de lancement** : il vous suffit d'importer vos scripts disponibles dans Uptrends pour utiliser immédiatement ce moniteur. Aucune adaptation ni ajustement au système d'Uptrends ne sont nécessaires.

- **Rien à apprendre** : vos connaissances de Postman vous suffisent pour utiliser facilement ce moniteur. Montrez-nous seulement où sont vos scripts Postman, et vous aurez les résultats en un rien de temps.

- **Votre flux de travail reste inchangé** : vous pouvez continuer d'utiliser Postman pour vos scripts. Lorsque vous apportez des changements à votre collection, il suffit de l'actualiser sur Uptrends.

[SHORTCODE_1] Les [emplacements privés]([LINK_URL_2]) ne sont pas encore disponibles dans le moniteur API Postman. [SHORTCODE_2]

## Configurer un moniteur d'API Postman

Il existe deux méthodes pour configurer un moniteur d'API Postman : [en important des scripts Postman depuis un fichier JSON]([LINK_URL_3]) ou [en important des scripts Postman depuis une URL d'API]([LINK_URL_4]).

[SHORTCODE_3] **Remarque :** Lorsque vous importez des scripts Postman au moyen d'une URL d'API, vous devez sélectionner l'option **Share** > **Via API** (Partager > Par API). Cette option est uniquement accessible aux comptes Postman payants. [SHORTCODE_4]

### Importer à partir d'un fichier JSON

Cette option vous permet de sauvegarder simultanément vos fichiers Postman et d'importer les changements de Postman vers Uptrends.

Voici comment configurer un moniteur en important un fichier JSON :

1. Ouvrez le menu [SHORTCODE_7] API > Gérer les moniteurs API (+) [SHORTCODE_8].
2. Sélectionnez l'option **API Postman**.
3. Configurez les [paramètres du moniteur]([LINK_URL_5]) selon vos besoins de surveillance.

4. Dans l'onglet [SHORTCODE_9] Collection Postman [SHORTCODE_10], sélectionnez l'option  
   **Importer à partir d'un fichier JSON**. Pour exporter votre fichier JSON depuis Postman, reportez-vous à l'article [Export collections from Postman]([LINK_URL_6]).

5. Cliquez sur le bouton [SHORTCODE_11] Choose File [SHORTCODE_12] (Choisir le fichier) et importez votre fichier JSON.

Une fois l'importation effectuée, la section **Détails de la collection** se remplit automatiquement avec les informations figurant dans Postman. Des détails tels que le nom et l'identifiant de la collection ainsi que les requêtes sont alors visibles.

![Importation d'un fichier JSON]([LINK_URL_7])

6. Cliquez sur [SHORTCODE_13] Enregistrer [SHORTCODE_14] pour confirmer les changements.

Votre moniteur est maintenant configuré. Utilisez le bouton **Tester maintenant** dans l'éditeur de moniteur pour tester et afficher les [résultats du moniteur]([LINK_URL_8]).

### Importer via une URL d'API

Cette option vous permet d'importer des changements depuis Postman vers Uptrends en utilisant une URL d'API, ce qui facilite les tests en direct. Cette méthode actualise votre collection en un seul clic et vous permet aussi de gagner de l'espace de mémoire.

Voici comment configurer un moniteur au moyen l'URL d'API d'une collection Postman :

1. Ouvrez le menu [SHORTCODE_15] API > Gérer les moniteurs API (+) [SHORTCODE_16].
2. Sélectionnez l'option **API Postman**.
3. Configurez les [paramètres du moniteur]([LINK_URL_9]) selon vos besoins de surveillance.

4. Dans l'onglet [SHORTCODE_17] Collection Postman [SHORTCODE_18], sélectionnez l'option  
   **Importer via une URL API**.

5. Collez l'URL de l'API Postman dans le champ textuel vide. Pour obtenir l'URL de l'API Postman, lisez l'article [Share using the Postman API]([LINK_URL_10]).

6. Cliquez sur le bouton [SHORTCODE_19] Récupérer la collection[SHORTCODE_20] pour extraire les données de votre URL.

Une fois l'opération effectuée, la section **Détails de la collection** se remplit automatiquement avec les informations figurant dans Postman. Des détails tels que le nom et l'identifiant de la collection ainsi que les requêtes sont alors visibles.

![Importer via une URL API]([LINK_URL_11])

[SHORTCODE_5] **Remarque :** Vous devez cliquer sur le bouton [SHORTCODE_21] Récupérer la collection [SHORTCODE_22] à chaque fois que la collection est modifiée. Cela permet à Uptrends de récupérer les derniers changements et de remplacer les scripts Postman en cours de surveillance. [SHORTCODE_6]

7. Cliquez sur [SHORTCODE_23] Enregistrer [SHORTCODE_24] pour confirmer les changements.

Votre moniteur est maintenant configuré. Utilisez le bouton **Tester maintenant** dans l'éditeur de moniteur pour tester et afficher les [résultats du moniteur]([LINK_URL_12]).

Pour plus d'informations, consultez la [documentation de Postman]([LINK_URL_13]).

## Résultats du moniteur

Les **résultats des tests du moniteur API Postman** sont très proches des résultats de la surveillance d'API multi-étapes. Dans la section **Voir les détails**, chacune des étapes correspond à chaque requête contenue dans la collection Postman, et fournit les informations ci-dessous :

- **Durée étape** : il s'agit de la durée en millisecondes de l'exécution d'une étape.
- **Assertions des étapes** : les résultats de tests réels basés sur les scripts de pré-requête et de post-réponse, parallèlement aux résultats des tests Postman. Vous pouvez voir le nombre total d'assertions ayant réussi et échoué. Les premières sont marquées par des coches vertes, et les secondes par des croix rouges.
- Vous voyez aussi d'autres détails tels que les en-têtes de requête, le contenu des requêtes et les en-têtes de réponse, de la même façon que dans Postman. Par exemple : Cache-control, Content-Length, Server, Date, etc.

## Crédits

Tout comme avec les moniteurs d'API multi-étapes, le moniteur API Postman utilise des crédits d'API. Chaque requête contenue dans la collection importée correspond à un crédit.