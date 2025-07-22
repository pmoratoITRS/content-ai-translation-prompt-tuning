{
"hero": {
"title": "Ignorer les erreurs pour les étapes et actions facultatives"
},
"title": "Ignorer les erreurs pour les étapes et actions facultatives",
"summary": "Vos scripts de transaction doivent pouvoir prendre en compte des changements dynamiques du site. La possibilité d'ignorer les erreurs vous donne le contrôle dont vous avez besoin pour insérer des instructions conditionnelles ou pouvant être ignorées dans les étapes et les actions de votre script.",
"url": "/support/kb/surveillance-synthetique/transactions/ignorer-erreurs-pour-étapes-et-actions-facultatives",
"translationKey": "https://www.uptrends.com/support/kb/transactions/using-ignore-errors-for-optional-steps-and-actions"
}

Il est rare qu'un site web n'ait pas de variations dans le chemin de clic de l'utilisateur. Votre site peut présenter des variations dynamiques de contenu pour de nombreuses raisons :

- Différences de page dues à l'emplacement de l'utilisateur
- Tests A/B
- Modifications des champs de saisie
- Cookie walls (murs de traceurs)
- Pages insérées temporairement

Toute variation dans le chemin de clic est un défi pour vos scripts de transaction. L'option *ignorer les erreurs* peut vous aider à passer outre les modifications dynamiques du site telles que celles répertoriées ci-dessus.

## En quoi « ignorer les erreurs » ressemble-t-il à une instruction conditionnelle ?

Lorsque vous choisissez d'ignorer les erreurs, vous dites au moniteur d'effectuer une action, puis, selon que l'assertion ou l'action échoue (ou réussit), d'effectuer une autre action. Pensez à l'option d'ignorer les erreurs comme un moyen d'insérer une instruction conditionnelle. Vous pouvez ignorer les erreurs au niveau de l'étape, ou au niveau des actions individuelles.

- **Ignorer les erreurs au niveau de l'étape** En choisissant d'ignorer les erreurs au niveau de l'étape, vous indiquez au script d'abandonner l'étape et de passer à l'étape suivante si le script rencontre une erreur. Si l'action X de l'étape Y réussit, continuer dans l'étape ; si l'action X de l'étape Y échoue, abandonnez l'étape et passez à l'étape Z.
- **Ignorer les erreurs au niveau de l'action**  En choisissant d'ignorer les erreurs au niveau de l'action, vous indiquez au script de passer à l'action suivante même si l'action échoue. Si l'action X réussit, passez à l'action Y ; si l'action X échoue, passez quand même à l'action Y.

## Comment ça fonctionne ?

En règle générale, lorsque votre transaction rencontre une erreur, l'exécution du script s'arrête et Uptrends enregistre l'erreur. L'erreur peut entraîner l'envoi d'une alerte par Uptrends si un autre point de contrôle vérifie l'erreur. Si vous rendez l'erreur conditionnelle (ignorer les erreurs), l'exécution se poursuit à l'étape ou à l'action suivante selon votre choix, au niveau de l'étape ou de l'action. Uptrends note l'erreur dans le rapport détaillé de la vérification ; cependant, les erreurs ignorées n'affectent pas le reporting de votre site.

### Ignorer les erreurs au niveau des étapes

L'activation de l'option d'ignorer les erreurs au niveau de l'étape entraîne l'arrêt de l'exécution de l'étape en cours par le script et le passage à l'étape suivante si une action échoue. Par exemple, la figure 1 représente une transaction avec un mur de cookies. Le mur de cookies exige que l'utilisateur clique sur un bouton d'acceptation lorsque le mur apparaît, mais le mur n'apparaît pas pour tous les utilisateurs.

Pour gérer le mur de cookies, nous mettons en place une étape conditionnelle. Dans ce cas, une vérification de contenu détermine si le site a inséré un mur de cookies (représenté à l'étape X de la figure 1). S'il y a un mur de cookies, la vérification du contenu réussit, le moniteur clique sur le bouton pour accepter les termes et l'exécution se poursuit (à l'étape Y). Si la vérification du contenu ne trouve pas de mur de cookies, l'étape X échoue, mais le moniteur continue quand même à l'étape Y. L'étape Y n'est pas configurée pour ignorer les erreurs, donc toute erreur qui se produit à l'étape Y entraîne l'arrêt du script par le moniteur et Uptrends enregistre l'erreur.

![](/img/content/28f28080-958d-4d25-866e-cd73efade7d2.png)

*Figure 1*: Utilisation de l'option ignorer les erreurs pour tester et passer un mur de cookies s'il est présent.

### Ignorer les erreurs au niveau des actions

Lorsque vous ignorez les erreurs sur des actions uniques, l'exécution passe à l'action suivante. La figure 2 montre une transaction avec un test A/B. À l'étape X, le script nécessite la réussite des actions un et deux, mais les actions trois et quatre ne sont valides que pour la version A de la page. Si vous n'ignorez pas les erreurs pour les actions trois et quatre, le script produira une erreur à chaque fois que le serveur enverra la page B.

![](/img/content/8d1b26cd-3c66-4363-a82a-cdad2423b0f4.png)

Figure 2 : Organigramme d'une transaction avec un test A/B.

## Exemples

Pour vous aider, examinons de plus près quelques exemples courants. Votre cas particulier peut nécessiter une solution différente, [contactez-nous]({{< ref path="contact" lang="fr" >}}) si vous avez besoin d'aide pour votre solution.

