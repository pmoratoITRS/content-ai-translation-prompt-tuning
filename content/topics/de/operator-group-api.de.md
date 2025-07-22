{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operator-Gruppen.",
  "url": "/support/kb/api/operator-group-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-group-api"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Operator-Gruppen. Operator-Gruppen dienen der Organisation von Operatoren (Nutzer-Accounts) in deinem Account. Diese API bietet Methoden zur Verwaltung jeder Gruppe sowie zum Hinzufügen/Entfernen von Operatoren zu/von einer Gruppe.

## Operator-Gruppen-Objekte

Die folgenden OperatorGroup-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                   | Beschreibung                                                 | Datentyp |
|------------------------|-------------------------------------------------------------|-----------|
| `OperatorGroupGuid`    | Die einzigartige Kennung dieser Operator-Gruppe              | Guid      |
| `Description`          | Eine Zeichenfolge mit einem beschreibenden Namen                     | String    |
| `IsEveryone`           | Zeigt an, ob dies die Systemgruppe „Jeder“ ist      | Boolean   |
| `IsAdministratorGroup` | Zeigt an, ob dies die Systemgruppe „Administratoren“ ist | Boolean   |

Die Gruppe „Jeder“ ist eine automatisch vom System erstellte Gruppe. Die Gruppe „Jeder“ kann nicht geändert werden: Jeder Operator wird automatisch zu dieser Gruppe hinzugefügt.

"Administratoren" ist ebenfalls eine vom System erstellte Gruppe, aber du kannst einzelne Operatoren hinzufügen oder entfernen. Wenn ein Operator zur Gruppe "Administratoren" hinzugefügt wird, verfügt dieser Operator automatisch über alle Administratorrechte.

## OperatorGroup-Endpunkte

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Operator-Gruppen verfügbar.

| Anfragetyp | Endpunkt                                                           | Einsatz                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | `/OperatorGroup`                                                   | Ruft alle Operator-Gruppen ab                                     |
| GET          | `/OperatorGroup/{operatorGroupGuid}`                               | Ruft Informationen zu einer Operator-Gruppe ab                        |
| POST         | `/OperatorGroup`                                                   | Erstellt eine neue Operator-Gruppe                                 |
| PUT          | `/OperatorGroup/{operatorGroupGuid}`                               | Aktualisiert eine bestehende Operator-Gruppe                           |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}`                               | Löscht eine bestehende Operator-Gruppe                           |
| GET          | `/OperatorGroup/{operatorGroupGuid}/Member`                        | Ruft den Dienstplan eines bestehenden Operators ab             |
| POST         | `/OperatorGroup/{operatorGroupGuid}/DutySchedule`                  | Fügt einen Dienstplan für alle Operatoren in der angegebenen Gruppe hinzu |
| PUT          | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Aktualisiert den angegebenen Dienstplan                          |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Löscht den angegebenen Dienstplan                          |

#### GET OperatorGroup

Diese GET-Anfrage ergibt eine Sammlung mit allen Operator-Gruppen, einschließlich der besonderen System-Gruppen.

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

Diese GET-Anfrage ergibt die Informationen für die durch die Operator-Gruppen GUID spezifizierte Operator-Gruppe.

Beispiel-Ausgabe:

```json
{
    "OperatorGroupGuid": "27ef4bcf-92bb-4a84-8786-d91b7ceb0b99",
    "Description": "Everyone",
    "IsEveryone": true,
    "IsAdministratorsGroup": false
}
```

#### POST OperatorGroup

Diese Eingabe dient der Erstellung einer neuen Operator-Gruppe mit den bereitgestellten Informationen.

Beispiel-Eingabe:

```json
{
    "Description": "Example Operator Group"
} 
```

Die Antwort enthält die erstellte Operator-Gruppe, einschließlich der zugewiesenen Operator-Gruppen GUID:

```json
{
    "OperatorGroupGuid": "2c4abb71-4c40-4f57-bd3d-672c08c4ad82",
    "Description": "Example Operator Group"
} 
```


#### DELETE OperatorGroup/{operatorGroupGuid}

Diese Methode löscht die durch die Operator-Gruppen GUID spezifizierte Operator-Gruppe mit den Daten, die in der Anfrage übermittelt werden.
