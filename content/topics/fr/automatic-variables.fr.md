{
  "hero": {
    "title": "Variables automatiques"
  },
  "title": "Variables automatiques",
"summary": "Liste des variables automatiques à utiliser dans les moniteurs de transactions et Multi-step API",
  "url": "/support/kb/surveillance-synthetique/transactions/variables-automatiques",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/automatic-variables"
}

Les types de moniteurs [Transaction]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}) et [Multi-Step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}) d'Uptrends vous permettent de suivre un parcours composé de plusieurs étapes, soit sur une page web, soit en interagissant directement avec une API. Dans certains cas, vous aurez peut-être à soumettre des données. Par exemple, un formulaire dans l'une de vos transactions peut nécessiter un horodatage, ou vous devrez peut-être générer un identifiant unique à utiliser dans l'une des requêtes API. Uprends vous fournit un certain nombre de **variables automatiques**. La plupart d'entre elles sont en fait des fonctions qui génèrent une valeur que vous pouvez utiliser dans vos requêtes HTTP, insérer dans des champs textuels ou ajouter aux sélecteurs dans vos moniteurs de transactions.

## Variables automatiques génériques

Les variables automatiques suivantes sont disponibles pour les types de moniteurs **Transaction** et **API multi-étapes** :

### Date et heure

{{< Code/Symbol type="variable" >}}{{@DateTime(format,offset)}}{{< /Code/Symbol >}} : Cette variable génère des valeurs dynamiques de date et heure, selon le format que vous spécifiez et avec un décalage (offset) facultatif. La date/heure (sans un décalage) est toujours l'heure actuelle exprimée en UTC (coordinated universal time).

Pour formatter la date/heure selon vos besoins, définissez le paramètre `format` sur :

- une valeur compatible avec le formatage de date .NET, par exemple `jj/MM/aaaa` ou alors `MM/jj/aaaa`
- `Iso`, pour le format ISO 8601
- `Unix`, pour l'époque Unix

L'option `offset` peut être utilisée pour recalculer la date/heure en fonction d'une différence donnée (en secondes) ou d'une fonction date/heure. Si le paramètre de décalage est absent, aucun décalage n'est appliqué. Pour recalculer la date et l'heure, utilisez les options suivantes :

- Donnez au paramètre de décalage une valeur en secondes, positive ou négative. Le nombre de secondes spécifié est ajouté ou soustrait de la valeur de date/heure actuelle. Un cas d'utilisation typique est de calculer la date et l'heure dans un fuseau horaire différent ou de passer à un jour différent avant ou après la date/heure actuelle.

   Le tableau ci-dessous présente quelques exemples.

- Utilisez une fonction de date/heure pour calculer le dernier ou le premier jour du mois en cours, du mois précédent ou du mois suivant, par rapport à la valeur de date/heure donnée. Les valeurs possibles pour le décalage sont :
   - `LastDayOfMonth`
   - `FirstDayOfMonth`
   - `LastDayOfPreviousMonth`
   - `FirstDayOfPreviousMonth`
   - `LastDayOfNextMonth`
   - `FirstDayOfNextMonth`

Le tableau ci-dessous montre quelques exemples pour une date/heure de 24 février 2018 à 22h30 UTC.
| Expression                                  | Valeur                        | Description                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| `{{@DateTime(dd-MM-yyyy HH:mm)}}`           | 24-02-2018 22:30             | Maintenant, au format dd-MM-yyyy HH:mm               |
| `{{@DateTime(dd-MM-yyyy HH:mm),-18000}}`    | 24-02-2018 17:30             | Maintenant, au fuseau horaire EST (côte Est américaine)  (UTC-5)         |
| `{{@DateTime(ISO)}}`                        | 2018-02-24T22:30:00.0000000Z | Maintenant, au format ISO 8601                        |
| `{{@DateTime(UNIX)}}`                       | 1519511400                   | Maintenant, au format Unix epoch                       |
| `{{@DateTime(MM/dd/yyyy,-86400)}}`          | 02/23/2018                   | Hier, au format MM/dd/yyyy               |
| `{{@DateTime(MM/dd/yyyy,86400)}}`           | 02/25/2018                   | Demain, au format MM/dd/yyyy                |
| `{{@DateTime(MM/dd/yyyy,FirstDayOfMonth)}}` | 02/01/2018                   | Premier jour du mois, au format MM/dd/yyyy |
| `{{@DateTime(MM/dd/yyyy,LastDayOfMonth)}}`  | 02/28/2018                   | Dernier jour du mois, au format MM/dd/yyyy  |

