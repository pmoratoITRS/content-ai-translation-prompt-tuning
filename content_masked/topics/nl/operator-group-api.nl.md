{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "De beschikbare API-methodes voor het manipuleren van operatorgroepen.",
  "url": "[URL_BASE_TOPICS]api/operator-group-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Op deze pagina worden de beschikbare API-methodes voor het manipuleren van operatorgroepen beschreven. Operatorgroepen worden gebruikt om de operators (gebruikersaccounts) in uw account te organiseren. Deze API leverde methoden voor het beheren van elke groep en voor het toevoegen/verwijderen van operators aan/uit een groep.

## Objectbeschrijving operatorgroep

Het volgende OperatorGroup-object wordt gebruikt in de hieronder beschreven API-methodes:

| Naam                   | Beschrijving                                                 | Datatype |
|------------------------|-------------------------------------------------------------|-----------|
| [INLINE_CODE_1]    | De unieke ID van deze operatorgroep.              | Guid      |
| [INLINE_CODE_2]          | Een string die een beschrijvende naam bevat.                     | String    |
| [INLINE_CODE_3]           | Geeft aan of dit de systeemgroep “Iedereen” is.      | Boolean   |
| [INLINE_CODE_4] | Geeft aan of dit de systeemgroep “Administrators” is. | Boolean   |

De groep “Iedereen” is een automatische, door het systeem gecreëerde groep. De groep Iedereen kan niet worden gewijzigd: elke operator wordt automatisch aan deze groep toegevoegd.

De “Administrators” is ook een door het systeem gecreëerde groep, maar u kunt individuele operators aan deze groep toevoegen of ze er weer uit verwijderen. Wanneer een operator wordt toegevoegd als lid van de groep Administrators, worden alle administratorrechten automatisch toegewezen aan die operator.

## Eindpunten OperatorGroup

De volgende API-eindpunten zijn beschikbaar voor het ophalen, maken, bijwerken en verwijderen van operatorgroepen:

| Type request | Eindpunt                                                           | Gebruik                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | [INLINE_CODE_5]                                                   | Verkrijgt alle operatorgroepen.                                     |
| GET          | [INLINE_CODE_6]                               | Verkrijgt de details van een operatorgroep.                        |
| POST         | [INLINE_CODE_7]                                                   | Creëert een nieuwe operatorgroep.                                 |
| PUT          | [INLINE_CODE_8]                               | Werkt een bestaande operatorgroep bij.                           |
| DELETE       | [INLINE_CODE_9]                               | Verwijdert een bestaande operatorgroep.                           |
| GET          | [INLINE_CODE_10]                        | Verkrijgt de geen-dienstperiodes voor een bestaande operator.             |
| POST         | [INLINE_CODE_11]                  | Voegt een geen-dienstperiode toe aan alle operators in de gespecificeerde groep. |
| PUT          | [INLINE_CODE_12] | Werkt de gespecificeerde geen-dienstperiode bij.                          |
| DELETE       | [INLINE_CODE_13] | Verwijdert de gespecificeerde geen-dienstperiode.                          |

#### GET OperatorGroup

Deze GET request retourneert een verzameling die alle operatorgroepen bevat, inclusief de speciale systeemgroepen.                          |

[CODE_BLOCK_1]

#### GET OperatorGroup/{operatorGroupGuid}

Deze GET request retourneert de details van de specifieke operatorgroep die wordt geïdentificeerd door de gespecificeerde operatorgroep-GUID.

Voorbeeld uitvoer:

[CODE_BLOCK_2]

#### POST OperatorGroup

Hiermee wordt een nieuwe operatorgroep gemaakt met de verstrekte gegevens.

Voorbeeld invoer:

[CODE_BLOCK_3]

De response bevat de gecreëerde operatorgroep, inclusief de operator-GUID die is toegewezen:

[CODE_BLOCK_4]


#### DELETE OperatorGroup/{operatorGroupGuid}

Deze methode verwijdert de operatorgroep die wordt geïdentificeerd door de gespecificeerde operator-GUID met behulp van de in de request verstrekte data.
