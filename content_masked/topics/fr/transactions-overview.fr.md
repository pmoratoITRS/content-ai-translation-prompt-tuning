{
  "hero": {
    "title": "Vue d'ensemble de la surveillance des transactions"
  },
  "title": "Vue d'ensemble de la surveillance des transactions",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/apercu-du-suivi-des-transactions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

La surveillance des transactions, également connue sous le nom de surveillance des applications web, est utilisée pour vérifier le bon fonctionnement des interactions des utilisateurs de votre site web. L'interaction peut être une simple connexion ou toutes les actions nécessaires à l'achat d'un produit dans votre boutique en ligne.

Pour surveiller ces interactions d'utilisateurs, il faut les placer dans un script qui peut être exécuté à plusieurs reprises pour vérifier si tout fonctionne toujours comme prévu. Uptrends fournit un enregistreur de transaction (en tant qu'extension Chrome) pour construire un script de manière simple. Une fois que vous avez enregistré le script, vous pouvez l'affiner vous-même (transactions en libre-service) ou demander au support Uptrends de l'affiner (transactions en service complet). Si vous savez écrire les scripts, vous pouvez décider d'omettre l'enregistrement et placer directement votre propre script dans un moniteur de transaction.

Lorsque vous chargez l'enregistrement d'une transaction vers votre compte Uptrends, un moniteur de transaction est créé avec quelques informations de base. Il vous faut ensuite ajuster certains paramètres en fonction de vos besoins.

Une fois que vous avez testé votre moniteur de transaction et que son fonctionnement vous convient, mettez en place des [alertes]([LINK_URL_1]) pour ce moniteur. Après tout, c'est de cela qu'il s'agit : recevoir des alertes lorsque quelque chose ne fonctionne pas comme prévu.

[SHORTCODE_1]
Notre tutoriel [Parcours d'utilisation du panier d'achats]([LINK_URL_2]) vous guide pas à pas dans la mise en place de la surveillance des transactions et la vérification des données de surveillance.
[SHORTCODE_2]

## 1. Introduction

Si vous débutez dans la surveillance des applications/transactions web, les articles suivants vous donneront de bonnes bases :

