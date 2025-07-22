{
  "hero": {
    "title": "Erreurs et alertes pour les moniteurs de Surveillance simultanée"
  },
  "title": "Erreurs et alertes pour les moniteurs de Surveillance simultanée",
  "summary": "Comment fonctionnent la génération d'erreurs et les alertes pour les moniteurs de Surveillance simultanée ?",
  "url": "/support/kb/surveillance-synthetique/surveillance-simultanee/erreurs-alertes-pour-moniteurs-surveillance-simultanee",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors"
}

Par rapport à la surveillance standard, la génération d'erreurs pour la surveillance simultanée est légèrement différente. La surveillance standard suit généralement une séquence de *[Ok (vert) - Erreur non confirmée (jaune) - Erreur confirmée (rouge)](/support/kb/alerter/erreurs/erreurs-non-confirmees-et-erreurs-confirmees)* pour la génération d'erreurs, les alertes étant générées après un nombre spécifié d'erreurs confirmées pour une surveillance donnée. Pour la surveillance simultanée cependant, les erreurs sont générées différemment. Dans cet article, nous allons examiner en profondeur comment un moniteur de surveillance simultanée génère des erreurs. Gardez à l'esprit qu'une fois les erreurs générées, l'alerte fonctionne [de la même manière que pour la surveillance standard](/support/kb/alerter).

## Seuils d'erreur pour la surveillance simultanée

Lors de la création d'un moniteur de Surveillance simultanée (ou de la mise en mode surveillance simultanée d'un moniteur existant), vous aurez à remplir deux nouveaux champs : **Seuil d'erreur non confirmé** et **Seuil d'erreur confirmé**. En outre, un moniteur de Surveillance simultanée nécessite un minimum de 3 points de contrôle à haute disponibilité, ou 5 points de contrôle sélectionnés parmi l'ensemble complet. Ensemble, ces paramètres déterminent les circonstances dans lesquelles la vérification reçoit un statut Ok, une erreur non confirmée ou une erreur confirmée. En bref, un moniteur de Surveillance simultanée signalera les erreurs si le nombre de points de contrôle qui détectent individuellement une erreur dépasse les seuils fixés.

Prenons l'exemple d'un moniteur Https, qui a un seuil d'erreur non confirmé de 30 %, un seuil d'erreur confirmé de 50 % et 10 points de contrôle sélectionnés.

-   En temps normal, chacun des points de contrôle sélectionnés individuellement renvoie un résultat correct - aucun des points de contrôle qui exécutent le test en même temps ne détecte d'erreur, ce qui signifie que le pourcentage d'erreur est de 0 %. Dans ce cas, le résultat global de la surveillance simultanée est *Ok*.
-   Si deux des points de contrôle sélectionnés détectent une erreur, le pourcentage d'erreur est de 20 % (puisque 2 sur 10 des points de contrôle sélectionnés ont détecté une erreur). Comme aucun des deux seuils d'erreur n'est atteint, le résultat global du contrôle est toujours indiqué comme *Ok*.
-   Dans le cas où quatre des points de contrôle sélectionnés détectent des erreurs, le pourcentage d'erreur devient 40 %. Ce taux dépasse le seuil d'erreur non confirmée (30 %), mais pas le seuil d'erreur confirmée (50 %). Le résultat global du contrôle sera *non confirmé*, et ne déclenchera donc en aucun cas une alerte.
-   Lorsque cinq (ou plus) points de contrôle détectent individuellement une erreur, le pourcentage d'erreur atteint ou dépasse le seuil d'erreur confirmé. Dans ce cas, le résultat global sera immédiatement enregistré comme une erreur *confirmée*. Cette situation va donc déclencher une alerte, selon les paramètres de vos définitions d'alerte.

Dans l'image ci-dessous, vous pouvez voir que deux des six points de contrôle sélectionnés (ou \~33%) ont signalé une erreur. Cela dépasse le seuil pour les erreurs *non confirmées* (25 % dans cet exemple), mais pas le seuil pour les erreurs *confirmées* (fixé à 50 %). Cela signifie que le résultat global de la vérification est *non confirmé*, et ne générera pas d'alerte. ![](/img/content/5d220dc1-4e11-45a7-b13f-152bd67a10b1.png)

En d'autres termes, la surveillance simultanée ne vérifie pas ses erreurs de la même manière que les contrôles standard. Un moniteur standard, lorsqu'il détecte une erreur, effectue immédiatement un nouveau test à partir d'un autre point de contrôle pour confirmer l'erreur. Pour la surveillance simultanée, nous allons plus loin dans la robustesse en effectuant les vérifications à partir de plusieurs endroits en même temps. Si un certain nombre d'entre elles détectent des erreurs, on peut supposer que l'erreur est authentique.

{{< callout >}}
**Remarque :** les contrôles individuels des moniteurs ne suivent pas le schéma d'erreurs *Ok - Non confirmé - Confirmé*. Les contrôles individuels donneront soit *Ok* (vert) ou *Confirmés* (rouge). Étant donné que le statut de votre moniteur est décidé en fonction des seuils d'erreur que vous avez fixés, une erreur individuelle confirmée ne provoquera pas d'alerte par elle-même.
{{< /callout >}}

## Les indisponibilités des points de contrôle

Comme notre [réseau mondial de points de contrôle](/checkpoints) est très étendu, des temps d'arrêt sont inévitables. Principalement c'est en raison d'un entretien régulier, mais parfois, pour d'autres raisons, certains points de contrôle peuvent ne pas être disponibles pour l'exécution de votre contrôle. Si cela se produit pour l'un des points de contrôle que vous avez sélectionnés pour votre moniteur de Surveillance simultanée pendant qu'une vérification est en cours, le résultat global du contrôle affichera une icône grise **?** pour ce point de contrôle spécifique. Le résultat pour ce point de contrôle sera *non-concluant*, et nous n'en tiendrons pas compte dans le calcul du dépassement du seuil d'erreur. ![](/img/content/052d85fc-3b36-448c-b4bd-e30431fe53a8.png)
