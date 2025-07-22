{
  "hero": {
"title": "Rappels d'alerte dans les niveaux d'escalade"
  },
"title": "Rappels d'alerte dans les niveaux d'escalade",
"summary": "Les définitions d'alertes proposent une option de rappel pour tous les niveaux d'escalade.",
"url": "/support/kb/alerter/rappels-d-alertes-dans-les-niveaux-d-escalade",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-reminders-in-escalations"
}

## Qu'est-ce qu'un rappel ?

Un rappel est une méthode qui permet d'informer les opérateurs d'une erreur, jusqu'à sa résolution. Lorsqu'une alerte est générée (toujours sur la base d'une erreur confirmée), les opérateurs ou les systèmes peuvent être informés par message (à l'aide d'une intégration). Les opérateurs doivent ensuite prendre des mesures pour résoudre le problème signalé. S'ils ne voient pas le message ou n'y donnent pas suite, vous pouvez envoyer des rappels pour attirer leur attention sur le problème ou pour insister sur son caractère urgent.  
Si les SLA (accords de niveau de service) conclus entre vous et vos clients garantissent qu'une solution sera trouvée dans un délai spécifié, vous avez intérêt à ce que les opérateurs reçoivent le message et agissent conformément aux attentes énoncées dans l'accord.

Dans l'application Uptrends, la configuration des rappels se fait dans les niveaux d'escalade des définitions d'alertes. Selon les niveaux d'escalade prévus dans vos contrats SLA, le mécanisme de rappel d'Uptrends pourrait vous intéresser.

Si une alerte persiste, les rappels sont envoyés selon vos spécifications tant qu'aucune alerte OK n'est générée. Dès que l'erreur signalée est résolue (par une vérification OK et une alerte OK), l'envoi de rappels s'arrête.

## Comment configurer des rappels

Le paramètre *Rappels* se trouve dans les [niveaux d'escalade]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="fr" >}}) des définitions d'alerte.

![](/img/content/c8407764-8f48-49fa-8608-79e3ee2b1c4f.png)

Définissez le nombre maximum de rappels ainsi que l'intervalle entre les rappels en complétant la phrase suivante avec les valeurs correspondant à "n" et "x" :  
*Envoyer un maximum de 'n' rappels d'alerte toutes les 'x' minutes.*

Tenez compte des conseils ci-dessous pour définir les valeurs :

- Si vous ne souhaitez pas envoyer de rappels, indiquez 0 à la place de "n"
- Synchronisez l'intervalle de rappel "x" avec l'intervalle d'escalade (si vous l'utilisez). Par exemple, si votre définition d'escalade est "Générer une alerte quand une erreur dure plus de 5 minutes", un intervalle de rappel de 3 minutes n'aurait pas de sens.
- Prenez en compte l'intervalle de vérification (dans les paramètres du moniteur). Si les rappels sont plus fréquents que les vérifications du moniteur, le fonctionnement ne sera pas efficace. Vous pourriez vous retrouver avec une situation où vous envoyez un rappel alors même que la prochaine vérification du moniteur renvoie un résultat OK, ce qui rendrait votre rappel inutile.

{{< callout >}}
**Remarque :** Pour garder le contrôle de vos rappels, évitez tout chevauchement entre les rappels des différents niveaux d'escalade. Par exemple, si vous définissez 3 rappels toutes les 5 minutes au niveau d'escalade 1, et que le niveau d'escalade 2 se déclenche après 10 minutes, les deux niveaux de rappel vont se chevaucher.
{{< /callout >}}

## Intégrations adaptées aux rappels

Les intégrations définissent la façon dont un message est envoyé une fois qu'une alerte est créée. Toutes les intégrations ne sont pas compatibles avec les rappels.

La configuration des rappels fonctionne bien avec les intégrations comme l'e-mail, les SMS et Slack. Autrement dit, les rappels ont un sens pour les intégrations où une personne réelle reçoit le message et agit en conséquence.

Pour d'autres intégrations comme PagerDuty, Statushub, Splunk On-Call, ServiceNow et certainement plusieurs intégrations personnalisées, les rappels ne sont pas adaptés. Souvent, ces intégrations définissent un statut dans le système d'après une alerte d'erreur ou une alerte OK. Un rappel ne changera pas ce statut, et n'a donc aucun sens dans la plupart des cas. Le statut d'erreur persistera dans le système jusqu'à ce que le système reçoive une notification d'alerte OK. Un rappel ne modifie pas ce processus et n'est donc pas recommandé.
