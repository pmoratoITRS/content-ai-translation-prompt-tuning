{
  "hero": {
    "title": "Arrêt temporaire des alertes"
  },
  "title": "Arrêt temporaire des alertes",
  "summary": "Découvrez comment arrêter temporairement les alertes Uptrends le temps de résoudre le problèle, puis comment réactiver les alertes.",
  "url": "/support/kb/alerter/arret-temporaire-des-alertes",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/temporarily-pausing-alerts"
}

Recevoir des alertes instantanées en cas d'erreur ou d'arrêt est fabuleux, mais il y a des moments où cela ne vous arrange pas. Pour savoir comment arrêter temporairement les alertes d'Uptrends, lisez la suite ...

## Comment arrêter temporairement les alertes

Il est possible d'arrêter temporairement tout ou partie des alertes au moyen **d'une** des **deux méthodes** : *All-Stop*; qui interrompt toutes les alertes en un clic via le tableau de bord Account Overview, ou bien via les *paramètres de vos moniteurs*.

Vous pouvez également choisir de [mettre en place une fenêtre de maintenance]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="fr" >}}) si vous cherchez à de faire des pauses programmées régulièrement.

## Via le All-Stop 

Si vous voulez arrêter toutes vos alertes en une seule fois ...

1.  Connectez-vous à votre compte Uptrends, puis dans le tableau de bord**Account Overview**déplacez votre curseur au-dessus de la barre de titre grise de la fenêtre*Account Status – All Monitors*.
2.  Vous verrez alors apparaître un bouton rouge {{< AppElement type="button" >}}Stop All Alerts{{< /AppElement >}}. Cliquez dessus et confirmez afin de faire une pause dans les alertes.
3.  Pour réactiver les alertes, déplacez votre curseur au-dessus de la barre de titre à nouveau, puis cliquez sur le bouton vert {{< AppElement type="savebutton" >}}Start All Alerts{{< /AppElement >}}.

{{< callout >}}
**Remarque :** Vous devez manuellement réactiver les alertes avant d'en recevoir de nouvelles.
{{< /callout >}}

## Via les paramètres du moniteur

Cette option est particulièrement utile si vous cherchez à arrêter temporairement les alertes pour un moniteur donné.

{{< callout >}}
**Remarque :**Vous devrez manuellement réactiver les alertes dans les paramètres du moniteur lorsque vous voudrez les recevoir à nouveau.
{{< /callout >}}

1.  Connectez-vous à votre compte Uptrends.
2.  Clique sur le lien *Monitors* dans le menu déroulant *Monitor*.
3.  Vous verrez alors une liste des moniteurs en cours d'exécution dans votre compte. Cliquez sur celui pour lequel vous cherchez à arrêter les alertes.
4.  La fenêtre de réglages du moniteur apparaît - pour activer / désactiver les alertes pour ce moniteur, cochez / décochez la case marquée ***Generate Alerts***.
5.  Une fois que vous avez terminé, cliquez sur le bouton vert {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.
