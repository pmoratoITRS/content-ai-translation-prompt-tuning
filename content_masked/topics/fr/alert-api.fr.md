{
  "hero": {
    "title": "API Alert"
  },
  "title": "API Alert",
  "summary": "Apprenez à vous servir de l'API Alert pour récupérer et utiliser les informations d'alerte dans votre compte Uptrends.",
  "url": "[URL_BASE_TOPICS]api/api-alert",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true,
  "tableofcontents": true
}

L'[API Alert]([LINK_URL_1]) contient des endpoints qui fournissent les informations d'alerte provenant d'un moniteur ou d'un groupe de moniteurs.

## Paramètres de l'API Alert

Les paramètres suivants sont disponibles dans l'API Alert :

| Nom | Description |
|--|--|
| [INLINE_CODE_1] | Identifiant unique du moniteur |
| [INLINE_CODE_2] | Identifiant unique du groupe de moniteurs |
| [INLINE_CODE_3] | Une valeur booléenne définie sur **false** par défaut. Si cette valeur est définie sur **true**, les rappels d'alerte sont inclus dans la réponse de l'API. |
| [INLINE_CODE_4]| [SHORTCODE_1] Une valeur de chaîne (requête) utilisée pour parcourir l'ensemble de données. Pour en savoir plus, reportez-vous à la section [Cursor]([LINK_URL_2]). [SHORTCODE_2]|
| [INLINE_CODE_5]| Une chaîne qui trie les alertes par ordre **ascendant** ou **descendant**. |
| [INLINE_CODE_6]| Un nombre entier allant de **0** à **100**, et indiquant le nombre d'enregistrements d'alerte renvoyés. |
| [INLINE_CODE_7]| Un paramètre de date personnalisé (AAAA-mm-jj) couplé au paramètre [INLINE_CODE_8] pour préciser la date de début des enregistrements d'alerte renvoyés. Ce paramètre n'est pas compatible avec la valeur PresetPeriod. |
| [INLINE_CODE_9]| Un paramètre de date personnalisé (AAAA-mm-jj) couplé au paramètre [INLINE_CODE_10] pour préciser la date de fin des enregistrements d'alerte renvoyés. Ce paramètre n'est pas compatible avec la valeur PresetPeriod. |
| [INLINE_CODE_11]| [SHORTCODE_3] Une liste de durées permettant de filtrer les alertes pour une période donnée. Ce paramètre n'est pas compatible avec les valeurs [INLINE_CODE_12] et [INLINE_CODE_13]. Pour en savoir plus, reportez-vous à la section [PresetPeriod]([LINK_URL_3]).  [SHORTCODE_4]|

### Cursor

Le paramètre Cursor agit comme un curseur qui vous permet de parcourir l'ensemble des données d'alerte. Il permet de déterminer quels enregistrements d'alerte ont été générés et quel enregistrement d'alerte vient ensuite.

Par exemple, imaginons que vous souhaitiez récupérer les alertes 101 à 200 sur un total de 300 alertes de moniteur. L'API Alert vous permet de récupérer un maximum de 100 alertes par lot. La réponse de l'appel adressé à l'API pour récupérer le premier lot génère un objet JSON **Cursors** contenant les valeurs **Next** et **Self** :

[CODE_BLOCK_1]

Dans cet exemple, vous utiliserez la valeur **Next** pour récupérer les alertes à partir de la 101e. Vous utiliserez la valeur **Self** comme curseur pour récupérer le premier lot d'alertes (de 1 à 100).

[SHORTCODE_5] **Remarque :** Le paramètre **Cursor** est généré par lot et non par enregistrement d'alerte. Si vous récupérez le premier lot d'alertes et qu'aucune autre alerte ne suit, aucun paramètre **Cursor** ne sera généré. Si d'autres données sont disponibles, un paramètre **Cursor** sera créé pour ce lot. Le paramètre **Take** vous permet de préciser la taille du lot, avec une valeur comprise entre 1 et 100 enregistrements d'alerte. [SHORTCODE_6]

### PresetPeriod

Les options suivantes sont disponibles pour filtrer facilement les alertes au cours d'une période donnée :

- CurrentDay, CurrentWeek, CurrentMonth, CurrentQuarter, CurrentYear
- Previous Day, Previous Week, Previous Month, Previous Quarter, Previous Year
- Last2Hours, Last6Hours, Last12Hours, Last24Hours, Last48Hours
- Last7Days, Last30Days, Last60Days, Last90Days, Last365Days
- Last3Months, Last6Months, Last12Months, Last24Months

Notez que les périodes commençant par "Previous" et "Last" s'appliquent seulement une fois la période entièrement écoulée.

Si vous définissez la valeur **PresetPeriod** sur **Last7Days** et que vous générez des enregistrements d'alerte un lundi à 8h00, vous obtiendrez les résultats du dimanche au dimanche, soit les sept derniers jours complets. Le jour (lundi) auquel vous avez généré le rapport n'est pas inclus car cette période n'est pas encore terminée.

De même, si vous définissez la valeur **PresetPeriod** sur **Last12Months** et que vous générez des enregistrements le 25 janvier 2025, vous obtiendrez les résultats incluant le 31 décembre 2024 et les 11 mois précédents. Les alertes de janvier 2024 et de janvier 2025 ne sont pas incluses dans le rapport car le mois de janvier n'est pas encore terminé.

## Endpoints de l'API Alert

Les méthodes API suivantes sont disponibles :

### GET /Alert/Monitor/{monitorGuid}

Cette méthode renvoie les informations d'alerte pour un moniteur spécifique.

[CODE_BLOCK_2]

### GET /Alert/MonitorGroup/{monitorGroupGuid}

Cette méthode renvoie les informations d'alerte pour un groupe de moniteurs spécifique.

```json
{
  "Data": [
    {
      "Type": "Alert",
      "Id": "afd846be-ddbf-49e1-ad15-2eee5f6d7544",
      "Attributes": {
        "AlertType": "Error",
        "MonitorGuid": "a591a38a-16e0-4dd2-9f15-d575b4c5a433",
        "Timestamp": "2025-01-02T02:30:46",
        "FirstError": "2024-12-11T20:11:01",
        "MonitorCheckId": 171193848695,
        "FirstErrorMonitorCheckId": 169412140540,
        "ErrorDescription": "Step 4 ([URL_1]): Element '.wn-product-btn' not found.",
        "IncidentKey": "9632cd34-0c13-4e2c-92cc-cca104432cd9-0-169412140545"
      },
      "Relationships": [
        {
          "Id": 171193848695,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/171193848695"
          }
        },
        {
          "Id": 169412140540,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/169412140540"
          }
        }
      ]
    },
    .....
  ]
}

