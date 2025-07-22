{
"hero": {
"title": "Vérifications de contenu"
},
"title": "Vérifications de contenu",
"summary": "Plusieurs points doivent être pris en compte lors de la configuration des moniteurs de transactions.",
"url": "/support/kb/surveillance-synthetique/transactions/verification-contenu",
"translationKey": "https://www.uptrends.com/support/kb/transactions/content-checks"
}

Pour assurer le bon déroulement de votre transaction, les *vérifications de contenu* sont l'outil le plus précieux à votre disposition. Une vérification de contenu bien utilisée peut faire toute la différence dans une transaction. En général, le but des vérifications de contenu est de vérifier que l'action précédemment exécutée (par exemple, cliquer sur un lien, se connecter/déconnecter, naviguer vers une page) s'est déroulée comme attendu. Dans la mesure où les moniteurs de transactions s'exécutent à l'aide d'un script, l'ajout d'une vérification de contenu est inestimable pour garantir le bon déroulement de la transaction et obtenir des informations précises concernant votre site web.

**Les vérifications de contenu sont gratuites, nous vous encourageons donc à les utiliser !** Elles ajoutent de la valeur à votre moniteur de transaction après toute action qui génère un nouveau contenu sur la page.

La vérification de contenu incluse dans votre script de transaction attend le chargement du contenu indiqué, ce qui vous donne deux avantages supplémentaires :

- Tout d'abord, vous pouvez savoir avec certitude que la navigation s'est terminée sur la bonne page en vérifiant la présence de contenu spécifique à la page.
- Ensuite, vous pouvez vous assurer que la page s'est chargée correctement et complètement en attendant la fin du chargement de l'élément indiqué. Le fait de vérifier que l'élément a terminé son chargement permet d'éviter que la transaction ne passe trop rapidement à l'action suivante.

## Quand utiliser les vérifications de contenu

En général, le but d'une vérification de contenu est de vérifier la réussite de l'action précédemment exécutée. Il est donc conseillé d'ajouter des vérifications de contenu après toute action qui modifie le contenu de la page de quelque manière que ce soit. Grâce à la vérification de contenu, vous pouvez tester explicitement si des actions spécifiques du script ont eu le résultat souhaité dans le navigateur. Exemples de cas d'utilisation d'une vérification de contenu :

- après la saisie des identifiants et le clic sur le bouton de connexion ;
- après un clic sur un lien de produit sur un site de commerce en ligne ;
- après la déconnexion ;
- après une navigation vers une nouvelle page.

Vous pouvez également utiliser une vérification de contenu pour vérifier qu'un champ de texte rempli automatiquement a fonctionné, qu'un tableau a été correctement rempli avec des données ou qu'un script a été exécuté avec succès.

## Comment ajouter des vérifications de contenu

Vous pouvez ajouter des vérifications de contenu pendant [l’enregistrement]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks#use-content-checks" lang="fr" >}}) ou au moyen de l’éditeur d’étape de moniteur, comme indiqué ci-dessous.

Pour ajouter une vérification de contenu :

1. Ouvrez le moniteur de transaction à modifier.
2. Ouvrez l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}}.
3. Ouvrez l'étape à laquelle vous voulez ajouter une action de vérification de contenu.
4. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter une action {{< /AppElement >}}. Dans la liste des actions disponibles, vous remarquerez que les vérifications de contenu sont identifiées au moyen d'une mention "test" en vert.
   ![capture d'écran ajouter une vérification de contenu dans une transaction](/img/content/scr_transaction-add-content-check.min.png)
5. Sélectionnez le type d'action approprié dans la fenêtre contextuelle. Après avoir effectué votre sélection, la nouvelle action apparaît dans l'éditeur.
   ![capture d'écran de la configuration d'une vérification de contenu dans une étape de transaction](/img/content/scr_transaction-content-check-element.min.png)
   Cette capture d'écran montre le type d'action *Contenu de l'élément de test* (ou Tester le contenu de l'élément).
6. Définissez les paramètres de votre vérification de contenu. Les options de paramétrage varieront selon le type d'action sélectionné. Reportez-vous à la rubrique [Types de vérifications de contenu]({{< ref path="#content-check-types" lang="fr" >}}) pour en savoir plus sur les options disponibles pour chaque type.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour enregistrer vos changements.r

