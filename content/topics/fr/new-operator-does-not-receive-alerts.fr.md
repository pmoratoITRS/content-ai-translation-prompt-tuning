{
"hero": {
"title": "Un nouvel opérateur ne reçoit pas d'alertes"
},
"title": "Un opérateur ne reçoit pas d'alertes",
"summary": "Cet article vous explique comment procéder si un nouvel opérateur ne reçoit pas d'alertes.",
 "url": "/support/kb/alerter/nouvel-operateur-ne-recoit-pas-d-alertes",
"translationKey": "https://www.uptrends.com/support/kb/alerting/new-operator-does-not-receive-alerts"
}

Toute équipe d'opération a besoin de connaître l'état des sites web, serveurs et services web. Si un nouvel opérateur de votre compte Uptrends **ne reçoit pas d'alertes**, cela peut avoir des conséquences importantes. Mais ne vous inquiétez pas, nous sommes là pour vous aider !

## Vérification des définitions d'alerte

La première chose que vous devez faire est de vérifier la **définition d'alerte** mise en place pour le service sous surveillance.

**Définitions d'alerte par défaut**

Chaque compte Uptrends est préconfiguré avec une *définition d'alerte par défaut*, qui envoie des alertes au groupe d'opérateurs *Tout le monde* dès lors qu'un moniteur du groupe *Tous les moniteurs* trouve une erreur. Cela signifie que pour chaque erreur survenue, tous les opérateurs sont avertis, parce que par défaut, tous les opérateurs sont automatiquement membres du groupe d'opérateurs *Tout le monde*.

**Définitions d'alerte par défaut modifiées ou personnalisées**

Certains utilisateurs choisissent de modifier les paramètres de la définition d'alerte par défaut, ou de créer leur propre *définition d'alerte personnalisée* à partir de zéro. Dans ces cas, les nouveaux opérateurs ne sont pas automatiquement ajoutés aux définitions d'alerte, et ne reçoivent donc pas les alertes.

Pour savoir comment ajouter un opérateur (ou un groupe d'opérateurs) à une définition d'alerte, consultez l'article [Niveaux d'escalade des alertes]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="fr" >}}) dans notre base de connaissances.
