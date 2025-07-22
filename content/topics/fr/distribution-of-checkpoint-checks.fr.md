{
"hero": {
"title": "Fonctionnement du système de checkpoints"
},
"title": "Fonctionnement du système de checkpoints",
"summary": "Comment fonctionne le système de checkpoints d'Uptrends ?",
"url": "/support/kb/surveillance-synthetique/points-de-controle/fonctionnement-systeme-checkpoints",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/distribution-of-checkpoint-checks"
}

Uptrends possède l'un des plus vastes [réseaux de checkpoints de surveillance de site web et de serveur](/checkpoints) du secteur. Il n'a jamais été aussi simple de surveiller vos sites web, vos serveurs et vos services web depuis différents emplacements situés dans le monde entier.

**Mais comment fonctionne le système de checkpoints d'Uptrends ?**

## Algorithme des checkpoints

Lorsque vous ajoutez un moniteur de surveillance, vous pouvez choisir plusieurs checkpoints de notre réseau mondial de surveillance pour vérifier l'état de vos services.

Les vérifications sont effectuées par des checkpoints sélectionnés au hasard, et jamais un checkpoint n'est utilisé deux fois de suite.

En cas d'erreur non confirmée, le service d'Uptrends effectue une deuxième vérification à partir d'un autre checkpoint afin de déterminer si l'erreur est avérée.

- Si ce checkpoint signale également une erreur, l'erreur est confirmée et répertoriée comme telle dans le journal des {{< AppElement type="menuitem" >}}erreurs de moniteur{{< /AppElement >}}.
- Si ce checkpoint ne signale pas d'erreur, l'erreur est considérée comme temporaire.

## Support de type "round-robin" (avec des vérifications effectuées par les checkpoints dans un ordre fixe)

Nous n'avons pas d'option de type "round robin".
