{
"hero": {
"title": "Personnalisation des scripts pour les moniteurs d'API multi-étapes"
},
"title": "Personnalisation des scripts pour les moniteurs d'API multi-étapes",
"summary":"Découvrez les options de personnalisation des scripts pour le monitoring d'API multi-étapes",
"url": "/support/kb/synthetic-monitoring/api-monitoring/personnalisation-script-multi-etapes",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-custom-scripting"
}

Le moniteur d'API multi-étapes s'accompagne de puissantes [fonctions intégrées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) qui fournissent une solution sans code facile à employer pour tester le comportement de vos API.

L'approche sans code est très commode pour configurer des moniteurs, mais il est possible que vous ayez besoin d'un langage de script pour effectuer des tests fonctionnels approfondis et décrire en détail ce que vous attendez de vos API. Par exemple, vous pouvez avoir besoin d'ajouter une logique personnalisée ou de gérer des comportements plus avancés qui ne peuvent pas être traités dans une simple interface.

Le moniteur MSA vous permet d'utiliser à la fois les fonctionnalités sans code et les scripts personnalisés. Vous pouvez associer les fonctions d'interface intégrées et les fonctions de scripts. Ainsi, vous n'avez pas à créer entièrement de nouveaux moniteurs si vous voulez ajouter des scripts personnalisés à des moniteurs d'API existants. Commencez simplement par ajouter quelques scripts à votre configuration.

## Script de pré-requête et de post-réponse

Un moniteur d'API peut exécuter une seule ou plusieurs étapes à la suite. Pour chaque étape du moniteur MSA (à l'exception des étapes d'attente), deux éditeurs de scripts sont disponibles :
{{< AppElement type="tab" >}} Pré-Requête {{< /AppElement >}} et {{< AppElement type="tab" >}} Post-Réponse {{< /AppElement >}}.

- L'éditeur de **script de pré-requête** vous permet d'écrire des scripts pour préparer l'envoi d'une requête HTTP. Cette étape est utile pour préparer et calculer les valeurs à inclure dans la requête, comme les variables d'environnement, les paramètres d'URL, les en-têtes de requête ou le contenu du corps de requête. Le script écrit dans cet éditeur s'exécute *avant* que la requête API soit envoyée au serveur.

- L'éditeur de **script de post-réponse** vous permet d'écrire des scripts pour vérifier et traiter la réponse HTTP fournie par l'API. Cette étape est utile pour définir une logique personnalisée permettant de vérifier les en-têtes de réponse, de valider l'exhaustivité et la cohérence de votre contenu et d'utiliser ces données pour préparer les étapes suivantes. Le script écrit dans l'éditeur s'exécute uniquement *après* que la réponse d'API a été reçue depuis le serveur. Si une erreur de connexion se produit, le script n'est pas exécuté et toute assertion ou variable dans l'onglet {{< AppElement type="tab" >}} Réponse {{< /AppElement >}} n'est pas validée.

Ces éditeurs incluent aussi les fonctionnalités suivantes :
![Onglets liés aux scripts personnalisés](/img/content/API-monitoring-custom-scripting-editors-min.png)

- Numérotation des lignes : affiche des valeurs numériques qui permettent d'identifier les scripts ou les codes ligne par ligne.
- Mise en surbrillance du code : affiche les codes dans une couleur qui permet de repérer facilement les erreurs de syntaxe et les mots-clés.
- Remplissage du code : suggère automatiquement des combinaisons de code pour faciliter l'écriture.
- Extraits de code : un panneau fournit une liste d'extraits de code utiles que vous pouvez insérer automatiquement dans votre éditeur de code au moyen d'un simple clic.

## Extraits de code

Les éditeurs de scripts **pré-requête** et **post-réponse** vous permettent d'insérer et d'exécuter des scripts écrits en langage Javascript. En plus de toutes les possibilités offertes par Javascript, vous pouvez utiliser les **extraits de code**.

