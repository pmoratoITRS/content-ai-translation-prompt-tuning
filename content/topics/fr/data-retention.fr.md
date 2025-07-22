{
  "hero": {
    "title": "La conservation des données"
  },
  "title": "Conservation des données",
  "summary": "Informations sur la conservation des données de surveillance Uptrends : quelles données sont conservées et pour combien de temps.",
  "url": "/support/kb/dashboards-et-rapports/dashboards/conservation-des-donnees",
  "translationKey": "https://www.uptrends.com/support/kb/reporting/data-retention"
}

La collecte de grandes quantités de données concernant *disponibilité* et *performance* est essentielle pour maximiser le potentiel de votre site web, de votre serveur et de votre application web, mais toute cette collecte est inutile si vous ne pouvez pas conserver les données au fil du temps.

Uptrends peut conserver les données à long terme des utilisateurs payants afin qu'ils puissent tirer le meilleur parti de leurs données de surveillance. La durée de conservation varie en fonction de votre plan d'abonnement.

## Uptrends Synthetics
### Les mesures individuelles de surveillance

Le service d'Uptrends maintient les données de surveillance individuelles des clients payants **pendant 90 jours**, y compris des données telles que :

-   Données de vérifications des moniteurs individuels
-   Les captures d'écran des vérifications
-   Données de cascade FPC
-   Données détaillées des transactions

**Conservation des données pour les mesures individuelles de surveillance par plan**

| Starter  | Premium  | Professional | Business | Enterprise |
|----------|----------|--------------|----------|------------|
| 14 jours | 30 jours | 60 jours     | 90 jours | 90 jours   |

### Les données statistiques

Les données statistiques restent à votre disposition **pendant 2 ans** après leur collecte pour les clients payants. Elles comprennent ce que vous voyez généralement dans les tableaux et les graphiques, par exemple :

-   La disponibilité moyenne en %
-   Le temps de chargement moyen
-   Les données SLA calculées

**Conservation des données pour les statistiques par plan**

| Starter | Premium | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| 1 an    | 1 an    | 2 ans        | 2 ans    | 2 ans      |

### Les rapports précédemment générés

Les données historiques des rapports déjà générés restent disponibles **pendant 2 ans** pour les clients payants. Les données disponibles comprennent :

-   Rapports PDF
-   Rapports Excel
-   Rapports par e-mail

Vous pouvez télécharger ces données depuis l'onglet {{< AppElement type="tab" >}}Historique{{< /AppElement >}} de tout rapport planifié.

**Conservation des données pour les rapports planifiés précédemment générés par plan**

| Starter | Premium | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| 1 an    | 1 an    | 2 ans        | 2 ans    | 2 ans      |

### Les données FPC\+ détaillées

Les données FPC\+ (ou Full Page Check\+) sont conservées et restent disponibles pour les clients payants **pendant 21 jours** à partir de la date initiale de collecte des données.

## Uptrends Real User Monitoring (RUM)

Les données de Real User Monitoring (RUM) sont immédiatement traitées et stockées sous forme de données statistiques:

  - la médiane
  - la moyenne
  - le minimum
  - le maximum

Vous pouvez ensuite inspecter ces données avec une précision d'intervalles de cinq minutes. Les données basées sur les intervalles de cinq minutes restent disponibles **pendant 90 jours**, en fonction de votre plan.

Pour pouvoir analyser les tendances à long terme, nous combinons les intervalles de cinq minutes en intervalles d'une heure. Uptrends conserve et stocke les données **pendant deux ans**, en fonction de votre plan. Vous pouvez consulter ces données avec un affichage par heure ou par mois.

Conservation des données RUM par plan :

| Intervalle       | Starter  | Premium  | Professional | Business | Enterprise |
|------------------|----------|----------|--------------|----------|------------|
| **Cinq minutes** | 14 jours | 30 jours | 60 jours     | 90 jours | 90 jours   |
| **Une heure**    | 1 an     | 1 an     | 2 ans        | 2 ans    | 2 ans      |


## Uptrends Infra

### Mesures individuelles

Les mesures individuelles suivantes des abonnements payants sont conservées **jusqu'à 90 jours**:

- Journaux des appareils
- Captures d'écran des capteurs http
- Valeurs individuelles des capteurs
- Informations d'erreurs individuelles

**Conservation des données pour les mesures individuelles par plan :**

| Starter | Premium | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| 14 jours | 30 jours | 60 jours | 90 jours | 90 jours |


### Données statistiques

Pour les abonnements payants, les données statistiques Infra restent à votre disposition **pendant 2 ans** après leur collecte. Ces données comprennent :

- Valeurs moyennes des capteurs
- Moyennes journalières pour les mesures des capteurs
- Nombre total d'erreurs (nombre d'erreurs et d'avertissements) par jour
- Temps de disponibilité total par appareil et par jour
- Derniers états de l'appareil
- Dernières valeurs des capteurs
- Alertes

**Conservation des données pour les données statistiques par plan :**
| Starter | Premium | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| 1 an  | 1 an  | 2 ans      | 2 ans  | 2 ans    |