Les instructions ci-dessous s'appliquent à l'éditeur visuel. Vous pouvez aussi ajouter ou modifier des étapes à l'aide de [l'éditeur textuel]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="fr" >}}).

## Types de vérifications de contenu {id="content-check-types"}

Vous avez le choix entre plusieurs types de vérifications de contenu.

### Contenu de l'élément de test {id="test-element-content"}

Pour le type de test *Contenu de l'élément de test* (ou Tester l'élément de contenu), Uptrends vérifie un élément spécifique sur la page pour le contenu indiqué. La vérification *Contenu de l'élément de test* permet d'effectuer des contrôles plus spécifiques et plus robustes que la vérification *Tester le contenu du document*. Dans la plupart des cas, nous vous recommandons d'utiliser le type *Contenu de l'élément de test*. Le type *Contenu de l'élément de test* nécessite que vous pointiez sur un élément spécifique de la page à l'aide d'un sélecteur CSS ou XPath et que vous définissiez une chaîne que l'élément doit contenir. Vous pouvez ainsi effectuer des contrôles très robustes qui vérifient la réussite des actions exécutées par le script.

L'action *Contenu de l'élément de test* nécessite l'utilisation d'un sélecteur CSS ou XPath pour pointer vers un élément spécifique dont vous souhaitez vérifier le contenu.

![capture d'écran de la partie supérieure de l'action contenu de l'élément de test](/img/content/scr_transaction-action-content-check-main.min.png)

Utilisez le menu déroulant pour choisir l'un des deux types de sélecteurs. Pour en savoir plus sur les sélecteurs, consultez les articles de notre base de connaissances sur [l'utilisation des sélecteurs]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="fr" >}}) et les [sélecteurs alternatifs]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}).

Après avoir sélectionné et défini un type de sélecteur (CSS/XPath), vous pouvez choisir l'une des conditions de correspondance suivantes :

- contient ;
- ne contient pas (vous pouvez aussi [tester l'absence de contenu]({{< ref path="#negation-content-checks" lang="fr" >}})) ;
- correspond à l'expression régulière ;
- ne correspond pas à l'expression régulière (de même, vous pouvez aussi [tester l'absence de contenu]({{< ref path="#negation-content-checks" lang="fr" >}})).

Pour terminer la configuration, saisissez le texte à vérifier pour l'élément indiqué dans le champ **exemple de texte**.

Les autres paramètres d'action sont facultatifs.

**Description** : Ajoutez une description de votre vérification de contenu, telle que "Tester si la connexion a réussi".

**Message d'échec** : Précisez le message à afficher si cette vérification de contenu génère une erreur, tel que "La connexion n'a pas réussi".

**Attendre jusqu'à** : Définissez la condition d'attente pour cette vérification. Reportez-vous à l'article [Comment utiliser les conditions d’attente]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}) pour en savoir plus. Remarque : L'option Attendre jusqu'à n'est pas disponible pour le type d'action *Tester le contenu du document*.

**Délai d'attente** : Précisez combien de temps, en millisecondes, Uptrends doit attendre que le contenu apparaisse. La valeur par défaut est de 30 secondes. Dans la plupart des cas, nous vous recommandons de vous en tenir à la valeur par défaut. Cependant, dans certains cas, il peut être utile d'augmenter le délai d'attente. La valeur maximale du délai d'attente est de 60 secondes. N'augmentez pas trop ce délai, car il existe une limite supérieure absolue à la durée d'une transaction complète. Sachez aussi que l'augmentation ou la diminution du délai d'attente n'affecte pas la mesure des métriques de durée de la transaction.

**Affecter une variable** : Saisissez un nom de variable au format `{{name}}`. Pour en savoir plus, consultez notre article sur [l'utilisation des variables dans les transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transaction-variables" lang="fr" >}}).

**Hôte DOM fantôme** : cette option vous permet de préciser un hôte [DOM fantôme]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="fr" >}}), voire des DOM fantômes imbriqués.

