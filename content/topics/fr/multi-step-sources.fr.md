{
"hero": {
"title": "Sources possibles pour la surveillance multi-étapes"
},
"title": "Sources possibles pour la surveillance multi-étapes",
"summary": "Comment extraire des valeurs pour créer des assertions ou affecter des variables lors de la configuration d'une surveillance d'API multi-étapes.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/source-multi-etapes",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-sources"
}

Pour configurer une [assertion de vérification de contenu]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="fr" >}}) ou extraire une [valeur à stocker en tant que variable]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}) dans le cadre de votre moniteur API multi-étapes, vous devrez spécifier la valeur à examiner. Les options suivantes sont disponibles :

## Corps de réponse en tant que JSON
Choisissez cette option si le contenu du corps de votre réponse contient des données JSON et que vous souhaitez inspecter ou capturer un élément dans la structure JSON. Dans le champ de propriété de l'assertion ou de la variable, spécifiez quel élément JSON nous devons inspecter.

### Exemples
Supposons que votre réponse JSON ait le contenu suivant :

```json
{
  "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
  "token_type":"Bearer",
  "expires_in":86400
}
```


Pour capturer la valeur de l'attribut **access\_token**, définissez {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}} comme valeur de propriété.

Si l'objet contenant la clé **access_token** est **l'enfant** d'un autre objet JSON, précisez le chemin complet. Par exemple :

```json
{
   "response":{
      "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
      "token_type":"Bearer",
      "expires_in":86400
   }
}
```

Ici, le jeton d'accès peut être récupéré en indiquant {{< Code/Symbol type="property" >}}response.access\_token{{< /Code/Symbol >}} comme valeur de propriété.


Autre exemple JSON : supposons que vos données JSON contiennent un **tableau** incluant un ou plusieurs éléments. Ici, imaginons un tableau de trois produits :

```json
[
  {
    "Name": "Alpha Cygnus IX",
    "Price": 20000,
  },
  {
    "Name": "Norcadia Prime",
    "Price": 25000,
  },
  {
    "Name": "Risa", 
    "Price": 37500,
  }
]
```

Pour accéder à un attribut de l'un de ces produits, nous devons d'abord pointer vers un élément particulier du tableau en fournissant un index. L'index du premier élément d'un tableau JSON est toujours zéro :`[0]`. Donc, pour capturer l'attribut Price du premier produit de notre tableau, nous spécifierions {{< Code/Symbol type="property" >}}\[0\].Price{{< /Code/Symbol >}}, ce qui nous renverra la valeur "20000".

Si vos données JSON contiennent un tableau qui est l'enfant d'un autre objet, vous devrez préciser chaque "étape", y compris l'index pour l'élément qui se trouve dans le tableau. Supposons que votre réponse JSON ait le contenu suivant :

```json
{
   "Destinations":[
      {
         "Name":"Alpha Cygnus IX",
         "Price":20000
      },
      {
         "Name":"Norcadia Prime",
         "Price":25000
      },
      {
         "Name":"Risa",
         "Price":37500
      }
   ]
}
```

Dans ce cas, la valeur du premier `Name` peut être capturée avec {{< Code/Symbol type="property" >}}Destinations.\[0\].Name{{< /Code/Symbol >}} (la valeur pour **Name** dans le premier élément du tableau **Destinations**), ce qui produirait "Alpha Cygnus IX".


{{< callout >}}**Remarque** : Si le corps de la réponse ne peut pas être analysé selon les règles JSON, cette fonction va générer une erreur.{{< /callout >}}

## Corps de réponse en tant que XML
Si votre réponse contient un document XML, choisissez cette option et spécifiez une requête XPath pour affiner le contenu à inspecter ou à capturer.

### Exemple

Supposons que votre réponse XML ait le contenu suivant :

```xml
<AuthInfo> 
  <access_token>MjAxNy0xMC0wMlQxMDowOTo1My45MDUxNjEyWg==</access_token> 
  <expires_in>86400</expires_in> 
  <token_type>Bearer</token_type> 
</AuthInfo>
```



Pour capturer la valeur interne du nœud **access\_token**, utilisez la requête XPath {{< Code/Symbol type="property" >}}/AuthInfo/access\_token/text(){{< /Code/Symbol >}} comme valeur de propriété.

Pour en savoir plus, consultez d'autres [exemples XPath, qui incluent le SOAP au format XML]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="fr" >}}).

Si le corps de la réponse ne peut pas être analysé en tant que document XML autonome, si la requête XPath est invalide ou si elle ne sélectionne pas une valeur réelle du document, une erreur sera générée.

## Corps de réponse en tant que XML

Si le contenu de votre réponse n'est pas au format JSON ou XML (par exemple, texte brut, HTML ou un format propriétaire), vous pouvez tout de même utiliser cette option pour rechercher du contenu. Par défaut, nous considérerons tout le contenu du corps de la réponse. Cela fonctionne bien si vous voulez seulement effectuer une simple recherche de type "contient" (par exemple : si le corps de la réponse doit contenir l'expression "Prix", la vérification sera satisfaite tant que le mot Prix apparaîtra quelque part dans le contenu). Pour utiliser le contenu entier pour votre assertion ou pour votre définition de variable, laissez le champ de propriété vide.

