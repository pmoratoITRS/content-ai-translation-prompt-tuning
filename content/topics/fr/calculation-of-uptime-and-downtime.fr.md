{
  "hero": {
    "title": "Calcul de la disponibilité et des temps d'arrêt"
  },
  "title": "Calcul de la disponibilité et des temps d'arrêt",
"summary": "Comment les résultats des vérifications et l'arrêt temporaire des moniteurs ou les périodes de maintenance influent-ils sur le calcul de la disponibilité de votre moniteur ?",
"url": "/support/kb/dashboards-et-rapports/dashboards/calcul-de-la-disponibilite-et-des-temps-d-arret",
  "translationKey": "https://www.uptrends.com/support/kb/reporting/calculation-of-uptime-and-downtime"
}

Les calculs de temps de disponibilité et d'indisponibilité fournissent des données essentielles pour plusieurs mesures présentées dans les tuiles de données de vos dashboards, mais aussi pour vos [accords de niveau de service]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="fr" >}}) (SLA ou Service Level Agreement). Regardons ensemble comment ces calculs sont effectués et quels facteurs sont à prendre en compte.
## Présentation de la double vérification d'Uptrends

Lorsqu'une erreur est détectée sur votre site web ou un serveur, Uptrends effectue toujours une deuxième vérification au moyen d'un autre point de contrôle. Voilà pourquoi, pendant les temps d'arrêt, vos dashboards de [surveillance de site web]({{< ref path="products/synthetics/website-monitoring" lang="fr" >}}) présentent toujours des erreurs non confirmées et des erreurs confirmées.

C'est ainsi que fonctionne le monitoring standard. Avec la surveillance simultanée, aucune double vérification n'est effectuée. Pour comprendre la différence, lisez l'article [Erreurs et alertes pour les moniteurs de surveillance simultanée]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors" lang="fr" >}}).

{{< callout >}}
**Astuce :** Pour obtenir une analyse détaillée des mesures effectuées et des erreurs détectées, consultez le rapport de votre dashboard **Journal moniteurs** que vous trouverez dans le menu {{< AppElement type="menuitem" >}} Surveillance > Journal moniteurs {{< /AppElement >}} menu.
{{< /callout >}}

## Comment le temps de disponibilité est-il calculé ?

La méthode de calcul du temps de fonctionnement est facile à comprendre : pour une période donnée, prenez le nombre de secondes pendant lesquelles votre moniteur était indisponible et divisez ce temps par le nombre total de secondes où votre moniteur était surveillé. Vous obtenez ainsi le pourcentage d'indisponibilité, et soustrayez-le de 100 % pour obtenir le pourcentage de disponibilité.

{{< callout >}}
**Astuce :** Les SLA vous indiquent un temps de disponibilité sous forme de pourcentage. Mais comment savoir à quelle durée cela correspond ? Avec le [calculateur gratuit de disponibilité et de SLA]({{< ref path="tools/free-sla-uptime-calculator" lang="fr" >}}), convertissez facilement les secondes de temps d'indisponibilité en pourcentage, et vice-versa.
{{< /callout >}}

### Exemple

Mettons que vous avez suivi un site web pendant 24 heures (ce qui correspond à 86 400 secondes) et que, pendant cette période, le site a été à l'arrêt pendant 10 minutes (600 secondes). Pour déterminer les pourcentages de temps de disponibilité et d'indisponibilité, le calcul suivant est effectué :

Temps total d'arrêt du site web : 600 secondes  
Temps total de surveillance du site web : 86 400 secondes  
Pourcentage d'indisponibilité = 600 secondes / 86 400 secondes = 0,0069 = 0,69 %  
Pourcentage de disponibilité = 100 % - 0,69 % = 99,31 %

