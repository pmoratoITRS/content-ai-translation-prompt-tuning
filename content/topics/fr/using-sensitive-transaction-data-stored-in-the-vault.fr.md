{
"hero": {
"title": "Comment utiliser les données de transaction sensibles stockées dans le coffre-fort"
},
"title": "Comment utiliser les données de transaction sensibles stockées dans le coffre-fort",
"summary": "Lorsque vous enregistrez une transaction, Uptrends enregistre vos informations sensibles dans le coffre-fort Uptrends. Découvrez comment utiliser vos données sensibles dans vos scripts de transaction.",
"url": "/support/kb/surveillance-synthetique/transactions/utiliser-donnees-de-transaction-sensibles-du-coffre-fort",
"translationKey": "https://www.uptrends.com/support/kb/transactions/using-sensitive-transaction-data-stored-in-the-vault"
}

Le coffre-fort Uptrends stocke les informations confidentielles dont vous avez besoin pour votre surveillance en toute sécurité, accessibles seulement par les opérateurs autorisés. Lorsque vous enregistrez une nouvelle transaction ou qu'Uptrends convertit une transaction plus ancienne en une transaction en libre-service, Uptrends place toutes les informations sensibles telles que les mots de passe dans le coffre-fort.

## Accéder à vos nouveaux éléments de coffre-fort

Pour accéder aux éléments de votre coffre-fort, allez à {{< AppElement type="menuitem" >}} Configuration de compte > Coffre-fort {{< /AppElement >}}. À l'intérieur du coffre-fort, vous allez trouver vos nouveaux éléments dans des *Éléments de coffre-fort créés automatiquement*. L'élément du coffre-fort aura le même nom que le moniteur lorsque vous l'avez créé pour la première fois, ou lorsqu'il a été converti par un membre de notre équipe d'assistance.

## Modification de vos nouveaux éléments de coffre-fort

Si vous avez l'autorisation d'accéder et modifier une section du coffre-fort, vous pouvez ouvrir l'élément et ajuster le nom, la description et le nom d'utilisateur. Le mot de passe est modifiable mais non visible.

![](/img/content/bce5dcae-cd73-4d14-b45d-5eec4a2f703c.png)

## Utilisation d'un élément de coffre-fort dans votre script

Votre script importé fait déjà référence à l'élément de coffre-fort ; vous modifier les informations d'identification directement dans le coffre-fort. Vous pouvez modifier l'élément de coffre-fort auquel votre script accède en cliquant sur le bouton à points de suspension dans le champ de saisie. La boîte de dialogue contextuelle vous permet de passer à une valeur de texte brut, de sélectionner un autre élément de coffre-fort ou d'ajouter un nouvel élément de coffre-fort.

![](/img/content/scr_MSA_predefined_variables_1.min.png)

Nous avons un [article spécial](/support/kb/coffre-fort) pour vous donner plus de détails sur l'utilisation du coffre-fort pour protéger à la fois les informations d'identification, les clés publiques et les certificats.  L'équipe de [Support Uptrends](/contact) peut également vous aider avec toutes les questions que vous pourriez avoir.