- Apprenez le B.A.BA en lisant l'article [Qu'est-ce que la surveillance de site web ?]([LINK_URL_3])
- Découvrez [pourquoi vous avez intérêt à utiliser la surveillance d'applications web]([LINK_URL_4]).
- Vérifiez si la surveillance des applications web est [la bonne solution]([LINK_URL_5]) pour vous.

## 2. Planifier la surveillance de vos transactions

Comprendre la mécanique de vos transactions, les fonctionnalités à tester et l'impact de la surveillance sur vos systèmes est une part cruciale de la planification de vos transactions. Il sera peut-être également nécessaire d'impliquer d'autres équipes de votre entreprise dans la mise en place d'une surveillance des transactions.

- [Cartographiez les différents chemins de transaction possibles]([LINK_URL_6]).
- Déterminez [ce que vous allez tester]([LINK_URL_7]).
- Lisez nos [mises en garde et astuces]([LINK_URL_8]) qui recensent les éléments à prendre en compte et à surveiller lors de la mise en place de votre surveillance.
- Sachez [dans quels cas]([LINK_URL_9]) vous pourriez avoir besoin de l'aide d'autres équipes de votre entreprise.

## 3. Enregistrer vos transactions

Une utilisation correcte de l'[enregistreur de transaction]([LINK_URL_10]) donne des enregistrements plus propres et une configuration du moniteur plus efficace.

- [Téléchargez et utilisez l'enregistreur de transaction]([LINK_URL_11])
- Apprenez à utiliser l'enregistreur de transaction en suivant le [tutoriel sur le parcours d'utilisation du panier d'achats]([LINK_URL_12]).
- Choisissez les [transactions en libre-service ou en service complet]([LINK_URL_13]).

## 4. Tester et modifier vos scripts de transaction

Une fois votre transaction enregistrée et le moyen de tester le script choisi (par vous-même ou par notre équipe de support), vous devez résoudre les problèmes dans le script, configurer les vérifications de contenu si ce n'est pas déjà fait, et définir les autorisations du coffre-fort sur les éléments nouvellement créés. Enfin, vous devez suivre de près le moniteur en mode "simulation" avant de le déplacer vers la production.

- Pour en savoir plus sur l'éditeur, les étapes et les actions, lisez l'article [Comprendre l'éditeur d'étapes]([LINK_URL_14])

- Les actions sont au cœur des transactions. Apprenez-en plus à leur sujet dans les articles suivants :
   - [Interactions de page : naviguer, cliquer, définir, etc.]([LINK_URL_15])
   - [Actions de test : vérifications de contenu et délais d'attente]([LINK_URL_16])
   - [Actions de contrôle : changement de cadre (intégré) ou d'onglet]([LINK_URL_17])
   - [Actions de contrôle : ajustement du contenu d'une variable]([LINK_URL_18])
   - [Ignorer les erreurs pour les étapes et actions facultatives]([LINK_URL_19])
   - [Utilisation des sélecteurs]([LINK_URL_20]) et des [sélecteurs alternatifs]([LINK_URL_21])
   - [Utilisation de variables dans les transactions]([LINK_URL_22]) et [ajustement des variables de transaction]([LINK_URL_23])

- Dans l'exercice [Tester et modifier votre script de transaction]([LINK_URL_24]), vous pouvez expérimenter la fonction *Tester maintenant* et apprendre à gérer les erreurs liées aux ID dynamiques et à l'expiration des temps d'attente. Cet exercice contient également une [checklist pour le test]([LINK_URL_25]).

- En fonction de votre configuration et de vos transactions, vous aurez peut-être à gérer également :
   - [Les valeurs sensibles]([LINK_URL_26]) qui ont été automatiquement ajoutées au coffre-fort lors de l'enregistrement
   - [Les autorisations du coffre-fort (sections créées automatiquement)]([LINK_URL_27])
   - La surveillance des transactions pour les [appareils mobiles]([LINK_URL_28])
   - L'utilisation d'un [DOM fantôme]([LINK_URL_29]) pour votre transaction
   - L'utilisation de la [double authentification par SMS]([LINK_URL_30]) ou de la [double authentification basée sur un mot de passe à usage unique]([LINK_URL_31]) pour votre transaction

   - L'ajout de [métriques supplémentaires]([LINK_URL_32]) telles que les [Core Web Vitals]([LINK_URL_33]) et les [durées de navigation du W3C]([LINK_URL_34]) aux résultats relatifs à vos transactions

   - Le contournement ou le remplacement du système DNS classique par l'application d'un [contournement DNS]([LINK_URL_35]) à votre transaction

## 5. Résultats de la surveillance des transactions

Une fois vos transactions surveillées, vous recevrez des retours. En cas de problème, plusieurs ressources peuvent vous aider à comprendre ce qui ne va pas.

- [Les captures d'écran]([LINK_URL_36])

- [Les graphiques en cascade]([LINK_URL_37])

- [Les durées de navigation du W3C]([LINK_URL_38])

- [Les Core Web Vitals]([LINK_URL_39])

- [L'analyse des erreurs]([LINK_URL_40])

## 6. Dépannage

Lorsque la surveillance des transactions ne fonctionne pas comme prévu, voici quelques points à vérifier :

- [Excluez les tests A/B]([LINK_URL_41])

- [Utilisez le mode de navigation privée]([LINK_URL_42])

- [Lisez nos mises en garde et astuces]([LINK_URL_43])

## Crédits

Créer des moniteurs de transactions et planifier leur exécution utilisent des crédits de transaction. Uptrends utilise des crédits pour calculer le prix des différents services de surveillance. Pour en savoir plus, vous pouvez lire l'article de notre base de connaissances sur les [crédits]([LINK_URL_44]).