### Identifiant unique aléatoire

{{< Code/Symbol type="variable" >}}{{@RandomGuid}}{{< /Code/Symbol >}} : Cette variable produit une valeur aléatoire sous la forme `AB0AD14D-9611-41A8-9C25-7D94B895CFF1`. Vous pouvez utiliser cette variable si vous devez inclure une valeur aléatoire dans votre URL, vos données POST ou votre en-tête HTTP. Si vous utilisez la variable {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} dans plusieurs étapes, chaque étape aura une valeur aléatoire différente. À chaque exécution du moniteur, vous obtiendrez de nouvelles valeurs aléatoires.
### Identifiant unique aléatoire récurrent
{{< Code/Symbol type="variable" >}}{{@UniqueGuid}}{{< /Code/Symbol >}} : Cette variable unique et aléatoire peut être réutilisée plusieurs fois tout au long de la transaction. À la différence de la variable {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} présentée ci-dessus, qui crée une nouvelle valeur à chaque fois, vous pouvez utiliser cette variable pour inclure une valeur récurrente dans votre URL, vos données POST ou votre en-tête HTTP.
Par exemple, cela peut vous être utile pour créer le script d'un processus d'inscription, dans lequel l'adresse e-mail générée et l'adresse e-mail confirmée doivent être identiques.
### Entier aléatoire

{{< Code/Symbol type="variable" >}}{{@RandomInt(min,max)}}{{< /Code/Symbol >}} : Cette variable produit un nombre entier aléatoire, entre les valeurs minimum et maximum que vous spécifiez (minimum et maximum incluses). Par exemple, si vous spécifiez `{{@RandomInt(0,100)}}`, cette variable produit un nombre compris entre 0 et 100.
### Lettres aléatoires en majuscules

{{< Code/Symbol type="variable" >}}{{@RandomChar(length)}}{{< /Code/Symbol >}} : Cette variable automatique vous permet de générer une série aléatoire de caractères alphabétiques dans une longueur donnée. Tous les caractères seront en majuscules. Par exemple, `{{@RandomChar(5)}}` produit une valeur aléatoire sous la forme `GPLMQ`.
### Identifiants aléatoires pour les bénéficiaires Medicare (aux États-Unis)
{{< Code/Symbol type="variable" >}}{{@RandomUSMedicare}}{{< /Code/Symbol >}} : Cette variable automatique vous permet de générer des identifiants pour les bénéficiaires du programme Medicare aux États-Unis. Ces identifiants, connus sous l'acronyme MBI (Medicare Beneficiary Identifier), sont composés d'une série de 11 caractères alphanumériques. Par exemple, `1EG4TE5MK73`. Veuillez noter que le code est généré sans tiret. Les codes MBI peuvent être utilisés par les entreprises du secteur de la santé aux États-Unis.

## Variables (héritées) spécifiques à la transaction

L'ensemble suivant de variables automatiques est plus ancien, mais peut toujours être utilisé. Ces variables ne sont disponibles que pour les moniteurs **Transaction**.

### Horodatages

