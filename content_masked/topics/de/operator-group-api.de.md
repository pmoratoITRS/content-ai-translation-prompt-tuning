{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operator-Gruppen.",
  "url": "[URL_BASE_TOPICS]api/operator-group-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Operator-Gruppen. Operator-Gruppen dienen der Organisation von Operatoren (Nutzer-Accounts) in deinem Account. Diese API bietet Methoden zur Verwaltung jeder Gruppe sowie zum Hinzufügen/Entfernen von Operatoren zu/von einer Gruppe.

## Operator-Gruppen-Objekte

Die folgenden OperatorGroup-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                   | Beschreibung                                                 | Datentyp |
|------------------------|-------------------------------------------------------------|-----------|
| [INLINE_CODE_1]    | Die einzigartige Kennung dieser Operator-Gruppe              | Guid      |
| [INLINE_CODE_2]          | Eine Zeichenfolge mit einem beschreibenden Namen                     | String    |
| [INLINE_CODE_3]           | Zeigt an, ob dies die Systemgruppe „Jeder“ ist      | Boolean   |
| [INLINE_CODE_4] | Zeigt an, ob dies die Systemgruppe „Administratoren“ ist | Boolean   |

Die Gruppe „Jeder“ ist eine automatisch vom System erstellte Gruppe. Die Gruppe „Jeder“ kann nicht geändert werden: Jeder Operator wird automatisch zu dieser Gruppe hinzugefügt.

"Administratoren" ist ebenfalls eine vom System erstellte Gruppe, aber du kannst einzelne Operatoren hinzufügen oder entfernen. Wenn ein Operator zur Gruppe "Administratoren" hinzugefügt wird, verfügt dieser Operator automatisch über alle Administratorrechte.

## OperatorGroup-Endpunkte

Die folgenden API-Endpunkte sind zum Abruf, Erstellen, Ändern und Entfernen von Operator-Gruppen verfügbar.

| Anfragetyp | Endpunkt                                                           | Einsatz                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | [INLINE_CODE_5]                                                   | Ruft alle Operator-Gruppen ab                                     |
| GET          | [INLINE_CODE_6]                               | Ruft Informationen zu einer Operator-Gruppe ab                        |
| POST         | [INLINE_CODE_7]                                                   | Erstellt eine neue Operator-Gruppe                                 |
| PUT          | [INLINE_CODE_8]                               | Aktualisiert eine bestehende Operator-Gruppe                           |
| DELETE       | [INLINE_CODE_9]                               | Löscht eine bestehende Operator-Gruppe                           |
| GET          | [INLINE_CODE_10]                        | Ruft den Dienstplan eines bestehenden Operators ab             |
| POST         | [INLINE_CODE_11]                  | Fügt einen Dienstplan für alle Operatoren in der angegebenen Gruppe hinzu |
| PUT          | [INLINE_CODE_12] | Aktualisiert den angegebenen Dienstplan                          |
| DELETE       | [INLINE_CODE_13] | Löscht den angegebenen Dienstplan                          |

#### GET OperatorGroup

Diese GET-Anfrage ergibt eine Sammlung mit allen Operator-Gruppen, einschließlich der besonderen System-Gruppen.

[CODE_BLOCK_1]

#### GET OperatorGroup/{operatorGroupGuid}

Diese GET-Anfrage ergibt die Informationen für die durch die Operator-Gruppen GUID spezifizierte Operator-Gruppe.

Beispiel-Ausgabe:

[CODE_BLOCK_2]

#### POST OperatorGroup

Diese Eingabe dient der Erstellung einer neuen Operator-Gruppe mit den bereitgestellten Informationen.

Beispiel-Eingabe:

[CODE_BLOCK_3]

Die Antwort enthält die erstellte Operator-Gruppe, einschließlich der zugewiesenen Operator-Gruppen GUID:

[CODE_BLOCK_4]


#### DELETE OperatorGroup/{operatorGroupGuid}

Diese Methode löscht die durch die Operator-Gruppen GUID spezifizierte Operator-Gruppe mit den Daten, die in der Anfrage übermittelt werden.
