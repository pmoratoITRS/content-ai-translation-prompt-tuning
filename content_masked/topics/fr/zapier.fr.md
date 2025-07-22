{
  "hero": {
    "title": "Intégrer Uptrends avec Zapier"
  },
  "title": "Zapier",
  "summary": "Découvrez comment intégrer vos alertes Uptrends dans Zapier",
  "url": "[URL_BASE_TOPICS]alerter/integrations/zapier",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Zapier** est un outil d'automatisation en ligne qui connecte vos applications et services. Cet outil vous permet de connecter vos alertes Uptrends à pratiquement n'importe quelle autre application. Dans cet article, nous vous aidons à configurer votre intégration Uptrends avec Zapier, puis nous vous montrons où vont ensuite vos données.

1. Mise en place d'une action *When this happens* (Quand ceci arrive) dans Zapier.
2. Configuration de l'intégration dans Uptrends
3. Test du webhook dans Zapier
4. Configuration d'une action *Do This…* (Il faut faire cela) dans Zapier
5. Ajout de l'intégration à une définition d'alerte dans Uptrends

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Mise en place d'une action "When this happens" (Quand ceci arrive) dans Zapier.

1. Dans Zapier, les flux d'actions automatisés sont appelés des *Zaps*. Allez à *Zaps* et cliquez sur *Create Zap*. Sinon, cliquez sur le bouton *MAKE A ZAP* en haut à gauche de l'écran.
2. Donnez à votre nouveau Zap un nom parlant.
3. Sélectionnez *Webhooks by Zapier*.
4. Sélectionnez *Catch hook* puis cliquez sur *Continue*.
5. Prenez note de l'**URL du webhook personnalisée** car vous en aurez besoin pour configurer l'intégration dans Uptrends.
6. Cliquez sur *Continue*.

À ce stade, Zapier vous demandera de tester le webhook en lui envoyant des données. Pour ce faire, nous devons d'abord configurer l'intégration Uptrends.

## 2. Configuration de l'intégration dans Uptrends

1. Ouvrez [SHORTCODE_3] Alerte > Intégrations [SHORTCODE_4].
2. Cliquez sur [SHORTCODE_5]Ajouter intégration[SHORTCODE_6] en haut à droite.
3. Choisissez Zapier comme type d'intégration.
4. Donnez un nom à cette intégration.
5. Prenez l'**URL du webhook personnalisée** que vous avez enregistrée plus tôt, et collez-la dans le champ correspondant des [SHORTCODE_7]Variables prédéfinies[SHORTCODE_8].
6. Cliquez sur [SHORTCODE_9]Enregistrer[SHORTCODE_10] pour enregistrer vos paramètres. La nouvelle intégration Zapier apparaîtra sur la page Intégrations.

## 3. Test du webhook dans Zapier

1. Allez à la nouvelle intégration **Zapier** dans Uptrends.
2. Dans l'onglet [SHORTCODE_11]Personnalisations[SHORTCODE_12], cliquez sur le bouton [SHORTCODE_13]Envoyer une alerte de test[SHORTCODE_14].
3. Cliquez sur [SHORTCODE_15]Démarrer le test[SHORTCODE_16] pour envoyer une alerte de test au webhook Zapier. Peu importe le *type d'alerte* que vous sélectionnez.
4. Dans Zapier, cliquez sur le bouton *Test trigger*. Cette action forcera Zapier à examiner les données entrantes envoyées à l'étape précédente, et à analyser son corps JSON. Nous pourrons nous référer aux champs individuels dans le message sortant plus tard.![]([LINK_URL_1])
5. Cliquez sur le bouton *Continue* dans Zapier.

## 4. Configuration d'une action "Do This…" (Il faut faire cela) dans Zapier

### Exemple 1 : Intégration de messagerie via Zapier

À titre d'exemple, commençons par configurer une intégration de messagerie simple via Zapier.

1. Dans Zapier, recherchez et sélectionnez l'application intégrée *Email by Zapier*.
2. Cliquez sur *Continue*.
3. Ajoutez votre adresse e-mail dans le champ **To**.
4. Les champs **Subject** et **Body** peuvent être personnalisés à l'aide des données Uptrends entrantes. Puisque Zapier a reçu et analysé une alerte de test à l'étape 3, il connaît déjà les données contenues dans les alertes Uptrends entrantes. Lorsque vous cliquez sur l'un des champs, une liste intitulée **Insert data** apparaît, à partir de laquelle vous pouvez sélectionner des références aux valeurs incluses dans une alerte Uptrends. Lorsque Zapier envoie le message sortant, il insère automatiquement les valeurs correctes.![]([LINK_URL_2])
5. Après avoir personnalisé le message sortant, cliquez sur le bouton *Continue*.
6. Si vous le souhaitez, vous pouvez tester le message sortant dans cette fenêtre. Le test devrait vous envoyer immédiatement un e-mail contenant des données fictives.![]([LINK_URL_3])
7. Terminez la configuration de l'intégration dans Zapier en cliquant sur **TURN ON ZAP**.

### Exemple 2 : Intégration de Trello via Zapier

Votre intégration Zapier peut faire bien plus encore. Comme deuxième exemple, examinons la configuration d'une intégration avec Trello. Vous devrez connecter votre compte Trello à Zapier. Pour cela, passez par l'option *My Apps* dans le menu latéral de Zapier.

1. Ajoutez un nouveau Zap en suivant les étapes décrites dans la section 1 (*Mettre en place une action "When this happens…" (Quand ceci arrive) dans Zapier*) ci-dessus.
2. Vous obtenez une nouvelle **URL de webhook personnalisée**. Cette nouvelle URL de webhook doit être ajoutée à une intégration distincte dans Uptrends. Suivez les instructions de l'étape 2 pour configurer une nouvelle intégration dans Uptrends, mais assurez-vous d'utiliser cette nouvelle URL de webhook.
3. Reproduisez les actions décrites à l'étape 3 pour envoyer des données de test à ce nouveau webhook, afin que Zapier puisse analyser les données entrantes. En bref : dans l'onglet [SHORTCODE_17]Personnalisations[SHORTCODE_18], cliquez sur le bouton [SHORTCODE_19]Envoyer une alerte de test[SHORTCODE_20]. Dans Zapier, cliquez sur le bouton *Test trigger*. Terminez en cliquant sur *CONTINUE*.
4. Pour configurer l'intégration avec Trello, sélectionnez l'application *Trello* sous **Your Apps**.
5. Vous pouvez sélectionner l'action exacte à effectuer dans Trello lorsqu'une alerte Uptrends est reçue. Pour cet exemple, choisissons *Create Card*. Cliquez sur *CONTINUE* dans la fenêtre suivante.
6. Sélectionnez le compte Trello connecté et cliquez sur *CONTINUE*.
7. Choisissez les **tableaux** et les **listes** qui vous intéressent. Renseignez le champ **Description** pour la carte à créer. Une fois de plus, vous pouvez personnaliser entièrement le contenu, en utilisant les données d'alerte Uptrends précédemment analysées par Zapier. Définissez les autres options au besoin et terminez en cliquant sur *CONTINUE*.![]([LINK_URL_4])
8. Si vous le souhaitez, vous pouvez tester le message sortant dans cette fenêtre.![]([LINK_URL_5])
9. Terminez la configuration de l'intégration dans Zapier en cliquant sur **TURN ON ZAP**.

[SHORTCODE_1]
**Astuce :** Cet article ne fournit que deux exemples, mais Zapier vous permet de transmettre vos alertes Uptrends vers pratiquement n'importe quelle plateforme externe.
[SHORTCODE_2]

## 5. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu [SHORTCODE_21] Alerte > Définitions d'alerte [SHORTCODE_22], sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet [SHORTCODE_23]Niveau d'escalade[SHORTCODE_24] contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]([LINK_URL_6]).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, sélectionnez **l'intégration personnalisée** pour Zapier.
4. N'oubliez pas de cliquer sur le bouton [SHORTCODE_25]Enregistrer[SHORTCODE_26] pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration de Zapier.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support]([LINK_URL_7]).