{{< callout >}}
**Astuce :** Vous pouvez jouer avec les données dans votre compte pour récupérer le nombre réel de secondes. Les [tuiles personnalisées]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="fr" >}}) de type _Liste de données_ et _Graphique de données_ vous permettent d'afficher le nombre de secondes pendant lesquelles vos moniteurs étaient disponibles ou indisponibles. Sélectionnez une tuile et cliquez sur les points de suspension {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} pour ouvrir les paramètres des tuiles. Vous y retrouverez les métriques qu'il est possible de sélectionner.
{{< /callout >}}

## Prise en compte des résultats des vérifications de moniteurs

Comment Uptrends qualifie-t-il le temps écoulé entre les différents résultats des vérifications de moniteurs (OK, erreur non confirmée et erreur confirmée) ? Le temps entre une erreur non confirmée et une erreur confirmée est-il considéré comme disponible ou indisponible ?

L'illustration ci-dessous vous montre les conséquences possibles des résultats de vérification ainsi que la façon dont ces périodes sont considérées. Évidemment, dans le cas d'une surveillance constante d'un service ou d'un serveur, il y a beaucoup de résultats de vérifications d'affilée. Toutefois, tous les résultats peuvent se retrouver dans les situations suivantes :

![Illustration des séquences des résultats de vérifications](/img/content/uptime-calculation-min.svg)

De façon plus détaillée, les résultats des vérifications peuvent varier comme suit :

**Erreur non confirmée à erreur confirmée**  
Le temps entre les deux mesures est considéré comme **indisponible**.

**Erreur confirmée à erreur non confirmée**  
Le temps entre les deux mesures est considéré comme **indisponible**, parce que le moniteur est encore dans une condition d'erreur. Le moniteur reste en erreur jusqu'à la réception d'une indication OK.

**Erreur confirmée à OK**  
Le temps entre les deux mesures est considéré comme **indisponible**. Le moniteur est considéré comme disponible seulement à partir du moment où une indication OK a été reçue.

**OK à erreur non confirmée**   
Le temps entre les deux mesures est considéré comme **disponible**, parce qu'il n'est pas encore certain qu'une erreur se soit réellement produite.

**Erreur non confirmée à OK**  
Le temps entre les deux mesures est considéré comme **disponible**.

## Quelles erreurs contribuent à l'indisponibilité ?

Il faut savoir que **toutes les erreurs sont prises en compte** dans le calcul du temps d'indisponibilité.

Par exemple, lorsque vous définissez une limite de performance dans les conditions d'erreur d'un moniteur et que cette limite est atteinte, une erreur est générée pour cette condition. Même si votre site web n'est pas réellement indisponible (mais qu'il fonctionne sous les limites que vous avez fixées), il affichera une disponibilité de moins de 100 % parce que la condition de performance a généré une erreur.

## Comment l'arrêt temporaire des moniteurs affecte-t-il la disponibilité ?

Lorsque vous suspendez un moniteur, le temps pendant lequel il est à l'arrêt est enregistré comme "inconnu". Lors du calcul du pourcentage de disponibilité est calculé, sachez que le nombre total de secondes inconnues est ajouté et marqué comme disponible. La formule de calcul du pourcentage de disponibilité est la suivante : **(temps disponible + temps indisponible) / (temps disponible + temps indisponible + temps inconnu)**, où toutes ces durées sont exprimées en secondes.

Nous avons fait ce choix délibérément, parce que de nombreux clients nous l'ont demandé. Si vous voulez exclure le temps inconnu du calcul de disponibilité, vous pouvez récupérer le nombre total de secondes disponibles et indisponibles et faire votre propre calcul. Pour calculer le pourcentage de disponibilité, suivez cette formule : **temps disponible / (temps disponible + temps indisponible)**, où ces durées sont exprimées en secondes.

## Comment la maintenance affecte-t-elle la disponibilité ?

Les erreurs qui surviennent au cours d'une [période de maintenance]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="fr" >}}) sont exclues des calculs de disponibilité, aussi longtemps que le *type de maintenance* de la période de maintenance contient le réglage **Entièrement désactiver la surveillance** (au lieu de Désactiver seulement les notifications).
