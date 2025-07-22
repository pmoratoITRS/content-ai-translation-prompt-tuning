{
"hero": {
"title": "Ajuster une variable de transaction"
},
"title": "Ajuster une variable de transaction",
"summary": "Lors de la configuration de vos moniteurs de transactions, vous pouvez avoir besoin d'extraire et d'ajuster des variables. L'action de contrôle *Ajuster le contenu d'une variable* vous permet de modifier du contenu préalablement extrait. ",
"url": "/support/kb/surveillance-synthetique/transactions/action-ajuster-contenu-variable",
"translationKey": "https://www.uptrends.com/support/kb/transactions/action-adjust-variable-content"
}

L'action de transaction du type **Ajuster le contenu d'une variable** vous permet de modifier la valeur d'une variable définie dans une action [**Tester le contenu de l’élément**]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks#test-element-content" lang="fr" >}}) d'une étape de moniteur de transaction. L'ajustement se fait au moyen des expressions régulières (RegEx). Modifier une valeur de variable peut être utile si vous avez besoin d'utiliser seulement une partie ou une partie ajustée de la valeur dérivée d'un élément de page.

{{< callout >}} **Remarque** : L'ajustement d'une variable remplacera la valeur originale de la variable. La variable (ajustée) s'applique à partir de l'action où elle a été définie ou ajustée, et se retrouve dans toutes les actions et étapes suivantes jusqu'au bout de la transaction. {{< /callout >}}

## Définir une variable {id="defining-the-variable"}

Pour en savoir plus sur la configuration d'une variable de transaction, consultez l'article de notre base de connaissances sur [l'utilisation des variables dans les transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="fr" >}}).

## Ajuster une variable {id="adjust-variable"}

La deuxième partie consiste à ajouter une action *Ajuster le contenu de la variable* à l'étape :

1. Ouvrez le moniteur de transaction à modifier.
2. Ouvrez l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}.
3. Ouvrez l'étape à laquelle vous voulez changer une variable.
4. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter une action {{< /AppElement >}}.
5. Dans la liste des actions **Contrôle**, choisissez l'action *Ajuster le contenu de la variable* et cliquez sur le bouton {{< AppElement type="button" >}} Sélectionnez {{< /AppElement >}} pour ajouter l'action à l'étape.

   ![capture d'écran de l'action ajuster le contenu de la variable](/img/content/scr_transaction-action-transform-variable.min.png)

   Les valeurs *Variable*, *Type d'ajustement* et *Modèle d'expression régulière* sont obligatoires. Les autres paramètres sont facultatifs.

6. Indiquez le nom de la variable en utilisant le format `{{name}}`. Le nom doit être exactement le même que dans la [définition de la variable](#defining-the-variable). Le nom est sensible à la casse.
7. Choisissez le *type d'ajustement*, à savoir :  
   \- **Conserver tout ce qui correspond à un modèle** : pour extraire une valeur de la variable qui correspond à la valeur du *modèle d'expression régulière*  
   \- **Supprimer tout ce qui correspond à un modèle** : pour extraire tout le contenu sauf la partie qui correspond à la valeur du *modèle d'expression régulière*
8. Saisissez l'expression régulière (RegEx) qui devrait être utilisée pour ajuster la variable.
   Par exemple, si la valeur de la variable est initialement "Votre numéro de commande est 12345" et sachant que votre numéro de commande comprend toujours cinq chiffres, vous pourriez modifier la variable de façon à garder uniquement le numéro de commande en utilisant l'option *Conserver tout ce qui correspond à un modèle* en combinaison avec l'expression régulière `\d{5}` comme *modèle d'expression régulière* qui cherchera une série de cinq chiffres.
9. Assurez-vous que l'ajustement de la variable est réalisé après avoir défini la variable. Si nécessaire, vous pouvez déplacer les actions dans une étape.
10. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour enregistrer vos changements.r

La valeur de la variable ajustée est désormais disponible dans toutes les actions et étapes consécutives jusqu'à la fin de la transaction. Pour faire référence à la variable, utilisez le nom original ({{name}}) que vous avez donné lors de la définition de la variable. Consultez notre article sur [l'action Définir]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="fr" >}}) pour savoir comment utiliser la variable pour définir une valeur dans une autre étape ou action.
