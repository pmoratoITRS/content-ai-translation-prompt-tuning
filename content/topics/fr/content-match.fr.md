{
"hero": {
"title": "Conditions d'erreur liées au contenu de la page"
},
"title": "Conditions d'erreur liées au contenu de la page",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/correspondance-de-contenu",
"summary": "La correspondance de contenu permet de vérifier que la page que vous surveillez affiche le bon contenu",
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/content-match"
}

Il arrive parfois que seule la moitié du contenu d'un site web se charge correctement. Le non-chargement de certains blocs de texte, paragraphes et sections complique la navigation pour les utilisateurs. Si vous gérez un site d'e-commerce, cette mauvaise expérience utilisateur peut affecter les performances de votre site et diminuer vos ventes sans que vous vous en rendiez compte.

## Condition d'erreur liée au contenu de la page

La condition d'erreur Contenu de page vous permet de vous assurer que le contenu de votre site web se charge correctement et complètement. Elle vous permet de préciser les blocs de textes, les phrases et les expressions régulières qui doivent apparaître sur votre page, et de vérifier que ces éléments s'affichent.

![Condition d'erreur Contenu de page](/img/content/scr-error-condition-page-content.min.png)

## Correspondance de contenu

Une correspondance de contenu est une liste de mots que vous fournissez pour que le moniteur vérifie qu'elle figure bien dans le contenu chargé sur le site :

- Si un moniteur vérifiant la page *trouve* le contenu, *aucune erreur* n'est signalée.
- Si un moniteur vérifiant la page *ne trouve pas* le contenu, *une erreur* est signalée.

## Correspondance de contenu spécifique à chaque type de moniteur

Différents types de correspondance de contenu sont disponibles pour les différents moniteurs. La correspondance de contenu varie selon la catégorie du moniteur et les données collectées :

### Moniteurs de disponibilité

Les moniteurs de disponibilité vérifient le contenu de la page en adressant une requête GET à l'URL de votre site web. Si la requête réussit, le moniteur valide le contenu de la réponse GET de votre site web.

Si vous surveillez une URL de site web, comme https://galacticresorts.com/, les vérifications de contenu suivantes peuvent être effectuées :

| Types de correspondance de contenu | Exemples |
|--|--|
| Modèle objet de document (DOM) ou éléments HTML | {{< tableformatter >}}
- `<title>Home Page - GalacticResorts.com</title>`
- `<a class="btn btn-primary btn-lg" href="/Products/Index/97f8fcc9-11b5-4d86-b208-ccb6d2be35e3">Book now!</a>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />`
   {{< /tableformatter >}} |
   | {{< tableformatter >}} Textes contenant une [expression régulière]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="fr" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
   {{< /tableformatter >}} |
   | {{< tableformatter >}} [Correspondance de contenu avancée]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="fr" >}}){{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "GalacticResottt", "IsPositive": false }]`{{< /tableformatter >}} |

### Moniteurs de navigateur

Les moniteurs de navigateur vérifient le contenu de la page en contrôlant son code source. Le code source est la structure brute du site web au format HTML. Il comprend les métadonnées, les scripts et les styles de la page.

Si vous surveillez une URL de site web, comme https://galacticresorts.com/, les vérifications de contenu suivantes peuvent être effectuées :

| Types de correspondance de contenu | Exemples |
|--|--|
| Modèle objet de document (DOM) ou éléments HTML | {{< tableformatter >}}
- `<h2>Norcadia Prime</h2>`
- `<li><a href="/APIHelp" target="_blank">API</a></li>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />`
   {{< /tableformatter >}} |
   | {{< tableformatter >}} Textes contenant une [expression régulière]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="fr" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
   {{< /tableformatter >}} |
   | {{< tableformatter >}} [Correspondance de contenu avancée]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="fr" >}}){{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "Holiday destinations", "IsPositive": true }]`{{< /tableformatter >}} |

{{< callout >}} **Remarque :** Pour ouvrir le code source d'une page, ouvrez votre site web et pressez les touches **Ctrl + U**. Vous pouvez aussi cliquer n'importe où sur la page et sélectionner **Code source de la page**. Notez que tous les éléments du code source ne peuvent pas faire l'objet d'une vérification de contenu.{{< /callout >}}

### Moniteurs d'API multi-étapes (MSA)

Les moniteurs MSA vérifient les correspondances de contenu au moyen d'**assertions**. Les assertions vous permettent d'indiquer comment vérifier que la réponse de l'API répond aux conditions attendues. Par exemple, vous pouvez indiquer que la réponse doit contenir le code de statut 200 ou que le corps de réponse au format JSON doit contenir des textes spécifiques. Pour en savoir plus, lisez notre article sur les [assertions pour la surveillance multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="fr" >}}).