Les **extraits de code** sont des fonctions spéciales qui vous permettent d'accéder aux données des requêtes HTTP (pendant le processus de pré-requête) et des réponses HTTP (pendant le processus de post-réponse). Ils vous permettent aussi d'exécuter des instructions de log, de stocker des données calculées sous forme de [métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="fr" >}}), et d'exécuter des tests sur les données des étapes. Ces fonctions spéciales sont disponibles via un objet unique appelé `ut`.

## Objets ut généraux/de base

La liste des objets `ut` généraux est fournie dans cette section :

- `ut.request` vous donne accès à l'objet de requête d'API.
- `ut.response` vous donne accès à l'objet de réponse d'API.
- `ut.variables` désigne la collection de variables que vous pouvez utiliser dans les étapes d'API. Vous pouvez utiliser cette fonction pour faire passer des valeurs d'une étape à la suivante. Les [variables prédéfinies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}) ou les variables que vous utilisez dans l'onglet {{< AppElement type="tab" >}} Réponse {{< /AppElement >}} sont incluses dans la collection d'objets.
- `ut.log()` est une fonction helper qui extrait les journaux indiqués dans le journal de la console. Lors de l'exécution des scripts de pré-requête, les logs se trouvent dans le **journal de la console du script de pré-requête**, tandis que les logs des scripts de post-réponse se trouvent dans le **journal de la console des scripts de post-réponse**.
- `ut.test()` est la principale fonction de saisie des résultats du test. Le résultat de test que vous définissez à l'intérieur de chaque appel `ut.test()` est enregistré et ajouté en tant que résultat d'**assertion**, aux côtés des assertions que vous définissez dans l'onglet {{< AppElement type="tab" >}} Réponse {{< /AppElement >}} de chaque étape.
- `ut.customMetrics` est une collection de valeurs numériques provenant directement d'une réponse d'API. Vous pouvez définir votre propre variable de métrique personnalisée pour enregistrer ou calculer les valeurs à partir de la réponse d'API. Cette valeur s'affiche pour chaque mesure dans les détails de vérification du moniteur, et peut aussi être listée et présentée sur les dashboards.
- `ut.crypto` permet de générer des hash MD5 et SHA pour manipuler et transmettre les données en toute sécurité. Cette fonction permet aussi d'analyser les listes de révocation de certificats (CRL).

Vous connaissez désormais les objets `ut` de base/généraux. La section ci-dessous détaille les attributs de chaque objet `ut`.

### Requête

Attributs de `ut.request` :

- `.url` : obtient ou définit l'URL de requête.
- `.method` : obtient ou définit la méthode HTTP de la requête (par exemple GET et POST).
- `.body` : obtient ou définit une version sous forme de texte brut du corps de la requête.

### En-têtes de requête

Fonctions de `ut.request.headers`:

- `.has(header, value)` : indique si l'en-tête existe et présente une valeur spécifique.
- `.get(header)` : indique la valeur de l'en-tête ou renvoie une chaîne vide si l'en-tête n'existe pas.
- `.add(header, value)` : crée un nouvel en-tête et sa `valeur` spécifiée (seulement si l'en-tête n'a pas encore été défini).
- `.upsert(header, value)` : insère l'en-tête avec la `valeur` spécifiée (si l'en-tête n'existe pas déjà) ou actualise l'en-tête avec la valeur spécifiée (si l'en-tête existe).
- `.remove(header)` : retire l'en-tête.

### Réponse

Attributs de `ut.response` :

- `.code` : obtient le code de statut numérique de la réponse HTTP (par exemple, 200, 404, 500).
- `.status` : obtient la description du statut HTTP (par exemple, OK).
- `.responseSize` : obtient la taille de la réponse en octets.
- `.bytes` : fournit un tableau d'octets contenant le corps de la requête. Les réponses ne peuvent excéder 100 Mo.

Fonctions de l'objet `ut.response` :

- `.text()` : renvoie une version sous forme de texte brut du corps de la réponse.
- `.json()` : renvoie un objet en analysant le texte de la réponse sous format JSON.

### En-têtes de réponse

Fonctions de `ut.response.headers`:

- `.has(header)` : indique si l'en-tête existe.
- `.get(header)` : indique la valeur de l'en-tête ou renvoie une chaîne vide si l'en-tête n'existe pas.

### Variables

Fonctions de `ut.variables` :

- `.has(key)` : indique si la variable existe.
- `.get(key)` : indique la valeur de la variable ou renvoie une chaîne vide si la variable n'existe pas.
- `.set(key, value)` :  crée la variable (si elle n'existe pas) et enregistre la `valeur` spécifiée dans la variable `clé`.

### Métriques personnalisées

Fonctions de `ut.customMetrics` :

- `.get(key)` : indique la valeur de la variable de métrique personnalisée ou renvoie une chaîne vide si la métrique personnalisée n'existe pas.
- `.set(key, value)` : enregistre la `valeur` spécifiée dans la variable `clé` de la métrique personnalisée.

Pour en savoir plus, consultez les articles de notre base de connaissances intitulés [Configuration des métriques personnalisées]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="fr" >}}) et [Variables de monitoring d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}}).

