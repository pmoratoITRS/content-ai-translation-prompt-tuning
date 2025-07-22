{
"hero": {
"title": "Commande Operator Group de l'API"
},
"title": "Commande Operator Group de l'API",
"summary": "Présentation des méthodes de la commande d'API permettant de manipuler les groupes d'opérateurs.",
"url": "/support/kb/api/api-du-groupe-operateurs",
"translationKey": "https://www.uptrends.com/support/kb/api/operator-group-api"
}

Cette page décrit les méthodes de la commande d'API permettant de manipuler des groupes d'opérateurs. Les groupes d'opérateurs servent à organiser les opérateurs (comptes d'utilisateur) dans votre compte. Cette commande de l'API fournit des méthodes pour gérer chaque groupe, et pour ajouter des opérateurs au groupe ou pour en supprimer.

## Description de l'objet OperatorGroup

L'objet OperatorGroup suivant est utilisé dans les méthodes de la commande d'API décrites ci-dessous :

| Nom | Description | Type de données |
|------------------------|-------------------------------------------------------------|-----------|
| `OperatorGroupGuid` | Identifiant unique pour ce groupe d'opérateurs | Guid |
| `Description` | Chaîne contenant un nom descriptif | Chaîne |
| `IsEveryone` | Indique s'il s'agit du groupe système "Everyone" | Booléen |
| `IsAdministratorGroup` | Indique s'il s'agit du groupe système "Administrators" | Booléen |

Le groupe "Everyone" (Tout le monde) est un groupe créé automatiquement par le système. Ce groupe ne peut pas être modifié : chaque opérateur est automatiquement ajouté à ce groupe.

Le groupe "Administrators" (Administrateurs) est également un groupe créé par le système, mais vous pouvez y ajouter des opérateurs individuels ou les supprimer. Lorsqu'un opérateur est ajouté en tant que membre du groupe Administrators, tous les privilèges d'administration lui sont automatiquement attribués.

## Endpoints pour la commande d'API OperatorGroup

Les endpoints API suivants sont disponibles pour l'extraction, la création, la mise à jour et la suppression de groupes d'opérateurs :

| Type de requête | Endpoint | Utilisation |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET | `/OperatorGroup` | Obtenir tous les groupes d'opérateurs. |
| GET | `/OperatorGroup/{operatorGroupGuid}` | Obtenir les détails d'un groupe d'opérateurs |
| POST | `/OperatorGroup` | Créer un nouveau groupe d'opérateurs |
| PUT | `/OperatorGroup/{operatorGroupGuid}` | Mettre à jour un groupe d'opérateurs |
| DELETE | `/OperatorGroup/{operatorGroupGuid}` | Supprimer un groupe d'opérateurs |
| GET | `/OperatorGroup/{operatorGroupGuid}/Member` | Obtenir les horaires de repos d'un opérateur |
| POST | `/OperatorGroup/{operatorGroupGuid}/DutySchedule` | Ajouter un horaire de repos à tous les opérateurs du groupe spécifié |
| PUT | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Mettre à jour l'horaire de repos spécifié |
| DELETE | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Supprimer l'horaire de repos spécifié |

#### GET OperatorGroup

Cette requête GET renvoie une collection contenant tous les groupes d'opérateurs, y compris les groupes système spéciaux.

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

Cette requête GET renvoie les détails du groupe d'opérateurs identifié par le GUID du groupe d'opérateurs spécifié.

Exemple de sortie :

```json
{
    "OperatorGroupGuid": "27ef4bcf-92bb-4a84-8786-d91b7ceb0b99",
    "Description": "Everyone",
    "IsEveryone": true,
    "IsAdministratorsGroup": false
}
```

#### POST OperatorGroup

Cette méthode crée un nouveau groupe d'opérateurs avec les détails fournis.

Exemple d'entrée :

```json
{
    "Description": "Example Operator Group"
} 
```

La réponse contient le groupe d'opérateurs créé, y compris le GUID attribué :

```json
{
    "OperatorGroupGuid": "2c4abb71-4c40-4f57-bd3d-672c08c4ad82",
    "Description": "Example Operator Group"
} 
```


#### DELETE OperatorGroup/{operatorGroupGuid}

Cette méthode supprime le groupe d'opérateurs identifié par le GUID de l'opérateur spécifié, à l'aide des données fournies dans la demande.
