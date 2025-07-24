{
  "hero": {
    "title": "Mesures des durées de navigation du W3C"
  },
  "title": "Mesures des durées de navigation du W3C",
  "summary": "Description des mesures des durées de navigation du W3C fournies dans les graphiques en cascade des moniteurs Full Page Check et de transactions",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/resultats-surveillance/metriques-duree-navigation-w3c",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le **World Wide Web Consortium** (ou W3C) est une organisation internationale qui travaille au développement de standards pour le World Wide Web. À ce titre, le W3C a défini une norme pour les navigateurs et les applications web, qui permet de générer et d'afficher des informations sur les durées de chargement des pages web. La spécification complète de la norme peut être consultée sur le [site web du W3C (Copyright © 2012, World Wide Web Consortium)]([LINK_URL_1]).

Les [moniteurs Full Page Check (FPC)]([LINK_URL_2]) et [les moniteurs de transactions]([LINK_URL_3]) d'Uptrends permettent d'afficher un sous-ensemble des métriques de durées de navigation du W3C (ainsi que quelques informations supplémentaires telles que les [Core Web Vitals]([LINK_URL_4])). Cet article vous présente les métriques fournies et ce qu'elles signifient.

Par exemple, l'image suivante montre tous les éléments de navigation définis par le W3C sur une frise chronologique.

![métriques de navigation du w3c]([LINK_URL_5])
(Copyright © 2012, [World Wide Web Consortium]([LINK_URL_6]))

## Métriques

Voici une vue d'ensemble des métriques des durées de navigation du W3C que vous pouvez trouver dans les rapports du moniteur Full Page Check d'Uptrends.

![Durées de navigation du W3C dans Uptrends]([LINK_URL_7])

- **Début de la requête** : équivaut au [INLINE_CODE_1] tel que défini par le W3C. Cet horodatage indique le moment où le navigateur commence à demander la ressource au serveur web après la consultation du DNS et la connexion TCP.
- **Durée jusqu'au premier octet** (Time to first byte) : équivaut à la différence entre [INLINE_CODE_2] et [INLINE_CODE_3] tels que définis par le W3C. En bref, c'est le temps entre le moment où la première requête a été envoyée du navigateur au serveur et le moment où le premier octet de la réponse suivante a été reçu par le navigateur (qui peut comprendre des redirections et des connexions SSL/TCP).
- **DOM interactif** : équivaut au [INLINE_CODE_4] tel que défini par le W3C. Il s'agit du moment où le document est devenu "interactif", ce qui indique que le navigateur a cessé d'analyser la page et que l'utilisateur peut commencer à interagir avec elle. Des ressources telles que les scripts, les images, les feuilles de style ou les cadres peuvent encore être en cours de chargement.
- **DOM terminé** : équivaut au [INLINE_CODE_5] tel que défini par le W3C. Il s'agit du moment où le document principal a été analysé, où le DOM a été entièrement chargé et où l'état de préparation de la page est devenu "terminé".
- **Load event** : équivaut à [INLINE_CODE_6] tel que défini par le W3C. Il s'agit du moment où le chargement du document actuel est terminé, y compris pour toutes les ressources dépendantes telles que les feuilles de style et les images.

## Rapports de performance

Vous pouvez afficher toutes les métriques dans un dashboard personnalisé. Ajoutez simplement une tuile personnalisée du type [Liste ou graphique de données simple]([LINK_URL_8]). Cliquez ensuite sur le bouton des paramètres [SHORTCODE_1] [SHORTCODE_2] de la tuile et choisissez les valeurs que vous souhaitez afficher en cochant leurs cases.

Vous pouvez afficher les métriques de navigation du W3C pour chaque étape d'un moniteur de transaction. Pour chaque étape que vous souhaitez afficher dans le graphique, vous devez activer les options *Cascade* et *Métriques de performance*. Pour en savoir plus, consultez les informations relatives à la [configuration des étapes]([LINK_URL_9]).

![capture d'écran des paramètres de la tuile]([LINK_URL_10])