{{< callout >}}
**Remarque** : Comme règle générale, utilisez ignorer les erreurs au niveau des actions pour une seule action et utilisez ignorer les erreurs au niveau de l'étape si plusieurs actions liées doivent être ignorées
{{< /callout >}}

### Cas d'utilisation : chemin de clic différent en raison de l'emplacement de l'utilisateur

Parfois, les sites se comportent différemment en fonction de l'emplacement d'un utilisateur pour diverses raisons, telles que les réglementations gouvernementales, la disponibilité du produit dans la région ou la langue. Par exemple, si un utilisateur se trouve dans l'UE, le site doit obtenir la confirmation que l'utilisateur comprend que le site web collecte des données personnelles auprès des visiteurs. Le site utilise une fenêtre contextuelle (popup) qui oblige l'utilisateur à cocher une case indiquant qu'il connaît les conditions selon lesquelles le site web collecte et conserve les données, et l'utilisateur doit également cliquer sur un bouton Continuer.

#### Solution : Ignorer l'étape

Dans cet exemple l'utilisateur doit effectuer deux actions pour accéder au site complet ; par conséquent, le niveau étape est un bon choix.

1. Ajoutez une étape au point de la transaction où l'utilisateur risque de recevoir la fenêtre popup.
2. Configurez l'étape pour qu'elle ignore les erreurs.
3. Insérez une action de clic qui coche la case.
4. Insérez une action de clic qui appuie sur le bouton Continuer.

Si l'action de clic de l'étape 3 échoue, c'est que l'invite ne s'était pas affichée pour l'utilisateur. Le script quitte l'étape et passe à la première action de l'étape suivante ; sinon, le moniteur reconnaît les conditions en effectuant les actions appropriées, et la transaction se déroule normalement.

### Cas d'utilisation : test A/B

Un test A/B vous permet de comparer les interactions des utilisateurs en fonction de deux versions différentes de la même page. La page A peut demander à l'utilisateur de fournir des informations dont la page B n'a pas besoin. Le test détermine quelle page génère le plus de conversions. Le serveur fournit différentes versions de page aux utilisateurs de manière aléatoire. Les changements dans les différentes interactions de page peuvent donc provoquer une erreur de votre moniteur.

#### Solution: Ignorer les actions

Dans ce cas, le moniteur doit effectuer certaines actions quelle que soit la page affichée et ignorer une ou plusieurs actions spécifiques aux autres versions de page. Pour gérer les tests A/B :

1. Pour les interactions que les deux pages ont en commun, utilisez des actions qui n'ignorent pas les erreurs.
2. Pour les actions supplémentaires, ignorez les erreurs.

En définissant les actions pour qu'elles ignorent les erreurs pour les champs supplémentaires, la transaction peut continuer quelle que soit la version de la page reçue par le moniteur (voir Figure 2).

### Cas d'utilisation : Un nombre variable de champs

Prenons l'exemple d'un site de commerce électronique de vêtements dont l'inventaire évolue rapidement. Votre transaction sélectionne le premier élément qui apparaît dans une recherche, mais le premier élément change fréquemment. Bien que chaque article ait un champ de quantité, tous les articles n'ont pas de taille (un foulard), de couleur (uniquement en noir) ou ni l'un ni l'autre (un sac à main). Les différences dans les actions disponibles peuvent entraîner une erreur de votre moniteur lorsqu'il tente de sélectionner une couleur alors que la couleur n'est pas une option.

#### Solution: Ignorer les actions

Puisque tous les champs de sélection n'apparaissent pas sur toutes les pages, il faut ignorer les erreurs des actions qui définissent des valeurs pour un élément qui n'existe pas. Pour gérer un nombre variable de champs :

1. Ajoutez une étape.
2. Ajoutez les actions appropriées pour chaque interaction de page possible : quantité, taille et couleur.
3. Pour la quantité, laissez décochée l'option ignorer les erreurs, pour les actions de sélection de taille et de couleur, cochez les cases ignorer les erreurs.

Le script tente de définir chaque valeur, mais si l'élément n'est pas présent, une erreur est générée et l'exécution du script passent de toute façon à l'action suivante (voir Figure 2).

### Cas d'utilisation : Pages de notification insérées

De temps en temps, un site a besoin d'informer ses utilisateurs, par exemple sur la maintenance à venir, les modifications des conditions d'utilisation, les ventes ou autres promotions. Le site web insère des pages temporaires comprenant la notification dans le chemin de clic normal de l'utilisateur. La page nécessite souvent une action de l'utilisateur pour accuser réception de la notification.

#### Solution : Ignorer l'étape ou l'action, selon

Ce cas d'utilisation peut avoir une ou plusieurs interactions utilisateur pour faire avancer la transaction.

**Si la confirmation prend une seule interaction, utilisez une action conditionnelle** ; insérez l'action à l'endroit approprié et définissez l'action pour ignorer les erreurs.

**Si la confirmation nécessite plusieurs actions, utilisez une étape conditionnelle**.

1. Ajoutez une étape à l'endroit du script où un message peut apparaître.
2. Configurez l'étape pour qu'elle ignore les erreurs.
3. Ajoutez les actions appropriées pour fermer la page : acceptez les nouvelles conditions, confirmez la réception de la notification et envoyez la réponse.

Si l'étape ou l'action réussit, la transaction avance. Si l'étape ou l'action échoue, il n'y a pas eu de page de notification, aucune autre action n'est nécessaire et le script passe à l'action ou à l'étape suivante.