Si vous utilisez directement le script de transaction JSON dans [l'éditeur textuel]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="fr" >}}), le type de vérification *Contenu de l'élément de test* doit être défini au format suivant :

```json
{
  "testElementContent": {
    "value": "Example text",
    "testType": "Contains",
    "element": {
      "xpath": "[@id='exampleId']",
      "alternatives": [],
      "shadowRoots": []
    },
    "timeoutMs": 3000,
    "description": "Description of this action"
  }
}
```

Les paramètres facultatifs, comme `timeoutMs`, `description` et `failureMessage`, peuvent être omis. Les valeurs des paramètres disponibles pour `testType` sont `Contains` (contient), `DoesNotContain` (ne contient pas), `MatchesRegex` (correspond à l'expression régulière) et `DoesNotMatchRegex` (ne correspond pas à l'expression régulière). Cet exemple vérifie que l'élément avec le sélecteur XPath `//*[@id='exampleId']` contient la chaîne "Example text". Bien sûr, un sélecteur CSS fonctionnera aussi, et il suffira d'utiliser la valeur `"css": "#exampleId"` au lieu de `"xpath": "[@id='exampleId']"`.

### Tester le contenu du document

Le type d'action *Tester le contenu du document* est le plus simple. L'action *Tester le contenu du document* recherche le contenu spécifié n'importe où dans le document de la page, que le contenu soit visible ou pas. En effet, tout le texte existant dans le document de page ou le DOM n'apparaît pas sur la page. Cependant, puisque le type de test *Tester le contenu du document* vérifie le document HTML plutôt que la page lorsque le navigateur charge le contenu, il est possible de vérifier le texte "invisible". Puisque le type *Tester le contenu du document* ne vérifie pas le contenu de la page chargée, vous ne pouvez pas utiliser de sélecteurs XPath ou CSS pour pointer vers un élément spécifique. Cependant, nous prenons en charge l'utilisation d'une expression régulière pour rechercher des motifs spécifiques dans le contenu DOM.

Si vous choisissez de travailler directement avec le script de transaction JSON plutôt que d'utiliser l'éditeur visuel, l'action *Tester le contenu du document* doit avoir le format suivant :

```json
    {
    "testDocumentContent": {
      "value": "Example content in the DOM",
      "testType": "Contains",
      "timeoutMs": 30000,
      "description": "This check will test the page DOM for the specified content.",
      "failureMessage": "Example failure message"
      }
    }
```

Notez que les paramètres `timeoutMs`, `description`, et`failureMessage` sont facultatifs, et que vous pouvez donc les omettre.

### Attendre l'élément

Le type de test *Attendre l'élément* est identique au type de test *Contenu de l'élément de test*, sauf que dans ce cas, l'élément n'a pas besoin de contenir du texte. Vous pouvez utiliser le test *Attendre l'élément*pour vérifier des éléments vides, tels que des éléments &lt;div&gt; sans texte, des images et des boutons.

Si vous choisissez de travailler directement avec le script de transaction JSON, l'option *Attendre l'élément* doit avoir le format suivant :

```json
    {
      "waitForElement": {
        "element": {
          "xpath": "//*[@id='exampleId']"
        },
        "timeoutMs": 30000,
        "description": "Verify that the element with the indicated XPath selector exists on the page.",
        "failureMessage": "Example failure message"
      }
    }
```

Notez que les paramètres `timeoutMs`, `description`, et`failureMessage` sont facultatifs, et que vous pouvez donc les omettre.

## Tester l'absence de contenu {id="negative-content-checks"}

Au lieu de vérifier qu'un contenu spécifique **existe** dans le DOM ou apparaît sur la page, vous pouvez aussi vérifier qu'un certain contenu **n'existe pas** sur la page. Par exemple, vous souhaiterez peut-être recevoir une alerte si un message d'erreur spécifique apparaît sur votre page. Il s'agit donc de *tester une absence de contenu*. Si le contenu spécifié apparaît sur la page, le moniteur génère une erreur.

Pour utiliser une vérification d'absence de contenu, ajoutez soit un type de vérification *Tester le contenu du document* ou un type *Contenu de l'élément de test*. Ensuite, remplacez la condition de correspondance par défaut **contient** par **ne contient pas** ou**ne correspond pas à l'expression régulière**.

Lors de l'utilisation d'une vérification d'absence de contenu, si la transaction rencontre l'élément ou le contenu spécifié, elle s'arrête et renvoie une erreur. Si l'élément ou le contenu n'apparaît pas, la transaction se poursuit normalement.

## Efficacité des vérifications de contenu

Afin de garantir les meilleurs résultats pour votre vérification de contenu, sélectionnez un élément unique sur la page qui contient un texte unique produit par l'action précédente. Une vérification de contenu utile doit permettre de tester une action de façon bien définie et non ambiguë. Pour la plupart des vérifications de type *Contenu de l'élément de test*, il s'agit de trouver une combinaison robuste et unique entre un **sélecteur** et une **valeur textuelle**.

### Valeur textuelle

La sélection d'une valeur de texte unique à tester est essentielle à la fois pour les types de vérifications *Contenu de l'élément de test* et *Tester le contenu du document*. Il n'est pas nécessaire de sélectionner des valeurs textuelles pour la vérification *Attendre l'élément* car ce test ne fait pas de vérification de texte.

Lors de la sélection du texte pour la vérification, assurez-vous que le texte est une conséquence directe de l'action qui précède. Par exemple :

- Après un clic sur un bouton de connexion ou de déconnexion, vous pouvez tester la page suivante pour vérifier la présence d'un nom de compte ou d'un lien de déconnexion ou de connexion.
- Après un clic sur un lien pour accéder à une page de produit, vous pouvez tester les spécifications du produit ou un bouton "ajouter au panier".
- Vous pouvez aussi rechercher un lien sur la nouvelle page dont vous avez besoin pour l'étape suivante.

**Ne choisissez pas un texte qui s'affiche de la même manière sur chaque page**. Par exemple, n'utilisez pas de texte de pied de page. Le texte du pied de page ne vous dit rien sur la progression de la transaction.

Utilisez des [expressions régulières](https://www.w3schools.com/jsref/jsref_obj_regexp.asp) si nécessaire. Par exemple, après avoir effectué une action de recherche, si votre page indique "15 résultat(s) trouvé(s)", définissez une vérification de contenu pour `.* résultat(s) trouvé(s)`, et utilisez la condition de vérification du contenu **correspond à une expression régulière**.

Après avoir choisi le texte de votre vérification, prenez soin de formuler un sélecteur CSS ou XPath unique et robuste (résistant aux modifications de la page).

### Sélecteurs

Choisir un sélecteur robuste et solide est essentiel pour les deux types de vérification *Contenu de l'élément de test* et *Attendre l'élément*. Ce paragraphe ne s'applique pas au type *Tester le contenu du document*, puisqu'il n'y a pas d'option de sélecteur.

Un bon sélecteur doit être unique sur la page. L'utilisation d'une valeur unique vous garantit qu'Uptrends regarde le bon élément. Dans la mesure du possible, utilisez l'attribut id de l'élément, car ces attributs sont généralement uniques. Par exemple, `//*[@id='testId']` ou`#testId`.

Pour en savoir plus sur les sélecteurs, consultez les articles de notre base de connaissances sur [l'utilisation des sélecteurs]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="fr" >}}) et les [sélecteurs alternatifs]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="fr" >}}).

## Mises en garde et astuces

**Prêtez attention à la casse du texte**. Avec l'utilisation d'un sélecteur CSS, il n'est pas rare que le texte apparaisse tout en majuscules sur la page, tandis qu'il affiche une majuscule en début de phrase dans le DOM. Cela signifie que le sélecteur pourrait être `//span[text()='Hello']`, mais le texte sur la page pourrait être "HELLO". Le sélecteur doit refléter les informations du DOM, et la chaîne que vous utilisez pour la correspondance doit refléter ce qui se trouve réellement sur la page.

**Certaines pages utilisent des ID dynamiques.**. Par exemple, nous pourrions enregistrer un clic sur un élément "span" s'affichant comme suit dans le DOM :  
`<span id="example-12345">`.  
Toutefois, après le rechargement de la page, le même élément s'afficherait comme suit :  
`<span id="example-12789">`.  
Utilisez XPath pour gérer les ID dynamiques. Par exemple :  
`//span[contains(@id,'example-')]`.
