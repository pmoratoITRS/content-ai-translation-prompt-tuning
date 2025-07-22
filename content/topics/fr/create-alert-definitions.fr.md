{
"hero": {
"title": "Créer des définitions d'alerte"
},
"title": "Créer des définitions d'alerte",
"summary": "Cet article vous explique comment définir des alertes adaptées à vos besoins concernant la disponibilité et les performances de votre site web.",
"url": "/support/kb/alerter/creer-definitions-alerte",
"translationKey": "https://www.uptrends.com/support/kb/alerting/create-alert-definitions"
}

La définition d'alerte établit comment et à qui une alerte doit être envoyée, et selon quels niveaux d'escalade. Pour qu'une alerte fonctionne (selon vos besoins), vous devez aussi configurer des [conditions d'erreur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="fr" >}}), qui définissent les circonstances devant entraîner l'envoi d'une alerte.

Chaque [niveau d'escalade]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="fr" >}}) contient une série de paramètres qui définissent les conditions d'envoi de l'alerte, le nombre de rappels, la méthode de notification et les destinataires de l'alerte.

{{< callout >}}
**Remarque** : Une définition d'alerte par défaut est déjà configurée dans votre compte Uptrends. Vous pouvez modifier ses paramètres ou créer une toute nouvelle définition d'alerte.
{{< /callout >}}

## Création d'une définition d'alerte

Pour configurer une définition d'alerte personnalisée :

1. Dans le menu, cliquez sur {{< AppElement type="menuitem" >}} Alerte > Définitions d'alerte {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="button" >}} Ajouter une définition d'alerte {{< /AppElement >}}.
3. Donnez un nom à la définition d'alerte.
3. Cochez la case **Actif** pour activer l'alerte.
4. Choisissez les moniteurs auxquels la définition d'alerte doit s'appliquer.
5. Configurez vos niveaux d'escalade. Pour en savoir plus, lisez l'article sur les [niveaux d'escalade]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="fr" >}}).
6. Cliquez sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.

Vous venez de créer votre propre définition d'alerte. Elle apparaît désormais dans le **dashboard Définitions d'alerte** lorsque vous utilisez le menu {{< AppElement type="menuitem" >}} Alertes > Définitions d'alerte {{< /AppElement >}}.

## Dashboard Définitions d'alerte

Le **dashboard Définitions d'alerte** présente un tableau synthétique où figurent toutes vos définitions d'alerte. Vous pouvez ainsi facilement consulter et vérifier les paramètres de vos définitions d'alerte, soit les informations suivantes :

- **Nom** : fournit le nom attribué à votre définition d'alerte lors de la configuration.
- **Niveaux d'escalade actifs** : précise le nombre de niveaux d'escalade actifs ou activés. Actuellement, le nombre minimum de niveaux d'escalade est fixé à 0 et le maximum est fixé à 3. Les niveaux d'escalade inactifs ne génèrent pas d'alertes.
- **Actif** : cette colonne précise l'état de votre définition d'alerte. Si la définition d'alerte est active, elle affiche *Oui*. Autrement, elle affiche *Non*.

Tous les dashboards d'Uptrends peuvent être exportés pour affiner les informations de surveillance dont vous disposez et y revenir ultérieurement. Lisez cet [article]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="fr" >}}) pour connaître la procédure à suivre pour exporter vos dashboards.

Quel que soit le format choisi, l'export de vos données contient des détails supplémentaires par rapport aux paramètres de définition d'alerte dont il est question dans le premier paragraphe de cette section. Les colonnes supplémentaires sont les suivantes :

- **Moniteurs** : cette colonne précise le ou les moniteurs qui utilisent la définition d'alerte.
- **Groupes de moniteurs** : cette colonne précise le ou les groupes de moniteurs qui utilisent la définition d'alerte.
- **La définition d'alerte est-elle active ?** : cette colonne indique *Oui* si la définition d'alerte est active, et *Non* si elle ne l'est pas.
- **Le niveau d'escalade n est-il actif ?** : cette colonne indique *Oui* si le niveau d'escalade est actif, et *Non* si il ne l'est pas.
- **Opérateurs pour le niveau d'escalade n** : cette colonne indique quels opérateurs sont affectés à chaque niveau d'escalade.
- **Groupes d'opérateurs pour le niveau d'escalade n** : cette colonne indique quels opérateurs sont affectés à chaque niveau d'escalade.
- **Intégrations pour le niveau d'escalade n**: cette colonne indique le type d'intégration ou la plateforme par laquelle vous recevrez vos alertes pour chaque niveau d'escalade. Les intégrations peuvent être *les alertes par e-mail, les alertes par SMS, les alertes par téléphone* et [les alertes personnalisées]({{< ref path="/support/kb/alerting/integrations" lang="fr" >}}).

{{< callout >}}
Comme Uptrends fournit trois niveaux d'escalade, la lettre **n** correspond au numéro du niveau d'escalade que vous avez configuré dans l'éditeur de définition d'alerte.
{{< /callout >}}