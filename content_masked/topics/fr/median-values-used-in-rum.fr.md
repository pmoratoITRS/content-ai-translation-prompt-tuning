{
  "hero": {
    "title": "Valeurs médianes utilisées dans le RUM"
  },
  "title": "Valeurs médianes utilisées dans le RUM",
  "summary": "Le RUM d'Uptrends vous donne le choix entre les valeurs médianes ou moyennes. Découvrez comment Uptrends calcule les valeurs médianes de vos rapports.",
  "url": "[URL_BASE_TOPICS]rum/valeurs-medianes-utilisees-dans-le-rum",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le [Real User Monitoring]([LINK_URL_1]) (RUM) concerne l'expérience des utilisateurs agrégés. Par conséquent, le rapport RUM calcule les résultats en fonction de tous vos utilisateurs. Comprendre comment Uptrends calcule les résultats est important, car vous devez savoir si les données incluses dans vos rapports RUM sont vraiment représentatives de l'expérience de vos utilisateurs. Par défaut, vos rapports RUM utilisent les valeurs médianes par rapport à la moyenne, mais vous pouvez toujours basculer entre les deux méthodes. Pour que vous puissiez faire le meilleur choix pour vos rapports, cet article compare les deux méthodes, explique comment Uptrends calcule les valeurs médianes et la raison pour laquelle nous pensons que l'échantillonnage des données n'est pas un bon choix lorsqu'il s'agit de vos données RUM.

## Moyenne vs. Médiane

Lorsque vous regardez vos tableaux et graphiques de RUM, vous remarquerez que, par défaut, nous rapportons des valeurs médianes plutôt que des moyennes. Nous utilisons la valeur médiane parce que nous estimons que la médiane est la plus représentative de l'ensemble de données. Prenons une seconde pour examiner les deux méthodes.

**Moyenne :** la somme de tous les nombres divisée par la quantité. Par exemple, la moyenne pour l'ensemble {1, 2, 2, 3, 12} est 4.

**Médiane :** le nombre du milieu dans un ensemble. Par exemple, la valeur médiane pour l'ensemble {1, 2, 2, 3, 12} est de 2.

Comme vous pouvez le voir dans les exemples ci-dessus, la donnée aberrante 12 déforme la valeur moyenne tandis que la valeur médiane représente plus précisément l'ensemble de données. Les calculs utilisant la valeur médiane capturent la masse centrale sans la distorsion provoquée par des valeurs exceptionnellement basses ou élevées dans l'ensemble.

## Comment Uptrends calcule la médiane

Dans un ensemble de données relativement limité, Uptrends calcule la médiane en triant le jeu de données et en utilisant la valeur du milieu, mais des ensembles de données plus importants provoquent des problèmes lors du calcul de la valeur médiane. Trouver les valeurs moyennes dans les grands ensembles de données prend beaucoup de temps, alors plutôt que de vous faire attendre, nous calculons la valeur médiane à l'aide d'un [histogramme]([LINK_URL_2]). L'approche de l'histogramme accélère le calcul, mais elle présente un faible écart-type d'environ 1%. Même avec le taux potentiel d'écart de 1%, nous estimons que le calcul de la médiane à l'aide d'un histogramme surpasse encore la moyenne pour décrire avec précision les expériences de vos utilisateurs.

## L'alternative d'échantillonnage aux histogrammes

Une approche alternative des histogrammes est [l'échantillonnage des données]([LINK_URL_3]). Avec l'échantillonnage des données, le calcul utilise uniquement un sous-ensemble des données pour établir la valeur moyenne ou médiane. Le RUM vous permet de regrouper vos données en fonction de l'emplacement, du navigateur et de la version de votre utilisateur, du système d'exploitation et de la version, du type de périphérique et de la page affichée. Avec l'échantillonnage des données, vous pouvez perdre des groupes d'utilisateurs entiers. Avec Uptrends, nous voulons que vous voyiez vos résultats en fonction de tous vos utilisateurs, mais comme nous l'avons expliqué précédemment, le calcul de vos résultats prend du temps. Avec l'approche de l'histogramme, vous obtenez vos résultats rapidement sans perte d'utilisateurs dans votre ensemble de données.

## Alterner entre les valeurs médianes ou moyennes

Vous pouvez désigner quelle méthode de calcul vous utilisez pour vos rapports.

1. Ouvrez la tuile de tableau de bord RUM que vous souhaitez modifier.
2. Cliquez sur les points de suspension [SHORTCODE_1][SHORTCODE_2] pour ouvrir les paramètres de la tuile.
3. Sélectionnez une option dans la liste **Agrégation**.
4. Cliquez sur [SHORTCODE_3]Définir[SHORTCODE_4].

![capture d'écran du paramétrage de la tuile d'agrégation]([LINK_URL_4])
