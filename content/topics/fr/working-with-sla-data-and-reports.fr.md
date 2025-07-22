{
"hero": {
"title": "Travailler avec les données et rapports SLA"
},
"title": "Travailler avec les données et rapports SLA",
"summary": "Apprenez à lire et à gérer vos données SLA.",
"url": "/support/kb/dashboards-et-rapports/sla/travailler-avec-donnees-et-rapports-sla",
"translationKey": "https://www.uptrends.com/support/kb/sla/working-with-sla-data-and-reports"
}

Par défaut, Uptrends contient un dashboard **Vue d'ensemble SLA** auquel vous pouvez accéder dans le menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Vue d'ensemble SLA {{< /AppElement >}}. Si vous avez créé des [dashboards personnalisés Vue d'ensemble SLA]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-multiple-SLA-definitions#custom-sla-overview-dashboard" lang="fr" >}}), vous les trouverez en ouvrant {{< AppElement type="menuitem" >}} Dashboards > Dashboards personnalisés {{< /AppElement >}}.

Le dashboard Vue d'ensemble SLA vous permet de vérifier la conformité à votre accord de niveau de service, de télécharger des fichiers PDF et Excel avec vos données SLA, et de planifier des rapports SLA réguliers.

## Vue d'ensemble SLA

Par défaut, la **Vue d'ensemble SLA** vous montre vos objectifs SLA et les valeurs réelles dans des colonnes doubles, selon la période choisie dans le menu d'accès rapide.

- **Objectif uptime SLA et Uptime SLA** : la première colonne désigne l'objectif de temps de disponibilité que vous avez défini et la deuxième correspond au pourcentage de disponibilité réel, en prenant en compte tous les jours ou heures que vous avez décidé d'exclure dans votre définition SLA.
- **Objectif temps total SLA et Temps total SLA** : la première colonne désigne la durée maximale en secondes qu'une page peut prendre pour charger sans enfreindre le SLA, et la deuxième colonne correspond aux temps de chargement moyens réels pour la période en question (en secondes).
- **Temps SLA de réponse opérateur et Objectif SLA de réponse opérateur** : la première colonne correspond à la durée maximale autorisée pour qu'un opérateur confirme un problème dans Uptrends, et la deuxième colonne désigne le temps réel enregistré.
- **Erreurs confirmées** : nombre d'erreurs vérifiées pendant la période.
- **Downtime** : total de toutes les indisponibilités, affiché en secondes.
- **Pourcentage downtime** : total de toutes les indisponibilités, affiché en pourcentage.

{{< callout >}}
**Remarque :** Si vous voyez des tirets et des zéros à la place des données dans votre rapport **Vue d'ensemble SLA**, c'est parce que le paramétrage de votre tuile/dashboard a entraîné un conflit dans les données et produit des données non valides. [En savoir plus]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="fr" >}}).
{{< /callout >}}

## Recalculer les données SLA

Tout le monde peut oublier de définir des fenêtres de maintenance et des exclusions temporaires dans les définitions SLA. Bien qu'un oubli puisse fortement embrouiller vos rapports SLA, vous n'êtes pas non plus complètement bloqué avec les mauvaises données.

### Le jour même

Si vous vous apercevez de votre erreur immédiatement, vous pouvez [supprimer les erreurs]({{< ref path="support/kb/alerting/errors/clearing-errors#clear-individual-errors" lang="fr" >}}) dans votre journal de moniteurs.

### Jours précédents (jusqu'à 90)

Supprimer des erreurs liées à des rapports SLA de la veille et de tous les jours précédents s'avère un peu plus compliqué. Uptrends stocke les données SLA séparément de vos données de surveillance courantes. Vos données SLA sont extraites à la fin de chaque journée. Par conséquent, effacer les erreurs dans vos journaux de moniteurs d'hier n'aura aucun impact sur vos rapports de SLA.

Cependant, Uptrends peut vous aider à résoudre ce problème. Suivez les étapes décrites dans l'article [Supprimer des lots d'erreurs]({{< ref path="support/kb/alerting/errors/clearing-errors#bulk-error-clearance" lang="fr" >}}). Cet article vous explique comment remplir une demande contenant les informations nécessaires. D'après ces informations, un ticket sera créé dans le système de tickets d'Uptrends. Pour rappel, la suppression des erreurs et l'actualisation des données SLA peut prendre un certain temps. Le système de ticket vous enverra une notification une fois le processus terminé.

## Télécharger ou partager des rapports de la Vue d'ensemble SLA

Il existe plusieurs méthodes pour télécharger les données d'un rapport SLA sous forme de fichier ou pour partager les données ici de la vue d'ensemble SLA par e-mail.

### Téléchargement

Vous pouvez télécharger le contenu de votre dashboard Vue d'ensemble SLA au format PDF et Excel à tout moment.

Ouvrez votre dashboard **Vue d'ensemble SLA** par défaut ou personnalisé :

1. Définissez les paramètres de date et les moniteurs concernés par le téléchargement dans le menu d'accès rapide.
2. Cliquez sur l'icône hamburger {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
3. Dans le menu, cliquez sur le bouton {{< AppElement type="button" >}}Export PDF{{< /AppElement >}} ou {{< AppElement type="button" >}}Export Excel{{< /AppElement >}}.
4. Attendez qu'Uptrends génère le rapport (cela peut prendre un certain temps si vous avez beaucoup de données) et retrouvez le fichier dans votre dossier de téléchargement.

### Envoi en tant qu'e-mail

Vous pouvez envoyer les données tirées de vos dashboards SLA par e-mail, au format PDF, Excel ou HTML.

1. Ouvrez le dashboard SLA dont vous souhaitez partager les données.
2. Cliquez sur l'icône hamburger {{< AppElement type="iconFeather" >}}{{< /AppElement >}}, puis sur {{< AppElement type="menuitem" >}}Envoyer par e-mail{{< /AppElement >}}.
3. Indiquez les adresses de vos destinataires, puis choisissez le type de fichier et ajoutez des notes, le cas échéant.
4. Cliquez sur le bouton {{< AppElement type="button" >}} Envoyer le rapport {{< /AppElement >}}.

### Planification de rapports pour envoyer des e-mails réguliers {id="scheduling-reports"}

Des rapports planifiés peuvent vous être envoyés par e-mail ainsi qu'à d'autres opérateurs de votre compte, au moyen des **définitions de rapport**. Votre rapport sera envoyé à votre liste de destinataires à partir du dashboard par défaut ou personnalisé **Vue d'ensemble SLA** :

1. Cliquez sur l'icône hamburger {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
2. Cliquez sur {{< AppElement type="menuitem" >}}Planifier rapport{{< /AppElement >}} pour ouvrir la définition du rapport planifié.
3. Complétez les champs des onglets {{< AppElement type="tab" >}}Principal{{< /AppElement >}} et {{< AppElement type="tab" >}}Destinataires{{< /AppElement >}}.
4. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.
5. Pour gérer vos rapports planifiés, passez par le menu {{< AppElement type="menuitem" >}} Configuration de compte > Rapports planifiés {{< /AppElement >}}.
