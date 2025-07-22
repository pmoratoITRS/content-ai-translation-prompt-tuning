{
"hero": {
"title": "Erreurs non confirmées et confirmées"
},
"title": "Erreurs non confirmées et confirmées",
"summary": "Découvrez la différence entre les erreurs confirmées et non confirmées, et comment elles sont prises en compte dans le calcul des temps d'arrêt.",
"url": "/support/kb/alerter/erreurs/erreurs-non-confirmees-et-erreurs-confirmees",
"translationKey": "https://www.uptrends.com/support/kb/error-analysis/unconfirmed-and-confirmed-errors"
}

L'un des points forts d'Uptrends pour la surveillance de sites web et de serveurs est sa capacité à tenir votre équipe informée des événements affectant leur disponibilité et leur performance. Mais qu'est-ce qui fait exactement qu'une erreur est non confirmée ou confirmée ?

## Différence entre les erreurs non confirmées et les erreurs confirmées

Une **erreur non confirmée** est une erreur détectée lors d'une vérification effectuée par un moniteur depuis un emplacement de checkpoint. Cette erreur doit ensuite être vérifiée par un deuxième checkpoint.

Une **erreur confirmée** est une erreur qui a été vérifiée par deux checkpoints situés à des emplacements distincts.

Cette **double vérification de l'indisponibilité** vise à éviter les fausses alertes. Toutefois, si la double vérification ne confirme pas une erreur, Uptrends suppose que la première erreur non confirmée était un problème temporaire.

{{< callout >}}
**Remarque :** Les erreurs non confirmées sont affichées en jaune dans le dashboard Journal moniteurs. Les erreurs confirmées sont affichées en rouge. L'absence d'erreur est affichée en vert.
{{< /callout >}}

## Comment les erreurs influencent l'indisponibilité et les alertes

Il est important de noter que le service Uptrends ne signale que les erreurs confirmées (doublement vérifiées) au système d'alerte d'indisponibilité.

Pour contrôler le moment où une alerte doit être envoyée, vous pouvez modifier la définition d'alerte par défaut, ou créer votre propre définition. Pour en savoir plus sur les définitions d'alerte, nous vous recommandons de lire l'article [Définitions d'alerte]({{< ref path="support/kb/alerting/create-alert-definitions" lang="fr" >}}).
