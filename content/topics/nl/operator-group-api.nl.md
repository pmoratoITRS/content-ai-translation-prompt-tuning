{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "De beschikbare API-methodes voor het manipuleren van operatorgroepen.",
  "url": "/support/kb/api/operator-group-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-group-api"
}

Op deze pagina worden de beschikbare API-methodes voor het manipuleren van operatorgroepen beschreven. Operatorgroepen worden gebruikt om de operators (gebruikersaccounts) in uw account te organiseren. Deze API leverde methoden voor het beheren van elke groep en voor het toevoegen/verwijderen van operators aan/uit een groep.

## Objectbeschrijving operatorgroep

Het volgende OperatorGroup-object wordt gebruikt in de hieronder beschreven API-methodes:

| Naam                   | Beschrijving                                                 | Datatype |
|------------------------|-------------------------------------------------------------|-----------|
| `OperatorGroupGuid`    | De unieke ID van deze operatorgroep.              | Guid      |
| `Description`          | Een string die een beschrijvende naam bevat.                     | String    |
| `IsEveryone`           | Geeft aan of dit de systeemgroep “Iedereen” is.      | Boolean   |
| `IsAdministratorGroup` | Geeft aan of dit de systeemgroep “Administrators” is. | Boolean   |

De groep “Iedereen” is een automatische, door het systeem gecreëerde groep. De groep Iedereen kan niet worden gewijzigd: elke operator wordt automatisch aan deze groep toegevoegd.

De “Administrators” is ook een door het systeem gecreëerde groep, maar u kunt individuele operators aan deze groep toevoegen of ze er weer uit verwijderen. Wanneer een operator wordt toegevoegd als lid van de groep Administrators, worden alle administratorrechten automatisch toegewezen aan die operator.

## Eindpunten OperatorGroup

De volgende API-eindpunten zijn beschikbaar voor het ophalen, maken, bijwerken en verwijderen van operatorgroepen:

| Type request | Eindpunt                                                           | Gebruik                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | `/OperatorGroup`                                                   | Verkrijgt alle operatorgroepen.                                     |
| GET          | `/OperatorGroup/{operatorGroupGuid}`                               | Verkrijgt de details van een operatorgroep.                        |
| POST         | `/OperatorGroup`                                                   | Creëert een nieuwe operatorgroep.                                 |
| PUT          | `/OperatorGroup/{operatorGroupGuid}`                               | Werkt een bestaande operatorgroep bij.                           |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}`                               | Verwijdert een bestaande operatorgroep.                           |
| GET          | `/OperatorGroup/{operatorGroupGuid}/Member`                        | Verkrijgt de geen-dienstperiodes voor een bestaande operator.             |
| POST         | `/OperatorGroup/{operatorGroupGuid}/DutySchedule`                  | Voegt een geen-dienstperiode toe aan alle operators in de gespecificeerde groep. |
| PUT          | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Werkt de gespecificeerde geen-dienstperiode bij.                          |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Verwijdert de gespecificeerde geen-dienstperiode.                          |

#### GET OperatorGroup

Deze GET request retourneert een verzameling die alle operatorgroepen bevat, inclusief de speciale systeemgroepen.                          |

```json
[
    {
        "OperatorGroupGuid": "8ceeddfc-acd0-4afb-9cd5-9400ea9d0d49",
        "Description": "Administrators",
        "IsEveryone": false,
        "IsAdministratorsGroup": true
    },
    {
        "OperatorGroupGuid": "983c3592-be7f-47ac-b53f-da856c841e57",
        "Description": "Everyone",
        "IsEveryone": true,
        "IsAdministratorsGroup": false
    },
    {
        "OperatorGroupGuid": "82f4171a-16c3-4bc6-ab4d-56edee7fd6c8",
        "Description": "Main operators",
        "IsEveryone": false,
        "IsAdministratorsGroup": false
    }
]
```

#### GET OperatorGroup/{operatorGroupGuid}

Deze GET request retourneert de details van de specifieke operatorgroep die wordt geïdentificeerd door de gespecificeerde operatorgroep-GUID.

Voorbeeld uitvoer:

```json
{
    "OperatorGroupGuid": "27ef4bcf-92bb-4a84-8786-d91b7ceb0b99",
    "Description": "Everyone",
    "IsEveryone": true,
    "IsAdministratorsGroup": false
}
```

#### POST OperatorGroup

Hiermee wordt een nieuwe operatorgroep gemaakt met de verstrekte gegevens.

Voorbeeld invoer:

```json
{
    "Description": "Example Operator Group"
} 
```

De response bevat de gecreëerde operatorgroep, inclusief de operator-GUID die is toegewezen:

```json
{
    "OperatorGroupGuid": "2c4abb71-4c40-4f57-bd3d-672c08c4ad82",
    "Description": "Example Operator Group"
} 
```


#### DELETE OperatorGroup/{operatorGroupGuid}

Deze methode verwijdert de operatorgroep die wordt geïdentificeerd door de gespecificeerde operator-GUID met behulp van de in de request verstrekte data.
