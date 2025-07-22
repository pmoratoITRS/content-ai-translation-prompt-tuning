{
"hero": {
"title": "Enregistrer un parcours d'utilisation du panier d'achats"
},
"title": "Enregistrer un parcours d'utilisation du panier d'achats",
"summary": "Ce tutoriel vous guide pas à pas dans l'enregistrement d'un parcours d'utilisation du panier d'achats.",
"url": "/support/kb/surveillance-synthetique/transactions/tutorial-record-user-journey-in-shop/enregistrer-votre-transaction",
"translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction",
"tableofcontents": false
}

Cet exemple va vous permettre de passer en revue le processus d'enregistrement du parcours d'un utilisateur qui ajoute et modifie des articles dans son panier d'achats.

Les instructions ci-dessous vous guident de façon détaillée dans un exemple d'enregistrement de transaction. Une fois le moniteur de transaction actif, il utilisera des crédits de transaction que vous devez acheter dans votre compte. Cet exemple inclut des indications sur les étapes qui consomment des crédits. Pour en savoir plus sur les crédits, vous pouvez lire l'article sur le [calcul du nombre de crédits utilisés par les moniteurs de transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}).

1. Trouvez l'enregistreur de transaction d'Uptrends depuis le Chrome Web Store et ajoutez l'extension à votre navigateur Chrome. Les étapes à suivre sont décrites dans l'article [Télécharger et utiliser l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder#download-transaction-recorder" lang="fr" >}}).
2. Dans une fenêtre du navigateur Chrome, ouvrez l'extension de l'enregistreur de transaction et cliquez sur le bouton {{< AppElement type="deletebutton" >}} Start Recording {{< /AppElement >}} (Commencer l'enregistrement). La fenêtre **REC** s'ouvre.
3. Saisissez l'URL [https://galacticshirts.com](https://galacticshirts.com/) dans la barre d'adresse de la fenêtre **REC**.  
   *Cette première transition vers une nouvelle page occasionne une requête à un serveur (nombre de crédits utilisés = 1).*  
   La page d'accueil de la boutique s'affiche.
   ![Capture d'écran de la page d'accueil Galactic Shirts](/img/content/f0180d9f-9bf2-4947-bf11-c47c48afcd23.png)
4. Cliquez sur l'image du premier tee-shirt pour ouvrir la page produit.  
   Le tee-shirt peut être différent, mais il y aura toujours un premier tee-shirt. Dans ce cas, le premier tee-shirt est le "Suraya Bay T-Shirt".  
   *Cliquer sur le lien entraîne une transition vers la page produit et l'envoi d'une requête au serveur. Cette étape utilise un nouveau crédit (nombre de crédits utilisés = 2).*
   Le page produit du tee-shirt s'affiche.
5. Cliquez sur le menu déroulant **Size** (Taille) pour sélectionner la taille **L**.
6. Définissez la quantité sur **2**.
   ![](/img/content/e1b42b45-fb3a-4687-af3e-fba30d780986.png)
   Que vous changiez la quantité en tapant le 2 ou en utilisant les flèches n'a pas d'incidence : l'enregistreur enregistre seulement le clic et le changement de valeur.
7. Cliquez sur **Add to cart** (Ajouter au panier).  
   *Cliquer sur le bouton* Add to cart* entraîne l'envoi d'une requête à un serveur et une actualisation de la page qui utilise un nouveau crédit (nombre de crédits utilisés = 3)*.
8. Ajoutez une vérification de contenu. Il est recommandé de toujours ajouter des [vérifications de contenu]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}) pour vérifier si le résultat de chaque chargement de page se déroule comme attendu. Dans cet exemple, nous voulons vérifier que l'action d'ajout au panier a bien fonctionné (c'est là un exemple des nombreuses vérifications de contenu que vous pouvez ajouter dans votre script). Il existe trois façons d’ajouter une vérification de contenu. Vous pouvez utiliser le bouton **Add content check** (Ajouter une vérification de contenu) ou le menu contextuel. Les vérifications de contenu peuvent aussi être ajoutées ultérieurement au moyen de l’éditeur d’étape du moniteur disponible dans votre compte.

   Pour ajouter une vérification de contenu via le bouton **Ajouter une vérification de contenu** :

   1. Retrouvez la fenêtre d'enregistrement (elle se trouve généralement derrière la fenêtre du navigateur) et cliquez sur {{< AppElement type="editbutton" >}} \+ Ajouter une vérification de contenu{{< /AppElement >}}
      ![capture d'écran d’une vérification de contenu dans l’enregistreur](/img/content/6101d30a-9158-40d0-9b28-d7422f3c94c3.png)

   2. Choisissez une partie de la page de confirmation qui est unique sur la page et peu susceptible de changer. Dans ce cas, vous pouvez choisir "added to your cart" (ajouté au panier). Saisissez ce texte dans la fenêtre contextuelle **Add content check** (Ajouter une vérification de contenu).
      ![Capture d'écran de la fenêtre contextuelle de vérification de contenu](/img/content/scr_transaction-recorder-add-content-check.min.png)
   3. Cliquez sur {{< AppElement type="button" >}}Save{{< /AppElement >}} (Enregistrer).
   4. Revenez à la fenêtre d'enregistrement.

   Pour ajouter une vérification de contenu depuis le menu contextuel :

   1. Sélectionnez le texte "added to your cart".
   2. Effectuez un clic droit et cliquez sur *ITRS Uptrends Transaction Recorder* dans le menu contextuel.
   3. Sélectionnez l’option *Create a content check* (Créer une vérification de contenu). Cette vérification de contenu est désormais enregistrée dans la fenêtre de l’enregistreur de transaction.
   4. Revenez à la fenêtre d'enregistrement.

   ![capture d’écran de l’option de vérification de contenu dans le menu contextuel](/img/content/scr_transaction-recorder-content-check-hover.min.png)

La vérification de contenu a bien été enregistrée.

9. Cliquez sur le bouton **View Cart** (Voir le panier) pour ouvrir le panier d'achats.  
   *Ce clic utilise un nouveau crédit (nombre de crédits utilisés = 4).*
10. Changez la quantité de "2" à "1."
11. Cliquez sur **Update cart** (Actualiser le panier).  
   *L'actualisation du panier met à jour la page, ce qui entraîne l'envoi d'une requête au serveur et l'utilisation d'un nouveau crédit (nombre de crédits utilisés = 5).*
   ![Capture d'écran de l'actualisation du panier d'achats](/img/content/5ba19828-a398-41bd-b67e-e8c615442cb1.png)
12. Ajoutez une vérification de contenu pour vérifier que la page s'est chargée correctement, en testant le texte "Cart updated" (Panier actualisé).
13. Cliquez sur la croix rouge pour retirer l'article du panier d'achats et conclure votre transaction.  
   *La suppression d'un article entraîne l'envoi d'une requête au serveur et l'utilisation d'un crédit (nombre de crédits utilisés = 6).*
14. Ajoutez une vérification de contenu en utilisant la phrase "Your cart is currently empty" (Votre panier est vide).
15. Pour vérifier si votre panier est vide, vous pouvez aussi survoler l’icône en forme de panier dans le coin supérieur droit de l’écran. Notez que l’enregistreur de transaction n’enregistre pas automatiquement une étape lorsque vous survolez les éléments d’un site Web. L’ajout doit être effectué manuellement.

   Pour ajouter une action de survol lors du processus d’enregistrement :
   1. Au moyen d’un clic droit, sélectionnez l’élément à survoler. Dans le cas présent, il s’agit de l’icône en forme de panier.
   2. Dans le menu contextuel, cliquez sur *ITRS Uptrends Transaction Recorder*.
   3. Cliquez sur *Create hover action* (Créer une action de survol). Vous remarquerez que l’étape est désormais enregistrée dans la fenêtre de l’enregistreur de transaction.
   4. Dans cet exemple, lorsque vous survolez l’icône en forme de panier, un message "No products in the cart." (Aucun produit dans le panier) s’affiche. Lorsqu’un survol fait apparaître un élément, vous pouvez aussi suivre l’activité d’un élément qui doit être visible. Pour cela, suivez la même méthode que pour l’action de survol en effectuant un clic droit sur l’élément rendu visible (ici, *"No products in the cart"*) > dans le menu contextuel, cliquez sur *ITRS Uptrends Transaction Recorder* > *Wait for this element to be visible* (Attendre que cet élément soit visible).

   ![capture d’écran du panier vide](/img/content/scr_transaction-recorder-hover.min.png)

L’action de survol et l’élément devant être visible sont désormais enregistrés.

16. Ajoutez une vérification de contenu en utilisant la phrase "No products in the cart.".
17. Maintenant que votre panier d’achats est vide, vous pouvez chercher un autre type de t-shirts au moyen du champ de recherche de produits qui se trouve en haut à droite de l’écran. Saisissez *Summer*. Vous remarquerez que ce champ ne contient pas de bouton de recherche. Vous devez appuyer sur la *touche Entrée* pour générer des résultats de recherche.

   L’enregistreur de transaction peut aussi enregistrer ce type de saisie au clavier effectuée par l’utilisateur. Cette fonctionnalité est pratique lorsqu’un site Web propose des instructions telles que *Appuyez sur n’importe quelle touche pour continuer* ou *Appuyez sur Entrée pour confirmer*. Cependant, contrairement aux actions reposant sur un clic de souris (qui sont automatiquement enregistrées comme un mouvement), vous devez ajouter manuellement l’action de clavier pour qu’elle soit enregistrée comme une activité réelle.

   Pour ajouter une action de clavier au processus d’enregistrement :
   1. Retrouvez la fenêtre d'enregistrement (elle se trouve généralement derrière la fenêtre du navigateur) :
      ![Capture d'écran de l'ajout d'une action de clavier](/img/content/scr_transaction-recorder-add-keyboard-action.min.png)
      Cliquez sur {{< AppElement type="editbutton" >}} \+ Add keyboard action{{< /AppElement >}} (Ajouter une action de clavier).
   2. Une fenêtre contextuelle affiche un menu déroulant qui vous permet de sélectionner la touche du clavier qui vous intéresse. Vous avez le choix entre différents caractères, dont les touches de contrôle, les touches spéciales. les touches numériques, les touches du pavé numériques, les touches majuscules et les touches minuscules.
      ![Capture d'écran de la fenêtre contextuelle permettant d’ajouter une action de clavier](/img/content/scr_transaction-recorder-add-keyboard-action-popup.png)
   3. Indiquez si la sélection de cette touche s’applique tout le temps ou seulement sur l’élément qui vous intéresse. Si vous choisissez l’option *Global*, cette action de clavier est reconnue dans toute l’application. Si vous choisissez *Last clicked element* (Dernier élément cliqué), l’action de clavier s’applique seulement à l’élément indiqué entre parenthèses sur la ligne du bouton radio.
   4. Cliquez sur {{< AppElement type="button" >}}Save{{< /AppElement >}} (Enregistrer) pour revenir à la fenêtre d’enregistrement du navigateur.

   *Chercher un nouveau tee-shirt génère une requête de serveur qui utilise un crédit (nombre de crédits utilisés = 7).*

18. Ajoutez une vérification de contenu pour vérifier que le tee-shirt n’existe pas en testant le texte "No products were found matching your selection." (Aucun produit correspondant à votre sélection n’a été trouvé).
19. Cliquez sur {{< AppElement type="button" >}} Stop recording {{< /AppElement >}} (Arrêter l'enregistrement).
20. Cliquez sur **Upload recording** (Charger l'enregistrement) et indiquez que vous souhaitez d'abord tester et optimiser la transaction vous-même (transaction en libre-service). Pour connaître la différence entre les transactions en service complet et en libre-service, référez-vous à l'article de la base de connaissances intitulé [Options pour les scripts de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="fr" >}}).

Vous avez maintenant terminé l'enregistrement du parcours d'utilisation du panier d'achats. Cette procédure aura créé un nouveau moniteur de transaction dans votre compte Uptrends. Ce moniteur de transaction utiliserait généralement sept crédits de transaction, mais d'autres facteurs influent sur le [calcul des crédits]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="fr" >}}).

La prochaine tâche consiste à tester votre transaction et à l'ajuster si nécessaire. Pour réaliser ce test, vous pouvez suivre les instructions présentées dans l'article [Tester et modifier votre script de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="fr" >}}).
