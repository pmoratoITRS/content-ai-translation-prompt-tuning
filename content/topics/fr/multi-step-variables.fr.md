{
"hero": {
"title": "Variables de monitoring d'API multi-étapes"
},
"title": "Variables de monitoring d'API multi-étapes",
"summary": "Cet article vous explique comment utiliser des variables pour stocker et réutiliser les valeurs extraites de vos réponses API.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/multi-step-variables",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-variables"
}

Lors de la [configuration d'un moniteur API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}), des variables sont généralement utilisées pour extraire des valeurs de vos réponses HTTP et les stocker temporairement, en vue d'une réutilisation ultérieure. Cette fonctionnalité vous permet de créer des liens entre les étapes : chaque fois que vous voulez récupérer une information dans une réponse HTTP afin de l'utiliser pour exécuter la prochaine requête HTTP, vous avez besoin d'une variable. Autrement dit : l'étape 1 reçoit une valeur de votre serveur et la stocke dans une variable. L'étape 2 prend la valeur qui vient d'être stockée et l'utilise pour construire une nouvelle requête. Vous pouvez créer autant de variables que vous le souhaitez et les utiliser dans autant d'étapes que vous le souhaitez.

Une deuxième raison d'utiliser des variables est de définir certaines valeurs une seule fois et de les réutiliser dans plusieurs étapes. Ces valeurs seront généralement rajoutées dans la section Variables prédéfinies, dont les variables sont disponibles à n'importe quelle étape du scénario. Reportez-vous à la section [Variables prédéfinies](#predefined-variables) pour en savoir plus.
Toutes les variables que vous définissez dans une étape sont évaluées dès que la requête HTTP a été exécutée et que la réponse a été traitée. À ce stade, si la variable existait déjà (soit par le biais d'une étape précédente, soit parce que vous l'aviez prédéfinie), sa valeur est remplacée par la nouvelle valeur. Dans le cas contraire, une nouvelle variable est créée et ajoutée à la liste. Cette liste de variables et de valeurs correspondantes est ensuite transmise à l'étape suivante.

## Définition des variables

Si vous voulez utiliser des variables, vous devez nous indiquer quelle valeur nous devrons stocker dans ces variables. Les variables sont définies d'une façon semblable aux assertions :

{{< Code/Symbol type="source" >}}Source{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Propriété{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}Nom de la variable{{< /Code/Symbol >}}

Par exemple :

{{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}access\_token{{< /Code/Symbol >}}

- La **source de la variable** : ce champ définit l'attribut de la réponse HTTP que vous souhaitez extraire. Lisez [cet article]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}}) pour connaître les options disponibles.
- La **propriété de la variable** : certaines options liées à la source (en particulier les options relatives à l'extraction de contenu et à l'en-tête) vous obligent à préciser le contenu ou l'en-tête à vérifier. [Plus d'informations sont accessibles ici]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="fr" >}}) pour chaque type de source.

- Le **nom de la variable** : c'est l'identifiant qui sera utilisé dans les étapes suivantes pour se référer à cette variable, selon une notation spéciale.

Si un problème survient lors de l'évaluation d'une variable (par exemple, si vous essayez d'extraire une valeur qui n'est pas présente dans le contenu de la réponse), l'étape échoue et une erreur est signalée.

## Utilisation des variables dans d'autres étapes

Une fois qu'une variable a été évaluée correctement, sa valeur peut être réutilisée dans la définition de la requête des étapes suivantes, ainsi qu'à l'intérieur des assertions (dans les vérifications du contenu de la réponse). La référence à une variable se fait en plaçant le nom de la variable entre des accolades doubles : {{< Code/Symbol type="variable" >}}{{Nom de la variable}}{{< /Code/Symbol >}}.

- Dans l'URL d'une étape : `https://myapi.customer.com/ProductInfo/{{ProductId}}`

- Dans un en-tête de requête : `"Authorization": Bearer {{access_token}}`