### Test ou assertion

Uptrends prend en charge les interfaces Expect et Should de Chai JS. Lisez [Chai - Should](https://www.chaijs.com/guide/styles/#should "https://www.chaijs.com/guide/styles/#should") et [Chai - Expect](https://www.chaijs.com/guide/styles/#expect "https://www.chaijs.com/guide/styles/#expect") pour en savoir plus sur l'expression des tests de valeur et des comparaisons :

- `ut.expect(value)` + différentes expressions
- `ut.should(value)` + différentes expressions

Lorsqu'elles sont utilisées seules et que les critères ne sont pas remplis, les expressions `.expect()` et `.should()` génèrent une erreur qui interrompt l'exécution du moniteur. Toute autre assertion figurant dans le restant du script ne sera pas exécutée.

Utilisez `ut.test()` pour exécuter l'ensemble des assertions malgré l'échec possible de l'une d'entre elles :

- `ut.test(descriptionText, testFunction)` : le résultat (succès ou échec) d'une assertion `.expect` ou `.should` définie dans la fonction spécifiée testFunction est présentée dans les résultats des assertions du moniteur. De plus, lorsqu'une assertion échoue, la fonction `ut.test()` garantit que l'exécution du script n'est pas interrompue.

## Hachage

Fonctions de `ut.crypto` :

- `.md5(value)` : génère un hash MD5 de la valeur précisée.
- `.sha1(value)` : génère un hash SHA-1 de la valeur précisée.
- `.sha256(value)` : génère un hash SHA-256 de la valeur précisée
- `.sha512(value)` : génère un hash SHA-512 de la valeur précisée.

Les méthodes de script permettant de générer des hash MD5 et SHA vous permettent de stocker et d'envoyer des valeurs de façon sécurisée, en garantissant la protection des données au moyen du hachage.

Exemple :

```js
var hashedMD5value = ut.crypto.md5("value here");
var hashedSHA1value = ut.crypto.sha1("value here");
```

- `.cert.parseCrl(bytes)` : analyse une liste de révocation de certificats (CRL) et fournit ses métadonnées. Un fichier CRL doit être fourni pour permettre l'exécution de la fonction `.cert.parseCrl(bytes)`. Par exemple, si vous voulez lire le champ `NextUpdate` d'un fichier ou d'une URL CRL, vous pouvez utiliser cette fonction de la façon suivante :

```js
  var crl = ut.crypto.cert.parseCrl(ut.response.bytes);
  var crlNextUpdate = new Date(crl.NextUpdate);
  ut.log(ut.crypto.cert.parseCrl(ut.response.bytes));

  // Assert the value of a variable
  ut.test("Variable {variable} should equal {value}", () => {
    expect(crlNextUpdate).at.least(new Date(2026, 1, 1));
  });
```
