{
  "hero": {
    "title": "Supprimer des erreurs"
  },
  "title": "Supprimer des erreurs",
  "summary": "Découvrez comment effacer les erreurs incorrectes ou indésirables dans l'historique d'erreurs",
  "url": "[URL_BASE_TOPICS]alerter/erreurs/supprimer-des-erreurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Vous avez la possibilité d'effacer des erreurs ou des groupes d'erreurs (non confirmées et confirmées) que vous jugez incorrectes ou indésirables. Les erreurs individuelles ou peu nombreuses peuvent être effacées par vos soins. Si vous avez de nombreuses erreurs à effacer, Uptrends est là pour vous aider. Pour savoir comment faire, consultez la section [Supprimer des lots d'erreurs]([LINK_URL_1]).

Sachez que la suppression d'erreurs n'est pas suivie automatiquement d'une actualisation du calcul des métriques basées sur les erreurs, comme les statistiques des accords de niveau de service ([SLA]([LINK_URL_2])) ou les données chiffrées des [pages de statut publiques]([LINK_URL_3]). Lisez la section [Incidence sur les données des SLA et des pages de statut publiques]([LINK_URL_4]) pour savoir comment recalculer les statistiques, selon que les erreurs ont été effacées par vous-même ou par le Support.

[SHORTCODE_1]
**Remarque** : Malheureusement, il est impossible de recalculer les données des SLA supérieures à 90 jours, car ces données ne sont pas conservées au-delà de cette période.
[SHORTCODE_2]

## Comment effacer des erreurs individuelles [ANCHOR_1]

Pour effacer une erreur dans votre compte :
1. Ouvrez le menu [SHORTCODE_3]Surveillance > Journal moniteurs[SHORTCODE_4].
2. Cliquez sur l'erreur que vous souhaitez effacer. La fenêtre contextuelle *Voir les détails* relative à cette erreur s'affiche.
3. En bas de la fenêtre, cliquez sur le bouton [SHORTCODE_5]Effacer erreur[SHORTCODE_6].
4. Confirmez l'action avec le bouton [SHORTCODE_7] Effacer [SHORTCODE_8].

L'erreur se transforme en un résultat "OK", qui devient immédiatement visible dans le dashboard *Journal moniteurs*.

Les données relatives au pourcentage de disponibilité sont aussi modifiées. Pour des raisons de mise en cache, les changements peuvent ne pas être visibles immédiatement.

## Supprimer des lots d'erreurs [ANCHOR_2]

Dans certaines situations, vous pouvez avoir besoin de supprimer des erreurs pour une plage de temps spécifique (par exemple, plusieurs journées d'indisponibilité). Plutôt que d'effacer chaque erreur individuellement, nous vous recommandons de procéder comme suit :

1. Si une fenêtre contextuelle *Voir les détails* est ouverte, cliquez sur le bouton [SHORTCODE_9] Effacer les erreurs multiples [SHORTCODE_10] en bas de cette fenêtre. Le formulaire *Demande de suppression des erreurs* s'affiche.
2. Vous pouvez aussi passer par le menu [SHORTCODE_11] Support [SHORTCODE_12] et cliquer sur l'option [SHORTCODE_13] Demande pour effacer les erreurs [SHORTCODE_14]. Le formulaire *Demande de suppression des erreurs* s'affiche.
3. Indiquez les informations obligatoires, à savoir le moniteur ou les groupes de moniteurs concernés, et la plage de dates. Ajoutez toute information facultative en lien avec votre requête, comme le code de statut.
4. Cliquez sur le bouton [SHORTCODE_15] Envoi [SHORTCODE_16].

Lorsque vous envoyez une requête, un ticket est automatiquement créé pour que votre demande soit traitée. Le traitement de votre demande peut prendre un certain temps, mais le système de ticket vous enverra une notification lorsque la suppression des erreurs et l'actualisation des données SLA auront été effectuées.

## Incidence sur les données des SLA et des pages de statut publiques [ANCHOR_3]

La suppression d'erreurs n'est pas suivie automatiquement d'une modification des données relatives aux accords de niveau de service existants [SLA]([LINK_URL_5]), ni des données des [pages de statut publiques]([LINK_URL_6]), qui sont aussi liées aux SLA.

Il est toutefois possible de les recalculer. Lorsque vous demandez à l'équipe de support de [supprimer plusieurs erreurs]([LINK_URL_7]), un nouveau calcul des données est effectué automatiquement. Il n'est pas nécessaire d'en faire la demande.

En revanche, la situation est différente si vous supprimez vous-même les erreurs. Dans ce cas, veuillez contacter le support au moyen d'un [ticket]([LINK_URL_8]) dans lequel vous indiquerez votre besoin.
