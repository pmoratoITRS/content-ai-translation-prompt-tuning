{
  "hero": {
    "title": "Outil de test de vitesse de site web: PageSpeed Insights"
  },
  "title": "Outil de test de vitesse de site web: PageSpeed Insights",
  "summary": "L'outil gratuit d'Uptrends de test de vitesse de site web  vous donne votre score Google PageSpeed Insights ainsi que votre graphique en cascade détaillé. En savoir plus sur PageSpeed Insights et sur la façon dont Google calcule le score de page.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/browser-monitoring/outil-de-test-de-vitesse-de-site-web-pagespeed-insights",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Votre [test de vitesse de site web]([LINK_URL_1]) gratuit inclut un score de page et des opportunités d'amélioration des performances, les deux fournis par [Google PageSpeed Insights]([LINK_URL_2]). Nous avons inclus les informations de Google aux côtés des résultats des tests Uptrends afin de vous fournir toutes les informations dont vous avez besoin pour améliorer l'expérience utilisateur de votre page. Uptrends vous donne les détails de la page élément par élément pour vous aider à trouver les éléments de page problématiques et vous montrer la progression du chargement de votre page à l'aide d'un graphique en cascade facile à lire.  

## Que sont les PageSpeed Insights ?

PageSpeed Insights est un outil fourni par Google aux développeurs web (et à tous ceux qui ont un esprit curieux) qui souhaitent obtenir une vue d'ensemble des performances de leur pages, telles que les voit Google. Google propose également des recommandations pour l'amélioration des performances pour vous aider à concentrer vos efforts sur l'optimisation de la vitesse.

## Pourquoi mon score de PageSpeed Insights a-t-il changé ?

Si vous avez déjà utilisé notre outil de test de vitesse gratuit, vous remarquerez peut-être que votre score a changé. Uptrends obtient le score de PageSpeed Insights et les recommandations ultérieures de Google. Votre score a changé parce que Google a modifié sa méthode de calcul du score dans la [cinquième version de l'API PageSpeed Insights]([LINK_URL_3]).

Auparavant, le score de PageSpeed Insights reposait principalement sur les conventions utilisées pour réduire la taille de la page et accélérer le processus de rendu. La nouvelle version prend ces éléments en compte, mais ajuste également le score en fonction d'autres facteurs provenant des outils de diagnostic de Lighthouse (données de laboratoire) et des données de terrain (expériences réelles).

## Comment Google calcule-t-il le score de ma page ?

Pour les vitesses sur mobiles et ordinateurs de bureau, PageSpeed Insights extrait les données de plusieurs sources ce qui se traduit par un score de page et des recommandations pour améliorer la page.

### Données de laboratoire

[Lighthouse]([LINK_URL_4]) collecte et analyse des données sur les temps de chargement des pages et leur attribue un [score]([LINK_URL_5]) : ≥90 rapide, 50–89 moyen, ≤ 50 lent. Le score est basé sur :

-   [First Contentful Paint]([LINK_URL_6])  : le moment où le navigateur affiche pour la première fois le contenu DOM.
-   [First Meaningful Paint]([LINK_URL_7]) : Le moment où un utilisateur estime que le contenu principal a été chargé.
-   [Speed Index]([LINK_URL_8]) : la vitesse d'affichage de la page
-   [First CPU Idle]([LINK_URL_9]) : lorsque la plupart des éléments de l'interface utilisateur deviennent interactifs
-   [Time to Interactive]([LINK_URL_10]) : la page a affiché un contenu utile, les gestionnaires d'événements sont enregistrés et la page répond dans les 50 millisecondes aux interactions de l'utilisateur.
-   [Estimated input latency]([LINK_URL_11]) : réactivité aux entrées

### Données de terrain

Les utilisateurs du navigateur Google Chrome peuvent permettre la collecte des données sur les performances de page lorsqu'ils naviguent sur le web. Lorsque Google calcule le score du site, il accède à ces données pour connaître l'expérience de vrais utilisateurs avec votre page en fonction des éléments suivants :

-   First Contentful Paint : le moment où le navigateur affiche pour la première fois le contenu DOM.
-   [First Input Delay]([LINK_URL_12]) : Le temps écoulé entre la première l'interaction d'un utilisateur et la réponse de la page.

Google compare également les vitesses de vos pages à celles des pages concurrentes et ajuste le score de la page en conséquence.

### Audits de page

Google examine la page telle qu'elle existe actuellement et vous fournit une liste des éléments indiquant lesquels fonctionne bien et ceux qui nécessitent une attention particulière. Dans les audits de page vous trouverez des informations sur :

-   **Des recommandations pour rendre votre page plus rapide,**
-   **Des diagnostics indiquant dans quelle mesure la page utilise les bonnes pratiques en matière de développement web, et**
-   **Les audits passés comprenant la liste des audits réussis de la page.**

Pour plus d'informations sur Google PageSpeed Insights, visitez [Stack Overflow]([LINK_URL_13]).

## Pourquoi votre score PageSpeed Insights est important ?

Google classe plus haut les pages avec des scores de performance mobiles rapides,  il faut donc un score élevé pour améliorer le référencement de votre page. Des études ont confirmé que les utilisateurs accordent le plus d'importance à la vitesse, et la performance des pages est directement liée aux taux de rebond, à la satisfaction des utilisateurs, aux taux de conversion et aux revenus.