- Dans le contenu du corps d'une requête :

   `{ "ProductId": "{{ProductId}}", "Code": "P123456" }`

- Dans la valeur cible d'une assertion. Par exemple, si vous avez une variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}} (issue d'une étape précédente ou en tant que variable prédéfinie), vous pouvez l'utiliser pour vérifier qu'une réponse contient la valeur réelle contenue dans cette variable :

   {{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products\[0\].Id{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}

- Dans la valeur de propriété d'une assertion. Si vous avez une variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}, vous pouvez l'intégrer dans une expression JSON ou une requête XPath pour sélectionner le contenu que vous souhaitez vérifier :

   {{< Code/Symbol type="source" >}}Response body as XML{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}//Product\[@Id="{{ProductId}}"\]/Name/text(){{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} `Chocolate chip cookie`

## Variables prédéfinies

En dessous de l'éditeur d'étapes, vous trouverez une section supplémentaire où vous pouvez spécifier plus de variables. Ces variables sont disponibles dès le début du scénario. Si vous avez besoin d'une même valeur plusieurs fois, vous pouvez définir cette valeur à l'avance et l'utiliser dans différentes étapes. Il peut s'agir d'un identifiant de produit que vous souhaitez utiliser tout au long de votre scénario, d'une clé d'API ou d'autres valeurs spéciales dont votre API a besoin. Un cas particulier consiste à utiliser une variable contenant le nom de domaine pour chaque API. En utilisant cette variable dans chaque URL, vous n'avez pas besoin de répéter le nom de domaine à chaque étape, ce qui vous permet de la modifier très facilement pour l'ensemble du scénario. Pour ajouter une variable prédéfinie, cliquez sur {{< AppElement type="button" >}}\+ Ajouter une variable{{< /AppElement >}} dans la section *Variables prédéfinies* des paramètres du moniteur.  Créez ensuite une variable nommée `BaseUrl` avec la valeur `https://test.yourapi.com`. Pour faire référence à cette variable, l'URL utilisée pour chaque étape de l'API peut alors prendre la forme `{{BaseURL}}/UserService/GetUserInfo`. Cette approche vous permet de modifier votre scénario multi-étapes pour qu'il pointe vers un environnement différent (par exemple, un environnement de test ou un environnement de production) sans avoir à modifier chaque étape.

Les variables prédéfinies peuvent également être utilisées lorsque des données sensibles doivent être envoyées pendant l'exécution du moniteur. Par exemple, si votre API nécessite un accès authentifié, vous devez peut-être vous connecter ou récupérer un jeton d'accès en ajoutant des informations d'identification à l'une de vos requêtes. Les données sensibles sont stockées [dans le coffre-fort]({{< ref path="/support/kb/account/vault" lang="fr" >}}).

Pour configurer les informations d'identification du coffre-fort à utiliser dans un moniteur d'API multi-étapes, procédez comme suit :

1. Tout d'abord, [ajoutez-les au coffre-fort]({{< ref path="/support/kb/account/vault#adding-a-new-item-to-the-vault" lang="fr" >}}).
2. Créez la variable prédéfinie comme vous le feriez normalement.
3. Pour faire référence à un élément du coffre-fort, cliquez sur l'icône [...] sous **Valeur** pour ouvrir le sélecteur de valeur.

![Sélecteur de valeur du coffre dans le moniteur d'API multi-étapes](/img/content/scr_MSA_predefined_variables_1.min.png)

4. Repérez les informations d'identification recherchées dans la liste, et sélectionnez une valeur dans le champ du nom d'utilisateur ou du mot de passe.
5. Donnez à votre variable un **nom** clair, que vous utiliserez pour y faire référence lors de l'exécution du moniteur, comme décrit dans cet article. Dans l'exemple ci-dessous, la variable *examplePassword* est représentée par `{{examplePassword}}`.

![Sélecteur de valeur du coffre dans le moniteur d'API multi-étapes](/img/content/scr-MSA-predefined-variables-example.min.png)

Dans le journal du moniteur, les valeurs provenant du champ *password* du coffre-fort sont affichées sous forme d'astérisques de façon à rester masquées.

![Sélecteur de valeur du coffre dans le moniteur d'API multi-étapes](/img/content/MSA_predefined_variables_result.png)

## Encodage des valeurs des variables

En fonction de l'endroit où vous utilisez vos variables, il est parfois nécessaire d'encoder les valeurs. Cet encodage consiste à convertir les caractères spéciaux dans un format qui convient à une requête HTTP. En règle générale, les variables utilisées dans une URL doivent être encodées. C'est par exemple le cas si vous voulez construire une URL contenant un paramètre de nom, et que vous souhaitez utiliser une variable appelée {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} pour spécifier une valeur pour ce paramètre. Sans encodage, le résultat serait le suivant :

`https://my.api.com/GetCompanyInfo?name={{CompanyName}}`

Supposons maintenant que la variable {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} contienne la valeur `Ben & Jerry's`. Cette valeur contient des espaces et un caractère “&”, qui ont une signification particulière dans une URL. Sans encodage, la valeur reçue sur le serveur serait incorrecte. En appliquant d'abord l'encodage, la valeur sera convertie en `Ben\+%26\+Jerry's`, que le serveur interprétera comme la valeur d'origine. Pour encoder vos variables, utilisez la fonction {{< Code/Symbol type="variable" >}}{{@UrlEncode(...)}}{{< /Code/Symbol >}}. À l'intérieur des parenthèses, mettez le nom complet de la variable, par exemple {{< Code/Symbol type="variable" >}}{{CompanyName}}{{< /Code/Symbol >}}. Dans une URL, le résultat serait le suivant :

`https://my.api.com/GetCompanyInfo?name={{@UrlEncode({{CompanyName}})}}`

Si vous savez qu'une variable ne contiendra jamais de caractères spéciaux (par exemple, uniquement des valeurs numériques), il n'est pas nécessaire d'utiliser la fonction @UrlEncode. Sachez toutefois que les valeurs de variables qui apparaissent dans le corps de requête de l'étape seront encodées automatiquement si un en-tête Content-Type a été spécifié avec la valeur application/x-www-forme-urlencoded. Les autres types de contenu ne nécessitent généralement pas d'encodage d'URL.

## Variables automatiques

En plus des variables que vous définissez dans la configuration de votre moniteur, vous avez également accès à un certain nombre de variables automatiques créées par notre équipe. La plupart de ces variables sont en fait des fonctions qui génèrent une valeur que vous pouvez utiliser dans vos requêtes HTTP, et lors de l'évaluation de vos réponses HTTP à l'aide d'assertions. Si vous souhaitez utiliser des variables automatiques dans votre surveillance d'API multi-étapes, consultez notre [liste complète des variables automatiques disponibles]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="fr" >}}).

## Fonctions définies par l'utilisateur

Dans certains cas, les données entrantes doivent être transformées ou converties pour être plus facilement comprises. Uptrends vous permet de définir vous-même des fonctions qui peuvent être utilisées pour convertir une valeur de variable (acquise lors d'une étape précédente ou à partir d'une variable système fournie par Uptrends) en une nouvelle valeur. Pour en savoir plus sur la configuration et l'utilisation des fonctions définies par l'utilisateur, consultez [cet article de notre base de connaissances]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="fr" >}}).

## Variables de métriques personnalisées

Lorsque votre moniteur d'API multi-étapes récupère des données auprès de vos API, il est possible que vous ayez besoin de surveiller des données numériques qui ne font pas partie des métriques standard, telles que le code de statut et la durée d'une réponse, afin d'évaluer le comportement de votre API.

Dans ces cas, la variable de métrique personnalisée vous permet de créer une variable pour stocker des données numériques extraites de la réponse de l'API. Pour configurer une variable de métrique personnalisée, reportez-vous à l'article [Personnalisation des scripts pour les moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#how-to-set-up-custom-api-monitoring" lang="fr" >}}) dans notre base de connaissances.