Toutefois, si vous souhaitez inspecter ou extraire du contenu à partir d'un emplacement spécifique du document, il faudra définir un moyen pour y parvenir. Pour ce faire, spécifiez une expression régulière dans le champ de propriété. En utilisant les capacités de mise en correspondance des expressions régulières, nous chercherons une correspondance dans votre contenu, et la première correspondance trouvée sera capturée en tant que valeur.

Si l'expression régulière contient un groupe de capture (ce qui permet de définir un motif à l'intérieur de l'expression régulière), nous utiliserons la première correspondance pour ce groupe de capture.

À noter que ces options s'appliquent uniquement à du texte (elles s'appliquent également aux réponses contenant du JSON ou du XML, car il s'agit toujours de texte) ; la recherche de contenu binaire n'est pas prise en charge.

## Code de statut

Cette option inspecte le code d'état HTTP numérique qui fait partie de chaque réponse HTTP. Dans la plupart des cas, vous vérifierez simplement que le code est égal à 200 (ce qui signifie OK), ou du moins ne représente pas un échec. De fait, nous le faisons pour vous par défaut : si vous ne spécifiez pas d'assertion de code d'état, nous effectuerons automatiquement l'assertion suivante, car les codes 4xx et 5xx sont généralement des codes d'erreur :

`Status code` {{< Code/Symbol type="comparison" >}}Is less than{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}400{{< /Code/Symbol >}}

Cependant, si vous définissez vous-même une assertion de code d'état, cela remplacera notre vérification par défaut. Par exemple, si vous définissez :

`Status code` {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}200{{< /Code/Symbol >}}

C'est cette condition que nous vérifierons.

{{< callout >}}**Remarque** : La situation est particulière lorsque vous ajoutez une assertion de code d'état pour les codes 301, 302, 303, 307 ou 308 (c'est-à-dire un code de redirection). Pour en savoir plus, lisez l'article sur la [gestion des redirections]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="fr" >}}).{{< /callout >}}

## Description du statut

Cette option examine la description textuelle du code d'état HTTP (officiellement appelé Reason-Phrase). Cela peut être utile lorsque vous vérifiez le comportement de certaines conditions d'erreur dans votre API : vous aurez peut-être besoin de vérifier que lorsque vous alimentez votre API avec une donnée incorrecte, une description d'état utile est renvoyée.

## Réponse complétée

Cette option renvoie toujours une valeur booléenne liée à la réussite ou à l'échec de la requête HTTP. Elle renvoie une valeur "false" si nous n'avons pas pu déterminer à quel serveur se connecter, si aucune connexion n'a pu être établie, ou si le serveur n'a pas répondu avec une réponse HTTP en temps opportun. Dans tous les autres cas, elle renvoie une valeur "true".

Vous n'aurez pas besoin de spécifier cette option dans la plupart des cas, car nous la vérifierons automatiquement : pour ce type d'assertion, nous signalerons une erreur chaque fois que nous ne pourrons pas récupérer une réponse HTTP de votre serveur.

`Response completed` {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}true{{< /Code/Symbol >}}

Dans certains cas, il est possible d'utiliser cette vérification à l'envers : si vous spécifiez "false" à la place de "true", nous vérifierons que l'obtention d'une réponse réussie n'est PAS possible. Cela peut être utile si vous avez une application web ou une API qui ne devrait être disponible que sur votre réseau interne, même si le nom de domaine correspondant est disponible publiquement. Avec cette vérification, nous vérifierons que nous ne pouvons pas atteindre votre API ou votre application web.

## Response header

Cette option vous permet d'inspecter un en-tête de réponse HTTP spécifique. Vous devez spécifier le nom de cet en-tête dans le champ de propriété.

## Cookie

Cette option renvoie la valeur actuelle d'un cookie. Vous devez spécifier le nom de ce cookie dans le champ de propriété. Notez que les cookies retournés par votre serveur sont traités comme des cookies de session : les valeurs des cookies sont lues, mises à jour et renvoyées à votre serveur pendant l'exécution du scénario entier, jusqu'à la dernière étape. Ensuite, tous les cookies sont supprimés, quelles que soient les directives d'expiration. Cela signifie que les cookies permanents sont traités comme des cookies de session.

## Longueur du contenu

Cette option renvoie la taille (en octets) du corps de la réponse. Notez qu'il s'agit de la longueur réelle du contenu de la réponse après décompression (si votre serveur l'avait compressé précédemment).

## Durée
Cette option renvoie la durée totale (en millisecondes) qui a été nécessaire pour l'exécution de la requête et la réception de la réponse. Cela vous permet de surveiller les durées des différentes étapes.