{{< Code/Symbol type="variable" >}}{timespan 0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Pour **appliquer un horodatage** (date actuelle) dans un champ de texte sur votre page.

{{< Code/Symbol type="variable" >}}{timespan 1:0:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Pour **décaler d'un jour** (demain).

{{< Code/Symbol type="variable" >}}{timespan 0:1:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : comme ci-dessus, mais pour un **décalage de 1 heure**.

{{< Code/Symbol type="variable" >}}{timespan 0:0:1:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} et {{< Code/Symbol type="variable" >}}{timespan 0:0:0:1}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Décaler l'heure actuelle d'une minute ou d'une seconde, respectivement.

### Valeur aléatoire à partir d'un tableau

{{< Code/Symbol type="variable" >}}{random 1 2 3 4 5}{{< /Code/Symbol >}} : Définir une variable aléatoire à partir d'un tableau. Cette fonction définit de manière aléatoire une des valeurs de un à cinq.

{{< Code/Symbol type="variable" >}}{random pomme banane orange}{{< /Code/Symbol >}} : Cette fonction définit de manière aléatoire une des chaînes du tableau, soit `pomme`, `banane`, ou `orange`.

## Variables spécifiques à l'API multi-étapes

Les variables et informations suivantes ne s'appliquent qu'aux moniteurs de type **API multi-étapes**.

### Identification du serveur (ID)

{{< Code/Symbol type="variable" >}}{{@ServerId}}{{< /Code/Symbol >}} : Lors de l'exécution d'un moniteur d'API multi-étapes, cette variable génère une valeur numérique qui identifie l'emplacement du point de contrôle Uptrends qui exécute cette vérification. Par exemple, si la vérification est en cours d'exécution sur le point de contrôle d'Uptrends à Sydney, en Australie, la variable affichera la valeur `30`. La liste des serveurs de checkpoints et des **identifiants de serveur** correspondants est disponible via [l'API d'Uptrends]({{< ref path="support/kb/api" lang="fr" >}}) au [endpoint Checkpoint](https://api.uptrends.com/v4/Checkpoint).

### URL de redirection

{{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}} : Si l'une des étapes de votre moniteur doit renvoyer un code de redirection et que vous souhaitez le capturer et tester plutôt que de le suivre automatiquement, cette variable automatique contiendra l'URL à laquelle la redirection fait référence. Cela ne se produit que si vous choisissez de ne pas suivre automatiquement les redirections, et que vous configurez une assertion qui vérifie le code de redirection approprié. Pour en savoir plus, lisez l'article [Multi-step monitoring - Gestion des redirections]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="fr" >}}).

### Flottant aléatoire

{{< Code/Symbol type="variable" >}}{{@RandomFloat(min,max)}}{{< /Code/Symbol >}} : Utilisez cette fonction pour générer un nombre en virgule flottante compris dans l'intervalle (min/max) indiqué. La précision (nombre de décimales après la virgule) du flottant généré est dérivée de la plus haute précision des valeurs `min` et `max`.

Par exemple, la variable `{{@RandomFloat(-1.2,3.00000)}}` générera un flottant aléatoire compris entre -1,2 et 3,0, avec une précision de 5, comme 2,12345.

## Comment utiliser une valeur générée automatiquement plusieurs fois de suite

Certaines de ces fonctions variables (en particulier celles produisant des valeurs aléatoires ou des valeurs date/heure) sont réévaluées chaque fois que vous les utilisez, et généreront donc une nouvelle valeur à chaque fois. Si vous souhaitez générer une valeur particulière et l'utiliser plusieurs fois tout au long de votre scénario multi-étapes, vous pouvez utiliser une variable prédéfinie (comme expliqué dans l'article sur les [variables de surveillance multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="fr" >}})) et lui assigner comme valeur une variable automatique.

### Exemples de variables prédéfinies utilisant des variables automatiques

| Nom | Valeur | Utilisation |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SearchDate` | `{{@DateTime(dd-MM-yyyy)}}` | Une valeur de date à utiliser comme entrée pour une requête de recherche. |
| `UniqueEmail` | `{{@RandomGuid}}@mycompany.com` | Une valeur guid aléatoire combinée avec du texte fixe pour générer une adresse e-mail qui est différente à chaque fois. |
| `OrderAmount` | `{{@RandomInt(1, 10)}}` | Un nombre aléatoire compris entre 1 et 10 à utiliser comme nombre de produits à commander. Lors d'un appel ultérieur, vous pouvez réutiliser cette variable pour vérifier le contenu d'un panier et voir s'il contient effectivement ce nombre d'articles. |
