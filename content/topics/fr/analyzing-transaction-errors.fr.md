{
  "hero": {
    "title": "Analyser les erreurs de transaction"
  },
  "title": "Analyser les erreurs de transaction",
  "summary": "Analyser les erreurs de transaction dans votre surveillance de site web avec Uptrends",
  "url": "/support/kb/surveillance-synthetique/transactions/analyser-erreurs-transaction",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/analyzing-transaction-errors"
}

Parfois, les choses ne fonctionnent pas comme nous voudrions - et c'est pareil pour vos transactions surveillées !

## Vérifier les données de sortie HTML

Dans le cas d'une erreur de transaction, le service Uptrends saisit une copie des données de sortie HTML au moment où l'erreur a été détectée. Ces données peuvent être un outil puissant pour apprendre ce à quoi ressemblait une page au moment où un problème est survenu.

**Pour vérifier les données de sortie HTML** :

1.  Connectez-vous à votre compte Uptrends, et accédez au tableau de bord {{< AppElement type="menuitem" >}}Monitor log{{< /AppElement >}} située dans le menu déroulant {{< AppElement type="menuitem" >}}Monitors{{< /AppElement >}} dropdown menu.  

2.  Cliquez sur une erreur de transaction dans la liste ( *soit confirmée soit non-confirmée*).  
      
    {{< callout >}}**Remarque** : Pour les transactions avec une erreur "Navigate", Uptrends ne peut pas fournir de données HTML, car nous avons été incapables d'atteindre ce site.{{< /callout >}} 

3.  Dans la section {{< AppElement type="menuitem" >}}Page Content{{< /AppElement >}} , et à côté de {{< AppElement type="menuitem" >}}HTML Result{{< /AppElement >}} vous pourrez voir les données de sortie HTML.  

4.  Pour voir à quoi la page ressemblait, sélectionnez le bout de code HTML et enregistrez-le (en utilisant le Bloc-notes par exemple) dans un fichier HTML.  

5.  Ouvrez le fichier dans un navigateur pour afficher la page.

## L'erreur est-elle détectée par un seul point de contrôle ?

Si une erreur est seulement détectée par un point de contrôle, cela signifie généralement qu'il peut y avoir un problème de connexion pour les utilisateurs dans cette région, ou un problème technique spécifique à ce point de contrôle.

Dans ce cas, nous vous conseillons [soumettre un ticket de support](/contact) afin que nous puissions enquêter sur le problème.

## Vos informations de connexion sont toujours valides ?

Parfois, les informations de connexion nécessaires dans une transaction à plusieurs étapes peuvent changer d'une étape à l'autre. Si cela se produit, il faut modifier les informations d'identification des transactions en utilisant l'éditeur d'étape de transaction.
