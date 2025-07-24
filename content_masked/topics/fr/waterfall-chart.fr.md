{
  "hero": {
    "title": "Graphique en cascade"
  },
  "title": "Graphique en cascade",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/resultats-surveillance/graphique-en-cascade",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le graphique en cascade est une représentation visuelle du chargement des éléments d'une page web suite à une vérification de moniteur. La cascade fait partie des résultats détaillés.

Pour les Full Page Checks (FPC), le graphique est généré par défaut. Pour les moniteurs de transaction, vous pouvez décider à chaque étape si vous voulez ajouter un graphique en cascade. L'article de la base de connaissances [Utilisation des captures d’écran et des cascades dans les transactions]([LINK_URL_1]) vous explique comment faire.

## Utiliser les graphiques en cascade pour le débogage

Connaître le temps de chargement de la page est déjà très utile, mais la cascade détaille en outre le temps de chargement pour chaque élément.

- Vous pouvez ainsi vérifier le délai de résolution, le délai de connexion TCP, le délai de négociation (ou handshake) HTTPS, le délai d'envoi, le délai d'attente, le délai de réception et le délai d'expiration (ou timeout) pour chaque élément. Les délais sont présentés plus en détail dans l'article de la base de connaissances [Timings des cascades]([LINK_URL_2]).
- Visualiser le chargement progressif de la page. Il est facile de repérer les éléments lents et bloquants dans le graphique en cascade.
- Trouver les éléments de page ayant échoué. Vous pouvez examiner les en-têtes de requête et de réponse pour obtenir des indices sur l'échec. Par exemple, vous pouvez déterminer si un nœud CDN a envoyé le mauvais contenu ou si la réponse a été trop lente.

## Où se trouve le graphique en cascade ? [ANCHOR_1]

Pour les FPC et les moniteurs de transactions, les graphiques en cascade sont situés dans les détails de vérification, mais la façon d'y accéder diffère légèrement. Suivez les étapes ci-dessous.

### Ouvrir un graphique en cascade pour un FPC

Pour ouvrir le rapport en cascade, vous devez ouvrir les détails du contrôle du moniteur. Procédez comme suit :

1. Ouvrez le dashboard *Journal des moniteurs*. Vous pouvez y accéder rapidement en saisissant "Journal moniteurs" dans la barre de recherche du menu.

2. Ouvrez l'une des vérifications du moniteur FPC en cliquant sur la ligne correspondante.

3. La fenêtre "Voir les détails" s'ouvre, avec le rapport en cascade en bas.

### Ouvrir un graphique en cascade pour une étape d'un moniteur de transaction

Le rapport de cascade se trouve dans les résultats détaillés de la vérification.

1. Ouvrez le dashboard *Journal moniteurs* et cliquez sur une vérification de moniteur de transaction.

2. En bas, vous trouverez le **Résultat par étape**. Cliquez sur l'icône de la cascade [SHORTCODE_1][SHORTCODE_2] pour afficher les détails.

### Exemple de graphique en cascade

Une fois que vous l'avez ouvert, le graphique ressemblera à celui-ci :

![Capture d'écran d'un graphique en cascade]([LINK_URL_3])

## Qu'est-ce qui est présenté dans le graphique en cascade ? [ANCHOR_2]

Le graphique en cascade présente les noms (URL) des éléments de la page dans la première colonne, puis la taille de l'élément de la page et les mesures du temps de chargement prises pendant la vérification du moniteur, et ce, pour tous les éléments de la page qui ont été chargés.
Les mesures sont présentées chronologiquement de gauche à droite, avec une ligne pour chaque élément de page.
Pour charger un élément de page, un certain nombre d'étapes sont nécessaires.

Les différentes étapes sont codées par couleur. La légende en haut du graphique indique la signification de chaque couleur.
Pour en savoir plus sur chaque étape, consultez l'article de la base de connaissances [Timings des cascades]([LINK_URL_4]).

Le graphique en cascade d'un moniteur de transaction fournit les métriques [Core Web Vitals]([LINK_URL_5]) et les [temps de navigation du W3C]([LINK_URL_6]) pour chaque action de navigation d'une étape de transaction. Les métriques sont affichées au-dessus du graphique en cascade. Lorsqu'une étape contient plusieurs actions de navigation, le graphique affiche les métriques de toutes les actions de navigation en affichant un trait vertical vert. La métrique exacte s'affiche lorsque vous survolez ce trait avec la souris.

Sous le graphique en cascade se trouve un résumé de tous les timings par type de requête.

## Timings détaillés

Pour obtenir des informations plus détaillées ou contextuelles sur les mesures d'un élément de la page, survolez la barre des mesures d'un élément et une fenêtre contextuelle contenant les détails de cet élément apparaîtra.

![Capture d'écran de la fenêtre contextuelle d'un graphique en cascade]([LINK_URL_7])


## Panneau de requête/réponse

Pour chaque élément individuel de la cascade, vous pouvez cliquer sur le symbole **+** pour ouvrir le panneau de requête/réponse. Ce panneau contient des informations sur la requête qui a été faite pour récupérer l'élément, et la réponse correspondante.

Il contient les informations suivantes :
- L'URL de la requête, la méthode et le protocole utilisé
- Une vue d'ensemble des request headers inclus dans la requête
- L'adresse IP du serveur répondant
- Des informations sur la taille (non) compressée de l'élément :
   - **Taille réseau** : nombre réel d'octets qui ont été téléchargés (taille compressée)
   - **Taille de la ressource (non compressée)** : taille de l'élément après décompression, le cas échéant
- Tout en-tête de réponse compris dans la réponse

Si vous utilisez un [Full Page Check avec des métriques supplémentaires]([LINK_URL_8]), les panneaux de requête/réponse comprennent également les **Informations TLS** pertinentes pour cet élément. De plus, ces cascades peuvent afficher d'autres détails sur les éléments, tels que la mise en cache, le préchargement ou l'abandon de la requête. Elles prennent aussi en charge les URI de données (lorsque la page HTML contient des données d'image inline). Ces informations supplémentaires sont affichées dans les panneaux de requête/réponse pour les éléments individuels, le cas échéant.

![Panneau de requête/réponse]([LINK_URL_9])

## Autres options permettant d'affiner les informations

Vous pouvez cliquer sur les en-têtes des trois premières colonnes, à savoir le numéro de l'élément de la page (#), le nom de l'élément (URL) et la taille de l'élément, pour trier le graphique en cascade en fonction des valeurs dans ces colonnes.

Si la page contient beaucoup d'éléments, il peut être nécessaire de filtrer le graphique en partant du nom (ou d'une partie du nom) de l'élément de la page. Utilisez le champ **Filtre** pour renseigner le terme à utiliser pour filtrer les résultats.

## Exporter le graphique en cascade

Le graphique en cascade peut être exporté dans un fichier PDF. Ces PDF peuvent être utilisés pour sauvegarder les mesures figurant dans vos cascades. Les graphiques au format PDF peuvent être pratiques si vous souhaitez montrer des graphiques en cascade à un tiers sans partager les dashboards.

Cliquez sur le bouton **Exporter au format PDF** à droite au-dessus du graphique pour générer un exemplaire PDF de votre graphique en cascade et l'enregistrer.
