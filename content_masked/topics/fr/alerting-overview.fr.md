{
  "hero": {
    "title": "Présentation des alertes"
  },
  "title": "Présentation des alertes",
  "summary": "Cet article vous explique comment fonctionnent les alertes. La vérification effectuée par le moniteur génère une erreur, qui génère une alerte, qui déclenche un message via une définition d'alerte.",
  "url": "[URL_BASE_TOPICS]alerter/vue-densemble-des-alertes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans un environnement réel, les sites web, les serveurs et tous les autres systèmes doivent fonctionner sans interruption et garantir une disponibilité de service continue. Les alertes sont alors un outil précieux pour être immédiatement informé lorsqu'un problème ou une anomalie survient dans votre système. Elles vous garantissent que votre système est toujours opérationnel et vous aident à réduire les temps d'arrêt.

Les **alertes** sont l'une des principales fonctionnalités du service de monitoring d'Uptrends. Lorsque votre moniteur détecte une erreur, vous recevez immédiatement un message d'alerte. L'illustration ci-dessous résume le workflow propre aux alertes d'Uptrends :

![Illustration montrant le workflow des alertes]([LINK_URL_1])

Dans les faits, une alerte est créée dès que ces quatre définitions existent : *une vérification par le moniteur, une condition d'erreur, une définition d'alerte et une intégration*. Une fois que vous avez créé et configuré votre moniteur et ses paramètres, ce dernier effectue les vérifications définies dans ses paramètres. Si une vérification de moniteur donne lieu à une [erreur confirmée]([LINK_URL_2]), une alerte est générée dans l'application web d'Uptrends. Cette alerte déclenche à son tour l'envoi d'un message à un opérateur ou à une application tierce.


Dans cet article, nous allons voir étape par étape comment une vérification effectuée par un moniteur génère un message d'alerte.

## Vérifications effectuées par un moniteur

Les moniteurs effectuent des vérifications aux intervalles que vous avez prédéfinis. Il peut s'agir de vérifications standard, dont l'objet dépend du type de moniteur, comme la disponibilité. De plus, vous pouvez définir vos propres conditions d'erreur, comme une limite pour le temps de chargement ou la recherche d'une correspondance dans le contenu de la page.

![Paramètres des vérifications de moniteur]([LINK_URL_3])

Pour savoir comment configurer les conditions d'erreur, lisez l'article de notre base de connaissances intitulé [Conditions d'erreur]([LINK_URL_4]).

Une erreur est signalée dès que le contrôle effectué par le moniteur trouve un problème lié à une vérification standard ou à une condition d'erreur.

## Erreurs

Toutes les erreurs sont visibles dans la section **Vue d'ensemble des erreurs**. Vous pouvez utiliser des filtres pour afficher certains types d'erreur (*OK, non confirmées, confirmées*) et définir les périodes à examiner. Pour en savoir plus sur les filtres et la personnalisation des paramètres de dashboard, lisez l'article de notre base de connaissances sur les [dashboards]([LINK_URL_5]).

Dans l'exemple suivant, la vue d'ensemble des erreurs montre les erreurs non confirmées (marquées en jaune) et confirmées (marquées en rouge) :

![Dashboard Vue d'ensemble des erreurs]([LINK_URL_6])

Comme l'indique l'illustration, la première occurrence d'une erreur est appelée une erreur non confirmée. Cette erreur n'est pas confirmée car elle peut être provisoire ou liée à un problème de checkpoint. C'est pourquoi une deuxième vérification est effectuée par le moniteur à partir d'un autre checkpoint. Si une erreur est signalée, le résultat est une erreur confirmée qui donne lieu à une alerte.

Pour en savoir plus sur ce principe, lisez l'article de notre base de connaissances intitulé [Erreurs non confirmées et confirmées]([LINK_URL_7]).

### Séquences d'erreurs

L'image ci-dessous montre les différents scénarios possibles pour les séquences d'erreurs.

- Une erreur non confirmée est suivie d'un résultat OK. Cela ne produit pas d'alerte.
- Une erreur non confirmée est suivie d'une erreur confirmée, puis du résultat OK. Cela se traduit par une alerte si l'option suivante est cochée dans votre définition d'alerte : "Générer une alerte quand 1 erreur(s) ou plus se sont produites".
- Un certain nombre (n) d'erreurs non confirmées et confirmées se produisent d'affilée. Cela se traduit par une alerte si l'option suivante est cochée dans votre définition d'alerte : "Générer une alerte quand n erreurs ou plus se sont produites". Vous pouvez également définir un délai pour les erreurs. Si la séquence d'erreurs atteint ce délai, par exemple si les erreurs se produisent pendant plus de 5 minutes, une alerte est créée.

![]([LINK_URL_8])

## Alertes

La définition d'alerte détermine la génération d'alertes pour différents niveaux d'escalade. Les niveaux d'escalade permettent de créer des alertes par étapes et d'avertir les opérateurs sélectionnés de la façon voulue, en tenant compte de l'urgence du problème et de l'augmentation de cette urgence si le problème persiste.

Pour chaque niveau, vous devez définir si une alerte est créée, quel opérateur (ou groupe d'opérateurs) est averti, après quel délai l'alerte est générée (si les erreurs se produisent pendant plus de x minutes) ou si l'alerte est créée après un certain nombre d'occurrences (une ou plusieurs erreurs se sont produites). Toutes les erreurs doivent être confirmées. Les erreurs non confirmées ne sont pas prises en compte pour ces conditions.

En plus de l'alerte d'origine, vous pouvez générer une ou plusieurs alertes de rappel. Vous devez définir le nombre maximum de rappels et l'intervalle de temps entre deux rappels. Cette option existe pour chaque niveau d'escalade.

Les articles de la base de connaissances [Créer des définitions d'alerte]([LINK_URL_9]) et [Niveaux d'escalade des alertes]([LINK_URL_10]) contiennent plus d'informations sur les définitions d'alerte.

Notez que le moniteur doit avoir la case *Générer alerte* activée afin de pouvoir générer des alertes.

Une fois l'erreur résolue (ce qui signifie que la même vérification renvoie le résultat OK au lieu d'une erreur), une alerte de récupération (alerte OK) est créée.

Toutes les alertes figurent dans l'**historique des alertes**. Les alertes dues à une erreur sont marquées en rouge et les alertes OK sont marquées en vert. Tant que l'erreur n'est pas résolue et qu'aucune alerte de récupération n'a été générée, l'alerte reste active. Les alertes actives figurent dans le dashboard **Statut d'alerte actuel**.

![]([LINK_URL_11])

Vous cherchez une **définition d'alerte** que vous avez créée ? Vous pouvez utiliser la [fonctionnalité de recherche]([LINK_URL_12]) pour la retrouver rapidement.

## Messages

Grâce au dashboard **Historique des alertes**, vous pouvez surveiller régulièrement vos alertes et les consulter depuis un même endroit. Toutefois, il est aussi pratique de recevoir des notifications en temps réel sur vos alertes sans devoir ouvrir l'application web. Uptrends fonctionne avec des [intégrations]([LINK_URL_13]), qui vous fournissent tout un ensemble d'options pour envoyer des messages d'alerte à vous-même, à d'autres personnes ou à des systèmes tiers. Les intégrations vous permettent aussi de recevoir des notifications immédiates.

Pour envoyer un message lorsqu'une alerte est générée, vous devez configurer une [définition d'alerte]([LINK_URL_14]), puis choisir le type d'[intégration]([LINK_URL_15]) que vous souhaitez pour chaque niveau d'escalade. Une fois cela effectué, vous pouvez facilement recevoir des mises à jour grâce à l'intégration que vous avez choisie.

### Tests des messages

Pour recevoir des alertes aussi rapidement que possible, vous devez d'abord vous assurer que l'envoi des messages fonctionne correctement. Pour savoir comment faire pour les différentes intégrations, lisez l'article de notre base de connaissances intitulé [Tester les messages d'alerte]([LINK_URL_16]).

Consultez la section de [dépannage]([LINK_URL_17]) pour en savoir plus.