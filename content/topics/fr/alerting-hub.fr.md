{
  "hero": {
"title": "Hub d'alertes"
},
"title": "Hub d'alertes",
"summary": "Le point de départ idéal pour explorer les alertes",
  "url": "/support/kb/alerter/hub-pour-alertes",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alerting-hub",
  "tableofcontents": false
}

La fonction d'alerte est un sujet complexe, et nécessite que de nombreux paramètres fonctionnent bien ensemble pour obtenir le résultat attendu. Elle dépend de la bonne configuration des conditions d'erreur, des définitions d'alerte, des niveaux d'escalade et des intégrations. Il y a donc beaucoup de paramètres à régler et le hub est là pour vous aider.

Le hub vous présente le fonctionnement théorique des alertes en vous orientant vers les concepts clés et les autres sujets pertinents dans la base de connaissances. Depuis le hub, vous pouvez accéder directement aux paramètres pertinents dans l'application Uptrends. Vous y trouverez aussi des indications sur la situation réelle : y a-t-il des alertes actives ? Les éléments sur lesquels vous comptez, comme les définitions d'alertes et les intégrations, sont-ils actifs ? Enfin, le hub vous indique s'il vous reste des crédits de message.

Pour ouvrir le hub Alertes, cliquez sur {{< AppElement type="menuitem" >}}Alerte > Explorer les alertes{{< /AppElement >}} dans le menu principal.

![](/img/content/scr-alerting-hub.min.png)

La partie supérieure du hub et la barre latérale contiennent des liens vers les concepts clés et des explications sur la configuration des alertes. Un certain nombre de liens renvoient aux articles de la base de connaissances. D'autres liens vous amènent directement à l'application où vous pourrez configurer les définitions nécessaires au fonctionnement des alertes.

La partie inférieure du hub vous informe sur la situation réelle de vos alertes, par exemple en vous indiquant le nombre de moniteurs qui ont des alertes en place. Cette vue d'ensemble est personnalisée et suit les règles suivantes :

- Seuls les moniteurs ou les définitions d'alerte pour lesquels vous avez l'autorisation d'[afficher les données des moniteurs]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="fr" >}}) ou de [modifier les définitions d'alerte]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="fr" >}}) s'affichent.
- Seules les intégrations pour lesquelles vous avez l'autorisation **Modifier l'intégration** s'affichent. Les autres intégrations ne s'affichent pas.



De là, vous pouvez accéder directement :

- aux moniteurs qui figurent en tête de la liste des alertes ;
- aux alertes en cours, ce qui vous amène au tableau de bord *Statut d'alerte* ;
- à l'historique complet des alertes, ce qui vous amène au tableau de bord *Journal d'alertes*.

Par ailleurs, des statistiques concernant votre configuration d'alerte vous donnent un aperçu de la situation et vous aident à résoudre les problèmes. Ces statistiques vous indiquent le nombre :

- d'intégrations actives ;
- de [moniteurs couverts par les définitions d'alerte]({{< ref path="support/kb/alerting/monitor-alerting-coverage" lang="fr" >}}) (uniquement les moniteurs en [mode production]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode#monitormodeproduction" lang="fr" >}})) ;
- de définitions d'alertes actives ;
- de crédits de messages disponibles.

Quand vous consultez la statistique **Définitions d'alerte actives**, gardez à l'esprit que ce chiffre ne tient compte que des définitions qui sont actives et qui ont au moins un niveau d'escalade actif. Il est tout à fait possible d'avoir une définition d'alerte active sans niveau d'escalade actif. Dans ce cas, des alertes seront générées (si vous les avez configurées) telles que vous les voyez dans l'application Uptrends, par exemple dans le journal des alertes, mais aucun message d'alerte ne sera envoyé aux opérateurs et cette définition ne sera pas comptabilisée dans la statistique **Définitions d'alertes actives**.

Il doit aussi y avoir au moins une intégration dans un niveau d'escalade de la définition d'alerte, pour laquelle l'autorisation **Utiliser l'intégration** (ou une autre autorisation supérieure) a été accordée à l'opérateur actuel. Autrement, la définition d'alerte ne figurera pas parmi les définitions actives.
