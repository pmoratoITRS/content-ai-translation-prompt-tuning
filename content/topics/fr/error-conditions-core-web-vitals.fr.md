{
"hero": {
"title": "Conditions d'erreur liées aux Core Web Vitals"
},
"title": "Conditions d'erreur liées aux Core Web Vitals",
"summary": "Découvrez comment utiliser les seuils relatifs aux Core Web Vitals pour définir des erreurs.",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-core-web-vitals",
"tableofcontents": true,
"translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-core-web-vitals"
}

Les Core Web Vitals sont un ensemble standard de métriques définies par Google pour mesurer l'expérience liée à l'utilisation des pages web.

Dans l'application Uptrends, les types de moniteurs qui utilisent un [navigateur avec des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}}) mesurent les indicateurs [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="fr" >}}). La disponibilité de ces données vous permet de les utiliser pour définir les seuils dont le dépassement constitue une erreur. Les conditions liées aux Core Web Vitals font donc partie des [conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}}).

Chaque type de moniteur s'accompagne de conditions d'erreur différentes. Consultez le tableau intitulé [Quelles conditions d'erreur sont disponibles ?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="fr" >}}) pour connaître les options associées à chaque type de moniteur.

Les conditions d'erreur liées aux Core Web Vitals sont décrites ci-dessous.

## Utilisation des indicateurs Core Web Vitals recommandés {id="use-current-recommended-core-web-vitals"}

Pour Google, la performance de votre site web peut être bonne, à améliorer ou médiocre.
Avec Uptrends, vous pouvez définir une erreur dès lors que le statut "à améliorer" est atteint. Uptrends utilise les valeurs de référence définies par Google, à savoir actuellement :

**First Contentful Paint :** 1,8 seconde  
**Largest Contentful Paint :** 2,5 secondes  
**Time to Interactive :** 3,8 secondes  
**Cumulative Layout Shift :** 0,1  
**Total Blocking Time :** 0,2 seconde (200 ms)

Si vous utilisez la condition d'erreur *Utiliser les Core Web Vitals recommandés*, une erreur est déclenchée dès qu'au moins une valeur de référence est dépassée.

Vous pouvez associer la condition d'erreur *Utiliser les Core Web Vitals recommandés* et des conditions d'erreur individuelles liées aux Core Web Vitals. Dans ce cas, vos conditions d'erreur prévalent sur les recommandations.

## Temps maximum pour le First Contentful Paint (FPC)

Utilisez cette condition d'erreur pour indiquer le temps d'attente maximum avant que le navigateur commence à afficher des parties de la page visibles pour l'utilisateur. Si l'utilisateur ne reçoit pas de confirmation visuelle du chargement de la page, cela peut nuire à l’expérience d'utilisation de votre site web.

## Temps maximum pour le Largest Contentful Paint (LCP)

Utilisez cette condition d'erreur pour indiquer le temps d'attente maximum avant que le navigateur affiche le contenu principal de la page. Si le chargement de la majeure partie du contenu est plus long qu'attendu, l'expérience d'utilisation peut se trouver affaiblie.

## Temps maximal pour le Time to interactive (TTI) (option Time to Interactive mixumum)

Utilisez cette condition d'erreur pour indiquer le temps d'attente maximum avant que la page réagisse aux actions de l'utilisateur. Si ce délai est trop long, l'utilisateur doit attendre le chargement de la page, puis que la page réagisse à ses actions.

## Score de Cumulative Layout Shift maximum (CLS)

L'indicateur Cumulative Layout Shift (CLS) mesure la stabilité visuelle de la page en contrôlant tout changement inattendu dans l'affichage des éléments pendant le chargement de la page. Utilisez cette condition d'erreur pour vous assurer que l'utilisateur ne subit aucune gêne liée au déplacement de certains éléments de la page, par exemple en raison du chargement tardif ou asynchrone des vidéos.

## Maximum Total Blocking Time (TBT)

Utilisez cette condition d'erreur pour indiquer la durée maximum pendant laquelle le chargement de la page peut rester bloqué dans le navigateur pour des raisons telles qu'un problème de connexion, l'exécution d'un script ou l'affichage des éléments. Si un délai trop long contraint l'utilisateur à attendre pour interagir avec la page, cela influe sur l'expérience d'utilisation de votre site web.