### Moniteurs de transactions

Les moniteurs de transactions vérifient le contenu de la page en contrôlant que ses éléments s'affichent dans le navigateur. Ils vérifient que des textes, des boutons, des images ou d'autres éléments de l'interface utilisateur sont visibles sur votre site web. Les moniteurs de transactions reposent sur des **vérifications de contenu**. Ces actions configurées à chaque étape vérifient que chaque chargement de page se déroule comme attendu. Par exemple, une vérification peut vérifier que le texte "L'article a été ajouté au panier" s'affiche sur la page. Pour en savoir plus, lisez notre article sur les [vérifications de contenu]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}).

## Types de correspondance de contenu

Voici les types de correspondance de contenu disponibles pour certains moniteurs :

### Correspondance de contenu régulière {id = "regular-content-match"}

Vous pouvez définir une correspondance de contenu au moyen d'expressions régulières. Une expression régulière (regex ou regexp) est une chaîne de caractères spéciale utilisée pour décrire un motif de recherche. Pour définir une correspondance de contenu, vous pouvez utiliser les éléments suivants :

- Un mot unique : `Uptrends`
- Plusieurs mots ou phrases dans un ordre précis : `produit.*commande` (dans cet exemple, product ET order doivent apparaître)
- Des symboles correspondant à d'autres éléments :
   - `!erreur` : utilisez un point d'exclamation pour inverser le sens d'un mot. Cette correspondance de contenu signifie que le mot *erreur* ne doit pas apparaître.
   - `En soldes|Meilleures ventes` : la barre verticale indique qu'un mot équivaut à un autre. Cette correspondance de contenu signifie que le texte `En soldes` OU `Meilleures ventes` doit apparaître sur votre site web.

Pour en savoir plus, consultez cette ressource (en anglais) sur les expressions régulières : [Regular Expression Language - Quick Reference](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference).


### Correspondance de contenu avancée

Vous pouvez utiliser simultanément plusieurs correspondances de contenu en enregistrant les valeurs au format JSON. Pour combiner deux motifs de recherche, sur n'importe quel élément de page ou expression régulière, utilisez le code suivant :

```json
    [
      {
        "Pattern": "PhraseA",
        "IsPositive": true
      },
      {
        "Pattern": "PhraseB",
        "IsPositive": false
      }
    ]
```

Fournissez une correspondance de contenu valide dans le champ `Pattern`. Définissez `IsPositive` sur `true` si le motif doit correspondre au contenu de votre site web, ou sur `false` s'il ne doit pas correspondre à un contenu sur le site.

{{< callout >}} **Remarque :** La correspondance de contenu avancée est disponible avec les moniteurs HTTPS, Webservices HTTP et HTTPS, et Full Page Check. {{< /callout >}}

Pour vérifier l'horodatage d'un élément de votre site web au moyen d'une correspondance de contenu, utilisez :

```json
    [
    {
      "Pattern": "contenu avant la valeur d'horodatage (?<hour>\\d\\d):(?<minute>\\d\\d)",
      "IsPositive": true,
      "DateTime": {
        "OffsetUTC": 60,
        "MaxDifference": 5
      }
    }
    ]
```

La valeur JSON, `Pattern`, peut contenir des valeurs sous la forme d'une expression régulière, comme \<year\>, \<month\>, \<day\>, \<hour\>, \<minute\> et \<second\>. Toutes ces valeurs peuvent être extraites du contenu du site web et seront fusionnées avec l'heure actuelle du serveur, puis évaluées en horaires UTC.

La valeur `OffsetUTC` est le nombre de minutes à soustraire afin de le comparer à l'heure du serveur en UTC. Si la page web contient un horodatage en UTC\+1, le décalage doit être de 60. Si la page web contient un horodatage en EST (UTC-5), le décalage devrait être de -300.

La valeur `MaxDifference` est la différence maximale en minutes autorisée entre l'heure de la page web et votre heure locale. Par exemple : s'il est 10h06 et que l'heure de la page web est 10h00, une erreur se produira si la valeur `MaxDifference` est égale ou inférieure à 5.

## Comment configurer une correspondance de contenu

Pour configurer une correspondance de contenu, vous devez ajouter une condition d'erreur de type **Vérifier le contenu de la page** :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Sélectionnez le moniteur auquel vous souhaitez ajouter une correspondance de contenu.
3. Affichez l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}}.
4. Saisissez les informations relatives à la correspondance de contenu dans la section **Vérifier le contenu de la page**.
5. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.

Une fois cela effectué, vous pouvez [créer une définition d'alerte ]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}) pour recevoir une notification lorsque la condition d'erreur **Vérifier le contenu de la page** est remplie.
