{
  "hero": {
    "title": "Effacer le cache du navigateur"
  },
  "title": "Effacer le cache du navigateur",
  "summary": "Lorsque votre transaction doit recharger des éléments d'une page directement depuis le serveur plutôt que depuis le cache, il est utile d'effacer le cache du navigateur.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/effacer-cache-navigateur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les [moniteurs de transactions]([LINK_URL_1]) d'Uptrends ouvrent toujours un navigateur pour vérifier les performances de votre site web en simulant les activités des utilisateurs. Au départ, le cache du navigateur ne contient aucune donnée. Au fur et à mesure qu'il simule les activités des utilisateurs (par exemple, connexion, défilement des produits et ajout au panier) sur votre site web, le navigateur enregistre temporairement des éléments dans le cache afin de reconnaître toutes les ressources de votre site web. Cette opération accélère le processus de chargement du navigateur lors du prochain passage sur la même page.

Cependant, vous aurez parfois besoin de surveiller différents comportements sur une page web. Effacer le cache du navigateur peut être utile pour comparer le comportement de votre site d'e-commerce selon que les articles du panier d'achats sont ajoutés par des utilisateurs préexistants (avec des données en cache) ou de nouveaux utilisateurs (sans données en cache).

## Action Effacer le cache du navigateur

L'action **Effacer le cache du navigateur** proposée dans les étapes des moniteurs de transactions vous permet d'effacer le cache du navigateur pour recharger les éléments de page directement depuis le serveur, plutôt que depuis le cache. Cette fonctionnalité vous aide à vérifier les performances des premières visites sur votre site web ainsi que le bon chargement des éléments de l'interface (par exemple, images, textes et autres contenus).

[SHORTCODE_1] **Remarque :** Cette action n'utilise aucun crédit de transaction. Servez-vous-en pour répondre à vos besoins de surveillance. Pour en savoir plus, lisez l'article [Comprendre le calcul du nombre de crédits utilisés par les moniteurs de transactions]([LINK_URL_2]). [SHORTCODE_2]

## Ajouter une action Effacer le cache du navigateur

Il existe deux façons d'ajouter une action **Efface le cache du navigateur** dans vos étapes de transaction : vous pouvez passer par [l'éditeur d'étapes de transaction]([LINK_URL_3]) ou par [l'éditeur de script de transaction]([LINK_URL_4]).

### Utilisation de l'éditeur d'étapes de transaction

Pour ajouter l'action **Efface le cache du navigateur** dans **l'éditeur d'étapes de transaction** :

1. Ouvrez [SHORTCODE_3] Transactions > Gérer les transactions [SHORTCODE_4].
2. Cliquez sur le moniteur de transaction auquel vous souhaitez ajouter l'action d'effacement du cache du navigateur.
3. Ouvrez l'onglet [SHORTCODE_5]Étapes[SHORTCODE_6].
4. Ouvrez l'**étape** pour laquelle vous souhaitez ajouter l'action d'effacement du cache du navigateur.
5. Cliquez sur le bouton [SHORTCODE_7] Ajouter une action [SHORTCODE_8].
6. Dans la fenêtre contextuelle **Ajouter une action**, sélectionnez **Effacer le cache du navigateur**.
7. Cliquez sur [SHORTCODE_9] Sélectionnez [SHORTCODE_10].
8. Dans le **champ Paramètres > Description**, ajoutez une description détaillée de l'action ajoutée.
9. Cliquez sur le bouton [SHORTCODE_11] Enregistrer [SHORTCODE_12] pour confirmer les changements apportés.

![GIF Effacer le cache du navigateur]([LINK_URL_5])

### Utilisation de l'éditeur de script de transaction

Pour ajouter l'action **Efface le cache du navigateur** dans **l'éditeur de script de transaction** :

1. Ouvrez [SHORTCODE_13] Transactions > Gérer les transactions [SHORTCODE_14].
2. Cliquez sur le moniteur de transaction auquel vous souhaitez ajouter l'action d'effacement du cache du navigateur.
3. Ouvrez l'onglet [SHORTCODE_15]Étapes[SHORTCODE_16].
4. Dans le coin supérieur droit, cliquez sur le bouton [SHORTCODE_17] Basculer vers le script [SHORTCODE_18].
5. Dans le **script de transaction**, ajoutez l'extrait de code [INLINE_CODE_1] suivant au tableau [INLINE_CODE_2] :

[CODE_BLOCK_1]

6. Cliquez sur le bouton [SHORTCODE_19] Enregistrer [SHORTCODE_20] pour confirmer les changements apportés.

L'action **Effacer le cache du navigateur** fait désormais partie des étapes et s'exécute avec votre moniteur de transaction.
